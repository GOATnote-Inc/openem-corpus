---
id: neuroleptic-malignant-syndrome
condition: Neuroleptic Malignant Syndrome
aliases: [NMS, neuroleptic malignant syndrome]
icd10: [G21.0]
esi: 1
time_to_harm: "< 24 hours"
mortality_if_delayed: "10-20% mortality overall; higher with delayed recognition"
category: psychiatric
track: tier1
sources:
  - type: review
    ref: "Wijdicks EFM, Ropper AH. Neuroleptic Malignant Syndrome. N Engl J Med. 2024;391(12):1130-1138"
    pmid: "39321364"
  - type: review
    ref: "Tse L et al. Neuroleptic Malignant Syndrome: A Review from a Clinically Oriented Perspective. Curr Neuropharmacol. 2015;13(3):395-406"
    pmid: "26411967"
  - type: review
    ref: "van Rensburg R, Decloedt EH. An Approach to the Pharmacotherapy of Neuroleptic Malignant Syndrome. Psychopharmacol Bull. 2019;49(1):84-91"
    pmid: "30858642"
  - type: review
    ref: "Pileggi DJ, Cook AM. Neuroleptic Malignant Syndrome. Ann Pharmacother. 2016;50(11):973-981"
    pmid: "27423483"
  - type: review
    ref: "Velamoor VR. Neuroleptic malignant syndrome: Recognition, prevention and management. Drug Saf. 1998;19(1):73-82"
    pmid: "9673859"
last_updated: "2026-02-19"
compiled_by: agent
risk_tier: A
validation:
  schema_version: "2.0"
  automated_consistency_check: null
  dose_range_validator: null
  unit_normalization_check: null
  cross_file_consistency_check: null
  citation_presence_check: null
  duplicate_content_check: null
  outlier_detection_flag: clear
  guideline_version_reference: null
  provenance_links: []
---
# Neuroleptic Malignant Syndrome

## Recognition

**Definition:** NMS is a life-threatening idiosyncratic reaction to dopamine-receptor antagonists characterized by the clinical tetrad of hyperthermia, severe muscular rigidity, autonomic instability, and altered mental status. Onset is typically 3-9 days after drug initiation or dose change, but ranges from hours to months.

**Diagnostic Criteria (DSM-5-TR):**
Exposure to a dopamine antagonist (or dopamine agonist withdrawal) within the preceding 72 hours, PLUS:
- Severe muscle rigidity
- Hyperthermia (>38.0C / 100.4F, often >40C / 104F)
- AND at least two of: diaphoresis, dysphagia, tremor, incontinence, altered level of consciousness (delirium to coma), mutism, tachycardia, blood pressure lability, leukocytosis, elevated creatine kinase

**Levenson Criteria (high sensitivity):**
Diagnosis is probable with 3 major criteria OR 2 major + 4 minor:
- Major: fever, rigidity, elevated CK
- Minor: tachycardia, abnormal blood pressure, tachypnea, altered consciousness, diaphoresis, leukocytosis

**Causative Agents:**
- First-generation antipsychotics (highest risk): haloperidol, fluphenazine, chlorpromazine
- Second-generation antipsychotics: olanzapine, risperidone, quetiapine, aripiprazole, clozapine
- Antiemetics with dopamine blockade: metoclopramide, promethazine, prochlorperazine, droperidol
- Abrupt withdrawal of dopaminergic agents: levodopa, bromocriptine, amantadine (Parkinson disease patients)
- Lithium (potentiates risk with concurrent antipsychotics)

**Risk Factors:**
- High-potency typical antipsychotic use (haloperidol)
- Rapid dose escalation or IM/IV route
- Dehydration, agitation, physical exhaustion
- Prior NMS episode (17-30% recurrence with rechallenge)
- Concurrent lithium
- Catatonia

**Key Exam Findings:**
- "Lead-pipe" rigidity (continuous, uniform resistance throughout range of motion — distinct from cogwheeling or clonus)
- Hyperthermia (core temp often 39-42C)
- Diaphoresis, sialorrhea
- Tachycardia, blood pressure lability (hypertension or hypotension)
- Tachypnea
- Altered mental status: agitated delirium progressing to obtundation and coma
- Tremor, dystonia, dysarthria, dysphagia
- Areflexia or hyporeflexia (distinguishes from serotonin syndrome)

**Typical Time Course:**
- Onset: 24-72 hours after drug exposure (90% within 10 days)
- Progression: hours to days (slower than serotonin syndrome or malignant hyperthermia)
- Resolution with treatment: 7-10 days (longer with depot antipsychotics — up to 21 days)

## Critical Actions

1. **Stop the offending agent immediately.** Discontinue all dopamine antagonists (antipsychotics, antiemetics). If NMS is from dopaminergic withdrawal, restart the dopamine agonist.
2. **Aggressive IV fluid resuscitation.** NS 1-2 L bolus, then 200-300 mL/hr targeting urine output >2 mL/kg/hr to prevent myoglobin-induced renal injury.
3. **Active cooling for temperature >39C.** Ice packs to axillae, groin, neck; evaporative cooling; cold IV saline. Target core temperature <38.5C.
4. **Benzodiazepines for agitation and rigidity.** Lorazepam 1-2 mg IV q4-6h. First-line pharmacotherapy; reduces rigidity, agitation, and sympathetic drive.
5. **Bromocriptine for moderate-to-severe NMS.** 2.5 mg PO/NG q8h, titrate up to 5 mg PO/NG q4-6h (max 40 mg/day). Continue for at least 10 days after NMS resolves, then taper slowly to avoid rebound.
6. **Dantrolene for severe rigidity or hyperthermia >40C.** 1-2.5 mg/kg IV, repeat q5-10 min PRN (max 10 mg/kg/day). Transition to dantrolene 1-3 mg/kg PO q6-8h once stabilized.
7. **ICU admission with continuous monitoring.** Cardiac telemetry, core temperature monitoring, hourly urine output, serial CK levels.
8. **Intubation if respiratory failure develops.** Respiratory failure from chest wall rigidity, aspiration, or obtundation. Avoid succinylcholine (hyperkalemia risk from rhabdomyolysis). Use rocuronium.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Serotonin syndrome | Serotonergic drug exposure; onset within hours; hyperkinetic features: clonus (especially lower extremity), hyperreflexia, myoclonus, agitation; rigidity less prominent; responds to cyproheptadine |
| Malignant hyperthermia | Volatile anesthetic/succinylcholine exposure; onset within minutes in OR/post-RSI; rising ETCO2 is earliest sign; no antipsychotic exposure; treat with dantrolene 2.5 mg/kg IV |
| Heat stroke | Environmental exposure; hot/dry skin (classic) or diaphoresis (exertional); no lead-pipe rigidity; no antipsychotic exposure; CK elevated but rigidity absent |
| Malignant catatonia | Psychiatric history (schizophrenia, mood disorders); catatonia precedes fever; waxy flexibility rather than lead-pipe rigidity; no clear drug trigger; may coexist with/progress to NMS; responds to benzodiazepines and ECT |
| CNS infection (meningitis/encephalitis) | Fever + AMS but no rigidity (nuchal rigidity differs from generalized lead-pipe); CSF pleocytosis; focal neurologic deficits; no CK elevation |
| Anticholinergic toxicity | Hot/dry/flushed skin (no diaphoresis); mydriasis; urinary retention; absent bowel sounds; no lead-pipe rigidity; responds to physostigmine |
| Thyroid storm | Known thyroid disease; tremor without lead-pipe rigidity; atrial fibrillation common; elevated free T4/T3; no antipsychotic exposure |
| Sympathomimetic toxicity (cocaine, amphetamines) | Tox history; mydriasis; agitation without lead-pipe rigidity; diaphoresis; seizures; urine drug screen positive |

## Workup

**Labs:**
- **CK (creatine kinase):** Hallmark finding. Often >1,000 IU/L; frequently >10,000 IU/L; levels >100,000 IU/L indicate severe rhabdomyolysis. Draw on presentation and q6-8h until trending down.
- **BMP:** Creatinine (acute kidney injury from rhabdomyolysis/myoglobinuria), potassium (hyperkalemia from muscle breakdown), calcium (hypocalcemia from myocyte calcium sequestration), BUN
- **CBC:** Leukocytosis (10,000-40,000/mcL) without left shift is typical
- **Hepatic panel:** AST/ALT elevation (from muscle and hepatic injury)
- **Coagulation studies:** PT/INR, PTT, fibrinogen, D-dimer — DIC occurs in severe cases
- **Myoglobin (serum and urine):** Urine dipstick positive for blood without RBCs = myoglobinuria
- **Lactate:** Elevated from rigidity-driven anaerobic metabolism
- **ABG/VBG:** Metabolic acidosis
- **Iron (serum):** Low serum iron (<10 mcmol/L) is seen in >90% of NMS cases; aids diagnosis when CK is equivocal
- **TSH, free T4:** Rule out thyroid storm
- **Blood cultures:** If infection not excluded
- **Urine drug screen:** Rule out sympathomimetic toxicity

**Imaging:**
- CT head without contrast: if altered mental status to exclude structural pathology
- CXR: if respiratory symptoms (aspiration pneumonia is a common complication)

**Other:**
- LP: if CNS infection is in the differential (CSF is normal in NMS)
- EEG: if concern for status epilepticus; NMS shows diffuse slowing without epileptiform activity

## Treatment

### Supportive Care (All Patients)
- **Stop the offending agent.** Every hour of continued exposure worsens outcome.
- **IV crystalloid:** NS 20 mL/kg bolus, then titrate to urine output >2 mL/kg/hr
- **Active cooling:** Evaporative cooling (mist + fan), ice packs, cold IV fluids. Target core temp <38.5C. Avoid antipyretics (ineffective; NMS hyperthermia is from muscular heat generation, not hypothalamic set-point elevation).
- **DVT prophylaxis:** Enoxaparin 40 mg SQ daily (immobilized, high DVT/PE risk)
- **Foley catheter:** Monitor urine output and urine color (dark = myoglobinuria)

### Pharmacotherapy

**Benzodiazepines (first-line for mild-moderate NMS):**
- Lorazepam 1-2 mg IV q4-6h, titrate to effect
- Reduces agitation, sympathetic overdrive, and mild-moderate rigidity
- Monotherapy sufficient for mild NMS (temp <39C, CK <1,000, no organ dysfunction)

**Bromocriptine (dopamine agonist — moderate-to-severe NMS):**
- 2.5 mg PO/NG q8h, increase by 2.5 mg q24h to max 5 mg q4-6h (max 40 mg/day)
- Restores dopaminergic transmission
- Do NOT stop abruptly after NMS resolves — taper over 10+ days to prevent rebound
- Contraindication: uncontrolled hypertension

**Amantadine (alternative dopamine agonist if bromocriptine unavailable):**
- 100 mg PO/NG q8h, increase to 200 mg PO/NG q12h (max 400 mg/day)
- Mechanism: enhances dopamine release, blocks NMDA receptors

**Dantrolene (severe NMS with rigidity, temp >40C, or rapidly worsening):**
- 1-2.5 mg/kg IV, repeat q5-10 min PRN (max 10 mg/kg/day)
- Maintenance: 1 mg/kg IV q4-6h for 48-72 hours after clinical improvement, then transition to dantrolene 1-3 mg/kg PO q6-8h
- Directly inhibits calcium release from sarcoplasmic reticulum, reducing rigidity and thermogenesis
- Monitor LFTs (hepatotoxicity risk, especially with oral dosing >10 days)
- Do NOT combine with calcium channel blockers (risk of hyperkalemia and cardiovascular collapse)

**Electroconvulsive Therapy (ECT):**
- Refractory NMS unresponsive to 48-72 hours of pharmacotherapy
- Particularly effective when catatonia is a prominent feature
- Bilateral electrode placement, 6-10 sessions

### Rhabdomyolysis Management
- Aggressive IV hydration: NS targeting urine output >2 mL/kg/hr (200-300 mL/hr in adults)
- Serial CK q6-8h until downtrending
- Sodium bicarbonate 1-2 mEq/kg IV to alkalinize urine (target urine pH >6.5) if CK >5,000
- Monitor potassium q4-6h (hyperkalemia from rhabdomyolysis)
- Nephrology consult if creatinine rising despite resuscitation

### Hyperkalemia Management (if present)
- Calcium gluconate 30 mL of 10% solution IV over 5 min (membrane stabilization)
- Regular insulin 10 units IV + D50W 50 mL IV (intracellular potassium shift)
- Sodium bicarbonate 50 mEq IV over 5 min
- Kayexalate 15-30 g PO or patiromer 8.4 g PO for ongoing hyperkalemia
- Emergent hemodialysis if refractory hyperkalemia with ECG changes

## Disposition

**ICU Admission (all confirmed NMS):**
- Core temperature >39C
- CK >5,000 IU/L
- Any organ dysfunction (AKI, DIC, respiratory failure)
- Required dantrolene or intubation
- Hemodynamic instability

**Monitored Bed (mild/resolving NMS):**
- Improving rigidity and mental status after offending agent stopped
- CK <5,000 and downtrending
- Stable vital signs on benzodiazepines alone

**Discharge:** Not appropriate from ED. All suspected NMS requires inpatient admission with minimum 48-72 hours of observation. CK must be downtrending, temperature normalized for >24 hours, and rigidity resolved before considering step-down.

**Antipsychotic Rechallenge (post-discharge, by psychiatry):**
- Wait minimum 2 weeks after full NMS resolution
- Use a low-potency or second-generation antipsychotic from a different structural class
- Start at lowest dose with slow titration
- Ensure adequate hydration
- Recurrence risk: 17-30%

## Pitfalls

1. **Attributing NMS features to the psychiatric illness itself.** Fever, rigidity, and altered mental status in a patient on antipsychotics is NMS until proven otherwise. Agitation, catatonia, and "noncompliance" are misdiagnoses that delay recognition and increase mortality.

2. **Administering additional antipsychotics for agitation.** A patient developing NMS who becomes agitated should NOT receive more dopamine antagonists. Use benzodiazepines (lorazepam 1-2 mg IV). Giving haloperidol or droperidol to an NMS patient worsens the syndrome.

3. **Forgetting antiemetics as causative agents.** Metoclopramide, promethazine, and prochlorperazine are dopamine antagonists. NMS occurs with these drugs at standard antiemetic doses, especially in post-surgical or oncology patients who are dehydrated. NMS is not limited to psychiatric medications.

4. **Expecting CK to be elevated on presentation.** CK elevation lags behind clinical onset by 24-48 hours. A normal CK in the first hours does not exclude NMS. Serial CK measurements are required. Clinical tetrad is diagnostic regardless of initial CK level.

5. **Giving antipyretics for NMS fever.** Acetaminophen and NSAIDs are ineffective. NMS hyperthermia results from heat generation by sustained muscle contraction and impaired hypothalamic thermoregulation, not from prostaglandin-mediated fever. Active cooling and treating the rigidity (dantrolene, benzodiazepines) lower temperature.

6. **Stopping bromocriptine too soon.** Abrupt discontinuation of bromocriptine after initial improvement causes NMS rebound. Taper over at least 10 days after all NMS features resolve. Depot antipsychotic-induced NMS requires even longer pharmacotherapy (up to 21 days) due to prolonged drug effect.

7. **Missing NMS from dopamine agonist withdrawal.** NMS occurs in Parkinson disease patients when levodopa, bromocriptine, or amantadine is abruptly stopped (parkinsonism-hyperpyrexia syndrome). The treatment is restarting the dopaminergic agent, not adding a new one.

8. **Confusing NMS with serotonin syndrome.** NMS: lead-pipe rigidity, hyporeflexia, slow onset (days), bradykinesia. Serotonin syndrome: clonus, hyperreflexia, rapid onset (hours), neuromuscular excitability. The treatments differ fundamentally (dopamine agonists vs. cyproheptadine). Misdiagnosis leads to wrong therapy.

9. **Using succinylcholine for intubation.** NMS causes rhabdomyolysis with massive potassium release from damaged muscle. Succinylcholine further depolarizes muscle and worsens hyperkalemia, risking cardiac arrest. Use rocuronium 1.2 mg/kg IV for RSI.

10. **Failing to monitor for renal failure.** Rhabdomyolysis with CK >5,000 IU/L carries significant risk of myoglobin-induced acute tubular necrosis. Aggressive IV hydration targeting urine output >2 mL/kg/hr and serial creatinine monitoring are mandatory. Mortality rises to approximately 50% if NMS is complicated by renal failure.
