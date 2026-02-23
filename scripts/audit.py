#!/usr/bin/env python3
"""OpenEM Corpus Automated Validation Suite (13-pass audit).

Implements all automated validation passes:
  1. Cross-file dosing consistency enforcement
  2. Unit normalization check
  3. Dose-range anomaly detection
  4. Citation presence and formatting validation
  5. Duplicate / near-duplicate detection
  6. High-risk medication tagging
  7. ICD-10 format validation
  8. Guideline currency flagging
  9. Content completeness (gate severity)
  10. Source currency (informational)
  11. Pediatric dose coverage (informational)
  12. International terminology (informational)
  13. Cross-reference completeness (informational)

Output: JSON report to stdout. Exit 0 always (flags issues, never blocks build).
"""

import json
import re
import sys
import yaml
from collections import defaultdict
from pathlib import Path
from datetime import date

REPO_ROOT = Path(__file__).resolve().parent.parent
CONDITIONS_DIR = REPO_ROOT / "corpus" / "tier1" / "conditions"
TODAY = date.today().isoformat()

# --- Drug reference data for cross-file consistency ---
# Canonical doses: {drug_name: {indication: expected_dose_pattern}}
CANONICAL_DOSES = {
    "epinephrine": {
        "cardiac_arrest": "1 mg IV",
        "anaphylaxis": "0.3 mg IM",
        "infusion": "0.01-0.5 mcg/kg/min",
    },
    "norepinephrine": {
        "vasopressor": "0.05-0.5 mcg/kg/min",
    },
    "vasopressin": {
        "adjunct_vasopressor": "0.03 units/min",
    },
    "calcium_gluconate": {
        "hyperkalemia": "3 g IV",
        "massive_transfusion": "3 g IV",
    },
    "vancomycin": {
        "loading": "25-30 mg/kg IV",
        "maintenance": "15-20 mg/kg IV",
        "monitoring": "AUC/MIC 400-600",
    },
    "piperacillin_tazobactam": {
        "standard": "4.5 g IV q6h",
    },
    "amiodarone": {
        "vfib_pvt": "300 mg IV",
        "infusion": "150 mg IV over 10 min",
    },
    "atropine": {
        "bradycardia": "1 mg IV q3-5min",
        "organophosphate": "2-5 mg IV q3-5min",
    },
}

# Standard dose units for normalization check
STANDARD_UNITS = [
    r"\d+\.?\d*\s*mg/kg",
    r"\d+\.?\d*\s*mcg/kg/min",
    r"\d+\.?\d*\s*mg\b",
    r"\d+\.?\d*\s*mcg\b",
    r"\d+\.?\d*\s*g\b",
    r"\d+\.?\d*\s*mL\b",
    r"\d+\.?\d*\s*units?\b",
    r"\d+\.?\d*\s*mEq\b",
    r"\d+\.?\d*\s*mg PE/kg",
    r"\d+\.?\d*\s*mcg/min",
]

# High-risk medication categories
HIGH_RISK_MEDS = {
    "vasopressors": ["norepinephrine", "epinephrine", "vasopressin", "phenylephrine", "dopamine"],
    "antiarrhythmics": ["amiodarone", "lidocaine", "procainamide", "adenosine"],
    "anticoagulants": ["heparin", "enoxaparin", "warfarin", "tpa", "alteplase", "tenecteplase"],
    "rsi_agents": ["succinylcholine", "rocuronium", "etomidate", "ketamine", "propofol"],
    "insulin": ["insulin"],
    "tox_antidotes": ["naloxone", "flumazenil", "fomepizole", "pyridoxine", "atropine", "pralidoxime",
                      "digifab", "n-acetylcysteine", "hydroxocobalamin", "glucagon"],
    "obstetric": ["oxytocin", "methylergonovine", "carboprost", "misoprostol", "magnesium sulfate"],
    "pediatric_critical": ["prostaglandin", "surfactant", "dextrose"],
}

# ICD-10-CM code format (basic validation)
ICD10_PATTERN = re.compile(r"^[A-TV-Z]\d{2}(\.[A-Z0-9]{1,4})?$")

# Known outdated guidelines (guideline string fragment -> note)
OUTDATED_GUIDELINES = {
    "2010 AHA": "2020 AHA guidelines available",
    "2012 AHA": "2020 AHA guidelines available",
    "2012 ESC": "newer ESC guidelines available",
    "ACLS 2010": "2020 ACLS guidelines available",
    "2008 IDSA": "check for updated IDSA guidelines",
}


def extract_frontmatter(text: str) -> dict | None:
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return None
    return yaml.safe_load(m.group(1))


def get_body(text: str) -> str:
    m = re.match(r"^---\n.*?\n---\n?(.*)", text, re.DOTALL)
    return m.group(1) if m else text


def load_all_conditions() -> list[dict]:
    """Load all condition files: returns list of {path, fm, body}."""
    results = []
    for f in sorted(CONDITIONS_DIR.glob("*.md")):
        text = f.read_text()
        fm = extract_frontmatter(text)
        body = get_body(text)
        if fm:
            results.append({"path": str(f), "name": f.stem, "fm": fm, "body": body, "text": text})
    return results


# === Pass 1: Cross-file dosing consistency ===
def check_cross_file_dosing(conditions: list[dict]) -> list[dict]:
    """Find drug dose mentions and flag inconsistencies across files."""
    findings = []
    drug_doses = defaultdict(list)

    dose_pattern = re.compile(
        r"(epinephrine|norepinephrine|vasopressin|calcium gluconate|calcium chloride|"
        r"vancomycin|piperacillin-tazobactam|amiodarone|atropine|rocuronium|"
        r"fosphenytoin|phenytoin|lorazepam|midazolam|diazepam|ketamine|propofol|"
        r"fentanyl|morphine|ketorolac|mannitol|furosemide|hydrocortisone|"
        r"dexamethasone|ceftriaxone|cefepime|meropenem|metoprolol|labetalol|"
        r"nicardipine|diltiazem|magnesium sulfate|sodium bicarbonate|"
        r"tranexamic acid|heparin|alteplase|tenecteplase)\s+"
        r"(\d+[\d.,\-/]*\s*(?:mg|mcg|g|units?|mEq|mL)[\w/]*(?:\s*(?:IV|IM|IO|SQ|SL|PO|PR|IN|ET|q\d+[hm]?))*)",
        re.IGNORECASE
    )

    for c in conditions:
        for match in dose_pattern.finditer(c["body"]):
            drug = match.group(1).lower().strip()
            dose = match.group(2).strip()
            drug_doses[drug].append({
                "file": c["name"],
                "dose": dose,
                "context": c["body"][max(0, match.start()-40):match.end()+40].replace("\n", " ").strip()
            })

    # Flag drugs with multiple distinct dose strings (potential inconsistencies)
    for drug, mentions in drug_doses.items():
        unique_doses = set(m["dose"] for m in mentions)
        if len(unique_doses) > 3:  # More than 3 distinct dose strings warrants review
            findings.append({
                "check": "cross_file_dosing",
                "drug": drug,
                "severity": "info",
                "unique_dose_count": len(unique_doses),
                "files": list(set(m["file"] for m in mentions)),
                "doses": list(unique_doses)[:10],
            })

    return findings


# === Pass 2: Unit normalization ===
def check_unit_normalization(conditions: list[dict]) -> list[dict]:
    """Flag non-standard unit formats."""
    findings = []

    # Non-standard patterns to flag
    bad_patterns = [
        (r"\d+\s*ug\b", "Use 'mcg' not 'ug'"),
        (r"\d+\s*cc\b", "Use 'mL' not 'cc'"),
        (r"\d+\s*gm\b", "Use 'g' not 'gm'"),
        (r"\d+\s*gms\b", "Use 'g' not 'gms'"),
        (r"\d+\s*mgm\b", "Use 'mg' not 'mgm'"),
        (r"\d+\s*liter\b", "Use 'L' not 'liter'"),
        (r"\d+\s*liters\b", "Use 'L' not 'liters'"),
        (r"\d+\s*mcg/kg/hour\b", "Use 'mcg/kg/min' or 'mcg/kg/hr'"),
        (r"\bmicrogram", "Use 'mcg' abbreviation"),
        (r"\bmilligram", "Use 'mg' abbreviation"),
    ]

    for c in conditions:
        for pat, msg in bad_patterns:
            matches = list(re.finditer(pat, c["body"], re.IGNORECASE))
            if matches:
                findings.append({
                    "check": "unit_normalization",
                    "file": c["name"],
                    "severity": "warning",
                    "message": msg,
                    "count": len(matches),
                    "examples": [m.group() for m in matches[:3]],
                })

    return findings


# === Pass 3: Dose-range anomaly detection ===
def check_dose_range_anomalies(conditions: list[dict]) -> list[dict]:
    """Flag doses that fall outside expected ranges."""
    findings = []

    # Known safe ranges: (drug_pattern, max_single_dose_mg, context)
    dose_limits = [
        (r"epinephrine\s+(\d+\.?\d*)\s*mg\s*(?:IV|IO)", 1.0, "epinephrine IV single dose"),
        (r"epinephrine\s+(\d+\.?\d*)\s*mg\s*IM", 0.5, "epinephrine IM single dose"),
        (r"atropine\s+(\d+\.?\d*)\s*mg", 5.0, "atropine single dose"),
        (r"lorazepam\s+(\d+\.?\d*)\s*mg", 8.0, "lorazepam single dose"),
        (r"midazolam\s+(\d+\.?\d*)\s*mg", 10.0, "midazolam single dose"),
        (r"amiodarone\s+(\d+\.?\d*)\s*mg", 450.0, "amiodarone single dose"),
        (r"adenosine\s+(\d+\.?\d*)\s*mg", 18.0, "adenosine single dose"),
        (r"naloxone\s+(\d+\.?\d*)\s*mg", 10.0, "naloxone single dose"),
        (r"ondansetron\s+(\d+\.?\d*)\s*mg", 16.0, "ondansetron single dose"),
        (r"ketorolac\s+(\d+\.?\d*)\s*mg", 60.0, "ketorolac single dose"),
    ]

    for c in conditions:
        for pat, max_dose, label in dose_limits:
            for m in re.finditer(pat, c["body"], re.IGNORECASE):
                try:
                    dose_val = float(m.group(1))
                    if dose_val > max_dose:
                        findings.append({
                            "check": "dose_range_anomaly",
                            "file": c["name"],
                            "severity": "critical",
                            "message": f"{label}: {dose_val} mg exceeds max {max_dose} mg",
                            "match": m.group(),
                        })
                except (ValueError, IndexError):
                    pass

    return findings


# === Pass 4: Citation presence and formatting ===
def check_citations(conditions: list[dict]) -> list[dict]:
    findings = []

    for c in conditions:
        fm = c["fm"]
        sources = fm.get("sources", [])

        if not sources:
            findings.append({
                "check": "citation_presence",
                "file": c["name"],
                "severity": "critical",
                "message": "No sources listed",
            })
            continue

        for i, src in enumerate(sources):
            if "type" not in src:
                findings.append({
                    "check": "citation_format",
                    "file": c["name"],
                    "severity": "warning",
                    "message": f"source[{i}] missing 'type'",
                })
            if "ref" not in src:
                findings.append({
                    "check": "citation_format",
                    "file": c["name"],
                    "severity": "warning",
                    "message": f"source[{i}] missing 'ref'",
                })

            # Validate PMID format (digits only)
            if "pmid" in src and src["pmid"]:
                if not re.match(r"^\d+$", str(src["pmid"])):
                    findings.append({
                        "check": "citation_format",
                        "file": c["name"],
                        "severity": "warning",
                        "message": f"source[{i}] invalid PMID format: '{src['pmid']}'",
                    })

            # Validate DOI format
            if "doi" in src and src["doi"]:
                if not re.match(r"^10\.\d{4,}", str(src["doi"])):
                    findings.append({
                        "check": "citation_format",
                        "file": c["name"],
                        "severity": "warning",
                        "message": f"source[{i}] invalid DOI format: '{src['doi']}'",
                    })

        # Check pubmed sources have PMIDs
        pubmed_sources = [s for s in sources if s.get("type") == "pubmed"]
        for i, src in enumerate(pubmed_sources):
            if "pmid" not in src:
                findings.append({
                    "check": "citation_format",
                    "file": c["name"],
                    "severity": "info",
                    "message": f"pubmed source missing PMID: {src.get('ref', '?')[:60]}",
                })

    return findings


# === Pass 5: Duplicate / near-duplicate detection ===
def check_duplicates(conditions: list[dict]) -> list[dict]:
    """Check for near-duplicate paragraphs across files."""
    findings = []

    # Extract paragraphs (>50 chars) from each file
    file_paragraphs = {}
    for c in conditions:
        paras = [p.strip() for p in c["body"].split("\n\n") if len(p.strip()) > 80]
        file_paragraphs[c["name"]] = paras

    # Compare paragraphs across files (using first 100 chars as signature)
    sig_map = defaultdict(list)
    for fname, paras in file_paragraphs.items():
        for p in paras:
            # Normalize whitespace for comparison
            sig = re.sub(r"\s+", " ", p[:100]).lower()
            sig_map[sig].append(fname)

    for sig, files in sig_map.items():
        unique_files = list(set(files))
        if len(unique_files) > 1:
            findings.append({
                "check": "duplicate_content",
                "severity": "info",
                "message": f"Near-duplicate paragraph across {len(unique_files)} files",
                "files": unique_files,
                "signature": sig[:80],
            })

    return findings


# === Pass 6: High-risk medication tagging ===
def check_high_risk_meds(conditions: list[dict]) -> list[dict]:
    """Tag files containing high-risk medications."""
    findings = []

    for c in conditions:
        body_lower = c["body"].lower()
        file_tags = set()

        for category, drugs in HIGH_RISK_MEDS.items():
            for drug in drugs:
                if drug in body_lower:
                    file_tags.add(category)
                    break

        if file_tags:
            findings.append({
                "check": "high_risk_med_tagging",
                "file": c["name"],
                "severity": "info",
                "risk_tier": c["fm"].get("risk_tier", "?"),
                "high_risk_categories": sorted(file_tags),
            })

    return findings


# === Pass 7: ICD-10 format validation ===
def check_icd10(conditions: list[dict]) -> list[dict]:
    findings = []

    for c in conditions:
        codes = c["fm"].get("icd10", [])
        if not codes:
            findings.append({
                "check": "icd10_validation",
                "file": c["name"],
                "severity": "critical",
                "message": "No ICD-10 codes listed",
            })
            continue

        for code in codes:
            if not ICD10_PATTERN.match(str(code)):
                findings.append({
                    "check": "icd10_validation",
                    "file": c["name"],
                    "severity": "warning",
                    "message": f"Invalid ICD-10-CM format: '{code}'",
                })

    return findings


# === Pass 8: Guideline currency flagging ===
def check_guideline_currency(conditions: list[dict]) -> list[dict]:
    findings = []

    for c in conditions:
        sources = c["fm"].get("sources", [])
        for src in sources:
            ref = src.get("ref", "")
            for fragment, note in OUTDATED_GUIDELINES.items():
                if fragment in ref:
                    findings.append({
                        "check": "guideline_currency",
                        "file": c["name"],
                        "severity": "info",
                        "message": f"Potentially outdated: '{ref[:80]}' — {note}",
                    })

    return findings


# === Pass 9: Content completeness ===
REQUIRED_CONTENT_SECTIONS = [
    "Recognition",
    "Critical Actions",
    "Differential Diagnosis",
    "Workup",
    "Treatment",
    "Disposition",
    "Pitfalls",
]

def check_content_completeness(conditions: list[dict]) -> list[dict]:
    """Check that all required sections are present and substantive (>= 50 chars)."""
    findings = []

    for c in conditions:
        body = c["body"]
        for section in REQUIRED_CONTENT_SECTIONS:
            # Match the section header (## Section or ## Section ...)
            pattern = re.compile(
                r"##\s+" + re.escape(section) + r"[^\n]*\n(.*?)(?=\n##\s|\Z)",
                re.DOTALL | re.IGNORECASE,
            )
            m = pattern.search(body)
            if not m:
                findings.append({
                    "check": "content_completeness",
                    "file": c["name"],
                    "severity": "critical",
                    "section": section,
                    "message": f"Section '## {section}' missing entirely",
                })
            else:
                section_content = m.group(1).strip()
                # Strip markdown formatting noise for length measurement
                cleaned = re.sub(r"[#*`|_\-\[\]]+", " ", section_content)
                cleaned = re.sub(r"\s+", " ", cleaned).strip()
                if len(cleaned) < 50:
                    findings.append({
                        "check": "content_completeness",
                        "file": c["name"],
                        "severity": "critical",
                        "section": section,
                        "message": (
                            f"Section '## {section}' has < 50 chars of content "
                            f"(found {len(cleaned)} chars after stripping headers)"
                        ),
                    })

    return findings


# === Pass 10: Source currency ===
_YEAR_RE = re.compile(r"\b(19|20)\d{2}\b")

def check_source_currency(conditions: list[dict]) -> list[dict]:
    """Flag conditions where no source year is >= 2021 (all sources older than 5 years)."""
    findings = []

    for c in conditions:
        sources = c["fm"].get("sources", [])
        if not sources:
            continue  # covered by Pass 4

        years = []
        for src in sources:
            ref = src.get("ref", "")
            for m in _YEAR_RE.finditer(ref):
                years.append(int(m.group()))

        if not years:
            findings.append({
                "check": "source_currency",
                "file": c["name"],
                "severity": "info",
                "message": "No 4-digit years found in any source ref — cannot assess currency",
            })
            continue

        mean_year = sum(years) / len(years)
        max_year = max(years)

        if max_year < 2021:
            findings.append({
                "check": "source_currency",
                "file": c["name"],
                "severity": "info",
                "message": (
                    f"All sources older than 5 years (newest: {max_year}, "
                    f"mean: {mean_year:.1f}). Review for updated guidelines."
                ),
                "max_year": max_year,
                "mean_year": round(mean_year, 1),
                "years_found": sorted(set(years)),
            })

    return findings


# === Pass 11: Pediatric dose coverage ===
_PEDS_MENTION_RE = re.compile(
    r"\b(pediatric|child(?:ren)?|neonatal|neonate|infant)\b", re.IGNORECASE
)
_PEDS_DOSE_RE = re.compile(
    r"\b(mg/kg|pediatric\s+dose|child\s+dose|neonatal\s+dose|per\s+kg)\b",
    re.IGNORECASE,
)

def check_pediatric_doses(conditions: list[dict]) -> list[dict]:
    """Flag conditions mentioning pediatric populations without pediatric dosing."""
    findings = []

    for c in conditions:
        body = c["body"]
        has_peds_mention = bool(_PEDS_MENTION_RE.search(body))
        if not has_peds_mention:
            continue

        has_peds_dose = bool(_PEDS_DOSE_RE.search(body))
        if not has_peds_dose:
            # Count how many mentions to gauge depth of pediatric coverage
            mention_count = len(_PEDS_MENTION_RE.findall(body))
            findings.append({
                "check": "pediatric_dose_coverage",
                "file": c["name"],
                "severity": "info",
                "message": (
                    f"Pediatric population mentioned ({mention_count} times) "
                    "but no pediatric dosing found (mg/kg, pediatric dose, neonatal dose, etc.)"
                ),
                "mention_count": mention_count,
            })

    return findings


# === Pass 12: International terminology ===
_INTL_TERMS = {
    "A&E": r"\bA&E\b",
    "999": r"\b999\b",
    "112": r"\b112\b",
    "NHS": r"\bNHS\b",
    "NICE": r"\bNICE\b",
    "BNF": r"\bBNF\b",
    "SIGN": r"\bSIGN\b",
    "RCPCH": r"\bRCPCH\b",
}

def check_international_terminology(conditions: list[dict]) -> list[dict]:
    """Count UK/international terminology mentions per file (informational)."""
    findings = []

    for c in conditions:
        body = c["body"]
        matches_found = {}
        for term, pattern in _INTL_TERMS.items():
            hits = re.findall(pattern, body)
            if hits:
                matches_found[term] = len(hits)

        if matches_found:
            total = sum(matches_found.values())
            findings.append({
                "check": "international_terminology",
                "file": c["name"],
                "severity": "info",
                "message": (
                    f"Contains {total} international/UK terminology reference(s): "
                    + ", ".join(f"{t}({n})" for t, n in sorted(matches_found.items()))
                ),
                "term_counts": matches_found,
                "total_count": total,
            })

    return findings


# === Pass 13: Cross-reference completeness ===
_CAPITALIZED_PHRASE_RE = re.compile(
    r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)\b"
)
# Terms to exclude — common medical/anatomical capitalized phrases that aren't conditions
_XREF_EXCLUDE = frozenset([
    "Emergency Department", "Emergency Medicine", "Intensive Care Unit",
    "Critical Care", "Intensive Care", "Emergency Room", "Operating Room",
    "Emergency Medical", "United States", "World Health", "American Heart",
    "American College", "European Society", "Surviving Sepsis",
    "Clinical Practice", "Evidence Based", "Systematic Review",
    "Case Report", "Randomized Controlled", "Meta Analysis",
])

def check_cross_references(conditions: list[dict]) -> list[dict]:
    """Check that conditions referenced in Differential Diagnosis sections have corpus files."""
    findings = []

    # Build set of known condition filenames (stems)
    known_stems = {Path(c["path"]).stem for c in conditions}

    for c in conditions:
        body = c["body"]

        # Extract Differential Diagnosis section
        ddx_match = re.search(
            r"##\s+Differential\s+Diagnosis[^\n]*\n(.*?)(?=\n##\s|\Z)",
            body,
            re.DOTALL | re.IGNORECASE,
        )
        if not ddx_match:
            continue

        ddx_text = ddx_match.group(1)

        # Find capitalized multi-word phrases (candidate condition names)
        candidates = set()
        for m in _CAPITALIZED_PHRASE_RE.finditer(ddx_text):
            phrase = m.group(1)
            if phrase not in _XREF_EXCLUDE and len(phrase) >= 6:
                candidates.add(phrase)

        if not candidates:
            continue

        # Check which candidates don't have a corresponding corpus file
        # Normalize: lowercase, replace spaces with hyphens
        missing = []
        for phrase in sorted(candidates):
            slug = re.sub(r"\s+", "-", phrase.lower())
            # Try exact match and common abbreviation patterns
            if slug not in known_stems:
                # Also try removing trailing -s, -syndrome, -disease (common normalization)
                slug_trunc = re.sub(r"-(syndrome|disease|disorder|injury|failure)$", "", slug)
                if slug_trunc not in known_stems:
                    missing.append(phrase)

        if missing:
            findings.append({
                "check": "cross_reference_completeness",
                "file": c["name"],
                "severity": "info",
                "message": (
                    f"{len(missing)} DDx reference(s) have no corresponding corpus file"
                ),
                "missing_files": missing[:10],  # cap output at 10
            })

    return findings


# === Main runner ===
def main():
    conditions = load_all_conditions()
    print(f"Loaded {len(conditions)} conditions", file=sys.stderr)

    report = {
        "date": TODAY,
        "file_count": len(conditions),
        "passes": {},
    }

    # Run all 13 passes
    passes = [
        ("cross_file_dosing", check_cross_file_dosing),
        ("unit_normalization", check_unit_normalization),
        ("dose_range_anomaly", check_dose_range_anomalies),
        ("citation_validation", check_citations),
        ("duplicate_detection", check_duplicates),
        ("high_risk_med_tagging", check_high_risk_meds),
        ("icd10_validation", check_icd10),
        ("guideline_currency", check_guideline_currency),
        ("content_completeness", check_content_completeness),
        ("source_currency", check_source_currency),
        ("pediatric_dose_coverage", check_pediatric_doses),
        ("international_terminology", check_international_terminology),
        ("cross_reference_completeness", check_cross_references),
    ]

    total_findings = 0
    critical_count = 0

    for name, fn in passes:
        findings = fn(conditions)
        report["passes"][name] = {
            "finding_count": len(findings),
            "findings": findings,
        }
        total_findings += len(findings)
        critical_count += sum(1 for f in findings if f.get("severity") == "critical")
        print(f"  {name}: {len(findings)} findings", file=sys.stderr)

    report["total_findings"] = total_findings
    report["critical_findings"] = critical_count

    print(json.dumps(report, indent=2))
    print(f"\nTotal: {total_findings} findings ({critical_count} critical)", file=sys.stderr)

    # Always exit 0 — audit flags but does not block
    return 0


if __name__ == "__main__":
    sys.exit(main())
