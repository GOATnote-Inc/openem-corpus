# Compile Condition

Compile a single emergency medicine condition into the corpus.

## Usage
```
/compile-condition [condition name]
```

## Team
Spawn an agent team with the following roles:

1. **condition-compiler** (Sonnet): Research the condition and draft the .md file in `corpus/tier1/conditions/`. Follow the schema in `schemas/condition.schema.yaml`. Include all required sections: Recognition, Critical Actions, Differential Diagnosis, Workup, Treatment, Disposition, Pitfalls.

2. **evidence-reviewer** (Sonnet): After the compiler finishes, review every clinical claim against its cited source. Flag unsupported, outdated, or inaccurate claims.

3. **cross-reference-checker** (Sonnet): Validate ICD-10-CM codes, check that conditions mentioned in the differential exist in the corpus (or flag as gaps), verify internal consistency.

4. **clinical-validator** (Opus): Final review for clinical accuracy. Check for dangerous omissions, incorrect doses, missing contraindications. Must approve before the file is considered complete.

## Completion Criteria
- File exists at `corpus/tier1/conditions/{id}.md`
- Passes `python scripts/validate.py`
- Clinical validator has approved or listed revisions
- All revisions from clinical validator have been addressed
