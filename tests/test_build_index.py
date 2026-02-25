"""Tests for build_index.py parsing and chunking logic.

Tests parse_condition, build_chunks, and section_to_key without
requiring a real embedding model or LanceDB instance.
"""

import sys
import textwrap
import tempfile
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from build_index import parse_condition, build_chunks, section_to_key


# ---- Sample markdown fixture ----

SAMPLE_MD = textwrap.dedent("""\
    ---
    id: test-stemi
    condition: Test STEMI
    aliases: [STEMI, ST-elevation MI]
    icd10: [I21.01, I21.02]
    esi: 1
    time_to_harm: "< 90 minutes"
    category: cardiovascular
    track: tier1
    sources:
      - type: guideline
        ref: "AHA 2023"
    last_updated: "2026-01-01"
    compiled_by: agent
    risk_tier: A
    validation:
      schema_version: "2.0"
    ---
    # Test STEMI

    ## Recognition

    ST elevation in two contiguous leads. Classic presentation includes
    substernal chest pain with radiation to arm or jaw.

    ## Critical Actions

    - Activate cath lab immediately
    - Aspirin 325 mg PO stat
    - IV access, monitoring

    ## Treatment

    Primary PCI preferred over thrombolytics when door-to-balloon < 90 min.

    ## Disposition

    Cardiac ICU admission required. Cardiology consult immediately.

    ## Pitfalls

    - Missing posterior STEMI without V7-V9 leads
    - Giving nitrates with RV infarct
    - Failing to recognize LBBB as STEMI equivalent
""")

MINIMAL_VALID_MD = textwrap.dedent("""\
    ---
    id: minimal-condition
    condition: Minimal Condition
    icd10: [Z00.00]
    esi: 3
    category: cardiovascular
    track: tier1
    sources:
      - type: guideline
        ref: "Some guideline"
    last_updated: "2026-01-01"
    compiled_by: agent
    risk_tier: C
    validation:
      schema_version: "2.0"
    ---
    # Minimal Condition

    ## Recognition

    Simple recognition text here.

    ## Pitfalls

    Only pitfall entry here.
""")

NO_FRONTMATTER_MD = textwrap.dedent("""\
    # Just a heading

    No YAML frontmatter here at all.
""")


@pytest.fixture
def sample_file(tmp_path):
    p = tmp_path / "test-stemi.md"
    p.write_text(SAMPLE_MD)
    return p


@pytest.fixture
def minimal_file(tmp_path):
    p = tmp_path / "minimal-condition.md"
    p.write_text(MINIMAL_VALID_MD)
    return p


@pytest.fixture
def no_frontmatter_file(tmp_path):
    p = tmp_path / "no-fm.md"
    p.write_text(NO_FRONTMATTER_MD)
    return p


# ---- parse_condition ----


class TestParseCondition:
    def test_returns_frontmatter_dict(self, sample_file):
        fm, sections = parse_condition(sample_file)
        assert fm is not None
        assert isinstance(fm, dict)

    def test_frontmatter_has_id(self, sample_file):
        fm, _ = parse_condition(sample_file)
        assert fm["id"] == "test-stemi"

    def test_frontmatter_has_condition_name(self, sample_file):
        fm, _ = parse_condition(sample_file)
        assert fm["condition"] == "Test STEMI"

    def test_frontmatter_has_icd10(self, sample_file):
        fm, _ = parse_condition(sample_file)
        assert fm["icd10"] == ["I21.01", "I21.02"]

    def test_sections_dict_returned(self, sample_file):
        _, sections = parse_condition(sample_file)
        assert sections is not None
        assert isinstance(sections, dict)

    def test_sections_keys_are_h2_names(self, sample_file):
        _, sections = parse_condition(sample_file)
        assert "Recognition" in sections
        assert "Critical Actions" in sections
        assert "Treatment" in sections
        assert "Disposition" in sections
        assert "Pitfalls" in sections

    def test_section_text_not_empty(self, sample_file):
        _, sections = parse_condition(sample_file)
        for name, text in sections.items():
            assert text.strip(), f"Section '{name}' is empty"

    def test_section_text_content(self, sample_file):
        _, sections = parse_condition(sample_file)
        assert "ST elevation" in sections["Recognition"]
        assert "cath lab" in sections["Critical Actions"]

    def test_no_frontmatter_returns_none_tuple(self, no_frontmatter_file):
        fm, sections = parse_condition(no_frontmatter_file)
        assert fm is None
        assert sections is None

    def test_minimal_file_parsed(self, minimal_file):
        fm, sections = parse_condition(minimal_file)
        assert fm is not None
        assert "Recognition" in sections


# ---- section_to_key ----


class TestSectionToKey:
    def test_critical_actions(self):
        assert section_to_key("Critical Actions") == "critical_actions"

    def test_single_word(self):
        assert section_to_key("Recognition") == "recognition"

    def test_multiple_spaces(self):
        assert section_to_key("Differential  Diagnosis") == "differential_diagnosis"

    def test_special_characters_stripped(self):
        result = section_to_key("Section (Note)")
        assert re.search(r"[^a-z0-9_]", result) is None

    def test_hyphenated_name(self):
        result = section_to_key("Sub-section Name")
        assert "_" in result or result == "sub_section_name"

    def test_already_lowercase(self):
        assert section_to_key("pitfalls") == "pitfalls"

    def test_trailing_underscore_stripped(self):
        result = section_to_key("Section!")
        assert not result.startswith("_")
        assert not result.endswith("_")


# ---- build_chunks ----


class TestBuildChunks:
    def test_returns_list(self, sample_file):
        fm, sections = parse_condition(sample_file)
        chunks = build_chunks(fm, sections, "test-stemi")
        assert isinstance(chunks, list)

    def test_one_chunk_per_section(self, sample_file):
        fm, sections = parse_condition(sample_file)
        chunks = build_chunks(fm, sections, "test-stemi")
        assert len(chunks) == len(sections)

    def test_chunk_has_required_keys(self, sample_file):
        fm, sections = parse_condition(sample_file)
        chunks = build_chunks(fm, sections, "test-stemi")
        required = {
            "id",
            "condition_id",
            "condition",
            "section",
            "text",
            "category",
            "risk_tier",
            "esi",
            "aliases",
            "icd10",
        }
        for chunk in chunks:
            for key in required:
                assert key in chunk, f"Chunk missing key '{key}'"

    def test_chunk_id_format(self, sample_file):
        fm, sections = parse_condition(sample_file)
        chunks = build_chunks(fm, sections, "test-stemi")
        for chunk in chunks:
            cid = chunk["id"]
            assert cid.startswith("test-stemi/"), (
                f"id '{cid}' must start with 'test-stemi/'"
            )

    def test_chunk_text_includes_condition_name(self, sample_file):
        fm, sections = parse_condition(sample_file)
        chunks = build_chunks(fm, sections, "test-stemi")
        for chunk in chunks:
            assert "Test STEMI" in chunk["text"], (
                f"Chunk text must include condition name; id={chunk['id']}"
            )

    def test_chunk_text_includes_section_name(self, sample_file):
        fm, sections = parse_condition(sample_file)
        chunks = build_chunks(fm, sections, "test-stemi")
        for chunk in chunks:
            section = chunk["section"]
            assert section in chunk["text"], (
                f"Chunk text must include section name '{section}'"
            )

    def test_chunk_section_field_matches_original(self, sample_file):
        fm, sections = parse_condition(sample_file)
        chunks = build_chunks(fm, sections, "test-stemi")
        chunk_sections = {c["section"] for c in chunks}
        assert chunk_sections == set(sections.keys())

    def test_aliases_included_in_text(self, sample_file):
        fm, sections = parse_condition(sample_file)
        chunks = build_chunks(fm, sections, "test-stemi")
        for chunk in chunks:
            # Aliases should be embedded in the chunk text header
            assert "STEMI" in chunk["text"]

    def test_icd10_in_text(self, sample_file):
        fm, sections = parse_condition(sample_file)
        chunks = build_chunks(fm, sections, "test-stemi")
        for chunk in chunks:
            assert "I21.01" in chunk["text"]

    def test_aliases_field_as_string(self, sample_file):
        fm, sections = parse_condition(sample_file)
        chunks = build_chunks(fm, sections, "test-stemi")
        for chunk in chunks:
            assert isinstance(chunk["aliases"], str)

    def test_icd10_field_as_string(self, sample_file):
        fm, sections = parse_condition(sample_file)
        chunks = build_chunks(fm, sections, "test-stemi")
        for chunk in chunks:
            assert isinstance(chunk["icd10"], str)

    def test_empty_section_skipped(self, tmp_path):
        md = textwrap.dedent("""\
            ---
            id: sparse
            condition: Sparse Condition
            icd10: [Z00.00]
            esi: 3
            category: cardiovascular
            track: tier1
            sources:
              - type: guideline
                ref: "Test guideline"
            last_updated: "2026-01-01"
            compiled_by: agent
            risk_tier: C
            validation:
              schema_version: "2.0"
            ---

            ## Recognition

            Has content here.

            ## Empty Section

        """)
        p = tmp_path / "sparse.md"
        p.write_text(md)
        fm, sections = parse_condition(p)
        chunks = build_chunks(fm, sections, "sparse")
        chunk_sections = {c["section"] for c in chunks}
        # Empty section should be skipped
        assert "Empty Section" not in chunk_sections
        assert "Recognition" in chunk_sections

    def test_condition_id_used_as_fallback_condition_name(self, tmp_path):
        md = textwrap.dedent("""\
            ---
            id: no-name
            icd10: [Z00.00]
            esi: 3
            category: cardiovascular
            track: tier1
            sources:
              - type: guideline
                ref: "Test"
            last_updated: "2026-01-01"
            compiled_by: agent
            risk_tier: C
            validation:
              schema_version: "2.0"
            ---

            ## Recognition

            Some text here.
        """)
        p = tmp_path / "no-name.md"
        p.write_text(md)
        fm, sections = parse_condition(p)
        chunks = build_chunks(fm, sections, "no-name")
        for chunk in chunks:
            assert "no-name" in chunk["text"]


# ---- import guard for regex ----
import re
