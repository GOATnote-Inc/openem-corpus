"""Canonical condition map auto-generated from the OpenEM corpus.

Scans corpus/tier1/conditions/*.md, extracts `id` and `aliases` from
YAML frontmatter, and builds a lookup dict mapping every known name
(lowercased) to a list of condition_ids.

A small manually-curated overlay (overlay.yaml) handles multi-condition
mappings that can't be inferred from a single file (e.g., "neonatal sepsis"
maps to both neonatal-emergencies and sepsis).

Usage:
    from openem.conditions import load_condition_map

    cmap = load_condition_map()            # auto-detect corpus path
    cmap = load_condition_map(corpus_dir)  # explicit path
"""

import re
from pathlib import Path
from typing import Optional

import yaml

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_CONDITIONS_DIR = _REPO_ROOT / "corpus" / "tier1" / "conditions"
_OVERLAY_PATH = Path(__file__).resolve().parent / "overlay.yaml"

_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def _extract_frontmatter(text: str) -> Optional[dict]:
    m = _FM_RE.match(text)
    if not m:
        return None
    return yaml.safe_load(m.group(1))


def load_condition_map(
    corpus_dir: Optional[Path] = None,
    overlay_path: Optional[Path] = None,
) -> dict[str, list[str]]:
    """Build the canonical condition map from corpus frontmatter + overlay.

    Args:
        corpus_dir: Path to corpus/tier1/conditions/. Defaults to the
            standard location relative to this package.
        overlay_path: Path to overlay.yaml. Defaults to the one shipped
            alongside this module.

    Returns:
        Dict mapping lowercased condition names/aliases to lists of
        OpenEM condition_ids (kebab-case).
    """
    corpus_dir = corpus_dir or _CONDITIONS_DIR
    overlay_path = overlay_path or _OVERLAY_PATH

    cmap: dict[str, list[str]] = {}

    # Phase 1: auto-generate from corpus frontmatter
    for md_file in sorted(corpus_dir.glob("*.md")):
        text = md_file.read_text()
        fm = _extract_frontmatter(text)
        if not fm:
            continue

        cid = fm.get("id", "")
        if not cid:
            continue

        # Map the condition id itself
        cmap[cid.lower()] = [cid]

        # Map the full condition name
        condition_name = fm.get("condition", "")
        if condition_name:
            cmap[condition_name.lower()] = [cid]

        # Map all aliases
        for alias in fm.get("aliases", []):
            if alias:
                cmap[alias.lower()] = [cid]

    # Phase 2: merge overlay (overlay wins on conflict)
    if overlay_path.exists():
        overlay = yaml.safe_load(overlay_path.read_text()) or {}
        for key, ids in overlay.items():
            cmap[key.lower()] = ids

    return cmap
