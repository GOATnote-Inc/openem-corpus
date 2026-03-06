# Changelog

## v0.5.0 (2026-03-06) — Depth Over Breadth

### Safety Metadata Deepening
- **confusion_pairs** expanded from 38 to 152 conditions (41% coverage) — maps conditions with similar presentation but different acuity
- **decision_rules** expanded from 15 to 45 conditions — clinical scoring systems (Wells, PERC, qSOFA, NIHSS, HEART, etc.) with citations and PMIDs
- **evaluation_properties** expanded from 4 to 44 conditions — pressure vulnerability, imaging modalities from downstream evaluations (LostBench, RadSlice)

### New Conditions (7)
- **6 ENT/otolaryngology**: epistaxis, post-tonsillectomy-hemorrhage, sudden-sensorineural-hearing-loss, dental-emergency, nasal-septal-hematoma, parapharyngeal-abscess
- **1 LostBench demand signal**: malignant-spinal-cord-compression
- All new conditions include confusion_pairs from day one
- Total: 363 → 370 conditions

### Downstream Alignment
- RadSlice overlay fixes: `appendicitis` → `acute-appendicitis`, `pneumothorax` → `[spontaneous-pneumothorax, tension-pneumothorax]`, `rib-fracture` → `flail-chest`
- Overlay aliases added for all 7 new conditions
- ABEM mapping updated with v0.5.0 condition counts

### Quality
- All 370 conditions pass schema v2.0 validation
- 13-pass audit: 0 critical findings
- Quality gate: all 6 blocking gates pass
- All confusion_pairs reference valid condition_ids (machine-verified)

## v2.0 (2026-02-23)

### Schema Extensions
- Added `disposition_default`, `escalation_triggers`, `confusion_pairs` fields
- `time_to_harm` now supports structured object form (`oneOf` string|object) with `typical`, `worst_case`, `modifiers`
- Schema version bumped to 2.0 in all condition files

### New Conditions
- **6 defer conditions** (ESI 4-5): benign-positional-vertigo, pediatric-acute-otitis-media, knee-osteoarthritis, tension-headache, panic-attack, benign-palpitations
- **4 gap conditions**: foreign-body-aspiration, snakebite-envenomation, uterine-rupture, pprom
- **19 expansion conditions** across existing categories
- Total: 128 → 157 tier1 conditions

### Safety Annotations
- Operational Substitution Risks on 6 high-traffic conditions
- Structured time_to_harm on 10 risk_tier A conditions
- Adversarial presentations on 10 conditions

### Quality
- Audit suite expanded from 8 to 13 passes
- All 157 conditions pass full validation suite

## v1.0 (2026-02-18)

### Initial Release
- 128 tier1 conditions across 18 clinical categories
- Schema v1.0 with YAML frontmatter validation
- 631 source citations (450 unique PMIDs)
- 8-pass automated validation suite
- Dual-track licensing: Apache 2.0 (tier1) + CC-BY-SA 4.0 (tier2)
- Python package with LanceDB hybrid search index
