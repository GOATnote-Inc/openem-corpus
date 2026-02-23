#!/usr/bin/env python3
"""Compute corpus diversity and coverage metrics.

Output: JSON report to stdout with entropy, balance, and coverage scores.

Metrics:
  1. Category entropy — Shannon entropy across 18 categories
  2. ESI balance — Gini coefficient across ESI 1-5
  3. Risk tier x category matrix — flag zero cells
  4. Demographic representation — elderly, pediatric, pregnant, immunocompromised, obese
  5. Geographic representation — UK/WHO/international vs US-only
  6. Temporal drift — citation recency vs known guideline milestones
"""

import json
import math
import re
import sys
import yaml
from collections import Counter, defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONDITIONS_DIR = REPO_ROOT / "corpus" / "tier1" / "conditions"

# Canonical category list from validate.py
VALID_CATEGORIES = [
    "cardiovascular",
    "neurological",
    "respiratory",
    "gastrointestinal",
    "genitourinary",
    "obstetric-gynecologic",
    "endocrine-metabolic",
    "infectious",
    "musculoskeletal",
    "hematologic",
    "toxicologic",
    "traumatic",
    "environmental",
    "psychiatric",
    "pediatric",
    "ophthalmologic",
    "dermatologic",
    "allergic-immunologic",
]

VALID_RISK_TIERS = ["A", "B", "C"]

# Demographic keyword patterns
DEMOGRAPHIC_PATTERNS = {
    "elderly_geriatric": re.compile(
        r"\b(elderly|geriatric|older\s+adult|aged?\s+patient|nursing\s+home|age[d\s]+>\s*6[05])\b",
        re.IGNORECASE,
    ),
    "pediatric_child": re.compile(
        r"\b(pediatric|child(?:ren)?|neonatal|neonate|infant|adolescent|newborn)\b",
        re.IGNORECASE,
    ),
    "pregnant_obstetric": re.compile(
        r"\b(pregnant|pregnancy|obstetric|peripartum|postpartum|gravid|trimester|antepartum)\b",
        re.IGNORECASE,
    ),
    "immunocompromised": re.compile(
        r"\b(immunocompromised|immunosuppressed|neutropenic|hiv|transplant\s+patient|"
        r"chemotherapy|biologics?\s+user|steroid.dependent)\b",
        re.IGNORECASE,
    ),
    "obese": re.compile(
        r"\b(obese|obesity|morbidly\s+obese|bmi\s*[>≥]\s*3[05]|bariatric)\b",
        re.IGNORECASE,
    ),
}

# Geographic / guideline provenance patterns
INTL_PATTERNS = re.compile(
    r"\b(A&E|NHS|NICE|BNF|SIGN|RCPCH|WHO|PHEIC|999\b|112\b|ERC|ESC|ESVS|ESICM|"
    r"international\s+guidelines?|global\s+guidelines?)\b",
    re.IGNORECASE,
)
US_PATTERNS = re.compile(
    r"\b(ACLS|AHA|ACC|ACEP|IDSA|CDC|FDA|CMS|911\b|EMS|911|"
    r"american\s+(?:heart|college|academy|association))\b",
    re.IGNORECASE,
)

# Guideline milestone dates for temporal drift
GUIDELINE_MILESTONES = {
    "AHA_ACLS_2020": {
        "description": "AHA ACLS 2020 guidelines",
        "cutoff_year": 2020,
        "pattern": re.compile(r"\b(AHA|ACLS)\b.*?\b(201[0-9])\b|\b(201[0-9])\b.*?\b(AHA|ACLS)\b", re.IGNORECASE),
        "flag_message": "AHA/ACLS reference predates 2020 guidelines",
    },
    "SSC_2021": {
        "description": "Surviving Sepsis Campaign 2021 guidelines",
        "cutoff_year": 2021,
        "pattern": re.compile(
            r"(surviving\s+sepsis|SSC).*?\b(201[0-9])\b|\b(201[0-9])\b.*(surviving\s+sepsis|SSC)",
            re.IGNORECASE,
        ),
        "flag_message": "Surviving Sepsis Campaign reference predates 2021 guidelines",
    },
    "AHA_STEMI_2023": {
        "description": "AHA STEMI guidelines 2023",
        "cutoff_year": 2023,
        "pattern": re.compile(
            r"(STEMI|ST.Elevation).*?\b(201[0-9]|2020|2021|2022)\b|\b(201[0-9]|2020|2021|2022)\b.*(STEMI|ST.Elevation)",
            re.IGNORECASE,
        ),
        "flag_message": "STEMI guideline reference predates 2023 AHA update",
    },
}

_YEAR_RE = re.compile(r"\b(19|20)\d{2}\b")


# ---- Shared file loading (mirrors audit.py) ----

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
            results.append({"path": str(f), "name": f.stem, "fm": fm, "body": body})
    return results


# ---- Metric 1: Category entropy ----

def compute_category_entropy(conditions: list[dict]) -> dict:
    """Shannon entropy H = -sum(p * log2(p)) across categories."""
    counts = Counter(c["fm"].get("category", "unknown") for c in conditions)
    total = len(conditions)

    entropy = 0.0
    probs = {}
    for cat in VALID_CATEGORIES:
        n = counts.get(cat, 0)
        p = n / total if total else 0.0
        probs[cat] = {"count": n, "proportion": round(p, 4)}
        if p > 0:
            entropy -= p * math.log2(p)

    max_entropy = math.log2(len(VALID_CATEGORIES)) if VALID_CATEGORIES else 0.0
    balance_score = round(entropy / max_entropy, 4) if max_entropy > 0 else 0.0

    zero_categories = [cat for cat in VALID_CATEGORIES if counts.get(cat, 0) == 0]
    unknown_count = sum(n for cat, n in counts.items() if cat not in VALID_CATEGORIES)

    return {
        "shannon_entropy_bits": round(entropy, 4),
        "max_entropy_bits": round(max_entropy, 4),
        "balance_score_0_to_1": balance_score,
        "category_counts": {cat: counts.get(cat, 0) for cat in VALID_CATEGORIES},
        "category_proportions": probs,
        "zero_count_categories": zero_categories,
        "unknown_category_count": unknown_count,
    }


# ---- Metric 2: ESI balance (Gini coefficient) ----

def compute_esi_gini(conditions: list[dict]) -> dict:
    """Gini coefficient across ESI 1-5. 0 = perfect equality, 1 = maximally unequal."""
    counts = Counter()
    for c in conditions:
        esi = c["fm"].get("esi")
        if esi in (1, 2, 3, 4, 5):
            counts[esi] += 1

    total = sum(counts.values())
    values = [counts.get(level, 0) for level in range(1, 6)]

    # Gini coefficient via sorted-values formula
    n = len(values)
    sorted_vals = sorted(values)
    gini_num = sum((2 * (i + 1) - n - 1) * v for i, v in enumerate(sorted_vals))
    gini_denom = n * sum(sorted_vals)
    gini = round(gini_num / gini_denom, 4) if gini_denom > 0 else 0.0

    return {
        "esi_counts": {str(level): counts.get(level, 0) for level in range(1, 6)},
        "esi_proportions": {
            str(level): round(counts.get(level, 0) / total, 4) if total > 0 else 0.0
            for level in range(1, 6)
        },
        "gini_coefficient": gini,
        "interpretation": (
            "well-balanced" if gini < 0.3
            else "moderate imbalance" if gini < 0.6
            else "high imbalance"
        ),
        "missing_esi_count": len(conditions) - total,
    }


# ---- Metric 3: Risk tier x category matrix ----

def compute_tier_category_matrix(conditions: list[dict]) -> dict:
    """Count per (risk_tier, category) pair. Flag zero cells."""
    matrix: dict[str, dict[str, int]] = {tier: defaultdict(int) for tier in VALID_RISK_TIERS}
    unclassified = 0

    for c in conditions:
        tier = c["fm"].get("risk_tier", "")
        cat = c["fm"].get("category", "unknown")
        if tier in VALID_RISK_TIERS:
            matrix[tier][cat] += 1
        else:
            unclassified += 1

    # Build output matrix (only non-zero cells for readability)
    output_matrix = {
        tier: dict(counts) for tier, counts in matrix.items()
    }

    # Find zero cells: (tier, category) pairs present in neither row nor column
    zero_cells = []
    for tier in VALID_RISK_TIERS:
        for cat in VALID_CATEGORIES:
            if matrix[tier].get(cat, 0) == 0:
                zero_cells.append(f"{tier}×{cat}")

    return {
        "matrix": output_matrix,
        "zero_cells": zero_cells,
        "zero_cell_count": len(zero_cells),
        "total_possible_cells": len(VALID_RISK_TIERS) * len(VALID_CATEGORIES),
        "filled_cells": len(VALID_RISK_TIERS) * len(VALID_CATEGORIES) - len(zero_cells),
        "fill_rate": round(
            (len(VALID_RISK_TIERS) * len(VALID_CATEGORIES) - len(zero_cells))
            / (len(VALID_RISK_TIERS) * len(VALID_CATEGORIES)),
            4,
        ),
        "unclassified_condition_count": unclassified,
    }


# ---- Metric 4: Demographic representation ----

def compute_demographic_representation(conditions: list[dict]) -> dict:
    """Per-condition mention counts for 5 demographic groups. Summary stats."""
    per_condition = {}
    group_totals: Counter = Counter()
    covered_by_any = 0

    for c in conditions:
        body = c["body"]
        hits = {}
        for group, pattern in DEMOGRAPHIC_PATTERNS.items():
            matches = pattern.findall(body)
            if matches:
                hits[group] = len(matches)
                group_totals[group] += 1

        if hits:
            covered_by_any += 1
        per_condition[c["name"]] = hits

    total = len(conditions)
    return {
        "per_condition": per_condition,
        "group_coverage": {
            group: {
                "conditions_mentioning": group_totals.get(group, 0),
                "coverage_rate": round(group_totals.get(group, 0) / total, 4) if total else 0.0,
            }
            for group in DEMOGRAPHIC_PATTERNS
        },
        "conditions_with_any_demographic_mention": covered_by_any,
        "conditions_with_no_demographic_mention": total - covered_by_any,
        "total_conditions": total,
    }


# ---- Metric 5: Geographic representation ----

def compute_geographic_representation(conditions: list[dict]) -> dict:
    """Count files with international vs US-only mentions."""
    intl_files = []
    us_only_files = []
    both_files = []
    neither_files = []

    for c in conditions:
        body = c["body"]
        has_intl = bool(INTL_PATTERNS.search(body))
        has_us = bool(US_PATTERNS.search(body))

        if has_intl and has_us:
            both_files.append(c["name"])
        elif has_intl:
            intl_files.append(c["name"])
        elif has_us:
            us_only_files.append(c["name"])
        else:
            neither_files.append(c["name"])

    total = len(conditions)
    return {
        "international_only_count": len(intl_files),
        "us_only_count": len(us_only_files),
        "both_count": len(both_files),
        "neither_count": len(neither_files),
        "international_coverage_rate": round((len(intl_files) + len(both_files)) / total, 4) if total else 0.0,
        "international_only_files": intl_files,
        "us_only_files": us_only_files,
        "both_files": both_files,
        "neither_files": neither_files,
    }


# ---- Metric 6: Temporal drift ----

def compute_temporal_drift(conditions: list[dict]) -> dict:
    """Flag citations that predate known guideline milestone dates."""
    flagged: dict[str, list] = {key: [] for key in GUIDELINE_MILESTONES}
    all_source_years: list[int] = []

    for c in conditions:
        sources = c["fm"].get("sources", [])
        for src in sources:
            ref = src.get("ref", "")
            for year_m in _YEAR_RE.finditer(ref):
                all_source_years.append(int(year_m.group()))

            # Check each milestone pattern against this source ref
            for milestone_key, milestone in GUIDELINE_MILESTONES.items():
                if milestone["pattern"].search(ref):
                    # Extract year from ref
                    years_in_ref = [int(m.group()) for m in _YEAR_RE.finditer(ref)]
                    if years_in_ref:
                        ref_year = max(years_in_ref)
                        if ref_year < milestone["cutoff_year"]:
                            flagged[milestone_key].append({
                                "file": c["name"],
                                "ref": ref[:100],
                                "ref_year": ref_year,
                                "flag": milestone["flag_message"],
                            })

    year_distribution: Counter = Counter(all_source_years)
    sorted_years = sorted(year_distribution.items())
    mean_year = (
        sum(y * n for y, n in year_distribution.items()) / sum(year_distribution.values())
        if year_distribution
        else None
    )

    return {
        "flagged_by_milestone": {
            key: {
                "milestone": GUIDELINE_MILESTONES[key]["description"],
                "cutoff_year": GUIDELINE_MILESTONES[key]["cutoff_year"],
                "flag_count": len(entries),
                "flagged_refs": entries,
            }
            for key, entries in flagged.items()
        },
        "corpus_year_distribution": {str(y): n for y, n in sorted_years},
        "mean_source_year": round(mean_year, 1) if mean_year else None,
        "total_source_year_extractions": len(all_source_years),
    }


# ---- Main ----

def main() -> int:
    conditions = load_all_conditions()
    print(f"Loaded {len(conditions)} conditions", file=sys.stderr)

    report = {
        "corpus_size": len(conditions),
        "conditions_dir": str(CONDITIONS_DIR),
        "metrics": {
            "category_entropy": compute_category_entropy(conditions),
            "esi_balance": compute_esi_gini(conditions),
            "tier_category_matrix": compute_tier_category_matrix(conditions),
            "demographic_representation": compute_demographic_representation(conditions),
            "geographic_representation": compute_geographic_representation(conditions),
            "temporal_drift": compute_temporal_drift(conditions),
        },
    }

    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
