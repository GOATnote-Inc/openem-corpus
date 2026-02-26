# OpenEM Corpus — Detailed Reference

This document contains detailed information about the corpus structure, validation, categories, and agent architecture. For quick-start usage, see the [README](../README.md).

## Category Coverage

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

## Condition Expansion (v2.1)

The corpus has grown from 128 to 185 tier1 conditions:
- **6 defer conditions** (ESI 4-5): benign-positional-vertigo, pediatric-acute-otitis-media, knee-osteoarthritis, tension-headache, panic-attack, benign-palpitations
- **4 gap conditions**: foreign-body-aspiration, snakebite-envenomation, uterine-rupture, pprom
- **19 expansion conditions**: Additional high-priority conditions across existing categories
- **28 MCI/HALO/procedural conditions**: mass-casualty-triage, active-shooter-response, resuscitative-thoracotomy, perimortem-cesarean-delivery, lateral-canthotomy, difficult-airway-management, and more

## Source Composition

| Source Type | Count |
|-------------|-------|
| Clinical guidelines (ACC/AHA, ACEP, IDSA, etc.) | 257 |
| PubMed-indexed original research | 219 |
| Review articles | 130 |
| Meta-analyses | 22 |
| CDC publications | 3 |

## Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `id` | Yes | URL-safe identifier (`lowercase-hyphens-only`) |
| `condition` | Yes | Full clinical name |
| `aliases` | No | Alternative names, abbreviations, lay terms |
| `icd10` | Yes | ICD-10-CM codes (US public domain) |
| `esi` | Yes | Emergency Severity Index (1-5) |
| `time_to_harm` | Yes | Time window before irreversible harm (string or structured object) |
| `mortality_if_delayed` | No | Mortality risk with delayed treatment |
| `category` | Yes | One of 20 clinical categories |
| `track` | Yes | `tier1` (Apache 2.0) or `tier2` (CC-BY-SA) |
| `sources` | Yes | Array of citations with `type`, `ref`, optional `pmid`/`doi` |
| `compiled_by` | Yes | `agent` or `human` |
| `reviewed_by` | No | Physician reviewer name and credentials |
| `review_date` | No | ISO 8601 date of physician review |
| `risk_tier` | Yes | `A` (high-risk), `B` (moderate), `C` (general) |
| `validation` | Yes | Automated validation checks with dates |

## Validation (Schema v2.0)

Each condition file carries a `validation` block recording which automated checks have passed. All 185 conditions pass the full 13-check suite.

| Check | What it validates |
|-------|-------------------|
| `automated_consistency_check` | Internal consistency of clinical content |
| `dose_range_validator` | Drug doses within safe ranges |
| `unit_normalization_check` | Consistent units (mg vs mcg, etc.) |
| `cross_file_consistency_check` | Same drug/dose across files for same indication |
| `citation_presence_check` | Every clinical assertion has a source |
| `duplicate_content_check` | No duplicated content across files |
| `outlier_detection_flag` | Flags statistical outliers in dosing/timing |

Three checks are **blocking** in CI (cross_file_dosing, dose_range_anomaly, content_completeness). The remaining checks are informational.

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
5. **PMID Verification**: All 450 unique PMIDs batch-verified against PubMed API (initial 23% hallucination rate corrected)
6. **Automated Validation Suite**: 13-check pipeline. All 185 conditions pass.
7. **Physician Review**: Risk tier A conditions reviewed by board-certified emergency medicine physician

## Source Licensing Rules

All tier1 content is compiled exclusively from copyright-free or permissively licensed sources:

- **Clinical guidelines** (ACC/AHA, ESC, ATS/IDSA, ACOG, etc.): Facts and clinical recommendations are not copyrightable
- **PubMed Open Access** (CC-BY, CC0): Freely reusable with attribution
- **WHO, CDC publications**: Public domain or open-access government works
- **Original synthesis**: Clinical knowledge synthesized by AI agents from multiple sources

**Explicitly excluded from tier1:** StatPearls (CC BY-NC-ND), SNOMED CT codes (restricted redistribution), copyrighted textbooks, UpToDate/DynaMed.

**ICD-10-CM codes** are US public domain (maintained by CMS/NCHS) and freely redistributable.

## Directory Structure

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

## Attribution and Credit

- **Clinical guidelines** are cited by name in each condition's `sources` field
- **PubMed literature** is cited with PMIDs — all 450 unique PMIDs verified against PubMed
- **WikEM / OpenEM Foundation** (CC-BY-SA 4.0) — tier2 content attributes WikEM as source
- **AI compilation** by Claude (Anthropic) agent teams — noted in `compiled_by: agent`
- **Medical review** by Brandon Dent, MD — tracked in `reviewed_by` field

## Related Projects

- [ScribeGOAT2](https://github.com/GOATnote-Inc/scribegoat2) — Multi-turn safety evaluation framework
- [LostBench](https://github.com/GOATnote-Inc/lostbench) — Safety persistence benchmark
- [SafeShift](https://github.com/GOATnote-Inc/safeshift) — Safety degradation under inference optimization
