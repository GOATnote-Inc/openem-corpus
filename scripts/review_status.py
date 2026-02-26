#!/usr/bin/env python3
"""Scan corpus conditions and report physician review status.

Output:
  - REVIEWED conditions (grouped by risk tier)
  - NEEDS REVIEW conditions (grouped by risk tier, priority ordered)
  - Summary counts

Usage:
    python scripts/review_status.py
"""

import re
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CONDITIONS_DIR = REPO_ROOT / "corpus" / "tier1" / "conditions"

_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)

# Priority order for review: A (highest), then B, then C
TIER_ORDER = {"A": 0, "B": 1, "C": 2}
TIER_LABELS = {"A": "Risk Tier A (ESI 1 — resuscitation)", "B": "Risk Tier B (ESI 2 — emergent)", "C": "Risk Tier C (ESI 3+ — urgent/general)"}


def extract_frontmatter(text: str) -> dict | None:
    m = _FM_RE.match(text)
    if not m:
        return None
    return yaml.safe_load(m.group(1))


def main() -> None:
    reviewed: dict[str, list[str]] = {"A": [], "B": [], "C": []}
    needs_review: dict[str, list[str]] = {"A": [], "B": [], "C": []}

    for md_file in sorted(CONDITIONS_DIR.glob("*.md")):
        text = md_file.read_text()
        fm = extract_frontmatter(text)
        if not fm:
            continue

        cid = fm.get("id", md_file.stem)
        tier = fm.get("risk_tier", "C")
        reviewer = fm.get("reviewed_by")

        if reviewer:
            reviewed[tier].append(cid)
        else:
            needs_review[tier].append(cid)

    # Print results
    total_reviewed = sum(len(v) for v in reviewed.values())
    total_needs = sum(len(v) for v in needs_review.values())

    print("=== OpenEM Physician Review Status ===\n")
    print(f"REVIEWED: {total_reviewed} conditions")
    print(f"NEEDS REVIEW: {total_needs} conditions\n")

    print("--- REVIEWED ---")
    for tier in ["A", "B", "C"]:
        conditions = reviewed[tier]
        if conditions:
            print(f"\n  {TIER_LABELS[tier]} ({len(conditions)}):")
            for cid in conditions:
                print(f"    {cid}")

    print("\n--- NEEDS REVIEW (priority order) ---")
    for tier in ["A", "B", "C"]:
        conditions = needs_review[tier]
        if conditions:
            print(f"\n  {TIER_LABELS[tier]} ({len(conditions)}):")
            for cid in conditions:
                print(f"    {cid}")

    if not any(needs_review.values()):
        print("\n  All conditions reviewed!")

    print()


if __name__ == "__main__":
    main()
