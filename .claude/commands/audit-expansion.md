# Audit Expansion

Post-expansion audit: schema validation, diversity metrics, retrieval evaluation, and downstream compatibility testing.

## Usage
```
/audit-expansion
```

Run this after any batch of new conditions is added to the corpus.

## Team

1. **cross-reference-checker** (Sonnet): Validate all ICD-10-CM codes across the full corpus, check cross-references between new and existing conditions, identify orphaned references.

2. **sourcing-auditor** (Haiku): Batch-verify all sources in newly added conditions. Check PMC license compliance, confirm no blocked sources.

3. **integration-tester** (Sonnet): Run the full integration test suite — schema validation, audit, condition map, overlay, retrieval eval, diversity metrics, downstream bridges, test suite.

4. **clinical-validator** (Opus): Spot-check a random sample of new conditions (at least 10% of the batch or 5, whichever is greater). Focus on cross-category consistency — do new cardiovascular conditions conflict with existing ones? Do new differentials reference conditions correctly?

## Automated Checks

```bash
cd /Users/kiteboard/openem-corpus

# 1. Schema validation (all conditions)
python scripts/validate.py

# 2. Full audit suite (13 passes)
python scripts/audit.py

# 3. Diversity metrics
python scripts/diversity_metrics.py

# 4. Condition map test
PYTHONPATH=python python -c "
from openem.conditions import load_condition_map
cm = load_condition_map()
print(f'Condition map: {len(cm)} entries')
"

# 5. Index rebuild + freshness
python scripts/build_index.py --incremental
python scripts/check_index_freshness.py

# 6. Retrieval evaluation
python scripts/eval_retrieval.py

# 7. Overlay validation
python scripts/validate.py --overlay

# 8. Test suite
PYTHONPATH=python pytest tests/ -v --ignore=tests/test_index.py
```

## Output

Produce a structured audit report:

```
EXPANSION AUDIT REPORT
======================
Date: {ISO 8601}
Conditions before: {N}
Conditions after: {M}
New conditions: {M - N}

AUTOMATED CHECKS
  Schema validation:     PASS/FAIL
  Audit (blocking):      PASS/FAIL
  Audit (informational): {N} findings
  Condition map:         {N} entries
  Overlay validation:    PASS/FAIL
  Index rebuild:         PASS/FAIL
  Retrieval Recall@5:    {value} (target >= 0.70)
  Retrieval MRR:         {value} (target >= 0.75)
  Diversity entropy:     {value}
  Test suite:            {N} passed, {M} skipped, {K} failed

CROSS-REFERENCE AUDIT
  Orphaned references:   {N} (conditions referenced but not in corpus)
  Duplicate aliases:     {N}
  ICD-10 validation:     {N}/{M} valid

SOURCE AUDIT
  Total sources checked: {N}
  License compliant:     {N}
  License risks:         {N}
  Blocked sources:       {N}

CLINICAL SPOT-CHECK
  Conditions reviewed:   {N}
  Approved:              {N}
  Revisions needed:      {N}

DOWNSTREAM COMPATIBILITY
  ScribeGoat2 bridge:    PASS/FAIL
  LostBench bridge:      PASS/FAIL
  SafeShift integration: PASS/FAIL

Overall: PASS/FAIL
```

## Completion Criteria
- All automated checks pass
- No license risks in new conditions
- Clinical spot-check: all reviewed conditions approved (or revisions tracked)
- All downstream bridges load successfully
- Retrieval metrics at or above thresholds
