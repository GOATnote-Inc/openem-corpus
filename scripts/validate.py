#!/usr/bin/env python3
"""Validate all condition files against the v2.0 frontmatter schema.

Exit 0 = all pass, exit 1 = errors found. This is a build gate.
"""

import sys
import re
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "schemas" / "condition.schema.yaml"

REQUIRED_FIELDS = [
    "id",
    "condition",
    "icd10",
    "esi",
    "time_to_harm",
    "category",
    "track",
    "sources",
    "last_updated",
    "compiled_by",
    "risk_tier",
    "validation",
]
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
    "disaster-mci",
    "procedural",
]
VALID_TRACKS = ["tier1", "tier2"]
VALID_RISK_TIERS = ["A", "B", "C"]
REQUIRED_SECTIONS = ["Recognition", "Critical Actions", "Pitfalls"]


def extract_frontmatter(text: str) -> dict | None:
    """Extract YAML frontmatter from markdown text."""
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return None
    return yaml.safe_load(match.group(1))


def validate_file(path: Path) -> list[str]:
    """Validate a single condition file. Returns list of errors."""
    errors = []
    text = path.read_text()

    # Check frontmatter exists
    fm = extract_frontmatter(text)
    if fm is None:
        return [f"{path}: No YAML frontmatter found"]

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in fm:
            errors.append(f"{path}: Missing required field '{field}'")

    # Validate field values
    if "id" in fm:
        if not re.match(r"^[a-z0-9-]+$", str(fm["id"])):
            errors.append(f"{path}: id must be lowercase alphanumeric with hyphens")
        if fm["id"] != path.stem:
            errors.append(
                f"{path}: id '{fm['id']}' does not match filename '{path.stem}'"
            )

    if "icd10" in fm:
        if not isinstance(fm["icd10"], list) or len(fm["icd10"]) == 0:
            errors.append(f"{path}: icd10 must be a non-empty list")

    if "esi" in fm:
        if not isinstance(fm["esi"], int) or fm["esi"] < 1 or fm["esi"] > 5:
            errors.append(f"{path}: esi must be integer 1-5")

    if "category" in fm:
        if fm["category"] not in VALID_CATEGORIES:
            errors.append(f"{path}: Invalid category '{fm['category']}'")

    if "track" in fm:
        if fm["track"] not in VALID_TRACKS:
            errors.append(f"{path}: Invalid track '{fm['track']}'")

    if "risk_tier" in fm:
        if fm["risk_tier"] not in VALID_RISK_TIERS:
            errors.append(
                f"{path}: Invalid risk_tier '{fm['risk_tier']}' (must be A, B, or C)"
            )

    if "validation" in fm:
        val = fm["validation"]
        if not isinstance(val, dict):
            errors.append(f"{path}: validation must be an object")
        elif "schema_version" not in val:
            errors.append(f"{path}: validation.schema_version is required")

    if "sources" in fm:
        if not isinstance(fm["sources"], list) or len(fm["sources"]) == 0:
            errors.append(f"{path}: sources must be a non-empty list")
        else:
            for i, src in enumerate(fm["sources"]):
                if "type" not in src:
                    errors.append(f"{path}: source[{i}] missing 'type'")
                if "ref" not in src:
                    errors.append(f"{path}: source[{i}] missing 'ref'")

    # Validate time_to_harm (string or structured object)
    if "time_to_harm" in fm:
        tth = fm["time_to_harm"]
        if not isinstance(tth, (str, dict)):
            errors.append(f"{path}: time_to_harm must be a string or object")
        elif isinstance(tth, dict):
            valid_tth_keys = {
                "irreversible_injury",
                "death",
                "optimal_intervention_window",
            }
            for k in tth:
                if k not in valid_tth_keys:
                    errors.append(f"{path}: time_to_harm has unknown key '{k}'")

    # Validate optional defer fields
    if "disposition_default" in fm:
        valid_dispositions = ["admission", "outpatient", "observation"]
        if fm["disposition_default"] not in valid_dispositions:
            errors.append(
                f"{path}: Invalid disposition_default '{fm['disposition_default']}'"
            )

    if "escalation_triggers" in fm:
        if not isinstance(fm["escalation_triggers"], list):
            errors.append(f"{path}: escalation_triggers must be an array")

    if "confusion_pairs" in fm:
        if not isinstance(fm["confusion_pairs"], list):
            errors.append(f"{path}: confusion_pairs must be an array")
        else:
            for i, cp in enumerate(fm["confusion_pairs"]):
                if not isinstance(cp, dict):
                    errors.append(f"{path}: confusion_pairs[{i}] must be an object")
                elif "condition" not in cp or "differentiators" not in cp:
                    errors.append(
                        f"{path}: confusion_pairs[{i}] missing 'condition' or 'differentiators'"
                    )

    # Reject legacy fields
    if "reviewed_by" in fm:
        errors.append(
            f"{path}: Legacy field 'reviewed_by' present — remove it (schema v2.0)"
        )

    # Check required markdown sections
    for section in REQUIRED_SECTIONS:
        if f"## {section}" not in text:
            errors.append(f"{path}: Missing required section '## {section}'")

    return errors


def main() -> None:
    all_errors = []
    file_count = 0

    for tier_dir in ["corpus/tier1/conditions", "corpus/tier2/conditions"]:
        conditions_dir = REPO_ROOT / tier_dir
        if not conditions_dir.exists():
            continue
        for md_file in sorted(conditions_dir.glob("*.md")):
            file_count += 1
            errors = validate_file(md_file)
            all_errors.extend(errors)

    if all_errors:
        print(f"FAILED: {len(all_errors)} errors in {file_count} files:\n")
        for err in all_errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print(f"PASSED: {file_count} files validated successfully (schema v2.0).")
        sys.exit(0)


if __name__ == "__main__":
    main()
