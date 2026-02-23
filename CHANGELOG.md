# Changelog

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
