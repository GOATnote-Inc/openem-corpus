#!/usr/bin/env python3
"""Check that README.md condition/category counts match the actual corpus.

Compares the hardcoded counts in the README table against:
  1. Number of .md files in corpus/tier1/conditions/
  2. Number of unique categories in schemas/condition.schema.yaml

Exit 0 = fresh, Exit 1 = stale.
"""

import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CONDITIONS_DIR = REPO_ROOT / "corpus" / "tier1" / "conditions"
SCHEMA_PATH = REPO_ROOT / "schemas" / "condition.schema.yaml"
README_PATH = REPO_ROOT / "README.md"

CONDITION_RE = re.compile(r"\|\s*Conditions\s*\|\s*(\d+)\s*\|")
CATEGORY_RE = re.compile(r"\|\s*Categories\s*\|\s*(\d+)\s*\|")


def main() -> int:
    # --- Actual counts ---
    md_files = sorted(CONDITIONS_DIR.glob("*.md"))
    actual_conditions = len(md_files)

    schema = yaml.safe_load(SCHEMA_PATH.read_text())
    actual_categories = len(schema["properties"]["category"]["enum"])

    # --- README counts ---
    readme_text = README_PATH.read_text()

    m_cond = CONDITION_RE.search(readme_text)
    m_cat = CATEGORY_RE.search(readme_text)

    if not m_cond or not m_cat:
        print("STALE: Could not find Conditions/Categories table rows in README.md")
        return 1

    readme_conditions = int(m_cond.group(1))
    readme_categories = int(m_cat.group(1))

    # --- Compare ---
    errors = []
    if readme_conditions != actual_conditions:
        errors.append(
            f"Conditions: README says {readme_conditions}, "
            f"corpus has {actual_conditions}"
        )
    if readme_categories != actual_categories:
        errors.append(
            f"Categories: README says {readme_categories}, "
            f"schema has {actual_categories}"
        )

    if errors:
        for e in errors:
            print(f"STALE: {e}")
        print("Fix README.md counts to match the corpus.")
        return 1

    print(
        f"FRESH: README counts match corpus "
        f"({actual_conditions} conditions, {actual_categories} categories)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
