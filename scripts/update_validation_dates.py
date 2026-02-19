#!/usr/bin/env python3
"""Batch update validation check dates across all condition files.

Usage:
  python3 scripts/update_validation_dates.py <check_name> [files...]

If no files given, updates all condition files.
Valid check names:
  automated_consistency_check, dose_range_validator, unit_normalization_check,
  cross_file_consistency_check, citation_presence_check, duplicate_content_check,
  icd10_verified, guideline_currency
"""

import re
import sys
from pathlib import Path
from datetime import date

REPO_ROOT = Path(__file__).resolve().parent.parent
CONDITIONS_DIR = REPO_ROOT / "corpus" / "tier1" / "conditions"
TODAY = date.today().isoformat()

# Map of check names to their YAML key in the validation block
VALID_CHECKS = {
    "automated_consistency_check",
    "dose_range_validator",
    "unit_normalization_check",
    "cross_file_consistency_check",
    "citation_presence_check",
    "duplicate_content_check",
    "outlier_detection_flag",
    "guideline_version_reference",
}


def update_check_date(path: Path, check_name: str, value: str) -> bool:
    """Update a validation check date in a file. Returns True if modified."""
    text = path.read_text()

    # Pattern: find the check line within the validation block
    pattern = rf"(  {check_name}: )(?:null|\"[^\"]*\"|clear|flagged)"
    replacement = rf'\1"{value}"'

    new_text, count = re.subn(pattern, replacement, text)
    if count > 0:
        path.write_text(new_text)
        return True
    return False


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    check_name = sys.argv[1]
    value = sys.argv[2] if len(sys.argv) > 2 else TODAY

    # Get files to update
    if len(sys.argv) > 3:
        files = [Path(f) for f in sys.argv[3:]]
    else:
        files = sorted(CONDITIONS_DIR.glob("*.md"))

    updated = 0
    for f in files:
        if update_check_date(f, check_name, value):
            updated += 1

    print(f"Updated {check_name} to '{value}' in {updated}/{len(files)} files")


if __name__ == "__main__":
    main()
