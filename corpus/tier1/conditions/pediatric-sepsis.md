---
id: pediatric-sepsis
condition: Pediatric Sepsis
aliases: [pediatric severe sepsis, pediatric septic shock, neonatal sepsis, childhood sepsis]
icd10: [R65.20, R65.21, A41.9, P36.9]
esi: 1
time_to_harm:
  irreversible_injury: "< 1 hour"
  death: "< 6 hours without intervention"
  optimal_intervention_window: "< 1 hour (first fluid bolus and antibiotics)"
mortality_if_delayed: "Each hour delay in antibiotics increases mortality 3-7%"
category: pediatric
track: tier1
sources:
  - type: guideline
    ref: "Surviving Sepsis Campaign International Guidelines for the Management of Septic Shock and Sepsis-Associated Organ Dysfunction in Children, 2020"
  - type: guideline
    ref: "American College of Critical Care Medicine Clinical Practice Parameters for Hemodynamic Support of Pediatric and Neonatal Septic Shock, 2017 Update"
last_updated: "2026-03-01"
compiled_by: agent
risk_tier: A
validation:
  automated_consistency_check: null
  dose_range_validator: null
  unit_normalization_check: null
  cross_file_consistency_check: null
  citation_presence_check: null
  duplicate_content_check: null
  outlier_detection_flag: clear
  schema_version: "2.0"
  provenance_links: []
---
# Pediatric Sepsis

## Recognition

**Sepsis in children = suspected infection + signs of systemic inflammatory response with organ dysfunction**

**Early signs (do NOT wait for hypotension):**
- Tachycardia (often the earliest sign — age-adjusted)
- Tachypnea
- Altered mental status (irritability, lethargy, poor interaction)
- Delayed capillary refill > 3 seconds (cold shock) OR flash capillary refill < 1 second (warm shock)
- Mottled, cool extremities (cold shock) OR bounding pulses, warm flushed skin (warm shock)
- Decreased urine output (< 1 mL/kg/hr)
- Fever or hypothermia (hypothermia is ominous in neonates)

**Age-adjusted vital sign thresholds for tachycardia:**
- Neonate (0-28 days): HR > 180
- Infant (1-12 months): HR > 180
- Toddler (1-5 years): HR > 140
- Child (6-12 years): HR > 130
- Adolescent (13-18 years): HR > 110

**Hypotension is a LATE sign in children** (5th percentile SBP):
- Neonate: < 60 mmHg
- Infant: < 70 mmHg
- Child 1-10 years: < 70 + (2 x age in years) mmHg
- Child > 10 years: < 90 mmHg

**High-risk populations:**
- Neonates (< 28 days), especially preterm
- Immunocompromised (oncology, transplant, sickle cell, asplenic)
- Central venous catheter (line sepsis)
- Recent surgery

## Critical Actions

| Action | Target |
|---|---|
| Recognition and IV/IO access | < 5 minutes |
| First fluid bolus (20 mL/kg) | < 15 minutes |
| Blood cultures drawn | Before antibiotics |
| Empiric IV antibiotics | < 60 minutes (< 30 min if shock) |
| Reassess after each fluid bolus | Every 5-10 minutes |
| Vasopressors if fluid-refractory | < 60 minutes |

1. **IV or IO access** — do not delay for peripheral IV; place IO if two peripheral attempts fail within 5 minutes
2. **Fluid resuscitation:** NS or LR 20 mL/kg bolus over 5-10 minutes; repeat up to 40-60 mL/kg in the first hour; reassess after each bolus (hepatomegaly, rales = stop fluids)
3. **Blood cultures x 2** before antibiotics (do not delay antibiotics > 15 minutes for cultures)
4. **Empiric IV antibiotics** (see Treatment)
5. **Glucose check** — hypoglycemia is common in septic children; treat with D10W 5 mL/kg IV if < 60 mg/dL
6. **Calcium check** — ionized calcium; replace if < 1.1 mmol/L (calcium chloride 20 mg/kg IV through central line or calcium gluconate 60 mg/kg IV through peripheral line)
7. **Vasopressors** if shock persists after 40-60 mL/kg fluid

## Differential Diagnosis

- Viral illness with dehydration (no organ dysfunction, responds to fluids)
- Diabetic ketoacidosis (hyperglycemia, Kussmaul respirations, ketones)
- Myocarditis (gallop, cardiomegaly, poor response to fluids)
- Inborn errors of metabolism (neonates — acidosis, hyperammonemia)
- Toxic ingestion (history, toxidrome)
- Kawasaki disease (prolonged fever, mucocutaneous findings, conjunctivitis)
- Adrenal crisis (ambiguous genitalia in neonates, hyperpigmentation, hyponatremia/hyperkalemia)
- Anaphylaxis (urticaria, wheezing, exposure history)
- Intussusception (intermittent pain, currant jelly stool, abdominal mass)
- Non-accidental trauma (inconsistent history, bruising pattern)

## Workup

- **Blood cultures x 2** (before antibiotics)
- **CBC with differential:** leukocytosis or leukopenia, bandemia, thrombocytopenia
- **BMP:** electrolytes, glucose, BUN, creatinine
- **Lactate:** elevated > 2 mmol/L supports tissue hypoperfusion
- **VBG/ABG:** acidosis (metabolic > respiratory)
- **CRP, procalcitonin:** markers of bacterial infection (procalcitonin > 2 ng/mL supports bacterial sepsis)
- **Coagulation studies:** PT, INR, fibrinogen, D-dimer (DIC screening)
- **Urinalysis and urine culture**
- **CSF analysis** (neonates < 28 days and febrile infants < 60 days — only if stable enough for LP; do NOT delay antibiotics for LP)
- **Chest X-ray** if respiratory symptoms present
- **Point-of-care ultrasound:** IVC collapsibility (fluid responsiveness), cardiac function

## Treatment

### Empiric Antibiotics (Administer < 60 Minutes From Recognition)

**Neonates (< 28 days):**
- Ampicillin 50 mg/kg IV q8h + gentamicin 4 mg/kg IV q24h
- ADD cefotaxime 50 mg/kg IV q8h if meningitis suspected (or acyclovir 20 mg/kg IV q8h if HSV suspected)

**Infants and children (1 month - 18 years):**
- **Ceftriaxone 100 mg/kg IV (max 4 g)** as first dose
- ADD vancomycin 15 mg/kg IV (max 1 g) if MRSA risk (central line, recent hospitalization, skin/soft tissue source)
- ADD metronidazole 10 mg/kg IV (max 500 mg) if abdominal source suspected

**Immunocompromised:**
- **Cefepime 50 mg/kg IV q8h (max 2 g per dose)** (Pseudomonas coverage)
- ADD vancomycin 15 mg/kg IV q6h (max 1 g per dose)

**Toxic shock syndrome suspected:**
- ADD clindamycin 10 mg/kg IV q8h (max 900 mg) for toxin inhibition

### Fluid-Refractory Shock — Vasopressors
- **Cold shock (poor perfusion, delayed cap refill):** epinephrine 0.05-0.3 mcg/kg/min IV
- **Warm shock (bounding pulses, flash cap refill, wide pulse pressure):** norepinephrine 0.05-0.3 mcg/kg/min IV
- Titrate to MAP and clinical endpoints (capillary refill, urine output, mental status)
- Through central or IO access (do NOT delay for central line if IO available)

### Catecholamine-Resistant Shock
- **Hydrocortisone 2 mg/kg IV bolus (max 100 mg)** if catecholamine-resistant shock or known adrenal insufficiency
- Maintain glucose > 60 mg/dL: D10W 5 mL/kg IV bolus PRN

## Disposition

- **Septic shock:** PICU admission; continuous hemodynamic monitoring; arterial line and central venous catheter placement
- **Sepsis without shock but with organ dysfunction:** PICU or step-down unit
- **Febrile infant with suspected sepsis, hemodynamically stable:** admit to pediatric ward with close monitoring
- **Transfer:** if no PICU capability, stabilize and transfer; continue fluids and vasopressors during transport

## Pitfalls

1. **Waiting for hypotension to diagnose shock in children.** Children compensate for hypovolemia through tachycardia and vasoconstriction. By the time blood pressure drops, they are in decompensated shock. Tachycardia, altered mental status, and abnormal perfusion (cap refill) are the key early signs.

2. **Under-resuscitating with fluids due to fear of fluid overload.** Septic children may need 40-60 mL/kg or more in the first hour. Reassess after each 20 mL/kg bolus for hepatomegaly and rales, but do not withhold fluids empirically.

3. **Delaying antibiotics for lumbar puncture in a sick neonate.** If the infant is hemodynamically unstable, give antibiotics immediately. CSF cultures can still be positive hours after the first antibiotic dose. LP can be performed later when the patient is stabilized.

4. **Not checking glucose.** Hypoglycemia is common in septic neonates and young children and can cause seizures and brain injury. Check point-of-care glucose immediately and treat with D10W 5 mL/kg if < 60 mg/dL.

5. **Using cold shock management (epinephrine) for warm shock.** Pediatric shock has two distinct phenotypes. Cold shock (vasoconstricted) responds to epinephrine. Warm shock (vasodilated) responds to norepinephrine. Reassess the shock phenotype at each interval.

6. **Failing to consider adrenal insufficiency.** Children on chronic corticosteroids, those with purpura fulminans (Waterhouse-Friderichsen syndrome), or those with catecholamine-resistant shock may have adrenal crisis. Empiric hydrocortisone 2 mg/kg IV can be lifesaving.
