---
id: diabetic-ketoacidosis
condition: Diabetic Ketoacidosis
aliases: [DKA, diabetic ketosis, ketoacidosis]
icd10: [E10.10, E10.11, E11.10, E11.11, E13.10, E13.11]
esi: 1
time_to_harm: "< 6 hours"
mortality_if_delayed: "2-5% overall, 20-30% with cerebral edema"
category: endocrine-metabolic
track: tier1
sources:
  - type: guideline
    ref: "2024 ADA Standards of Care in Diabetes — Chapter 16: Diabetes Care in the Hospital"
  - type: guideline
    ref: "2023 ISPAD Clinical Practice Consensus Guidelines: DKA and Hyperglycemic Hyperosmolar State"
  - type: guideline
    ref: "2009 ADA Consensus Statement: Hyperglycemic Crises in Adult Patients with Diabetes"
  - type: review
    ref: "Kitabchi AE et al. Hyperglycemic Crises in Adult Patients With Diabetes. Diabetes Care 2009"
    pmid: "19564476"
  - type: review
    ref: "Long B, Koyfman A. Emergency Medicine Myths: DKA. J Emerg Med 2017"
    pmid: "28412071"
last_updated: "2026-02-18"
compiled_by: agent
reviewed_by: null
verification:
  pmids_verified: "2026-02-18"
  audit_completed: "2026-02-18"
---

# Diabetic Ketoacidosis

## Recognition

**Diagnostic Criteria (all three required):**
1. Hyperglycemia: glucose > 250 mg/dL (may be lower in euglycemic DKA)
2. Metabolic acidosis: pH < 7.3 or bicarb < 18 mEq/L
3. Ketosis: serum or urine ketones positive, or beta-hydroxybutyrate > 3 mmol/L

**Severity Classification:**

| Severity | pH | Bicarb | Mental Status |
|----------|----|--------|---------------|
| Mild | 7.25-7.30 | 15-18 | Alert |
| Moderate | 7.00-7.24 | 10-14 | Drowsy |
| Severe | < 7.00 | < 10 | Obtunded/coma |

**Presentation:**
- Polyuria, polydipsia, weight loss (days to weeks)
- Nausea, vomiting, abdominal pain (can mimic acute abdomen)
- Kussmaul respirations (deep, rapid — compensatory for metabolic acidosis)
- Fruity breath (acetone)
- Tachycardia, hypotension (volume depletion averages 5-7 L in adults)
- Altered mental status (correlates with osmolality more than pH)
- Hypothermia (common; infection may not produce fever)

**Precipitants (5 I's):**
- **I**nfection (most common — UTI, pneumonia, sepsis)
- **I**nsulin omission/noncompliance
- **I**nfarction (MI, stroke, mesenteric ischemia)
- **I**ntoxication/drugs (cocaine, SGLT2 inhibitors, steroids)
- **I**nitial presentation of new-onset diabetes

**Euglycemic DKA (glucose < 250 mg/dL):**
- SGLT2 inhibitor use (empagliflozin, dapagliflozin, canagliflozin)
- Pregnancy
- Starvation + diabetes
- Partial treatment prior to arrival
- Missed if glucose is used as sole screening criterion

## Critical Actions

1. **Volume resuscitation** — NS 1-1.5 L/hr for first 1-2 hours (15-20 mL/kg/hr). Average deficit is 5-7 L. Switch to 0.45% NS at 250-500 mL/hr when corrected Na normalizes.
2. **Insulin infusion** — Regular insulin 0.1-0.14 units/kg/hr IV continuous. If bolus protocol: 0.1 units/kg IV bolus then 0.1 units/kg/hr. Do NOT give insulin until K > 3.3 mEq/L.
3. **Potassium replacement** — Check K before insulin. If K < 3.3: hold insulin, give 20-40 mEq/hr KCl until K > 3.3. If K 3.3-5.3: give 20-30 mEq K per liter of IV fluids. If K > 5.3: recheck in 2 hours.
4. **Monitor q1-2h** — glucose, BMP (K, bicarb, anion gap), VBG. Glucose should drop 50-75 mg/dL/hr.
5. **Dextrose when glucose reaches 200-250 mg/dL** — Switch to D5 0.45% NS. Continue insulin to close anion gap (do not stop insulin just because glucose normalized).
6. **Search for precipitant** — UA, CXR, blood cultures, ECG, lipase, pregnancy test.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Hyperosmolar hyperglycemic state (HHS) | Glucose > 600, osmolality > 320, minimal ketosis, pH > 7.30, profound dehydration |
| Alcoholic ketoacidosis | History of alcohol use, low-normal glucose, elevated beta-hydroxybutyrate, anion gap acidosis |
| Starvation ketosis | Mild ketosis, bicarb rarely < 18, no significant acidosis |
| Uremic acidosis | Elevated BUN/Cr, anion gap acidosis, no ketosis |
| Lactic acidosis | Elevated lactate, sepsis/shock/liver failure, no ketosis |
| Toxic alcohol ingestion | Osmolar gap, specific toxin levels, no ketosis |
| Salicylate toxicity | Mixed respiratory alkalosis + metabolic acidosis, tinnitus, salicylate level |

## Workup

**Point-of-Care:**
- Glucose (fingerstick)
- VBG (pH, pCO2) — VBG pH correlates within 0.03 of ABG pH
- POC lactate
- Urinalysis (ketones, infection)
- Beta-hydroxybutyrate (preferred over urine ketones)
- ECG (peaked T waves for hyperkalemia, ischemia as precipitant)

**Labs:**
- BMP (glucose, Na, K, Cl, bicarb, BUN, Cr)
- Anion gap = Na - (Cl + HCO3). Expected: > 12 in DKA
- Corrected Na = measured Na + 1.6 x [(glucose - 100) / 100]
- Serum osmolality (calculated: 2Na + glucose/18 + BUN/2.8)
- CBC with diff (leukocytosis common in DKA even without infection — WBC > 25,000 more suggestive of infection)
- Phosphate, magnesium (deplete during treatment)
- Lipase (if abdominal pain — but DKA itself causes elevated lipase in up to 15%)
- HbA1c (new diagnosis vs. noncompliance)
- Blood cultures (if infectious precipitant suspected)
- Pregnancy test (reproductive-age females)

**Imaging:**
- CXR (pneumonia as precipitant)
- CT head (if AMS out of proportion to metabolic derangement)

## Treatment

**Phase 1: Resuscitation (0-2 hours)**
- NS 1-1.5 L/hr (15-20 mL/kg/hr)
- Correct K before starting insulin (see Critical Actions)
- Regular insulin 0.1-0.14 units/kg/hr IV (do not bolus if using 0.14 units/kg/hr rate)
- Hold insulin if K < 3.3 mEq/L

**Phase 2: Continued Management (2-12+ hours)**
- Reduce fluids to 250-500 mL/hr of 0.45% NS (if corrected Na normal or elevated) or continue NS (if corrected Na low)
- When glucose 200-250 mg/dL: switch to D5 0.45% NS AND reduce insulin to 0.02-0.05 units/kg/hr
- Continue insulin infusion until anion gap closes (< 12) AND patient is eating
- K replacement ongoing in IV fluids (target 4-5 mEq/L)

**Bicarbonate:**
- Only if pH < 6.9: 100 mEq NaHCO3 in 400 mL sterile water + 20 mEq KCl, infuse at 200 mL/hr. Recheck VBG in 2 hours.
- pH > 6.9: bicarbonate not indicated (causes paradoxical CNS acidosis, worsens hypokalemia, shifts oxyhemoglobin curve left)

**Phosphate:**
- Replace if < 1.0 mg/dL or symptomatic (weakness, respiratory failure, rhabdomyolysis)
- K-Phos 20-30 mmol IV over 6 hours (replaces K and PO4 simultaneously)
- Excessive phosphate replacement causes hypocalcemia

**Transition to Subcutaneous Insulin:**
- Give SC insulin 1-2 hours BEFORE stopping IV infusion (overlap required to prevent rebound hyperglycemia/ketosis)
- Basal-bolus: 0.5-0.8 units/kg/day divided as 50% basal (glargine/detemir) + 50% bolus (lispro/aspart)
- For new-onset T1DM: start at 0.5 units/kg/day
- Do not transition until: AG closed, pH > 7.30, bicarb > 18, patient tolerating PO

## Disposition

**ICU Admission:**
- Severe DKA (pH < 7.0, bicarb < 10, obtunded)
- Hemodynamic instability
- K < 3.3 at presentation
- Significant comorbidities (ACS, sepsis)
- Requiring bicarb infusion

**Stepdown/Floor:**
- Mild-moderate DKA responding to treatment
- Stable hemodynamics
- Improving mental status
- Reliable IV access and monitoring

**Pediatric DKA:**
- Fluid resuscitation more conservative: 10-20 mL/kg NS bolus, then 1.5-2x maintenance
- Insulin 0.05-0.1 units/kg/hr (no bolus)
- Cerebral edema risk: headache, bradycardia, altered consciousness, Cushing triad
- If cerebral edema suspected: mannitol 0.5-1 g/kg IV over 20 min OR hypertonic saline 3% 2.5-5 mL/kg over 10-15 min. Elevate head of bed. Reduce fluid rate.

## Pitfalls

1. **Starting insulin before checking potassium.** Insulin drives K intracellularly. If K < 3.3 mEq/L, insulin causes life-threatening hypokalemia and cardiac arrest. Replace K first, then start insulin.

2. **Stopping insulin when glucose normalizes.** DKA resolution is defined by anion gap closure (< 12), NOT glucose normalization. Glucose normalizes hours before the anion gap closes. Stopping insulin prematurely causes rebound ketoacidosis. Add dextrose to fluids and continue insulin.

3. **Missing euglycemic DKA.** SGLT2 inhibitors cause DKA with normal or near-normal glucose. If a patient on empagliflozin/dapagliflozin/canagliflozin presents with acidosis and ketosis, it is DKA regardless of glucose level.

4. **Aggressive bicarbonate use.** Bicarbonate worsens intracellular and CNS acidosis (CO2 crosses the blood-brain barrier, HCO3 does not). Reserve for pH < 6.9 only. It also causes hypokalemia and shifts the oxyhemoglobin dissociation curve left (impaired oxygen delivery).

5. **Ignoring the precipitant.** DKA is a symptom, not a final diagnosis. Failure to identify the trigger (MI, sepsis, noncompliance, new diagnosis) leads to recurrence and missed life-threatening conditions.

6. **Using urine ketones to monitor resolution.** Urine ketones detect acetoacetate, not beta-hydroxybutyrate (the predominant ketone in DKA). As DKA resolves, beta-hydroxybutyrate converts to acetoacetate, making urine ketones paradoxically increase. Use serum beta-hydroxybutyrate or anion gap to track resolution.

7. **Overly aggressive fluid resuscitation in pediatric patients.** Rapid fluid administration in children with DKA increases the risk of cerebral edema. Use 10-20 mL/kg bolus (not 1 L/hr adult protocols) and rehydrate over 24-48 hours.
