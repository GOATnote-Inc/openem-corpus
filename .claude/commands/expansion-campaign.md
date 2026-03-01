# Expansion Campaign

Full agent team campaign for EM content distribution alignment. Runs gap analysis, parallel category compilation, quality gates, index rebuild, and integration testing.

## Usage
```
/expansion-campaign [phase]
```

Phases: `p0`, `p1`, `p2`, or `all`

## Team Structure

```
TEAM LEAD (Opus) — orchestration + quality gate
├── category-compiler-1 (Sonnet) — partition A categories
├── category-compiler-2 (Sonnet) — partition B categories
├── category-compiler-3 (Sonnet) — partition C categories
├── category-compiler-4 (Sonnet) — partition D categories (if needed)
└── integration-tester (Sonnet) — post-batch verification
```

## Phase Definitions

### Phase P0 (~95 conditions)
- **Partition A:** cardiovascular (+18) + respiratory (+16) = 34 conditions
- **Partition B:** traumatic (+24) = 24 conditions
- **Partition C:** procedural (+21) = 21 conditions
- **Partition D:** gastrointestinal (+16) = 16 conditions

### Phase P1 (~62 conditions)
- **Partition A:** neurological (+11) + endocrine-metabolic (+11) = 22 conditions
- **Partition B:** infectious (+12) + hematologic (+6) + dermatologic (+7) = 25 conditions
- **Partition C:** presentations (+15) = 15 conditions (uses `presentations-compiler`)

### Phase P2 (~21 conditions)
- **Single partition:** genitourinary (+5), pediatric (+5), ophthalmologic (+4), allergic-immunologic (+3), psychiatric (+2), musculoskeletal (+1), disaster-mci (+1)

## Process

### Step 1: Gap Analysis
Run the **gap-analyst** agent to produce the prioritized condition list for this phase:
- Read `data/abem_mapping.yaml` for targets
- Inventory current corpus
- Consult downstream findings via `scripts/scan_repos.py`
- Output the finalized condition list per category

### Step 2: Parallel Category Compilation
Each category-compiler teammate runs `/expand-category` for their assigned categories. Per condition:
1. `condition-compiler` or `presentations-compiler` → draft
2. `evidence-reviewer` → citation verification
3. `sourcing-auditor` → license check
4. `cross-reference-checker` → ICD-10 + consistency
5. `clinical-validator` → clinical accuracy gate

### Step 3: Quality Gate (Team Lead)
After all teammates complete their batches:

```bash
cd /Users/kiteboard/openem-corpus

# Schema validation (all conditions)
python scripts/validate.py

# Full audit suite (13 passes, 3 blocking)
python scripts/audit.py

# Diversity metrics (category balance)
python scripts/diversity_metrics.py

# Condition map regeneration test
PYTHONPATH=python python -c "from openem.conditions import load_condition_map; cm = load_condition_map(); print(f'{len(cm)} entries')"
```

### Step 4: Index Rebuild
```bash
python scripts/build_index.py --incremental
python scripts/check_index_freshness.py
```

### Step 5: Retrieval Evaluation
```bash
python scripts/eval_retrieval.py
```
Targets: Recall@5 >= 0.70, MRR >= 0.75

### Step 6: Integration Testing
Run the **integration-tester** agent for full downstream verification:
- Condition map + overlay validation
- ScribeGoat2 bridge test
- LostBench bridge test
- SafeShift integration test
- Full test suite

### Step 7: Overlay Update
Update `python/openem/overlay.yaml` with aliases for all new conditions.

## Completion Criteria
- All target conditions compiled and validated
- Schema validation: 100% pass
- Audit (3 blocking checks): 100% pass
- Retrieval eval: Recall@5 >= 0.70, MRR >= 0.75
- All downstream bridge tests pass
- Test suite: 0 failures
- Overlay updated with new aliases

## Notes
- Teammates should claim conditions from the shared task list to avoid duplication
- Process within each partition is sequential (for cross-reference consistency)
- Partitions can run in parallel
- If a condition fails the clinical validator, address revisions before moving to the next condition
- Log progress: after each batch, note completed count vs target in the task list
