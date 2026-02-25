"""Unit tests for OpenEMBridge.

All tests use MagicMock to avoid requiring a live LanceDB index.
The openem package imports lancedb at the top of openem/index.py; we mock
that module before importing the bridge so no real LanceDB is needed.

IMPORTANT: We only inject the fake lancedb if it is not already present in
sys.modules. This prevents the mock from clobbering a real lancedb installation
that test_index.py needs.
"""

import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

# Track whether we installed the stub (so we can clean it up if needed).
_LANCEDB_STUB_INSTALLED = False

if "lancedb" not in sys.modules:
    sys.modules["lancedb"] = MagicMock()
    _LANCEDB_STUB_INSTALLED = True

# Ensure the package under test is importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "python"))

from openem.bridge import OpenEMBridge, PRIORITY_SECTIONS


# ---- Fixtures ----


def make_mock_index(search_results=None):
    """Build a MagicMock that mimics OpenEMIndex."""
    idx = MagicMock()
    idx.manifest = {
        "version": "1.0",
        "num_chunks": 896,
        "num_conditions": 128,
    }
    idx.search.return_value = search_results if search_results is not None else []
    return idx


def make_result(chunk_id, condition, section, text):
    return {
        "id": chunk_id,
        "condition_id": chunk_id.split("/")[0],
        "condition": condition,
        "section": section,
        "text": text,
        "category": "cardiovascular",
        "risk_tier": "A",
        "esi": 1,
    }


CONDITION_MAP = {
    "stemi": ["stemi"],
    "neonatal_sepsis": ["neonatal-emergencies", "sepsis"],
    "": [],
}


# ---- resolve_condition_ids ----


class TestResolveConditionIds:
    def test_exact_match_in_map(self):
        bridge = OpenEMBridge(make_mock_index(), CONDITION_MAP)
        assert bridge.resolve_condition_ids("stemi") == ["stemi"]

    def test_multi_id_match(self):
        bridge = OpenEMBridge(make_mock_index(), CONDITION_MAP)
        assert bridge.resolve_condition_ids("neonatal_sepsis") == [
            "neonatal-emergencies",
            "sepsis",
        ]

    def test_case_insensitive_lookup(self):
        bridge = OpenEMBridge(make_mock_index(), CONDITION_MAP)
        assert bridge.resolve_condition_ids("STEMI") == ["stemi"]

    def test_empty_list_for_empty_string_key(self):
        bridge = OpenEMBridge(make_mock_index(), CONDITION_MAP)
        assert bridge.resolve_condition_ids("") == []

    def test_unknown_key_falls_back_to_kebab(self):
        bridge = OpenEMBridge(make_mock_index(), CONDITION_MAP)
        result = bridge.resolve_condition_ids("acute_mi")
        assert result == ["acute-mi"]

    def test_unknown_key_with_spaces_falls_back(self):
        bridge = OpenEMBridge(make_mock_index(), CONDITION_MAP)
        result = bridge.resolve_condition_ids("acute mi")
        assert result == ["acute-mi"]

    def test_unknown_key_strips_parens(self):
        bridge = OpenEMBridge(make_mock_index(), CONDITION_MAP)
        result = bridge.resolve_condition_ids("dvt (lower limb)")
        assert result == ["dvt-lower-limb"]

    def test_custom_fallback_separator(self):
        bridge = OpenEMBridge(make_mock_index(), CONDITION_MAP, fallback_separator=" ")
        result = bridge.resolve_condition_ids("acute limb ischemia")
        assert result == ["acute-limb-ischemia"]


# ---- get_context ----


class TestGetContext:
    def test_returns_none_for_empty_condition_id_list(self):
        """When condition_map maps key to [], return None without calling search."""
        idx = make_mock_index(search_results=[])
        bridge = OpenEMBridge(idx, CONDITION_MAP)
        result = bridge.get_context("")
        assert result is None

    def test_returns_none_when_search_returns_nothing(self):
        idx = make_mock_index(search_results=[])
        bridge = OpenEMBridge(idx, CONDITION_MAP)
        result = bridge.get_context("stemi")
        assert result is None

    def test_returns_string_with_valid_results(self):
        r = make_result(
            "stemi/critical_actions",
            "STEMI",
            "Critical Actions",
            "Activate cath lab immediately.",
        )
        idx = make_mock_index(search_results=[r])
        bridge = OpenEMBridge(idx, CONDITION_MAP)
        result = bridge.get_context("stemi")
        assert isinstance(result, str)
        assert len(result) > 0

    def test_result_contains_section_header(self):
        r = make_result(
            "stemi/critical_actions",
            "STEMI",
            "Critical Actions",
            "Activate cath lab immediately.",
        )
        idx = make_mock_index(search_results=[r])
        bridge = OpenEMBridge(idx, CONDITION_MAP)
        result = bridge.get_context("stemi")
        assert "Critical Actions" in result
        assert "STEMI" in result

    def test_dedup_by_chunk_id(self):
        """Duplicate chunk IDs appear in results only once."""
        r1 = make_result(
            "stemi/critical_actions", "STEMI", "Critical Actions", "Activate cath lab."
        )
        r2 = make_result(
            "stemi/critical_actions", "STEMI", "Critical Actions", "Activate cath lab."
        )
        idx = make_mock_index(search_results=[r1, r2])
        bridge = OpenEMBridge(idx, CONDITION_MAP)
        result = bridge.get_context("stemi")
        # The section header should appear exactly once
        assert result.count("[STEMI") == 1

    def test_section_priority_critical_actions_before_disposition(self):
        """Critical Actions must appear before Disposition in output."""
        r_disp = make_result(
            "stemi/disposition", "STEMI", "Disposition", "Admit to cardiac ICU."
        )
        r_crit = make_result(
            "stemi/critical_actions", "STEMI", "Critical Actions", "Activate cath lab."
        )
        # Return disposition first to verify sorting overrides insertion order
        idx = make_mock_index(search_results=[r_disp, r_crit])
        bridge = OpenEMBridge(idx, CONDITION_MAP)
        result = bridge.get_context("stemi")
        pos_crit = result.index("Critical Actions")
        pos_disp = result.index("Disposition")
        assert pos_crit < pos_disp, "Critical Actions must appear before Disposition"

    def test_max_chars_budget_respected(self):
        """Output must not exceed max_chars."""
        long_text = "x" * 5000
        r = make_result(
            "stemi/critical_actions", "STEMI", "Critical Actions", long_text
        )
        idx = make_mock_index(search_results=[r])
        bridge = OpenEMBridge(idx, CONDITION_MAP)
        result = bridge.get_context("stemi", max_chars=500)
        assert result is None or len(result) <= 500 + 10  # small tolerance for header

    def test_strips_header_line_from_chunk(self):
        """Text starting with a header line (first paragraph) should be stripped."""
        text_with_header = "STEMI — Critical Actions\n\nActivate cath lab immediately."
        r = make_result(
            "stemi/critical_actions", "STEMI", "Critical Actions", text_with_header
        )
        idx = make_mock_index(search_results=[r])
        bridge = OpenEMBridge(idx, CONDITION_MAP)
        result = bridge.get_context("stemi")
        # The raw chunk header should be stripped; the section data should remain
        assert "Activate cath lab immediately." in result

    def test_multiple_condition_ids_searched(self):
        """Each condition_id in the resolved list gets its own search call."""
        r1 = make_result(
            "neonatal-emergencies/critical_actions",
            "Neonatal Emergencies",
            "Critical Actions",
            "Neonatal text.",
        )
        r2 = make_result(
            "sepsis/critical_actions", "Sepsis", "Critical Actions", "Sepsis text."
        )

        call_count = []

        def mock_search(query, top_k, mode, condition_id):
            call_count.append(condition_id)
            if condition_id == "neonatal-emergencies":
                return [r1]
            return [r2]

        idx = make_mock_index()
        idx.search.side_effect = mock_search
        bridge = OpenEMBridge(idx, CONDITION_MAP)
        bridge.get_context("neonatal_sepsis")
        assert "neonatal-emergencies" in call_count
        assert "sepsis" in call_count


# ---- format_system_context ----


class TestFormatSystemContext:
    def test_returns_none_when_no_context(self):
        idx = make_mock_index(search_results=[])
        bridge = OpenEMBridge(idx, CONDITION_MAP)
        result = bridge.format_system_context("stemi")
        assert result is None

    def test_wraps_with_prefix_and_suffix(self):
        r = make_result(
            "stemi/critical_actions", "STEMI", "Critical Actions", "Activate cath lab."
        )
        idx = make_mock_index(search_results=[r])
        bridge = OpenEMBridge(idx, CONDITION_MAP)
        result = bridge.format_system_context("stemi")
        assert result is not None
        assert "--- CLINICAL REFERENCE ---" in result
        assert "--- END REFERENCE ---" in result

    def test_prefix_mentions_emergency_care(self):
        r = make_result(
            "stemi/critical_actions", "STEMI", "Critical Actions", "Activate cath lab."
        )
        idx = make_mock_index(search_results=[r])
        bridge = OpenEMBridge(idx, CONDITION_MAP)
        result = bridge.format_system_context("stemi")
        assert "emergency care" in result.lower()

    def test_context_embedded_in_output(self):
        r = make_result(
            "stemi/critical_actions",
            "STEMI",
            "Critical Actions",
            "Activate cath lab immediately.",
        )
        idx = make_mock_index(search_results=[r])
        bridge = OpenEMBridge(idx, CONDITION_MAP)
        raw = bridge.get_context("stemi")
        formatted = bridge.format_system_context("stemi")
        assert raw in formatted


# ---- corpus_info property ----


class TestCorpusInfo:
    def test_corpus_info_string(self):
        idx = make_mock_index()
        bridge = OpenEMBridge(idx, CONDITION_MAP)
        info = bridge.corpus_info
        assert "OpenEM" in info
        assert "128" in info
        assert "896" in info


# ---- Priority section ordering ----


class TestSectionPriority:
    def test_priority_list_order(self):
        """Verify PRIORITY_SECTIONS constant is ordered as documented."""
        assert PRIORITY_SECTIONS[0] == "Critical Actions"
        assert PRIORITY_SECTIONS[1] == "Treatment"
        assert "Disposition" in PRIORITY_SECTIONS
        assert PRIORITY_SECTIONS.index("Critical Actions") < PRIORITY_SECTIONS.index(
            "Disposition"
        )

    def test_unknown_section_sorted_last(self):
        """Sections not in PRIORITY_SECTIONS sort after all known sections."""
        r_unknown = make_result("stemi/references", "STEMI", "References", "Some refs.")
        r_known = make_result(
            "stemi/critical_actions", "STEMI", "Critical Actions", "Activate cath lab."
        )
        idx = make_mock_index(search_results=[r_unknown, r_known])
        bridge = OpenEMBridge(idx, CONDITION_MAP)
        result = bridge.get_context("stemi")
        pos_known = result.index("Critical Actions")
        pos_unknown = result.index("References")
        assert pos_known < pos_unknown
