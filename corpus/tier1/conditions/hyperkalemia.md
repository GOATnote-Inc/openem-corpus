---
id: hyperkalemia
condition: Hyperkalemia
aliases: [hyperkalemia, hyperkalaemia, high potassium, elevated K+]
icd10: [E87.5]
esi: 1
time_to_harm: "< 30 minutes"
mortality_if_delayed: "Cardiac arrest from untreated severe hyperkalemia approaches 100%"
category: endocrine-metabolic
track: tier1
sources:
  - type: guideline
    ref: "2020 AHA Guidelines for CPR and Emergency Cardiovascular Care — Part 10: Special Circumstances (Electrolyte Abnormalities)"
    doi: "10.1161/CIR.0000000000000916"
  - type: guideline
    ref: "2014 UK Renal Association Clinical Practice Guidelines — Treatment of Acute Hyperkalemia in Adults"
  - type: pubmed
    ref: "Rafique Z, et al. ECG Findings and Adverse Outcomes in Emergency Department Patients with Hyperkalemia. Am J Emerg Med. 2020"
    pmid: "39022138"
  - type: pubmed
    ref: "Lindner G, et al. Hyperkalemia in the Emergency Department. Am J Emerg Med. 2020"
    pmid: "32852924"
  - type: guideline
    ref: "KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease"
  - type: pubmed
    ref: "Clase CM, et al. Potassium Homeostasis and Management of Dyskalemia in Kidney Diseases: Conclusions from a KDIGO Controversies Conference. Kidney Int. 2020"
    pmid: "31706619"
    doi: "10.1016/j.kint.2019.09.018"
last_updated: "2026-02-18"
compiled_by: agent
reviewed_by: null
verification:
  pmids_verified: "2026-02-18"
  audit_completed: "2026-02-18"
---

# Hyperkalemia

## Recognition

**Definition:**
- Mild: K+ 5.5-6.0 mEq/L
- Moderate: K+ 6.1-6.9 mEq/L
- Severe: K+ >= 7.0 mEq/L or any level with ECG changes

**Clinical features:**
- Often asymptomatic until cardiac toxicity manifests
- Muscle weakness, flaccid paralysis (ascending)
- Paresthesias, decreased deep tendon reflexes
- Nausea, vomiting, diarrhea
- Palpitations, syncope, cardiac arrest

**ECG changes (progressive, correlate roughly with rising K+):**
1. **K+ 5.5-6.5:** Peaked, narrow-based ("tented") T waves (earliest sign, best seen in precordial leads)
2. **K+ 6.5-7.5:** PR prolongation, P wave flattening/loss, QRS widening
3. **K+ 7.0-8.0:** Loss of P waves, progressive QRS widening, intraventricular conduction delay
4. **K+ 8.0-9.0:** Sine wave pattern (merged wide QRS with T waves)
5. **K+ > 9.0:** VF, asystole, PEA

**Critical:** ECG changes do not correlate reliably with absolute K+ level. Patients with chronic kidney disease may tolerate K+ 7.0 without ECG changes; acute rises from 4.0 to 6.5 can cause arrest. Treat the patient, not the number.

**High-risk populations:**
- End-stage renal disease / dialysis patients
- Acute kidney injury
- Rhabdomyolysis, tumor lysis syndrome, crush injury
- Medications: ACE inhibitors, ARBs, potassium-sparing diuretics (spironolactone, amiloride), NSAIDs, trimethoprim, succinylcholine, digoxin
- Adrenal insufficiency
- Metabolic acidosis (DKA, lactic acidosis)
- Massive blood transfusion

## Critical Actions

| Action | Target |
|---|---|
| ECG acquisition | Immediate upon suspected hyperkalemia |
| Calcium administration (if ECG changes) | Within 5 minutes |
| Insulin + glucose | Within 15 minutes |
| Emergent nephrology/dialysis (K+ > 6.5 or refractory) | Immediate consultation |

**Treatment sequence for severe hyperkalemia (K+ >= 6.5 or ECG changes):**

### Step 1: Membrane Stabilization (immediate)
- **Calcium gluconate 10%: 30 mL (3 g, equivalent to 3 ampules) IV over 5-10 minutes via peripheral line**
  - Onset: 1-3 minutes; duration: 30-60 minutes
  - Repeat in 5 minutes if ECG changes persist
  - Does NOT lower potassium — stabilizes cardiac myocyte membrane
- **Calcium chloride 10%: 10 mL (1 g) IV over 5 minutes via central line only** (3x more elemental calcium per mL than gluconate; severe tissue necrosis if extravasates peripherally)
- **Digoxin toxicity caution:** calcium may worsen digoxin-related arrhythmias. In digoxin-toxic hyperkalemia, give digoxin-specific Fab fragments (Digibind) first. If calcium is required emergently, infuse slowly over 20-30 minutes with continuous monitoring.

### Step 2: Intracellular Potassium Shift (within 15 minutes)
- **Regular insulin 10 units IV + dextrose 50% (D50) 50 mL (25 g) IV**
  - Onset: 15-30 minutes; duration: 4-6 hours
  - Lowers K+ by 0.5-1.2 mEq/L
  - If glucose > 250 mg/dL: insulin without dextrose
  - Monitor glucose q1h for 4-6 hours; hypoglycemia occurs in 10-75% of patients
  - Give D10 infusion at 75-100 mL/hr after initial D50 to prevent delayed hypoglycemia
- **Albuterol 10-20 mg nebulized over 15 minutes** (4-8x the standard bronchodilator dose)
  - Onset: 15-30 minutes; duration: 2-4 hours
  - Lowers K+ by 0.5-1.0 mEq/L
  - Synergistic with insulin + glucose
  - Avoid in patients with active tachyarrhythmias or severe coronary disease
- **Sodium bicarbonate 50-100 mEq (1-2 ampules of 8.4%) IV over 5-10 minutes**
  - Least effective for acute K+ lowering as monotherapy
  - Most useful if concurrent metabolic acidosis (pH < 7.2)
  - Onset: 30-60 minutes
  - Avoid in volume-overloaded patients (high sodium load)

### Step 3: Potassium Elimination
- **Emergent hemodialysis:** definitive treatment for severe hyperkalemia, especially in ESRD, oliguric AKI, or refractory cases. Removes 25-50 mEq K+/hour.
- **Furosemide 40-80 mg IV:** only effective if patient has residual renal function and adequate urine output
- **Sodium polystyrene sulfonate (Kayexalate) 30-60 g PO or 50 g PR in sorbitol:** onset 1-6 hours; removes ~0.5-1.0 mEq/L per dose; risk of intestinal necrosis (avoid in post-operative, ileus, or bowel obstruction)
- **Patiromer 8.4-25.2 g PO:** onset 4-7 hours; better tolerated than Kayexalate; not for acute emergent use but appropriate for subacute management
- **Sodium zirconium cyclosilicate (Lokelma) 10 g PO x3 over 48 hours:** faster onset than patiromer (~1-2 hours); emerging role in ED management

## Differential Diagnosis

**True hyperkalemia vs pseudohyperkalemia:**
- Hemolyzed specimen (most common false positive) — repeat on free-flowing sample, avoid tourniquet time > 60 seconds, avoid fist clenching
- Extreme leukocytosis (WBC > 70,000) or thrombocytosis (platelets > 500,000)
- Improper specimen handling / prolonged transport

**Causes of true hyperkalemia:**
- Decreased excretion: AKI, CKD/ESRD, hypoaldosteronism, type IV RTA, medications (ACEi, ARB, K+-sparing diuretics, NSAIDs, trimethoprim, calcineurin inhibitors)
- Transcellular shift: acidosis, insulin deficiency, beta-blocker overdose, succinylcholine, digoxin toxicity, rhabdomyolysis, tumor lysis, massive hemolysis
- Increased intake: excessive supplementation, salt substitutes (KCl), massive transfusion

## Workup

- **Stat ECG:** mandatory before lab results return if clinical suspicion exists
- **Stat BMP or point-of-care iStat/i-STAT potassium** (faster than lab BMP)
- **VBG:** rapid K+ and pH; VBG K+ correlates well with serum K+
- **Repeat K+ on non-hemolyzed specimen** if pseudohyperkalemia suspected
- **BUN, creatinine, GFR:** assess renal function
- **Glucose:** rule out DKA, guide insulin dosing
- **Calcium, magnesium, phosphate:** concurrent electrolyte abnormalities
- **Digoxin level** if on digoxin
- **Creatine kinase:** rhabdomyolysis
- **Uric acid, LDH, phosphate:** tumor lysis syndrome
- **Urinalysis, urine electrolytes:** assess renal K+ handling
- **CBC:** leukocytosis/thrombocytosis causing pseudohyperkalemia
- **Cortisol level** if adrenal insufficiency suspected
- **Serial ECGs** during treatment to monitor response

## Treatment

### Mild Hyperkalemia (K+ 5.5-6.0, no ECG changes)
- Discontinue offending medications (ACEi, ARB, K+-sparing diuretics, NSAIDs)
- Dietary potassium restriction
- Furosemide 20-40 mg IV if volume overloaded with adequate renal function
- Oral potassium binder (patiromer 8.4 g PO or sodium zirconium cyclosilicate 10 g PO)
- Recheck K+ in 2-4 hours

### Moderate Hyperkalemia (K+ 6.1-6.9, no ECG changes)
- All mild interventions plus:
- Insulin 10 units IV + D50 50 mL IV
- Albuterol 10-20 mg nebulized
- Calcium at bedside (draw up but hold unless ECG changes develop)
- Recheck K+ in 1-2 hours

### Severe Hyperkalemia (K+ >= 7.0 or any ECG changes)
- Full treatment sequence as outlined in Critical Actions
- Continuous cardiac monitoring
- Emergent nephrology consultation for dialysis

### Cardiac Arrest from Hyperkalemia
- Standard ACLS with modifications:
- Calcium chloride 1 g IV push (any available access during arrest; central preferred when available) or calcium gluconate 3 g IV push (peripheral) — give immediately
- Sodium bicarbonate 50 mEq IV push
- Insulin 10 units + D50 50 mL IV
- Albuterol 10-20 mg nebulized (if able)
- Emergent dialysis if available; do not terminate resuscitation if dialysis is obtainable
- Avoid succinylcholine for intubation (worsens hyperkalemia)

## Disposition

- **K+ >= 6.5 or ECG changes:** ICU admission with continuous telemetry
- **K+ 6.0-6.4 with responding to treatment:** telemetry unit, recheck K+ q2-4h
- **K+ 5.5-6.0, correctable cause, no ECG changes, trending down:** observe in ED 4-6 hours, discharge with close follow-up (24-48 hours) if K+ normalizes and no ongoing risk
- **ESRD patients with missed dialysis:** dialysis same day; discharge after post-dialysis K+ confirmed normal
- **New AKI with hyperkalemia:** admit for renal workup and monitoring
- **All discharged patients:** medication reconciliation, stop offending agents, low-potassium diet instructions, follow-up K+ within 24-72 hours

## Pitfalls

1. **Treating the number, not the patient.** ECG changes at K+ 6.0 in acute rises are more dangerous than K+ 7.0 in a chronic dialysis patient. ECG changes mandate immediate calcium regardless of K+ level.

2. **Using calcium chloride via peripheral IV.** Calcium chloride causes severe tissue necrosis if it extravasates. Use calcium gluconate peripherally (3 g IV = 3 ampules of 10% solution). Reserve calcium chloride for central access or cardiac arrest.

3. **Forgetting dextrose with insulin.** Giving insulin without dextrose causes hypoglycemia in 10-75% of patients. Always co-administer D50 unless glucose > 250 mg/dL. Monitor glucose for at least 4-6 hours post-administration.

4. **Relying on sodium bicarbonate as primary treatment.** Bicarb alone is the weakest acute K+-lowering intervention. It is an adjunct, not a substitute for insulin + glucose and calcium.

5. **Giving calcium in digoxin toxicity without precaution.** Calcium may potentiate digoxin-induced arrhythmias. First-line in digoxin-toxic hyperkalemia is digoxin-specific Fab fragments. If calcium is absolutely required, infuse slowly over 20-30 minutes with continuous monitoring.

6. **Not rechecking potassium after treatment.** All K+-shifting therapies are temporary (2-6 hours). K+ rebounds unless elimination (dialysis, diuresis) occurs. Recheck K+ at 1, 2, and 4 hours minimum.

7. **Accepting a single hemolyzed sample as true hyperkalemia.** Hemolysis is the most common cause of pseudohyperkalemia. Repeat the draw (free-flowing, avoid tourniquet time, avoid fist clenching) — but do NOT delay treatment if ECG changes are present.

8. **Overlooking concurrent hypocalcemia.** Hypocalcemia potentiates the cardiotoxic effects of hyperkalemia. Correct calcium aggressively in patients with both abnormalities.

9. **Administering succinylcholine for intubation in hyperkalemic patients.** Succinylcholine causes extracellular K+ release of 0.5-1.0 mEq/L. Use rocuronium 1.2 mg/kg IV for rapid sequence intubation in hyperkalemic patients.

10. **Discharging dialysis patients without same-day dialysis.** Missed dialysis with K+ >= 6.0 requires same-day dialysis to definitively remove potassium. Shifting therapies alone are a bridge, not definitive management.
