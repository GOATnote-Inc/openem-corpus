#!/usr/bin/env python3
"""Query the OpenEM hybrid search index.

Supports vector (semantic), full-text (BM25), and hybrid search modes.

Usage:
    python scripts/query_index.py "dose of amiodarone in stable VT"
    python scripts/query_index.py "pediatric DKA insulin" --mode hybrid --top-k 5
    python scripts/query_index.py "I47.21" --mode fts
    python scripts/query_index.py "anaphylaxis" --filter-category allergic-immunologic
    python scripts/query_index.py "intubation" --filter-risk-tier A

Modes:
    hybrid  — RRF fusion of vector + BM25 (default)
    vector  — dense semantic search only
    fts     — full-text BM25 search only
"""

import argparse
import json
import sys
import textwrap
from pathlib import Path

import lancedb

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INDEX_DIR = REPO_ROOT / "data" / "index"


def load_index(index_dir: Path):
    """Load LanceDB table and manifest."""
    manifest_path = index_dir / "manifest.json"
    if not manifest_path.exists():
        print(
            f"ERROR: No manifest at {manifest_path}. Run build_index.py first.",
            file=sys.stderr,
        )
        sys.exit(1)

    manifest = json.loads(manifest_path.read_text())
    db = lancedb.connect(str(index_dir / "openem.lance"))
    table = db.open_table("conditions")
    return table, manifest


def _apply_filters(query_builder, **filters):
    """Apply metadata filters to a LanceDB query builder."""
    if filters.get("category"):
        query_builder = query_builder.where(f"category = '{filters['category']}'")
    if filters.get("risk_tier"):
        query_builder = query_builder.where(f"risk_tier = '{filters['risk_tier']}'")
    if filters.get("condition_id"):
        query_builder = query_builder.where(
            f"condition_id = '{filters['condition_id']}'"
        )
    return query_builder


def _rrf_merge(
    vector_results: list[dict], fts_results: list[dict], k: int = 60
) -> list[dict]:
    """Reciprocal Rank Fusion of two result lists. Returns merged list sorted by RRF score."""
    scores: dict[str, float] = {}
    results_by_id: dict[str, dict] = {}

    for rank, r in enumerate(vector_results):
        rid = r["id"]
        scores[rid] = scores.get(rid, 0.0) + 1.0 / (k + rank + 1)
        results_by_id[rid] = r

    for rank, r in enumerate(fts_results):
        rid = r["id"]
        scores[rid] = scores.get(rid, 0.0) + 1.0 / (k + rank + 1)
        results_by_id[rid] = r

    sorted_ids = sorted(scores, key=lambda x: scores[x], reverse=True)
    merged = []
    for rid in sorted_ids:
        result = results_by_id[rid]
        result["_rrf_score"] = round(scores[rid], 6)
        merged.append(result)
    return merged


def search(table, query: str, mode: str, top_k: int, model_name: str, **filters):
    """Execute search and return results."""
    if mode == "fts":
        qb = table.search(query, query_type="fts").limit(top_k)
        qb = _apply_filters(qb, **filters)
        return qb.to_list()

    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(model_name)
    vec = model.encode(query).tolist()

    if mode == "vector":
        qb = table.search(vec, query_type="vector").limit(top_k)
        qb = _apply_filters(qb, **filters)
        return qb.to_list()

    # Hybrid: manual RRF fusion of vector + FTS
    fetch_k = top_k * 4  # over-fetch for better fusion

    vec_qb = _apply_filters(
        table.search(vec, query_type="vector").limit(fetch_k), **filters
    )
    fts_qb = _apply_filters(
        table.search(query, query_type="fts").limit(fetch_k), **filters
    )

    vec_results = vec_qb.to_list()
    fts_results = fts_qb.to_list()

    merged = _rrf_merge(vec_results, fts_results)
    return merged[:top_k]


def format_result(r: dict, rank: int, verbose: bool = False) -> str:
    """Format a single search result for display."""
    score = r.get("_rrf_score", r.get("_relevance_score", r.get("_distance", "n/a")))
    lines = [
        f"  [{rank}] {r['condition']} — {r['section']}",
        f"      id: {r['id']}  |  tier: {r['risk_tier']}  |  ESI: {r['esi']}  |  score: {score}",
    ]
    if verbose:
        text = r["text"].split("\n\n", 1)[-1]  # strip the prepended header
        wrapped = textwrap.fill(
            text[:500], width=80, initial_indent="      ", subsequent_indent="      "
        )
        lines.append(wrapped)
        if len(text) > 500:
            lines.append(f"      ... ({len(text)} chars total)")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Query OpenEM index")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--mode", choices=["hybrid", "vector", "fts"], default="hybrid")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--verbose", "-v", action="store_true", help="Show chunk text")
    parser.add_argument("--index-dir", type=Path, default=DEFAULT_INDEX_DIR)
    parser.add_argument("--filter-category", dest="category", help="Filter by category")
    parser.add_argument(
        "--filter-risk-tier", dest="risk_tier", help="Filter by risk tier (A/B/C)"
    )
    parser.add_argument(
        "--filter-condition", dest="condition_id", help="Filter by condition ID"
    )
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    table, manifest = load_index(args.index_dir)

    results = search(
        table,
        args.query,
        args.mode,
        args.top_k,
        manifest["embedding_model"],
        category=args.category,
        risk_tier=args.risk_tier,
        condition_id=args.condition_id,
    )

    if args.json:
        # Strip vectors from JSON output
        for r in results:
            r.pop("vector", None)
        print(json.dumps(results, indent=2))
        return

    print(f'\nQuery: "{args.query}"  (mode={args.mode}, top_k={args.top_k})')
    print(
        f"Index: {manifest['num_chunks']} chunks / {manifest['num_conditions']} conditions"
    )
    print(f"{'─' * 70}")

    if not results:
        print("  No results found.")
        return

    for i, r in enumerate(results, 1):
        print(format_result(r, i, verbose=args.verbose))
        if i < len(results):
            print()


if __name__ == "__main__":
    main()
