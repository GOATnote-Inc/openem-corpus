"""Tests for audit.py validation passes.

Uses synthetic condition dicts (matching the structure returned by
audit.load_all_conditions) to test each pass in isolation.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from audit import (
    check_cross_file_dosing,
    check_unit_normalization,
    check_dose_range_anomalies,
    check_citations,
    check_duplicates,
    check_icd10,
    check_guideline_currency,
)


# ---- Helpers ----

def make_condition(name, body, fm_overrides=None):
    """Build a synthetic condition dict as returned by audit.load_all_conditions."""
    fm = {
        "id": name,
        "condition": name.replace("-", " ").title(),
        "icd10": ["I21.01"],
        "esi": 1,
        "category": "cardiovascular",
        "track": "tier1",
        "sources": [{"type": "guideline", "ref": "AHA 2023 Guidelines"}],
        "last_updated": "2026-01-01",
        "compiled_by": "agent",
        "risk_tier": "A",
        "validation": {"schema_version": "2.0"},
    }
    if fm_overrides:
        fm.update(fm_overrides)
    return {
        "path": f"/fake/corpus/tier1/conditions/{name}.md",
        "name": name,
        "fm": fm,
        "body": body,
        "text": f"---\n---\n{body}",
    }


# ---- Pass 1: Cross-file dosing ----

class TestCheckCrossFileDosing:
    def test_no_findings_when_single_file(self):
        c = make_condition("stemi", "Give epinephrine 1 mg IV push for cardiac arrest.")
        findings = check_cross_file_dosing([c])
        # Single file -> only one dose string per drug -> no inconsistency
        assert findings == []

    def test_no_findings_when_doses_consistent(self):
        c1 = make_condition("stemi", "epinephrine 1 mg IV for cardiac arrest.")
        c2 = make_condition("sepsis", "epinephrine 1 mg IV for cardiac arrest.")
        findings = check_cross_file_dosing([c1, c2])
        assert findings == []

    def test_flags_inconsistent_doses_across_files(self):
        """More than 3 distinct dose strings for a drug should be flagged."""
        bodies = [
            "Give epinephrine 1 mg IV push.",
            "Give epinephrine 2 mg IV push.",
            "Give epinephrine 3 mg IV push.",
            "Give epinephrine 4 mg IV push.",
        ]
        conditions = [make_condition(f"cond-{i}", b) for i, b in enumerate(bodies)]
        findings = check_cross_file_dosing(conditions)
        epi_findings = [f for f in findings if f.get("drug") == "epinephrine"]
        assert len(epi_findings) >= 1

    def test_finding_has_required_keys(self):
        bodies = [f"Give epinephrine {d} mg IV." for d in [1, 2, 3, 4, 5]]
        conditions = [make_condition(f"c{i}", b) for i, b in enumerate(bodies)]
        findings = check_cross_file_dosing(conditions)
        for f in findings:
            assert "check" in f
            assert "drug" in f
            assert "severity" in f

    def test_empty_conditions_list(self):
        findings = check_cross_file_dosing([])
        assert findings == []


# ---- Pass 2: Unit normalization ----

class TestCheckUnitNormalization:
    def test_flags_ug_unit(self):
        c = make_condition("tox", "Give 50 ug fentanyl IV.")
        findings = check_unit_normalization([c])
        assert any("ug" in f.get("message", "").lower() or "ug" in str(f.get("examples", [])).lower()
                   for f in findings)

    def test_flags_cc_unit(self):
        c = make_condition("fluid", "Give 500 cc normal saline.")
        findings = check_unit_normalization([c])
        assert any("cc" in f.get("message", "").lower() or "cc" in str(f.get("examples", [])).lower()
                   for f in findings)

    def test_flags_gm_unit(self):
        c = make_condition("acetaminophen", "Give 1 gm acetaminophen.")
        findings = check_unit_normalization([c])
        assert any("gm" in f.get("message", "").lower() or "gm" in str(f.get("examples", [])).lower()
                   for f in findings)

    def test_no_findings_for_correct_units(self):
        c = make_condition("stemi", "Give epinephrine 1 mg IV. Norepinephrine 0.1 mcg/kg/min.")
        findings = check_unit_normalization([c])
        assert findings == []

    def test_finding_has_severity_warning(self):
        c = make_condition("tox", "Give 50 ug fentanyl IV.")
        findings = check_unit_normalization([c])
        for f in findings:
            assert f.get("severity") == "warning"

    def test_finding_includes_file_name(self):
        c = make_condition("my-condition", "Give 50 cc saline.")
        findings = check_unit_normalization([c])
        assert any(f.get("file") == "my-condition" for f in findings)


# ---- Pass 3: Dose-range anomaly detection ----

class TestCheckDoseRangeAnomalies:
    def test_flags_epinephrine_iv_overdose(self):
        # Max epinephrine IV single dose is 1.0 mg; 5 mg should be flagged
        c = make_condition("crit", "Give epinephrine 5 mg IV for cardiac arrest.")
        findings = check_dose_range_anomalies([c])
        assert len(findings) >= 1
        assert any(f.get("severity") == "critical" for f in findings)

    def test_epinephrine_normal_dose_not_flagged(self):
        c = make_condition("crit", "Give epinephrine 1 mg IV push.")
        findings = check_dose_range_anomalies([c])
        epi_findings = [f for f in findings if "epinephrine" in f.get("message", "").lower()]
        assert epi_findings == []

    def test_flags_atropine_overdose(self):
        # Max atropine single dose is 5.0 mg
        c = make_condition("bradycardia", "Give atropine 10 mg IV.")
        findings = check_dose_range_anomalies([c])
        assert any("atropine" in f.get("message", "").lower() for f in findings)

    def test_flags_lorazepam_overdose(self):
        # Max lorazepam single dose is 8.0 mg
        c = make_condition("seizure", "Give lorazepam 20 mg IV.")
        findings = check_dose_range_anomalies([c])
        assert any("lorazepam" in f.get("message", "").lower() for f in findings)

    def test_no_findings_for_normal_doses(self):
        c = make_condition("svt", "Give adenosine 6 mg IV rapid push.")
        findings = check_dose_range_anomalies([c])
        adenosine_findings = [f for f in findings if "adenosine" in f.get("message", "").lower()]
        assert adenosine_findings == []

    def test_finding_has_critical_severity(self):
        c = make_condition("overdose-test", "Give epinephrine 10 mg IV.")
        findings = check_dose_range_anomalies([c])
        for f in findings:
            assert f.get("severity") == "critical"


# ---- Pass 4: Citations ----

class TestCheckCitations:
    def test_flags_missing_sources(self):
        c = make_condition("nosource", "Body text here.", fm_overrides={"sources": []})
        findings = check_citations([c])
        assert any(f.get("check") == "citation_presence" for f in findings)

    def test_flags_source_missing_type(self):
        src = {"ref": "Some reference without type"}
        c = make_condition("badtype", "Body.", fm_overrides={"sources": [src]})
        findings = check_citations([c])
        assert any("missing 'type'" in f.get("message", "") for f in findings)

    def test_flags_source_missing_ref(self):
        src = {"type": "guideline"}
        c = make_condition("badref", "Body.", fm_overrides={"sources": [src]})
        findings = check_citations([c])
        assert any("missing 'ref'" in f.get("message", "") for f in findings)

    def test_no_findings_for_valid_source(self):
        src = {"type": "guideline", "ref": "AHA 2023 Guidelines"}
        c = make_condition("good", "Body.", fm_overrides={"sources": [src]})
        findings = check_citations([c])
        assert findings == []

    def test_flags_invalid_pmid_format(self):
        src = {"type": "pubmed", "ref": "Some paper", "pmid": "ABC123"}
        c = make_condition("badpmid", "Body.", fm_overrides={"sources": [src]})
        findings = check_citations([c])
        assert any("PMID" in f.get("message", "") for f in findings)

    def test_valid_pmid_not_flagged(self):
        src = {"type": "pubmed", "ref": "Some paper", "pmid": "12345678"}
        c = make_condition("goodpmid", "Body.", fm_overrides={"sources": [src]})
        findings = check_citations([c])
        pmid_errors = [f for f in findings if "invalid PMID" in f.get("message", "")]
        assert pmid_errors == []

    def test_flags_missing_sources_key(self):
        c = make_condition("nosourceskey", "Body.")
        del c["fm"]["sources"]
        findings = check_citations([c])
        assert any(f.get("check") == "citation_presence" for f in findings)


# ---- Pass 5: Duplicates ----

class TestCheckDuplicates:
    def test_no_findings_for_unique_content(self):
        c1 = make_condition("cond1", "Unique paragraph about condition one management in the emergency department.")
        c2 = make_condition("cond2", "Different paragraph about condition two with separate clinical content.")
        findings = check_duplicates([c1, c2])
        assert findings == []

    def test_detects_duplicate_paragraphs_across_files(self):
        shared = (
            "Administer epinephrine 0.3 mg IM to the lateral thigh for anaphylaxis. "
            "Monitor vital signs and repeat in 5-15 minutes if no improvement."
        )
        c1 = make_condition("allergy", f"{shared}\n\nUnique allergy content here.")
        c2 = make_condition("anaphylaxis", f"{shared}\n\nUnique anaphylaxis content here.")
        findings = check_duplicates([c1, c2])
        dup_findings = [f for f in findings if f.get("check") == "duplicate_content"]
        assert len(dup_findings) >= 1

    def test_duplicate_finding_has_correct_structure(self):
        shared = (
            "This is a shared paragraph that appears in multiple files. "
            "It is long enough to be detected as a duplicate paragraph."
        )
        c1 = make_condition("file1", f"{shared}\n\nUnique to file 1.")
        c2 = make_condition("file2", f"{shared}\n\nUnique to file 2.")
        findings = check_duplicates([c1, c2])
        for f in findings:
            assert "files" in f
            assert "signature" in f
            assert "severity" in f

    def test_empty_conditions_list(self):
        findings = check_duplicates([])
        assert findings == []

    def test_single_condition_no_duplicates(self):
        c = make_condition("solo", "Single condition paragraph here. No other files to compare against.")
        findings = check_duplicates([c])
        assert findings == []


# ---- Pass 7: ICD-10 ----

class TestCheckICD10:
    def test_flags_missing_icd10(self):
        c = make_condition("noid", "Body.", fm_overrides={"icd10": []})
        findings = check_icd10([c])
        assert any(f.get("severity") == "critical" for f in findings)

    def test_flags_invalid_code_format(self):
        c = make_condition("badicd", "Body.", fm_overrides={"icd10": ["123.45"]})
        findings = check_icd10([c])
        assert any("Invalid ICD-10" in f.get("message", "") for f in findings)

    def test_valid_code_not_flagged(self):
        c = make_condition("goodicd", "Body.", fm_overrides={"icd10": ["I21.01"]})
        findings = check_icd10([c])
        assert findings == []

    def test_valid_code_format_letter_digit(self):
        """Codes like A41.9, T39.1X1A must pass."""
        for code in ["A41.9", "T39.1X1A", "J18.9", "K72.00"]:
            c = make_condition("test", "Body.", fm_overrides={"icd10": [code]})
            findings = check_icd10([c])
            invalid = [f for f in findings if "Invalid ICD-10" in f.get("message", "")]
            assert invalid == [], f"Valid code '{code}' was incorrectly flagged"

    def test_code_starting_with_digit_flagged(self):
        c = make_condition("bad", "Body.", fm_overrides={"icd10": ["9AB.1"]})
        findings = check_icd10([c])
        assert any("Invalid ICD-10" in f.get("message", "") for f in findings)

    def test_multiple_codes_both_checked(self):
        c = make_condition("multi", "Body.", fm_overrides={"icd10": ["I21.01", "BAD_CODE"]})
        findings = check_icd10([c])
        invalid = [f for f in findings if "Invalid ICD-10" in f.get("message", "")]
        assert len(invalid) >= 1


# ---- Pass 8: Guideline currency ----

class TestCheckGuidelineCurrency:
    def test_flags_outdated_2010_aha(self):
        src = {"type": "guideline", "ref": "2010 AHA Guidelines for CPR"}
        c = make_condition("cpr", "Body.", fm_overrides={"sources": [src]})
        findings = check_guideline_currency([c])
        assert len(findings) >= 1
        assert any("2010 AHA" in f.get("message", "") for f in findings)

    def test_flags_outdated_2012_aha(self):
        src = {"type": "guideline", "ref": "2012 AHA Heart Failure Guidelines"}
        c = make_condition("hf", "Body.", fm_overrides={"sources": [src]})
        findings = check_guideline_currency([c])
        assert len(findings) >= 1

    def test_no_finding_for_current_guideline(self):
        src = {"type": "guideline", "ref": "2023 AHA/ACC Guidelines for Chest Pain"}
        c = make_condition("cp", "Body.", fm_overrides={"sources": [src]})
        findings = check_guideline_currency([c])
        assert findings == []

    def test_finding_has_info_severity(self):
        src = {"type": "guideline", "ref": "2012 ESC Guidelines"}
        c = make_condition("esc", "Body.", fm_overrides={"sources": [src]})
        findings = check_guideline_currency([c])
        for f in findings:
            assert f.get("severity") == "info"

    def test_finding_includes_file_name(self):
        src = {"type": "guideline", "ref": "ACLS 2010 Guidelines"}
        c = make_condition("acls-test", "Body.", fm_overrides={"sources": [src]})
        findings = check_guideline_currency([c])
        assert any(f.get("file") == "acls-test" for f in findings)

    def test_empty_sources_no_findings(self):
        c = make_condition("nosrc", "Body.", fm_overrides={"sources": []})
        findings = check_guideline_currency([c])
        assert findings == []
