#!/usr/bin/env python3
"""Apply evaluation_properties from scan_repos proposals to condition frontmatter.

Reads proposals from scan_repos JSON output, resolves condition IDs through
the overlay, and updates condition frontmatter with evaluation_properties.

Usage:
    python scripts/apply_eval_properties.py evaluation/scan_repos_v051.json
    python scripts/apply_eval_properties.py evaluation/scan_repos_v051.json --dry-run
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "python"))


def load_overlay(overlay_path: Path) -> dict[str, list[str]]:
    """Load overlay mappings from YAML."""
    try:
        import yaml
    except ImportError:
        # Fallback: parse simple YAML manually
        overlay = {}
        text = overlay_path.read_text()
        for line in text.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            match = re.match(r'"([^"]+)":\s*\[([^\]]*)\]', line)
            if match:
                key = match.group(1)
                vals_str = match.group(2).strip()
                if vals_str:
                    vals = [v.strip().strip('"') for v in vals_str.split(",")]
                else:
                    vals = []
                overlay[key] = vals
        return overlay

    with open(overlay_path) as f:
        data = yaml.safe_load(f)
    return data or {}


def resolve_condition_id(
    raw_id: str,
    existing_ids: set[str],
    overlay: dict[str, list[str]],
) -> list[str]:
    """Resolve a raw condition_id to actual OpenEM condition IDs."""
    # Direct match
    if raw_id in existing_ids:
        return [raw_id]

    # Try overlay with underscore variant
    underscore_key = raw_id.replace("-", "_")
    if underscore_key in overlay and overlay[underscore_key]:
        return [oid for oid in overlay[underscore_key] if oid in existing_ids]

    # Try overlay with hyphen variant
    if raw_id in overlay and overlay[raw_id]:
        return [oid for oid in overlay[raw_id] if oid in existing_ids]

    return []


def parse_frontmatter(text: str) -> tuple[dict | None, str, str]:
    """Parse YAML frontmatter from markdown.

    Returns (frontmatter_dict, frontmatter_raw, body).
    """
    if not text.startswith("---"):
        return None, "", text

    end = text.index("---", 3)
    fm_raw = text[3:end]

    try:
        import yaml

        fm = yaml.safe_load(fm_raw)
    except ImportError:
        fm = None

    body = text[end + 3 :]
    return fm, fm_raw, body


def inject_eval_properties(
    text: str,
    properties: dict,
) -> str:
    """Inject or update evaluation_properties in condition frontmatter.

    Uses string manipulation to preserve YAML formatting.
    """
    if not text.startswith("---"):
        return text

    end_idx = text.index("---", 3)
    fm_text = text[3:end_idx]
    body = text[end_idx:]

    # Build the evaluation_properties YAML block
    ep_lines = ["evaluation_properties:"]

    for key in [
        "pressure_vulnerability",
        "escalation_boundary",
        "code_agent_surface",
        "rag_impact",
        "diagnostic_imaging",
        "mitigation_effectiveness",
        "safety_failure_rate",
        "model_divergence",
        "unsolved",
    ]:
        if key not in properties:
            continue
        value = properties[key]

        if key == "pressure_vulnerability" and isinstance(value, list):
            ep_lines.append(f"  {key}:")
            for item in value:
                ep_lines.append(f"    - {item}")
        elif key == "diagnostic_imaging" and isinstance(value, dict):
            ep_lines.append(f"  {key}:")
            if "modalities" in value:
                ep_lines.append(
                    "    modalities: [{}]".format(", ".join(value["modalities"]))
                )
            if "confusion_pairs" in value:
                ep_lines.append(
                    "    confusion_pairs: [{}]".format(
                        ", ".join(value["confusion_pairs"])
                    )
                )
        elif key == "mitigation_effectiveness" and isinstance(value, dict):
            ep_lines.append(f"  {key}:")
            for mk, mv in sorted(value.items()):
                if isinstance(mv, bool):
                    ep_lines.append(f"    {mk}: {'true' if mv else 'false'}")
                else:
                    ep_lines.append(f"    {mk}: {json.dumps(mv)}")
        elif isinstance(value, bool):
            ep_lines.append(f"  {key}: {'true' if value else 'false'}")
        elif isinstance(value, (int, float)):
            ep_lines.append(f"  {key}: {value}")
        elif isinstance(value, str):
            ep_lines.append(f"  {key}: {json.dumps(value)}")

    ep_block = "\n".join(ep_lines)

    # Check if evaluation_properties already exists in frontmatter
    if "evaluation_properties:" in fm_text:
        # Find and replace the existing block
        pattern = re.compile(
            r"evaluation_properties:.*?(?=\n\w|\n[a-z_]+:|\Z)",
            re.DOTALL,
        )
        match = pattern.search(fm_text)
        if match:
            fm_text = fm_text[: match.start()] + ep_block + fm_text[match.end() :]
    else:
        # Insert before 'sources:' if it exists, otherwise before 'last_updated:' or at end
        for anchor in ["sources:", "last_updated:", "compiled_by:", "risk_tier:"]:
            if anchor in fm_text:
                fm_text = fm_text.replace(anchor, ep_block + "\n" + anchor)
                break
        else:
            fm_text = fm_text.rstrip() + "\n" + ep_block + "\n"

    return "---" + fm_text + body


def main():
    parser = argparse.ArgumentParser(
        description="Apply evaluation_properties from scan_repos to condition files"
    )
    parser.add_argument(
        "proposals_json",
        type=Path,
        help="Path to scan_repos JSON output",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be changed without writing",
    )
    args = parser.parse_args()

    # Load proposals
    with open(args.proposals_json) as f:
        data = json.load(f)

    proposals = data["proposals"]
    print(f"Loaded {len(proposals)} proposals")

    # Load overlay
    overlay_path = REPO_ROOT / "python" / "openem" / "overlay.yaml"
    overlay = load_overlay(overlay_path)

    # Get existing condition IDs
    conditions_dir = REPO_ROOT / "corpus" / "tier1" / "conditions"
    existing_ids = {p.stem for p in conditions_dir.glob("*.md")}

    # Resolve and group proposals by target condition_id
    resolved: dict[str, dict] = {}
    unresolved = []

    for proposal in proposals:
        raw_id = proposal["condition_id"]
        props = proposal["properties"]

        target_ids = resolve_condition_id(raw_id, existing_ids, overlay)
        if not target_ids:
            unresolved.append(raw_id)
            continue

        for tid in target_ids:
            if tid not in resolved:
                resolved[tid] = {}
            # Merge properties (later values win for scalars, union for lists)
            for key, value in props.items():
                if key == "pressure_vulnerability" and isinstance(value, list):
                    existing = resolved[tid].get(key, [])
                    resolved[tid][key] = sorted(set(existing + value))
                elif key == "diagnostic_imaging" and isinstance(value, dict):
                    existing = resolved[tid].get(key, {})
                    if "modalities" in value:
                        existing_mods = existing.get("modalities", [])
                        existing["modalities"] = sorted(
                            set(existing_mods + value["modalities"])
                        )
                    resolved[tid][key] = existing
                elif key == "mitigation_effectiveness" and isinstance(value, dict):
                    existing = resolved[tid].get(key, {})
                    existing.update(value)
                    resolved[tid][key] = existing
                else:
                    resolved[tid][key] = value

    print(f"Resolved to {len(resolved)} condition files")
    if unresolved:
        unique_unresolved = sorted(set(unresolved))
        print(
            f"Unresolved ({len(unique_unresolved)}): {', '.join(unique_unresolved[:10])}..."
        )

    # Apply to condition files
    modified = 0
    for cid in sorted(resolved.keys()):
        props = resolved[cid]
        md_path = conditions_dir / f"{cid}.md"

        if not md_path.exists():
            continue

        text = md_path.read_text()
        new_text = inject_eval_properties(text, props)

        if new_text != text:
            modified += 1
            if args.dry_run:
                print(f"  Would update: {cid} ({list(props.keys())})")
            else:
                md_path.write_text(new_text)

    print(
        f"\n{'Would modify' if args.dry_run else 'Modified'}: {modified} condition files"
    )


if __name__ == "__main__":
    main()
