"""Schema validation tests over all condition files.

Each real condition file in corpus/tier1/ and corpus/tier2/ is tested
independently via the parametrized all_condition_files fixture.
"""

import re
from pathlib import Path

import pytest
import yaml


# ---- Constants matching validate.py ----

REQUIRED_FIELDS = [
    "id",
    "condition",
    "icd10",
    "esi",
    "time_to_harm",
    "category",
    "track",
    "sources",
    "last_updated",
    "compiled_by",
    "risk_tier",
    "validation",
]

VALID_CATEGORIES = [
    "cardiovascular",
    "neurological",
    "respiratory",
    "gastrointestinal",
    "genitourinary",
    "obstetric-gynecologic",
    "endocrine-metabolic",
    "infectious",
    "musculoskeletal",
    "hematologic",
    "toxicologic",
    "traumatic",
    "environmental",
    "psychiatric",
    "pediatric",
    "ophthalmologic",
    "dermatologic",
    "allergic-immunologic",
    "disaster-mci",
    "procedural",
    "presentations",
]

VALID_TRACKS = ["tier1", "tier2"]
VALID_RISK_TIERS = ["A", "B", "C"]
REQUIRED_SECTIONS = ["Recognition", "Critical Actions", "Pitfalls"]

VALID_DISPOSITIONS = ["admission", "outpatient", "observation"]
VALID_SOURCE_TYPES = [
    "guideline",
    "pubmed",
    "textbook",
    "who",
    "cdc",
    "wikem",
    "review",
    "meta-analysis",
    "consensus-statement",
]

ICD10_PATTERN = re.compile(r"^[A-Z][0-9]")


# ---- Helpers ----


def parse_file(path: Path):
    """Return (frontmatter_dict, full_text) for a condition file."""
    text = path.read_text()
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return None, text
    fm = yaml.safe_load(match.group(1))
    return fm, text


# ---- Tests ----


class TestRequiredFrontmatterFields:
    def test_frontmatter_exists(self, all_condition_files):
        path = all_condition_files
        text = path.read_text()
        match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
        assert match is not None, f"{path.name}: No YAML frontmatter found"

    @pytest.mark.parametrize("field", REQUIRED_FIELDS)
    def test_required_field_present(self, all_condition_files, field):
        path = all_condition_files
        fm, _ = parse_file(path)
        if fm is None:
            pytest.skip(f"{path.name}: No frontmatter")
        assert field in fm, f"{path.name}: Missing required field '{field}'"


class TestFieldValues:
    def test_id_matches_filename(self, all_condition_files):
        path = all_condition_files
        fm, _ = parse_file(path)
        if fm is None or "id" not in fm:
            pytest.skip("No frontmatter or id field")
        assert fm["id"] == path.stem, (
            f"{path.name}: id '{fm['id']}' does not match filename '{path.stem}'"
        )

    def test_id_format_kebab_case(self, all_condition_files):
        path = all_condition_files
        fm, _ = parse_file(path)
        if fm is None or "id" not in fm:
            pytest.skip("No frontmatter or id field")
        assert re.match(r"^[a-z0-9-]+$", str(fm["id"])), (
            f"{path.name}: id '{fm['id']}' must be lowercase alphanumeric with hyphens only"
        )

    def test_esi_range(self, all_condition_files):
        path = all_condition_files
        fm, _ = parse_file(path)
        if fm is None or "esi" not in fm:
            pytest.skip("No frontmatter or esi field")
        esi = fm["esi"]
        assert isinstance(esi, int), (
            f"{path.name}: esi must be an integer, got {type(esi)}"
        )
        assert 1 <= esi <= 5, f"{path.name}: esi {esi} out of range 1-5"

    def test_category_valid(self, all_condition_files):
        path = all_condition_files
        fm, _ = parse_file(path)
        if fm is None or "category" not in fm:
            pytest.skip("No frontmatter or category field")
        assert fm["category"] in VALID_CATEGORIES, (
            f"{path.name}: Invalid category '{fm['category']}'"
        )

    def test_track_valid(self, all_condition_files):
        path = all_condition_files
        fm, _ = parse_file(path)
        if fm is None or "track" not in fm:
            pytest.skip("No frontmatter or track field")
        assert fm["track"] in VALID_TRACKS, (
            f"{path.name}: Invalid track '{fm['track']}' (must be tier1 or tier2)"
        )

    def test_risk_tier_valid(self, all_condition_files):
        path = all_condition_files
        fm, _ = parse_file(path)
        if fm is None or "risk_tier" not in fm:
            pytest.skip("No frontmatter or risk_tier field")
        assert fm["risk_tier"] in VALID_RISK_TIERS, (
            f"{path.name}: Invalid risk_tier '{fm['risk_tier']}' (must be A, B, or C)"
        )


class TestICD10:
    def test_icd10_is_nonempty_list(self, all_condition_files):
        path = all_condition_files
        fm, _ = parse_file(path)
        if fm is None or "icd10" not in fm:
            pytest.skip("No frontmatter or icd10 field")
        codes = fm["icd10"]
        assert isinstance(codes, list), f"{path.name}: icd10 must be a list"
        assert len(codes) >= 1, f"{path.name}: icd10 must be non-empty"

    def test_icd10_code_format(self, all_condition_files):
        path = all_condition_files
        fm, _ = parse_file(path)
        if fm is None or "icd10" not in fm:
            pytest.skip("No frontmatter or icd10 field")
        codes = fm["icd10"]
        if not isinstance(codes, list):
            pytest.skip("icd10 is not a list")
        for code in codes:
            assert ICD10_PATTERN.match(str(code)), (
                f"{path.name}: ICD-10 code '{code}' must start with letter then digit"
            )


class TestSources:
    def test_sources_nonempty(self, all_condition_files):
        path = all_condition_files
        fm, _ = parse_file(path)
        if fm is None or "sources" not in fm:
            pytest.skip("No frontmatter or sources field")
        sources = fm["sources"]
        assert isinstance(sources, list), f"{path.name}: sources must be a list"
        assert len(sources) >= 1, f"{path.name}: sources must be non-empty"

    def test_each_source_has_type(self, all_condition_files):
        path = all_condition_files
        fm, _ = parse_file(path)
        if fm is None or "sources" not in fm:
            pytest.skip("No frontmatter or sources field")
        sources = fm["sources"]
        if not isinstance(sources, list):
            pytest.skip("sources is not a list")
        for i, src in enumerate(sources):
            assert "type" in src, f"{path.name}: source[{i}] missing 'type'"

    def test_each_source_has_ref(self, all_condition_files):
        path = all_condition_files
        fm, _ = parse_file(path)
        if fm is None or "sources" not in fm:
            pytest.skip("No frontmatter or sources field")
        sources = fm["sources"]
        if not isinstance(sources, list):
            pytest.skip("sources is not a list")
        for i, src in enumerate(sources):
            assert "ref" in src, f"{path.name}: source[{i}] missing 'ref'"

    def test_source_type_valid(self, all_condition_files):
        path = all_condition_files
        fm, _ = parse_file(path)
        if fm is None or "sources" not in fm:
            pytest.skip("No frontmatter or sources field")
        sources = fm["sources"]
        if not isinstance(sources, list):
            pytest.skip("sources is not a list")
        for i, src in enumerate(sources):
            if "type" in src:
                assert src["type"] in VALID_SOURCE_TYPES, (
                    f"{path.name}: source[{i}] has unknown type '{src['type']}'"
                )


class TestValidationBlock:
    def test_validation_is_dict(self, all_condition_files):
        path = all_condition_files
        fm, _ = parse_file(path)
        if fm is None or "validation" not in fm:
            pytest.skip("No frontmatter or validation field")
        assert isinstance(fm["validation"], dict), (
            f"{path.name}: validation must be an object"
        )

    def test_schema_version_exists(self, all_condition_files):
        path = all_condition_files
        fm, _ = parse_file(path)
        if fm is None or "validation" not in fm:
            pytest.skip("No frontmatter or validation field")
        val = fm["validation"]
        if not isinstance(val, dict):
            pytest.skip("validation is not a dict")
        assert "schema_version" in val, (
            f"{path.name}: validation.schema_version is required"
        )


class TestRequiredSections:
    @pytest.mark.parametrize("section", REQUIRED_SECTIONS)
    def test_required_section_present(self, all_condition_files, section):
        path = all_condition_files
        _, text = parse_file(path)
        assert f"## {section}" in text, (
            f"{path.name}: Missing required section '## {section}'"
        )


class TestOptionalDeferFields:
    def test_disposition_default_valid_if_present(self, all_condition_files):
        path = all_condition_files
        fm, _ = parse_file(path)
        if fm is None or "disposition_default" not in fm:
            pytest.skip("disposition_default not present")
        assert fm["disposition_default"] in VALID_DISPOSITIONS, (
            f"{path.name}: Invalid disposition_default '{fm['disposition_default']}'"
        )

    def test_escalation_triggers_is_list_if_present(self, all_condition_files):
        path = all_condition_files
        fm, _ = parse_file(path)
        if fm is None or "escalation_triggers" not in fm:
            pytest.skip("escalation_triggers not present")
        assert isinstance(fm["escalation_triggers"], list), (
            f"{path.name}: escalation_triggers must be an array"
        )

    def test_confusion_pairs_is_list_if_present(self, all_condition_files):
        path = all_condition_files
        fm, _ = parse_file(path)
        if fm is None or "confusion_pairs" not in fm:
            pytest.skip("confusion_pairs not present")
        pairs = fm["confusion_pairs"]
        assert isinstance(pairs, list), f"{path.name}: confusion_pairs must be an array"

    def test_confusion_pairs_entries_have_required_keys(self, all_condition_files):
        path = all_condition_files
        fm, _ = parse_file(path)
        if fm is None or "confusion_pairs" not in fm:
            pytest.skip("confusion_pairs not present")
        pairs = fm["confusion_pairs"]
        if not isinstance(pairs, list):
            pytest.skip("confusion_pairs is not a list")
        for i, cp in enumerate(pairs):
            assert isinstance(cp, dict), (
                f"{path.name}: confusion_pairs[{i}] must be an object"
            )
            assert "condition" in cp, (
                f"{path.name}: confusion_pairs[{i}] missing 'condition'"
            )
            assert "differentiators" in cp, (
                f"{path.name}: confusion_pairs[{i}] missing 'differentiators'"
            )

    def test_reviewed_by_format_if_present(self, all_condition_files):
        """If reviewed_by is present, it must be a non-empty string with review_date."""
        path = all_condition_files
        fm, _ = parse_file(path)
        if fm is None:
            pytest.skip("No frontmatter")
        if "reviewed_by" not in fm:
            return  # Optional field
        assert isinstance(fm["reviewed_by"], str) and len(fm["reviewed_by"]) > 0, (
            f"{path.name}: reviewed_by must be a non-empty string"
        )
        assert "review_date" in fm, (
            f"{path.name}: reviewed_by present but review_date missing"
        )

    def test_time_to_harm_is_string_or_dict(self, all_condition_files):
        path = all_condition_files
        fm, _ = parse_file(path)
        if fm is None or "time_to_harm" not in fm:
            pytest.skip("No frontmatter or time_to_harm")
        tth = fm["time_to_harm"]
        assert isinstance(tth, (str, dict)), (
            f"{path.name}: time_to_harm must be a string or object, got {type(tth)}"
        )

    def test_time_to_harm_dict_has_valid_keys(self, all_condition_files):
        path = all_condition_files
        fm, _ = parse_file(path)
        if fm is None or "time_to_harm" not in fm:
            pytest.skip("No frontmatter or time_to_harm")
        tth = fm["time_to_harm"]
        if not isinstance(tth, dict):
            pytest.skip("time_to_harm is not a dict")
        valid_keys = {"irreversible_injury", "death", "optimal_intervention_window"}
        for k in tth:
            assert k in valid_keys, f"{path.name}: time_to_harm has unknown key '{k}'"
