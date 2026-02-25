# Architecture

OpenEM Corpus is structured as a machine-readable emergency medicine knowledge base with a hybrid retrieval layer and downstream integration via a bridge pattern.

## Corpus Structure

```
corpus/
  tier1/conditions/    # 157 conditions, Apache 2.0 (copyright-free sources only)
  tier2/conditions/    # CC-BY-SA 4.0 (WikEM-derived, attribution required)
```

Each condition is a single Markdown file with YAML frontmatter. Filename matches the `id` field in kebab-case (e.g., `septic-arthritis.md`).

### Condition Format

```yaml
---
id: septic-arthritis
condition: Septic Arthritis
icd10: ["M00.9"]
esi: 2
risk_tier: B
time_to_harm: "< 24 hours"
category: musculoskeletal
sources:
  - type: guideline
    ref: "..."
    pmid: "12345678"
validation:
  schema_version: "2.0"
---
## Recognition
## Critical Actions
## Differential Diagnosis
## Workup
## Treatment
## Disposition
## Pitfalls
```

Schema definition: `schemas/condition.schema.yaml` (JSON Schema v7 in YAML form).

### Schema v2.0 Extensions

| Field | Type | Context |
|-------|------|---------|
| `disposition_default` | string | ESI 4-5 conditions: expected discharge disposition |
| `escalation_triggers` | string[] | ESI 4-5 conditions: red flags requiring escalation |
| `confusion_pairs` | array of objects | Conditions commonly confused with this one |
| `time_to_harm` | string or object | Simple (`"< 6 hours"`) or structured (`{typical, worst_case, modifiers}`) |

## LanceDB Hybrid Search Index

Pre-built index at `data/index/openem.lance/`. Rebuilt via `make build-index`.

- **Embedding model:** PubMedBERT (768 dimensions)
- **Index size:** 157 conditions, 1,721 chunks
- **Search modes:**
  - `hybrid` (default): RRF fusion of dense vector + BM25 full-text search
  - `vector`: Dense semantic search only
  - `fts`: BM25 full-text search only (via Tantivy)

RRF scoring: over-fetches `top_k * 4` from each modality, then merges with `score += 1.0 / (60 + rank + 1)`.

### Chunking Strategy

1. Parse YAML frontmatter + Markdown body from each condition file
2. Split at H2 headers (`## Section`) as primary chunk boundaries
3. Subsection split at H3 headers (`### Subsection`) when section text exceeds 800 characters
4. Enrich each chunk with metadata: condition name, aliases, ICD-10 codes, category, risk tier, ESI

Result: 157 conditions produce 1,721 chunks (~11 per condition on average).

## Python Package

```
python/openem/
  __init__.py      # Exports: OpenEMIndex, OpenEMBridge
  index.py         # LanceDB index wrapper (hybrid search)
  bridge.py        # Downstream integration bridge
```

Install: `pip install -e .` (core) or `pip install -e ".[embeddings]"` (+ sentence-transformers).

### OpenEMIndex

Wraps the LanceDB table with search methods supporting filtering by category, risk tier, or condition ID.

### OpenEMBridge

Thin integration layer for downstream projects. Handles:

- **Condition mapping:** Downstream projects define `condition_map` dicts mapping their naming convention to OpenEM IDs
- **Fallback resolution:** Converts separators (`_` to `-`) and lowercases for fuzzy matching
- **Section priority ordering:** Critical Actions > Treatment > Recognition > Disposition > Pitfalls
- **Deduplication:** Removes duplicate chunks by ID before building context
- **Character budget:** Truncates at `max_chars`, preserving section boundaries
- **Escalation triggers:** `get_context_with_differentials()` appends confusion-pair data for low-acuity defer conditions

## Downstream Integration

Two projects consume OpenEM via the bridge:

| Project | Wrapper Location | Naming Convention |
|---------|-----------------|-------------------|
| ScribeGoat2 | `evaluation/bloom_eval_v2/openem_bridge.py` | Mixed-case (`"Septic Arthritis"`) |
| LostBench | `src/lostbench/openem.py` | Snake-case (`"septic_arthritis"`) |

Both projects install OpenEM as an editable package and define their own `condition_map`.

## Validation Pipeline

```
validate.py (schema) --> audit.py (13-pass) --> quality_gate.py (coverage) --> tests/
```

| Script | Purpose |
|--------|---------|
| `scripts/validate.py` | Schema compliance (must pass for build) |
| `scripts/audit.py` | 13-pass quality suite: cross-file dosing, citations, ICD-10, terminology, pediatric doses, cross-references |
| `scripts/quality_gate.py` | Category and ESI coverage, time-to-harm consistency |
| `scripts/diversity_metrics.py` | Source composition and category balance |
| `scripts/eval_retrieval.py` | Retrieval evaluation against ground truth (43 queries) |

CI enforces validation, tests, audit, and quality-gate on every push via 4 GitHub Actions workflows.
