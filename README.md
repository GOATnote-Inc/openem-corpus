# OpenEM Corpus

[![Tests](https://github.com/GOATnote-Inc/openem-corpus/actions/workflows/tests.yml/badge.svg)](https://github.com/GOATnote-Inc/openem-corpus/actions/workflows/tests.yml)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE-APACHE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

**The AI-native emergency medicine knowledge base.**
Agent-compiled. Machine-validated. Structured for LLM consumption.

## Quick Start

```bash
# Search for all conditions mentioning chest pain
rg "chest pain" corpus/

# Find all ESI-1 conditions
rg "^esi: 1" corpus/ --glob "*.md"

# List all cardiovascular conditions
rg "^category: cardiovascular" corpus/ --glob "*.md" -l

# Find drug doses for a specific medication
rg "epinephrine" corpus/ --glob "*.md"
```

```python
from openem import OpenEMIndex, OpenEMBridge

index = OpenEMIndex("data/index/openem.lance")
bridge = OpenEMBridge(index)  # auto-loads canonical condition map
context = bridge.get_context("chest pain", max_chars=2000)
print(context)
```

Install: `pip install -e .` from the repo root.

## What This Is

A structured, token-efficient corpus of 185 emergency medicine conditions designed for AI/LLM evaluation and safety research. Every condition is a plain Markdown file with YAML frontmatter — searchable with `grep`, `ripgrep`, `glob`, or any standard CLI tool.

The corpus used to evaluate whether LLMs maintain safety boundaries in emergency medicine conversations. Downstream consumers: [ScribeGOAT2](https://github.com/GOATnote-Inc/scribegoat2), [LostBench](https://github.com/GOATnote-Inc/lostbench), [SafeShift](https://github.com/GOATnote-Inc/safeshift).

## Important Disclaimers

**This corpus is NOT a substitute for clinical judgment.** It is a research artifact for AI safety evaluation.

- All 185 conditions are `compiled_by: agent` (AI-compiled from clinical guidelines and PubMed literature)
- 80 risk_tier A (highest-acuity) conditions have been physician-reviewed; 105 conditions have not
- Content reflects clinical guidelines and PubMed literature as of February 2026
- Drug doses and protocols should be cross-referenced with institutional formularies
- This corpus is not FDA-approved or endorsed by any medical board or specialty society

## Corpus at a Glance

| Metric | Value |
|--------|-------|
| Conditions | 185 |
| Words | ~235,000 |
| Source citations | 631 (450 unique PMIDs) |
| Categories | 20 |
| ESI 1 (resuscitation) | 80 |
| ESI 2 (emergent) | 60 |
| ESI 3 (urgent) | 19 |
| ESI 4-5 (less urgent) | 6 |
| Physician-reviewed (risk tier A) | 80 |
| License | Apache 2.0 (tier1) |
| Validation | All 185 pass automated 13-check suite (schema v2.0) |

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

---

For detailed documentation on categories, source composition, validation pipeline, agent architecture, and schema extensions, see [`docs/`](docs/).
