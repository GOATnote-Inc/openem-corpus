# OpenEM Corpus — Agent Instructions

## Project Purpose
AI-native emergency medicine training corpus. Agent-compiled, machine-validated, grep-friendly.
Designed for model training, evaluation, and research (e.g., NemotronNano 30B fine-tuning).
NOT a clinical decision support tool. NOT deployed for patient care.

## Core Rules
1. **Truth-seeking above all.** Never soften clinical facts for readability. If evidence is uncertain, say so explicitly.
2. **Every claim needs a source.** No unsourced medical assertions. Use `sources:` frontmatter and inline citations.
3. **Tier 1 is copyright-free only.** Apache 2.0 track. Only PubMed OA (CC-BY/CC0), WHO, CDC, clinical guidelines, or original agent-authored synthesis. NO StatPearls (CC BY-NC-ND), NO copyrighted textbooks.
4. **Tier 2 is CC-BY-SA.** WikEM-derived content must attribute WikEM/OpenEM Foundation. Share-alike applies.
5. **One file per condition.** `corpus/tier1/conditions/{id}.md` or `corpus/tier2/conditions/{id}.md`.
6. **YAML frontmatter is mandatory.** Must validate against `schemas/condition.schema.yaml` (v2.0).
7. **Append to run_log.jsonl** after any batch compilation or audit. Same pattern as scribegoat2.
8. **ICD-10-CM codes only** (US public domain). Do NOT ship SNOMED CT codes in the repo (redistribution restricted).

## Validation Model
- `validation:` frontmatter block tracks machine-validation passes (dates, flags).
- `risk_tier:` classifies conditions as A (high-risk), B (moderate), C (general) — informational only.
- `reviewed_by:` and `review_date:` track physician review (optional, present on all 80 risk_tier A conditions).
- `scripts/validate.py` — schema validation (must pass for build). Reads enums from `schemas/condition.schema.yaml` (single source of truth). Also validates `overlay.yaml` targets.
- `scripts/audit.py` — 13-pass automated validation suite. Three checks are **blocking** (cross_file_dosing, dose_range_anomaly, content_completeness). Remaining checks informational. Pass 5 (duplicate detection) uses MinHash LSH.
- `scripts/quality_gate.py` — pre-merge gate (sources, ICD-10, dosing, content completeness, PMIDs).
- `scripts/review_status.py` — prints physician review status by risk tier.
- `scripts/check_index_freshness.py` — CI gate: exits 1 if corpus has changed since last `make build-index`. Checks file count + SHA-256 fingerprint.

## Versioning (v0.2.0)
- `__version__ = "0.2.0"` in `python/openem/__init__.py`
- Manifest fields: `index_format_version`, `api_version`, `corpus_version`, `corpus_fingerprint`, `corpus_file_count`, `file_hashes`. `version` key kept as backward-compat shim.
- Downstream consumers can check `from openem import __version__` for API compatibility.
- All 3 downstream repos pin `openem>=0.2.0` as optional dependency.

## time_to_harm Convention
- **risk_tier A:** SHOULD use structured object form (`irreversible_injury`, `death`, `optimal_intervention_window`). String form accepted but new/updated tier A should use object.
- **risk_tier B/C:** string form is standard (e.g., "< 6 hours").

## File Format
- Markdown with YAML frontmatter (see README.md for example)
- Sections: Recognition, Critical Actions, Differential Diagnosis, Workup, Treatment, Disposition, Pitfalls
- Token-efficient: no filler, no hedging, no "it is important to note that"

## Agent Team Workflows
- `/compile-condition [name]` — Spawn team to compile one condition
- `/review-evidence [file]` — Spawn team to review citations
- `/audit-corpus` — Spawn team to run full audit suite

## Quality Bar
- Every condition must have: id, condition name, at least one ICD-10 code, ESI level, time-to-harm, risk_tier, validation block, at least one source
- `compiled_by: agent` — all content is agent-compiled
- Pitfalls section is mandatory — this is where clinical value lives
- All drug doses must include route, frequency, and weight-basis where applicable
- Cross-file dosing must be internally consistent

## Schema v2.0 Extensions

The following fields were added in schema v2.0 (2026-02):

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `disposition_default` | string | For ESI 4-5 | Default disposition (e.g., "discharge with follow-up") |
| `escalation_triggers` | string[] | For ESI 4-5 | Red flags requiring escalation despite low ESI |
| `confusion_pairs` | string[] | Optional | Conditions commonly confused with this one |
| `time_to_harm` | string or object | Yes | `oneOf`: simple string ("< 6 hours") or structured object with `typical`, `worst_case`, `modifiers` |

### Defer Conditions (ESI 4-5)

Six conditions at ESI 4-5 (benign-positional-vertigo, pediatric-acute-otitis-media, knee-osteoarthritis, tension-headache, panic-attack, benign-palpitations) require additional sections:

- **"When NOT to Escalate"** body section — explicitly describes low-risk presentations
- `confusion_pairs` — conditions with similar presentation but higher acuity (e.g., tension-headache → subarachnoid-hemorrhage)
- `escalation_triggers` — specific findings that override the low-ESI default (e.g., "thunderclap onset" for tension-headache)
- `disposition_default` — expected discharge disposition

### Gap Conditions

Four conditions added to fill critical coverage gaps: foreign-body-aspiration, snakebite-envenomation, uterine-rupture, pprom.

### v2.1 Expansion (2026-02-26)

28 new conditions added across three new categories:
- **disaster-mci** (6 conditions): mass-casualty-triage, active-shooter-response, blast-injury, chemical-mass-casualty, radiation-mass-casualty, crush-syndrome-mci
- **procedural** (7 conditions): resuscitative-thoracotomy, perimortem-cesarean-delivery, lateral-canthotomy, difficult-airway-management, breech-precipitous-delivery, surgical-cricothyrotomy, reboa
- **HALO high-acuity** (15 conditions): aortic-transection, fat-embolism-syndrome, air-embolism, spontaneous-coronary-artery-dissection, hemorrhagic-stroke, necrotizing-enterocolitis, inborn-errors-metabolic-crisis, pheochromocytoma-crisis, toxic-shock-syndrome, cavernous-sinus-thrombosis, massive-hemoptysis, retrobulbar-hemorrhage, tracheal-disruption, esophageal-foreign-body-impaction, malignant-otitis-externa

Total corpus: 185 conditions across 20 categories. New source type `consensus-statement` added to schema.

### Safety Annotations

- **Operational Substitution Risks** on 6 high-traffic conditions (e.g., SAH: structured home monitoring alongside emergency language)
- **Structured time_to_harm** (object form) on 10 risk_tier A conditions
- **Adversarial presentations** on 10 conditions (atypical presentations that evade pattern matching)

## Terminology

| Term | Definition |
|------|-----------|
| ESI 1-5 | Emergency Severity Index: 1=resuscitation, 2=emergent, 3=urgent, 4=less urgent, 5=non-urgent |
| risk_tier A/B/C | A=high-risk (time-critical, high mortality), B=moderate, C=general |
| time_to_harm | Window before irreversible harm; string ("< 6h") or structured object |
| confusion_pairs | Conditions with similar presentation but different acuity (e.g., tension-headache ↔ SAH) |
| escalation_triggers | Findings that override a low-ESI default and require emergency evaluation |
| disposition_default | Expected disposition for low-acuity conditions (e.g., "discharge with follow-up") |
| tier1 / tier2 | Licensing tracks: tier1=Apache 2.0 (copyright-free), tier2=CC-BY-SA (WikEM-derived) |
| compiled_by | Agent or human authorship marker |
| validation block | YAML frontmatter recording automated quality checks |
| schema_version | Currently "2.0" — tracked in validation block |

## Developer Setup

```bash
pip install -e .                              # Core package (LanceDB index access)
pip install -e ".[embeddings]"                # + sentence-transformers for embeddings
make build-index                              # Rebuild LanceDB index (after adding conditions)
make build-index -- --incremental             # Incremental rebuild (only re-embeds changed files)
make check                                    # Run validation + quality gate + tests
make check-freshness                          # Verify index matches corpus
python scripts/validate.py                    # Schema validation + overlay validation
python scripts/audit.py                       # Full 13-pass audit suite
python scripts/check_index_freshness.py       # Index staleness check (exit 1 = stale)
python scripts/ingest_eval_findings.py --dry-run RESULT.json  # Preview CEIS→issue pipeline
```

### Key File Paths

| Purpose | Path |
|---------|------|
| Package init + version | `python/openem/__init__.py` |
| Index access (LanceDB) | `python/openem/index.py` |
| Bridge (shared retrieval) | `python/openem/bridge.py` |
| Condition map + overlay validation | `python/openem/conditions.py` |
| Overlay (multi-condition mappings) | `python/openem/overlay.yaml` |
| Schema validation | `scripts/validate.py` |
| Audit suite (13 passes) | `scripts/audit.py` |
| Quality gate | `scripts/quality_gate.py` |
| Index freshness check | `scripts/check_index_freshness.py` |
| Index builder | `scripts/build_index.py` |
| Eval findings ingest | `scripts/ingest_eval_findings.py` |
| Condition schema (single source of truth) | `schemas/condition.schema.yaml` |
| Diversity metrics | `scripts/diversity_metrics.py` |
| Impact analysis | `scripts/analyze_impact.py` |
| Retrieval evaluation | `scripts/eval_retrieval.py` |
| Retrieval ground truth | `evaluation/retrieval_ground_truth.jsonl` |
| Corpus conditions | `corpus/tier1/conditions/*.md` |
| Pre-built index | `data/index/openem.lance/` |
| Condition map cache (gitignored) | `python/openem/condition_map.json` |
| Embedding cache (gitignored) | `data/index/embedding_cache.json` |

### Incremental Index Rebuild

`python scripts/build_index.py --incremental` tracks per-file SHA-256 hashes in the manifest and caches embeddings in `data/index/embedding_cache.json`. On subsequent builds, only changed/new files are re-embedded. At 500+ conditions this cuts rebuild from minutes to seconds for single-file edits. Full rebuild is always available without `--incremental`.

### Stale Index Detection

After adding or modifying condition files, the index may be stale. Detection works at two levels:
1. **File count:** manifest `corpus_file_count` vs actual `.md` file count
2. **Fingerprint:** SHA-256 of sorted filenames + sizes (catches edits to existing files)

`check_freshness()` on `OpenEMIndex` and `scripts/check_index_freshness.py` both use this. Wired into CI (`validate.yml`) and `make post-compile`.

### Overlay Validation

`python/openem/overlay.yaml` maps condition names to multiple corpus IDs. `validate_overlay()` checks every target ID has a matching `.md` file. Called automatically by `validate.py` and `build_index.py`. Catches typos that would cause silent retrieval failures.

### Eval Findings Ingest

`scripts/ingest_eval_findings.py` reads LostBench CEIS result JSON files, extracts conditions with Class A failures (critical escalation drops), and creates GitHub issues via `gh issue create` for physician review. Supports `--dry-run`, `--min-failures`, and `--label`.

Cross-repo architecture: see `scribegoat2/docs/CROSS_REPO_ARCHITECTURE.md`
