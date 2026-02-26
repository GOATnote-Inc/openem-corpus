---
id: rhabdomyolysis
condition: Rhabdomyolysis
aliases: [rhabdo, myoglobinuria, crush syndrome]
icd10: [M62.82, T79.6XXA]
esi: 2
time_to_harm: "< 24 hours for renal injury"
mortality_if_delayed: "8-20% with AKI; higher in crush syndrome"
category: musculoskeletal
track: tier1
sources:
  - type: pubmed
    ref: "Long B, Koyfman A, Gottlieb M. An Evidence-Based Narrative Review of the Emergency Department Evaluation and Management of Rhabdomyolysis. Am J Emerg Med. 2019;37(3):518-523"
    pmid: "30630682"
  - type: pubmed
    ref: "Sawhney JS, Kasotakis G, Goldenberg A, et al. Management of Rhabdomyolysis: A Practice Management Guideline from the Eastern Association for the Surgery of Trauma. Am J Surg. 2022;224(1 Pt A):196-204"
    pmid: "34836603"
  - type: pubmed
    ref: "Kodadek L, Carmichael SP II, Seshadri A, et al. Rhabdomyolysis: An American Association for the Surgery of Trauma Critical Care Committee Clinical Consensus Document. Trauma Surg Acute Care Open. 2022;7(1):e000836"
    pmid: "35136842"
  - type: pubmed
    ref: "Chavez LO, Leon M, Einav S, Varon J. Beyond Muscle Destruction: A Systematic Review of Rhabdomyolysis for Clinical Consideration. Crit Care. 2016;20(1):135"
    pmid: "27301374"
  - type: pubmed
    ref: "Bosch X, Poch E, Grau JM. Rhabdomyolysis and Acute Kidney Injury. N Engl J Med. 2009;361(1):62-72"
    pmid: "19571284"
last_updated: "2026-02-19"
compiled_by: agent
risk_tier: B
validation:
  schema_version: "2.0"
  automated_consistency_check: "2026-02-27"
  dose_range_validator: "2026-02-27"
  unit_normalization_check: "2026-02-27"
  cross_file_consistency_check: "2026-02-27"
  citation_presence_check: "2026-02-27"
  duplicate_content_check: "2026-02-27"
  outlier_detection_flag: clear
  provenance_links: []
---
# Rhabdomyolysis

## Recognition

**Definition:** Skeletal muscle necrosis with release of intracellular contents (CK, myoglobin, potassium, phosphate, lactate dehydrogenase, uric acid) into the circulation. Diagnosed by CK > 5x upper limit of normal (typically > 1000 U/L). CK > 5000 U/L significantly increases AKI risk; CK > 15,000 U/L carries highest renal risk.

**Classic triad:**
1. Myalgia (muscle pain, tenderness, swelling)
2. Weakness (focal or generalized)
3. Dark (tea/cola-colored) urine — myoglobinuria

**Triad present in < 10% of cases.** Many patients present with only one or two features. Dark urine requires > 100 mg/dL myoglobin and is absent early.

**Etiologic categories:**

| Category | Examples |
|----------|----------|
| Traumatic/crush | Crush injury, entrapment, prolonged immobilization (found down), surgical positioning |
| Exertional | Military training, endurance events, CrossFit, seizures, status epilepticus, agitated delirium |
| Drug/toxin | Statins (especially + fibrates/CYP3A4 inhibitors), cocaine, amphetamines, heroin, alcohol, carbon monoxide |
| Hyperthermia syndromes | NMS, serotonin syndrome, malignant hyperthermia, heat stroke |
| Ischemic | Compartment syndrome, vascular occlusion, tourniquet, sickle cell crisis |
| Metabolic | Hypokalemia, hypophosphatemia, DKA, hypothyroidism, McArdle disease |
| Infectious | Influenza, HIV, Legionella, Coxsackie, COVID-19 |
| Inflammatory | Polymyositis, dermatomyositis |

## Critical Actions

| Action | Target |
|--------|--------|
| IV crystalloid resuscitation | Start 1-2 L bolus, then 200-300 mL/hr; target UOP 200-300 mL/hr (approximately 3 mL/kg/hr) |
| Stat potassium (VBG or iStat) | Within 15 minutes of recognition |
| ECG | Immediate — assess for hyperkalemia changes |
| Foley catheter | Insert for strict I/O monitoring; UOP is the resuscitation endpoint |
| Treat hyperkalemia | Per hyperkalemia protocol if K+ >= 6.0 or ECG changes |
| Nephrology consultation | CK > 15,000, oliguria/anuria despite fluids, refractory hyperkalemia, acidosis |

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Myocardial infarction | CK-MB and troponin elevated disproportionately to total CK; ECG changes; chest pain |
| Hemolytic anemia | LDH elevated, haptoglobin low, peripheral smear with schistocytes; CK normal |
| Myositis (inflammatory) | Gradual onset, proximal weakness, CK usually < 5000, autoantibodies (anti-Jo-1, anti-MDA5) |
| Hepatic injury | AST/ALT elevated but CK normal or mildly elevated; transaminase rise without myoglobinuria |
| Renal colic | Flank pain, hematuria (RBCs on microscopy, not myoglobinuria); CK normal |
| Compartment syndrome | Tense compartment, pain with passive stretch, elevated compartment pressures; CK is elevated as a consequence |
| NMS / serotonin syndrome | Rigidity, hyperthermia, autonomic instability; rhabdomyolysis is a complication, not the primary diagnosis — treat the underlying syndrome |

## Workup

**Labs:**
- **CK** (creatine kinase) — diagnostic. Peaks 24-72 hours after injury. Repeat q6-12h to trend. CK > 5000 U/L: significant AKI risk. CK > 15,000 U/L: high AKI risk.
- **BMP** — potassium (hyperkalemia from cell lysis), calcium (hypocalcemia early from Ca2+-phosphate deposition; hypercalcemia in recovery phase), phosphate (hyperphosphatemia), BUN/creatinine (AKI)
- **VBG** — rapid potassium and pH; metabolic acidosis from organic acids
- **Urinalysis** — dipstick positive for blood (heme pigment from myoglobin) with absent RBCs on microscopy = myoglobinuria. Dipstick cannot distinguish hemoglobin from myoglobin.
- **Serum myoglobin** — clears faster than CK (half-life 2-3 hours vs 36 hours); normal myoglobin does not exclude rhabdomyolysis if CK is elevated
- **Lactate** — tissue ischemia, systemic illness severity
- **Coags (PT/INR, PTT, fibrinogen, D-dimer)** — DIC screening (rhabdomyolysis can trigger DIC)
- **Uric acid** — elevated from purine release
- **Hepatic panel** — AST released from injured muscle (AST:ALT ratio > 5:1 suggests muscle source)
- **CBC** — leukocytosis (stress response), thrombocytopenia (if DIC)
- **Toxicology screen** — cocaine, amphetamines, opioids if etiology unclear

**ECG:** Mandatory. Peaked T waves, QRS widening, sine wave from hyperkalemia.

**Imaging:** Based on etiology — CT of the affected extremity if compartment syndrome suspected; chest/pelvic X-ray if crush injury.

## Treatment

### IV Fluid Resuscitation (cornerstone of therapy)

- **Crystalloid:** Normal saline (0.9% NaCl) or lactated Ringer's
- **Initial bolus:** 1-2 L over first hour
- **Maintenance rate:** 200-300 mL/hr (up to 400 mL/hr in severe cases with CK > 15,000)
- **UOP target:** 200-300 mL/hr (approximately 3 mL/kg/hr) via Foley catheter
- **Duration:** Continue until CK is clearly downtrending AND < 5000 U/L AND myoglobinuria resolved
- **Volume assessment:** Auscultate lungs q2-4h, monitor JVP; reduce rate if pulmonary edema develops
- **Caution in heart failure/ESRD:** Aggressive fluids may precipitate pulmonary edema; early dialysis threshold

### Urine Alkalinization (controversial — EAST conditionally recommends against)

- **Regimen if used:** Sodium bicarbonate 150 mEq (3 ampules of 50 mEq) in 1 L D5W at 150-200 mL/hr
- **Goal:** Urine pH > 6.5 (myoglobin precipitates in acidic tubular fluid)
- **Monitor:** Serum pH (stop if > 7.50), ionized calcium (alkalosis worsens hypocalcemia), urine pH q2h
- **Do not use if:** Patient is already alkalotic, hypocalcemic with tetany, or anuric
- **Evidence:** No RCTs demonstrate reduced AKI or mortality; EAST 2022 and AAST 2022 guidelines do not support routine use

### Electrolyte Management

- **Hyperkalemia (K+ >= 6.0 or ECG changes):**
  - Calcium gluconate 10%: 30 mL (3 g) IV over 5-10 minutes (membrane stabilization)
  - Regular insulin 10 units IV + D50 50 mL (25 g) IV (intracellular shift)
  - Albuterol 10-20 mg nebulized over 15 minutes (synergistic with insulin)
  - See hyperkalemia condition file for full protocol
- **Hypocalcemia:** Do NOT empirically replace unless symptomatic (tetany, seizures, QT prolongation). Exogenous calcium deposits in damaged muscle and worsens tissue injury. Treat only if ionized calcium < 0.8 mmol/L with symptoms.
- **Hyperphosphatemia:** Restrict phosphate intake. Resolves with fluid resuscitation and renal recovery.
- **Hyperuricemia:** Responds to IV fluids. Allopurinol 300 mg PO daily if uric acid > 8 mg/dL and not anuric.

### Mannitol (limited role)

- 1-2 g/kg IV over 30-60 minutes as osmotic diuretic
- Only in oliguric patients WITH residual renal function
- Contraindicated if anuric (accumulates, causes osmotic injury)
- EAST 2022 conditionally recommends against routine use

### Renal Replacement Therapy (dialysis)

Indications:
- Refractory hyperkalemia (K+ > 6.5 despite medical management)
- Severe metabolic acidosis (pH < 7.1) unresponsive to bicarbonate
- Volume overload with pulmonary edema refractory to diuretics
- Oliguria/anuria despite adequate fluid resuscitation
- Uremic symptoms (encephalopathy, pericarditis)

CRRT preferred over intermittent HD in hemodynamically unstable patients.

### Avoid Nephrotoxins

- No NSAIDs (ibuprofen, ketorolac) — use acetaminophen 1 g IV/PO q6h or opioids for pain
- No IV contrast if avoidable (if CT required, benefit must outweigh risk; hydrate aggressively pre/post)
- No aminoglycosides
- Hold ACE inhibitors, ARBs

### Treat Underlying Cause

- NMS: stop offending antipsychotic, dantrolene 1-2.5 mg/kg IV q6h (max 10 mg/kg/day), active cooling
- Serotonin syndrome: stop serotonergic agents, cyproheptadine 12 mg PO loading then 4 mg PO q6h, active cooling
- Compartment syndrome: emergent fasciotomy
- Seizures: benzodiazepines, definitive seizure control
- Crush injury: address other traumatic injuries per ATLS

## Disposition

**ICU admission:**
- CK > 15,000 U/L
- AKI (rising creatinine, oliguria)
- Hyperkalemia requiring IV treatment
- DIC
- Need for dialysis or CRRT
- Associated compartment syndrome requiring fasciotomy
- NMS, serotonin syndrome, or malignant hyperthermia

**Telemetry/monitored bed:**
- CK 5000-15,000 U/L without AKI or hyperkalemia
- Responding to fluid resuscitation (adequate UOP, CK trending down)
- Electrolytes stable

**Discharge (rare from ED):**
- Mild rhabdomyolysis (CK 1000-5000 U/L) with:
  - Normal renal function (creatinine at baseline)
  - Normal potassium
  - Adequate oral hydration tolerated
  - CK clearly downtrending on repeat at 6 hours
  - Reliable follow-up within 24-48 hours for repeat CK and BMP
  - Clear, self-limited etiology (e.g., single exertional episode)

**All admitted patients:** serial CK q6-12h, BMP q6-8h, strict I/O, Foley catheter, daily weights.

## Pitfalls

1. **Inadequate fluid resuscitation.** Under-resuscitation is the most common error. Target UOP 200-300 mL/hr, not the standard 0.5 mL/kg/hr used for general resuscitation. Early aggressive crystalloid is the only intervention with consistent evidence for preventing AKI.

2. **Relying on urine dipstick to rule out myoglobinuria.** Dipstick detects heme pigment (hemoglobin AND myoglobin). A positive "blood" with no RBCs on microscopy suggests myoglobinuria. A negative dipstick does not exclude rhabdomyolysis — myoglobin clears the serum within hours (half-life 2-3 hours) while CK remains elevated for days. CK is the diagnostic test, not UA.

3. **Missing hyperkalemia.** Potassium rises rapidly from massive cell lysis and can reach lethal levels within hours, especially in patients with pre-existing renal insufficiency. Stat potassium (VBG or iStat) at presentation and ECG are mandatory. Do not wait for the BMP to return.

4. **Empirically repleting calcium in asymptomatic hypocalcemia.** Early hypocalcemia in rhabdomyolysis results from calcium deposition in damaged muscle. Exogenous calcium supplementation worsens tissue calcification and muscle injury. Replace only for symptomatic hypocalcemia (tetany, seizures, QTc prolongation, ionized Ca < 0.8 mmol/L).

5. **Ignoring the underlying cause.** Rhabdomyolysis is a syndrome, not a diagnosis. Failing to identify NMS, serotonin syndrome, compartment syndrome, or ongoing seizures leads to continued muscle destruction despite IV fluids. Treat the cause simultaneously.

6. **Using NSAIDs for pain control.** Ketorolac and ibuprofen are nephrotoxic and compound myoglobin-induced renal tubular injury. Use acetaminophen 1 g IV/PO q6h or opioids (morphine 0.1 mg/kg IV, hydromorphone 0.5-1 mg IV).

7. **Stopping fluids when CK begins to decline.** CK half-life is approximately 36 hours. A single downward trend does not mean the myoglobin burden has cleared. Continue aggressive fluids until CK < 5000 U/L and urine is clear.

8. **Discharging based on a single normal creatinine.** AKI from rhabdomyolysis is delayed — peak renal injury occurs 24-72 hours after muscle insult. A normal creatinine at ED presentation does not exclude impending AKI. Repeat BMP at 6-12 hours before disposition.

9. **Failing to check for compartment syndrome.** Rhabdomyolysis and compartment syndrome are bidirectional: each causes the other. Palpate all at-risk compartments in patients with extremity involvement. Pain out of proportion with passive stretch mandates pressure measurement or surgical consultation.

10. **Ordering urine myoglobin to "confirm" rhabdomyolysis.** Myoglobin has a short serum and urine half-life (2-3 hours) and is cleared before CK peaks. A negative urine myoglobin does not rule out rhabdomyolysis. CK > 5x ULN is the diagnostic standard. Do not delay treatment waiting for myoglobin results.
