---
id: rhabdomyolysis-metabolic
condition: Rhabdomyolysis
aliases: [rhabdomyolysis, muscle breakdown, myoglobinuria, crush syndrome metabolic, exertional rhabdomyolysis]
icd10: [M62.82]
esi: 2
time_to_harm:
  irreversible_injury: "< 24 hours"
  death: "< 72 hours"
  optimal_intervention_window: "< 6 hours"
category: endocrine-metabolic
track: tier1
sources:
  - type: guideline
    ref: "Long B et al. Rhabdomyolysis: An American Association for the Surgery of Trauma Critical Care Committee Clinical Consensus Document. J Trauma Acute Care Surg. 2022;92(2):e40-e53"
  - type: guideline
    ref: "Keltz E et al. Rhabdomyolysis: The Role of Diagnostic and Prognostic Factors. Muscles Ligaments Tendons J. 2013;3(4):303-312"
  - type: consensus-statement
    ref: "Eastern Association for the Surgery of Trauma. Management of rhabdomyolysis: A practice management guideline. Am J Surg. 2022;223(1):132-137"
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
# Rhabdomyolysis

## Recognition

**Definition:**
- Skeletal muscle injury with release of intracellular contents (myoglobin, CK, potassium, phosphate, uric acid) into circulation
- CK > 5x upper limit of normal (typically > 1000 U/L); CK > 5000 U/L = significant risk of AKI

**Classic triad (present in < 10% of cases):**
- Muscle pain/tenderness
- Weakness
- Dark (tea/cola-colored) urine

**Other presentations:**
- Myalgia, muscle swelling, tenderness
- Nausea, vomiting, abdominal pain
- Confusion, altered mental status
- Oliguria/anuria (AKI)
- Fever
- Can be completely asymptomatic with isolated CK elevation

**Common etiologies:**
- **Traumatic:** crush injury, compartment syndrome, prolonged immobilization, surgical positioning
- **Exertional:** intense exercise (especially eccentric), heat stroke, seizures, status epilepticus
- **Drug/toxin:** statins (especially with fibrates), alcohol, cocaine, amphetamines, heroin, NMS, serotonin syndrome, snake envenomation
- **Metabolic:** hypokalemia, hypophosphatemia, hypothyroidism, DKA
- **Infectious:** influenza, Legionella, Coxsackievirus, HIV, COVID-19
- **Genetic:** McArdle disease, CPT II deficiency (recurrent exercise-induced)

## Critical Actions

1. **Aggressive IV crystalloid resuscitation** — lactated Ringer's 200-400 mL/hr initially; goal urine output 200-300 mL/hr (3 mL/kg/hr)
2. **Check potassium immediately** — hyperkalemia is the most immediately life-threatening complication
3. **ECG** — K > 6.0 with ECG changes: calcium gluconate 3 g IV, insulin 10 units IV + D50 50 mL IV, albuterol 10-20 mg nebulized
4. **Foley catheter** — strict I/O monitoring; urine output is the primary treatment target
5. **Serial CK q6-12h** — peak usually 24-72 hours after insult; trending guides fluid therapy duration
6. **Evaluate for compartment syndrome** — palpate all compartments; emergent fasciotomy if compartment pressures > 30 mmHg or within 30 mmHg of diastolic pressure

## Differential Diagnosis

- Compartment syndrome (tense swelling, pain with passive stretch — surgical emergency)
- Acute kidney injury from other causes (pre-renal, ATN, obstruction)
- Myocardial infarction (elevated CK-MB; troponin more specific)
- Myositis (inflammatory; positive autoantibodies, subacute)
- Statin myopathy without rhabdomyolysis (mild CK elevation, myalgias)
- Neuroleptic malignant syndrome (rigidity, hyperthermia, altered mental status, antipsychotic exposure)
- Serotonin syndrome (clonus, agitation, diarrhea, serotonergic medication)
- Malignant hyperthermia (intraoperative, halogenated anesthetics/succinylcholine)
- Hemolysis (elevated LDH, bilirubin; low haptoglobin — NOT elevated CK)

## Workup

- **CK (creatine kinase)** — > 5x ULN diagnostic; > 5000 U/L significant AKI risk; > 15,000 high risk; > 40,000 very high risk
- **BMP:** potassium (hyperkalemia), calcium (hypocalcemia acutely → hypercalcemia in recovery), phosphate (hyperphosphatemia), creatinine, BUN
- **Urinalysis:** positive for blood on dipstick but no RBCs on microscopy = myoglobinuria (dipstick cannot distinguish hemoglobin from myoglobin)
- **ECG** — hyperkalemia changes: peaked T waves, prolonged PR, widened QRS, sine wave
- **CBC** — hemoconcentration, DIC screen
- **LDH, uric acid** — elevated in muscle necrosis
- **PT/INR, PTT, fibrinogen, D-dimer** — DIC screen
- **Lactate** — if shock or compartment syndrome suspected
- **Toxicology screen** — cocaine, amphetamines, other drugs of abuse
- **TSH** — hypothyroidism predisposes
- **CK-MB, troponin** — distinguish cardiac from skeletal muscle injury
- **Compartment pressures** — if clinical suspicion of compartment syndrome

## Treatment

### Volume Resuscitation (Cornerstone)
- **Lactated Ringer's** preferred over NS (avoids hyperchloremic acidosis; maintains urine pH > 6.5)
- Initial rate: 200-400 mL/hr; titrate to urine output 200-300 mL/hr (3 mL/kg/hr)
- Reduce rate for elderly and cardiac patients — monitor for volume overload
- CK < 5000 U/L: aggressive hydration generally not needed if renal function normal
- CK > 5000 U/L: aggressive hydration indicated

### Electrolyte Management

**Hyperkalemia (K > 6.0 or ECG changes):**
- Calcium gluconate 10% 30 mL (3 g) IV over 5-10 min — cardiac membrane stabilization
- Regular insulin 10 units IV + dextrose 50% 50 mL IV — intracellular K shift
- Albuterol 10-20 mg nebulized — intracellular K shift
- Sodium polystyrene sulfonate 30-60 g PO or rectal — K removal (delayed onset)
- Emergent hemodialysis if refractory

**Hypocalcemia:**
- Do NOT replace calcium unless symptomatic (tetany, seizures, ECG changes) — calcium deposits in injured muscle; rebound hypercalcemia occurs during recovery phase
- If symptomatic: calcium gluconate 1-2 g IV over 10-20 min

**Hyperphosphatemia:**
- Sevelamer 800-1600 mg PO TID with meals
- Calcium-based binders avoided (calcium already depositing in injured muscle)

### Bicarbonate Therapy (Controversial)
- Sodium bicarbonate to alkalinize urine (target urine pH > 6.5) — theoretically reduces myoglobin-induced tubular injury
- 150 mEq NaHCO3 in 1 L D5W at 200 mL/hr — only if urine pH < 6.5 AND CK > 30,000
- AAST/EAST guidelines: NOT routinely recommended; evidence insufficient
- Stop if metabolic alkalosis (pH > 7.50) or worsening hypocalcemia

### Renal Replacement Therapy
- Emergent hemodialysis for: refractory hyperkalemia, severe acidosis (pH < 7.1), volume overload, oliguric AKI unresponsive to fluids
- Continuous RRT (CRRT) preferred in hemodynamically unstable patients

### Compartment Syndrome
- Emergent surgical fasciotomy — do NOT delay for imaging or lab confirmation
- Compartment pressure > 30 mmHg or within 30 mmHg of diastolic = indication for fasciotomy

## Disposition

- **CK > 5000 with AKI or electrolyte abnormalities:** ICU or monitored bed
- **CK > 15,000:** admission for aggressive hydration and serial monitoring regardless of renal function
- **CK 1000-5000, normal renal function, adequate PO intake, no hyperkalemia:** observe in ED 6-12 hours, recheck CK; may discharge if trending down with aggressive PO hydration instructions
- **Compartment syndrome:** emergent OR
- **All admitted patients:** CK and BMP q6-12h until CK trending down; continue IV fluids until CK < 5000 and renal function stable

## Pitfalls

1. **Inadequate fluid resuscitation.** The single most important treatment is aggressive IV hydration. Underhydration leads to AKI from myoglobin-induced tubular obstruction and oxidative injury. Target urine output 200-300 mL/hr.

2. **Not checking potassium early and often.** Hyperkalemia is the most immediately life-threatening complication — it can cause fatal arrhythmia before AKI develops. Check K on arrival and q4-6h.

3. **Replacing calcium for asymptomatic hypocalcemia.** Calcium deposits in necrotic muscle during the acute phase. Replacing it paradoxically worsens muscle injury and causes rebound hypercalcemia during recovery. Treat only if symptomatic.

4. **Missing compartment syndrome.** Swollen, tense extremities with pain on passive stretch = compartment syndrome until proven otherwise. Fasciotomy must be performed emergently; delayed diagnosis leads to limb loss.

5. **Discharging with CK > 5000 without close follow-up.** AKI can develop 1-3 days after the initial insult. Patients discharged early need repeat BMP and CK within 24-48 hours.

6. **Using NS for large-volume resuscitation.** Large-volume NS causes hyperchloremic metabolic acidosis and lowers urine pH, potentially worsening myoglobin toxicity. LR is preferred.
