# Physician Review Guide

This document describes how clinicians can review OpenEM conditions and contribute their expertise.

## What "Review" Means

A review verifies clinical accuracy of these sections:

- **Recognition** — Are the diagnostic criteria correct and complete?
- **Critical Actions** — Are time-sensitive interventions accurate with correct targets?
- **Treatment** — Are drug doses correct (dose, route, frequency, weight-basis)?
- **Pitfalls** — Are the cognitive traps and atypical presentations clinically valid?

Flag any:
- Dose errors (wrong dose, wrong route, wrong frequency)
- Missing contraindications
- Dangerous omissions (critical actions missing from high-acuity conditions)
- Outdated guidelines (superseded by newer evidence)

You are NOT expected to rewrite content. Flag issues and the compilation team will fix them.

## How to Claim a Condition

1. Fork the repository
2. Pick an unreviewed condition (run `python scripts/review_status.py` to see what's available)
3. Review the clinical content
4. Add to the YAML frontmatter (after `compiled_by: agent`):
   ```yaml
   reviewed_by: "Your Name, MD — Your Board Certification"
   review_date: "YYYY-MM-DD"
   ```
5. Submit a PR with your review

If you find errors, note them in the PR description. Minor fixes (typos, formatting) can be made directly.

## Review Priority

1. **Risk Tier A** (ESI 1) — highest-acuity, time-critical conditions
2. **Risk Tier B** (ESI 2) — emergent conditions
3. **Risk Tier C** (ESI 3+) — urgent and less-urgent conditions

Run `python scripts/review_status.py` to see current status and priority ordering.

## What's Already Reviewed

All 80 risk_tier A (ESI 1) conditions have been reviewed by the corpus author (board-certified emergency medicine physician). The remaining 105 conditions across risk tiers B and C need review.

## Quality Standards

- This corpus is written for emergency physicians, not patients
- Drug doses must include route and frequency
- Time-to-harm must be specific (e.g., "< 6 hours" not "time-sensitive")
- Each condition must have at least 7 pitfalls
- All content must be sourced (check the `sources:` frontmatter)

## Questions?

Open an issue on the repository or contact the maintainers.
