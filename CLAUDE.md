# OpenEM Corpus — Agent Instructions

## Project Purpose
AI-native emergency medicine knowledge base. Agent-compiled, physician-verified, grep-friendly.

## Core Rules
1. **Truth-seeking above all.** Never soften clinical facts for readability. If evidence is uncertain, say so explicitly.
2. **Every claim needs a source.** No unsourced medical assertions. Use `sources:` frontmatter and inline citations.
3. **Tier 1 is copyright-free only.** Apache 2.0 track. Only PubMed OA (CC-BY/CC0), WHO, CDC, clinical guidelines, or original physician-authored synthesis. NO StatPearls (CC BY-NC-ND), NO copyrighted textbooks.
4. **Tier 2 is CC-BY-SA.** WikEM-derived content must attribute WikEM/OpenEM Foundation. Share-alike applies.
5. **One file per condition.** `corpus/tier1/conditions/{id}.md` or `corpus/tier2/conditions/{id}.md`.
6. **YAML frontmatter is mandatory.** Must validate against `schemas/condition.schema.yaml`.
7. **Append to run_log.jsonl** after any batch compilation or audit. Same pattern as scribegoat2.
8. **ICD-10-CM codes only** (US public domain). Do NOT ship SNOMED CT codes in the repo (redistribution restricted).

## File Format
- Markdown with YAML frontmatter (see README.md for example)
- Sections: Recognition, Critical Actions, Differential Diagnosis, Workup, Treatment, Disposition, Pitfalls
- Token-efficient: no filler, no hedging, no "it is important to note that"

## Agent Team Workflows
- `/compile-condition [name]` — Spawn team to compile one condition
- `/review-evidence [file]` — Spawn team to review citations
- `/audit-corpus` — Spawn team to audit all conditions for staleness

## Quality Bar
- Every condition must have: id, condition name, at least one ICD-10 code, ESI level, time-to-harm, at least one source
- `compiled_by: agent` until physician reviews, then `reviewed_by: [name]`
- Pitfalls section is mandatory — this is where clinical value lives
