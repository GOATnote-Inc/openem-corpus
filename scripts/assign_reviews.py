#!/usr/bin/env python3
"""Auto-assign unreviewed conditions to matching reviewers.

Reads the reviewer registry, current assignments, and condition frontmatter.
Matches reviewer specialties to condition categories, respects max_concurrent limits,
and generates updated assignments.

Usage:
    python scripts/assign_reviews.py                # update assignments.yaml
    python scripts/assign_reviews.py --dry-run       # preview without writing
    python scripts/assign_reviews.py --tier A        # assign only tier A
    python scripts/assign_reviews.py --category cardiovascular  # specific category
"""

import argparse
import re
import sys
from datetime import date, timedelta
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CONDITIONS_DIR = REPO_ROOT / "corpus" / "tier1" / "conditions"
REGISTRY_PATH = REPO_ROOT / "reviewers" / "registry.yaml"
ASSIGNMENTS_PATH = REPO_ROOT / "reviewers" / "assignments.yaml"

_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)

# SLA durations by tier
SLA_DAYS = {"A": 14, "B": 28, "C": 56}

# Priority by tier
PRIORITY_MAP = {"A": "high", "B": "medium", "C": "low"}


def extract_frontmatter(text: str) -> dict | None:
    m = _FM_RE.match(text)
    if not m:
        return None
    return yaml.safe_load(m.group(1))


def load_conditions(tier_filter: str | None = None, category_filter: str | None = None) -> list[dict]:
    conditions = []
    for f in sorted(CONDITIONS_DIR.glob("*.md")):
        text = f.read_text()
        fm = extract_frontmatter(text)
        if not fm:
            continue
        if tier_filter and fm.get("risk_tier") != tier_filter:
            continue
        if category_filter and fm.get("category") != category_filter:
            continue
        conditions.append(fm)
    return conditions


def load_registry() -> dict:
    if not REGISTRY_PATH.exists():
        return {"reviewers": []}
    return yaml.safe_load(REGISTRY_PATH.read_text()) or {"reviewers": []}


def load_assignments() -> dict:
    if not ASSIGNMENTS_PATH.exists():
        return {"assignments": []}
    data = yaml.safe_load(ASSIGNMENTS_PATH.read_text()) or {"assignments": []}
    if data.get("assignments") is None:
        data["assignments"] = []
    return data


def get_active_reviewers(registry: dict) -> list[dict]:
    return [r for r in registry.get("reviewers", []) if r.get("status") == "active"]


def reviewer_matches_category(reviewer: dict, category: str) -> bool:
    match = reviewer.get("category_match", [])
    if "all" in match:
        return True
    return category in match


def count_active_assignments(reviewer_id: str, assignments: list[dict]) -> int:
    return sum(
        1 for a in assignments
        if a.get("reviewer_id") == reviewer_id
        and a.get("status") in ("pending", "in_progress")
    )


def find_best_reviewer(
    category: str,
    reviewers: list[dict],
    assignments: list[dict],
) -> dict | None:
    """Find the best available reviewer for a given category."""
    candidates = []
    for r in reviewers:
        if not reviewer_matches_category(r, category):
            continue
        active = count_active_assignments(r["id"], assignments)
        max_concurrent = r.get("max_concurrent", 5)
        if active >= max_concurrent:
            continue
        candidates.append((r, active))

    if not candidates:
        return None

    # Sort by current load (least loaded first)
    candidates.sort(key=lambda x: x[1])
    return candidates[0][0]


def main() -> int:
    parser = argparse.ArgumentParser(description="Auto-assign reviews to matching reviewers")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument("--tier", type=str, help="Filter by risk tier (A/B/C)")
    parser.add_argument("--category", type=str, help="Filter by category")
    args = parser.parse_args()

    registry = load_registry()
    assignments_data = load_assignments()
    assignments = assignments_data["assignments"]
    reviewers = get_active_reviewers(registry)
    conditions = load_conditions(args.tier, args.category)

    if not reviewers:
        print("No active reviewers in registry. Add reviewers to reviewers/registry.yaml first.")
        return 1

    print(f"Active reviewers: {len(reviewers)}")
    print(f"Conditions to consider: {len(conditions)}")
    print(f"Existing assignments: {len(assignments)}")
    print()

    # Find conditions needing review (not already assigned)
    assigned_ids = {a["condition_id"] for a in assignments}
    # Also skip conditions already reviewed (have reviewed_by)
    needs_assignment = []
    already_reviewed = []

    for c in conditions:
        cid = c.get("id", "")
        if cid in assigned_ids:
            continue
        if c.get("reviewed_by"):
            already_reviewed.append(cid)
            continue
        needs_assignment.append(c)

    print(f"Already reviewed: {len(already_reviewed)}")
    print(f"Already assigned: {len(assigned_ids)}")
    print(f"Needs assignment: {len(needs_assignment)}")
    print()

    if not needs_assignment:
        print("All conditions are either reviewed or assigned.")
        return 0

    # Assign conditions
    new_assignments = []
    unassignable = []
    today = date.today()

    for c in needs_assignment:
        cid = c.get("id", "")
        category = c.get("category", "")
        tier = c.get("risk_tier", "C")

        reviewer = find_best_reviewer(category, reviewers, assignments + new_assignments)
        if not reviewer:
            unassignable.append({"condition_id": cid, "category": category, "tier": tier})
            continue

        sla_days = SLA_DAYS.get(tier, 56)
        due = today + timedelta(days=sla_days)

        assignment = {
            "condition_id": cid,
            "reviewer_id": reviewer["id"],
            "review_type": "full",
            "assigned_date": today.isoformat(),
            "due_date": due.isoformat(),
            "status": "pending",
            "priority": PRIORITY_MAP.get(tier, "low"),
            "category_match_required": [category],
        }
        new_assignments.append(assignment)

    # Summary
    print(f"=== Assignment Summary ===")
    print(f"New assignments: {len(new_assignments)}")
    print(f"Unassignable (no matching reviewer): {len(unassignable)}")
    print()

    if new_assignments:
        print("New assignments:")
        for a in new_assignments:
            print(f"  {a['condition_id']} -> {a['reviewer_id']} (due {a['due_date']}, {a['priority']})")
        print()

    if unassignable:
        print("Unassignable (need matching reviewer):")
        for u in unassignable:
            print(f"  {u['condition_id']} (category: {u['category']}, tier: {u['tier']})")
        print()

    # Write
    if not args.dry_run and new_assignments:
        assignments_data["assignments"].extend(new_assignments)
        ASSIGNMENTS_PATH.write_text(
            yaml.dump(assignments_data, default_flow_style=False, sort_keys=False)
        )
        print(f"Updated {ASSIGNMENTS_PATH}")
    elif args.dry_run:
        print("(dry run — no files written)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
