#!/usr/bin/env python3
"""Review Dashboard: progress tracking, SLA compliance, and agreement metrics.

Displays:
  - Overall review coverage (by tier)
  - Per-reviewer workload and completion
  - SLA compliance (on-track / at-risk / overdue)
  - Category coverage percentages
  - Krippendorff's alpha for inter-reviewer agreement (when data available)
  - Gold standard performance per reviewer

Usage:
    python scripts/review_dashboard.py
    python scripts/review_dashboard.py --json     # machine-readable output
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CONDITIONS_DIR = REPO_ROOT / "corpus" / "tier1" / "conditions"
REGISTRY_PATH = REPO_ROOT / "reviewers" / "registry.yaml"
ASSIGNMENTS_PATH = REPO_ROOT / "reviewers" / "assignments.yaml"
GOLD_DIR = REPO_ROOT / "review" / "gold_standards"

_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
TODAY = date.today()


def extract_frontmatter(text: str) -> dict | None:
    m = _FM_RE.match(text)
    if not m:
        return None
    return yaml.safe_load(m.group(1))


def load_all_conditions() -> list[dict]:
    results = []
    for f in sorted(CONDITIONS_DIR.glob("*.md")):
        text = f.read_text()
        fm = extract_frontmatter(text)
        if fm:
            results.append(fm)
    return results


def load_registry() -> dict:
    if not REGISTRY_PATH.exists():
        return {"reviewers": []}
    return yaml.safe_load(REGISTRY_PATH.read_text()) or {"reviewers": []}


def load_assignments() -> list[dict]:
    if not ASSIGNMENTS_PATH.exists():
        return []
    data = yaml.safe_load(ASSIGNMENTS_PATH.read_text()) or {}
    return data.get("assignments") or []


def compute_sla_status(assignment: dict) -> str:
    """Classify assignment SLA status."""
    if assignment.get("status") == "complete":
        return "complete"

    due_str = assignment.get("due_date", "")
    if not due_str:
        return "unknown"

    try:
        due = date.fromisoformat(due_str)
    except (ValueError, TypeError):
        return "unknown"

    if TODAY > due:
        return "overdue"
    elif TODAY > due - timedelta(days=3):
        return "at-risk"
    else:
        return "on-track"


def compute_krippendorff_alpha(ratings: list[list[float | None]]) -> float | None:
    """Compute Krippendorff's alpha for ordinal/nominal data.

    ratings: list of items, each item is a list of ratings from different raters.
    None means the rater did not rate this item.

    Returns alpha or None if insufficient data.
    """
    if not ratings or len(ratings) < 2:
        return None

    # Flatten to get all non-None values
    all_values = []
    for item_ratings in ratings:
        all_values.extend(v for v in item_ratings if v is not None)

    if len(all_values) < 4:
        return None

    # Count coincidence matrix
    unique_values = sorted(set(all_values))
    if len(unique_values) < 2:
        return 1.0  # perfect agreement (all same)

    val_to_idx = {v: i for i, v in enumerate(unique_values)}
    n_values = len(unique_values)

    # Observed disagreement
    o_matrix = [[0.0] * n_values for _ in range(n_values)]
    n_pairs = 0

    for item_ratings in ratings:
        valid = [v for v in item_ratings if v is not None]
        m = len(valid)
        if m < 2:
            continue
        for i in range(m):
            for j in range(i + 1, m):
                ci = val_to_idx[valid[i]]
                cj = val_to_idx[valid[j]]
                o_matrix[ci][cj] += 1
                o_matrix[cj][ci] += 1
                n_pairs += 1

    if n_pairs == 0:
        return None

    # Expected disagreement (from marginals)
    marginals = [0.0] * n_values
    for item_ratings in ratings:
        valid = [v for v in item_ratings if v is not None]
        m = len(valid)
        if m < 2:
            continue
        for v in valid:
            marginals[val_to_idx[v]] += 1

    total_marginals = sum(marginals)
    e_matrix = [[0.0] * n_values for _ in range(n_values)]
    for i in range(n_values):
        for j in range(n_values):
            if i != j:
                e_matrix[i][j] = marginals[i] * marginals[j]

    # Compute Do and De
    Do = sum(o_matrix[i][j] for i in range(n_values) for j in range(n_values) if i != j)
    De = sum(e_matrix[i][j] for i in range(n_values) for j in range(n_values) if i != j)

    if De == 0:
        return 1.0

    Do_norm = Do / n_pairs
    De_norm = De / (total_marginals * (total_marginals - 1))

    if De_norm == 0:
        return 1.0

    alpha = 1.0 - (Do_norm / De_norm)
    return alpha


def main() -> int:
    parser = argparse.ArgumentParser(description="Review progress dashboard")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    conditions = load_all_conditions()
    registry = load_registry()
    assignments = load_assignments()

    # === Overall coverage ===
    total = len(conditions)
    reviewed = sum(1 for c in conditions if c.get("reviewed_by"))
    by_tier = defaultdict(lambda: {"total": 0, "reviewed": 0})

    for c in conditions:
        tier = c.get("risk_tier", "C")
        by_tier[tier]["total"] += 1
        if c.get("reviewed_by"):
            by_tier[tier]["reviewed"] += 1

    # Conditions with 2+ reviews (consensus)
    consensus_count = sum(
        1 for c in conditions
        if len(c.get("reviews", [])) >= 2
    )

    # === Per-category coverage ===
    by_category = defaultdict(lambda: {"total": 0, "reviewed": 0})
    for c in conditions:
        cat = c.get("category", "unknown")
        by_category[cat]["total"] += 1
        if c.get("reviewed_by"):
            by_category[cat]["reviewed"] += 1

    # === Per-reviewer stats ===
    reviewer_stats = defaultdict(lambda: {
        "assigned": 0, "completed": 0, "overdue": 0, "issues_total": 0
    })
    sla_summary = {"on-track": 0, "at-risk": 0, "overdue": 0, "complete": 0, "unknown": 0}

    for a in assignments:
        rid = a.get("reviewer_id", "unassigned")
        reviewer_stats[rid]["assigned"] += 1

        status = compute_sla_status(a)
        sla_summary[status] += 1

        if a.get("status") == "complete":
            reviewer_stats[rid]["completed"] += 1
        if status == "overdue":
            reviewer_stats[rid]["overdue"] += 1

    # === Output ===
    if args.json:
        report = {
            "date": TODAY.isoformat(),
            "overall": {
                "total": total,
                "reviewed": reviewed,
                "review_pct": round(reviewed / total * 100, 1) if total else 0,
                "consensus": consensus_count,
            },
            "by_tier": dict(by_tier),
            "by_category": dict(by_category),
            "sla": dict(sla_summary),
            "reviewers": dict(reviewer_stats),
            "assignments_total": len(assignments),
        }
        print(json.dumps(report, indent=2))
        return 0

    # Text output
    print("=" * 60)
    print("  OpenEM Review Dashboard")
    print(f"  Generated: {TODAY.isoformat()}")
    print("=" * 60)
    print()

    # Overall
    pct = round(reviewed / total * 100, 1) if total else 0
    print(f"OVERALL: {reviewed}/{total} reviewed ({pct}%)")
    tier_a = by_tier.get("A", {"total": 0, "reviewed": 0})
    print(f"  Tier A consensus (2+ reviews): {consensus_count}/{tier_a['total']}")
    print()

    # By tier
    print("BY TIER:")
    for tier in ["A", "B", "C"]:
        t = by_tier.get(tier, {"total": 0, "reviewed": 0})
        pct = round(t["reviewed"] / t["total"] * 100, 1) if t["total"] else 0
        label = {"A": "ESI 1 — resuscitation", "B": "ESI 2 — emergent", "C": "ESI 3+ — urgent/general"}
        print(f"  {tier} ({label.get(tier, '')}): {t['reviewed']}/{t['total']} ({pct}%)")
    print()

    # SLA compliance
    if assignments:
        print("SLA COMPLIANCE:")
        print(f"  On-track: {sla_summary['on-track']}")
        print(f"  At-risk: {sla_summary['at-risk']}")
        print(f"  Overdue: {sla_summary['overdue']}")
        print(f"  Complete: {sla_summary['complete']}")
        print()

    # Per-reviewer
    if reviewer_stats:
        print("PER-REVIEWER:")
        for rid, stats in sorted(reviewer_stats.items()):
            print(f"  {rid}: {stats['completed']}/{stats['assigned']} complete, {stats['overdue']} overdue")
        print()

    # Category coverage
    print("CATEGORY COVERAGE:")
    for cat in sorted(by_category.keys()):
        c = by_category[cat]
        pct = round(c["reviewed"] / c["total"] * 100, 1) if c["total"] else 0
        bar = "#" * int(pct / 5) + "." * (20 - int(pct / 5))
        print(f"  {cat:30s} {c['reviewed']:3d}/{c['total']:3d} ({pct:5.1f}%) [{bar}]")
    print()

    # Krippendorff's alpha (placeholder — computed when multi-reviewer data exists)
    multi_reviewed = [c for c in conditions if len(c.get("reviews", [])) >= 2]
    if multi_reviewed:
        # Build ratings matrix from reviews
        # For now, use issues_found count as the rating
        ratings = []
        for c in multi_reviewed:
            item_ratings = [r.get("issues_found", 0) for r in c["reviews"]]
            ratings.append(item_ratings)

        alpha = compute_krippendorff_alpha(ratings)
        if alpha is not None:
            print(f"INTER-REVIEWER AGREEMENT:")
            print(f"  Krippendorff's alpha: {alpha:.3f}")
            if alpha >= 0.80:
                print(f"  Status: Strong agreement")
            elif alpha >= 0.67:
                print(f"  Status: Acceptable agreement")
            elif alpha >= 0.50:
                print(f"  Status: Weak agreement — consider rubric clarification")
            else:
                print(f"  Status: Poor agreement — pause and retrain")
            print()
    else:
        print("INTER-REVIEWER AGREEMENT:")
        print("  Insufficient data (need 2+ reviews on same conditions)")
        print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
