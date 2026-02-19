# OpenEM Corpus — Agent Instructions

## Project Purpose
AI-native emergency medicine training corpus. Agent-compiled, machine-validated, grep-friendly.
Designed for model training, evaluation, and research (e.g., NemotronNano 30B fine-tuning).
NOT a clinical decision support tool. NOT deployed for patient care.

## Core Rules
1. **Truth-seeking above all.** Never soften clinical facts for readability. If evidence is uncertain, say so explicitly.
2. **Every claim needs a source.** No unsourced medical assertions. Use `sources:` frontmatter and inline citations.
3. **Tier 1 is copyright-free only.** Apache 2.0 track. Only PubMed OA (CC-BY/CC0), WHO, CDC, clinical guidelines, or original agent-authored synthesis. NO StatPearls (CC BY-NC-ND), NO copyrighted textbooks.
4. **Tier 2 is CC-BY-SA.** WikEM-derived content must attribute WikEM/OpenEM Foundation. Share-alike applies.
5. **One file per condition.** `corpus/tier1/conditions/{id}.md` or `corpus/tier2/conditions/{id}.md`.
6. **YAML frontmatter is mandatory.** Must validate against `schemas/condition.schema.yaml` (v2.0).
7. **Append to run_log.jsonl** after any batch compilation or audit. Same pattern as scribegoat2.
8. **ICD-10-CM codes only** (US public domain). Do NOT ship SNOMED CT codes in the repo (redistribution restricted).

## Validation Model
- **No manual attestation layer.** All quality gates are automated.
- `validation:` frontmatter block tracks machine-validation passes (dates, flags).
- `risk_tier:` classifies conditions as A (high-risk), B (moderate), C (general) — informational only.
- `scripts/validate.py` — schema validation (must pass for build).
- `scripts/audit.py` — 8-pass automated validation suite (flags issues, does not block build).

## File Format
- Markdown with YAML frontmatter (see README.md for example)
- Sections: Recognition, Critical Actions, Differential Diagnosis, Workup, Treatment, Disposition, Pitfalls
- Token-efficient: no filler, no hedging, no "it is important to note that"

## Agent Team Workflows
- `/compile-condition [name]` — Spawn team to compile one condition
- `/review-evidence [file]` — Spawn team to review citations
- `/audit-corpus` — Spawn team to run full audit suite

## Quality Bar
- Every condition must have: id, condition name, at least one ICD-10 code, ESI level, time-to-harm, risk_tier, validation block, at least one source
- `compiled_by: agent` — all content is agent-compiled
- Pitfalls section is mandatory — this is where clinical value lives
- All drug doses must include route, frequency, and weight-basis where applicable
- Cross-file dosing must be internally consistent
