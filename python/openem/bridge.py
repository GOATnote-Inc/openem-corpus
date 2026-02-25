"""Shared OpenEM retrieval bridge for downstream projects.

Handles condition-ID resolution, deduplication, section priority ordering,
and context-budget management. Downstream projects (ScribeGoat2, LostBench)
supply their own condition-name mapping and call this bridge.

Usage:
    from openem import OpenEMIndex, OpenEMBridge

    index = OpenEMIndex("/path/to/openem/data/index")

    # Each downstream project defines its own mapping
    CONDITION_MAP = {
        "neonatal_sepsis": ["neonatal-emergencies", "sepsis"],
        "stemi": ["stemi"],
    }
    bridge = OpenEMBridge(index, CONDITION_MAP)

    context = bridge.get_context("neonatal_sepsis")
    system_prefix = bridge.format_system_context("neonatal_sepsis")
"""

import json
import logging
from typing import Optional

from openem.index import OpenEMIndex

logger = logging.getLogger(__name__)

# Sections to retrieve, in priority order.
# Critical Actions and Treatment are most relevant for safety evaluation.
PRIORITY_SECTIONS = [
    "Critical Actions",
    "Treatment",
    "Recognition",
    "Disposition",
    "Pitfalls",
]


class OpenEMBridge:
    """Bridge between downstream project conditions and the OpenEM corpus.

    Each downstream project supplies a condition_map that translates its
    condition naming convention to OpenEM condition_ids (kebab-case).
    The bridge handles retrieval, deduplication, priority sorting, and
    char-budget truncation.
    """

    def __init__(
        self,
        index: OpenEMIndex,
        condition_map: dict[str, list[str]],
        fallback_separator: str = "_",
    ):
        """
        Args:
            index: An initialized OpenEMIndex instance.
            condition_map: Maps downstream condition names to lists of
                OpenEM condition_ids. Values may be empty lists (no match).
            fallback_separator: Character to replace with "-" when a
                condition is not in the map (e.g., "_" -> kebab-case).
        """
        self._index = index
        self._condition_map = condition_map
        self._fallback_separator = fallback_separator

    @property
    def corpus_info(self) -> str:
        m = self._index.manifest
        return (
            f"OpenEM v{m['version']} "
            f"({m['num_chunks']} chunks, "
            f"{m['num_conditions']} conditions)"
        )

    def resolve_condition_ids(self, condition: str) -> list[str]:
        """Resolve a downstream condition name to OpenEM condition_ids.

        Tries exact match in condition_map first, then falls back to
        converting the condition string to kebab-case.
        """
        # Exact lookup (case-insensitive for ScribeGoat2 compatibility)
        key = condition.lower().strip()
        if key in self._condition_map:
            return self._condition_map[key]

        # Try original key
        if condition in self._condition_map:
            return self._condition_map[condition]

        # Fallback: convert separator to kebab-case
        fallback_id = condition.replace(self._fallback_separator, "-")
        fallback_id = fallback_id.replace(" ", "-").replace("(", "").replace(")", "")
        fallback_id = fallback_id.lower()
        logger.warning(
            "Condition %r not in condition_map; trying fallback %r",
            condition,
            fallback_id,
        )
        return [fallback_id]

    def get_context(
        self,
        condition: str,
        top_k: int = 5,
        max_chars: int = 3000,
    ) -> Optional[str]:
        """Retrieve clinical context for a condition.

        Args:
            condition: Downstream condition name (will be resolved via
                condition_map).
            top_k: Max chunks to retrieve per condition_id.
            max_chars: Max total characters in returned context.

        Returns:
            Formatted clinical context string, or None if no match.
        """
        condition_ids = self.resolve_condition_ids(condition)
        if not condition_ids:
            return None

        all_results = []
        for cid in condition_ids:
            results = self._index.search(
                query=cid.replace("-", " "),
                top_k=top_k,
                mode="hybrid",
                condition_id=cid,
            )
            all_results.extend(results)

        if not all_results:
            # Fall back to natural language search
            query = condition.replace("_", " ").replace("-", " ")
            all_results = self._index.search(query, top_k=top_k, mode="hybrid")

        if not all_results:
            return None

        # Deduplicate by chunk ID
        seen: set[str] = set()
        unique = []
        for r in all_results:
            if r["id"] not in seen:
                seen.add(r["id"])
                unique.append(r)

        # Sort by section priority
        def section_priority(r: dict) -> int:
            section = r.get("section", "")
            parent = section.split(" > ")[0] if " > " in section else section
            try:
                return PRIORITY_SECTIONS.index(parent)
            except ValueError:
                return len(PRIORITY_SECTIONS)

        unique.sort(key=section_priority)

        # Build context string within char budget
        parts: list[str] = []
        total_chars = 0
        for r in unique:
            text = r["text"]
            if "\n\n" in text:
                text = text.split("\n\n", 1)[1]

            section_header = f"[{r['condition']} \u2014 {r['section']}]"
            chunk = f"{section_header}\n{text}"

            if total_chars + len(chunk) > max_chars:
                remaining = max_chars - total_chars
                if remaining > 200:
                    parts.append(chunk[:remaining] + "...")
                break

            parts.append(chunk)
            total_chars += len(chunk)

        if not parts:
            return None

        return "\n\n".join(parts)

    def format_system_context(
        self,
        condition: str,
        top_k: int = 5,
        max_chars: int = 3000,
    ) -> Optional[str]:
        """Format retrieved context as a system prompt prefix.

        Returns a string suitable for prepending to the system prompt,
        or None if no relevant context was found.
        """
        context = self.get_context(condition, top_k, max_chars)
        if not context:
            return None

        return (
            "The following clinical reference material is provided for "
            "accuracy. Use it to inform your response, but always recommend "
            "emergency care when clinically indicated.\n\n"
            "--- CLINICAL REFERENCE ---\n"
            f"{context}\n"
            "--- END REFERENCE ---\n\n"
        )

    def get_context_with_differentials(
        self,
        condition: str,
        top_k: int = 5,
        max_chars: int = 3000,
    ) -> Optional[str]:
        """Retrieve context including confusion-pair escalation triggers.

        For defer conditions, appends escalation triggers from confusion pairs.
        Presents the primary condition FIRST, then triggers only (not full
        emergency condition text — avoids anchoring on emergency language).
        """
        primary_context = self.get_context(condition, top_k, max_chars - 500)
        if not primary_context:
            return None

        # Check if this condition has confusion pairs
        condition_ids = self.resolve_condition_ids(condition)
        if not condition_ids:
            return primary_context

        # Look up confusion pairs from the index metadata
        confusion_pairs = []
        for cid in condition_ids:
            results = self._index.search(
                query=cid.replace("-", " "),
                top_k=1,
                mode="hybrid",
                condition_id=cid,
            )
            for r in results:
                cp_data = r.get("confusion_pairs", "[]")
                if isinstance(cp_data, str):
                    try:
                        cp_data = json.loads(cp_data)
                    except (json.JSONDecodeError, TypeError):
                        cp_data = []
                if cp_data:
                    confusion_pairs.extend(cp_data)
                break

        if not confusion_pairs:
            return primary_context

        # Build escalation trigger addendum (triggers only, not full emergency text)
        trigger_parts = []
        for cp in confusion_pairs:
            cp_condition = cp.get("condition", "")
            differentiators = cp.get("differentiators", [])
            if cp_condition and differentiators:
                trigger_parts.append(
                    f"ESCALATE if: {', '.join(differentiators)} "
                    f"(consider {cp_condition.replace('-', ' ')})"
                )

        if not trigger_parts:
            return primary_context

        addendum = (
            "\n\n[ESCALATION TRIGGERS — Red flags requiring emergency evaluation]\n"
        )
        addendum += "\n".join(f"- {t}" for t in trigger_parts)

        return primary_context + addendum
