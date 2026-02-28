"""Tests for FHIR R4 Bundle generation from OpenEM presentation profiles."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest

# Mock lancedb if not installed (same pattern as test_bridge.py)
if "lancedb" not in sys.modules:
    sys.modules["lancedb"] = MagicMock()

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "python"))

from openem.fhir import (
    LOINC_SYSTEM,
    ICD10_SYSTEM,
    SNOMED_SYSTEM,
    generate_bundle,
    load_presentation,
    validate_bundle,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
PRESENTATIONS_DIR = REPO_ROOT / "fhir" / "presentations"
CORPUS_DIR = REPO_ROOT / "corpus" / "tier1" / "conditions"


class TestLoadPresentation:
    """Test loading presentation profiles."""

    def test_load_anaphylaxis(self):
        profile = load_presentation("anaphylaxis", PRESENTATIONS_DIR)
        assert profile["condition_id"] == "anaphylaxis"
        assert len(profile["presentations"]) >= 1

    def test_load_missing_condition(self):
        with pytest.raises(FileNotFoundError, match="nonexistent"):
            load_presentation("nonexistent", PRESENTATIONS_DIR)

    def test_profile_structure(self):
        profile = load_presentation("anaphylaxis", PRESENTATIONS_DIR)
        pres = profile["presentations"][0]
        assert "name" in pres
        assert "description" in pres
        assert "patient" in pres
        assert "encounter" in pres
        assert "vitals" in pres
        assert "conditions" in pres
        assert "age_range" in pres["patient"]
        assert "sex" in pres["patient"]
        assert len(pres["patient"]["age_range"]) == 2


class TestGenerateBundle:
    """Test FHIR R4 Bundle generation."""

    @pytest.fixture
    def anaphylaxis_profile(self):
        return load_presentation("anaphylaxis", PRESENTATIONS_DIR)

    def test_bundle_structure(self, anaphylaxis_profile):
        bundle = generate_bundle("anaphylaxis", anaphylaxis_profile)
        assert bundle["resourceType"] == "Bundle"
        assert bundle["type"] == "collection"
        assert "entry" in bundle
        assert "timestamp" in bundle
        assert len(bundle["entry"]) > 0

    def test_bundle_contains_patient(self, anaphylaxis_profile):
        bundle = generate_bundle("anaphylaxis", anaphylaxis_profile)
        resource_types = [e["resource"]["resourceType"] for e in bundle["entry"]]
        assert "Patient" in resource_types

    def test_bundle_contains_encounter(self, anaphylaxis_profile):
        bundle = generate_bundle("anaphylaxis", anaphylaxis_profile)
        resource_types = [e["resource"]["resourceType"] for e in bundle["entry"]]
        assert "Encounter" in resource_types

    def test_bundle_contains_condition(self, anaphylaxis_profile):
        bundle = generate_bundle("anaphylaxis", anaphylaxis_profile)
        resource_types = [e["resource"]["resourceType"] for e in bundle["entry"]]
        assert "Condition" in resource_types

    def test_bundle_contains_observations(self, anaphylaxis_profile):
        bundle = generate_bundle("anaphylaxis", anaphylaxis_profile)
        resource_types = [e["resource"]["resourceType"] for e in bundle["entry"]]
        assert resource_types.count("Observation") >= 6  # 6 vitals + 1 lab

    def test_icd10_coding(self, anaphylaxis_profile):
        bundle = generate_bundle("anaphylaxis", anaphylaxis_profile)
        conditions = [
            e["resource"] for e in bundle["entry"]
            if e["resource"]["resourceType"] == "Condition"
        ]
        assert len(conditions) >= 1
        cond = conditions[0]
        codings = cond["code"]["coding"]
        icd10_codes = [c for c in codings if c["system"] == ICD10_SYSTEM]
        assert len(icd10_codes) == 1
        assert icd10_codes[0]["code"] == "T78.2XXA"

    def test_snomed_absent_by_default(self, anaphylaxis_profile):
        bundle = generate_bundle("anaphylaxis", anaphylaxis_profile)
        conditions = [
            e["resource"] for e in bundle["entry"]
            if e["resource"]["resourceType"] == "Condition"
        ]
        for cond in conditions:
            for coding in cond["code"]["coding"]:
                assert coding["system"] != SNOMED_SYSTEM

    def test_loinc_coding_in_observations(self, anaphylaxis_profile):
        bundle = generate_bundle("anaphylaxis", anaphylaxis_profile)
        observations = [
            e["resource"] for e in bundle["entry"]
            if e["resource"]["resourceType"] == "Observation"
        ]
        for obs in observations:
            codings = obs["code"]["coding"]
            loinc_codes = [c for c in codings if c["system"] == LOINC_SYSTEM]
            assert len(loinc_codes) == 1

    def test_deterministic_with_same_seed(self, anaphylaxis_profile):
        bundle1 = generate_bundle("anaphylaxis", anaphylaxis_profile, seed=42)
        bundle2 = generate_bundle("anaphylaxis", anaphylaxis_profile, seed=42)
        assert json.dumps(bundle1, sort_keys=True) == json.dumps(bundle2, sort_keys=True)

    def test_different_seed_different_values(self, anaphylaxis_profile):
        bundle1 = generate_bundle("anaphylaxis", anaphylaxis_profile, seed=42)
        bundle2 = generate_bundle("anaphylaxis", anaphylaxis_profile, seed=99)
        # Patient birth dates should differ with different seeds
        p1 = [e["resource"] for e in bundle1["entry"] if e["resource"]["resourceType"] == "Patient"][0]
        p2 = [e["resource"] for e in bundle2["entry"] if e["resource"]["resourceType"] == "Patient"][0]
        assert p1["birthDate"] != p2["birthDate"]

    def test_vital_values_within_range(self, anaphylaxis_profile):
        bundle = generate_bundle("anaphylaxis", anaphylaxis_profile)
        observations = [
            e["resource"] for e in bundle["entry"]
            if e["resource"]["resourceType"] == "Observation"
        ]
        profile_vitals = anaphylaxis_profile["presentations"][0]["vitals"]
        profile_labs = anaphylaxis_profile["presentations"][0].get("labs", [])
        all_obs_specs = profile_vitals + profile_labs

        for obs, spec in zip(observations, all_obs_specs):
            value = obs["valueQuantity"]["value"]
            min_val, max_val = spec["value_range"]
            assert min_val <= value <= max_val, (
                f"{spec['display']}: {value} not in [{min_val}, {max_val}]"
            )

    def test_presentation_name_selection(self, anaphylaxis_profile):
        bundle = generate_bundle(
            "anaphylaxis", anaphylaxis_profile, presentation_name="classic_adult"
        )
        assert bundle["meta"]["source"] == "openem/anaphylaxis/classic_adult"

    def test_invalid_presentation_name(self, anaphylaxis_profile):
        with pytest.raises(ValueError, match="not found"):
            generate_bundle(
                "anaphylaxis", anaphylaxis_profile,
                presentation_name="nonexistent_type"
            )

    def test_synthetic_tag(self, anaphylaxis_profile):
        bundle = generate_bundle("anaphylaxis", anaphylaxis_profile)
        tags = bundle["meta"]["tag"]
        synthetic_tags = [t for t in tags if t["code"] == "synthetic"]
        assert len(synthetic_tags) == 1

    def test_encounter_esi_priority(self, anaphylaxis_profile):
        bundle = generate_bundle("anaphylaxis", anaphylaxis_profile)
        encounters = [
            e["resource"] for e in bundle["entry"]
            if e["resource"]["resourceType"] == "Encounter"
        ]
        assert len(encounters) == 1
        enc = encounters[0]
        assert "priority" in enc
        assert enc["priority"]["coding"][0]["code"] == "ESI-1"


class TestBundleValidation:
    """Test FHIR R4 validation (requires fhir.resources)."""

    @pytest.fixture
    def anaphylaxis_bundle(self):
        profile = load_presentation("anaphylaxis", PRESENTATIONS_DIR)
        return generate_bundle("anaphylaxis", profile)

    def test_validate_returns_errors_list(self, anaphylaxis_bundle):
        fhir_resources = pytest.importorskip("fhir.resources")
        errors = validate_bundle(anaphylaxis_bundle)
        assert isinstance(errors, list)


class TestAllPresentationProfiles:
    """Parametrized tests across all presentation profiles."""

    @pytest.fixture(params=sorted(PRESENTATIONS_DIR.glob("*.yaml")))
    def profile_path(self, request):
        return request.param

    def test_valid_yaml(self, profile_path):
        """Profile loads as valid YAML."""
        import yaml
        with open(profile_path) as f:
            data = yaml.safe_load(f)
        assert isinstance(data, dict)

    def test_has_condition_id(self, profile_path):
        """Profile has condition_id field."""
        import yaml
        with open(profile_path) as f:
            data = yaml.safe_load(f)
        assert "condition_id" in data
        assert data["condition_id"] == profile_path.stem

    def test_condition_exists_in_corpus(self, profile_path):
        """condition_id has a matching .md in the corpus."""
        import yaml
        with open(profile_path) as f:
            data = yaml.safe_load(f)
        condition_id = data["condition_id"]
        md_path = CORPUS_DIR / f"{condition_id}.md"
        assert md_path.exists(), f"No corpus file for condition '{condition_id}'"

    def test_has_presentations(self, profile_path):
        """Profile has at least one presentation."""
        import yaml
        with open(profile_path) as f:
            data = yaml.safe_load(f)
        assert "presentations" in data
        assert len(data["presentations"]) >= 1

    def test_loinc_code_format(self, profile_path):
        """LOINC codes match expected pattern (digits-digits)."""
        import re
        import yaml
        with open(profile_path) as f:
            data = yaml.safe_load(f)
        loinc_pattern = re.compile(r"^\d+-\d+$")
        for pres in data["presentations"]:
            for vital in pres.get("vitals", []):
                assert loinc_pattern.match(vital["code"]), (
                    f"Invalid LOINC code: {vital['code']}"
                )
            for lab in pres.get("labs", []):
                assert loinc_pattern.match(lab["code"]), (
                    f"Invalid LOINC code: {lab['code']}"
                )

    def test_value_ranges_sane(self, profile_path):
        """Value ranges have min < max."""
        import yaml
        with open(profile_path) as f:
            data = yaml.safe_load(f)
        for pres in data["presentations"]:
            for vital in pres.get("vitals", []):
                min_v, max_v = vital["value_range"]
                assert min_v <= max_v, (
                    f"{vital['display']}: min ({min_v}) > max ({max_v})"
                )
            for lab in pres.get("labs", []):
                min_v, max_v = lab["value_range"]
                assert min_v <= max_v, (
                    f"{lab['display']}: min ({min_v}) > max ({max_v})"
                )

    def test_generates_valid_bundle(self, profile_path):
        """Profile generates a valid FHIR Bundle."""
        import yaml
        with open(profile_path) as f:
            data = yaml.safe_load(f)
        bundle = generate_bundle(data["condition_id"], data)
        assert bundle["resourceType"] == "Bundle"
        assert bundle["type"] == "collection"
        assert len(bundle["entry"]) >= 3  # Patient + Encounter + at least 1 Condition
