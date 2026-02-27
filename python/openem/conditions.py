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

import hashlib
import json
import logging
import re
from pathlib import Path
from typing import Optional

import yaml

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_CONDITIONS_DIR = _REPO_ROOT / "corpus" / "tier1" / "conditions"
_OVERLAY_PATH = Path(__file__).resolve().parent / "overlay.yaml"
_SIDECAR_PATH = Path(__file__).resolve().parent / "condition_map.json"

_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)

log = logging.getLogger(__name__)


def _extract_frontmatter(text: str) -> Optional[dict]:
    m = _FM_RE.match(text)
    if not m:
        return None
    return yaml.safe_load(m.group(1))


def _corpus_fingerprint(corpus_dir: Path) -> str:
    """Compute a fingerprint from sorted filenames + sizes in the corpus dir."""
    entries = []
    for md_file in sorted(corpus_dir.glob("*.md")):
        entries.append(f"{md_file.name}:{md_file.stat().st_size}")
    return hashlib.sha256("\n".join(entries).encode()).hexdigest()[:16]


def validate_overlay(
    corpus_dir: Optional[Path] = None,
    overlay_path: Optional[Path] = None,
) -> list[str]:
    """Validate that every overlay target ID exists as a .md file in the corpus.

    Returns:
        List of error strings. Empty list = valid.
    """
    corpus_dir = corpus_dir or _CONDITIONS_DIR
    overlay_path = overlay_path or _OVERLAY_PATH

    if not overlay_path.exists():
        return []

    overlay = yaml.safe_load(overlay_path.read_text()) or {}
    valid_ids = {f.stem for f in corpus_dir.glob("*.md")}
    errors = []

    for key, ids in overlay.items():
        if not isinstance(ids, list):
            errors.append(f"overlay key '{key}': value must be a list, got {type(ids).__name__}")
            continue
        for cid in ids:
            if cid and cid not in valid_ids:
                errors.append(
                    f"overlay key '{key}': target '{cid}' has no matching .md file in corpus"
                )

    return errors


def load_condition_map(
    corpus_dir: Optional[Path] = None,
    overlay_path: Optional[Path] = None,
) -> dict[str, list[str]]:
    """Build the canonical condition map from corpus frontmatter + overlay.

    Uses a JSON sidecar cache for fast loads when the corpus hasn't changed.

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

    # Try sidecar cache first
    fingerprint = _corpus_fingerprint(corpus_dir)
    if _SIDECAR_PATH.exists():
        try:
            cached = json.loads(_SIDECAR_PATH.read_text())
            if cached.get("fingerprint") == fingerprint:
                return cached["map"]
        except (json.JSONDecodeError, KeyError):
            pass

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


def save_condition_map_sidecar(
    corpus_dir: Optional[Path] = None,
    overlay_path: Optional[Path] = None,
    sidecar_path: Optional[Path] = None,
) -> Path:
    """Build condition map and write JSON sidecar cache.

    Called by build_index.py during index build. Not needed for normal usage.

    Returns:
        Path to the written sidecar file.
    """
    corpus_dir = corpus_dir or _CONDITIONS_DIR
    sidecar_path = sidecar_path or _SIDECAR_PATH

    cmap = load_condition_map(corpus_dir=corpus_dir, overlay_path=overlay_path)
    fingerprint = _corpus_fingerprint(corpus_dir)

    sidecar = {
        "fingerprint": fingerprint,
        "num_entries": len(cmap),
        "map": cmap,
    }
    sidecar_path.write_text(json.dumps(sidecar, indent=2) + "\n")
    return sidecar_path
