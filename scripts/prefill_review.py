#!/usr/bin/env python3
"""Pre-fill review metadata in a condition's YAML frontmatter.

Saves reviewers from manually editing YAML. Adds reviewed_by, review_date,
and a structured reviews[] entry to the condition file.

Usage:
    python scripts/prefill_review.py CONDITION_ID "Reviewer Name, MD — Board Certification"
    python scripts/prefill_review.py stemi "Brandon Dent, MD — Board Certified Emergency Medicine"

Options:
    --review-type TYPE   Review type: full, dosing-focused, red-team, spot-check, consensus
                         (default: full)
    --issues N           Number of issues found (default: 0)
    --issues-ref REF     PR or issue reference for reported issues (e.g., "PR#42")
    --date YYYY-MM-DD    Review date (default: today)
    --dry-run            Print the updated frontmatter without writing the file

The script will refuse to overwrite an existing review by the same reviewer
unless --force is passed.
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CONDITIONS_DIR = REPO_ROOT / "corpus" / "tier1" / "conditions"

_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)

VALID_REVIEW_TYPES = {"full", "dosing-focused", "red-team", "spot-check", "consensus"}


def find_condition_file(condition_id: str) -> Path | None:
    """Find the condition markdown file by ID."""
    candidate = CONDITIONS_DIR / f"{condition_id}.md"
    if candidate.exists():
        return candidate
    # Try tier2 as fallback
    tier2 = REPO_ROOT / "corpus" / "tier2" / "conditions" / f"{condition_id}.md"
    if tier2.exists():
        return tier2
    return None


def parse_frontmatter(text: str) -> tuple[dict, str] | None:
    """Extract frontmatter dict and the body after the closing ---."""
    m = _FM_RE.match(text)
    if not m:
        return None
    fm = yaml.safe_load(m.group(1))
    body = text[m.end():]
    return fm, body


def serialize_frontmatter(fm: dict, body: str) -> str:
    """Reserialize frontmatter + body into the full file content."""
    # Use default_flow_style=False for readable YAML, but allow inline lists
    # for simple fields like aliases and icd10.
    dumped = yaml.dump(
        fm,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        width=120,
    )
    return f"---\n{dumped}---{body}"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Pre-fill review metadata in a condition's YAML frontmatter.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("condition_id", help="Condition ID (e.g., stemi, anaphylaxis)")
    parser.add_argument("reviewer", help='Reviewer name and credentials (e.g., "Jane Doe, MD — Board Certified EM")')
    parser.add_argument(
        "--review-type",
        default="full",
        choices=sorted(VALID_REVIEW_TYPES),
        help="Review type (default: full)",
    )
    parser.add_argument("--issues", type=int, default=0, help="Number of issues found (default: 0)")
    parser.add_argument("--issues-ref", default="", help='PR or issue reference (e.g., "PR#42")')
    parser.add_argument("--date", default=None, help="Review date as YYYY-MM-DD (default: today)")
    parser.add_argument("--dry-run", action="store_true", help="Print updated frontmatter without writing")
    parser.add_argument("--force", action="store_true", help="Overwrite existing review by the same reviewer")

    args = parser.parse_args()

    # Resolve date
    review_date = args.date or date.today().isoformat()
    try:
        date.fromisoformat(review_date)
    except ValueError:
        print(f"Error: invalid date format '{review_date}'. Use YYYY-MM-DD.", file=sys.stderr)
        return 1

    # Find the condition file
    condition_file = find_condition_file(args.condition_id)
    if condition_file is None:
        print(f"Error: no condition file found for '{args.condition_id}'.", file=sys.stderr)
        print(f"  Looked in: {CONDITIONS_DIR}", file=sys.stderr)
        # Suggest close matches
        candidates = sorted(CONDITIONS_DIR.glob("*.md"))
        matches = [c.stem for c in candidates if args.condition_id in c.stem]
        if matches:
            print(f"  Did you mean: {', '.join(matches[:5])}?", file=sys.stderr)
        return 1

    # Read and parse
    text = condition_file.read_text()
    result = parse_frontmatter(text)
    if result is None:
        print(f"Error: could not parse YAML frontmatter in {condition_file}", file=sys.stderr)
        return 1

    fm, body = result

    # Check for existing review by same reviewer — check both the flat
    # reviewed_by field (legacy, used on the first 80 conditions) and
    # the structured reviews[] array.
    existing_reviews = fm.get("reviews", []) or []
    existing_reviewer = fm.get("reviewed_by", "")
    has_legacy_match = existing_reviewer == args.reviewer and not existing_reviews
    has_array_match = any(r.get("reviewer") == args.reviewer for r in existing_reviews)

    if (has_legacy_match or has_array_match) and not args.force:
        existing_date = fm.get("review_date", "unknown")
        if has_array_match:
            existing_date = next(
                r.get("date", "unknown") for r in existing_reviews if r.get("reviewer") == args.reviewer
            )
        print(
            f"Error: {args.condition_id} already has a review by {args.reviewer} "
            f"(date: {existing_date}).",
            file=sys.stderr,
        )
        print("  Use --force to overwrite.", file=sys.stderr)
        return 1

    if has_array_match:
        existing_reviews = [r for r in existing_reviews if r.get("reviewer") != args.reviewer]

    # Build the new review entry
    new_review = {
        "reviewer": args.reviewer,
        "date": review_date,
        "type": args.review_type,
        "issues_found": args.issues,
        "issues_ref": args.issues_ref,
    }

    # Update frontmatter
    fm["reviewed_by"] = args.reviewer
    fm["review_date"] = review_date
    fm["reviews"] = existing_reviews + [new_review]

    # Serialize
    updated = serialize_frontmatter(fm, body)

    if args.dry_run:
        # Print just the frontmatter portion
        m = _FM_RE.match(updated)
        if m:
            print("--- DRY RUN — updated frontmatter ---")
            print(f"---\n{m.group(1)}\n---")
        else:
            print(updated)
        print(f"\nFile: {condition_file} (not modified)")
        return 0

    # Write
    condition_file.write_text(updated)
    print(f"Updated: {condition_file.relative_to(REPO_ROOT)}")
    print(f"  reviewed_by: {args.reviewer}")
    print(f"  review_date: {review_date}")
    print(f"  review_type: {args.review_type}")
    if args.issues > 0:
        print(f"  issues_found: {args.issues}")
        if args.issues_ref:
            print(f"  issues_ref: {args.issues_ref}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
