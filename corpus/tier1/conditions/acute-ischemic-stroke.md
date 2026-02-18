---
id: acute-ischemic-stroke
condition: Acute Ischemic Stroke
aliases: [AIS, ischemic stroke, cerebrovascular accident, CVA, brain attack]
icd10: [I63.9, I63.5, I63.3, I63.4]
esi: 1
time_to_harm: "< 4.5 hours for IV tPA; < 24 hours for thrombectomy"
mortality_if_delayed: "1.9 million neurons lost per minute of untreated large vessel occlusion"
category: neurological
track: tier1
sources:
  - type: guideline
    ref: "2019 AHA/ASA Guidelines for the Early Management of Acute Ischemic Stroke"
  - type: guideline
    ref: "2018 AHA/ASA Guidelines for the Management of Acute Ischemic Stroke (Updated)"
  - type: guideline
    ref: "2015 AHA/ASA Focused Update on Endovascular Therapy"
  - type: guideline
    ref: "NINDS rt-PA Stroke Study, ECASS III, DAWN, and DEFUSE 3 Trials"
last_updated: "2026-02-18"
compiled_by: agent
reviewed_by: null
---

# Acute Ischemic Stroke

## Recognition

**Acute onset of focal neurological deficit:**
- Unilateral weakness or numbness (face, arm, leg)
- Speech disturbance (aphasia, dysarthria)
- Visual field cut, diplopia
- Ataxia, vertigo, gait instability
- Neglect, confusion, decreased level of consciousness

**Last known well (LKW):** The critical time anchor. If onset during sleep, LKW = time patient last seen normal.

**NIHSS assessment:** Perform immediately; drives treatment decisions.
- 0-4: minor stroke
- 5-15: moderate stroke
- 16-20: moderate-severe stroke
- 21-42: severe stroke

**Rapid stroke screen (prehospital/triage):**
- Cincinnati Stroke Scale: facial droop, arm drift, speech abnormality
- Any one finding = 72% probability of stroke

**Large vessel occlusion (LVO) screening:**
- NIHSS >= 6 with cortical signs (gaze deviation, neglect, aphasia)
- RACE scale >= 5 or LAMS >= 4 suggest LVO

## Critical Actions

| Action | Target |
|---|---|
| Door-to-CT | < 25 minutes |
| Door-to-needle (IV alteplase) | < 60 minutes |
| Door-to-groin puncture (thrombectomy) | < 90 minutes |
| Stroke team notification | Immediate at triage |

1. **ABCs and stabilize** — do not lower BP unless > 220/120 (or > 185/110 if tPA candidate)
2. **Fingerstick glucose** — hypoglycemia mimics stroke; treat if < 60 mg/dL
3. **Non-contrast CT head STAT** — rule out hemorrhage
4. **CT angiography (CTA) head and neck** — identify LVO for thrombectomy candidacy
5. **CT perfusion** if LKW > 6 hours or wake-up stroke (identify salvageable penumbra)
6. **IV alteplase** if eligible (see Treatment)
7. **Activate neurointerventional team** if LVO identified on CTA
8. **NPO** until swallow screen completed

## Differential Diagnosis

- Hypoglycemia (check glucose immediately)
- Todd's paralysis (postictal; ask about seizure activity)
- Complex migraine with aura (headache, visual symptoms, gradual onset)
- Intracranial hemorrhage (CT differentiates)
- Brain tumor/mass lesion (subacute onset, CT/MRI)
- Hypertensive encephalopathy (severely elevated BP, papilledema)
- Conversion disorder/functional neurological symptom disorder
- Posterior reversible encephalopathy syndrome (PRES)
- Cerebral venous sinus thrombosis (headache, papilledema, seizures)
- Aortic dissection with carotid extension

## Workup

- **Non-contrast CT head:** Must precede tPA; rules out hemorrhage
- **CTA head and neck:** Identify LVO (ICA, M1, M2, basilar occlusion)
- **CT perfusion:** Mismatch between core infarct and penumbra guides extended-window treatment (DAWN/DEFUSE 3 criteria)
- **MRI DWI/FLAIR:** Mismatch helpful for wake-up strokes; do NOT delay tPA for MRI
- **Labs:** Glucose (STAT, fingerstick), CBC, BMP, coagulation studies (PT/INR, aPTT), troponin
  - Only glucose result needed before tPA; other labs can result after administration unless clinical suspicion of coagulopathy
- **ECG:** Identify atrial fibrillation or acute MI as embolic source
- **Swallow screen:** Before any oral intake

## Treatment

### IV Thrombolysis (Alteplase)

**Eligibility:** Age >= 18, measurable neurological deficit, CT without hemorrhage

**Alteplase 0.9 mg/kg IV (max 90 mg):**
- 10% as IV bolus over 1 minute
- Remaining 90% infused over 60 minutes

**Time windows:**
- 0-3 hours from LKW: standard indication
- 3-4.5 hours from LKW: eligible per ECASS III with additional exclusions (age > 80, NIHSS > 25, oral anticoagulant use regardless of INR, history of both diabetes and prior stroke)

**Tenecteplase (emerging alternative):**
- 0.25 mg/kg IV single bolus (max 25 mg)
- Non-inferior to alteplase for LVO stroke per AcT trial
- Simpler administration (single bolus vs. 1-hour infusion)

**Key absolute contraindications:**
- Intracranial hemorrhage on CT
- Active internal bleeding
- Platelet count < 100,000
- INR > 1.7 or PT > 15 seconds
- aPTT elevated (if on heparin)
- DOAC use within 48 hours with abnormal drug-specific coag assay (or unknown timing)
- Blood glucose < 50 mg/dL
- Intracranial surgery/serious head trauma within 3 months
- GI/GU hemorrhage within 21 days
- Arterial puncture at non-compressible site within 7 days

### Blood Pressure Management

**Pre-tPA targets:**
- Must lower to < 185/110 before administering alteplase
- Labetalol 10-20 mg IV over 1-2 minutes (may repeat x1)
- OR nicardipine 5 mg/hr IV, titrate by 2.5 mg/hr q5-15min (max 15 mg/hr)
- OR clevidipine 1-2 mg/hr IV, titrate

**During and 24h post-tPA:**
- Maintain BP < 180/105
- Same agents as above

**Non-tPA candidates:**
- Permissive hypertension up to 220/120
- Treat only if > 220/120 or end-organ damage (aortic dissection, acute HF, hypertensive encephalopathy)
- Lower by 15% in the first 24 hours

### Mechanical Thrombectomy

**Eligibility (0-6 hours from LKW):**
- LVO (ICA, M1) confirmed on CTA
- NIHSS >= 6
- Pre-stroke mRS 0-1
- ASPECTS >= 6 on CT
- Age >= 18

**Extended window (6-24 hours from LKW):**
- DAWN criteria: clinical-imaging mismatch (NIHSS >= 10 with small core)
- DEFUSE 3 criteria: perfusion mismatch ratio >= 1.8, core < 70 mL, mismatch volume >= 15 mL
- CTP or MRI required to determine eligibility

**IV tPA should NOT be withheld or delayed to pursue thrombectomy.** Administer tPA first, then proceed to thrombectomy (bridging therapy).

### Supportive Care
- Normothermia: treat temperature > 38C with acetaminophen 650-1000 mg
- Euglycemia: target glucose 140-180 mg/dL; insulin for > 180 mg/dL
- Isotonic IV fluids (NS); avoid hypotonic solutions (cerebral edema risk)
- Head of bed 0 degrees (flat) unless risk of aspiration or elevated ICP
- DVT prophylaxis: pneumatic compression devices (hold chemical prophylaxis 24h post-tPA)

## Disposition

- **All acute strokes:** Stroke unit or neuro-ICU admission
- **Post-tPA patients:** ICU-level monitoring for 24 hours minimum; no antiplatelets/anticoagulants for 24 hours; repeat CT before starting
- **Large territory infarcts (e.g., complete MCA):** ICU for malignant edema monitoring; neurosurgery consult for possible decompressive craniectomy (age < 60, within 48h of symptom onset per DESTINY II, DECIMAL, HAMLET trials)
- **Posterior fossa strokes:** ICU; risk of obstructive hydrocephalus, herniation
- **Transfer:** If no endovascular capability and LVO identified, transfer to comprehensive stroke center immediately; continue tPA infusion during transport

## Pitfalls

1. **Treating the blood pressure too aggressively in non-tPA candidates.** Permissive hypertension up to 220/120 maintains perfusion through collaterals. Dropping the BP precipitously extends the infarct.

2. **Waiting for all lab results before giving tPA.** Only a fingerstick glucose is required before administration. CBC and coags can result afterward unless there is clinical suspicion of thrombocytopenia or coagulopathy (e.g., known warfarin use, liver disease).

3. **Dismissing posterior circulation stroke.** Vertigo, ataxia, diplopia, and dysarthria without limb weakness are frequently attributed to benign causes. Basilar artery occlusion has > 80% mortality if untreated. CTA is mandatory when posterior stroke is suspected.

4. **Excluding patients from thrombectomy based on NIHSS alone.** LVO with low NIHSS (< 6) can rapidly deteriorate. Obtain CTA for any suspected stroke with cortical signs.

5. **Not obtaining CTA simultaneously with non-contrast CT.** Single-pass CT/CTA protocols save critical minutes. CTA should not be a separate decision point delayed after the initial CT.

6. **Misidentifying stroke mimics as contraindications to tPA.** The risk of tPA in stroke mimics is extremely low (< 1% symptomatic ICH). When in doubt and within the window, treat.

7. **Ignoring wake-up strokes as untreatable.** CT perfusion or MRI DWI-FLAIR mismatch can identify candidates for both tPA (per WAKE-UP trial) and thrombectomy (per DAWN/DEFUSE 3) well beyond traditional time windows.
