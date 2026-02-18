# OpenEM Corpus

**The AI-native emergency medicine knowledge base.**
Agent-compiled. Physician-verified. Grep-friendly.

## What This Is

A structured, token-efficient corpus of emergency medicine knowledge designed for AI/LLM consumption. Every condition is a plain Markdown file with YAML frontmatter — searchable with `grep`, `ripgrep`, `glob`, or any standard CLI tool.

Built by [Brandon Dent, MD](https://github.com/GOATnote-Inc) (emergency medicine physician) and AI agent teams. Designed for worldwide healthcare use.

## Why This Exists

No AI-native emergency medicine knowledge corpus exists. WikEM is the world's largest open EM reference but is HTML/wiki format. MedRAG has chunked textbooks but isn't EM-specific. StatPearls is CC BY-NC-ND (no derivatives). This project fills the gap.

## Dual-Track Licensing

| Track | Directory | License | Sources |
|-------|-----------|---------|---------|
| **Tier 1 (Free)** | `corpus/tier1/` | Apache 2.0 | PubMed OA, WHO, CDC, clinical guidelines, original synthesis |
| **Tier 2 (Share-Alike)** | `corpus/tier2/` | CC-BY-SA 4.0 | WikEM-derived content restructured + supplemented |

Tier 1 has no licensing friction. Tier 2 gets content faster via WikEM. Both use identical format.

## File Format

Every condition is a Markdown file with YAML frontmatter:

```yaml
---
id: stemi
condition: ST-Elevation Myocardial Infarction
aliases: [heart attack, STEMI, acute MI]
icd10: [I21.0, I21.1, I21.2, I21.3]
esi: 1
time_to_harm: "< 90 minutes"
mortality_if_delayed: "7-10% per 30min delay"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "2023 ACC/AHA STEMI Guidelines"
last_updated: "2026-02-18"
compiled_by: agent
reviewed_by: null
---

# ST-Elevation Myocardial Infarction (STEMI)

## Recognition
...

## Critical Actions
...
```

## Quick Start

```bash
# Search for all conditions mentioning chest pain
rg "chest pain" corpus/

# Find all ESI-1 conditions
rg "^esi: 1" corpus/ --glob "*.md"

# List all cardiovascular conditions
rg "^category: cardiovascular" corpus/ --glob "*.md" -l

# Find conditions with < 60 minute time-to-harm
rg "time_to_harm:" corpus/ --glob "*.md"
```

## Structure

```
corpus/
├── tier1/                   # Apache 2.0 (copyright-free sources)
│   ├── conditions/          # One .md per condition
│   ├── procedures/          # EM procedures
│   ├── medications/         # EM pharmacology
│   └── decision-aids/       # Clinical decision rules
└── tier2/                   # CC-BY-SA 4.0 (WikEM-derived)
    ├── conditions/
    └── procedures/
```

## Agent Team Architecture

This corpus is compiled and maintained by AI agent teams:

| Agent | Role |
|-------|------|
| `condition-compiler` | Ingests source material, produces first-draft .md files |
| `evidence-reviewer` | Reviews against PubMed sources, checks citations |
| `cross-reference-checker` | Validates ICD/SNOMED codes, checks cross-links |
| `clinical-validator` | Final quality gate from clinical accuracy perspective |

## Contributing

Contributions welcome. Every file must:
1. Follow the schema in `schemas/condition.schema.yaml`
2. Include at least one verifiable source citation
3. Pass validation (`python scripts/validate.py`)

Physician review is tracked in the `reviewed_by` frontmatter field.

## Related Projects

- [ScribeGOAT2](https://github.com/GOATnote-Inc/scribegoat2) — Multi-turn safety evaluation framework (consumes this corpus)
- [LostBench](https://github.com/GOATnote-Inc/lostbench) — Safety persistence benchmark (references this corpus for clinical grounding)

## License

- `corpus/tier1/`: Apache License 2.0 (see `LICENSE-APACHE`)
- `corpus/tier2/`: Creative Commons Attribution-ShareAlike 4.0 International (see `LICENSE-CC-BY-SA`)
- Everything else (scripts, schemas, agent configs): Apache License 2.0
