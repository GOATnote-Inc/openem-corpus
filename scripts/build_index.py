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


def build_chunks(frontmatter: dict, sections: dict, condition_id: str) -> list[dict]:
    """Build section-level chunks with metadata from a single condition."""
    chunks = []
    condition_name = frontmatter.get("condition", condition_id)
    aliases = frontmatter.get("aliases", [])
    icd10 = frontmatter.get("icd10", [])

    for section_name, section_text in sections.items():
        if not section_text.strip():
            continue

        # Prepend condition name, aliases, ICD-10 codes, and section header
        # for both dense and sparse retrieval
        header_parts = [condition_name]
        if aliases:
            header_parts.append(f"({', '.join(aliases)})")
        if icd10:
            header_parts.append(f"[{', '.join(icd10)}]")
        header = " ".join(header_parts)
        chunk_text = f"{header} — {section_name}\n\n{section_text}"

        chunk = {
            "id": f"{condition_id}/{section_to_key(section_name)}",
            "condition_id": condition_id,
            "condition": condition_name,
            "section": section_name,
            "text": chunk_text,
            "category": frontmatter.get("category", ""),
            "risk_tier": frontmatter.get("risk_tier", ""),
            "esi": int(frontmatter.get("esi", 0)),
            "aliases": ", ".join(aliases) if aliases else "",
            "icd10": ", ".join(icd10) if icd10 else "",
        }
        chunks.append(chunk)

    return chunks


def main():
    parser = argparse.ArgumentParser(description="Build OpenEM hybrid search index")
    parser.add_argument(
        "--model", default=DEFAULT_MODEL, help=f"Embedding model (default: {DEFAULT_MODEL})"
    )
    parser.add_argument(
        "--output", type=Path, default=DEFAULT_INDEX_DIR, help="Output directory for index"
    )
    args = parser.parse_args()

    # Collect all condition files
    md_files = sorted(CONDITIONS_DIR.glob("*.md"))
    if not md_files:
        print(f"ERROR: No .md files found in {CONDITIONS_DIR}", file=sys.stderr)
        sys.exit(1)

    print(f"Parsing {len(md_files)} condition files...")
    all_chunks = []
    for path in md_files:
        frontmatter, sections = parse_condition(path)
        if frontmatter and sections:
            cid = frontmatter.get("id", path.stem)
            chunks = build_chunks(frontmatter, sections, cid)
            all_chunks.extend(chunks)

    print(f"  {len(all_chunks)} chunks from {len(md_files)} conditions")

    # Generate dense embeddings
    print(f"Loading embedding model: {args.model}")
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(args.model)

    print(f"Encoding {len(all_chunks)} chunks...")
    t0 = time.time()
    texts = [c["text"] for c in all_chunks]
    embeddings = model.encode(texts, show_progress_bar=True, batch_size=32)
    elapsed = time.time() - t0
    print(f"  Encoded in {elapsed:.1f}s ({len(all_chunks) / elapsed:.0f} chunks/sec)")

    # Attach vectors
    for i, chunk in enumerate(all_chunks):
        chunk["vector"] = embeddings[i].tolist()

    # Create LanceDB index
    args.output.mkdir(parents=True, exist_ok=True)
    db_path = str(args.output / "openem.lance")
    db = lancedb.connect(db_path)

    print(f"Writing LanceDB table to {db_path}...")
    table = db.create_table("conditions", all_chunks, mode="overwrite")

    # Create full-text search index on the text column
    table.create_fts_index("text", replace=True)

    # Write manifest
    manifest = {
        "corpus": "openem",
        "version": "1.0",
        "embedding_model": args.model,
        "embedding_dim": len(all_chunks[0]["vector"]),
        "num_conditions": len(md_files),
        "num_chunks": len(all_chunks),
        "index_path": db_path,
        "built_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    manifest_path = args.output / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")

    print(f"\nIndex built successfully:")
    print(f"  Conditions: {manifest['num_conditions']}")
    print(f"  Chunks:     {manifest['num_chunks']}")
    print(f"  Embedding:  {manifest['embedding_model']} ({manifest['embedding_dim']}d)")
    print(f"  Index:      {db_path}")
    print(f"  Manifest:   {manifest_path}")


if __name__ == "__main__":
    main()
