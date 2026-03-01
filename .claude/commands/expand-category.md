# Expand Category

Compile a batch of conditions for a single category using the full agent pipeline.

## Usage
```
/expand-category [category] [condition1, condition2, ...]
```

Examples:
```
/expand-category cardiovascular complete-heart-block, wpw-syndrome, torsades-de-pointes
/expand-category presentations chest-pain, syncope, dyspnea
```

## Process

### Step 1: Gap Validation
Before compiling, verify these conditions don't already exist:
- Read `corpus/tier1/conditions/` to check for existing files
- Check `python/openem/overlay.yaml` for existing aliases
- Consult `data/abem_mapping.yaml` to confirm these conditions are in the expansion plan

### Step 2: Per-Condition Compilation
For each condition in the batch, run the `/compile-condition` pipeline:

1. **condition-compiler** (Sonnet) or **presentations-compiler** (Sonnet, for `presentations` category): Research and draft the .md file
2. **evidence-reviewer** (Sonnet): Verify citations against primary sources
3. **sourcing-auditor** (Haiku): Check every source license is tier1-compliant
4. **cross-reference-checker** (Sonnet): Validate ICD-10-CM codes, check cross-links
5. **clinical-validator** (Opus): Final clinical accuracy review

### Step 3: Batch Validation
After all conditions in the batch are compiled:

```bash
cd /Users/kiteboard/openem-corpus

# Schema validation
python scripts/validate.py

# Audit suite (3 blocking checks)
python scripts/audit.py

# Diversity metrics (check category balance)
python scripts/diversity_metrics.py
```

### Step 4: Overlay Update
Add aliases for new conditions to `python/openem/overlay.yaml` where clinically appropriate (e.g., abbreviations, alternative names, common misspellings).

## Completion Criteria
- All condition files exist at `corpus/tier1/conditions/{id}.md`
- `python scripts/validate.py` passes with 0 errors
- `python scripts/audit.py` — all 3 blocking checks pass
- Clinical validator approved all conditions (or revisions addressed)
- Sourcing auditor verified all citations are tier1-compliant
- Overlay updated with new aliases

## Notes
- For the `presentations` category, use `presentations-compiler` instead of `condition-compiler`
- Process conditions sequentially within the batch to avoid cross-reference conflicts
- If a condition references another condition that doesn't exist yet, note it as a gap to be filled later
