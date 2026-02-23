#!/usr/bin/env python3
"""Analyze impact of corpus changes on evaluation metrics.

Reads run_log.jsonl and correlates corpus additions with metric deltas.

Groups experiments by:
  - baseline vs RAG (task names containing 'rag' vs matching baselines)
  - before vs after corpus milestones (by timestamp)

Outputs a summary table to stdout.

Usage:
    python scripts/analyze_impact.py --run-log /path/to/run_log.jsonl
    python scripts/analyze_impact.py --run-log /path/to/run_log.jsonl --json
    python scripts/analyze_impact.py  # defaults to scribegoat2 run_log
"""

import argparse
import json
import math
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

# Default run log path (scribegoat2 canonical location)
DEFAULT_RUN_LOG = (
    Path(__file__).resolve().parent.parent.parent / "scribegoat2" / "experiments" / "run_log.jsonl"
)

# Corpus milestone dates (add more as corpus grows)
CORPUS_MILESTONES = [
    {
        "name": "openem_initial_128_conditions",
        "date": "2026-02-18T00:00:00+00:00",
        "description": "OpenEM corpus v1: 128 conditions compiled",
    },
]


# ---- Parsing ----

def load_run_log(path: Path) -> list[dict]:
    """Parse JSONL run log. Skip malformed lines with a warning."""
    entries = []
    with path.open() as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"  WARNING: line {i} malformed — {e}", file=sys.stderr)
    return entries


# ---- Metric extraction ----

def extract_pass_k(entry: dict, model: str) -> float | None:
    """Extract pass^k from a run log entry for a given model."""
    results = entry.get("results", {})
    model_results = results.get(model, {})

    # Direct pass_k field
    if "pass_k" in model_results:
        return float(model_results["pass_k"])

    # Compute from pass / total
    passed = model_results.get("pass", model_results.get("enforced_pass"))
    total = model_results.get("total", model_results.get("enforced_total"))
    if passed is not None and total and total > 0:
        return passed / total

    # success_rate field
    if "success_rate" in model_results:
        return float(model_results["success_rate"])

    return None


def extract_ers(entry: dict, model: str) -> int | None:
    """Extract ERS score if present."""
    results = entry.get("results", {})
    model_results = results.get(model, {})
    return model_results.get("ers") or model_results.get("ERS")


def parse_ts(ts_str: str) -> datetime | None:
    """Parse ISO timestamp string."""
    if not ts_str:
        return None
    try:
        # Handle both Z and +00:00 suffixes
        ts_str = ts_str.replace("Z", "+00:00")
        return datetime.fromisoformat(ts_str)
    except (ValueError, TypeError):
        return None


# ---- Grouping ----

def is_rag_experiment(entry: dict) -> bool:
    """Heuristic: experiment uses RAG/corpus grounding."""
    task = entry.get("task", "").lower()
    notes = entry.get("notes", "").lower()
    tags = entry.get("tags", [])
    return (
        "rag" in task
        or "openem" in task
        or "corpus" in task
        or "rag" in notes
        or "openem" in notes
        or "rag" in tags
    )


def get_models(entry: dict) -> list[str]:
    return entry.get("models", [])


def milestone_phase(ts: datetime | None) -> str:
    """Return 'pre-corpus' or 'post-corpus' relative to the first OpenEM milestone."""
    if ts is None:
        return "unknown"
    cutoff = parse_ts(CORPUS_MILESTONES[0]["date"])
    if cutoff and ts < cutoff:
        return "pre-corpus"
    return "post-corpus"


# ---- Analysis ----

def analyze_baseline_vs_rag(entries: list[dict]) -> dict:
    """Compare baseline vs RAG pass^k per model."""
    baseline_by_model: dict[str, list[float]] = defaultdict(list)
    rag_by_model: dict[str, list[float]] = defaultdict(list)

    for entry in entries:
        rag = is_rag_experiment(entry)
        for model in get_models(entry):
            pk = extract_pass_k(entry, model)
            if pk is not None:
                if rag:
                    rag_by_model[model].append(pk)
                else:
                    baseline_by_model[model].append(pk)

    all_models = sorted(set(list(baseline_by_model) + list(rag_by_model)))
    rows = []
    for model in all_models:
        bl_vals = baseline_by_model.get(model, [])
        rag_vals = rag_by_model.get(model, [])
        bl_mean = sum(bl_vals) / len(bl_vals) if bl_vals else None
        rag_mean = sum(rag_vals) / len(rag_vals) if rag_vals else None
        delta = (rag_mean - bl_mean) if (bl_mean is not None and rag_mean is not None) else None
        rows.append({
            "model": model,
            "baseline_n": len(bl_vals),
            "baseline_mean_pass_k": round(bl_mean, 4) if bl_mean is not None else None,
            "rag_n": len(rag_vals),
            "rag_mean_pass_k": round(rag_mean, 4) if rag_mean is not None else None,
            "delta_pp": round(delta, 4) if delta is not None else None,
            "direction": (
                "improvement" if delta and delta > 0.01
                else "regression" if delta and delta < -0.01
                else "neutral" if delta is not None
                else "insufficient_data"
            ),
        })

    return {"by_model": rows}


def analyze_pre_post_corpus(entries: list[dict]) -> dict:
    """Compare pre-corpus vs post-corpus metrics for all experiments."""
    pre_by_model: dict[str, list[float]] = defaultdict(list)
    post_by_model: dict[str, list[float]] = defaultdict(list)

    for entry in entries:
        ts = parse_ts(entry.get("ts", ""))
        phase = milestone_phase(ts)
        for model in get_models(entry):
            pk = extract_pass_k(entry, model)
            if pk is not None:
                if phase == "pre-corpus":
                    pre_by_model[model].append(pk)
                elif phase == "post-corpus":
                    post_by_model[model].append(pk)

    all_models = sorted(set(list(pre_by_model) + list(post_by_model)))
    rows = []
    for model in all_models:
        pre_vals = pre_by_model.get(model, [])
        post_vals = post_by_model.get(model, [])
        pre_mean = sum(pre_vals) / len(pre_vals) if pre_vals else None
        post_mean = sum(post_vals) / len(post_vals) if post_vals else None
        delta = (post_mean - pre_mean) if (pre_mean is not None and post_mean is not None) else None
        rows.append({
            "model": model,
            "pre_corpus_n": len(pre_vals),
            "pre_corpus_mean_pass_k": round(pre_mean, 4) if pre_mean is not None else None,
            "post_corpus_n": len(post_vals),
            "post_corpus_mean_pass_k": round(post_mean, 4) if post_mean is not None else None,
            "delta_pp": round(delta, 4) if delta is not None else None,
        })

    return {
        "corpus_milestone": CORPUS_MILESTONES[0]["description"],
        "cutoff_date": CORPUS_MILESTONES[0]["date"],
        "by_model": rows,
    }


def analyze_rag_experiments_detail(entries: list[dict]) -> list[dict]:
    """Return details for all RAG experiments, sorted by timestamp."""
    rag_entries = [e for e in entries if is_rag_experiment(e)]
    rag_entries.sort(key=lambda e: e.get("ts", ""))

    rows = []
    for entry in rag_entries:
        row = {
            "id": entry.get("id", "?"),
            "ts": entry.get("ts", ""),
            "task": entry.get("task", ""),
            "scorer": entry.get("scorer", ""),
            "n_scenarios": entry.get("n_scenarios"),
            "n_trials": entry.get("n_trials"),
            "models": get_models(entry),
            "metrics_per_model": {},
            "notes": entry.get("notes", ""),
        }
        for model in get_models(entry):
            pk = extract_pass_k(entry, model)
            ers = extract_ers(entry, model)
            row["metrics_per_model"][model] = {
                "pass_k": pk,
                "ers": ers,
            }
        rows.append(row)

    return rows


def compute_corpus_lift_summary(entries: list[dict]) -> dict:
    """
    Find explicit baseline/RAG experiment pairs and compute lift.

    Pairs are detected by:
    - Same model
    - One has 'rag' in task, one does not
    - Similar n_scenarios / n_trials
    - RAG experiment notes reference 'OpenEM' or 'corpus'
    """
    rag_entries = [e for e in entries if is_rag_experiment(e)]
    baseline_entries = [e for e in entries if not is_rag_experiment(e)]

    pairs_found = []
    for rag_e in rag_entries:
        rag_ts = parse_ts(rag_e.get("ts", ""))
        rag_scenarios = rag_e.get("n_scenarios")
        rag_trials = rag_e.get("n_trials")
        rag_models = set(get_models(rag_e))

        for bl_e in baseline_entries:
            bl_ts = parse_ts(bl_e.get("ts", ""))
            bl_models = set(get_models(bl_e))
            bl_scenarios = bl_e.get("n_scenarios")
            bl_trials = bl_e.get("n_trials")

            # Must share at least one model
            shared_models = rag_models & bl_models
            if not shared_models:
                continue

            # RAG experiment must come after baseline
            if rag_ts and bl_ts and rag_ts <= bl_ts:
                continue

            # Scenarios/trials should match (within factor of 2)
            if rag_scenarios and bl_scenarios:
                if not (0.5 <= rag_scenarios / bl_scenarios <= 2.0):
                    continue

            for model in sorted(shared_models):
                bl_pk = extract_pass_k(bl_e, model)
                rag_pk = extract_pass_k(rag_e, model)
                if bl_pk is None or rag_pk is None:
                    continue

                delta = rag_pk - bl_pk
                pairs_found.append({
                    "model": model,
                    "baseline_id": bl_e.get("id", "?"),
                    "rag_id": rag_e.get("id", "?"),
                    "baseline_task": bl_e.get("task", ""),
                    "rag_task": rag_e.get("task", ""),
                    "baseline_pass_k": round(bl_pk, 4),
                    "rag_pass_k": round(rag_pk, 4),
                    "delta_pp": round(delta, 4),
                    "lift_pct": round(delta / bl_pk * 100, 1) if bl_pk > 0 else None,
                })

    # Sort by delta descending
    pairs_found.sort(key=lambda x: x["delta_pp"], reverse=True)
    return {"explicit_pairs": pairs_found}


def render_table(rows: list[dict], columns: list[str], title: str) -> str:
    """Render a list of dicts as an ASCII table."""
    if not rows:
        return f"\n{title}\n  (no data)\n"

    lines = [f"\n{title}"]
    lines.append("-" * min(120, max(len(title), 80)))

    # Compute column widths
    widths = {col: len(col) for col in columns}
    for row in rows:
        for col in columns:
            val = row.get(col, "")
            widths[col] = max(widths[col], len(str(val) if val is not None else "-"))

    # Header
    header = "  ".join(col.ljust(widths[col]) for col in columns)
    lines.append(header)
    lines.append("  ".join("-" * widths[col] for col in columns))

    # Rows
    for row in rows:
        line = "  ".join(
            str(row.get(col, "-") if row.get(col) is not None else "-").ljust(widths[col])
            for col in columns
        )
        lines.append(line)

    return "\n".join(lines)


# ---- Main ----

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Analyze impact of corpus changes on evaluation metrics."
    )
    parser.add_argument(
        "--run-log",
        type=Path,
        default=DEFAULT_RUN_LOG,
        help=f"Path to run_log.jsonl (default: {DEFAULT_RUN_LOG})",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output full JSON report instead of summary table",
    )
    args = parser.parse_args()

    run_log_path: Path = args.run_log
    if not run_log_path.exists():
        print(f"ERROR: run_log.jsonl not found at {run_log_path}", file=sys.stderr)
        print(
            "Pass --run-log /path/to/run_log.jsonl to specify location.",
            file=sys.stderr,
        )
        return 1

    print(f"Loading run log: {run_log_path}", file=sys.stderr)
    entries = load_run_log(run_log_path)
    print(f"Parsed {len(entries)} log entries", file=sys.stderr)

    # Run analyses
    baseline_vs_rag = analyze_baseline_vs_rag(entries)
    pre_post = analyze_pre_post_corpus(entries)
    rag_detail = analyze_rag_experiments_detail(entries)
    lift_summary = compute_corpus_lift_summary(entries)

    report = {
        "run_log": str(run_log_path),
        "total_entries": len(entries),
        "rag_experiment_count": len(rag_detail),
        "corpus_milestones": CORPUS_MILESTONES,
        "baseline_vs_rag": baseline_vs_rag,
        "pre_post_corpus": pre_post,
        "explicit_pair_lifts": lift_summary,
        "rag_experiments": rag_detail,
    }

    if args.json:
        print(json.dumps(report, indent=2))
        return 0

    # Human-readable summary tables
    print(f"\n{'='*70}")
    print("OpenEM Corpus Impact Analysis")
    print(f"Run log: {run_log_path}")
    print(f"Total experiments: {len(entries)}  |  RAG experiments: {len(rag_detail)}")
    print(f"{'='*70}")

    # Table 1: Baseline vs RAG by model
    t1_cols = [
        "model", "baseline_n", "baseline_mean_pass_k",
        "rag_n", "rag_mean_pass_k", "delta_pp", "direction",
    ]
    print(render_table(baseline_vs_rag["by_model"], t1_cols, "Table 1: Baseline vs RAG (all experiments, by model)"))

    # Table 2: Pre- vs post-corpus by model
    t2_cols = [
        "model",
        "pre_corpus_n", "pre_corpus_mean_pass_k",
        "post_corpus_n", "post_corpus_mean_pass_k",
        "delta_pp",
    ]
    print(render_table(
        pre_post["by_model"],
        t2_cols,
        f"Table 2: Pre- vs Post-Corpus ({pre_post['cutoff_date'][:10]})",
    ))

    # Table 3: Explicit baseline/RAG pairs
    t3_cols = [
        "model", "baseline_id", "rag_id",
        "baseline_pass_k", "rag_pass_k", "delta_pp", "lift_pct",
    ]
    print(render_table(
        lift_summary["explicit_pairs"],
        t3_cols,
        "Table 3: Explicit Baseline/RAG Pairs (matched by model + scenario count)",
    ))

    # Table 4: RAG experiment details
    rag_flat = []
    for r in rag_detail:
        for model, metrics in r["metrics_per_model"].items():
            rag_flat.append({
                "id": r["id"],
                "date": r["ts"][:10] if r["ts"] else "?",
                "model": model,
                "pass_k": metrics.get("pass_k"),
                "ers": metrics.get("ers"),
                "n_scenarios": r.get("n_scenarios"),
                "task": r.get("task", "")[:40],
            })

    t4_cols = ["id", "date", "model", "pass_k", "ers", "n_scenarios", "task"]
    print(render_table(rag_flat, t4_cols, "Table 4: RAG Experiment Details"))

    print(f"\n{'='*70}\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
