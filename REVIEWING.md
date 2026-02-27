# Physician Review Guide

Structured workflow for clinical review of OpenEM conditions, modeled on expert annotation best practices.

---

## 1. Reviewer Qualifications

**Required credentials:**
- Board-certified physician (MD/DO) in emergency medicine, internal medicine, or relevant subspecialty
- Active medical license (US or equivalent)
- Category-matched expertise preferred (e.g., toxicologist for toxicologic conditions)

**How to register:**
1. Fork the repository
2. Add your profile to `reviewers/registry.yaml` with `status: pending_verification`
3. Submit a PR with credentials documentation
4. Pass the onboarding screening quiz (see Section 7)
5. Maintainer verifies credentials and updates status to `active`

---

## 2. Review Types

| Type | Scope | When Used |
|------|-------|-----------|
| **full** | All sections: Recognition, Critical Actions, Treatment, Pitfalls, DDx, Workup, Disposition | Initial review of tier A conditions |
| **dosing-focused** | Drug doses, routes, frequencies, weight-based calculations, max doses | After automated dose audit flags |
| **red-team** | Adversarial review: dangerous omissions, incorrect context, outdated protocols | After `scripts/red_team_review.py` flags |
| **spot-check** | Targeted review of specific sections flagged by automated checks | Maintenance / post-update |
| **consensus** | Adjudication review when two prior reviewers disagree | Disagreement resolution (tier A only) |

---

## 3. Review Rubric

### Recognition (5 items)
- [ ] Diagnostic criteria are correct and complete
- [ ] Atypical presentations are listed
- [ ] Key exam findings match current evidence
- [ ] High-risk populations identified
- [ ] Scoring systems (if any) are current version

### Critical Actions (7 items)
- [ ] All time-sensitive interventions listed
- [ ] Time targets are specific and current (e.g., "< 90 minutes" not "timely")
- [ ] Actions are imperative — no hedging ("consider", "may want to")
- [ ] Order of actions is clinically appropriate
- [ ] All drug doses include route and frequency
- [ ] Concentration specified where ambiguous (epinephrine 1:1,000 vs 1:10,000)
- [ ] No dangerous omissions for this acuity level

### Treatment (8 items)
- [ ] Drug doses are correct (dose, route, frequency)
- [ ] Weight-based dosing includes max dose cap
- [ ] Contraindications listed for high-risk medications
- [ ] Drug-drug interactions noted where relevant
- [ ] Infusion rates specified for drips
- [ ] Second-line agents listed
- [ ] Procedural interventions described with indications
- [ ] Disposition criteria are specific

### Pitfalls (4 items)
- [ ] At least 7 pitfalls for tier A conditions
- [ ] Cognitive traps are clinically realistic
- [ ] Atypical presentations that cause missed diagnoses included
- [ ] Common management errors addressed

### Pass/Fail Criteria
- **Pass:** No critical or major issues found; minor issues documented
- **Fail:** Any critical issue (patient safety), or 3+ major issues (clinical accuracy)
- A failed review generates a GitHub issue and blocks condition sign-off until fixed

---

## 4. Issue Reporting

Report issues using this structured format in your PR description:

```yaml
issues:
  - category: dose-error          # dose-error | missing-contraindication |
                                   # dangerous-omission | outdated-guideline |
                                   # terminology | citation-gap
    severity: critical             # critical | major | minor
    section: Treatment             # which section
    description: "Epinephrine dose listed as 0.5mg IV — should be 1mg IV for cardiac arrest"
    suggested_fix: "Change to 'epinephrine 1 mg IV/IO push every 3-5 minutes'"
    reference: "2020 AHA ACLS Guidelines"
```

**Issue categories:**
| Category | Description | Typical Severity |
|----------|-------------|-----------------|
| `dose-error` | Wrong dose, route, or frequency | critical |
| `missing-contraindication` | Drug used without noting contraindication | critical / major |
| `dangerous-omission` | Critical action or warning missing | critical |
| `outdated-guideline` | Guideline superseded by newer evidence | major |
| `terminology` | Incorrect or ambiguous medical terminology | minor |
| `citation-gap` | Claim without supporting source | minor |

---

## 5. Claiming and Submitting

1. **Check availability:** Run `python scripts/review_dashboard.py` to see unclaimed conditions
2. **Claim:** Add yourself to `reviewers/assignments.yaml` for the condition
3. **Review:** Follow the rubric (Section 3). Run `python scripts/red_team_review.py` for automated pre-check
4. **Record:** Add a `reviews` entry to the condition's frontmatter:
   ```yaml
   reviews:
     - reviewer: "Your Name, MD — Board Certification"
       date: "YYYY-MM-DD"
       type: full
       issues_found: 0
       issues_ref: ""
   ```
5. **Submit PR:** One condition per PR. Include structured issue report (Section 4) if issues found
6. **Update assignment:** Set status to `complete` in `reviewers/assignments.yaml`

Minor fixes (typos, formatting) can be made directly in the PR. Content changes require maintainer review.

---

## 6. Consensus Requirements

| Risk Tier | Reviews Required | Disagreement Resolution |
|-----------|-----------------|------------------------|
| **A** (ESI 1) | 2 independent reviews | Escalate to corpus maintainer for adjudication |
| **B** (ESI 2) | 1 review | Author review sufficient |
| **C** (ESI 3+) | 1 review | Author review sufficient |

**Disagreement protocol:**
1. If reviewers disagree on severity of an issue, the higher severity stands
2. If reviewers disagree on clinical accuracy, a third reviewer with subspecialty expertise adjudicates
3. Adjudication decisions are recorded in a `consensus` review entry

---

## 7. Onboarding Screening Quiz

Before receiving live assignments, new reviewers must pass a screening quiz.

**Format:**
- 3-5 synthetic condition files with planted errors
- Errors span: dose errors, missing contraindications, dangerous omissions, outdated guidelines, wrong ICD-10 codes
- Reviewer must identify ≥ 80% of planted errors
- False-positive rate on clean sections must be < 20%

**Location:** `review/onboarding_quiz/`

**Process:**
1. Review the synthetic conditions as you would real ones
2. Submit your findings to the maintainer
3. Maintainer scores against the answer key
4. Pass → status changed to `active` in registry
5. Fail → feedback provided, can retry after 2 weeks

---

## 8. Gold Standard Seeding

Gold standard conditions are seeded into the live review queue at ~8% rate, indistinguishable from real assignments. They calibrate reviewer accuracy over time.

**Distribution:**
| Type | Proportion | Purpose |
|------|-----------|---------|
| Clean | 40% | Tests false-positive rate — correct answer is "no issues" |
| Boundary | 30% | Tests calibration — clinical judgment varies |
| Genuine issues | 20% | Tests sensitivity — real flaggable problems |
| Confusion pairs | 10% | Tests domain knowledge — similar presentations |

**Passing threshold:**
- ≥ 80% sensitivity (find genuine issues)
- < 20% false-positive rate (don't flag clean conditions)

**Tracking:**
- Krippendorff's alpha computed per batch and cumulatively
- Alpha < 0.67 → rubric clarification issued
- Alpha < 0.50 → reviewer retraining required

---

## 9. SLAs

| Risk Tier | Review Deadline | Escalation |
|-----------|----------------|------------|
| **A** | 2 weeks from assignment | Maintainer reassigns after 2 weeks |
| **B** | 4 weeks from assignment | Reminder at 3 weeks |
| **C** | 8 weeks from assignment | Reminder at 6 weeks |

Run `python scripts/review_dashboard.py` to see SLA compliance.

---

## 10. Agreement Tracking

Inter-reviewer agreement is measured using **Krippendorff's alpha** across all gold standard and multi-reviewer conditions.

| Alpha Range | Interpretation | Action |
|-------------|---------------|--------|
| ≥ 0.80 | Strong agreement | No action needed |
| 0.67–0.80 | Acceptable agreement | Monitor trends |
| 0.50–0.67 | Weak agreement | Issue rubric clarification |
| < 0.50 | Poor agreement | Pause assignments, retrain reviewers |

Alpha is reported per batch and cumulatively by `scripts/review_dashboard.py`.

---

## Current Review Status

All 80 risk_tier A (ESI 1) conditions have been reviewed by the corpus author (board-certified emergency medicine physician). The remaining 105 conditions across risk tiers B and C need review.

Run `python scripts/review_status.py` to see detailed status by tier.

Run `python scripts/review_dashboard.py` for full dashboard with SLA tracking.

---

## Questions?

Open an issue on the repository or contact the maintainers.
