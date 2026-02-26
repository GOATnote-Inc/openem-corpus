# OpenEM Corpus

[![Tests](https://github.com/GOATnote-Inc/openem-corpus/actions/workflows/tests.yml/badge.svg)](https://github.com/GOATnote-Inc/openem-corpus/actions/workflows/tests.yml)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE-APACHE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

**The AI-native emergency medicine knowledge base.**
Agent-compiled. Physician-verified. Grep-friendly.

## What This Is

A structured, token-efficient corpus of emergency medicine knowledge designed for AI/LLM consumption. Every condition is a plain Markdown file with YAML frontmatter — searchable with `grep`, `ripgrep`, `glob`, or any standard CLI tool.

Built by [Brandon Dent, MD](https://github.com/GOATnote-Inc) (emergency medicine physician) and AI agent teams. Designed for worldwide healthcare use.

## Corpus at a Glance

| Metric | Value |
|--------|-------|
| Conditions | 185 |
| Words | ~235,000 |
| Source citations | 631 (450 unique PMIDs) |
| Categories | 20 / 20 |
| ESI 1 (resuscitation) | 49 |
| ESI 2 (emergent) | 60 |
| ESI 3 (urgent) | 19 |
| ESI 4-5 (less urgent) | 6 |
| License | Apache 2.0 (tier1) |
| Validation | All 185 pass automated 13-check suite (schema v2.0) |

### Category Coverage

| Category | Count | Category | Count |
|----------|-------|----------|-------|
| cardiovascular | 15 | neurological | 7 |
| toxicologic | 10 | obstetric-gynecologic | 7 |
| infectious | 10 | environmental | 7 |
| pediatric | 9 | traumatic | 7 |
| gastrointestinal | 8 | ophthalmologic | 6 |
| musculoskeletal | 8 | genitourinary | 6 |
| respiratory | 7 | endocrine-metabolic | 6 |
| hematologic | 5 | psychiatric | 4 |
| allergic-immunologic | 3 | dermatologic | 3 |
| disaster-mci | 6 | procedural | 7 |

### Condition Expansion (v2.1)

The corpus has grown from 128 to 185 tier1 conditions:
- **6 defer conditions** (ESI 4-5): benign-positional-vertigo, pediatric-acute-otitis-media, knee-osteoarthritis, tension-headache, panic-attack, benign-palpitations. These include `confusion_pairs`, `escalation_triggers`, and `disposition_default` fields.
- **4 gap conditions**: foreign-body-aspiration, snakebite-envenomation, uterine-rupture, pprom
- **19 expansion conditions**: Additional high-priority conditions across existing categories
- **28 MCI/HALO/procedural conditions** (disaster-mci, procedural categories): mass-casualty-triage, active-shooter-response, resuscitative-thoracotomy, perimortem-cesarean-delivery, lateral-canthotomy, difficult-airway-management, ...

### Source Composition

| Source Type | Count |
|-------------|-------|
| Clinical guidelines (ACC/AHA, ACEP, IDSA, etc.) | 257 |
| PubMed-indexed original research | 219 |
| Review articles | 130 |
| Meta-analyses | 22 |
| CDC publications | 3 |

## Why This Exists

No AI-native emergency medicine knowledge corpus exists. WikEM is the world's largest open EM reference but is HTML/wiki format. MedRAG has chunked textbooks but isn't EM-specific. StatPearls is CC BY-NC-ND (no derivatives). This project fills the gap.

## Important Disclaimers

**This corpus is NOT a substitute for clinical judgment.** It is a reference tool compiled by AI agents and has not yet undergone physician review. All content should be independently verified against primary sources before clinical use.

- All conditions are `compiled_by: agent` — none have been physician-reviewed yet
- Content reflects clinical guidelines and PubMed literature as of February 2026
- Drug doses and protocols should be cross-referenced with institutional formularies
- This corpus is not FDA-approved or endorsed by any medical board or specialty society

## Dual-Track Licensing

| Track | Directory | License | Sources |
|-------|-----------|---------|---------|
| **Tier 1 (Free)** | `corpus/tier1/` | Apache 2.0 | PubMed OA, WHO, CDC, clinical guidelines, original synthesis |
| **Tier 2 (Share-Alike)** | `corpus/tier2/` | CC-BY-SA 4.0 | WikEM-derived content restructured + supplemented |

Tier 1 has no licensing friction. Tier 2 gets content faster via WikEM. Both use identical format.

### Source Licensing Rules

All tier1 content is compiled exclusively from copyright-free or permissively licensed sources:

- **Clinical guidelines** (ACC/AHA, ESC, ATS/IDSA, ACOG, etc.): Facts and clinical recommendations are not copyrightable. We cite guidelines as authoritative references but do not reproduce copyrighted text verbatim.
- **PubMed Open Access** (CC-BY, CC0): Freely reusable with attribution.
- **WHO, CDC publications**: Public domain or open-access government works.
- **Original synthesis**: Clinical knowledge synthesized by AI agents from multiple sources, structured in our own format.

**Explicitly excluded from tier1:**
- StatPearls content (CC BY-NC-ND — no derivatives)
- SNOMED CT codes (redistribution restricted by IHTSDO)
- Copyrighted textbook content (Tintinalli's, Rosen's, etc. — referenced by citation only)
- UpToDate, DynaMed, or other subscription content

**ICD-10-CM codes** are US public domain (maintained by CMS/NCHS) and freely redistributable.

## File Format

Every condition is a Markdown file with YAML frontmatter:

```yaml
---
id: stemi
condition: ST-Elevation Myocardial Infarction
aliases: [STEMI, ST-elevation MI, acute MI with ST elevation]
icd10: [I21.01, I21.02, I21.09, I21.11, I21.19, I21.21, I21.29, I21.3]
esi: 1
time_to_harm: "< 90 minutes"
mortality_if_delayed: "7.5% per 30-minute delay to reperfusion"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "2013 ACCF/AHA Guideline for the Management of ST-Elevation Myocardial Infarction"
  - type: guideline
    ref: "2022 ACC/AHA Guideline for Chest Pain Evaluation and Diagnosis"
  - type: guideline
    ref: "2023 ESC Guidelines for the Management of Acute Coronary Syndromes"
last_updated: "2026-02-18"
compiled_by: agent
risk_tier: A
validation:
  automated_consistency_check: "2026-02-18"
  dose_range_validator: "2026-02-19"
  schema_version: "2.0"
---

# ST-Elevation Myocardial Infarction (STEMI)

## Recognition
...
## Critical Actions
...
## Differential Diagnosis
...
## Workup
...
## Treatment
...
## Disposition
...
## Pitfalls
...
```

### Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `id` | Yes | URL-safe identifier (`lowercase-hyphens-only`) |
| `condition` | Yes | Full clinical name |
| `aliases` | No | Alternative names, abbreviations, lay terms |
| `icd10` | Yes | ICD-10-CM codes (US public domain) |
| `esi` | Yes | Emergency Severity Index (1-5) |
| `time_to_harm` | Yes | Time window before irreversible harm |
| `mortality_if_delayed` | No | Mortality risk with delayed treatment |
| `category` | Yes | One of 20 clinical categories |
| `track` | Yes | `tier1` (Apache 2.0) or `tier2` (CC-BY-SA) |
| `sources` | Yes | Array of citations with `type`, `ref`, optional `pmid`/`doi` |
| `compiled_by` | Yes | `agent` or `human` |
| `risk_tier` | Yes | `A` (high-risk), `B` (moderate), `C` (general) |
| `validation` | Yes | Automated validation checks with dates (see Validation below) |

### Required Sections

Every condition file contains these 7 sections:
1. **Recognition** — How to identify this condition
2. **Critical Actions** — Time-sensitive interventions with targets
3. **Differential Diagnosis** — What else could this be
4. **Workup** — Diagnostic studies and interpretation
5. **Treatment** — Drug doses with routes, procedural interventions
6. **Disposition** — Admission criteria, transfer indications, discharge safety
7. **Pitfalls** — Cognitive traps, atypical presentations, common errors (minimum 7 per condition)

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

# Find conditions with specific ICD-10 codes
rg "I21" corpus/ --glob "*.md"

# List all conditions with their ESI levels
rg "^esi:" corpus/ --glob "*.md"
```

## Structure

```
corpus/
├── tier1/                   # Apache 2.0 (copyright-free sources)
│   ├── conditions/          # 185 condition files (.md)
│   ├── procedures/          # EM procedures (planned)
│   ├── medications/         # EM pharmacology (planned)
│   └── decision-aids/       # Clinical decision rules (planned)
└── tier2/                   # CC-BY-SA 4.0 (WikEM-derived, planned)
    ├── conditions/
    └── procedures/
```

## Validation (Schema v2.0)

Each condition file carries a `validation` block in its frontmatter recording which automated checks have passed. All 185 conditions pass the full suite.

```yaml
validation:
  automated_consistency_check: "2026-02-18"
  dose_range_validator: "2026-02-19"
  unit_normalization_check: "2026-02-19"
  cross_file_consistency_check: "2026-02-19"
  citation_presence_check: "2026-02-19"
  duplicate_content_check: "2026-02-19"
  outlier_detection_flag: clear
  schema_version: "2.0"
  guideline_version_reference: null
```

| Check | What it validates |
|-------|-------------------|
| `automated_consistency_check` | Internal consistency of clinical content |
| `dose_range_validator` | Drug doses within safe ranges |
| `unit_normalization_check` | Consistent units (mg vs mcg, etc.) |
| `cross_file_consistency_check` | Same drug/dose across files for same indication |
| `citation_presence_check` | Every clinical assertion has a source |
| `duplicate_content_check` | No duplicated content across files |
| `outlier_detection_flag` | Flags statistical outliers in dosing/timing |

Each file also carries a `risk_tier` field (A = high-risk, B = moderate, C = general) as informational metadata.

## Agent Team Architecture

This corpus is compiled and maintained by AI agent teams:

| Agent | Model | Role |
|-------|-------|------|
| `condition-compiler` | Sonnet | Synthesizes condition from clinical guidelines and PubMed literature |
| `evidence-reviewer` | Sonnet | Reviews citations for accuracy, currency, and license compatibility |
| `cross-reference-checker` | Sonnet | Validates ICD-10 codes, checks cross-links, finds coverage gaps |
| `clinical-validator` | Opus | Adversarial review for dangerous omissions, incorrect doses, missing contraindications |
| `pmid-verifier` | Script + PubMed API | Batch-verifies all PMIDs against PubMed E-utilities (esummary/esearch) |

### Quality Pipeline

1. **Compile**: Agent synthesizes condition from clinical guidelines and PubMed OA
2. **Evidence Review**: Citations checked for accuracy, currency, and license compatibility
3. **Cross-Reference**: ICD-10 codes validated, differential diagnoses cross-linked
4. **Clinical Validation**: 4-agent adversarial red-team audit — clinical accuracy, evidence basis, licensing, coverage gaps
5. **PMID Verification**: All 450 unique PMIDs batch-verified against PubMed API. Initial compilation had a 23% PMID hallucination rate; all were corrected or removed.
6. **Automated Validation Suite**: 13-check validation pipeline (consistency, dosing, units, cross-file, citations, duplicates, outliers, schema). All 185 conditions pass.

## Attribution and Credit

This corpus is built on the work of the global emergency medicine community:

- **Clinical guidelines** are cited by name in each condition's `sources` field (ACC/AHA, ESC, ATS/IDSA, ACOG, SSC, BTF, ATLS, and many others)
- **PubMed literature** is cited with PMIDs — all 450 unique PMIDs verified against PubMed
- **WikEM / OpenEM Foundation** (CC-BY-SA 4.0) — tier2 content attributes WikEM as source
- **AI compilation** by Claude (Anthropic) agent teams — noted in `compiled_by: agent`
- **Medical review** by Brandon Dent, MD — tracked in `reviewed_by` field

If you use this corpus, please cite:
```
OpenEM Corpus. GOATnote Inc. https://github.com/GOATnote-Inc/openem-corpus
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup, validation workflow, and submission guidelines.

Physician reviewers: review a condition and submit a PR setting `reviewed_by: "Your Name, MD"` in the YAML frontmatter.

## Related Projects

- [ScribeGOAT2](https://github.com/GOATnote-Inc/scribegoat2) — Multi-turn safety evaluation framework (consumes this corpus)
- [LostBench](https://github.com/GOATnote-Inc/lostbench) — Safety persistence benchmark (references this corpus for clinical grounding)

## License

- `corpus/tier1/`: Apache License 2.0 (see `LICENSE-APACHE`)
- `corpus/tier2/`: Creative Commons Attribution-ShareAlike 4.0 International (see `LICENSE-CC-BY-SA`)
- Everything else (scripts, schemas, agent configs): Apache License 2.0
