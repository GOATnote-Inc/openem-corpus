# Audit Corpus

Run a full audit of all conditions in the corpus.

## Usage
```
/audit-corpus
```

## Team
1. **cross-reference-checker** (Sonnet): Validate all ICD-10-CM codes, check cross-references between conditions, find gaps in differential diagnoses, detect duplicates.

2. **evidence-reviewer** (Sonnet): Check for conditions with sources older than 5 years. Flag any that may have newer guidelines available.

3. **clinical-validator** (Opus): Review the overall corpus for coverage gaps. Are there high-acuity EM conditions missing? Are any conditions clinically incomplete?

## Output
An audit report with:
- Total conditions by tier, category, ESI level
- Conditions needing updated sources
- Cross-reference gaps (conditions mentioned in differentials but not in corpus)
- Coverage gaps (high-acuity conditions not yet compiled)
- ICD-10-CM validation results
