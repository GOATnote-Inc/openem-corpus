# OpenEM Corpus

[![Tests](https://github.com/GOATnote-Inc/openem-corpus/actions/workflows/tests.yml/badge.svg)](https://github.com/GOATnote-Inc/openem-corpus/actions/workflows/tests.yml)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE-APACHE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

**370 emergency medicine conditions. 80 physician-reviewed. 631 source citations.**
Agent-compiled from clinical guidelines and PubMed literature. Machine-validated with a 13-pass automated quality suite.

## Quick Start

```python
from openem import OpenEMIndex, OpenEMBridge

index = OpenEMIndex("data/index/openem.lance")
bridge = OpenEMBridge(index)  # auto-loads canonical condition map
context = bridge.get_context("chest pain", max_chars=2000)
print(context)
```

Install: `pip install -e .` from the repo root.

### CLI

Every condition is a plain Markdown file — searchable with standard tools:

```bash
rg "chest pain" corpus/                              # Full-text search
rg "^esi: 1" corpus/ --glob "*.md"                   # Find all ESI-1 conditions
rg "^category: cardiovascular" corpus/ --glob "*.md" -l  # List cardiovascular conditions
```

## What This Is

A structured, token-efficient corpus of 370 emergency medicine conditions designed for AI/LLM evaluation and safety research. Every condition is a plain Markdown file with YAML frontmatter — searchable with `grep`, `ripgrep`, `glob`, or any standard CLI tool.

The corpus is used to evaluate whether LLMs maintain safety boundaries in emergency medicine conversations. Downstream consumers: [ScribeGOAT2](https://github.com/GOATnote-Inc/scribegoat2), [LostBench](https://github.com/GOATnote-Inc/lostbench), [SafeShift](https://github.com/GOATnote-Inc/safeshift), [RadSlice](https://github.com/GOATnote-Inc/radslice).

Downstream evaluations show measurable safety impact: RAG context from OpenEM lifts model safety pass^k from 0.217 to 0.391 (+80%) and reduces urgency-minimization failures by 65% ([LostBench CEIS](https://github.com/GOATnote-Inc/lostbench), N=78 scenarios). [RadSlice](https://github.com/GOATnote-Inc/radslice) maps 133 OpenEM conditions to multimodal imaging tasks. [SafeShift](https://github.com/GOATnote-Inc/safeshift) uses optional OpenEM context enrichment for inference optimization safety testing.

## Important Disclaimers

**This corpus is NOT a substitute for clinical judgment.** It is a research artifact for AI safety evaluation.

- All conditions are `compiled_by: agent` (AI-compiled from clinical guidelines and PubMed literature)
- 80 risk_tier A (highest-acuity) conditions have been physician-reviewed; 283 conditions have not
- Content reflects clinical guidelines and PubMed literature as of February 2026
- Drug doses and protocols should be cross-referenced with institutional formularies
- This corpus is not FDA-approved or endorsed by any medical board or specialty society

## Corpus at a Glance

| Metric | Value |
|--------|-------|
| Conditions | 370 |
| Words | ~235,000 |
| Source citations | 631 (450 unique PMIDs) |
| Categories | 21 |
| ESI 1 (resuscitation) | 80 |
| ESI 2 (emergent) | 60 |
| ESI 3 (urgent) | 19 |
| ESI 4-5 (less urgent) | 6 |
| Physician-reviewed (risk tier A) | 80 |
| License | Apache 2.0 (tier1) |
| Validation | All conditions pass automated 13-check suite (schema v2.0) |

## Quality Assurance

| Layer | What | Details |
|-------|------|---------|
| Schema validation | Every condition validates against [`condition.schema.yaml`](schemas/condition.schema.yaml) (v2.0) | 22 required fields, ICD-10 format, source citations |
| 13-pass audit | [`scripts/audit.py`](scripts/audit.py) — 3 blocking, 10 informational | Cross-file dosing consistency, dose range anomalies, content completeness |
| Physician review | 80 risk_tier A conditions reviewed by board-certified EM physician | Structured [category-specific rubrics](review/rubric/), blind review protocol |
| CI pipeline | 5 workflows: validate, audit, quality-gate, review-gate, tests | All block merge to main |

Physician review workflow: [`REVIEWING.md`](REVIEWING.md). Full validation pipeline: [`docs/CORPUS_DETAILS.md`](docs/CORPUS_DETAILS.md).

## File Format

Every condition is a Markdown file with YAML frontmatter:

```yaml
---
id: stemi
condition: ST-Elevation Myocardial Infarction
aliases: [STEMI, ST-elevation MI, acute MI with ST elevation]
icd10: [I21.01, I21.02, I21.09, I21.11, I21.19, I21.21, I21.29, I21.3]
esi: 1
time_to_harm:
  irreversible_injury: "< 6 hours"
  death: "< 12 hours"
  optimal_intervention_window: "< 90 minutes"
mortality_if_delayed: "7.5% per 30-minute delay to reperfusion"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "2013 ACCF/AHA Guideline for the Management of ST-Elevation Myocardial Infarction"
last_updated: "2026-02-18"
compiled_by: agent
reviewed_by: "Brandon Dent, MD — Board Certified Emergency Medicine"
review_date: "2026-02-27"
risk_tier: A
validation:
  schema_version: "2.0"
  automated_consistency_check: "2026-02-18"
  dose_range_validator: "2026-02-19"
---

# ST-Elevation Myocardial Infarction (STEMI)

## Recognition
...
## Critical Actions
...
## Treatment
...
## Pitfalls
...
```

Every condition file contains 7 required sections: Recognition, Critical Actions, Differential Diagnosis, Workup, Treatment, Disposition, Pitfalls.

### Safety-Specific Fields

38 conditions include `confusion_pairs` linking to conditions with similar presentation but different acuity (e.g., tension-headache → subarachnoid-hemorrhage). 13 conditions include `escalation_triggers` — red flags that override a low-ESI default. 10 risk_tier A conditions carry structured `time_to_harm` with `irreversible_injury`, `death`, and `optimal_intervention_window` fields. Full schema: [`schemas/condition.schema.yaml`](schemas/condition.schema.yaml).

## Python API

```bash
pip install -e .                              # Core package
pip install -e ".[embeddings]"                # + sentence-transformers for embeddings
```

```python
from openem import OpenEMIndex, OpenEMBridge

# Hybrid search (vector + FTS + RRF fusion)
index = OpenEMIndex("data/index/openem.lance")
results = index.search("chest pain tearing", top_k=5, mode="hybrid")

# Bridge with auto-loaded canonical condition map
bridge = OpenEMBridge(index)
context = bridge.get_context("stemi", max_chars=3000)
system_prefix = bridge.format_system_context("stemi")

# With differentials (for defer conditions)
context = bridge.get_context_with_differentials("tension_headache")
```

Downstream projects can override the canonical map:

```python
bridge = OpenEMBridge(index, condition_map={"my_condition": ["stemi", "sepsis"]})
```

## FHIR Export

Eight conditions have synthetic FHIR R4 presentation profiles ([`fhir/presentations/`](fhir/presentations/)) that generate deterministic patient bundles for evaluating EHR-facing AI — prior authorization, CDS Hooks, triage routing.

```bash
pip install -e ".[fhir]"           # Optional: fhir.resources validation
make generate-fhir                  # Generate bundles from presentation profiles
```

POC conditions: anaphylaxis, bacterial-meningitis, diabetic-ketoacidosis, neonatal-emergencies, stemi, subarachnoid-hemorrhage, testicular-torsion, acute-limb-ischemia.

## Licensing

`corpus/tier1/` is **Apache 2.0** — no licensing friction. Only uses PubMed OA (CC-BY/CC0), WHO, CDC, clinical guidelines, and original agent synthesis. See [LICENSE-APACHE](LICENSE-APACHE).

`corpus/tier2/` is **CC-BY-SA 4.0** for WikEM-derived content. See [LICENSE-CC-BY-SA](LICENSE-CC-BY-SA).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and submission guidelines.

**Physician reviewers:** See [REVIEWING.md](REVIEWING.md) for the review workflow. Run `python scripts/review_status.py` to find conditions that need review.

## Citation

If you use this corpus, please cite:

```bibtex
@dataset{openem_corpus_2026,
  title  = {OpenEM Corpus: An AI-Native Emergency Medicine Knowledge Base},
  author = {Dent, Brandon},
  year   = {2026},
  url    = {https://github.com/GOATnote-Inc/openem-corpus}
}
```

Or see [CITATION.cff](CITATION.cff) for machine-readable citation metadata.

## Part of the GOATnote Evaluation Program

| Repository | Purpose |
|------------|---------|
| [LostBench](https://github.com/GOATnote-Inc/lostbench) | Safety persistence benchmark |
| [ScribeGoat2](https://github.com/GOATnote-Inc/scribegoat2) | Research framework and whitepaper |
| [OpenEM Corpus](https://github.com/GOATnote-Inc/openem-corpus) | Emergency medicine knowledge base |
| [SafeShift](https://github.com/GOATnote-Inc/safeshift) | Inference optimization safety |
| [RadSlice](https://github.com/GOATnote-Inc/radslice) | Multimodal radiology benchmark |

Architecture overview: [CROSS_REPO_ARCHITECTURE.md](https://github.com/GOATnote-Inc/scribegoat2/blob/main/docs/CROSS_REPO_ARCHITECTURE.md)

## Further Reading

- [Architecture](docs/ARCHITECTURE.md) — retrieval layer design, bridge pattern, index chunking
- [Corpus Details](docs/CORPUS_DETAILS.md) — categories, expansion history, source composition, validation
- [Condition Schema](schemas/condition.schema.yaml) — YAML frontmatter specification (v2.0)
- [Changelog](CHANGELOG.md) — version history
- [Reviewing Guide](REVIEWING.md) — physician review workflow and rubrics
