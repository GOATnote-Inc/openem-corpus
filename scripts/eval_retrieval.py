#!/usr/bin/env python3
"""Evaluate retrieval quality against ground truth.

Metrics: Recall@k, MRR, Precision@k, Condition accuracy.

Usage:
    python scripts/eval_retrieval.py [--ground-truth PATH] [--top-k N] [--mode MODE]

Defaults:
    --ground-truth  evaluation/retrieval_ground_truth.jsonl
    --top-k         5
    --mode          hybrid
"""

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "python"))

from openem.index import OpenEMIndex

DEFAULT_GROUND_TRUTH = REPO_ROOT / "evaluation" / "retrieval_ground_truth.jsonl"
DEFAULT_INDEX_DIR = REPO_ROOT / "data" / "index"


def load_ground_truth(path: Path) -> list[dict]:
    """Load JSONL ground truth file."""
    records = []
    with path.open() as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(
                    f"WARNING: Skipping malformed line {line_num}: {e}", file=sys.stderr
                )
    return records


def recall_at_k(retrieved_ids: list[str], expected_ids: list[str]) -> float:
    """Fraction of expected condition_ids found in retrieved results."""
    if not expected_ids:
        return 1.0
    found = sum(1 for eid in expected_ids if eid in retrieved_ids)
    return found / len(expected_ids)


def precision_at_k(retrieved_ids: list[str], expected_ids: list[str]) -> float:
    """Fraction of retrieved results that are relevant."""
    if not retrieved_ids:
        return 0.0
    relevant = sum(1 for rid in retrieved_ids if rid in expected_ids)
    return relevant / len(retrieved_ids)


def reciprocal_rank(retrieved_ids: list[str], expected_ids: list[str]) -> float:
    """Reciprocal rank of first relevant result (for MRR computation)."""
    for rank, rid in enumerate(retrieved_ids, 1):
        if rid in expected_ids:
            return 1.0 / rank
    return 0.0


def section_recall(
    retrieved_sections: list[str], expected_sections: list[str]
) -> float:
    """Fraction of expected sections found in retrieved chunks.

    Handles sub-section names (e.g., 'Treatment > Pain Management') by checking
    if the parent section matches.
    """
    if not expected_sections:
        return 1.0

    def section_matches(retrieved: str, expected: str) -> bool:
        parent = retrieved.split(" > ")[0] if " > " in retrieved else retrieved
        return parent == expected or retrieved == expected

    found = 0
    for exp_sec in expected_sections:
        if any(section_matches(ret_sec, exp_sec) for ret_sec in retrieved_sections):
            found += 1
    return found / len(expected_sections)


def evaluate_query(
    index: OpenEMIndex,
    record: dict,
    top_k: int,
    mode: str,
) -> dict:
    """Run a single query and compute per-query metrics."""
    query = record["query"]
    expected_ids = record.get("expected_condition_ids", [])
    expected_sections = record.get("expected_sections", [])
    scenario_type = record.get("scenario_type", "unknown")

    results = index.search(query, top_k=top_k, mode=mode)

    retrieved_ids = [r["condition_id"] for r in results]
    retrieved_sections = [r["section"] for r in results]

    rec = recall_at_k(retrieved_ids, expected_ids)
    prec = precision_at_k(retrieved_ids, expected_ids)
    rr = reciprocal_rank(retrieved_ids, expected_ids)
    sec_rec = section_recall(retrieved_sections, expected_sections)

    # Condition accuracy: at least one expected condition_id in top-1
    top1_hit = bool(retrieved_ids) and retrieved_ids[0] in expected_ids

    return {
        "query": query,
        "scenario_type": scenario_type,
        "expected_ids": expected_ids,
        "retrieved_ids": retrieved_ids,
        "recall": rec,
        "precision": prec,
        "reciprocal_rank": rr,
        "section_recall": sec_rec,
        "top1_hit": top1_hit,
        "num_results": len(results),
    }


def aggregate_metrics(per_query: list[dict]) -> dict:
    """Aggregate per-query metrics into summary statistics."""
    n = len(per_query)
    if n == 0:
        return {}

    def mean(values):
        return sum(values) / len(values)

    recalls = [r["recall"] for r in per_query]
    precisions = [r["precision"] for r in per_query]
    rrs = [r["reciprocal_rank"] for r in per_query]
    sec_recalls = [r["section_recall"] for r in per_query]
    top1_hits = [r["top1_hit"] for r in per_query]

    # Per scenario type
    scenario_types = sorted(set(r["scenario_type"] for r in per_query))
    by_scenario = {}
    for stype in scenario_types:
        subset = [r for r in per_query if r["scenario_type"] == stype]
        by_scenario[stype] = {
            "n": len(subset),
            "recall": mean([r["recall"] for r in subset]),
            "precision": mean([r["precision"] for r in subset]),
            "mrr": mean([r["reciprocal_rank"] for r in subset]),
            "section_recall": mean([r["section_recall"] for r in subset]),
            "top1_accuracy": mean([r["top1_hit"] for r in subset]),
        }

    return {
        "n": n,
        "recall": mean(recalls),
        "precision": mean(precisions),
        "mrr": mean(rrs),
        "section_recall": mean(sec_recalls),
        "top1_accuracy": mean(top1_hits),
        "by_scenario": by_scenario,
    }


def print_report(agg: dict, per_query: list[dict], verbose: bool = False) -> None:
    """Print formatted evaluation report."""
    print("\n" + "=" * 60)
    print("RETRIEVAL EVALUATION REPORT")
    print("=" * 60)
    print(f"  Queries evaluated : {agg['n']}")
    print(f"  Recall@k          : {agg['recall']:.3f}")
    print(f"  Precision@k       : {agg['precision']:.3f}")
    print(f"  MRR               : {agg['mrr']:.3f}")
    print(f"  Section Recall    : {agg['section_recall']:.3f}")
    print(f"  Top-1 Accuracy    : {agg['top1_accuracy']:.3f}")

    if agg.get("by_scenario"):
        print("\nBy scenario type:")
        for stype, metrics in agg["by_scenario"].items():
            print(f"  {stype} (n={metrics['n']})")
            print(
                f"    Recall={metrics['recall']:.3f}  Prec={metrics['precision']:.3f}  "
                f"MRR={metrics['mrr']:.3f}  SecRecall={metrics['section_recall']:.3f}  "
                f"Top1={metrics['top1_accuracy']:.3f}"
            )

    if verbose:
        print("\nPer-query detail:")
        print("-" * 60)
        for r in per_query:
            status = "OK" if r["recall"] >= 1.0 else "MISS"
            print(f"[{status}] ({r['scenario_type']}) {r['query'][:60]}")
            print(f"       expected: {r['expected_ids']}")
            print(f"       got:      {r['retrieved_ids']}")
            print(
                f"       recall={r['recall']:.2f}  prec={r['precision']:.2f}  "
                f"rr={r['reciprocal_rank']:.2f}  sec_recall={r['section_recall']:.2f}"
            )

    print("=" * 60 + "\n")


def main():
    parser = argparse.ArgumentParser(description="Evaluate OpenEM retrieval quality")
    parser.add_argument(
        "--ground-truth",
        type=Path,
        default=DEFAULT_GROUND_TRUTH,
        help=f"Ground truth JSONL file (default: {DEFAULT_GROUND_TRUTH})",
    )
    parser.add_argument(
        "--index",
        type=Path,
        default=DEFAULT_INDEX_DIR,
        help=f"OpenEM index directory (default: {DEFAULT_INDEX_DIR})",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=5,
        help="Number of results to retrieve per query (default: 5)",
    )
    parser.add_argument(
        "--mode",
        choices=["hybrid", "vector", "fts"],
        default="hybrid",
        help="Retrieval mode (default: hybrid)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print per-query detail",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Write JSON results to this file",
    )
    parser.add_argument(
        "--scenario",
        default=None,
        help="Filter to a single scenario type (escalation, defer, differential)",
    )
    args = parser.parse_args()

    # Load ground truth
    if not args.ground_truth.exists():
        print(
            f"ERROR: Ground truth file not found: {args.ground_truth}", file=sys.stderr
        )
        sys.exit(1)

    records = load_ground_truth(args.ground_truth)
    if not records:
        print("ERROR: No valid records in ground truth file", file=sys.stderr)
        sys.exit(1)

    # Optionally filter by scenario type
    if args.scenario:
        records = [r for r in records if r.get("scenario_type") == args.scenario]
        if not records:
            print(
                f"ERROR: No records with scenario_type={args.scenario!r}",
                file=sys.stderr,
            )
            sys.exit(1)

    print(f"Loaded {len(records)} queries from {args.ground_truth}")

    # Load index
    print(f"Loading OpenEM index from {args.index}...")
    try:
        index = OpenEMIndex(args.index)
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    manifest = index.manifest
    print(
        f"  Index: {manifest['num_conditions']} conditions, "
        f"{manifest['num_chunks']} chunks, "
        f"model={manifest['embedding_model']}"
    )

    # Run evaluation
    print(
        f"\nEvaluating {len(records)} queries (top_k={args.top_k}, mode={args.mode})..."
    )
    per_query = []
    for i, record in enumerate(records):
        result = evaluate_query(index, record, args.top_k, args.mode)
        per_query.append(result)
        if (i + 1) % 10 == 0:
            print(f"  {i + 1}/{len(records)} queries done")

    # Aggregate and report
    agg = aggregate_metrics(per_query)
    print_report(agg, per_query, verbose=args.verbose)

    # Optionally write JSON output
    if args.output:
        output = {
            "config": {
                "ground_truth": str(args.ground_truth),
                "index": str(args.index),
                "top_k": args.top_k,
                "mode": args.mode,
            },
            "summary": agg,
            "per_query": per_query,
        }
        args.output.write_text(json.dumps(output, indent=2) + "\n")
        print(f"Results written to {args.output}")


if __name__ == "__main__":
    main()
