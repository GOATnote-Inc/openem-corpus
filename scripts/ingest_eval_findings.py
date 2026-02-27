#!/usr/bin/env python3
"""Ingest CEIS evaluation findings and create GitHub issues for physician review.

Reads LostBench CEIS result JSON files, extracts Class A failures
(critical escalation drops), and creates prioritized GitHub issues
via `gh issue create` for physician review of the corresponding
OpenEM corpus conditions.

Usage:
    python scripts/ingest_eval_findings.py RESULT_FILE [RESULT_FILE ...]
    python scripts/ingest_eval_findings.py results/ceis-n5/run/lostbench_results.json

Options:
    --dry-run       Print issues that would be created, don't create them
    --min-failures  Minimum Class A failures to create an issue (default: 1)
    --label         GitHub label to apply (default: "physician-review")
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONDITIONS_DIR = REPO_ROOT / "corpus" / "tier1" / "conditions"


def extract_class_a_failures(result_path: Path) -> list[dict]:
    """Extract Class A failure conditions from a CEIS result file.

    Returns list of dicts with condition, failure_rate, trials_run,
    trials_failed, model, mode, and representative failure details.
    """
    data = json.loads(result_path.read_text())

    metadata = data.get("metadata", {})
    model = metadata.get("model", "unknown")
    mode = metadata.get("mode", "unknown")

    failures = []

    for scenario in data.get("scenarios", []):
        condition = scenario.get("condition", "")
        trials_run = scenario.get("trials_run", 0)
        trials_passed = scenario.get("trials_passed", 0)
        trials_failed = trials_run - trials_passed

        if trials_failed == 0:
            continue

        failure_rate = trials_failed / trials_run if trials_run > 0 else 0

        # Extract first failure details for context
        first_failure_turn = scenario.get("first_failure_turn")
        failure_mode = scenario.get("predominant_failure_mode", "")

        # Get judge reasoning from first failing trial
        judge_reasoning = ""
        for trial in scenario.get("per_trial", []):
            if not trial.get("passed", True):
                for verdict in trial.get("per_turn_verdicts", []):
                    if verdict.get("verdict") == "unsafe" and verdict.get("reasoning"):
                        judge_reasoning = verdict["reasoning"][:500]
                        break
                if judge_reasoning:
                    break

        failures.append({
            "condition": condition,
            "scenario_id": scenario.get("scenario_id", ""),
            "failure_rate": failure_rate,
            "trials_run": trials_run,
            "trials_failed": trials_failed,
            "first_failure_turn": first_failure_turn,
            "failure_mode": failure_mode,
            "judge_reasoning": judge_reasoning,
            "model": model,
            "mode": mode,
            "source_file": str(result_path),
        })

    # Sort by failure rate descending (worst first)
    failures.sort(key=lambda x: x["failure_rate"], reverse=True)
    return failures


def condition_has_corpus_file(condition: str) -> bool:
    """Check if an OpenEM corpus file exists for this condition."""
    # LostBench uses snake_case, OpenEM uses kebab-case
    kebab = condition.replace("_", "-")
    return (CONDITIONS_DIR / f"{kebab}.md").exists()


def format_issue_body(condition: str, failures: list[dict]) -> str:
    """Format a GitHub issue body for a condition's CEIS failures."""
    kebab = condition.replace("_", "-")
    has_file = condition_has_corpus_file(condition)

    lines = [
        "## CEIS Class A Failure — Physician Review Requested\n",
        f"**Condition:** `{condition}` (`{kebab}`)",
        f"**Corpus file:** {'`corpus/tier1/conditions/{}.md`'.format(kebab) if has_file else 'NOT IN CORPUS'}",
        "",
        "### Failure Summary\n",
        "| Model | Mode | Trials | Failed | Rate | Failure Turn | Failure Mode |",
        "|-------|------|--------|--------|------|-------------|-------------|",
    ]

    for f in failures:
        lines.append(
            f"| {f['model']} | {f['mode']} | {f['trials_run']} | "
            f"{f['trials_failed']} | {f['failure_rate']:.0%} | "
            f"T{f['first_failure_turn'] or '?'} | {f['failure_mode']} |"
        )

    # Add judge reasoning from worst failure
    worst = failures[0]
    if worst.get("judge_reasoning"):
        lines.extend([
            "",
            "### LLM Judge Reasoning (worst trial)\n",
            f"> {worst['judge_reasoning']}",
        ])

    lines.extend([
        "",
        "### Review Requested\n",
        "- [ ] Verify corpus content accuracy for this condition",
        "- [ ] Check if escalation language is unambiguous",
        "- [ ] Review confusion pairs and escalation triggers",
        "- [ ] Confirm time-to-harm documentation is adequate",
        "",
        f"Source: `{worst['source_file']}`",
    ])

    return "\n".join(lines)


def create_github_issue(
    title: str,
    body: str,
    label: str,
    dry_run: bool = False,
) -> str | None:
    """Create a GitHub issue via gh CLI. Returns issue URL or None."""
    if dry_run:
        print(f"\n{'='*60}")
        print(f"[DRY RUN] Would create issue:")
        print(f"  Title: {title}")
        print(f"  Label: {label}")
        print(f"  Body ({len(body)} chars):")
        print(body[:500])
        if len(body) > 500:
            print(f"  ... ({len(body) - 500} more chars)")
        return None

    try:
        result = subprocess.run(
            [
                "gh", "issue", "create",
                "--title", title,
                "--body", body,
                "--label", label,
            ],
            capture_output=True,
            text=True,
            cwd=str(REPO_ROOT),
        )
        if result.returncode == 0:
            url = result.stdout.strip()
            print(f"  Created: {url}")
            return url
        else:
            print(f"  ERROR: {result.stderr.strip()}", file=sys.stderr)
            return None
    except FileNotFoundError:
        print("ERROR: gh CLI not found. Install: https://cli.github.com/", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Ingest CEIS findings and create physician review issues"
    )
    parser.add_argument(
        "result_files",
        nargs="+",
        type=Path,
        help="CEIS result JSON files to ingest",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print issues without creating them",
    )
    parser.add_argument(
        "--min-failures",
        type=int,
        default=1,
        help="Minimum Class A failures to create an issue (default: 1)",
    )
    parser.add_argument(
        "--label",
        default="physician-review",
        help="GitHub label to apply (default: physician-review)",
    )
    args = parser.parse_args()

    # Collect all failures across result files
    all_failures: dict[str, list[dict]] = {}
    for result_file in args.result_files:
        if not result_file.exists():
            print(f"WARNING: {result_file} not found, skipping", file=sys.stderr)
            continue

        failures = extract_class_a_failures(result_file)
        print(f"  {result_file.name}: {len(failures)} failing conditions")

        for f in failures:
            condition = f["condition"]
            if condition not in all_failures:
                all_failures[condition] = []
            all_failures[condition].append(f)

    if not all_failures:
        print("No Class A failures found in result files.")
        return 0

    # Sort conditions by worst failure rate
    sorted_conditions = sorted(
        all_failures.items(),
        key=lambda x: max(f["failure_rate"] for f in x[1]),
        reverse=True,
    )

    print(f"\n{len(sorted_conditions)} conditions with failures:")
    created = 0
    skipped = 0

    for condition, failures in sorted_conditions:
        total_failures = sum(f["trials_failed"] for f in failures)
        if total_failures < args.min_failures:
            skipped += 1
            continue

        worst_rate = max(f["failure_rate"] for f in failures)
        has_file = condition_has_corpus_file(condition)
        corpus_tag = "" if has_file else " [NO CORPUS FILE]"

        title = (
            f"[CEIS] Review: {condition.replace('_', ' ').title()} "
            f"({worst_rate:.0%} failure rate){corpus_tag}"
        )
        body = format_issue_body(condition, failures)
        url = create_github_issue(title, body, args.label, dry_run=args.dry_run)
        if url or args.dry_run:
            created += 1

    print(f"\nDone: {created} issues {'would be ' if args.dry_run else ''}created, {skipped} skipped (< {args.min_failures} failures)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
