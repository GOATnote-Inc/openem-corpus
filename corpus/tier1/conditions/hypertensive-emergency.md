---
id: hypertensive-emergency
condition: Hypertensive Emergency
aliases: [hypertensive crisis, malignant hypertension, accelerated hypertension, hypertensive urgency with end-organ damage]
icd10: [I16.1, I16.9, I67.4]
esi: 2
time_to_harm: "< 1 hour"
mortality_if_delayed: "Up to 50% mortality at 12 months if untreated"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "2017 ACC/AHA Guideline for the Prevention, Detection, Evaluation, and Management of High Blood Pressure in Adults"
    doi: "10.1161/HYP.0000000000000065"
  - type: guideline
    ref: "2018 ESC/ESH Guidelines for the management of arterial hypertension"
    doi: "10.1093/eurheartj/ehy339"
  - type: pubmed
    ref: "van den Born BJH et al. ESC Council on hypertension position document on the management of hypertensive emergencies. Eur Heart J Cardiovasc Pharmacother. 2019;5(1):37-46"
    pmid: "30165588"
  - type: pubmed
    ref: "Peixoto AJ. Acute Severe Hypertension. N Engl J Med. 2019;381(19):1843-1852"
    pmid: "31693807"
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
  guideline_version_reference: null
  provenance_links: []
---
# Hypertensive Emergency

## Recognition

**Definition:** Severe blood pressure elevation (typically SBP > 180 and/or DBP > 120 mmHg) with acute target organ damage. The presence of end-organ damage — not the absolute BP number — defines hypertensive emergency.

**End-organ damage syndromes:**
- **Neurological:** Hypertensive encephalopathy (headache, confusion, visual changes, seizures, papilledema), ischemic stroke, hemorrhagic stroke, posterior reversible encephalopathy syndrome (PRES)
- **Cardiovascular:** Acute aortic dissection, acute coronary syndrome, acute decompensated heart failure/pulmonary edema
- **Renal:** Acute kidney injury (rising creatinine, hematuria, proteinuria), thrombotic microangiopathy
- **Ophthalmologic:** Grade III/IV retinopathy (flame hemorrhages, cotton-wool spots, papilledema)
- **Obstetric:** Eclampsia, HELLP syndrome

**Distinguish from hypertensive urgency:**
- Urgency = severely elevated BP WITHOUT end-organ damage
- Urgency does not require IV antihypertensives or ICU admission
- Oral agents and outpatient follow-up within 24-72 hours are sufficient for urgency

## Critical Actions

| Action | Target |
|---|---|
| Focused exam for end-organ damage | < 15 minutes |
| IV antihypertensive initiation | Within 30 minutes of identifying end-organ damage |
| BP reduction | 25% in first hour (except aortic dissection and stroke — see Treatment) |
| Arterial line placement | As soon as feasible for continuous monitoring |

1. **Confirm BP in both arms** with appropriately sized cuff (bladder encircling >= 80% of arm circumference)
2. **Targeted history:** Medication noncompliance, sympathomimetic use (cocaine, amphetamines), pregnancy, prior hypertensive crises
3. **Focused exam:** Neurological status, fundoscopy, cardiac auscultation (S3, murmur of aortic regurgitation), lung auscultation (rales), assess pulses for deficits
4. **Start IV antihypertensive** based on end-organ involvement (see Treatment)
5. **Place arterial line** for continuous BP monitoring
6. **Do NOT reduce BP too rapidly** — ischemic stroke and renal infarction from overshoot

## Differential Diagnosis

- Hypertensive urgency (no end-organ damage)
- Secondary hypertension: pheochromocytoma, renal artery stenosis, primary aldosteronism, Cushing syndrome
- Sympathomimetic toxicity (cocaine, methamphetamine, PCP)
- Serotonin syndrome
- Medication withdrawal (clonidine rebound)
- Thyroid storm
- Pre-eclampsia/eclampsia
- Autonomic dysreflexia (in spinal cord injury patients)
- Intracranial pathology causing Cushing reflex (hypertension + bradycardia)
- Aortic coarctation

## Workup

- **CBC with peripheral smear:** Schistocytes suggest thrombotic microangiopathy
- **BMP:** Creatinine (AKI), potassium (secondary causes), bicarbonate
- **Urinalysis:** Proteinuria, hematuria, RBC casts (renal end-organ damage)
- **Troponin:** Rule out demand ischemia or ACS
- **BNP/NT-proBNP:** If heart failure suspected
- **ECG:** LVH, ischemia, strain pattern
- **Chest X-ray:** Pulmonary edema, mediastinal widening (dissection)
- **CT head without contrast:** If neurological symptoms (encephalopathy, focal deficits, seizures)
- **CT angiography of aorta:** If aortic dissection suspected (tearing chest/back pain, pulse differential, widened mediastinum)
- **Fundoscopic exam:** Papilledema, hemorrhages, exudates
- **Urine drug screen:** Cocaine, amphetamines
- **Pregnancy test** in women of reproductive age
- **LDH, haptoglobin, reticulocyte count** if microangiopathic hemolytic anemia suspected

## Treatment

### General Principle
Reduce MAP by no more than 25% in the first hour, then to 160/100 mmHg over the next 2-6 hours. Exceptions below.

### Hypertensive Encephalopathy / General Hypertensive Emergency
- **Nicardipine** 5 mg/hr IV, titrate by 2.5 mg/hr q5-15min (max 15 mg/hr) — preferred first-line
- **Clevidipine** 1-2 mg/hr IV, titrate by doubling q90sec (max 32 mg/hr short-term; average ≤ 21 mg/hr over 24h due to lipid load) — ultra-short acting
- **Labetalol** 20 mg IV bolus, then 40 mg, then 80 mg q10min (max 300 mg total); infusion 0.5-2 mg/min

### Acute Aortic Dissection
- **Target HR < 60 bpm FIRST, then SBP 100-120 mmHg within 20 minutes**
- Esmolol 500 mcg/kg IV bolus, then 50-200 mcg/kg/min infusion (first-line, titratable)
- Add nicardipine or nitroprusside AFTER beta-blocker achieves rate control
- **NEVER give vasodilators before beta-blocker** — reflex tachycardia increases aortic shear stress

### Acute Pulmonary Edema / Heart Failure
- Nitroglycerin 20-200 mcg/min IV for hypertensive pulmonary edema (potent venodilator, reduces preload; start higher than generic 5 mcg/min — titrate aggressively)
- Nicardipine 5-15 mg/hr IV
- Clevidipine 1-32 mg/hr IV (average ≤ 21 mg/hr over 24h)
- Add furosemide 40-80 mg IV for volume overload
- Avoid labetalol in acute decompensated HF (negative inotropy)

### Acute Ischemic Stroke
- Treat only if SBP > 220 or DBP > 120 mmHg (unless thrombolytic candidate)
- If tPA candidate: lower to < 185/110 mmHg before tPA, maintain < 180/105 for 24 hours post-tPA
- Nicardipine or labetalol; avoid nitroprusside (raises ICP)

### Intracerebral Hemorrhage
- Target SBP 140 mmHg (INTERACT2, ATACH-2 trials)
- Nicardipine or clevidipine first-line

### Sympathomimetic Crisis (Cocaine, Amphetamine)
- Benzodiazepines first-line: diazepam 5-10 mg IV q5-10min or lorazepam 2-4 mg IV
- Nicardipine or nitroglycerin for persistent hypertension
- Phentolamine 5 mg IV for refractory cases
- **Avoid beta-blockers** — unopposed alpha stimulation worsens hypertension

### Eclampsia/Pre-eclampsia
- Magnesium sulfate 4-6 g IV over 15-20 minutes, then 1-2 g/hr infusion (seizure prophylaxis and treatment)
- Labetalol 20 mg IV, escalating doses; OR hydralazine 5 mg IV q20min; OR nicardipine 5-15 mg/hr
- Target SBP < 160, DBP < 110
- Delivery is definitive treatment

## Disposition

- **ICU admission:** All hypertensive emergencies require continuous BP monitoring (arterial line) and IV antihypertensive infusion
- **Step-down/telemetry:** Once BP controlled on oral agents for 6-12 hours
- **Transition to oral agents:** Overlap IV and oral medications; common oral agents include amlodipine 5-10 mg PO daily, lisinopril 10-20 mg PO daily, labetalol 200 mg PO BID
- **Discharge:** Never discharge an active hypertensive emergency; hypertensive urgency can be discharged with oral agents and 24-72 hour follow-up
- **Nephrology consultation** if AKI or microangiopathy
- **Neurosurgery** if intracranial hemorrhage

## Pitfalls

1. **Dropping blood pressure too fast.** Rapid BP reduction causes watershed ischemic stroke, coronary ischemia, and renal cortical necrosis. Target 25% MAP reduction in the first hour — not normalization.

2. **Treating the number, not the patient.** SBP 200 without end-organ damage is hypertensive urgency, not emergency. Oral agents and follow-up are appropriate. Unnecessary IV antihypertensives and ICU admission waste resources and risk iatrogenic hypotension.

3. **Giving sublingual nifedipine.** Sublingual nifedipine causes unpredictable, precipitous BP drops and has been associated with stroke and MI. It has no role in hypertensive management.

4. **Failing to obtain a CT head in encephalopathic hypertensive patients.** Hypertensive encephalopathy is a diagnosis of exclusion. Intracerebral hemorrhage, subarachnoid hemorrhage, and ischemic stroke must be ruled out — treatment differs substantially.

5. **Giving vasodilators before beta-blockers in aortic dissection.** Vasodilators cause reflex tachycardia that increases aortic wall shear stress and propagates the dissection. Esmolol first, then add vasodilator.

6. **Using beta-blockers for cocaine-induced hypertensive emergency.** Beta-blockade causes unopposed alpha-adrenergic stimulation, worsening hypertension and coronary vasoconstriction. Benzodiazepines are first-line; phentolamine for refractory cases.

7. **Ignoring the underlying cause.** Medication noncompliance, cocaine use, pheochromocytoma, renal artery stenosis, pregnancy, and clonidine withdrawal all require specific interventions beyond BP reduction.

8. **Using nitroprusside without monitoring for cyanide toxicity.** Nitroprusside infusions > 2 mcg/kg/min for > 24 hours accumulate cyanide. Monitor thiocyanate levels. Prefer nicardipine or clevidipine when available.

9. **Discharging without a clear antihypertensive regimen and follow-up.** Recurrent hypertensive emergencies are common. Ensure medication reconciliation, adherence plan, and primary care follow-up within 72 hours.
