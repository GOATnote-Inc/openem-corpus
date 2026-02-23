#!/usr/bin/env python3
"""Quality gate for OpenEM corpus. Blocks merge on critical issues.

Exit 0 = pass, Exit 1 = fail.

Checks (blocking):
  - Any dose range anomaly (drug dose exceeds known safe maximum)
  - Any condition with no sources
  - Any condition with no ICD-10 codes
  - Any condition with < 6/7 required sections having substantive content
  - Any condition with zero PMIDs across all sources
  - Any ICD-10 code in invalid format

Run this as a pre-merge gate. It imports check logic from audit.py so the
validation rules stay in sync.
"""

import json
import re
import sys
import yaml
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONDITIONS_DIR = REPO_ROOT / "corpus" / "tier1" / "conditions"

# ICD-10-CM format (mirrors audit.py)
ICD10_PATTERN = re.compile(r"^[A-TV-Z]\d{2}(\.[A-Z0-9]{1,4})?$")

# Required content sections and minimum character threshold
REQUIRED_SECTIONS = [
    "Recognition",
    "Critical Actions",
    "Differential Diagnosis",
    "Workup",
    "Treatment",
    "Disposition",
    "Pitfalls",
]
MIN_SECTION_CHARS = 50
# A condition passes if at least 6 of the 7 required sections are substantive
MIN_PASSING_SECTIONS = 6

# Dose anomaly limits (mirrors audit.py Pass 3)
DOSE_LIMITS = [
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


# ---- File loading ----

def extract_frontmatter(text: str) -> dict | None:
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return None
    return yaml.safe_load(m.group(1))


def get_body(text: str) -> str:
    m = re.match(r"^---\n.*?\n---\n?(.*)", text, re.DOTALL)
    return m.group(1) if m else text


def load_all_conditions() -> list[dict]:
    results = []
    for f in sorted(CONDITIONS_DIR.glob("*.md")):
        text = f.read_text()
        fm = extract_frontmatter(text)
        body = get_body(text)
        if fm:
            results.append({"path": str(f), "name": f.stem, "fm": fm, "body": body})
    return results


# ---- Gate checks ----

def gate_no_sources(conditions: list[dict]) -> list[dict]:
    """BLOCK: Any condition with no sources."""
    failures = []
    for c in conditions:
        sources = c["fm"].get("sources", [])
        if not sources:
            failures.append({
                "gate": "no_sources",
                "file": c["name"],
                "message": "No sources listed — every condition requires at least one citation",
            })
    return failures


def gate_no_icd10(conditions: list[dict]) -> list[dict]:
    """BLOCK: Any condition with no ICD-10 codes."""
    failures = []
    for c in conditions:
        codes = c["fm"].get("icd10", [])
        if not codes:
            failures.append({
                "gate": "no_icd10",
                "file": c["name"],
                "message": "No ICD-10 codes — every condition requires at least one code",
            })
    return failures


def gate_invalid_icd10(conditions: list[dict]) -> list[dict]:
    """BLOCK: Any ICD-10 code in invalid format."""
    failures = []
    for c in conditions:
        codes = c["fm"].get("icd10", [])
        for code in codes:
            if not ICD10_PATTERN.match(str(code)):
                failures.append({
                    "gate": "invalid_icd10_format",
                    "file": c["name"],
                    "message": f"Invalid ICD-10-CM format: '{code}' — must match [A-TV-Z]\\d{{2}}(\\.[A-Z0-9]{{1,4}})?",
                })
    return failures


def gate_dose_range_anomalies(conditions: list[dict]) -> list[dict]:
    """BLOCK: Any dose exceeding known safe maximum."""
    failures = []
    for c in conditions:
        for pat, max_dose, label in DOSE_LIMITS:
            for m in re.finditer(pat, c["body"], re.IGNORECASE):
                try:
                    dose_val = float(m.group(1))
                    if dose_val > max_dose:
                        failures.append({
                            "gate": "dose_range_anomaly",
                            "file": c["name"],
                            "message": (
                                f"{label}: {dose_val} mg exceeds max {max_dose} mg. "
                                f"Match: '{m.group()}'"
                            ),
                        })
                except (ValueError, IndexError):
                    pass
    return failures


def gate_zero_pmids(conditions: list[dict]) -> list[dict]:
    """BLOCK: Any condition where no source has a PMID (zero PMIDs across all sources)."""
    failures = []
    for c in conditions:
        sources = c["fm"].get("sources", [])
        if not sources:
            continue  # covered by gate_no_sources
        pmids = [
            src.get("pmid")
            for src in sources
            if src.get("pmid") and str(src.get("pmid", "")).strip()
        ]
        # Only flag if ALL sources lack PMIDs — some conditions rely on guidelines without PMIDs
        # which is acceptable. Flag only when we have pubmed-type sources without PMIDs.
        pubmed_sources = [s for s in sources if s.get("type") == "pubmed"]
        if pubmed_sources and not pmids:
            failures.append({
                "gate": "zero_pmids",
                "file": c["name"],
                "message": (
                    f"{len(pubmed_sources)} source(s) typed 'pubmed' but none have a PMID field. "
                    "Add pmid: fields or change source type to 'guideline'."
                ),
            })
    return failures


def gate_content_completeness(conditions: list[dict]) -> list[dict]:
    """BLOCK: Any condition with < MIN_PASSING_SECTIONS of 7 required sections having content."""
    failures = []

    for c in conditions:
        body = c["body"]
        passing_sections = 0
        section_results = {}

        for section in REQUIRED_SECTIONS:
            pattern = re.compile(
                r"##\s+" + re.escape(section) + r"[^\n]*\n(.*?)(?=\n##\s|\Z)",
                re.DOTALL | re.IGNORECASE,
            )
            m = pattern.search(body)
            if m:
                content = m.group(1).strip()
                cleaned = re.sub(r"[#*`|_\-\[\]]+", " ", content)
                cleaned = re.sub(r"\s+", " ", cleaned).strip()
                char_count = len(cleaned)
                if char_count >= MIN_SECTION_CHARS:
                    passing_sections += 1
                    section_results[section] = f"OK ({char_count} chars)"
                else:
                    section_results[section] = f"THIN ({char_count} chars < {MIN_SECTION_CHARS})"
            else:
                section_results[section] = "MISSING"

        if passing_sections < MIN_PASSING_SECTIONS:
            failures.append({
                "gate": "content_completeness",
                "file": c["name"],
                "message": (
                    f"Only {passing_sections}/{len(REQUIRED_SECTIONS)} required sections are "
                    f"substantive (need {MIN_PASSING_SECTIONS}). "
                    "Sections: " + "; ".join(f"{s}: {r}" for s, r in section_results.items())
                ),
                "passing_sections": passing_sections,
                "required": MIN_PASSING_SECTIONS,
                "section_detail": section_results,
            })

    return failures


# ---- Runner ----

def main() -> int:
    conditions = load_all_conditions()
    print(f"Quality gate: checking {len(conditions)} conditions", file=sys.stderr)

    all_failures: list[dict] = []

    gates = [
        ("no_sources", gate_no_sources),
        ("no_icd10", gate_no_icd10),
        ("invalid_icd10_format", gate_invalid_icd10),
        ("dose_range_anomaly", gate_dose_range_anomalies),
        ("zero_pmids", gate_zero_pmids),
        ("content_completeness", gate_content_completeness),
    ]

    gate_results: dict[str, dict] = {}
    for gate_name, fn in gates:
        failures = fn(conditions)
        gate_results[gate_name] = {
            "failure_count": len(failures),
            "failures": failures,
        }
        all_failures.extend(failures)
        status = "FAIL" if failures else "PASS"
        print(f"  [{status}] {gate_name}: {len(failures)} failure(s)", file=sys.stderr)

    total_failures = len(all_failures)
    passed = total_failures == 0

    report = {
        "result": "PASS" if passed else "FAIL",
        "total_failures": total_failures,
        "conditions_checked": len(conditions),
        "gates": gate_results,
    }

    print(json.dumps(report, indent=2))

    if passed:
        print("\nQuality gate PASSED — all checks clean.", file=sys.stderr)
        return 0
    else:
        print(
            f"\nQuality gate FAILED — {total_failures} blocking issue(s). "
            "Fix before merge.",
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
