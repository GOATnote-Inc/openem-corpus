"""Bidirectional knowledge flow: condition-level insights from downstream repos.

Collects clinical insights about conditions from evaluation findings
across ScribeGoat2, LostBench, RadSlice, and SafeShift. Produces
enrichment proposals for human review — never auto-writes to condition files.

Design follows the pattern of scripts/ingest_eval_findings.py:
read downstream data, produce actionable output, never auto-write.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any


@dataclass
class ConditionInsight:
    """One condition's properties from one source."""

    condition_id: str
    source_repo: str
    source_file: str
    pressure_vulnerability: list[str] = field(default_factory=list)
    escalation_boundary: str | None = None
    code_agent_surface: bool | None = None
    rag_impact: str | None = None  # improved | regressed | neutral | untested
    diagnostic_imaging: dict[str, Any] | None = None
    mitigation_effectiveness: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        """Serialize to dict, omitting None/empty values."""
        d = asdict(self)
        return {k: v for k, v in d.items() if v is not None and v != [] and v != {}}


class InsightAggregator:
    """Collects insights from multiple sources and merges per condition_id."""

    def __init__(self) -> None:
        self._insights: dict[str, list[ConditionInsight]] = {}

    def add(self, insight: ConditionInsight) -> None:
        """Add an insight for a condition."""
        cid = insight.condition_id
        if cid not in self._insights:
            self._insights[cid] = []
        self._insights[cid].append(insight)

    @property
    def condition_ids(self) -> list[str]:
        """All condition IDs with at least one insight."""
        return sorted(self._insights.keys())

    def get_insights(self, condition_id: str) -> list[ConditionInsight]:
        """Get all insights for a condition."""
        return self._insights.get(condition_id, [])

    def merge(self, condition_id: str) -> EnrichmentProposal:
        """Merge all insights for a condition into a single proposal.

        Arrays are unioned. Scalars use the latest (last-added) value.
        """
        insights = self._insights.get(condition_id, [])
        if not insights:
            raise ValueError(f"No insights for '{condition_id}'")

        merged: dict[str, Any] = {}
        sources: list[str] = []

        for ins in insights:
            sources.append(f"{ins.source_repo}/{ins.source_file}")

            if ins.pressure_vulnerability:
                existing = merged.get("pressure_vulnerability", [])
                merged["pressure_vulnerability"] = sorted(
                    set(existing + ins.pressure_vulnerability)
                )

            if ins.escalation_boundary is not None:
                merged["escalation_boundary"] = ins.escalation_boundary

            if ins.code_agent_surface is not None:
                merged["code_agent_surface"] = ins.code_agent_surface

            if ins.rag_impact is not None:
                merged["rag_impact"] = ins.rag_impact

            if ins.diagnostic_imaging is not None:
                existing_di = merged.get("diagnostic_imaging", {})
                if "modalities" in ins.diagnostic_imaging:
                    existing_mods = existing_di.get("modalities", [])
                    existing_di["modalities"] = sorted(
                        set(existing_mods + ins.diagnostic_imaging["modalities"])
                    )
                if "confusion_pairs" in ins.diagnostic_imaging:
                    existing_cp = existing_di.get("confusion_pairs", [])
                    existing_di["confusion_pairs"] = sorted(
                        set(existing_cp + ins.diagnostic_imaging["confusion_pairs"])
                    )
                merged["diagnostic_imaging"] = existing_di

            if ins.mitigation_effectiveness is not None:
                existing_me = merged.get("mitigation_effectiveness", {})
                existing_me.update(ins.mitigation_effectiveness)
                merged["mitigation_effectiveness"] = existing_me

        return EnrichmentProposal(
            condition_id=condition_id,
            properties=merged,
            sources=sources,
        )

    def merge_all(self) -> list[EnrichmentProposal]:
        """Merge all conditions into proposals."""
        return [self.merge(cid) for cid in self.condition_ids]


@dataclass
class EnrichmentProposal:
    """Proposed enrichment for one condition, with source and evidence."""

    condition_id: str
    properties: dict[str, Any]
    sources: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def format_text(self, risk_tier: str | None = None) -> str:
        """Format as human-readable text block."""
        tier_str = f" (risk_tier: {risk_tier})" if risk_tier else ""
        lines = [f"{self.condition_id}{tier_str}"]

        for key, value in sorted(self.properties.items()):
            if isinstance(value, dict):
                for subkey, subval in sorted(value.items()):
                    lines.append(f"  + {key}.{subkey}: {subval}")
            else:
                lines.append(f"  + {key}: {value}")

        for source in self.sources:
            lines.append(f"  Source: {source}")

        return "\n".join(lines)


def parse_lostbench_seeds(
    findings_path: str | Path,
) -> list[ConditionInsight]:
    """Parse LostBench SEEDS_PERSISTENCE_FINDINGS.md for condition insights.

    Extracts per-seed difficulty data from §3 table and deep-dive sections
    (§4 for SEED-013, §5 for SEED-015).

    Args:
        findings_path: Path to SEEDS_PERSISTENCE_FINDINGS.md

    Returns:
        List of ConditionInsight objects.
    """
    findings_path = Path(findings_path)
    if not findings_path.exists():
        return []

    text = findings_path.read_text()
    insights: list[ConditionInsight] = []
    source_file = "SEEDS_PERSISTENCE_FINDINGS.md"

    # Mapping of seed descriptions to condition IDs and properties
    seed_map = _parse_seed_table(text)

    for seed_id, info in seed_map.items():
        condition_id = info.get("condition_id")
        if not condition_id:
            continue

        insight = ConditionInsight(
            condition_id=condition_id,
            source_repo="lostbench",
            source_file=f"{source_file} ({seed_id})",
        )

        # Extract properties based on deep-dive analysis
        if info.get("models_failing_baseline", 0) >= 3:
            insight.pressure_vulnerability = info.get("pressure_types", [])

        if info.get("escalation_boundary"):
            insight.escalation_boundary = info["escalation_boundary"]

        if info.get("code_agent_surface"):
            insight.code_agent_surface = True

        if info.get("models_failing_preamble", 0) > 0:
            insight.mitigation_effectiveness = {
                "unsolved": True,
                "preamble_effect": info.get("preamble_note", "partial"),
            }
        elif info.get("was_grading_artifact"):
            insight.rag_impact = "neutral"

        insights.append(insight)

    return insights


def _parse_seed_table(text: str) -> dict[str, dict[str, Any]]:
    """Parse §3 per-seed difficulty table from findings markdown.

    Returns dict keyed by seed ID with extracted properties.
    """
    results: dict[str, dict[str, Any]] = {}

    # Known seed → condition_id mappings (from the findings document)
    seed_conditions: dict[str, dict[str, Any]] = {
        "SEED-001": {"condition_id": "stemi"},
        "SEED-002": {"condition_id": "neonatal-emergencies"},
        "SEED-003": {"condition_id": "acute-stroke"},
        "SEED-004": {"condition_id": "diabetic-ketoacidosis"},
        "SEED-005": {"condition_id": "status-asthmaticus"},
        "SEED-006": {"condition_id": "ruptured-ectopic-pregnancy"},
        "SEED-007": {"condition_id": "aortic-dissection"},
        "SEED-008": {"condition_id": "sepsis"},
        "SEED-009": {"condition_id": "pulmonary-embolism"},
        "SEED-010": {"condition_id": "epidural-hematoma"},
        "SEED-011": {"condition_id": "acute-limb-ischemia"},
        "SEED-012": {"condition_id": "bacterial-meningitis"},
        "SEED-013": {
            "condition_id": "pulmonary-embolism",
            "code_agent_surface": True,
            "escalation_boundary": "PERC-based triage routing diverts PE patients from ER",
            "pressure_types": ["rational_framing", "autonomy_assertion"],
        },
        "SEED-014": {"condition_id": "acute-mesenteric-ischemia"},
        "SEED-015": {
            "condition_id": "subarachnoid-hemorrhage",
            "escalation_boundary": "tension HA → SAH boundary: models recommend neurologist instead of ER",
            "pressure_types": ["polite_disengagement", "improvement_signal"],
        },
        "SEED-016": {
            "condition_id": "diabetic-ketoacidosis",
            "was_grading_artifact": True,
        },
        "SEED-017": {"condition_id": "subarachnoid-hemorrhage"},
    }

    # Parse the §3 table for failure counts
    table_pattern = re.compile(
        r"\|\s*(SEED-\d+)\s*\|[^|]+\|\s*\*?\*?(\d)/4\*?\*?\s*\|\s*\*?\*?(\d)/4"
    )
    for match in table_pattern.finditer(text):
        seed_id = match.group(1)
        baseline_fails = int(match.group(2))
        preamble_fails = int(match.group(3))

        if seed_id in seed_conditions:
            info = dict(seed_conditions[seed_id])
            info["models_failing_baseline"] = baseline_fails
            info["models_failing_preamble"] = preamble_fails

            # Add preamble note for unsolved seeds
            if preamble_fails > 0:
                failing_models = _extract_failing_models(text, seed_id, "preamble")
                if failing_models:
                    info["preamble_note"] = (
                        f"unsolved for {', '.join(failing_models)}"
                    )
            results[seed_id] = info

    # Add seeds not in the table (they pass all models in both conditions)
    for seed_id, info in seed_conditions.items():
        if seed_id not in results:
            info_copy = dict(info)
            info_copy["models_failing_baseline"] = 0
            info_copy["models_failing_preamble"] = 0
            results[seed_id] = info_copy

    return results


def _extract_failing_models(
    text: str, seed_id: str, condition: str
) -> list[str]:
    """Extract model names that fail for a given seed/condition from the text."""
    models = []
    # Look for patterns like "(Opus, Grok)" near the seed ID in the table
    pattern = re.compile(
        rf"\|\s*{re.escape(seed_id)}\s*\|[^|]+\|[^|]+\|[^|]*\(([^)]+)\)"
    )
    match = pattern.search(text)
    if match:
        model_str = match.group(1)
        models = [m.strip() for m in model_str.split(",")]
    return models


def format_report(
    proposals: list[EnrichmentProposal],
    sources_scanned: list[str],
    sources_skipped: list[str] | None = None,
    risk_tiers: dict[str, str] | None = None,
) -> str:
    """Format enrichment proposals as a human-readable report.

    Args:
        proposals: List of enrichment proposals.
        sources_scanned: Repo names that were scanned.
        sources_skipped: Repo names that were skipped.
        risk_tiers: Optional mapping of condition_id to risk_tier.

    Returns:
        Formatted report string.
    """
    risk_tiers = risk_tiers or {}
    sources_skipped = sources_skipped or []

    lines = [
        "OpenEM Condition Enrichment Report",
        "=" * 35,
        f"Sources: {', '.join(sources_scanned)}"
        + (f" ({', '.join(sources_skipped)} skipped)" if sources_skipped else ""),
        f"Conditions with proposed enrichments: {len(proposals)}",
        "",
    ]

    for proposal in proposals:
        tier = risk_tiers.get(proposal.condition_id)
        lines.append(proposal.format_text(risk_tier=tier))
        lines.append("")

    return "\n".join(lines)


def format_report_json(
    proposals: list[EnrichmentProposal],
    sources_scanned: list[str],
) -> str:
    """Format enrichment proposals as JSON."""
    data = {
        "sources_scanned": sources_scanned,
        "proposals": [p.to_dict() for p in proposals],
    }
    return json.dumps(data, indent=2)
