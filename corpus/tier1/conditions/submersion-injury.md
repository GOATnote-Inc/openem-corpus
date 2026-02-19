---
id: submersion-injury
condition: Submersion Injury
aliases: [drowning, near-drowning, freshwater drowning, saltwater drowning, immersion injury, submersion]
icd10: [T75.1XXA, W65.XXXA, W67.XXXA, W69.XXXA, W74.XXXA]
esi: 1
time_to_harm: "< 5 minutes (irreversible anoxic brain injury)"
mortality_if_delayed: "25-50% mortality for submersion with cardiac arrest; survivors have high rates of anoxic brain injury"
category: environmental
track: tier1
sources:
  - type: guideline
    ref: "2020 AHA Guidelines for CPR and ECC — Drowning"
  - type: guideline
    ref: "2021 WHO Global Report on Drowning: Preventing a Leading Killer"
    url: "https://www.who.int/publications/i/item/drowning"
  - type: review
    ref: "Szpilman D et al. Drowning. N Engl J Med 2012;366:2102-2110"
    pmid: "22646632"
  - type: guideline
    ref: "2023 European Resuscitation Council Guidelines: Cardiac Arrest in Special Circumstances — Drowning"
  - type: review
    ref: "Schmidt AC et al. Drowning: Epidemiology, Prevention, Pathophysiology, Resuscitation, and Rewarming. Wilderness Environ Med 2016;27(2):236-251"
    pmid: "27061040"
last_updated: "2026-02-18"
compiled_by: agent
risk_tier: A
validation:
  automated_consistency_check: "2026-02-18"
  dose_range_validator: "2026-02-19"
  unit_normalization_check: "2026-02-19"
  cross_file_consistency_check: "2026-02-19"
  citation_presence_check: "2026-02-19"
  duplicate_content_check: "2026-02-19"
  outlier_detection_flag: clear
  schema_version: "2.0"
  guideline_version_reference: null
  provenance_links: []
---
# Submersion Injury

## Recognition

**Definition:** Respiratory impairment from submersion or immersion in liquid. Per 2002 WHO/Utstein consensus, "drowning" is the unified term regardless of outcome. Terms "near-drowning," "dry drowning," "wet drowning," and "secondary drowning" are deprecated.

**Pathophysiology:**
- Hypoxia is the primary mechanism of death and injury
- Aspiration of as little as 1-3 mL/kg causes surfactant washout, atelectasis, intrapulmonary shunting, and pulmonary edema
- Fresh water: rapid absorption from alveoli, surfactant destruction, alveolar instability
- Salt water: osmotic pull of fluid into alveoli, pulmonary edema
- Clinical distinction between freshwater and saltwater drowning is irrelevant to ED management
- Hypothermia is frequently concurrent (especially cold water immersion)

**Classification by Severity (Szpilman Grading):**
- Grade 1: cough, no foam at mouth/nose, normal auscultation
- Grade 2: rales in some lung fields, small amount of foam
- Grade 3: acute pulmonary edema without hypotension
- Grade 4: acute pulmonary edema with hypotension
- Grade 5: respiratory arrest
- Grade 6: cardiac arrest

**Presentation:**
- Cough, dyspnea, tachypnea
- Vomiting (swallowed water)
- Altered mental status, agitation, unresponsiveness
- Cyanosis, frothy sputum (pulmonary edema)
- Hypothermia
- Cardiac arrest (PEA/asystole most common; VF if hypothermic)
- Possible concurrent: cervical spine injury (diving), trauma, seizures, intoxication

## Critical Actions

1. **Rescue breathing first** — drowning is a hypoxic arrest. Prioritize ventilation over compressions. Begin rescue breaths as soon as possible, even in the water if trained.
2. **Cervical spine precautions** — if mechanism suggests diving, fall, or trauma. Do not apply routinely to all submersion victims (delays resuscitation).
3. **Aggressive oxygenation** — high-flow O2 via NRB. Early intubation for Grade 3-6 (pulmonary edema, respiratory failure, coma).
4. **Warm the patient** — remove wet clothing, active rewarming. Hypothermic patients receive full resuscitation until core temp ≥ 32°C.
5. **Decompress the stomach** — vomiting and aspiration of swallowed water is common. Place OG/NG tube after airway is secured.
6. **Do NOT perform abdominal thrusts (Heimlich maneuver)** — does not remove water from lungs, delays ventilation, increases aspiration risk.
7. **Prolonged resuscitation** — intact neurologic survival has been reported after prolonged submersion, especially in cold water (children). Continue ACLS for at least 30 minutes; extend further for hypothermic patients.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Primary cardiac event (arrhythmia, MI) causing submersion | History of cardiac disease, preceding symptoms, ECG findings after resuscitation |
| Seizure causing submersion | History of epilepsy, witnessed tonic-clonic activity, postictal state, bitten tongue |
| Cervical spine injury (diving) | Mechanism (shallow water diving, fall), focal neurologic deficits, spinal tenderness |
| Intentional submersion (non-accidental) | Inconsistent history, pediatric patients with unexplained injuries, pattern injuries |
| Long QT syndrome | Family history of sudden death, QTc prolongation, young patient without risk factors |
| Trauma | Boat injury, propeller injury, fall with associated injuries |
| Intoxication causing submersion | Alcohol/drug use, toxicology positive |

## Workup

**Labs:**
- ABG/VBG (assess oxygenation, ventilation, acid-base status — lactic acidosis common)
- CBC
- BMP (electrolyte derangements uncommon despite theoretical freshwater/saltwater differences)
- Lactate
- Point-of-care glucose
- Coagulation studies (DIC in prolonged resuscitation)
- Troponin (if cardiac event suspected as cause or consequence)
- Ethanol, toxicology screen
- Blood type and screen (if traumatic mechanism)
- Core temperature (esophageal or rectal probe)

**Imaging:**
- Chest X-ray: pulmonary edema, aspiration, atelectasis. May be initially normal and worsen over 4-6 hours
- CT head: if altered mental status persists after resuscitation, concern for anoxic brain injury, or traumatic mechanism
- CT cervical spine: if diving, fall, or traumatic mechanism

**ECG:**
- Assess for arrhythmias, ischemia, QT prolongation
- Rule out primary cardiac event as cause of submersion

## Treatment

**Airway and Breathing:**
- Grade 1-2 (cough, mild rales): high-flow O2 via NRB, observation, supplemental O2 to maintain SpO2 > 94%
- Grade 3-4 (pulmonary edema): CPAP/BiPAP if conscious (CPAP 10-15 cmH2O). Intubate if not improving, altered, or cannot protect airway
- Grade 5-6 (respiratory/cardiac arrest): immediate intubation with PEEP 5-10 cmH2O, titrate up to 15-20 cmH2O for refractory hypoxemia
- Lung-protective ventilation: tidal volume 6-8 mL/kg ideal body weight, plateau pressure < 30 cmH2O (acute lung injury/ARDS from aspiration is common)
- Suction airway aggressively — particulate matter, vomitus, water

**Cardiac Arrest (Grade 6):**
- Standard ACLS with modifications:
  - Prioritize oxygenation/ventilation — 5 initial rescue breaths before compressions
  - Epinephrine 1 mg IV/IO q3-5 min per standard ACLS
  - If hypothermic: follow hypothermia-specific ACLS modifications (limit shocks to 3 below 30°C, withhold epinephrine below 30°C)
  - Defibrillation for VF/pVT per standard protocol (if normothermic)
  - Prolonged resuscitation: continue ≥ 30 min; extend for hypothermic patients until rewarmed to ≥ 32°C

**Hemodynamic Support:**
- IV crystalloid resuscitation for hypotension: NS or LR 20 mL/kg bolus
- Vasopressors (norepinephrine 0.05-0.5 mcg/kg/min IV) if persistent hypotension despite fluid resuscitation
- Inotropic support as needed

**Hypothermia Management:**
- Remove wet clothing immediately
- Active external rewarming (forced warm air, warm blankets)
- Warm IV fluids 40-42°C
- Severe hypothermia with arrest: ECMO/cardiopulmonary bypass if available

**Adjunctive:**
- Bronchospasm: albuterol 2.5 mg nebulized, repeat as needed
- Dextrose 50% 50 mL IV (adults) or dextrose 25% 2 mL/kg IV (pediatrics) if hypoglycemic
- Empiric antibiotics are NOT recommended; aspiration pneumonitis from clean water does not require antibiotics. Treat pneumonia if it develops.
- Corticosteroids: no benefit. Not indicated.
- Prophylactic antibiotics: not indicated for clean water submersion. Initiate antibiotics for grossly contaminated water (sewage, stagnant water) with evidence of pneumonia.

## Disposition

**ICU Admission:**
- Cardiac arrest survivors (Grade 6)
- Respiratory failure requiring intubation/mechanical ventilation (Grade 3-6)
- Persistent hemodynamic instability
- GCS < 13
- Hypothermia requiring active rewarming
- Targeted temperature management for neuroprotection post-arrest

**Floor/Observation (6-8 hours minimum):**
- Grade 1-2 with persistent symptoms or abnormal CXR
- Any submersion victim with cough, abnormal lung exam, or abnormal vitals
- Asymptomatic patients with significant mechanism (prolonged submersion, CPR in field)

**Discharge (after 6-8 hour observation):**
- Grade 1 (cough only), now asymptomatic
- Normal exam, normal SpO2 on room air, normal CXR at 6 hours
- Reliable follow-up, responsible adult at home
- Return precautions: cough, dyspnea, fever within 72 hours

**Do NOT discharge:**
- Any patient who required positive pressure ventilation in ED
- Any patient with persistent abnormal lung exam
- Any patient with abnormal CXR (even if asymptomatic — delayed pulmonary edema develops over 4-24 hours)

## Pitfalls

1. **Discharging too early.** Pulmonary edema from submersion can develop 4-24 hours after the event. Asymptomatic patients with significant submersion require a minimum 6-8 hour observation period with repeat CXR before safe discharge.

2. **Prioritizing chest compressions over ventilation.** Unlike cardiac arrest from primary cardiac etiology, drowning is a hypoxic arrest. The 2020 AHA guidelines emphasize rescue breathing first: 5 initial breaths before compressions. Compression-only CPR is inadequate for drowning.

3. **Performing abdominal thrusts to "drain the lungs."** The Heimlich maneuver does not remove water from the lungs. It delays effective ventilation, causes gastric distension and vomiting, and increases aspiration risk. Abandoned from all major drowning guidelines.

4. **Assuming brief submersion is benign.** Children can aspirate significant volumes in seconds. Even "minor" submersions with cough or transient dyspnea warrant ED evaluation and observation. Parents may minimize the event.

5. **Failing to address the cause of submersion.** Drowning in an adult in a bathtub or pool without clear circumstances requires evaluation for seizure, arrhythmia (long QT, Brugada), intoxication, or non-accidental injury. Drowning is the result, not the diagnosis.

6. **Routine cervical spine immobilization in all drowning.** C-spine precautions are indicated only when mechanism suggests spine injury (diving, fall, motorized watercraft). Universal spinal immobilization delays airway management, impedes effective ventilation, and is not supported by evidence for bathtub or supervised pool submersions.

7. **Giving prophylactic antibiotics.** Clean freshwater or chlorinated pool aspiration causes chemical pneumonitis, not bacterial pneumonia. Prophylactic antibiotics increase resistance and do not improve outcomes. Antibiotics are reserved for grossly contaminated water exposure with developing pneumonia.

8. **Premature termination of resuscitation.** Cold water submersion, especially in children, has produced intact neurologic survival after prolonged arrests. Fixed dilated pupils, asystole, and prolonged downtime in a hypothermic patient do not mandate termination. Continue resuscitation until core temp ≥ 32°C.

9. **Forgetting to evaluate for child abuse.** Submersion in young children with inconsistent history, delayed presentation, accompanying injuries, or prior ED visits for injuries should prompt concern for non-accidental trauma. Document findings meticulously and involve social work/child protective services.
