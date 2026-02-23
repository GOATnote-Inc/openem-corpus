"""Tests for OpenEMIndex.

All tests are marked slow and require lancedb to be installed.
Tests build a mini in-memory index from synthetic data rather than
requiring the pre-built corpus index on disk.
"""

import sys
import tempfile
from pathlib import Path

import pytest
from unittest.mock import MagicMock

# importorskip will allow a MagicMock stub (truthy) through, so we also
# verify the module is a genuine lancedb installation, not the stub that
# test_bridge.py may have injected into sys.modules.
lancedb = pytest.importorskip("lancedb")
if isinstance(lancedb, MagicMock):
    pytest.skip("lancedb is not installed (stub detected)", allow_module_level=True)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "python"))

pytestmark = pytest.mark.slow

# ---- Minimal synthetic data ----

SYNTHETIC_CHUNKS = [
    {
        "id": "stemi/critical_actions",
        "condition_id": "stemi",
        "condition": "ST-Elevation Myocardial Infarction",
        "section": "Critical Actions",
        "text": "STEMI — Critical Actions\n\nActivate cath lab. Aspirin 325 mg PO.",
        "category": "cardiovascular",
        "risk_tier": "A",
        "esi": 1,
        "aliases": "STEMI, ST-elevation MI",
        "icd10": "I21.01",
        "vector": [0.1] * 768,
    },
    {
        "id": "stemi/recognition",
        "condition_id": "stemi",
        "condition": "ST-Elevation Myocardial Infarction",
        "section": "Recognition",
        "text": "STEMI — Recognition\n\nST elevation in two contiguous leads.",
        "category": "cardiovascular",
        "risk_tier": "A",
        "esi": 1,
        "aliases": "STEMI",
        "icd10": "I21.01",
        "vector": [0.2] * 768,
    },
    {
        "id": "sepsis/critical_actions",
        "condition_id": "sepsis",
        "condition": "Sepsis",
        "section": "Critical Actions",
        "text": "Sepsis — Critical Actions\n\nBlood cultures before antibiotics.",
        "category": "infectious",
        "risk_tier": "A",
        "esi": 2,
        "aliases": "",
        "icd10": "A41.9",
        "vector": [0.9] * 768,
    },
]


def build_test_index(tmp_path: Path):
    """Build a minimal LanceDB index from SYNTHETIC_CHUNKS."""
    import lancedb as ldb
    db = ldb.connect(str(tmp_path / "openem.lance"))
    table = db.create_table("conditions", SYNTHETIC_CHUNKS, mode="overwrite")
    # FTS index
    try:
        table.create_fts_index("text", replace=True)
    except Exception:
        pass  # FTS creation may fail in environments without tantivy

    import json
    manifest = {
        "corpus": "openem-test",
        "version": "test",
        "embedding_model": "NeuML/pubmedbert-base-embeddings",
        "embedding_dim": 768,
        "num_conditions": 2,
        "num_chunks": len(SYNTHETIC_CHUNKS),
        "index_path": str(tmp_path / "openem.lance"),
        "built_at": "2026-01-01T00:00:00Z",
    }
    (tmp_path / "manifest.json").write_text(json.dumps(manifest))
    return tmp_path


@pytest.fixture(scope="module")
def test_index_dir(tmp_path_factory):
    tmp = tmp_path_factory.mktemp("openem_index")
    return build_test_index(tmp)


@pytest.fixture(scope="module")
def openem_index(test_index_dir):
    from openem.index import OpenEMIndex
    # Patch the model so it returns a fixed vector instead of loading PubMedBERT
    idx = OpenEMIndex.__new__(OpenEMIndex)
    import json
    idx.manifest = json.loads((test_index_dir / "manifest.json").read_text())
    idx._model_name = "NeuML/pubmedbert-base-embeddings"
    idx._model = None

    import lancedb as ldb
    db = ldb.connect(str(test_index_dir / "openem.lance"))
    idx.table = db.open_table("conditions")

    # Override the model property to return a MagicMock
    from unittest.mock import MagicMock
    import numpy as np
    mock_model = MagicMock()
    mock_model.encode.return_value = np.array([0.15] * 768)
    idx._model = mock_model

    return idx


# ---- Tests ----

class TestIndexBuilding:
    def test_manifest_written(self, test_index_dir):
        manifest_path = test_index_dir / "manifest.json"
        assert manifest_path.exists(), "manifest.json must exist after build"

    def test_manifest_fields(self, test_index_dir):
        import json
        m = json.loads((test_index_dir / "manifest.json").read_text())
        assert "num_chunks" in m
        assert "num_conditions" in m
        assert m["num_chunks"] == len(SYNTHETIC_CHUNKS)

    def test_lance_table_exists(self, test_index_dir):
        import lancedb as ldb
        db = ldb.connect(str(test_index_dir / "openem.lance"))
        tables = db.table_names()
        assert "conditions" in tables


class TestVectorSearch:
    def test_vector_search_returns_results(self, openem_index):
        results = openem_index.search("stemi", top_k=2, mode="vector")
        assert isinstance(results, list)
        assert len(results) > 0

    def test_vector_search_result_has_required_keys(self, openem_index):
        results = openem_index.search("stemi", top_k=2, mode="vector")
        assert len(results) > 0
        r = results[0]
        for key in ("id", "condition_id", "condition", "section", "text"):
            assert key in r, f"Result missing key '{key}'"

    def test_vector_search_strips_vector_from_results(self, openem_index):
        results = openem_index.search("stemi", top_k=2, mode="vector")
        for r in results:
            assert "vector" not in r, "Vector should be stripped from results"

    def test_vector_search_top_k_honored(self, openem_index):
        results = openem_index.search("stemi", top_k=1, mode="vector")
        assert len(results) <= 1


class TestConditionIdFilter:
    def test_filter_by_condition_id_returns_only_that_condition(self, openem_index):
        results = openem_index.search("critical actions", top_k=10, mode="vector", condition_id="stemi")
        for r in results:
            assert r["condition_id"] == "stemi", (
                f"Filter by condition_id='stemi' returned '{r['condition_id']}'"
            )

    def test_filter_by_category(self, openem_index):
        results = openem_index.search("treatment", top_k=10, mode="vector", category="infectious")
        for r in results:
            assert r["category"] == "infectious"

    def test_filter_by_risk_tier(self, openem_index):
        results = openem_index.search("treatment", top_k=10, mode="vector", risk_tier="A")
        for r in results:
            assert r["risk_tier"] == "A"


class TestRRFMerge:
    def test_rrf_merge_combines_results(self):
        from openem.index import OpenEMIndex
        vec = [{"id": "a", "score": 0.9}, {"id": "b", "score": 0.8}]
        fts = [{"id": "b", "score": 0.95}, {"id": "c", "score": 0.7}]
        merged = OpenEMIndex._rrf_merge(vec, fts)
        ids = [r["id"] for r in merged]
        assert set(ids) == {"a", "b", "c"}

    def test_rrf_merge_boosts_overlap(self):
        """An item appearing in both lists should rank higher than items in only one."""
        from openem.index import OpenEMIndex
        # 'b' appears in both lists; 'a' and 'c' appear once each
        vec = [{"id": "a"}, {"id": "b"}]
        fts = [{"id": "b"}, {"id": "c"}]
        merged = OpenEMIndex._rrf_merge(vec, fts)
        ids = [r["id"] for r in merged]
        assert ids[0] == "b", f"'b' should rank first (appears in both lists), got {ids}"

    def test_rrf_merge_empty_inputs(self):
        from openem.index import OpenEMIndex
        merged = OpenEMIndex._rrf_merge([], [])
        assert merged == []

    def test_clean_strips_vector_field(self):
        from openem.index import OpenEMIndex
        rows = [{"id": "x", "text": "hello", "vector": [0.1, 0.2]}]
        cleaned = OpenEMIndex._clean(rows)
        assert "vector" not in cleaned[0]
        assert cleaned[0]["text"] == "hello"
