---
id: carbon-monoxide-poisoning
condition: Carbon Monoxide Poisoning
aliases: [CO poisoning, carbon monoxide exposure, carboxyhemoglobinemia, smoke inhalation CO toxicity]
icd10: [T58.91XA, T58.01XA]
esi: 2
time_to_harm: "< 6 hours for neurologic injury; delayed sequelae in 15-40%"
mortality_if_delayed: "1-3% overall; up to 30% in severe poisoning with delayed treatment"
category: toxicologic
track: tier1
sources:
  - type: guideline
    ref: "Undersea and Hyperbaric Medical Society. Carbon Monoxide Poisoning: Indications for Hyperbaric Oxygen Therapy (2014)"
  - type: pubmed
    ref: "Weaver LK et al. Hyperbaric oxygen for acute carbon monoxide poisoning. N Engl J Med 2002;347(14):1057-1067"
    pmid: "12362006"
  - type: pubmed
    ref: "Hampson NB et al. Practice recommendations in the diagnosis, management, and prevention of carbon monoxide poisoning. Am J Respir Crit Care Med 2012;186(11):1095-1101"
    pmid: "23087025"
  - type: review
    ref: "Rose JJ et al. Carbon monoxide poisoning: pathogenesis, management, and future directions of therapy. Am J Respir Crit Care Med 2017;195(5):596-606"
    pmid: "27753502"
  - type: pubmed
    ref: "Thom SR et al. Delayed neuropathology after carbon monoxide poisoning is immune-mediated. Proc Natl Acad Sci U S A 2004;101(37):13660-13665"
    pmid: "15342916"
last_updated: "2026-02-19"
compiled_by: agent
risk_tier: B
validation:
  automated_consistency_check: null
  dose_range_validator: null
  unit_normalization_check: null
  cross_file_consistency_check: null
  citation_presence_check: null
  duplicate_content_check: null
  outlier_detection_flag: clear
  schema_version: "2.0"
  guideline_version_reference: null
  provenance_links: []
---
# Carbon Monoxide Poisoning

## Recognition

**Pathophysiology:** Carbon monoxide (CO) binds hemoglobin with 200-250x the affinity of oxygen, forming carboxyhemoglobin (COHb). This left-shifts the oxyhemoglobin dissociation curve, impairing oxygen delivery at the tissue level beyond what COHb percentage alone would predict. CO also binds myoglobin (cardiac and skeletal muscle toxicity), cytochrome c oxidase (mitochondrial dysfunction), and triggers oxidative stress, lipid peroxidation, and immune-mediated demyelination responsible for delayed neurologic sequelae.

**The "Great Mimicker" -- Symptoms by Severity:**
- **Mild (COHb 3-15%):** Headache (most common presenting symptom), nausea, dizziness, fatigue. Frequently misdiagnosed as viral illness, migraine, or food poisoning.
- **Moderate (COHb 15-25%):** Confusion, impaired judgment, visual disturbances, tachycardia, tachypnea, chest pain, shortness of breath.
- **Severe (COHb >25%):** Syncope, seizures, coma, cardiac ischemia/arrhythmia, pulmonary edema, lactic acidosis, rhabdomyolysis, death.

**Symptom-level correlation is poor.** Patients with low COHb levels at presentation may have had higher peak levels before measurement. Tissue toxicity (mitochondrial, myocardial) does not reliably track COHb.

**Exposure Contexts:**
- House fires / smoke inhalation (CO + cyanide co-exposure -- consider concurrent cyanide toxicity)
- Furnace/heater malfunction (winter clustering)
- Indoor use of generators, charcoal grills, or gasoline-powered equipment
- Motor vehicle exhaust in enclosed spaces (intentional or accidental)
- Methylene chloride exposure (paint stripper metabolized to CO in the liver -- delayed and prolonged COHb elevation)

**Critical Diagnostic Fact:** Standard pulse oximetry CANNOT detect CO poisoning. Conventional pulse oximeters measure the ratio of oxyhemoglobin to deoxyhemoglobin at two wavelengths and cannot distinguish COHb from oxyhemoglobin. SpO2 reads falsely normal (often 94-100%) in severe CO poisoning. Diagnosis requires co-oximetry (venous or arterial blood gas with co-oximetry), which measures COHb directly using multiple wavelengths.

**Significant COHb Levels:**
- Non-smokers: >3% (urban non-smokers may have 1-3% at baseline)
- Smokers: >10% (baseline COHb 3-8%)
- Symptomatic at any level warrants treatment

**Delayed Neurologic Sequelae (DNS):**
- Occurs in 15-40% of CO-poisoned patients, even after seemingly mild exposure
- Onset 2-40 days after exposure (typically 2-3 weeks)
- Manifestations: cognitive deficits, personality changes, parkinsonism, dementia, psychosis, gait disturbance, incontinence
- Pathology: immune-mediated perivascular demyelination (basal ganglia, white matter)
- Risk factors: loss of consciousness during exposure, age >36, prolonged exposure, COHb >25%

## Critical Actions

1. **Remove from exposure** and administer 100% O2 via non-rebreather mask (NRB) immediately. Do NOT wait for COHb level to initiate high-flow oxygen. NRB delivers FiO2 of 0.60-0.90 at 15 L/min with a tight seal.
2. **Obtain co-oximetry** (venous or arterial). Venous COHb is clinically equivalent to arterial COHb (within 1-2%). Do NOT rely on standard pulse oximetry -- it is falsely normal.
3. **ECG on all patients.** CO causes direct myocardial injury and demand ischemia. Troponin if any cardiac symptoms, ECG changes, or COHb >15%.
4. **Assess for concurrent cyanide poisoning** in fire victims. If altered mental status with lactic acidosis >8 mmol/L in a fire victim, administer empiric hydroxocobalamin 5g IV over 15 minutes.
5. **Evaluate for hyperbaric oxygen (HBO) criteria:** loss of consciousness/syncope, COHb >25%, pregnancy (any symptomatic or COHb >15%), persistent neurologic symptoms, cardiac ischemia/arrhythmia.
6. **Pregnancy test** in all females of reproductive age. Fetal hemoglobin binds CO with higher affinity than maternal hemoglobin; fetal COHb levels peak later and clear slower. Pregnant patients have a lower threshold for HBO referral.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Viral syndrome / influenza | No CO exposure history; no multiple patients from same dwelling; normal COHb. Cluster pattern (multiple household members sick simultaneously) suggests CO. |
| Migraine headache | Typical aura/pattern; no exposure context; normal COHb |
| Acute coronary syndrome | Primary cardiac event; no exposure history; but CO itself causes troponin elevation and ischemic ECG changes -- always check COHb in undifferentiated chest pain with headache |
| Cyanide poisoning | Occurs with CO in fire victims; profound lactic acidosis (>8 mmol/L), rapid cardiovascular collapse, cherry-red skin (rare); COHb may be co-elevated |
| Methemoglobinemia | Cyanosis unresponsive to supplemental O2; chocolate-brown blood; co-oximetry shows elevated MetHb, not COHb |
| Tension headache / gastroenteritis | Diagnosis of exclusion; always consider CO when multiple household members present with headache, nausea simultaneously |
| Drug or alcohol intoxication | Toxicology screen positive; no exposure history; normal COHb |

## Workup

**Labs:**
- **Co-oximetry (COHb level)** -- THE diagnostic test. Venous or arterial. Venous is adequate and avoids arterial puncture. Obtain immediately; level decreases with time and supplemental O2. COHb >3% (non-smoker) or >10% (smoker) is significant when symptomatic.
- ABG/VBG with lactate -- metabolic acidosis and elevated lactate reflect tissue hypoxia. Lactate >2 mmol/L in CO poisoning indicates significant tissue effect.
- Troponin -- myocardial injury in 30-40% of moderate-severe CO poisoning. Elevated troponin is associated with increased mortality.
- BMP -- renal function (rhabdomyolysis risk), electrolytes
- CBC -- leukocytosis common in severe poisoning
- CK -- rhabdomyolysis from prolonged unresponsiveness on hard surface or direct myotoxicity
- Pregnancy test (urine hCG) -- all females of reproductive age; lowers HBO threshold
- Serum ethanol and toxicology screen -- co-intoxication common in intentional exposure

**ECG:**
- All patients. Look for: ST changes (ischemia), QTc prolongation, arrhythmias (atrial fibrillation, ventricular ectopy). CO causes direct myocardial injury independent of coronary artery disease.

**Imaging:**
- CXR -- if smoke inhalation (pulmonary edema, aspiration, thermal airway injury)
- CT head (non-contrast) -- if altered mental status, seizures, or focal neurologic deficits. Acute findings: bilateral globus pallidus hypodensities (classic but late finding). MRI is more sensitive for white matter demyelination in DNS.

**Do NOT order:**
- Standard pulse oximetry as a diagnostic tool for CO (reads falsely normal)
- Methemoglobin level is on co-oximetry panel (obtain it, but it does not diagnose CO)

## Treatment

**Normobaric Oxygen (NBO2) -- All Patients:**
- 100% O2 via non-rebreather mask at 15 L/min with tight seal
- Reduces COHb half-life from 4-6 hours (room air) to 60-90 minutes (100% NBO2)
- Continue until COHb <3% AND symptoms resolved (typically 4-6 hours minimum)
- Intubated patients: FiO2 1.0 on ventilator
- Do NOT titrate O2 down based on SpO2 -- SpO2 is unreliable in CO poisoning

**Hyperbaric Oxygen (HBO) -- Criteria for Referral:**
- Loss of consciousness or syncope at any point during exposure
- COHb >25% (regardless of symptoms)
- Pregnancy with COHb >15% or any symptoms
- Persistent neurologic symptoms after NBO2 (confusion, ataxia, visual changes)
- Cardiac ischemia or arrhythmia attributable to CO
- Recurrent symptoms after initial improvement

HBO at 2.5-3.0 ATA reduces COHb half-life to 15-23 minutes and increases dissolved oxygen in plasma independent of hemoglobin. The Weaver 2002 RCT demonstrated that 3 sessions of HBO within 24 hours reduced cognitive sequelae at 6 weeks and 12 months compared to NBO2. Contact nearest HBO facility early -- transport logistics take time.

**Concurrent Cyanide Poisoning (Fire Victims):**
- If lactate >8 mmol/L with altered mental status in a fire victim, administer hydroxocobalamin (Cyanokit) 5g IV over 15 minutes empirically
- Hydroxocobalamin is safe to co-administer with oxygen therapy
- Do NOT give sodium thiosulfate as sole cyanide antidote in combined CO/CN poisoning (does not address CO)

**Supportive Care:**
- Continuous cardiac monitoring -- arrhythmia risk
- IV crystalloid for volume support (rhabdomyolysis prevention if CK elevated)
- Seizures: benzodiazepines first-line (midazolam 5-10 mg IV/IM or diazepam 10 mg IV)
- Cerebral edema: elevate head of bed, osmotic therapy per TBI protocol if evidence of elevated ICP

## Disposition

**ICU Admission:**
- COHb >25%
- Loss of consciousness, seizures, or coma
- Cardiac ischemia, arrhythmia, or elevated troponin
- Requiring mechanical ventilation
- Significant metabolic acidosis (pH <7.2, lactate >5 mmol/L)
- Pregnancy with significant exposure

**Admit to Monitored Bed (Observation/Telemetry):**
- COHb 15-25% with resolving symptoms on NBO2
- Ongoing NBO2 therapy with symptom monitoring
- Psychiatric evaluation if intentional exposure (medical clearance first)

**HBO Transfer:**
- Arrange transfer to nearest HBO facility if criteria met. Continue 100% O2 during transport. Do NOT delay transfer for repeat COHb levels.
- HBO is time-sensitive -- most effective within 6 hours of exposure, still beneficial up to 24 hours

**Discharge Criteria (must meet ALL):**
- COHb <3% on co-oximetry
- Completely asymptomatic (no headache, no dizziness, no confusion)
- Normal ECG and troponin (if obtained)
- Source of CO identified and corrected (or patient cannot return to the environment)
- Psychiatric evaluation completed if intentional
- Clear return precautions: return immediately for headache, confusion, gait difficulty, personality changes (DNS warning, with written instructions)
- Follow-up neuropsychiatric testing recommended at 4-6 weeks for patients with LOC, COHb >15%, or any neurologic symptoms

**Fire Department/Utility Notification:**
- If accidental exposure from home source, ensure fire department or gas utility has been contacted to evaluate the dwelling before patient returns

## Pitfalls

1. **Trusting pulse oximetry.** Standard pulse oximeters cannot distinguish COHb from oxyhemoglobin and display a falsely normal SpO2. A patient with COHb of 40% may show SpO2 of 98%. Diagnosis requires co-oximetry. Any patient with headache, nausea, or altered mental status in an exposure-risk context needs a COHb level, not a pulse ox.

2. **Failing to consider CO in the "cluster" presentation.** When multiple members of the same household present simultaneously with headache, nausea, and dizziness, CO poisoning must be the working diagnosis until excluded by co-oximetry. This pattern is frequently misdiagnosed as a "GI bug going around the family" or food poisoning.

3. **Using COHb level alone to determine severity.** Symptoms correlate poorly with COHb levels. Patients may present with low COHb after prolonged time since exposure or after O2 administration by EMS, yet have sustained significant tissue injury. A normal or near-normal COHb does not exclude serious poisoning if the clinical history suggests significant exposure.

4. **Not testing for pregnancy.** Fetal hemoglobin binds CO with higher affinity than adult hemoglobin. Fetal COHb peaks later and clears slower than maternal levels. Pregnant patients need HBO at lower thresholds (any symptoms or COHb >15%). Missing a pregnancy changes the treatment plan.

5. **Forgetting concurrent cyanide poisoning in fire victims.** Structural fires produce both CO and hydrogen cyanide (HCN) from combustion of synthetic materials. A fire victim with profound lactic acidosis (>8 mmol/L), cardiovascular collapse, or altered mental status disproportionate to COHb level likely has co-existent cyanide poisoning. Administer hydroxocobalamin 5g IV empirically.

6. **Stopping O2 too early based on a "normal" repeat COHb.** COHb level reflects blood compartment only, not tissue burden. A normalized COHb does not mean the mitochondrial, myocardial, and neurologic injury has resolved. Continue 100% O2 for a minimum of 4-6 hours and until symptoms have fully resolved, not just until COHb normalizes.

7. **Discharging without DNS counseling and follow-up.** Delayed neurologic sequelae occur in 15-40% of patients, even after apparently mild exposures. Symptoms (cognitive decline, personality changes, parkinsonism, gait disturbance) emerge 2-40 days after exposure. Every discharged CO patient needs written return precautions for neuropsychiatric symptoms and a recommended 4-6 week neuropsychiatric follow-up.

8. **Not obtaining an ECG and troponin.** CO causes direct myocardial injury and demand ischemia independent of coronary artery disease. Elevated troponin in CO poisoning is associated with increased long-term mortality. Cardiac ischemia is an indication for HBO. Missing it changes disposition and treatment.

9. **Dismissing methylene chloride exposure.** Methylene chloride (paint stripper) is metabolized to CO in the liver. COHb elevation is delayed (peaks hours after exposure) and prolonged (continues to rise after removal from source because the liver continues converting). Standard half-life calculations do not apply. These patients need prolonged monitoring and often HBO.
