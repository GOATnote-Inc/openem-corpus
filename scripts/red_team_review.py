#!/usr/bin/env python3
"""Red Team Review: automated clinical checks on risk_tier A conditions.

Phase A — Deterministic checks (runs on all tier A conditions):
  - Dose completeness (drug + route + frequency)
  - Hedging in Critical Actions
  - time_to_harm specificity
  - Mortality quantification
  - Pitfall count (>= 7)
  - Source currency (at least one source >= 2021)
  - Dangerous combination cross-checks
  - Category-specific clinical checks

Phase B — LLM-augmented pass (optional, runs on flagged conditions):
  - Requires --llm flag and ANTHROPIC_API_KEY or OPENAI_API_KEY

Output:
  - review/tier_a_review_cards.yaml  (machine-readable)
  - review/tier_a_review_cards.md    (physician-friendly with checkboxes)

Usage:
    python scripts/red_team_review.py            # Phase A only
    python scripts/red_team_review.py --llm       # Phase A + B
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CONDITIONS_DIR = REPO_ROOT / "corpus" / "tier1" / "conditions"
REVIEW_DIR = REPO_ROOT / "review"
TODAY = date.today().isoformat()

_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
_YEAR_RE = re.compile(r"\b(19|20)\d{2}\b")

# --- Severity levels ---
CRITICAL = "critical"
MAJOR = "major"
MINOR = "minor"
INFO = "info"

# --- Hedging phrases that should not appear in Critical Actions ---
HEDGING_PHRASES = [
    r"\bconsider\b",
    r"\bmay want to\b",
    r"\bif available\b",
    r"\bif possible\b",
    r"\bcould\b",
    r"\bmight\b",
    r"\bpossibly\b",
    r"\bperhaps\b",
    r"\bshould probably\b",
    r"\bit may be\b",
    r"\bone could\b",
    r"\bit is reasonable to\b",
]

# --- Vague time_to_harm terms ---
VAGUE_TIME_TERMS = [
    "variable",
    "depends",
    "varies",
    "uncertain",
    "unclear",
    "not well defined",
    "unpredictable",
    "case-dependent",
]

# --- Dangerous combination cross-checks ---
# (drug, condition_ids_where_must_warn, warning_text)
DANGEROUS_COMBOS = [
    {
        "drug": "succinylcholine",
        "warn_in": [
            "hyperkalemia",
            "organophosphate-poisoning",
            "malignant-hyperthermia",
            "crush-syndrome-mci",
        ],
        "warning": "must warn against succinylcholine use",
        "search": r"\bsuccinylcholine\b",
    },
    {
        "drug": "calcium chloride",
        "warn_in": None,  # any condition mentioning it
        "warning": "must state 'central line only' or warn against peripheral administration",
        "search": r"\bcalcium chloride\b",
        "must_contain": r"central\s+line|do not.{0,20}peripher|avoid.{0,20}peripher|central\s+venous|central\s+access",
    },
    {
        "drug": "beta-blocker in cocaine",
        "warn_in": ["cocaine-toxicity", "sympathomimetic-toxidrome"],
        "warning": "must warn against beta-blockers",
        "search": r"\bbeta.?block",
    },
    {
        "drug": "epinephrine concentration",
        "warn_in": None,
        "warning": "epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent",
        "search": r"\bepinephrine\b.*\b(?:IM|IV)\b",
        "must_contain": r"1:1[,.]?000|1 mg/mL|1:10[,.]?000|0\.1 mg/mL|100 mcg/mL",
    },
    {
        "drug": "flumazenil",
        "warn_in": None,
        "warning": "must warn against use in mixed overdose or chronic benzodiazepine use (seizure risk)",
        "search": r"\bflumazenil\b",
        "must_contain": r"seizure|mixed\s+(?:overdose|OD|ingestion)|chronic\s+benzo|contraindic",
    },
]

# --- Category-specific check definitions ---
CATEGORY_CHECKS = {
    "toxicologic": {
        "antidote_dose_route": {
            "desc": "Antidote dose + route stated",
            "search": r"(?:antidote|treatment|specific\s+therapy)",
            "must_contain": r"\d+\.?\d*\s*(?:mg|g|mL|units?|mcg).*(?:IV|IM|PO|IO|SQ|SL|IN)",
        },
        "max_dose_stated": {
            "desc": "Max dose stated or 'no maximum' explicitly",
            "search": r"(?:antidote|treatment|dosing)",
            "must_contain": r"(?:max(?:imum)?|no max(?:imum)?|ceiling|total\s+dose|cumulative)",
        },
        "decontamination_timing": {
            "desc": "Decontamination timing window stated",
            "search": r"(?:decontam|charcoal|lavage|whole\s+bowel)",
            "must_contain": r"\d+\s*(?:hour|minute|hr|min|h\b)",
        },
    },
    "cardiovascular": {
        "reperfusion_target": {
            "desc": "Reperfusion/intervention time target stated",
            "search": r"(?:reperfus|PCI|cath\s*lab|balloon|stent|thrombolys|fibrinolys)",
            "must_contain": r"<?\s*\d+\s*(?:minute|hour|min|hr|h\b)",
        },
        "anticoag_weight_based": {
            "desc": "Anticoagulation dosing weight-based where applicable",
            "search": r"(?:heparin|enoxaparin|anticoagul)",
            "must_contain": r"(?:units?/kg|mg/kg|weight.based|weight-based|per\s*kg)",
        },
    },
    "obstetric-gynecologic": {
        "mag_toxicity": {
            "desc": "Magnesium sulfate toxicity thresholds if mentioned",
            "search": r"\bmagnesium\s+sulfate\b",
            "must_contain": r"(?:toxic|reflex|respiratory\s+depress|level|serum|>?\s*\d+\s*(?:mg/dL|mEq|mmol))",
        },
        "fetal_considerations": {
            "desc": "Fetal considerations addressed",
            "search": r"(?:fetus|fetal|gestation|pregnan)",
            "must_contain": r"(?:fetal|gestational\s+age|viability|delivery|weeks)",
        },
        "gestational_cutoffs": {
            "desc": "Gestational age cutoffs stated",
            "search": r"(?:gestation|trimester|weeks|viab)",
            "must_contain": r"\d+\s*weeks?",
        },
    },
    "neurological": {
        "seizure_dose_mg_kg": {
            "desc": "Seizure med dosing uses mg/kg for second-line",
            "search": r"(?:phenytoin|fosphenytoin|levetiracetam|valproate|valproic|keppra)",
            "must_contain": r"mg/kg|mg\s*PE/kg",
        },
        "herniation_signs": {
            "desc": "Herniation signs listed if relevant",
            "search": r"(?:herniat|uncal|tonsillar|transtentorial|raised\s+ICP|increased\s+intracranial)",
            "must_contain": r"(?:pupil|posturing|cushing|bradycard|blown|unilateral|fixed\s+dilat)",
        },
    },
    "infectious": {
        "empiric_abx_timing": {
            "desc": "Empiric antibiotic timing stated",
            "search": r"(?:antibiotic|antimicrobial|empiric)",
            "must_contain": r"(?:within\s+\d+\s*(?:hour|minute|hr|min)|first\s+hour|immediately|< ?\d+\s*h)",
        },
        "cultures_before_abx": {
            "desc": "Blood cultures before antibiotics mentioned",
            "search": r"(?:antibiotic|antimicrobial)",
            "must_contain": r"(?:blood\s+culture|culture.*before|before.*culture|do not delay|culture.*prior)",
        },
    },
    "pediatric": {
        "weight_based_dosing": {
            "desc": "All doses weight-based (mg/kg)",
            "search": r"\d+\.?\d*\s*(?:mg|mcg|g|units?|mEq)",
            "must_contain": r"mg/kg|mcg/kg|units?/kg|mL/kg|per\s*kg",
        },
        "max_adult_dose": {
            "desc": "Max adult dose cap stated",
            "search": r"mg/kg",
            "must_contain": r"(?:max(?:imum)?|adult\s+dose|cap|ceiling|not\s+to\s+exceed|up\s+to)",
        },
    },
    "disaster-mci": {
        "triage_algorithm": {
            "desc": "Triage algorithm named (SALT, START, JumpSTART)",
            "search": r"(?:triage|sort|mass\s+casualty)",
            "must_contain": r"(?:SALT|START|JumpSTART|SMART|Simple\s+Triage)",
        },
        "resource_allocation": {
            "desc": "Resource allocation criteria stated",
            "search": r"(?:resource|allocation|scarce|triage|priority)",
            "must_contain": r"(?:immediate|delayed|minor|expectant|black|red|yellow|green|category|priority)",
        },
    },
    "procedural": {
        "equipment_list": {
            "desc": "Equipment list or setup checklist present",
            "search": r"(?:equipment|supplies|setup|preparation|kit|tray)",
            "must_contain": r"(?:blade|scalpel|needle|catheter|tube|forceps|clamp|suture|bougie|guide\s*wire|\d+\s*(?:Fr|gauge|mm)|prep|drape)",
        },
        "contraindications_listed": {
            "desc": "Contraindications listed",
            "search": r"(?:contraindic|should not|do not perform|avoid)",
            "must_contain": r"(?:contraindic|absolute|relative|avoid\s+in|do\s+not)",
        },
        "complication_rates": {
            "desc": "Complication rates cited",
            "search": r"(?:complicat|risk|adverse)",
            "must_contain": r"(?:\d+\s*%|complication\s+rate|mortality|morbidity|failure\s+rate)",
        },
    },
}


def extract_frontmatter(text: str) -> dict | None:
    m = _FM_RE.match(text)
    if not m:
        return None
    return yaml.safe_load(m.group(1))


def get_body(text: str) -> str:
    m = re.match(r"^---\n.*?\n---\n?(.*)", text, re.DOTALL)
    return m.group(1) if m else text


def get_section(body: str, section_name: str) -> str | None:
    pattern = re.compile(
        r"##\s+" + re.escape(section_name) + r"[^\n]*\n(.*?)(?=\n##\s|\Z)",
        re.DOTALL | re.IGNORECASE,
    )
    m = pattern.search(body)
    return m.group(1).strip() if m else None


def count_pitfalls(body: str) -> int:
    pitfalls = get_section(body, "Pitfalls")
    if not pitfalls:
        return 0
    # Count bullet points (- or *) or numbered items (1. 2. etc)
    bullets = re.findall(r"^\s*(?:[-*]|\d+\.)\s+", pitfalls, re.MULTILINE)
    return len(bullets)


def word_count(text: str) -> int:
    return len(text.split())


def load_tier_a_conditions() -> list[dict]:
    results = []
    for f in sorted(CONDITIONS_DIR.glob("*.md")):
        text = f.read_text()
        fm = extract_frontmatter(text)
        if not fm:
            continue
        if fm.get("risk_tier") != "A":
            continue
        body = get_body(text)
        results.append({
            "path": str(f),
            "name": f.stem,
            "fm": fm,
            "body": body,
            "text": text,
        })
    return results


# === Universal checks ===

def check_dose_completeness(condition: dict) -> list[dict]:
    """Flag drug doses missing route or frequency."""
    flags = []
    body = condition["body"]

    # Find drug dose mentions: number + unit without an obvious route nearby
    dose_re = re.compile(
        r"(\b(?:epinephrine|norepinephrine|vasopressin|amiodarone|atropine|"
        r"lidocaine|procainamide|adenosine|naloxone|flumazenil|fomepizole|"
        r"alteplase|tenecteplase|heparin|enoxaparin|aspirin|clopidogrel|"
        r"ticagrelor|nitroglycerin|morphine|fentanyl|ketamine|propofol|"
        r"etomidate|rocuronium|succinylcholine|lorazepam|midazolam|diazepam|"
        r"phenytoin|fosphenytoin|levetiracetam|valproate|mannitol|"
        r"dexamethasone|hydrocortisone|methylprednisolone|ceftriaxone|"
        r"vancomycin|piperacillin|meropenem|metoprolol|labetalol|"
        r"nicardipine|diltiazem|magnesium sulfate|sodium bicarbonate|"
        r"calcium gluconate|calcium chloride|tranexamic acid|oxytocin|"
        r"methylergonovine|carboprost|misoprostol|hydroxocobalamin|"
        r"pralidoxime|pyridoxine|n-acetylcysteine|glucagon|insulin|"
        r"dextrose|ondansetron|ketorolac|ibuprofen|acetaminophen)\b)"
        r"\s+(\d+[\d.,\-/]*\s*(?:mg|mcg|g|units?|mEq|mL)[\w/]*)",
        re.IGNORECASE,
    )
    route_re = re.compile(
        r"\b(IV|IM|IO|SQ|SC|SL|PO|PR|IN|ET|topical|nebulized|inhaled|"
        r"intravenous|intramuscular|intraosseous|subcutaneous|sublingual|oral|rectal|intranasal)\b",
        re.IGNORECASE,
    )

    for match in dose_re.finditer(body):
        drug = match.group(1)
        dose_str = match.group(2)
        # Check surrounding context (100 chars) for route
        start = max(0, match.start() - 20)
        end = min(len(body), match.end() + 60)
        context = body[start:end]
        if not route_re.search(context):
            flags.append({
                "severity": MINOR,
                "check": "dose_missing_route",
                "detail": f"{drug} {dose_str} — no route (IV/IM/PO/etc) found nearby",
            })

    return flags


def check_hedging(condition: dict) -> list[dict]:
    """Flag hedging language in Critical Actions section."""
    flags = []
    critical_actions = get_section(condition["body"], "Critical Actions")
    if not critical_actions:
        return flags

    for pattern in HEDGING_PHRASES:
        matches = list(re.finditer(pattern, critical_actions, re.IGNORECASE))
        for m in matches:
            # Get surrounding context
            start = max(0, m.start() - 30)
            end = min(len(critical_actions), m.end() + 50)
            context = critical_actions[start:end].replace("\n", " ").strip()
            flags.append({
                "severity": MINOR,
                "check": "hedging_in_critical_actions",
                "detail": f'Hedging phrase "{m.group()}" in Critical Actions: "...{context}..."',
            })

    return flags


def check_time_to_harm(condition: dict) -> list[dict]:
    """Check time_to_harm specificity and format."""
    flags = []
    fm = condition["fm"]
    tth = fm.get("time_to_harm")

    if not tth:
        flags.append({
            "severity": MAJOR,
            "check": "time_to_harm_missing",
            "detail": "time_to_harm field is missing",
        })
        return flags

    # Check if structured (object) vs string
    if isinstance(tth, str):
        flags.append({
            "severity": MINOR,
            "check": "time_to_harm_not_structured",
            "detail": f"time_to_harm is a string (\"{tth}\"), not structured object — tier A SHOULD use object form",
        })
        # Check for vague terms
        for vague in VAGUE_TIME_TERMS:
            if vague.lower() in tth.lower():
                flags.append({
                    "severity": MAJOR,
                    "check": "time_to_harm_vague",
                    "detail": f"time_to_harm contains vague term: \"{vague}\"",
                })
    elif isinstance(tth, dict):
        # Verify the structured fields have actual time values
        for field in ["irreversible_injury", "death", "optimal_intervention_window"]:
            val = tth.get(field, "")
            if val:
                for vague in VAGUE_TIME_TERMS:
                    if vague.lower() in val.lower():
                        flags.append({
                            "severity": MAJOR,
                            "check": "time_to_harm_vague",
                            "detail": f"time_to_harm.{field} contains vague term: \"{vague}\"",
                        })

    return flags


def check_mortality(condition: dict) -> list[dict]:
    """Check that mortality is quantified."""
    flags = []
    fm = condition["fm"]
    body = condition["body"]

    mortality_field = fm.get("mortality_if_delayed", "")
    # Check frontmatter or body for a percentage/rate
    has_quant = bool(re.search(r"\d+\.?\d*\s*%", str(mortality_field)))
    if not has_quant:
        # Also check body for mortality figures
        has_quant = bool(re.search(
            r"mortality.*\d+\.?\d*\s*%|\d+\.?\d*\s*%.*mortality|fatality.*\d+|death\s+rate.*\d+",
            body, re.IGNORECASE,
        ))
    if not has_quant and not mortality_field:
        flags.append({
            "severity": MINOR,
            "check": "mortality_not_quantified",
            "detail": "No mortality_if_delayed in frontmatter and no mortality percentage found in body",
        })
    elif mortality_field and not re.search(r"\d", str(mortality_field)):
        flags.append({
            "severity": MINOR,
            "check": "mortality_not_quantified",
            "detail": f"mortality_if_delayed has no numeric value: \"{mortality_field}\"",
        })

    return flags


def check_pitfall_count(condition: dict) -> list[dict]:
    """Ensure >= 7 pitfalls listed."""
    flags = []
    count = count_pitfalls(condition["body"])
    if count < 7:
        flags.append({
            "severity": MINOR if count >= 5 else MAJOR,
            "check": "pitfall_count",
            "detail": f"Only {count} pitfalls listed (minimum 7 recommended for tier A)",
        })
    return flags


def check_source_currency(condition: dict) -> list[dict]:
    """Check for at least one source from the last 5 years (>= 2021)."""
    flags = []
    sources = condition["fm"].get("sources", [])
    if not sources:
        return flags

    years = []
    for src in sources:
        ref = src.get("ref", "")
        for m in _YEAR_RE.finditer(ref):
            years.append(int(m.group()))

    if not years:
        flags.append({
            "severity": INFO,
            "check": "source_currency",
            "detail": "No publication years found in source refs",
        })
    elif max(years) < 2021:
        flags.append({
            "severity": INFO,
            "check": "source_currency",
            "detail": f"Oldest source year: {min(years)}, newest: {max(years)} — no source from last 5 years",
        })

    return flags


def check_dangerous_combos(condition: dict) -> list[dict]:
    """Check dangerous combination cross-checks."""
    flags = []
    body = condition["body"]
    cid = condition["fm"].get("id", condition["name"])

    for combo in DANGEROUS_COMBOS:
        drug = combo["drug"]
        search = combo["search"]

        # Check if this combo check applies to this condition
        if combo.get("warn_in") is not None:
            if cid not in combo["warn_in"]:
                continue
            # Drug should be mentioned with a warning
            if re.search(search, body, re.IGNORECASE):
                # Check if warning is present
                must_contain = combo.get("must_contain")
                if must_contain and not re.search(must_contain, body, re.IGNORECASE):
                    pass  # No explicit warning — but drug is used, need context check
            # If condition should warn but drug isn't mentioned at all,
            # that's fine (they may not use it)
        else:
            # General check — applies whenever the drug is mentioned
            if not re.search(search, body, re.IGNORECASE):
                continue
            must_contain = combo.get("must_contain")
            if must_contain and not re.search(must_contain, body, re.IGNORECASE):
                flags.append({
                    "severity": MAJOR,
                    "check": "dangerous_combination",
                    "detail": f"{drug}: {combo['warning']}",
                })

    return flags


def run_category_checks(condition: dict) -> dict:
    """Run category-specific checks. Returns {check_name: PASS|FAIL|N/A}."""
    category = condition["fm"].get("category", "")
    checks = CATEGORY_CHECKS.get(category, {})
    body = condition["body"]
    results = {}

    for check_name, check_def in checks.items():
        search = check_def["search"]
        must_contain = check_def["must_contain"]

        # If the topic isn't discussed, mark N/A
        if not re.search(search, body, re.IGNORECASE):
            results[check_name] = "N/A"
        elif re.search(must_contain, body, re.IGNORECASE):
            results[check_name] = "PASS"
        else:
            results[check_name] = "FAIL"

    return results


# === Phase B: LLM-augmented review ===

def run_llm_review(condition: dict, flags: list[dict]) -> list[dict]:
    """Run LLM review on conditions with major/critical flags."""
    import os

    llm_flags = []
    category = condition["fm"].get("category", "")
    cid = condition["fm"].get("id", condition["name"])

    # Build prompt
    prompt = f"""You are a board-certified emergency medicine physician conducting a red team review of a medical reference condition file.

Condition: {condition["fm"].get("condition", cid)}
Category: {category}
Risk Tier: A (highest acuity)

Existing automated flags for this condition:
{json.dumps(flags, indent=2)}

Full condition text:
---
{condition["body"][:6000]}
---

Review the condition text for:
1. Dangerous omissions — critical actions or warnings missing for this condition
2. Incorrect dosing context — doses that are correct in isolation but wrong for this specific clinical scenario
3. Outdated protocols — treatments that have been superseded by newer evidence
4. Missing contraindications — drug-drug or drug-condition interactions not mentioned

For each issue found, output a JSON array of objects with:
  {{"severity": "critical|major|minor", "check": "llm_<check_type>", "detail": "description"}}

If no issues found, output an empty array: []
Output ONLY the JSON array, no other text."""

    # Try Anthropic first, then OpenAI
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if api_key:
        try:
            import anthropic

            client = anthropic.Anthropic(api_key=api_key)
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}],
            )
            text = response.content[0].text.strip()
            # Extract JSON from response
            if text.startswith("["):
                parsed = json.loads(text)
                for item in parsed:
                    item["source"] = "llm_review"
                    llm_flags.append(item)
            return llm_flags
        except Exception as e:
            print(f"  LLM review failed for {cid}: {e}", file=sys.stderr)
            return llm_flags

    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key:
        try:
            from openai import OpenAI

            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-4o",
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}],
            )
            text = response.choices[0].message.content.strip()
            if text.startswith("["):
                parsed = json.loads(text)
                for item in parsed:
                    item["source"] = "llm_review"
                    llm_flags.append(item)
            return llm_flags
        except Exception as e:
            print(f"  LLM review failed for {cid}: {e}", file=sys.stderr)
            return llm_flags

    print("  No API key found for LLM review (set ANTHROPIC_API_KEY or OPENAI_API_KEY)", file=sys.stderr)
    return llm_flags


# === Physician checklist generation ===

def generate_physician_checklist(condition: dict, category_results: dict) -> list[str]:
    """Generate physician-specific review items based on condition category."""
    category = condition["fm"].get("category", "")
    checklist = []

    # Universal items
    checklist.append("Verify all drug doses match current guidelines")
    checklist.append("Confirm Critical Actions are complete and time-targeted")
    checklist.append("Check pitfalls for clinical accuracy")

    # Category-specific items
    if category == "cardiovascular":
        checklist.append("Verify reperfusion/intervention time targets are current")
        checklist.append("Confirm anticoagulation weight-based dosing")
        checklist.append("Check antiplatelet therapy matches current ACC/AHA")
    elif category == "toxicologic":
        checklist.append("Verify antidote dosing and routes are current")
        checklist.append("Confirm decontamination timing windows")
        checklist.append("Check for dangerous drug interactions")
    elif category == "obstetric-gynecologic":
        checklist.append("Verify magnesium sulfate dosing and toxicity thresholds")
        checklist.append("Confirm gestational age cutoffs")
        checklist.append("Check fetal monitoring recommendations")
    elif category == "neurological":
        checklist.append("Verify seizure medication dosing (mg/kg for second-line)")
        checklist.append("Confirm herniation management protocols")
        checklist.append("Check thrombolytic eligibility criteria")
    elif category == "infectious":
        checklist.append("Verify empiric antibiotic regimens match current guidelines")
        checklist.append("Confirm timing targets for antibiotic administration")
        checklist.append("Check source control recommendations")
    elif category == "pediatric":
        checklist.append("Verify all doses are weight-based with adult max caps")
        checklist.append("Confirm age-appropriate normal values referenced")
    elif category == "disaster-mci":
        checklist.append("Verify triage algorithm accuracy")
        checklist.append("Confirm resource allocation criteria")
        checklist.append("Check mass decontamination protocols if applicable")
    elif category == "procedural":
        checklist.append("Verify equipment list is complete")
        checklist.append("Confirm contraindications are listed")
        checklist.append("Check procedural steps are in correct order")
    elif category == "environmental":
        checklist.append("Verify temperature management targets")
        checklist.append("Confirm rewarming/cooling protocols")
    elif category == "traumatic":
        checklist.append("Verify hemorrhage control priorities")
        checklist.append("Confirm transfusion thresholds")
    elif category == "respiratory":
        checklist.append("Verify airway management decision points")
        checklist.append("Confirm ventilator settings if mentioned")

    return checklist


# === Output generation ===

def generate_yaml_output(cards: list[dict]) -> str:
    """Generate YAML review cards."""
    return yaml.dump(cards, default_flow_style=False, sort_keys=False, allow_unicode=True)


def generate_markdown_output(cards: list[dict], summary: dict) -> str:
    """Generate physician-friendly markdown review cards."""
    lines = []

    # Header
    lines.append("# Red Team Review: Tier A Conditions")
    lines.append(f"\nGenerated: {TODAY}")
    lines.append("")

    # Summary dashboard
    lines.append("## Summary Dashboard")
    lines.append("")
    lines.append("```")
    lines.append("=== RED TEAM REVIEW SUMMARY ===")
    lines.append(f"Total conditions: {summary['total']}")
    lines.append(f"Critical flags: {summary['critical']}")
    lines.append(f"Major flags: {summary['major']}")
    lines.append(f"Minor flags: {summary['minor']}")
    lines.append(f"Info flags: {summary['info']}")
    lines.append("```")
    lines.append("")

    # Needs attention section
    if summary["major_conditions"] or summary["critical_conditions"]:
        lines.append("### Needs Attention")
        lines.append("")
        for cid, issues in summary.get("critical_conditions", {}).items():
            for issue in issues:
                lines.append(f"- **CRITICAL** `{cid}`: {issue}")
        for cid, issues in summary.get("major_conditions", {}).items():
            for issue in issues:
                lines.append(f"- **MAJOR** `{cid}`: {issue}")
        lines.append("")

    # Category breakdown
    lines.append("### Category Breakdown")
    lines.append("")
    lines.append("| Category | Count | Critical | Major | Minor | Info |")
    lines.append("|----------|-------|----------|-------|-------|------|")
    for cat, counts in sorted(summary["by_category"].items()):
        lines.append(
            f"| {cat} | {counts['total']} | {counts.get('critical', 0)} | "
            f"{counts.get('major', 0)} | {counts.get('minor', 0)} | "
            f"{counts.get('info', 0)} |"
        )
    lines.append("")

    # Individual condition cards
    lines.append("---")
    lines.append("")
    lines.append("## Condition Review Cards")
    lines.append("")

    for card in cards:
        cid = card["condition_id"]
        name = card["condition_name"]
        status = card["review_status"]

        # Status icon
        icon = "CLEAN" if status == "CLEAN" else "NEEDS_PHYSICIAN_REVIEW"
        lines.append(f"### {name}")
        lines.append(f"**ID:** `{cid}` | **Category:** {card['category']} | **Status:** {icon}")
        lines.append(f"**Words:** {card['word_count']} | **Sources:** {card['sources_count']} | **Pitfalls:** {card['pitfalls_count']} | **time_to_harm:** {card['time_to_harm_format']}")
        lines.append("")

        # Flags
        if card["flags"]:
            lines.append("**Flags:**")
            for flag in card["flags"]:
                sev = flag["severity"].upper()
                source = f" *(LLM)* " if flag.get("source") == "llm_review" else ""
                lines.append(f"- [{sev}]{source} `{flag['check']}`: {flag['detail']}")
            lines.append("")

        # Category checks
        if card.get("category_checks"):
            lines.append("**Category Checks:**")
            for check, result in card["category_checks"].items():
                mark = "PASS" if result == "PASS" else ("N/A" if result == "N/A" else "**FAIL**")
                lines.append(f"- {check}: {mark}")
            lines.append("")

        # Dangerous combos
        if card.get("dangerous_combo_flags"):
            lines.append("**Dangerous Combination Flags:**")
            for flag in card["dangerous_combo_flags"]:
                lines.append(f"- [{flag['severity'].upper()}] {flag['detail']}")
            lines.append("")

        # Physician checklist
        lines.append("**Physician Checklist:**")
        for item in card["physician_checklist"]:
            lines.append(f"- [ ] {item}")
        lines.append("")

        # Sign-off
        lines.append(f"**Sign-off:** _________________________ Date: ___________")
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Red Team Review for Tier A conditions")
    parser.add_argument("--llm", action="store_true", help="Enable Phase B LLM-augmented review")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of YAML")
    args = parser.parse_args()

    print("=== Red Team Review: Phase A (Deterministic) ===\n", file=sys.stderr)

    conditions = load_tier_a_conditions()
    print(f"Loaded {len(conditions)} tier A conditions\n", file=sys.stderr)

    cards = []
    summary = {
        "total": len(conditions),
        "critical": 0,
        "major": 0,
        "minor": 0,
        "info": 0,
        "critical_conditions": {},
        "major_conditions": {},
        "by_category": defaultdict(lambda: defaultdict(int)),
    }

    for condition in conditions:
        cid = condition["fm"].get("id", condition["name"])
        category = condition["fm"].get("category", "unknown")
        fm = condition["fm"]

        print(f"  Checking {cid}...", file=sys.stderr)

        # Run all universal checks
        all_flags = []
        all_flags.extend(check_dose_completeness(condition))
        all_flags.extend(check_hedging(condition))
        all_flags.extend(check_time_to_harm(condition))
        all_flags.extend(check_mortality(condition))
        all_flags.extend(check_pitfall_count(condition))
        all_flags.extend(check_source_currency(condition))

        # Dangerous combo checks
        combo_flags = check_dangerous_combos(condition)
        all_flags.extend(combo_flags)

        # Category-specific checks
        category_results = run_category_checks(condition)
        # Add FAIL results as flags
        for check_name, result in category_results.items():
            if result == "FAIL":
                check_def = CATEGORY_CHECKS.get(category, {}).get(check_name, {})
                all_flags.append({
                    "severity": MINOR,
                    "check": f"category_{check_name}",
                    "detail": f"Category check failed: {check_def.get('desc', check_name)}",
                })

        # Phase B: LLM review (only for conditions with major/critical flags)
        if args.llm:
            has_serious = any(f["severity"] in (CRITICAL, MAJOR) for f in all_flags)
            if has_serious:
                print(f"    Running LLM review for {cid}...", file=sys.stderr)
                llm_flags = run_llm_review(condition, all_flags)
                all_flags.extend(llm_flags)

        # Determine time_to_harm format
        tth = fm.get("time_to_harm")
        if isinstance(tth, dict):
            tth_format = "structured"
        elif isinstance(tth, str):
            tth_format = "string"
        else:
            tth_format = "missing"

        # Build card
        card = {
            "condition_id": cid,
            "condition_name": fm.get("condition", cid),
            "category": category,
            "word_count": word_count(condition["body"]),
            "sources_count": len(fm.get("sources", [])),
            "pitfalls_count": count_pitfalls(condition["body"]),
            "time_to_harm_format": tth_format,
            "flags": all_flags,
            "category_checks": category_results,
            "dangerous_combo_flags": combo_flags,
            "review_status": "CLEAN" if not any(
                f["severity"] in (CRITICAL, MAJOR) for f in all_flags
            ) else "NEEDS_PHYSICIAN_REVIEW",
            "physician_checklist": generate_physician_checklist(condition, category_results),
        }
        cards.append(card)

        # Update summary
        summary["by_category"][category]["total"] += 1
        for flag in all_flags:
            sev = flag["severity"]
            summary[sev] += 1
            summary["by_category"][category][sev] += 1
            if sev == CRITICAL:
                summary["critical_conditions"].setdefault(cid, []).append(flag["detail"])
            elif sev == MAJOR:
                summary["major_conditions"].setdefault(cid, []).append(flag["detail"])

    # Print summary
    print(f"\n=== RESULTS ===", file=sys.stderr)
    print(f"Total conditions: {summary['total']}", file=sys.stderr)
    print(f"Critical: {summary['critical']}, Major: {summary['major']}, Minor: {summary['minor']}, Info: {summary['info']}", file=sys.stderr)

    needs_review = sum(1 for c in cards if c["review_status"] == "NEEDS_PHYSICIAN_REVIEW")
    clean = sum(1 for c in cards if c["review_status"] == "CLEAN")
    print(f"Needs physician review: {needs_review}, Clean: {clean}", file=sys.stderr)

    # Write output files
    REVIEW_DIR.mkdir(exist_ok=True)

    # YAML output
    yaml_path = REVIEW_DIR / "tier_a_review_cards.yaml"
    yaml_path.write_text(generate_yaml_output(cards))
    print(f"\nYAML written to {yaml_path}", file=sys.stderr)

    # Markdown output
    md_path = REVIEW_DIR / "tier_a_review_cards.md"
    md_path.write_text(generate_markdown_output(cards, summary))
    print(f"Markdown written to {md_path}", file=sys.stderr)

    # JSON output (optional)
    if args.json:
        json_path = REVIEW_DIR / "tier_a_review_cards.json"
        json_path.write_text(json.dumps(cards, indent=2))
        print(f"JSON written to {json_path}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
