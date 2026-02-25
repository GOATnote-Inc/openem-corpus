# Contributing to OpenEM Corpus

Contributions welcome. This document describes how to add or improve condition files.

## Requirements

Every contributed file must:

1. Follow the schema in `schemas/condition.schema.yaml` (v2.0)
2. Include at least one verifiable source citation (PubMed OA, WHO, CDC, or clinical guidelines)
3. Pass validation: `python scripts/validate.py`
4. Not include StatPearls content (CC BY-NC-ND) or redistribute SNOMED CT codes

## Development Setup

```bash
git clone https://github.com/GOATnote-Inc/openem-corpus.git
cd openem-corpus
pip install -e ".[dev]"
```

## Validation

Run the full check suite before submitting:

```bash
# Schema validation (required to pass)
python scripts/validate.py

# 13-pass automated audit
python scripts/audit.py

# Full check: validate + quality-gate + audit + tests
make check
```

## Adding a Condition

1. Create a new Markdown file in `corpus/tier1/conditions/` (Apache 2.0) or `corpus/tier2/conditions/` (CC-BY-SA)
2. Use kebab-case for the filename matching the `id` field (e.g., `septic-arthritis.md`)
3. Include all required YAML frontmatter fields (see `schemas/condition.schema.yaml`)
4. Include all required body sections: Recognition, Critical Actions, Differential Diagnosis, Workup, Treatment, Disposition, Pitfalls
5. Run `python scripts/validate.py` to confirm schema compliance
6. Run `python scripts/audit.py` to check cross-file consistency

## Physician Review

Physician reviewers: review a condition and submit a PR setting `reviewed_by: "Your Name, MD"` in the YAML frontmatter.

## Licensing

- **Tier 1** (`corpus/tier1/`): Apache License 2.0. Only copyright-free sources: PubMed OA (CC-BY/CC0), WHO, CDC, clinical guidelines, or original agent-authored synthesis.
- **Tier 2** (`corpus/tier2/`): CC-BY-SA 4.0. WikEM-derived content must attribute WikEM/OpenEM Foundation.

## Pull Request Process

1. Fork the repository and create a feature branch
2. Make your changes and ensure `make check` passes
3. Submit a PR with a description of what was added or changed
4. CI will run schema validation, tests, audit, and quality-gate checks automatically
