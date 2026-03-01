---
id: transient-ischemic-attack
condition: Transient Ischemic Attack
aliases: [TIA, mini-stroke, transient cerebral ischemia]
icd10: [G45.0, G45.1, G45.2, G45.3, G45.8, G45.9]
esi: 2
time_to_harm:
  irreversible_injury: "< 48 hours"
  death: "< 7 days"
  optimal_intervention_window: "< 24 hours"
category: neurological
track: tier1
sources:
  - type: guideline
    ref: "Kleindorfer DO et al. 2021 Guideline for the Prevention of Stroke in Patients With Stroke and Transient Ischemic Attack. AHA/ASA. Stroke. 2021;52:e364-e467"
  - type: guideline
    ref: "Easton JD et al. Diagnosis, Workup, Risk Reduction of Transient Ischemic Attack in the Emergency Department Setting. AHA Scientific Statement. Stroke. 2024;55:e54-e76"
  - type: guideline
    ref: "2026 AHA/ASA Guideline for the Early Management of Patients With Acute Ischemic Stroke. Stroke. 2026"
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
# Transient Ischemic Attack (TIA)

## Recognition

**Definition:**
- Transient episode of neurologic dysfunction caused by focal brain, spinal cord, or retinal ischemia without acute infarction on imaging
- Symptoms typically resolve within 1 hour; historical 24-hour cutoff is obsolete
- Up to 50% of patients with "TIA" by symptoms have DWI-positive lesions on MRI (tissue-based definition = stroke)

**Classic presentations:**
- Unilateral motor or sensory deficit (face, arm, leg)
- Aphasia or dysarthria
- Amaurosis fugax (monocular vision loss — retinal TIA)
- Homonymous hemianopia
- Vertigo with other posterior circulation signs (diplopia, dysarthria, ataxia)

**ABCD2 score (risk stratification):**
- Age >= 60 (1 pt), BP >= 140/90 (1 pt), Clinical features: unilateral weakness (2 pts) or speech impairment without weakness (1 pt), Duration >= 60 min (2 pts) or 10-59 min (1 pt), Diabetes (1 pt)
- Score >= 4: high risk (~8% 2-day stroke risk)
- Score 0-3: lower risk but NOT zero risk
- ABCD2 should NOT be used alone to decide disposition

**90-day stroke risk after TIA: up to 17.8%, with ~50% of strokes occurring within 48 hours.**

## Critical Actions

1. **Emergent neuroimaging** — CT head to exclude hemorrhage; MRI with DWI preferred (identifies completed stroke in ~50%)
2. **Start dual antiplatelet therapy (DAPT) within 24 hours** — aspirin 162-325 mg PO loading + clopidogrel 300-600 mg PO loading, then aspirin 81 mg + clopidogrel 75 mg daily for 21-90 days
3. **Vascular imaging within 24 hours** — CTA head/neck or MRA to identify large vessel stenosis; carotid duplex if CTA unavailable
4. **ECG and telemetry** — identify atrial fibrillation (present in ~25% of cryptogenic events)
5. **Initiate high-intensity statin** — atorvastatin 80 mg PO daily
6. **BP management** — do NOT acutely lower BP unless > 220/120; initiate antihypertensive before discharge with target < 130/80

## Differential Diagnosis

- Acute ischemic stroke (persistent deficits, DWI-positive on MRI)
- Seizure with Todd paralysis (postictal confusion, witnessed seizure activity)
- Migraine with aura (younger patient, gradual onset, visual symptoms march)
- Hypoglycemia (check point-of-care glucose immediately)
- Conversion disorder/functional neurologic symptom disorder (inconsistent exam)
- Peripheral vertigo (vertigo without other brainstem signs; HINTS exam negative for central cause)
- Brain tumor (subacute, progressive symptoms)
- Subdural hematoma (elderly, anticoagulation, fall history)

## Workup

- **CT head without contrast** — rule out hemorrhage (immediate)
- **MRI brain with DWI** — gold standard; identifies acute infarct in ~50% of clinical TIAs
- **CTA head and neck** or **MRA** — assess carotid and intracranial vasculature
- **ECG** — atrial fibrillation screen
- **Cardiac telemetry** — minimum 24 hours; consider extended cardiac monitoring (30-day event recorder) if cryptogenic
- **Echocardiogram** — TTE; TEE if PFO or cardiac source suspected
- **Labs:** CBC, BMP, glucose, lipid panel, HbA1c, PT/INR, troponin
- **Point-of-care glucose** — immediate, before imaging

## Treatment

### Antithrombotic Therapy
- **DAPT (non-cardioembolic TIA):** aspirin 162-325 mg PO load + clopidogrel 300 mg PO load, then aspirin 81 mg + clopidogrel 75 mg daily for 21 days (CHANCE/POINT trials); extend to 90 days for high-risk patients
- **Anticoagulation (AF-related TIA):** initiate DOAC within 1-14 days; apixaban 5 mg PO BID (preferred) or rivaroxaban 20 mg PO daily with food
- **Aspirin monotherapy:** aspirin 81 mg PO daily for long-term secondary prevention after DAPT period

### Statin Therapy
- Atorvastatin 80 mg PO daily or rosuvastatin 20-40 mg PO daily
- Start in ED regardless of lipid levels

### Blood Pressure Management
- Do NOT acutely lower BP in ED unless > 220/120 or evidence of end-organ damage
- Start antihypertensive before discharge: lisinopril 10 mg PO daily or amlodipine 5 mg PO daily
- Target < 130/80 mmHg outpatient

### Carotid Stenosis
- Symptomatic carotid stenosis >= 50%: urgent referral for carotid endarterectomy (CEA within 2 weeks)
- CEA preferred over carotid artery stenting for most patients

### Glucose Management
- New diabetes diagnosis: initiate metformin 500 mg PO BID, titrate
- HbA1c target < 7% for secondary stroke prevention

## Disposition

- **Admit (or 24h ED observation):** ABCD2 >= 4, DWI-positive MRI, large vessel stenosis, atrial fibrillation, recurrent TIA, incomplete workup
- **Rapid outpatient pathway (discharge from ED):** ABCD2 0-3, negative MRI-DWI, no large vessel stenosis, no AF, reliable follow-up within 24-48 hours, DAPT and statin started
- **All patients:** neurology follow-up within 7 days; vascular surgery referral if carotid stenosis >= 50%
- **Never discharge without:** antithrombotic therapy, statin, clear stroke warning education, and arranged follow-up

## Pitfalls

1. **Dismissing TIA as benign because symptoms resolved.** The 90-day stroke risk is up to 17.8%, with half of strokes occurring within 48 hours. TIA is a stroke warning — not a reassuring diagnosis.

2. **Using ABCD2 score alone to determine discharge.** The ABCD2 score has moderate sensitivity and should not be the sole determinant of disposition. Large vessel stenosis and AF can be present regardless of score.

3. **Failing to obtain vascular imaging.** Missing a high-grade carotid stenosis delays life-saving CEA. CTA or MRA of head and neck should be obtained within 24 hours.

4. **Missing atrial fibrillation on a single ECG.** Paroxysmal AF may not be present at the time of evaluation. Extended cardiac monitoring (14-30 day event recorder) should be arranged for cryptogenic events.

5. **Not starting DAPT early.** The benefit of dual antiplatelet therapy is greatest in the first 24 hours. Delaying clopidogrel loading reduces the protective effect (CHANCE, POINT trials).

6. **Misdiagnosing migraine with aura as TIA.** Migraine aura typically has positive visual phenomena (scintillations), gradual onset/spread over minutes, and marches across modalities. TIA deficits are sudden-onset and negative (loss of function).
