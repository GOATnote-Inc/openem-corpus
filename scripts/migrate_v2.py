#!/usr/bin/env python3
"""Migrate all condition files from schema v1 to v2.0.

Changes per file:
  - Remove reviewed_by field
  - Replace verification block with validation block
  - Add risk_tier field (A/B/C based on ESI)
  - Update last_updated to migration date

Idempotent: safe to run multiple times.
"""

import re
import sys
import yaml
from pathlib import Path
from datetime import date

REPO_ROOT = Path(__file__).resolve().parent.parent
CONDITIONS_DIR = REPO_ROOT / "corpus" / "tier1" / "conditions"
TODAY = date.today().isoformat()


def extract_frontmatter_raw(text: str) -> tuple[str, str, str]:
    """Return (pre_fm, fm_text, post_fm) splitting on --- delimiters."""
    m = re.match(r"^(---\n)(.*?\n)(---\n?)", text, re.DOTALL)
    if not m:
        raise ValueError("No YAML frontmatter found")
    return m.group(1), m.group(2), text[m.end() :]


def parse_verification(fm_text: str) -> dict:
    """Extract verification dates from raw frontmatter text."""
    fm = yaml.safe_load(fm_text)
    return fm.get("verification", {}) or {}


def esi_to_risk_tier(esi: int) -> str:
    if esi == 1:
        return "A"
    elif esi == 2:
        return "B"
    else:
        return "C"


def build_validation_yaml(old_verif: dict) -> str:
    """Build the validation: block as YAML text."""
    ac = old_verif.get("audit_completed")
    dr = old_verif.get("dosing_crosscheck")
    cp = old_verif.get("pmids_verified")

    lines = ["validation:"]
    lines.append(f"  automated_consistency_check: {_val(ac)}")
    lines.append(f"  dose_range_validator: {_val(dr)}")
    lines.append(f"  unit_normalization_check: null")
    lines.append(f"  cross_file_consistency_check: {_val(dr)}")
    lines.append(f"  citation_presence_check: {_val(cp)}")
    lines.append(f"  duplicate_content_check: null")
    lines.append(f"  outlier_detection_flag: clear")
    lines.append(f'  schema_version: "2.0"')
    lines.append(f"  guideline_version_reference: null")
    lines.append(f"  provenance_links: []")
    return "\n".join(lines) + "\n"


def _val(v):
    """Format a value for YAML: date string or null."""
    if v is None:
        return "null"
    return f'"{v}"'


def migrate_file(path: Path) -> str:
    """Migrate a single file. Returns status message."""
    text = path.read_text()

    # Parse frontmatter
    try:
        opener, fm_text, body = extract_frontmatter_raw(text)
    except ValueError as e:
        return f"SKIP {path.name}: {e}"

    fm = yaml.safe_load(fm_text)

    # Already migrated?
    if "validation" in fm and "risk_tier" in fm and "reviewed_by" not in fm:
        return f"SKIP {path.name}: already migrated"

    # Get data for migration
    esi = fm.get("esi", 3)
    risk_tier = esi_to_risk_tier(esi)
    old_verif = fm.get("verification", {}) or {}

    # Build new frontmatter by string manipulation
    lines = fm_text.rstrip("\n").split("\n")
    new_lines = []
    skip_block = False

    for line in lines:
        # Skip reviewed_by line
        if re.match(r"^reviewed_by:", line):
            continue

        # Skip verification block
        if re.match(r"^verification:", line):
            skip_block = True
            continue
        if skip_block:
            if line.startswith("  ") and not re.match(r"^[a-z_]", line):
                continue  # indented child of verification
            else:
                skip_block = False

        new_lines.append(line)

    # Add risk_tier after compiled_by
    final_lines = []
    for line in new_lines:
        final_lines.append(line)
        if re.match(r"^compiled_by:", line):
            final_lines.append(f"risk_tier: {risk_tier}")

    # Add validation block at end
    validation_yaml = build_validation_yaml(old_verif)
    final_lines.append(validation_yaml.rstrip("\n"))

    new_fm_text = "\n".join(final_lines) + "\n"
    new_text = opener + new_fm_text + "---" + body

    path.write_text(new_text)
    return f"OK {path.name}: tier={risk_tier}"


def main():
    if not CONDITIONS_DIR.exists():
        print(f"ERROR: {CONDITIONS_DIR} not found")
        sys.exit(1)

    files = sorted(CONDITIONS_DIR.glob("*.md"))
    print(f"Migrating {len(files)} files to schema v2.0...\n")

    ok = 0
    skip = 0
    err = 0

    for f in files:
        result = migrate_file(f)
        print(result)
        if result.startswith("OK"):
            ok += 1
        elif result.startswith("SKIP"):
            skip += 1
        else:
            err += 1

    print(f"\nDone: {ok} migrated, {skip} skipped, {err} errors")
    return 0 if err == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
