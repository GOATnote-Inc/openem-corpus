"""Tests for bidirectional knowledge flow — condition insights and aggregation."""

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

from openem.insights import (
    ConditionInsight,
    EnrichmentProposal,
    InsightAggregator,
    format_report,
    format_report_json,
    parse_lostbench_seeds,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
LOSTBENCH_DIR = Path.home() / "lostbench"


class TestConditionInsight:
    """Test ConditionInsight construction and serialization."""

    def test_basic_construction(self):
        insight = ConditionInsight(
            condition_id="pulmonary-embolism",
            source_repo="lostbench",
            source_file="SEEDS_PERSISTENCE_FINDINGS.md (SEED-013)",
            code_agent_surface=True,
        )
        assert insight.condition_id == "pulmonary-embolism"
        assert insight.code_agent_surface is True

    def test_to_dict_omits_none(self):
        insight = ConditionInsight(
            condition_id="stemi",
            source_repo="lostbench",
            source_file="test.md",
        )
        d = insight.to_dict()
        assert "condition_id" in d
        assert "source_repo" in d
        assert "rag_impact" not in d  # None should be omitted
        assert "pressure_vulnerability" not in d  # Empty list omitted

    def test_to_dict_includes_values(self):
        insight = ConditionInsight(
            condition_id="subarachnoid-hemorrhage",
            source_repo="lostbench",
            source_file="test.md",
            pressure_vulnerability=["polite_disengagement", "improvement_signal"],
            escalation_boundary="tension HA → SAH boundary",
        )
        d = insight.to_dict()
        assert d["pressure_vulnerability"] == ["polite_disengagement", "improvement_signal"]
        assert d["escalation_boundary"] == "tension HA → SAH boundary"

    def test_default_values(self):
        insight = ConditionInsight(
            condition_id="test",
            source_repo="test",
            source_file="test",
        )
        assert insight.pressure_vulnerability == []
        assert insight.escalation_boundary is None
        assert insight.code_agent_surface is None
        assert insight.rag_impact is None
        assert insight.diagnostic_imaging is None
        assert insight.mitigation_effectiveness is None


class TestInsightAggregator:
    """Test insight merging from multiple sources."""

    def test_single_source(self):
        agg = InsightAggregator()
        agg.add(ConditionInsight(
            condition_id="stemi",
            source_repo="lostbench",
            source_file="test.md",
            pressure_vulnerability=["financial_barrier"],
        ))
        proposal = agg.merge("stemi")
        assert proposal.condition_id == "stemi"
        assert proposal.properties["pressure_vulnerability"] == ["financial_barrier"]

    def test_merge_two_sources_union_arrays(self):
        agg = InsightAggregator()
        agg.add(ConditionInsight(
            condition_id="pulmonary-embolism",
            source_repo="lostbench",
            source_file="seeds.md",
            pressure_vulnerability=["rational_framing"],
        ))
        agg.add(ConditionInsight(
            condition_id="pulmonary-embolism",
            source_repo="scribegoat2",
            source_file="findings.md",
            pressure_vulnerability=["autonomy_assertion"],
        ))
        proposal = agg.merge("pulmonary-embolism")
        assert sorted(proposal.properties["pressure_vulnerability"]) == [
            "autonomy_assertion", "rational_framing"
        ]
        assert len(proposal.sources) == 2

    def test_merge_two_sources_latest_scalar(self):
        agg = InsightAggregator()
        agg.add(ConditionInsight(
            condition_id="stemi",
            source_repo="lostbench",
            source_file="a.md",
            rag_impact="neutral",
        ))
        agg.add(ConditionInsight(
            condition_id="stemi",
            source_repo="scribegoat2",
            source_file="b.md",
            rag_impact="improved",
        ))
        proposal = agg.merge("stemi")
        assert proposal.properties["rag_impact"] == "improved"

    def test_merge_imaging_modalities(self):
        agg = InsightAggregator()
        agg.add(ConditionInsight(
            condition_id="stemi",
            source_repo="radslice",
            source_file="tasks/",
            diagnostic_imaging={"modalities": ["xray"]},
        ))
        agg.add(ConditionInsight(
            condition_id="stemi",
            source_repo="radslice",
            source_file="tasks/",
            diagnostic_imaging={"modalities": ["ct", "xray"]},
        ))
        proposal = agg.merge("stemi")
        assert sorted(proposal.properties["diagnostic_imaging"]["modalities"]) == [
            "ct", "xray"
        ]

    def test_condition_ids(self):
        agg = InsightAggregator()
        agg.add(ConditionInsight("b-cond", "repo", "file"))
        agg.add(ConditionInsight("a-cond", "repo", "file"))
        assert agg.condition_ids == ["a-cond", "b-cond"]

    def test_merge_nonexistent(self):
        agg = InsightAggregator()
        with pytest.raises(ValueError, match="No insights"):
            agg.merge("nonexistent")

    def test_merge_all(self):
        agg = InsightAggregator()
        agg.add(ConditionInsight("a", "r", "f", pressure_vulnerability=["x"]))
        agg.add(ConditionInsight("b", "r", "f", rag_impact="neutral"))
        proposals = agg.merge_all()
        assert len(proposals) == 2
        assert proposals[0].condition_id == "a"
        assert proposals[1].condition_id == "b"


class TestLostBenchParser:
    """Test LostBench SEEDS_PERSISTENCE_FINDINGS.md parser."""

    def test_parse_from_actual_file(self):
        """Parse the real findings file if LostBench is available."""
        findings_path = LOSTBENCH_DIR / "SEEDS_PERSISTENCE_FINDINGS.md"
        if not findings_path.exists():
            pytest.skip("LostBench repo not found")

        insights = parse_lostbench_seeds(findings_path)
        assert len(insights) > 0

        # SEED-013 should produce PE insight with code_agent_surface
        pe_insights = [
            i for i in insights if i.condition_id == "pulmonary-embolism"
        ]
        assert len(pe_insights) >= 1
        pe_code = [i for i in pe_insights if i.code_agent_surface]
        assert len(pe_code) >= 1

        # SEED-015 should produce SAH insight with escalation_boundary
        sah_insights = [
            i for i in insights
            if i.condition_id == "subarachnoid-hemorrhage"
            and i.escalation_boundary is not None
        ]
        assert len(sah_insights) >= 1

    def test_parse_missing_file(self):
        insights = parse_lostbench_seeds("/nonexistent/path.md")
        assert insights == []

    def test_parse_extracts_seed_013(self):
        """SEED-013 PE code-agent should be extracted."""
        findings_path = LOSTBENCH_DIR / "SEEDS_PERSISTENCE_FINDINGS.md"
        if not findings_path.exists():
            pytest.skip("LostBench repo not found")

        insights = parse_lostbench_seeds(findings_path)
        pe_code = [
            i for i in insights
            if i.condition_id == "pulmonary-embolism"
            and i.code_agent_surface is True
        ]
        assert len(pe_code) >= 1
        pe = pe_code[0]
        assert pe.escalation_boundary is not None
        assert "PERC" in pe.escalation_boundary or "triage" in pe.escalation_boundary

    def test_parse_extracts_seed_016_artifact(self):
        """SEED-016 DKA should be flagged as grading artifact."""
        findings_path = LOSTBENCH_DIR / "SEEDS_PERSISTENCE_FINDINGS.md"
        if not findings_path.exists():
            pytest.skip("LostBench repo not found")

        insights = parse_lostbench_seeds(findings_path)
        dka_insights = [
            i for i in insights
            if i.condition_id == "diabetic-ketoacidosis"
            and i.rag_impact == "neutral"
        ]
        assert len(dka_insights) >= 1


class TestReportGeneration:
    """Test text and JSON report formatting."""

    @pytest.fixture
    def sample_proposals(self):
        return [
            EnrichmentProposal(
                condition_id="pulmonary-embolism",
                properties={
                    "pressure_vulnerability": ["rational_framing", "autonomy_assertion"],
                    "code_agent_surface": True,
                    "escalation_boundary": "PERC-based triage routing",
                    "mitigation_effectiveness": {"unsolved": True},
                },
                sources=["lostbench/SEEDS_PERSISTENCE_FINDINGS.md (SEED-013)"],
            ),
            EnrichmentProposal(
                condition_id="subarachnoid-hemorrhage",
                properties={
                    "pressure_vulnerability": ["polite_disengagement", "improvement_signal"],
                    "escalation_boundary": "tension HA → SAH boundary",
                },
                sources=["lostbench/SEEDS_PERSISTENCE_FINDINGS.md (SEED-015)"],
            ),
        ]

    def test_text_report_structure(self, sample_proposals):
        report = format_report(
            sample_proposals,
            sources_scanned=["lostbench"],
            sources_skipped=["safeshift"],
            risk_tiers={"pulmonary-embolism": "A", "subarachnoid-hemorrhage": "A"},
        )
        assert "OpenEM Condition Enrichment Report" in report
        assert "pulmonary-embolism (risk_tier: A)" in report
        assert "subarachnoid-hemorrhage (risk_tier: A)" in report
        assert "code_agent_surface: True" in report
        assert "lostbench" in report
        assert "safeshift skipped" in report
        assert "Conditions with proposed enrichments: 2" in report

    def test_json_report_structure(self, sample_proposals):
        report = format_report_json(
            sample_proposals,
            sources_scanned=["lostbench"],
        )
        data = json.loads(report)
        assert "sources_scanned" in data
        assert "proposals" in data
        assert len(data["proposals"]) == 2
        assert data["proposals"][0]["condition_id"] == "pulmonary-embolism"

    def test_proposal_format_text(self):
        proposal = EnrichmentProposal(
            condition_id="stemi",
            properties={"rag_impact": "improved"},
            sources=["scribegoat2/FINDINGS.md"],
        )
        text = proposal.format_text(risk_tier="A")
        assert "stemi (risk_tier: A)" in text
        assert "rag_impact: improved" in text
        assert "Source: scribegoat2/FINDINGS.md" in text
