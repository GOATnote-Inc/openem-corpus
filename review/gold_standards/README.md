# Gold Standard Calibration System

## Purpose

Gold standard conditions are seeded into the live review queue at approximately 8% rate. Reviewers do not know which assignments are gold standards and which are real review tasks. This ongoing calibration measures reviewer accuracy after onboarding and detects drift over time.

## Distribution

Gold standards follow a 40/30/20/10 distribution across four types:

| Type | Proportion | Description | Expected Reviewer Action |
|------|-----------|-------------|--------------------------|
| **Clean** | 40% | Verified correct condition -- no issues | Report "no issues found" |
| **Boundary** | 30% | Clinically debatable content where reasonable experts may disagree | May or may not flag -- used for calibration, not pass/fail |
| **Genuine issue** | 20% | Condition with a real, verifiable problem planted or identified | Must flag the issue with correct category and severity |
| **Confusion pair** | 10% | Condition with content that tests domain-specific knowledge (e.g., similar drug names, overlapping presentations) | Must correctly distinguish the conditions |

## How Gold Standards Are Created

1. **Source material:** Real corpus conditions that have been independently verified by 2 or more physicians.
2. **Clean type:** The verified condition is assigned as-is. The expected finding is "no issues."
3. **Boundary type:** A condition with a clinically debatable element (e.g., a dose at the upper end of the accepted range, a guideline that has been updated but the prior version is not strictly wrong). Created by the corpus maintainer with documented rationale.
4. **Genuine issue type:** A verified condition with a single planted error (dose error, missing contraindication, outdated guideline, etc.). The error is documented in `manifest.yaml` but not in the condition file itself.
5. **Confusion pair type:** A condition where the differential diagnosis includes a closely related entity that requires specific domain knowledge to distinguish (e.g., serotonin syndrome vs NMS, STEMI vs Wellens pattern).

## Tracking

### Inter-Rater Agreement

Reviewer performance on gold standards is tracked using **Krippendorff's alpha**, computed per batch and cumulatively.

| Alpha Range | Interpretation | Action |
|-------------|---------------|--------|
| >= 0.80 | Strong agreement | No action needed |
| 0.67 -- 0.80 | Acceptable agreement | Monitor trends |
| 0.50 -- 0.67 | Weak agreement | Issue rubric clarification to all reviewers |
| < 0.50 | Poor agreement | Pause new assignments; mandatory retraining |

### Per-Reviewer Metrics

Each reviewer accumulates a gold standard performance record:

- **Sensitivity:** proportion of genuine-issue gold standards where the reviewer correctly identified the issue.
- **False-positive rate:** proportion of clean gold standards where the reviewer incorrectly flagged an issue.
- **Calibration score:** agreement with the expected finding on boundary cases (informational, not used for pass/fail).

### Thresholds

- Sensitivity < 0.80 on genuine-issue gold standards across 5+ assignments: reviewer receives targeted feedback.
- False-positive rate > 0.20 on clean gold standards across 5+ assignments: reviewer receives calibration guidance.
- Alpha < 0.67 across a batch: rubric clarification issued to all reviewers in that batch.
- Alpha < 0.50 across a batch: all assignments in the batch are paused and reviewers must complete a recalibration exercise.

## Operational Security

- Gold standard assignments are indistinguishable from real assignments in the review queue.
- The `manifest.yaml` file in this directory is the single source of truth for gold standard metadata. It is not shared with reviewers.
- Reviewers should not be informed which specific assignments were gold standards until after the batch is scored.
- Batch scoring reports are shared with reviewers after all reviews in the batch are complete.

## Adding New Gold Standards

1. Select a condition that has been verified by 2+ physicians (check `reviewed_by` and `review_date` in frontmatter).
2. Determine the gold standard type (clean, boundary, genuine issue, or confusion pair).
3. For genuine-issue type: plant the error in a copy of the condition (do not modify the canonical corpus file).
4. Add an entry to `manifest.yaml` with all required fields.
5. Maintain the 40/30/20/10 distribution across the full set of gold standards.

## Files

| File | Description |
|------|-------------|
| `manifest.yaml` | Registry of all gold standard conditions with expected findings |
| `README.md` | This file -- system documentation |
