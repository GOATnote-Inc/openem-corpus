# Onboarding Screening Quiz

## Purpose

This quiz screens new reviewers before they receive live condition assignments. It measures two capabilities:

1. **Sensitivity** -- can you find real errors in clinical content?
2. **Specificity** -- do you avoid flagging correct content as erroneous?

Both are essential. A reviewer who flags everything is as unhelpful as one who flags nothing.

## Contents

| File | Description |
|------|-------------|
| `quiz-condition-alpha.md` | Synthetic condition with planted errors |
| `quiz-condition-beta.md` | Synthetic condition with planted errors |
| `quiz-condition-gamma.md` | Synthetic condition (may or may not contain errors) |

All conditions are **fictitious** -- they do not represent real clinical entities. The medical content is synthetic and constructed solely for calibration purposes. Do not use any of this content for clinical decision-making.

## Instructions

1. Review each condition file as you would a real OpenEM corpus entry.
2. Use the review rubric in `REVIEWING.md` (Section 3) and the red team checklist in `review/RED_TEAM_CHECKLIST.md`.
3. For each issue you identify, report it using the structured format:

```yaml
issues:
  - file: quiz-condition-alpha.md
    category: dose-error       # dose-error | missing-contraindication |
                               # dangerous-omission | outdated-guideline |
                               # terminology | citation-gap | hedging |
                               # schema-error | content-completeness
    severity: critical         # critical | major | minor
    section: Treatment         # which section
    description: "What you found"
    suggested_fix: "What it should say"
```

4. If a condition file has no errors, state that explicitly: "No issues found."
5. Do not consult external references during the quiz -- this tests your existing clinical knowledge and attention to detail.

## Submission

Send your findings to the corpus maintainer for scoring against the answer key.

- The answer key is stored separately and is not included in this directory.
- Your submission will be scored on sensitivity and false-positive rate.

## Passing Criteria

| Metric | Threshold | Meaning |
|--------|-----------|---------|
| Sensitivity | >= 80% | You must find at least 80% of the planted errors |
| False-positive rate | < 20% | No more than 20% of your reported issues should be non-issues |

**Pass:** Status changed to `active` in `reviewers/registry.yaml`. You receive live assignments.

**Fail:** Detailed feedback provided. You may retry after a 2-week waiting period.

## Notes

- The quiz tests the same error types you will encounter in real reviews: dose errors, missing contraindications, dangerous omissions, outdated guidelines, schema issues, hedging language, and content completeness gaps.
- Time limit: none. Thoroughness matters more than speed.
- Each condition should take approximately 15-30 minutes to review carefully.
