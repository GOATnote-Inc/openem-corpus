#!/usr/bin/env python3
"""Build hybrid search index from OpenEM corpus.

Creates a LanceDB index with PubMedBERT dense embeddings and tantivy
full-text search. Each H2 section of each condition file becomes one
chunk, with YAML frontmatter fields stored as filterable metadata.

Usage:
    python scripts/build_index.py [--model MODEL] [--output DIR]

Defaults:
    --model  NeuML/pubmedbert-base-embeddings
    --output data/index
"""

import argparse
import hashlib
import json
import re
import sys
import time
from pathlib import Path

import lancedb
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CONDITIONS_DIR = REPO_ROOT / "corpus" / "tier1" / "conditions"
DEFAULT_INDEX_DIR = REPO_ROOT / "data" / "index"
DEFAULT_MODEL = "NeuML/pubmedbert-base-embeddings"


def parse_condition(path: Path) -> tuple[dict | None, dict | None]:
    """Parse a condition file into (frontmatter, {section_name: text})."""
    text = path.read_text()
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, None

    frontmatter = yaml.safe_load(parts[1])
    body = parts[2]

    sections: dict[str, str] = {}
    current_section: str | None = None
    current_lines: list[str] = []

    for line in body.split("\n"):
        if line.startswith("## "):
            if current_section:
                sections[current_section] = "\n".join(current_lines).strip()
            current_section = line[3:].strip()
            current_lines = []
        else:
            current_lines.append(line)

    if current_section:
        sections[current_section] = "\n".join(current_lines).strip()

    return frontmatter, sections


def section_to_key(section_name: str) -> str:
    """Normalize section name to a key: 'Critical Actions' -> 'critical_actions'."""
    return re.sub(r"[^a-z0-9]+", "_", section_name.lower()).strip("_")


def split_subsections(
    section_name: str, section_text: str, threshold: int = 800
) -> dict[str, str]:
    """Split a section at H3 boundaries if it exceeds threshold chars."""
    if len(section_text) <= threshold:
        return {section_name: section_text}

    subsections = {}
    current_sub = None
    current_lines = []
    preamble_lines = []

    for line in section_text.split("\n"):
        if line.startswith("### "):
            if current_sub:
                subsections[f"{section_name} > {current_sub}"] = "\n".join(
                    current_lines
                ).strip()
            elif current_lines:
                preamble_lines = current_lines[:]
            current_sub = line[4:].strip()
            current_lines = []
        else:
            current_lines.append(line)

    if current_sub:
        subsections[f"{section_name} > {current_sub}"] = "\n".join(
            current_lines
        ).strip()

    if not subsections:
        return {section_name: section_text}

    if preamble_lines and len("\n".join(preamble_lines).strip()) > 50:
        subsections[f"{section_name} > Overview"] = "\n".join(preamble_lines).strip()

    return subsections


def build_chunks(frontmatter: dict, sections: dict, condition_id: str) -> list[dict]:
    """Build section-level chunks with metadata from a single condition."""
    chunks = []
    condition_name = frontmatter.get("condition", condition_id)
    aliases = frontmatter.get("aliases", [])
    icd10 = frontmatter.get("icd10", [])
    confusion_pairs = json.dumps(frontmatter.get("confusion_pairs", []))

    for section_name, section_text in sections.items():
        if not section_text.strip():
            continue

        sub_sections = split_subsections(section_name, section_text)
        for sub_name, sub_text in sub_sections.items():
            if not sub_text.strip():
                continue

            # Prepend condition name, aliases, ICD-10 codes, and section header
            # for both dense and sparse retrieval
            header_parts = [condition_name]
            if aliases:
                header_parts.append(f"({', '.join(aliases)})")
            if icd10:
                header_parts.append(f"[{', '.join(icd10)}]")
            header = " ".join(header_parts)
            chunk_text = f"{header} — {sub_name}\n\n{sub_text}"

            chunk = {
                "id": f"{condition_id}/{section_to_key(sub_name)}",
                "condition_id": condition_id,
                "condition": condition_name,
                "section": sub_name,
                "text": chunk_text,
                "category": frontmatter.get("category", ""),
                "risk_tier": frontmatter.get("risk_tier", ""),
                "esi": int(frontmatter.get("esi", 0)),
                "aliases": ", ".join(aliases) if aliases else "",
                "icd10": ", ".join(icd10) if icd10 else "",
                "confusion_pairs": confusion_pairs,
            }
            chunks.append(chunk)

    return chunks


def corpus_fingerprint(conditions_dir: Path) -> str:
    """SHA-256 fingerprint of sorted filenames + sizes. Used for staleness detection."""
    entries = []
    for md_file in sorted(conditions_dir.glob("*.md")):
        entries.append(f"{md_file.name}:{md_file.stat().st_size}")
    return hashlib.sha256("\n".join(entries).encode()).hexdigest()[:16]


def file_content_hash(path: Path) -> str:
    """SHA-256 of file content, truncated to 16 hex chars."""
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def per_file_hashes(conditions_dir: Path) -> dict[str, str]:
    """Compute content hash for every .md file in conditions_dir."""
    return {f.name: file_content_hash(f) for f in sorted(conditions_dir.glob("*.md"))}


def main():
    parser = argparse.ArgumentParser(description="Build OpenEM hybrid search index")
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Embedding model (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_INDEX_DIR,
        help="Output directory for index",
    )
    parser.add_argument(
        "--incremental",
        action="store_true",
        help="Only re-embed changed files (reuse cached embeddings for unchanged)",
    )
    args = parser.parse_args()

    # Validate overlay before building
    try:
        from openem.conditions import validate_overlay, save_condition_map_sidecar

        overlay_errors = validate_overlay(corpus_dir=CONDITIONS_DIR)
        if overlay_errors:
            print("ERROR: Overlay validation failed:", file=sys.stderr)
            for err in overlay_errors:
                print(f"  - {err}", file=sys.stderr)
            sys.exit(1)
        print("Overlay validation passed.")
    except ImportError:
        save_condition_map_sidecar = None

    # Collect all condition files
    md_files = sorted(CONDITIONS_DIR.glob("*.md"))
    if not md_files:
        print(f"ERROR: No .md files found in {CONDITIONS_DIR}", file=sys.stderr)
        sys.exit(1)

    # Compute per-file hashes for incremental rebuild
    current_hashes = per_file_hashes(CONDITIONS_DIR)

    # Load previous manifest for incremental mode
    manifest_path = args.output / "manifest.json"
    prev_manifest = None
    prev_hashes: dict[str, str] = {}
    embedding_cache_path = args.output / "embedding_cache.json"
    embedding_cache: dict[str, list[float]] = {}

    if args.incremental and manifest_path.exists():
        prev_manifest = json.loads(manifest_path.read_text())
        prev_hashes = prev_manifest.get("file_hashes", {})

        # Load cached embeddings if available
        if embedding_cache_path.exists():
            try:
                embedding_cache = json.loads(embedding_cache_path.read_text())
            except (json.JSONDecodeError, KeyError):
                embedding_cache = {}

    print(f"Parsing {len(md_files)} condition files...")
    all_chunks = []
    changed_chunk_indices: list[int] = []  # indices of chunks needing embedding

    for path in md_files:
        frontmatter, sections = parse_condition(path)
        if frontmatter and sections:
            cid = frontmatter.get("id", path.stem)
            chunks = build_chunks(frontmatter, sections, cid)

            file_changed = current_hashes.get(path.name) != prev_hashes.get(path.name)

            for chunk in chunks:
                chunk_idx = len(all_chunks)
                all_chunks.append(chunk)

                if args.incremental and not file_changed and chunk["id"] in embedding_cache:
                    # Reuse cached embedding
                    chunk["vector"] = embedding_cache[chunk["id"]]
                else:
                    changed_chunk_indices.append(chunk_idx)

    print(f"  {len(all_chunks)} chunks from {len(md_files)} conditions")

    if args.incremental and changed_chunk_indices:
        total = len(all_chunks)
        reused = total - len(changed_chunk_indices)
        print(f"  Incremental: {reused} cached, {len(changed_chunk_indices)} to embed")
    elif args.incremental and not changed_chunk_indices:
        print("  Incremental: all chunks cached, no embedding needed")
        changed_chunk_indices = []  # nothing to embed

    # Generate dense embeddings (only for changed chunks, or all if not incremental)
    if not args.incremental:
        changed_chunk_indices = list(range(len(all_chunks)))

    if changed_chunk_indices:
        print(f"Loading embedding model: {args.model}")
        from sentence_transformers import SentenceTransformer

        model = SentenceTransformer(args.model)

        texts_to_embed = [all_chunks[i]["text"] for i in changed_chunk_indices]
        print(f"Encoding {len(texts_to_embed)} chunks...")
        t0 = time.time()
        embeddings = model.encode(texts_to_embed, show_progress_bar=True, batch_size=32)
        elapsed = time.time() - t0
        print(f"  Encoded in {elapsed:.1f}s ({len(texts_to_embed) / elapsed:.0f} chunks/sec)")

        for idx_pos, chunk_idx in enumerate(changed_chunk_indices):
            all_chunks[chunk_idx]["vector"] = embeddings[idx_pos].tolist()

    # Create LanceDB index
    args.output.mkdir(parents=True, exist_ok=True)
    db_path = str(args.output / "openem.lance")
    db = lancedb.connect(db_path)

    print(f"Writing LanceDB table to {db_path}...")
    table = db.create_table("conditions", all_chunks, mode="overwrite")

    # Create full-text search index on the text column
    table.create_fts_index("text", replace=True)

    # Compute corpus fingerprint for staleness detection
    fp = corpus_fingerprint(CONDITIONS_DIR)

    # Save embedding cache for future incremental builds
    new_cache = {chunk["id"]: chunk["vector"] for chunk in all_chunks}
    embedding_cache_path.write_text(json.dumps(new_cache) + "\n")

    # Write manifest (restructured for v0.2.0)
    manifest = {
        "corpus": "openem",
        "version": "1.0",  # compat shim — kept for older consumers
        "index_format_version": "1.0",
        "api_version": "0.2.0",
        "corpus_version": "2.0",
        "corpus_fingerprint": fp,
        "corpus_file_count": len(md_files),
        "file_hashes": current_hashes,
        "embedding_model": args.model,
        "embedding_dim": len(all_chunks[0]["vector"]),
        "num_conditions": len(md_files),
        "num_chunks": len(all_chunks),
        "index_path": db_path,
        "built_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")

    # Generate condition map sidecar cache
    if save_condition_map_sidecar is not None:
        sidecar = save_condition_map_sidecar(corpus_dir=CONDITIONS_DIR)
        print(f"  Condition map sidecar: {sidecar}")

    print(f"\nIndex built successfully:")
    print(f"  Conditions: {manifest['num_conditions']}")
    print(f"  Chunks:     {manifest['num_chunks']}")
    print(f"  Fingerprint: {fp}")
    if args.incremental:
        print(f"  Incremental: {len(all_chunks) - len(changed_chunk_indices)} reused, {len(changed_chunk_indices)} re-embedded")
    print(f"  Embedding:  {manifest['embedding_model']} ({manifest['embedding_dim']}d)")
    print(f"  Index:      {db_path}")
    print(f"  Manifest:   {manifest_path}")


if __name__ == "__main__":
    main()
