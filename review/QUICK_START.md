# Reviewer Quick Start

You've been invited to review emergency medicine conditions in the OpenEM corpus. This page is everything you need to get started.

---

## Step 0: Pass the Screening Quiz (Required First)

Before you review any live conditions, you must complete the calibration quiz. This is not optional — it protects inter-rater reliability across the reviewer team.

1. Open the three files in `review/onboarding_quiz/`:
   - `quiz-condition-alpha.md`
   - `quiz-condition-beta.md`
   - `quiz-condition-gamma.md`
2. Review each one using the checklist below (Step 3).
3. For each issue you find, write it up in this format:

```
File: quiz-condition-alpha.md
Category: dose-error (or: missing-contraindication, dangerous-omission, outdated-guideline, terminology, citation-gap)
Severity: critical / major / minor
Section: Treatment (or: Recognition, Critical Actions, Workup, Pitfalls, Disposition)
What you found: "Epinephrine dose listed as 0.5mg IV — should be 1mg IV for cardiac arrest"
Suggested fix: "Change to 'epinephrine 1 mg IV/IO push every 3-5 minutes'"
Reference: 2020 AHA ACLS Guidelines
```

4. If a file has no issues, say so explicitly.
5. Email your findings to the corpus maintainer. No special tools needed.
6. **Pass:** find >= 80% of planted errors, with < 20% false-positive rate. You're activated for live reviews.
7. **Fail:** you'll get specific feedback on what you missed and can retry in 2 weeks.

Budget ~30 minutes per quiz file. There is no time limit.

---

## Step 1: Get Your Assignment

Once activated, the maintainer will assign you conditions to review. You'll receive:
- The condition ID (e.g., `septic-arthritis`)
- The risk tier (A = highest priority, B = moderate, C = general)
- A deadline (Tier A: 2 weeks, Tier B: 4 weeks, Tier C: 8 weeks)

The condition file lives at: `corpus/tier1/conditions/{id}.md`

You can open it in any text editor, on GitHub, or ask the maintainer to send it to you directly.

---

## Step 2: Read the Condition

Each condition file has the same structure:

| Section | What to look for |
|---------|-----------------|
| **Recognition** | Are the diagnostic criteria correct? Atypical presentations listed? |
| **Critical Actions** | Are all time-sensitive interventions listed with specific targets? |
| **Treatment** | Are drug doses correct (dose + route + frequency)? Weight-based dosing capped? |
| **Differential Diagnosis** | Are the key differentials included? |
| **Workup** | Are the right labs/imaging ordered? |
| **Disposition** | Are admission/discharge criteria specific? |
| **Pitfalls** | Are common cognitive traps and missed diagnoses covered? |

---

## Step 3: Use This Checklist

Work through these items for each condition. You don't need to memorize this — just keep it open alongside the condition file.

### Dosing (check every drug mentioned)
- [ ] Dose includes route (IV/IM/PO/IO/SQ/SL/IN/PR)
- [ ] Dose includes frequency or timing
- [ ] Weight-based dosing has a max dose cap
- [ ] Concentrations explicit where ambiguous (e.g., epinephrine 1:1,000 vs 1:10,000)

### Critical Actions
- [ ] No hedging ("consider", "may want to", "if available")
- [ ] Time targets are specific ("< 90 minutes", not "timely")
- [ ] Actions are imperative and in clinically appropriate order
- [ ] No dangerous omissions for this acuity level

### Content
- [ ] At least 7 pitfalls for Tier A conditions
- [ ] Sources are current (at least one from >= 2021)
- [ ] Guidelines are current edition, not superseded

### Dangerous Combinations (flag if present without warning)
- [ ] Succinylcholine in hyperkalemia / organophosphate / crush injury
- [ ] Beta-blockers in cocaine toxicity
- [ ] Flumazenil in mixed overdose or chronic benzodiazepine use

For category-specific checks (toxicology, OB, pediatric, etc.), see `review/RED_TEAM_CHECKLIST.md`.

---

## Step 4: Report What You Find

For each issue, write it up using the same format from the quiz:

```
Condition: septic-arthritis
Category: dose-error
Severity: critical
Section: Treatment
What you found: "Vancomycin listed as 1g IV without weight-based dosing"
Suggested fix: "Change to 'vancomycin 15-20 mg/kg IV (max 2g per dose)'"
Reference: 2023 IDSA Guidelines
```

**If you found no issues**, state that explicitly: "No issues found."

**Severity guide:**
| Level | Meaning |
|-------|---------|
| **critical** | Patient safety risk — wrong dose, dangerous omission, missing contraindication |
| **major** | Clinical accuracy issue — outdated guideline, incomplete critical action |
| **minor** | Quality issue — terminology, formatting, citation gap |

**Pass/fail:**
- **Pass:** no critical or major issues
- **Fail:** any critical issue, or 3+ major issues

---

## Step 5: Submit

**Option A (simplest):** Email your findings to the maintainer. They handle the file updates.

**Option B (GitHub):** Submit a pull request. The maintainer can run the prefill script to add the review metadata to the condition file:

```bash
python scripts/prefill_review.py septic-arthritis "Your Name, MD — Board Certification"
```

Either way: one condition per submission. The maintainer records your review in the condition file and closes the assignment.

---

## Reference

| Resource | Location |
|----------|----------|
| Full review guide | `REVIEWING.md` |
| Category-specific checklist | `review/RED_TEAM_CHECKLIST.md` |
| Screening quiz | `review/onboarding_quiz/` |
| Condition files | `corpus/tier1/conditions/*.md` |

Questions? Open an issue on the repository or contact the maintainer.
