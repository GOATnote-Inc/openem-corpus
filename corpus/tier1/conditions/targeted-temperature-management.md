---
id: targeted-temperature-management
condition: Targeted Temperature Management
aliases: [TTM, therapeutic hypothermia, post-arrest cooling, temperature management]
icd10: [I46.9, I46.2, G93.1]
esi: 1
time_to_harm:
  irreversible_injury: "Minutes to hours (ongoing secondary brain injury post-ROSC)"
  death: "Post-cardiac arrest mortality 50-70% at 6 months without neuroprotective strategies"
  optimal_intervention_window: "Initiate within 6 hours of ROSC"
category: procedural
track: tier1
sources:
  - type: guideline
    ref: "Donnino MW, Andersen LW, Berg KM, et al. Temperature Management After Cardiac Arrest: A Science Advisory From the American Heart Association. Circulation. 2023;148(9):e30-e48."
    pmid: "37497802"
  - type: pubmed
    ref: "Dankiewicz J, Cronberg T, Lilja G, et al. Hypothermia versus Normothermia after Out-of-Hospital Cardiac Arrest (TTM2). N Engl J Med. 2021;384(24):2283-2294."
    pmid: "34133859"
  - type: pubmed
    ref: "Bernard SA, Gray TW, Buist MD, et al. Treatment of comatose survivors of out-of-hospital cardiac arrest with induced hypothermia. N Engl J Med. 2002;346(8):557-563."
    pmid: "11856794"
  - type: guideline
    ref: "Panchal AR, Bartos JA, Cabanas JG, et al. Part 3: Adult Basic and Advanced Life Support: 2020 AHA Guidelines for CPR and ECC. Circulation. 2020;142(16_suppl_2):S366-S468."
    pmid: "33081529"
  - type: pubmed
    ref: "Nielsen N, Wetterslev J, Cronberg T, et al. Targeted temperature management at 33 degrees C versus 36 degrees C after cardiac arrest (TTM trial). N Engl J Med. 2013;369(23):2197-2206."
    pmid: "24237006"
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
# Targeted Temperature Management

## Recognition

**Indications (Post-Cardiac Arrest):**
- Comatose adult survivors (GCS motor < 6) of out-of-hospital cardiac arrest (OHCA) of any initial rhythm who achieve ROSC
- Comatose adult survivors of in-hospital cardiac arrest (IHCA) who achieve ROSC
- Active fever prevention (temperature < 37.5 degrees C) is recommended for ALL comatose post-arrest patients (ILCOR 2022, AHA 2023)
- Whether to target 33 degrees C vs normothermia (< 37.5 degrees C) remains institution-specific; TTM2 trial showed no mortality difference between 33 degrees C and normothermia with active fever prevention

**Current Evidence Landscape:**
- TTM2 (2021, N=1850): no difference in mortality or neurologic outcome between hypothermia at 33 degrees C vs normothermia with active fever prevention at < 37.5 degrees C
- AHA 2023 Science Advisory: "actively prevent fever by targeting a temperature <= 37.5 degrees C for patients who remain comatose after ROSC"
- ILCOR 2022: recommends temperature control for all comatose post-arrest patients; does not mandate specific target
- The key intervention is AVOIDING FEVER — fever after cardiac arrest is strongly associated with worse neurologic outcomes

**Contraindications to Active Hypothermia (33 degrees C):**
- Active hemorrhage or severe coagulopathy
- Refractory hemodynamic instability despite vasopressors (hypothermia causes vasoconstriction, increases SVR)
- Known terminal illness with comfort measures
- DNR order in place

**Not Indications for TTM:**
- Awake, purposeful patients post-ROSC (GCS motor >= 6) — these patients have intact neurologic function
- Patients with obvious non-survivable injuries

## Critical Actions

| Action | Target |
|--------|--------|
| ROSC achieved | Time zero |
| Temperature monitoring initiated | Immediately post-ROSC |
| Active fever prevention | Maintain < 37.5 degrees C for >= 24 hours |
| If targeting 33 degrees C: reach target | Within 4 hours of ROSC |
| Maintain target temperature | 24 hours minimum |
| Controlled rewarming | 0.25-0.5 degrees C/hour |
| Normothermia maintenance post-rewarming | >= 48 hours (avoid rebound hyperthermia) |

1. **Initiate continuous core temperature monitoring** — esophageal (preferred), bladder, or rectal probe
2. **Prevent fever** — active cooling if temperature >= 37.5 degrees C
3. **Choose target strategy** per institutional protocol (33 degrees C vs normothermia < 37.5 degrees C)
4. **Initiate cooling** — surface or intravascular device
5. **Sedate and paralyze** — prevent shivering (shivering generates heat and increases metabolic demand)
6. **Maintain target temperature** for >= 24 hours
7. **Controlled rewarming** at 0.25-0.5 degrees C/hour
8. **Prevent rebound hyperthermia** for >= 48 hours after rewarming

## Differential Diagnosis

**Other Post-Cardiac Arrest Interventions:**

| Intervention | Purpose |
|-------------|---------|
| Coronary angiography / PCI | Treat ST elevation or high suspicion of coronary occlusion |
| Hemodynamic optimization | MAP > 65 mmHg; avoid hypotension (SBP < 90) |
| Ventilatory targets | PaO2 > 75, avoid hyperoxia (FiO2 titrate to SpO2 94-98%); PaCO2 35-45 mmHg |
| Seizure management | Continuous EEG monitoring; treat electrographic seizures |
| Neuroprognostication | Defer until >= 72 hours after rewarming (or >= 72 hours after ROSC if normothermia) |

## Workup

**Pre-Procedure Assessment:**
- Confirm comatose status (GCS motor < 6)
- Identify and treat cause of arrest: 12-lead ECG (STEMI → cath lab), CT head (hemorrhagic stroke), CT chest (PE), labs (electrolytes, toxicology)
- Baseline labs: CBC, BMP, coagulation, lactate, troponin, ABG
- Core temperature measurement: esophageal probe (most accurate), bladder catheter with temperature sensor, or rectal probe

**Equipment:**

| Item | Specification |
|------|---------------|
| Temperature probe | Esophageal (preferred), bladder (acceptable), rectal (acceptable) |
| Surface cooling | Arctic Sun (hydrogel pads), cooling blankets, ice packs to axillae/groin/neck |
| Intravascular cooling | Thermogard (femoral or IJ catheter — closed-loop, most precise control) |
| Warm IV fluids | For controlled rewarming phase |
| Monitoring | Continuous core temp display, cardiac monitor, arterial line, Foley with temp sensor |
| Sedation/paralysis | For shivering control |

## Treatment

### Phase 1: Induction (ROSC to Target Temperature)

**Active Fever Prevention (All Patients):**
- Target: core temperature < 37.5 degrees C
- Initiate immediately post-ROSC
- Remove external warming (blankets, heated fluids)
- Cold IV saline (4 degrees C) 30 mL/kg bolus (rapid infusion) — reaches hypothermic targets faster but routine use for induction is no longer recommended (risk of pulmonary edema per RINSE trial); use judiciously
- Surface cooling: Arctic Sun pads or cooling blankets
- Antipyretics alone are insufficient — active cooling devices are needed

**Hypothermic TTM (33 degrees C, If Institutional Protocol):**
- Target core temp 33 degrees C (+/- 0.5 degrees C)
- Cold IV saline 4 degrees C, 30 mL/kg rapid infusion
- Surface cooling (Arctic Sun) or intravascular cooling (Thermogard)
- Goal: reach 33 degrees C within 4 hours of ROSC (faster is better)
- Intravascular devices reach target faster and maintain temp more precisely than surface devices

### Phase 2: Maintenance (24 Hours at Target)

**Shivering Management (Critical):**
- Shivering generates heat and increases metabolic demand by 40-100%, counteracting cooling
- **Bedside Shivering Assessment Scale (BSAS):** 0 = no shivering, 3 = generalized shivering
- **Step 1:** Skin counter-warming (warm blanket on hands/feet while cooling the core — reduces afferent cold signals)
- **Step 2:** Magnesium sulfate 2-4 g IV (raises shivering threshold)
- **Step 3:** Meperidine 25-50 mg IV q4h (lowers shivering threshold more than other opioids)
- **Step 4:** Buspirone 30 mg via NG tube
- **Step 5:** Propofol 20-50 mcg/kg/min + fentanyl 25-100 mcg/hr (deep sedation)
- **Step 6:** Neuromuscular blockade — cisatracurium 0.1-0.2 mg/kg IV bolus then 1-3 mcg/kg/min; MUST have continuous EEG monitoring with paralysis (cannot assess clinical seizures)

**Monitoring During Maintenance:**
- Core temp every 15 minutes (closed-loop device) or continuous
- Cardiac rhythm: bradycardia is expected (and generally beneficial) at 33 degrees C
- Labs q6h: K+, Mg2+, glucose, lactate, coagulation
- Potassium: hypothermia drives K+ intracellularly — serum K+ drops; replace cautiously (K+ will shift back out during rewarming)
- Glucose: insulin resistance increases at 33 degrees C — manage hyperglycemia (target 140-180 mg/dL)
- Coagulation: hypothermia impairs clotting; monitor for bleeding

### Phase 3: Rewarming (Controlled)

- Rate: 0.25-0.5 degrees C/hour (SLOW — rapid rewarming worsens outcomes)
- Total rewarming duration: 8-16 hours (from 33 degrees C to 37 degrees C)
- Use active warming device on controlled rate — do NOT passively rewarm
- Watch for:
  - Rebound hyperkalemia (K+ shifts out of cells; recheck K+ hourly during rewarming)
  - Hypotension (vasodilation with rewarming)
  - Seizures (often emerge during rewarming)

### Phase 4: Post-Rewarming Normothermia (>= 48 Hours)

- Target temperature < 37.5 degrees C for at least 48 hours after rewarming
- Active cooling remains in place — rebound hyperthermia occurs in 30-40% of patients and is associated with worse outcomes
- Continue sedation titration and monitoring

### Post-Procedure
- Neuroprognostication: defer multimodal assessment until >= 72 hours after achieving normothermia (or >= 72 hours after ROSC if normothermia target was used)
- Continuous or routine EEG monitoring for seizure detection
- MRI brain at 48-72 hours post-ROSC if neuroprognostication unclear
- Neurology consultation

## Disposition

- **All post-arrest patients undergoing TTM:** ICU admission with continuous monitoring, ventilator, and temperature management device
- **If STEMI or suspected ACS:** coronary angiography can and should be performed during TTM (hypothermia is NOT a contraindication to PCI)
- **Withdrawal of care considerations:** only after multimodal neuroprognostication at >= 72 hours; do NOT prognosticate early based on exam alone — sedation and hypothermia confound the exam
- **Transfer:** if facility lacks TTM capability, initiate cooling (cold saline, ice packs) and transfer to a cardiac arrest center

## Pitfalls

1. **Allowing fever in the post-arrest patient.** Fever (> 37.5 degrees C) after cardiac arrest is independently associated with worse neurologic outcomes. Whether the chosen strategy is 33 degrees C hypothermia or normothermia, the critical intervention is PREVENTING FEVER. Even if not targeting 33 degrees C, active temperature monitoring and cooling must be initiated.

2. **Aggressive potassium replacement during the hypothermic phase.** Hypothermia shifts K+ intracellularly, causing apparent hypokalemia. If K+ is replaced aggressively to normal levels during cooling, dangerous hyperkalemia develops during rewarming as K+ redistributes. Target K+ 3.0-3.5 mEq/L during the hypothermic phase.

3. **Rapid rewarming causing hemodynamic instability and rebound injury.** Rewarming faster than 0.5 degrees C/hour causes vasodilation (hypotension), rebound hyperkalemia, seizures, and potential worsening of neurologic injury. Use a closed-loop device at 0.25-0.5 degrees C/hour. Passive rewarming (removing blankets) provides no rate control.

4. **Prognosticating too early.** Sedation, hypothermia, and neuromuscular blockade confound neurologic examination. The earliest reliable neuroprognostication is >= 72 hours after rewarming. Premature withdrawal of care based on early exams is a leading cause of "self-fulfilling prophecy" in post-arrest mortality.

5. **Not treating shivering effectively.** Shivering increases metabolic demand by 40-100% and prevents the patient from reaching or maintaining target temperature. A stepwise anti-shivering protocol (counter-warming → magnesium → meperidine → sedation → paralysis) must be deployed aggressively. Paralysis requires concurrent EEG monitoring.

6. **Omitting EEG monitoring during neuromuscular blockade.** Paralyzed patients cannot manifest clinical seizures. Post-arrest seizures occur in 10-40% of patients. Without EEG, seizures go undetected and untreated, worsening secondary brain injury. Continuous EEG is mandatory when paralytics are used.
