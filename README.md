# OpenEM Corpus

**The AI-native emergency medicine knowledge base.**
Agent-compiled. Physician-verified. Grep-friendly.

## What This Is

A structured, token-efficient corpus of emergency medicine knowledge designed for AI/LLM consumption. Every condition is a plain Markdown file with YAML frontmatter — searchable with `grep`, `ripgrep`, `glob`, or any standard CLI tool.

Built by [Brandon Dent, MD](https://github.com/GOATnote-Inc) (emergency medicine physician) and AI agent teams. Designed for worldwide healthcare use.

## Corpus at a Glance

| Metric | Value |
|--------|-------|
| Conditions | 93 |
| Words | ~149,000 |
| Source citations | 456 (292 with verified PMIDs) |
| Categories | 18 / 18 |
| ESI 1 (resuscitation) | 42 |
| ESI 2 (emergent) | 45 |
| ESI 3 (urgent) | 6 |
| License | Apache 2.0 (tier1) |
| PMIDs verified against PubMed | 292 / 292 |
| Physician-reviewed | Not yet — all `reviewed_by: null` |

### Category Coverage

| Category | Count | Category | Count |
|----------|-------|----------|-------|
| cardiovascular | 13 | neurological | 5 |
| infectious | 8 | endocrine-metabolic | 5 |
| toxicologic | 7 | pediatric | 5 |
| gastrointestinal | 7 | ophthalmologic | 4 |
| respiratory | 6 | genitourinary | 4 |
| environmental | 6 | hematologic | 4 |
| obstetric-gynecologic | 6 | dermatologic | 3 |
| musculoskeletal | 3 | traumatic | 3 |
| psychiatric | 2 | allergic-immunologic | 2 |

### Source Composition

| Source Type | Count |
|-------------|-------|
| Clinical guidelines (ACC/AHA, ACEP, IDSA, etc.) | 205 |
| PubMed-indexed original research | 175 |
| Review articles | 71 |
| Meta-analyses | 3 |
| CDC publications | 2 |

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
aliases: [heart attack, STEMI, acute MI]
icd10: [I21.0, I21.1, I21.2, I21.3]
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
reviewed_by: null
verification:
  pmids_verified: "2026-02-18"
  audit_completed: "2026-02-18"
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
| `category` | Yes | One of 18 clinical categories |
| `track` | Yes | `tier1` (Apache 2.0) or `tier2` (CC-BY-SA) |
| `sources` | Yes | Array of citations with `type`, `ref`, optional `pmid`/`doi` |
| `compiled_by` | Yes | `agent` or `human` |
| `reviewed_by` | No | Physician name, or `null` if unreviewed |
| `verification` | No | Map of check names to dates (see Verification below) |

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
│   ├── conditions/          # 93 condition files (.md)
│   ├── procedures/          # EM procedures (planned)
│   ├── medications/         # EM pharmacology (planned)
│   └── decision-aids/       # Clinical decision rules (planned)
└── tier2/                   # CC-BY-SA 4.0 (WikEM-derived, planned)
    ├── conditions/
    └── procedures/
```

## Verification

Each condition file carries a `verification` object in its frontmatter that records what mechanical checks have actually been performed. Each key is a check name; each value is the ISO 8601 date it passed. Absence of a key means that check has not been run.

```yaml
verification:
  pmids_verified: "2026-02-18"    # all PMIDs verified against PubMed E-utilities API
  audit_completed: "2026-02-18"   # 4-agent clinical accuracy audit completed, issues resolved
```

Current checks performed on all 93 conditions:

| Check | What it means | Date |
|-------|--------------|------|
| `pmids_verified` | Every PMID in the file was fetched from PubMed and confirmed to match the cited paper (author + title) | 2026-02-18 |
| `audit_completed` | File passed a 4-agent adversarial clinical accuracy audit; identified errors were corrected | 2026-02-18 |

Future checks (not yet performed): `dosing_crosscheck`, `icd10_verified`, `guideline_currency`.

This field is intentionally not a quality grade. An A/B/C evidence tier would be either redundant (derivable from `sources[].type`) or unreliable (agents can't credibly self-grade). The `verification` object records binary facts about what was checked, not judgments about quality. The real quality signal is `reviewed_by` — and that's `null` on every file until a physician reviews it.

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
5. **PMID Verification**: All PMIDs batch-verified against PubMed API. Initial compilation had a 23% PMID hallucination rate; all were corrected or removed.
6. **Physician Review**: Human physician attestation (tracked in `reviewed_by` field) — not yet started

## Attribution and Credit

This corpus is built on the work of the global emergency medicine community:

- **Clinical guidelines** are cited by name in each condition's `sources` field (ACC/AHA, ESC, ATS/IDSA, ACOG, SSC, BTF, ATLS, and many others)
- **PubMed literature** is cited with PMIDs — all 292 PMIDs verified against PubMed
- **WikEM / OpenEM Foundation** (CC-BY-SA 4.0) — tier2 content attributes WikEM as source
- **AI compilation** by Claude (Anthropic) agent teams — noted in `compiled_by: agent`
- **Medical review** by Brandon Dent, MD — tracked in `reviewed_by` field

If you use this corpus, please cite:
```
OpenEM Corpus. GOATnote Inc. https://github.com/GOATnote-Inc/openem-corpus
```

## Contributing

Contributions welcome. Every file must:
1. Follow the schema in `schemas/condition.schema.yaml`
2. Include at least one verifiable source citation
3. Pass validation (`python scripts/validate.py`)
4. Not include StatPearls content or SNOMED CT codes

Physician reviewers: review a condition and submit a PR setting `reviewed_by: "Your Name, MD"`.

Run corpus statistics:
```bash
python scripts/stats.py
```

Validate all files:
```bash
python scripts/validate.py
```

## Related Projects

- [ScribeGOAT2](https://github.com/GOATnote-Inc/scribegoat2) — Multi-turn safety evaluation framework (consumes this corpus)
- [LostBench](https://github.com/GOATnote-Inc/lostbench) — Safety persistence benchmark (references this corpus for clinical grounding)

## License

- `corpus/tier1/`: Apache License 2.0 (see `LICENSE-APACHE`)
- `corpus/tier2/`: Creative Commons Attribution-ShareAlike 4.0 International (see `LICENSE-CC-BY-SA`)
- Everything else (scripts, schemas, agent configs): Apache License 2.0
