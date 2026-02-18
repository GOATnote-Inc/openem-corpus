#!/usr/bin/env python3
"""Print corpus statistics."""

import re
from pathlib import Path
from collections import Counter

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent


def extract_frontmatter(text: str) -> dict | None:
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return None
    return yaml.safe_load(match.group(1))


def main():
    categories = Counter()
    esi_counts = Counter()
    reviewed = 0
    unreviewed = 0
    total_words = 0
    tier_counts = {"tier1": 0, "tier2": 0}

    for tier_dir in ["corpus/tier1/conditions", "corpus/tier2/conditions"]:
        conditions_dir = REPO_ROOT / tier_dir
        if not conditions_dir.exists():
            continue
        for md_file in sorted(conditions_dir.glob("*.md")):
            text = md_file.read_text()
            fm = extract_frontmatter(text)
            if fm is None:
                continue

            track = fm.get("track", "unknown")
            tier_counts[track] = tier_counts.get(track, 0) + 1
            categories[fm.get("category", "unknown")] += 1
            esi_counts[fm.get("esi", 0)] += 1
            total_words += len(text.split())

            if fm.get("reviewed_by"):
                reviewed += 1
            else:
                unreviewed += 1

    total = sum(tier_counts.values())
    print(f"OpenEM Corpus Statistics")
    print(f"========================")
    print(f"Total conditions: {total}")
    print(f"  Tier 1 (Apache 2.0): {tier_counts.get('tier1', 0)}")
    print(f"  Tier 2 (CC-BY-SA):   {tier_counts.get('tier2', 0)}")
    print(f"  Reviewed: {reviewed}")
    print(f"  Unreviewed: {unreviewed}")
    print(f"  Total words: {total_words:,}")
    print()
    print("By ESI level:")
    for esi in sorted(esi_counts):
        print(f"  ESI {esi}: {esi_counts[esi]}")
    print()
    print("By category:")
    for cat, count in categories.most_common():
        print(f"  {cat}: {count}")


if __name__ == "__main__":
    main()
