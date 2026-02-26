---
id: high-altitude-illness
condition: High-Altitude Illness
aliases: [altitude sickness, mountain sickness, acute mountain sickness, AMS, high-altitude cerebral edema, HACE, high-altitude pulmonary edema, HAPE]
icd10: [T70.20XA, T70.29XA]
esi: 2
time_to_harm: "< 24 hours (HACE — progresses to coma and death)"
mortality_if_delayed: "HACE: near 100% if untreated at altitude; HAPE: 50% mortality if untreated, < 5% with descent and treatment"
category: environmental
track: tier1
sources:
  - type: guideline
    ref: "Wilderness Medical Society Clinical Practice Guidelines for the Prevention and Treatment of Acute Altitude Illness: 2019 Update. Luks AM et al. Wilderness Environ Med 2019;30(4S):S29-S32"
    pmid: "31248818"
  - type: pubmed
    ref: "Hackett PH, Roach RC. High-altitude illness. N Engl J Med 2001;345(2):107-114"
    pmid: "11450659"
  - type: pubmed
    ref: "Bartsch P, Swenson ER. Acute high-altitude illnesses. N Engl J Med 2013;368(24):2294-2302"
    pmid: "23758234"
  - type: pubmed
    ref: "Luks AM et al. Wilderness Medical Society Practice Guidelines for the Prevention and Treatment of Acute Altitude Illness. Wilderness Environ Med 2014;25(4 Suppl):S4-S14"
    pmid: "25498261"
  - type: pubmed
    ref: "Stream JO, Grissom CK. Update on high-altitude pulmonary edema: pathogenesis, prevention, and treatment. Wilderness Environ Med 2008;19(4):293-303"
    pmid: "19099331"
last_updated: "2026-02-18"
compiled_by: agent
risk_tier: B
validation:
  automated_consistency_check: "2026-02-18"
  dose_range_validator: "2026-02-19"
  unit_normalization_check: "2026-02-19"
  cross_file_consistency_check: "2026-02-19"
  citation_presence_check: "2026-02-19"
  duplicate_content_check: "2026-02-19"
  outlier_detection_flag: clear
  schema_version: "2.0"
  provenance_links: []
---
# High-Altitude Illness

## Recognition

**Definition:** Spectrum of illness caused by hypobaric hypoxia at altitude, ranging from benign acute mountain sickness (AMS) to life-threatening high-altitude cerebral edema (HACE) and high-altitude pulmonary edema (HAPE). Typically occurs above 2500 m (8200 ft).

**Acute Mountain Sickness (AMS):**
- Onset 6-12 hours after arrival at altitude
- Headache (required for diagnosis) PLUS one or more: nausea/vomiting, fatigue/weakness, dizziness/lightheadedness, insomnia
- Lake Louise Acute Mountain Sickness Score >= 3 with headache
- Self-limited if descent occurs or altitude is maintained without further ascent
- Risk factors: rapid ascent rate, prior AMS history, residence below 900 m, exertion on arrival

**High-Altitude Cerebral Edema (HACE):**
- Life-threatening progression of AMS
- Hallmark: ataxia (truncal > appendicular) and/or altered mental status
- Confusion, drowsiness, irrational behavior, hallucinations, focal neurologic deficits
- Progresses to obtundation, coma, and death within 24 hours if untreated
- Onset: typically after >= 2 days at altitude; can develop from AMS over hours
- Pathophysiology: vasogenic edema from blood-brain barrier disruption

**High-Altitude Pulmonary Edema (HAPE):**
- Non-cardiogenic pulmonary edema from exaggerated hypoxic pulmonary vasoconstriction
- Most common cause of death from high-altitude illness
- Onset: typically 2-4 days after arrival at altitude
- Early: decreased exercise tolerance, dry cough, dyspnea on exertion
- Progressive: dyspnea at rest, productive cough (pink/frothy sputum), orthopnea, crackles (initially right middle lobe), cyanosis, tachycardia, tachypnea
- Low-grade fever common (do not confuse with pneumonia)
- SpO2 disproportionately low for altitude (< 90% at elevations where 92-94% would be expected)
- Risk factors: rapid ascent, prior HAPE, heavy exertion, cold exposure, genetic susceptibility, pre-existing pulmonary hypertension

## Critical Actions

1. **Recognize HACE and HAPE as life-threatening emergencies.** AMS is benign; HACE and HAPE kill. Any ataxia, altered mental status, or rest dyspnea at altitude mandates immediate action.
2. **Immediate descent** — the single most effective treatment for all forms of altitude illness. Descend at least 300-1000 m (1000-3000 ft). Do not delay descent for any other intervention.
3. **Supplemental oxygen** — administer to maintain SpO2 > 90%. Flow rate 2-4 L/min by nasal cannula; higher flow for HAPE.
4. **Dexamethasone for HACE** — 8 mg IV/IM/PO initial dose, then 4 mg q6h. Temporizing measure; does not replace descent.
5. **Nifedipine for HAPE** — 30 mg extended-release PO q12h. Reduces pulmonary artery pressure.
6. **Portable hyperbaric chamber (Gamow bag)** — pressurize to simulate descent of 1500-2500 m. Use when descent is impossible due to weather, terrain, or patient condition. 2-4 hours per session.
7. **Do NOT administer opioids or sedatives.** These suppress respiratory drive and worsen hypoxia at altitude. Benzodiazepines and opioids are contraindicated.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Carbon monoxide poisoning | Cooking/heating in enclosed tent or shelter at altitude; headache and AMS-like symptoms; CO level on co-oximetry |
| Dehydration/exhaustion | No ataxia, no pulmonary edema; responds to rest and rehydration; may coexist with AMS |
| Hypothermia | Altered mental status and ataxia overlap with HACE; check core temperature; can coexist |
| Pneumonia | Fever, productive cough, crackles; overlaps with HAPE; HAPE improves rapidly with descent/O2, pneumonia does not |
| Viral gastroenteritis | Nausea/vomiting without headache; no altitude-dependent symptom onset |
| Migraine | Headache with aura/photophobia; may be triggered by altitude; no ataxia; responds to triptans |
| Meningitis/encephalitis | Fever, nuchal rigidity, altered mental status; LP if available; does not improve with descent |
| Pulmonary embolism | Dyspnea, pleuritic chest pain, hypoxia; risk increased by dehydration and immobility during travel; does not improve with descent or O2 to same degree |

## Workup

**Diagnosis is clinical. No laboratory or imaging is required in the field setting.**

**In Hospital/ED Setting:**

**Labs:**
- ABG/VBG: respiratory alkalosis (normal at altitude); PaO2 disproportionately low
- CBC: hemoconcentration common at altitude
- BMP: assess renal function (dehydration common)
- BNP/NT-proBNP: low in HAPE (non-cardiogenic); elevated in cardiogenic pulmonary edema
- Troponin: rule out cardiac etiology if indicated
- Procalcitonin: help differentiate HAPE from pneumonia

**Imaging:**
- Chest X-ray (HAPE): patchy, bilateral (often right > left) alveolar infiltrates; no cardiomegaly, no Kerley B lines, no pleural effusions (non-cardiogenic pattern)
- CT head (HACE): white matter edema, particularly in the splenium of the corpus callosum; often normal early
- MRI brain (HACE): T2/FLAIR hyperintensity in the splenium, corpus callosum, and subcortical white matter (more sensitive than CT)
- Echocardiography: elevated pulmonary artery systolic pressure in HAPE; normal LV function

**Clinical Scoring:**
- Lake Louise AMS Score: headache (0-3), GI symptoms (0-3), fatigue (0-3), dizziness (0-3); score >= 3 with headache = AMS
- HACE: AMS + ataxia (heel-to-toe walk) or altered mental status
- HAPE: Lake Louise HAPE score — dyspnea, cough, weakness, chest tightness, crackles, cyanosis, tachypnea, tachycardia

## Treatment

**Acute Mountain Sickness (AMS):**
- Stop ascent. Rest at current altitude.
- Acetazolamide 250 mg PO BID (accelerates acclimatization by inducing bicarbonate diuresis and metabolic acidosis, stimulating ventilation)
- Ibuprofen 600 mg PO q8h or acetaminophen 1000 mg PO q6h for headache
- Ondansetron 4 mg PO/IV for nausea
- Dexamethasone 4 mg PO/IM q6h if symptoms severe or acetazolamide not tolerated
- Descend if symptoms do not improve in 24 hours or worsen

**High-Altitude Cerebral Edema (HACE):**
- Immediate descent — minimum 300-1000 m; continue until symptoms improve
- Dexamethasone 8 mg IV/IM/PO loading dose, then 4 mg IV/IM/PO q6h
- Supplemental O2: 2-4 L/min to maintain SpO2 > 90%
- Gamow bag (portable hyperbaric chamber): inflate to 2 psi for 2-4 hours if descent not immediately possible
- Intubation and mechanical ventilation if GCS <= 8 or airway not protected
- Seizure management: lorazepam 0.1 mg/kg IV (balance respiratory depression risk against seizure control at altitude)
- Acetazolamide 250 mg PO BID as adjunct

**High-Altitude Pulmonary Edema (HAPE):**
- Immediate descent — minimum 300-1000 m
- Supplemental O2: titrate to SpO2 > 90% (most effective single intervention short of descent)
- Nifedipine 30 mg extended-release PO q12h (reduces pulmonary artery pressure)
- CPAP/BiPAP if available: improves oxygenation and may reduce pulmonary edema
- Gamow bag if descent impossible and supplemental O2 unavailable
- Phosphodiesterase-5 inhibitors: sildenafil 50 mg PO q8h or tadalafil 10 mg PO q12h (alternative/adjunct to nifedipine)
- Salmeterol 125 mcg inhaled BID — adjunct only (insufficient as monotherapy)
- Do NOT use diuretics (patient is typically volume-depleted)
- Bed rest; minimize exertion (even walking worsens pulmonary pressures)

**Prevention (for planned ascent):**
- Acetazolamide 125-250 mg PO BID, starting 1 day before ascent
- Gradual ascent: no more than 300-500 m/day of sleeping altitude above 3000 m
- Nifedipine 30 mg ER PO q12h for HAPE-susceptible individuals
- Dexamethasone 4 mg PO q6h for those intolerant of acetazolamide (prophylaxis only; does not aid acclimatization)

## Disposition

**Discharge (descent to lower altitude with follow-up):**
- AMS: improved with descent and/or acetazolamide; reliable follow-up; traveling companion aware of warning signs
- Mild HAPE: rapidly improving with descent and O2; SpO2 > 90% on room air at lower altitude; reliable follow-up within 24 hours

**Admit:**
- HACE: all patients. ICU if GCS <= 12 or requiring intubation. Dexamethasone continuation, serial neurologic exams, MRI brain.
- HAPE with persistent hypoxia: admit for supplemental O2, monitoring, and nifedipine. ICU if requiring CPAP/BiPAP or intubation.
- Any patient with altitude illness who cannot descend and is being managed at altitude — close monitoring mandatory.

**Return to Altitude:**
- After AMS: may re-ascend slowly after complete symptom resolution (24-48 hours at lower altitude)
- After HAPE/HACE: avoid re-ascent for remainder of the trip. Subsequent trips require prophylaxis and gradual ascent.

## Pitfalls

1. **Dismissing headache and malaise at altitude as dehydration or fatigue.** AMS is a clinical diagnosis. Any headache at altitude is AMS until proven otherwise. Failure to recognize early AMS allows progression to HACE.

2. **Delaying descent while waiting for medications to work.** Dexamethasone and nifedipine are temporizing. Descent is definitive. Pharmacotherapy should be administered during descent, not instead of descent.

3. **Administering opioids or benzodiazepines at altitude.** Respiratory depressants worsen hypoxia in an already hypoxic environment. They mask neurologic deterioration. Contraindicated for pain or anxiety management at altitude.

4. **Confusing HAPE with pneumonia and treating with antibiotics alone.** Low-grade fever and crackles at altitude suggest HAPE. HAPE improves dramatically with descent and O2 within hours. If there is any doubt, treat as HAPE (descent + O2 + nifedipine) AND cover for pneumonia, but do not delay descent for antibiotic administration.

5. **Assuming HAPE requires cardiogenic pulmonary edema management.** HAPE is non-cardiogenic. Diuretics worsen hypovolemia. Nitrates and ACE inhibitors are ineffective. Nifedipine reduces pulmonary artery pressure specifically.

6. **Allowing a patient with ataxia to continue ascending or remain at altitude.** Ataxia at altitude = HACE until proven otherwise. This patient will die at altitude without descent. Do not test "watchful waiting."

7. **Using pulse oximetry normal values from sea level.** SpO2 of 88% at 4000 m may be normal acclimatization; SpO2 of 80% at 3000 m is pathologic. Interpret SpO2 relative to expected values for the altitude and compare to companions at the same altitude.

8. **Missing HACE in a patient who appears intoxicated.** Ataxia, confusion, and personality changes from HACE mimic alcohol intoxication. At altitude, altered behavior is HACE until proven otherwise.

9. **Failing to counsel patients about re-ascent.** Patients who had HAPE or HACE are at high risk for recurrence. They require prophylaxis (nifedipine for HAPE, dexamethasone for HACE), gradual ascent, and education about early symptoms.

10. **Not recognizing that HAPE can occur on re-ascent after descent.** Residents of high altitude who descend and then return home (re-entry HAPE) are at risk, particularly children. Any dyspnea or cough during re-ascent should be evaluated for HAPE.
