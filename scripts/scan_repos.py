#!/usr/bin/env python3
"""Scan downstream repos for condition-level clinical insights.

Reads evaluation findings from LostBench, RadSlice, SafeShift, and
ScribeGoat2, then proposes enrichments to OpenEM condition records.

Never auto-writes to condition files. Outputs a report for human review.

Usage:
    python scripts/scan_repos.py                      # Scan all known repos
    python scripts/scan_repos.py --repo lostbench     # Scan one repo
    python scripts/scan_repos.py --dry-run             # Print report only
    python scripts/scan_repos.py --format json         # JSON output
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

# Import openem.insights directly to avoid lancedb dependency from openem.__init__
_python_dir = str(Path(__file__).resolve().parent.parent / "python")
if _python_dir not in sys.path:
    sys.path.insert(0, _python_dir)

_spec = importlib.util.spec_from_file_location(
    "openem.insights", Path(_python_dir) / "openem" / "insights.py"
)
_insights = importlib.util.module_from_spec(_spec)
sys.modules["openem.insights"] = _insights
_spec.loader.exec_module(_insights)

ConditionInsight = _insights.ConditionInsight
InsightAggregator = _insights.InsightAggregator
format_report = _insights.format_report
format_report_json = _insights.format_report_json
parse_lostbench_seeds = _insights.parse_lostbench_seeds

# Registry of known downstream repos
REPO_REGISTRY: dict[str, dict] = {
    "lostbench": {
        "path": Path.home() / "lostbench",
        "parser": "parse_lostbench",
    },
    "radslice": {
        "path": Path.home() / "radslice",
        "parser": "parse_radslice",
    },
    "safeshift": {
        "path": Path.home() / "safeshift",
        "parser": "parse_safeshift",
    },
    "scribegoat2": {
        "path": Path.home() / "scribegoat2",
        "parser": "parse_scribegoat2",
    },
    "healthcraft": {
        "path": Path.home() / "healthcraft",
        "parser": "parse_healthcraft",
    },
}


def parse_lostbench(repo_path: Path) -> list[ConditionInsight]:
    """Parse LostBench for condition insights."""
    insights: list[ConditionInsight] = []

    # Parse seeds persistence findings
    seeds_path = repo_path / "SEEDS_PERSISTENCE_FINDINGS.md"
    if seeds_path.exists():
        insights.extend(parse_lostbench_seeds(seeds_path))

    # Parse scenario YAMLs for condition → pressure type mapping
    scenario_dirs = [
        repo_path / "src" / "lostbench" / "scenarios" / "tier1",
        repo_path / "src" / "lostbench" / "scenarios" / "tier1_codeagent",
        repo_path / "src" / "lostbench" / "scenarios" / "tier1_adversarial",
    ]
    for scenario_dir in scenario_dirs:
        if scenario_dir.exists():
            insights.extend(_parse_lostbench_scenarios(scenario_dir))

    return insights


def _parse_lostbench_scenarios(
    scenario_dir: Path,
) -> list[ConditionInsight]:
    """Parse LostBench scenario YAMLs for condition metadata."""
    try:
        import yaml
    except ImportError:
        return []

    insights = []
    for yaml_path in sorted(scenario_dir.glob("*.yaml")):
        try:
            with open(yaml_path) as f:
                data = yaml.safe_load(f)
        except Exception:
            continue

        if not data or "condition" not in data:
            continue

        condition_snake = data["condition"]
        condition_id = condition_snake.replace("_", "-")

        pressure_types = []
        for pressure in data.get("pressure", []):
            ptype = pressure.get("type")
            if ptype:
                pressure_types.append(ptype)

        if pressure_types:
            insights.append(
                ConditionInsight(
                    condition_id=condition_id,
                    source_repo="lostbench",
                    source_file=f"scenarios/{scenario_dir.name}/{yaml_path.name}",
                    pressure_vulnerability=list(set(pressure_types)),
                )
            )

    return insights


def parse_radslice(repo_path: Path) -> list[ConditionInsight]:
    """Parse RadSlice for condition imaging metadata."""
    try:
        import yaml
    except ImportError:
        return []

    insights = []
    task_dirs = [
        repo_path / "configs" / "tasks" / modality
        for modality in ["xray", "ct", "mri", "ultrasound"]
    ]

    # Collect modalities per condition
    condition_modalities: dict[str, set[str]] = {}
    for task_dir in task_dirs:
        if not task_dir.exists():
            continue
        modality = task_dir.name
        for yaml_path in sorted(task_dir.glob("*.yaml")):
            try:
                with open(yaml_path) as f:
                    data = yaml.safe_load(f)
            except Exception:
                continue

            if not data or "condition_id" not in data:
                continue

            cid = data["condition_id"]
            if cid not in condition_modalities:
                condition_modalities[cid] = set()
            condition_modalities[cid].add(modality)

    for cid, modalities in sorted(condition_modalities.items()):
        insights.append(
            ConditionInsight(
                condition_id=cid,
                source_repo="radslice",
                source_file="configs/tasks/",
                diagnostic_imaging={
                    "modalities": sorted(modalities),
                },
            )
        )

    return insights


def parse_safeshift(repo_path: Path) -> list[ConditionInsight]:
    """Parse SafeShift for condition insights. Stub — no condition_ids yet."""
    return []


def parse_scribegoat2(repo_path: Path) -> list[ConditionInsight]:
    """Parse ScribeGoat2 FINDINGS.md for per-condition violation rates."""
    findings_path = repo_path / "experiments" / "FINDINGS.md"
    if not findings_path.exists():
        return []

    # Placeholder — would parse FINDINGS.md for condition-level data
    # Currently returns empty list; full parser deferred until
    # FINDINGS.md format stabilizes
    return []


def parse_healthcraft(repo_path: Path) -> list[ConditionInsight]:
    """Parse HealthCraft V7 evaluation data for per-condition insights.

    Reads task YAMLs for openem_condition mappings, then aggregates
    trajectory results per condition across both models and all trials.
    """
    try:
        import yaml
    except ImportError:
        return []

    # Step 1: Build task_id → openem_condition mapping from task YAMLs
    task_conditions: dict[str, str] = {}
    tasks_dir = repo_path / "configs" / "tasks"
    if not tasks_dir.exists():
        return []

    for category_dir in sorted(tasks_dir.iterdir()):
        if not category_dir.is_dir():
            continue
        for yaml_path in sorted(category_dir.glob("*.yaml")):
            try:
                with open(yaml_path) as f:
                    data = yaml.safe_load(f)
            except Exception:
                continue

            if not data or "id" not in data:
                continue

            task_id = data["id"]
            condition = (data.get("metadata") or {}).get("openem_condition")
            if condition and condition != "null":
                task_conditions[task_id] = condition

    if not task_conditions:
        return []

    # Step 2: Aggregate trajectory results per condition
    # Structure: condition → {model → [trajectory results]}
    condition_results: dict[str, dict[str, list[dict]]] = {}

    model_dirs = {
        "claude": "pilot-v7-claude-opus",
        "gpt": "pilot-v7-gpt54",
    }

    for model_key, dir_name in model_dirs.items():
        results_dir = repo_path / "results" / dir_name / "trajectories"
        if not results_dir.exists():
            continue

        for category_dir in sorted(results_dir.iterdir()):
            if not category_dir.is_dir():
                continue
            for traj_path in sorted(category_dir.glob("*.json")):
                try:
                    with open(traj_path) as f:
                        traj = json.load(f)
                except Exception:
                    continue

                task_id = traj.get("task_id")
                if not task_id or task_id not in task_conditions:
                    continue

                condition = task_conditions[task_id]
                if condition not in condition_results:
                    condition_results[condition] = {}
                if model_key not in condition_results[condition]:
                    condition_results[condition][model_key] = []

                condition_results[condition][model_key].append(
                    {
                        "passed": traj.get("passed", False),
                        "safety_gate_passed": traj.get("safety_gate_passed", True),
                        "reward": traj.get("reward", 0.0),
                        "total_tool_calls": traj.get("total_tool_calls", 0),
                    }
                )

    # Step 3: Compute per-condition metrics and create insights
    insights: list[ConditionInsight] = []

    for condition, model_data in sorted(condition_results.items()):
        # Convert HC snake_case to hyphenated condition_id
        condition_id = condition.replace("_", "-")

        # Aggregate across all models and trials
        all_trials = []
        for trials in model_data.values():
            all_trials.extend(trials)

        total = len(all_trials)
        if total == 0:
            continue

        safety_failures = sum(1 for t in all_trials if not t["safety_gate_passed"])
        safety_failure_rate = safety_failures / total

        # Per-model pass rates for divergence
        claude_trials = model_data.get("claude", [])
        gpt_trials = model_data.get("gpt", [])

        claude_pass_rate = (
            sum(1 for t in claude_trials if t["passed"]) / len(claude_trials)
            if claude_trials
            else 0.0
        )
        gpt_pass_rate = (
            sum(1 for t in gpt_trials if t["passed"]) / len(gpt_trials)
            if gpt_trials
            else 0.0
        )
        model_divergence = claude_pass_rate - gpt_pass_rate

        # Unsolved: both models fail all trials
        all_fail = all(not t["passed"] for t in all_trials)

        insights.append(
            ConditionInsight(
                condition_id=condition_id,
                source_repo="healthcraft",
                source_file=f"results/pilot-v7 ({condition})",
                safety_failure_rate=round(safety_failure_rate, 3),
                model_divergence=round(model_divergence, 3),
                unsolved=all_fail if all_fail else None,
            )
        )

    return insights


# Parser dispatch
PARSERS = {
    "lostbench": parse_lostbench,
    "radslice": parse_radslice,
    "safeshift": parse_safeshift,
    "scribegoat2": parse_scribegoat2,
    "healthcraft": parse_healthcraft,
}


def load_risk_tiers(corpus_dir: Path) -> dict[str, str]:
    """Load risk_tier for each condition from corpus frontmatter."""
    try:
        import yaml
    except ImportError:
        return {}

    tiers = {}
    conditions_dir = corpus_dir / "corpus" / "tier1" / "conditions"
    if not conditions_dir.exists():
        return tiers

    for md_path in sorted(conditions_dir.glob("*.md")):
        try:
            text = md_path.read_text()
            # Extract frontmatter
            if text.startswith("---"):
                end = text.index("---", 3)
                frontmatter = yaml.safe_load(text[3:end])
                if frontmatter and "id" in frontmatter and "risk_tier" in frontmatter:
                    tiers[frontmatter["id"]] = frontmatter["risk_tier"]
        except Exception:
            continue

    return tiers


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scan downstream repos for condition-level insights"
    )
    parser.add_argument(
        "--repo",
        choices=list(REPO_REGISTRY.keys()),
        help="Scan only this repo (default: all)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print report only, don't write files",
    )
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)",
    )
    parser.add_argument(
        "--output",
        help="Write report to file instead of stdout",
    )

    args = parser.parse_args()

    repos_to_scan = [args.repo] if args.repo else list(REPO_REGISTRY.keys())

    aggregator = InsightAggregator()
    scanned = []
    skipped = []

    for repo_name in repos_to_scan:
        repo_info = REPO_REGISTRY[repo_name]
        repo_path = repo_info["path"]

        if not repo_path.exists():
            skipped.append(f"{repo_name} (not found at {repo_path})")
            continue

        parser_fn = PARSERS.get(repo_name)
        if not parser_fn:
            skipped.append(f"{repo_name} (no parser)")
            continue

        insights = parser_fn(repo_path)
        for insight in insights:
            aggregator.add(insight)

        scanned.append(repo_name)
        print(f"Scanned {repo_name}: {len(insights)} insight(s)", file=sys.stderr)

    proposals = aggregator.merge_all()

    # Load risk tiers for report context
    repo_root = Path(__file__).resolve().parent.parent
    risk_tiers = load_risk_tiers(repo_root)

    if args.format == "json":
        output = format_report_json(proposals, scanned)
    else:
        output = format_report(
            proposals,
            scanned,
            skipped,
            risk_tiers=risk_tiers,
        )

    if args.output:
        output_path = Path(args.output)
        output_path.write_text(output)
        print(f"Report written to {output_path}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
