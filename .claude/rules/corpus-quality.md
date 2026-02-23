# Corpus Quality Rules

## Every condition file MUST have:
1. Valid YAML frontmatter matching `schemas/condition.schema.yaml` (v2.0)
2. All required sections: Recognition, Critical Actions, Differential Diagnosis, Workup, Treatment, Disposition, Pitfalls
3. At least one verifiable source citation
4. Accurate ICD-10-CM codes (US public domain only)
5. Filename matching the `id` field (e.g., `stemi.md` for `id: stemi`)
6. `risk_tier:` field (A, B, or C)
7. `validation:` block with `schema_version: "2.0"`

## Content standards:
- Write for emergency physicians, not patients
- No hedging language ("consider", "may want to", "it is important to note")
- Specific drug doses with routes (e.g., "epinephrine 0.3mg IM" not "give epinephrine")
- Time-to-harm must be specific (e.g., "< 6 hours" not "time-sensitive")
- Pitfalls section must include at least 3 items
- Drug doses must be cross-file consistent (same drug, same indication = same dose everywhere)

## Validation model:
- No manual review requirements. All quality gates are machine-automated.
- `scripts/validate.py` enforces schema compliance
- `scripts/audit.py` runs 13 automated validation passes
- Risk tiers (A/B/C) are informational metadata, not gatekeeping

## Licensing:
- tier1: ONLY use PubMed OA (CC-BY/CC0), WHO, CDC, clinical guidelines, original synthesis
- tier2: May use WikEM content with attribution to OpenEM Foundation
- NEVER include StatPearls content (CC BY-NC-ND — no derivatives)
- NEVER redistribute SNOMED CT codes (reference in comments only)
