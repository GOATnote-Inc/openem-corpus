"""OpenEM RAG adapter for ScribeGoat2 and LostBench.

Thin interface for loading the OpenEM search index and retrieving
clinical knowledge chunks. Designed to be copied into or imported
by downstream projects.

Usage:
    from openem_adapter import OpenEMIndex

    idx = OpenEMIndex("/path/to/openem/data/index")
    results = idx.search("dose of epinephrine in anaphylaxis", top_k=3)

    for r in results:
        print(r["condition"], r["section"], r["text"][:200])
"""

import json
from pathlib import Path
from typing import Optional

import lancedb


class OpenEMIndex:
    """Hybrid search over the OpenEM corpus index."""

    def __init__(self, index_dir: str | Path, model_name: Optional[str] = None):
        index_dir = Path(index_dir)
        manifest_path = index_dir / "manifest.json"
        if not manifest_path.exists():
            raise FileNotFoundError(
                f"No OpenEM index at {index_dir}. Run: python scripts/build_index.py"
            )

        self.manifest = json.loads(manifest_path.read_text())
        self._model_name = model_name or self.manifest["embedding_model"]
        self._model = None

        db = lancedb.connect(str(index_dir / "openem.lance"))
        self.table = db.open_table("conditions")

    @property
    def model(self):
        """Lazy-load embedding model."""
        if self._model is None:
            from sentence_transformers import SentenceTransformer

            self._model = SentenceTransformer(self._model_name)
        return self._model

    def search(
        self,
        query: str,
        top_k: int = 5,
        mode: str = "hybrid",
        category: Optional[str] = None,
        risk_tier: Optional[str] = None,
        condition_id: Optional[str] = None,
    ) -> list[dict]:
        """Search the OpenEM index.

        Args:
            query: Natural language query, drug name, ICD-10 code, etc.
            top_k: Number of results to return.
            mode: "hybrid" (default), "vector", or "fts".
            category: Filter by clinical category (e.g., "cardiovascular").
            risk_tier: Filter by risk tier ("A", "B", "C").
            condition_id: Filter by condition ID (e.g., "stemi").

        Returns:
            List of dicts with keys: id, condition_id, condition, section,
            text, category, risk_tier, esi, aliases, icd10.
        """
        if mode == "fts":
            qb = self.table.search(query, query_type="fts").limit(top_k)
            qb = self._apply_filters(qb, category, risk_tier, condition_id)
            return self._clean(qb.to_list())

        vec = self.model.encode(query).tolist()

        if mode == "vector":
            qb = self.table.search(vec, query_type="vector").limit(top_k)
            qb = self._apply_filters(qb, category, risk_tier, condition_id)
            return self._clean(qb.to_list())

        # Hybrid: RRF fusion
        fetch_k = top_k * 4
        vec_qb = self._apply_filters(
            self.table.search(vec, query_type="vector").limit(fetch_k),
            category, risk_tier, condition_id,
        )
        fts_qb = self._apply_filters(
            self.table.search(query, query_type="fts").limit(fetch_k),
            category, risk_tier, condition_id,
        )

        merged = self._rrf_merge(vec_qb.to_list(), fts_qb.to_list())
        return self._clean(merged[:top_k])

    @staticmethod
    def _apply_filters(qb, category, risk_tier, condition_id):
        if category:
            qb = qb.where(f"category = '{category}'")
        if risk_tier:
            qb = qb.where(f"risk_tier = '{risk_tier}'")
        if condition_id:
            qb = qb.where(f"condition_id = '{condition_id}'")
        return qb

    @staticmethod
    def _rrf_merge(vec_results, fts_results, k=60):
        scores, by_id = {}, {}
        for rank, r in enumerate(vec_results):
            rid = r["id"]
            scores[rid] = scores.get(rid, 0.0) + 1.0 / (k + rank + 1)
            by_id[rid] = r
        for rank, r in enumerate(fts_results):
            rid = r["id"]
            scores[rid] = scores.get(rid, 0.0) + 1.0 / (k + rank + 1)
            by_id[rid] = r
        return [by_id[rid] for rid in sorted(scores, key=lambda x: scores[x], reverse=True)]

    @staticmethod
    def _clean(results):
        """Strip embedding vectors from results."""
        for r in results:
            r.pop("vector", None)
        return results
