---
id: hemorrhagic-stroke
condition: Hemorrhagic Stroke (Intracerebral Hemorrhage)
aliases: [ICH, intracerebral hemorrhage, hemorrhagic CVA, cerebral hemorrhage, brain hemorrhage, hypertensive hemorrhage]
icd10: [I61.9, I61.0, I61.1, I61.2, I61.3, I61.4, I61.5]
esi: 1
time_to_harm:
  irreversible_injury: "< 1 hour (hematoma expansion)"
  death: "< 24 hours (30-day mortality 30-50%)"
  optimal_intervention_window: "< 60 minutes to BP control; < 4 hours for anticoagulation reversal"
mortality_if_delayed: "30-day mortality 30-50%; 1-year mortality 50-60%; hematoma expansion occurs in 38% within 3 hours"
category: neurological
track: tier1
sources:
  - type: guideline
    ref: "Greenberg SM, Ziai WC, Cordonnier C, et al. 2022 Guideline for the Management of Patients With Spontaneous Intracerebral Hemorrhage: A Guideline From the American Heart Association/American Stroke Association. Stroke. 2022;53(7):e282-e361."
    pmid: "35579034"
  - type: pubmed
    ref: "Anderson CS, Heeley E, Huang Y, et al. Rapid blood-pressure lowering in patients with acute intracerebral hemorrhage (INTERACT2). N Engl J Med. 2013;368(25):2355-2365."
    pmid: "23713578"
  - type: pubmed
    ref: "Qureshi AI, Palesch YY, Barsan WG, et al. Intensive blood-pressure lowering in patients with acute cerebral hemorrhage (ATACH-2). N Engl J Med. 2016;375(11):1033-1043."
    pmid: "27276234"
  - type: pubmed
    ref: "Hemphill JC, Greenberg SM, Anderson CS, et al. Guidelines for the Management of Spontaneous Intracerebral Hemorrhage: A Guideline for Healthcare Professionals From the American Heart Association/American Stroke Association. Stroke. 2015;46(7):2032-2060."
    pmid: "26022637"
  - type: pubmed
    ref: "Mayer SA, Brun NC, Begtrup K, et al. Efficacy and safety of recombinant activated factor VII for acute intracerebral hemorrhage (FAST trial). N Engl J Med. 2008;358(20):2127-2137."
    pmid: "18480205"
  - type: pubmed
    ref: "Steiner T, Poli S, Griebe M, et al. Fresh frozen plasma versus prothrombin complex concentrate in patients with intracranial haemorrhage related to vitamin K antagonists (INCH): a randomised trial. Lancet Neurol. 2016;15(6):566-573."
    pmid: "27302126"
confusion_pairs:
  - condition: acute-ischemic-stroke
    differentiators:
      - "CT head is mandatory: ICH shows hyperdense (white) lesion; ischemic stroke is hypodense (dark) or normal on early CT"
      - "Clinical exam alone cannot reliably distinguish hemorrhagic from ischemic stroke — CT before any treatment"
      - "ICH: more likely with anticoagulant use, severe hypertension (SBP >220), and rapid deterioration in level of consciousness"
      - "ICH: headache, vomiting, and early decreased consciousness more common than in ischemic stroke"
      - "Giving tPA to an ICH patient is catastrophic — CT must precede thrombolysis"
  - condition: subarachnoid-hemorrhage
    differentiators:
      - "ICH: intraparenchymal hyperdensity on CT; SAH: blood in subarachnoid cisterns and sulci"
      - "SAH: thunderclap headache onset; ICH: progressive headache with focal deficit"
      - "SAH: often aneurysmal (CTA shows aneurysm); ICH: hypertensive, amyloid, or coagulopathic"
      - "SAH: meningeal signs (neck stiffness, photophobia); ICH: focal neurological deficit matching hemorrhage location"
last_updated: "2026-02-26"
compiled_by: agent
reviewed_by: "Brandon Dent, MD — Board Certified Emergency Medicine"
review_date: "2026-02-27"
risk_tier: A
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
# Hemorrhagic Stroke (Intracerebral Hemorrhage)

## Recognition

**Definition:** Spontaneous (non-traumatic) bleeding into the brain parenchyma, with or without extension into the ventricles. Accounts for 10-15% of all strokes but causes 40-50% of stroke-related deaths.

**Etiology by location:**

| Location | Most Common Etiology |
|----------|---------------------|
| Basal ganglia (putamen, caudate) | Hypertensive vasculopathy (lenticulostriate arteries) |
| Thalamus | Hypertensive vasculopathy (thalamoperforating arteries) |
| Pons/cerebellum | Hypertensive vasculopathy (pontine perforators, superior cerebellar artery) |
| Lobar (frontal, temporal, parietal, occipital) | Cerebral amyloid angiopathy (elderly), AVM, cavernoma, tumor |

**Risk factors:**
- Hypertension (most common modifiable risk factor — present in 55-80%)
- Anticoagulant therapy (warfarin, DOACs — 12-20% of all ICH)
- Antiplatelet therapy (aspirin, clopidogrel)
- Cerebral amyloid angiopathy (elderly, recurrent lobar hemorrhages)
- Cocaine/amphetamine use
- Arteriovenous malformations (younger patients)
- Brain tumors (melanoma, renal cell carcinoma, choriocarcinoma metastases)
- Coagulopathy (thrombocytopenia, liver disease, DIC)
- Cerebral venous sinus thrombosis (hemorrhagic venous infarction)

**Clinical presentation:**
- Acute onset focal neurological deficit with progressive worsening over minutes to hours (unlike ischemic stroke which is maximal at onset)
- Headache (40-50%) — more common than in ischemic stroke
- Vomiting (40-50%) — due to elevated ICP
- Decreased level of consciousness (50-60%) — early obtundation suggests large hemorrhage, brainstem compression, or intraventricular extension
- Seizures (5-15%) — more common in lobar hemorrhages
- Focal signs depend on location: contralateral hemiparesis (basal ganglia/internal capsule), contralateral sensory loss with downgaze palsy (thalamus), ataxia/vertigo/vomiting with ipsilateral facial weakness (cerebellum), quadriplegia/coma (pons)

**ICH Score (prognostic — predicts 30-day mortality):**

| Component | Criteria | Points |
|-----------|----------|--------|
| GCS 3-4 | — | 2 |
| GCS 5-12 | — | 1 |
| GCS 13-15 | — | 0 |
| ICH volume >=30 mL | — | 1 |
| ICH volume <30 mL | — | 0 |
| IVH present | — | 1 |
| Infratentorial origin | — | 1 |
| Age >=80 | — | 1 |

| ICH Score | 30-day Mortality |
|-----------|-----------------|
| 0 | 0% |
| 1 | 13% |
| 2 | 26% |
| 3 | 72% |
| 4 | 97% |
| 5-6 | 100% |

**Hematoma expansion:** Occurs in 38% of patients within 3 hours of onset. The "spot sign" on CTA (active contrast extravasation within the hematoma) predicts expansion with 91% sensitivity. Expansion is the most modifiable determinant of outcome.

## Critical Actions

1. **Non-contrast CT head STAT.** This is the single most critical action — differentiates ICH from ischemic stroke. ICH appears as hyperdense (white) lesion. CT before any treatment decision.
2. **CTA head (simultaneously with NCCT if possible).** Identifies spot sign (predicts hematoma expansion), underlying vascular malformation (AVM, aneurysm), and venous sinus thrombosis.
3. **Blood pressure reduction to <140 mmHg SBP within 1 hour.** Target: SBP 130-150 mmHg. INTERACT2 demonstrated improved functional outcomes with intensive lowering.
   - Nicardipine 5 mg/hr IV, titrate by 2.5 mg/hr q5-15min (max 15 mg/hr) — first-line
   - OR clevidipine 1-2 mg/hr IV, double q90sec to max 21 mg/hr
   - OR labetalol 10-20 mg IV q10min (max 300 mg), then 2-8 mg/min infusion
4. **Reverse anticoagulation immediately.** Do NOT wait for INR/coag results if anticoagulant use is known.
5. **Neurosurgery consultation** — all ICH patients. Evaluate for surgical evacuation (see Treatment).
6. **Protect the airway.** Intubate for GCS <8, loss of protective airway reflexes, or respiratory failure. Avoid hypoxia (target SpO2 >94%) and hyperventilation (target PaCO2 35-40 mmHg).
7. **Seizure management.** Treat clinical seizures with levetiracetam 1500 mg IV (first-line; does not affect coagulation) or fosphenytoin 20 mg PE/kg IV. Prophylactic antiepileptics NOT recommended (AHA 2022).
8. **Elevate head of bed to 30 degrees** — reduces ICP without compromising cerebral perfusion.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Acute ischemic stroke | CT: hypodense or normal (not hyperdense); maximal deficit at onset (not progressive); eligible for tPA if within window and no hemorrhage on CT |
| Subarachnoid hemorrhage | CT: blood in subarachnoid space (cisterns, sulci, fissures) not parenchyma; thunderclap headache; meningeal signs; CTA may show aneurysm |
| Subdural hematoma | CT: crescent-shaped extra-axial hyperdensity (acute) or hypodensity (chronic) along convexity; history of trauma or anticoagulation |
| Epidural hematoma | CT: lens-shaped (biconvex) extra-axial hyperdensity; temporal bone fracture; lucid interval |
| Brain tumor with hemorrhage | CT: hemorrhage within or surrounding mass; ring enhancement on contrast CT; edema disproportionate to hemorrhage volume; known malignancy |
| Cerebral venous sinus thrombosis | CT: hemorrhage not conforming to arterial territory; "dense triangle" sign (thrombosed sinus); CTV/MRV diagnostic |
| Hemorrhagic transformation of ischemic stroke | CT: hemorrhage within an established ischemic infarct territory; prior ischemic event; post-tPA timing |
| Hypertensive encephalopathy | Posterior-predominant vasogenic edema on MRI (PRES); no hemorrhage on CT (unless complicated); severely elevated BP |

## Workup

**Emergent imaging:**
- **Non-contrast CT head:** Diagnostic — hyperdense lesion with surrounding edema. Identifies location, volume (ABC/2 method: A = largest diameter in cm, B = perpendicular diameter, C = number of 1-cm slices with hemorrhage, all divided by 2), intraventricular extension, hydrocephalus, midline shift.
- **CTA head and neck:** Spot sign (active contrast extravasation = high risk of expansion). Identifies underlying vascular lesion (AVM, aneurysm, dural AV fistula, moyamoya).
- **CT venography:** If venous sinus thrombosis suspected (hemorrhage location atypical for hypertensive ICH, young patient, no risk factors).
- **MRI brain (non-emergent):** Microbleeds (GRE/SWI sequences) indicate cerebral amyloid angiopathy (lobar pattern) or hypertensive vasculopathy (deep pattern). Identifies underlying tumor. Can be deferred to after acute stabilization.

**Labs:**
- **CBC** — platelet count (thrombocytopenia as cause; transfusion target >100,000 for ICH)
- **Coagulation studies** — PT/INR (warfarin), aPTT (heparin), anti-Xa level (DOACs), thrombin time (dabigatran)
- **BMP** — renal function (contrast planning, drug dosing), electrolytes
- **Glucose** — hypo/hyperglycemia correction (target 140-180 mg/dL)
- **Troponin** — neurogenic myocardial injury (catecholamine surge)
- **Type and screen** — anticipate FFP/PCC/platelet transfusion
- **Toxicology screen** — cocaine, amphetamines (young patients with unexplained ICH)
- **Liver function tests** — coagulopathy from hepatic dysfunction

## Treatment

### Blood Pressure Management

**Target SBP 130-150 mmHg (AHA 2022):**
- INTERACT2: intensive lowering to <140 improved functional outcomes vs. <180
- ATACH-2: intensive lowering to 110-139 did NOT improve outcomes vs. 140-179 and increased renal adverse events
- Consensus: target SBP 130-150 mmHg; avoid SBP <130 (risk of renal injury)

**Agents:**
- **Nicardipine** 5 mg/hr IV, titrate by 2.5 mg/hr q5-15min (max 15 mg/hr) — first-line; predictable dose-response
- **Clevidipine** 1-2 mg/hr IV, double q90sec (max 21 mg/hr) — ultra-short acting; alternative first-line
- **Labetalol** 10-20 mg IV bolus q10min (max 300 mg), then 2-8 mg/min — avoid in heart block, severe bradycardia, or acute HF
- Avoid nitroprusside (raises ICP via cerebral vasodilation)
- Avoid hydralazine (unpredictable response, long duration, raises ICP)

### Anticoagulation Reversal

**Warfarin (target INR <1.4 within 4 hours):**
- **4-factor PCC (Kcentra):** 25-50 units/kg IV (dose by INR: INR 2-4 = 25 units/kg, INR 4-6 = 35 units/kg, INR >6 = 50 units/kg). Onset 10-15 minutes. First-line (faster and more effective than FFP per INCH trial).
- **Vitamin K** 10 mg IV (infuse over 10 minutes to reduce anaphylactoid risk). Takes 6-24 hours for effect but prevents INR rebound after PCC wears off. Give concurrently with PCC.
- FFP 10-15 mL/kg only if PCC unavailable (slow onset, volume overload risk, incomplete reversal).

**Dabigatran:**
- **Idarucizumab (Praxbind)** 5 g IV (two 2.5 g boluses, max 15 minutes apart). Complete reversal within minutes. First-line.
- If unavailable: 4-factor PCC 50 units/kg IV (off-label, partial reversal) or hemodialysis (removes 60% in 2 hours).

**Rivaroxaban/apixaban/edoxaban (factor Xa inhibitors):**
- **Andexanet alfa (Andexxa):** Low dose (400 mg bolus at 30 mg/min then 4 mg/min x 120 min) if last dose >=8h ago or apixaban <=5 mg; high dose (800 mg bolus then 8 mg/min x 120 min) if last dose <8h ago or higher doses. Onset within minutes.
- If unavailable: **4-factor PCC 50 units/kg IV** (off-label but widely used; reasonable efficacy).
- Activated charcoal 50 g PO if DOAC ingested within 2 hours.

**Heparin:**
- **Protamine sulfate:** 1 mg per 100 units of heparin given in last 2-3 hours (max 50 mg). Slow IV push over 10 minutes. For LMWH: 1 mg protamine per 1 mg enoxaparin given in last 8 hours (60% reversal).

**Antiplatelet-related ICH:**
- **Platelet transfusion:** 1 apheresis unit (single donor). Role is controversial; PATCH trial showed harm with platelet transfusion in spontaneous ICH on antiplatelets. Reserve for patients requiring surgical evacuation.
- **Desmopressin (DDAVP):** 0.3 mcg/kg IV — improves platelet function within 30 minutes regardless of antiplatelet agent. Give empirically for antiplatelet-related ICH.

### Surgical Evacuation

**Indications for emergent surgery:**
- **Cerebellar hemorrhage >3 cm** or with brainstem compression or hydrocephalus — emergent posterior fossa decompression. This is the strongest surgical indication in ICH.
- **Superficial lobar hemorrhage >30 mL** with clinical deterioration — craniotomy for clot evacuation (STICH II showed trend toward benefit for superficial lobar ICH within 1 cm of surface)
- **Intraventricular hemorrhage with hydrocephalus** — external ventricular drain (EVD) placement

**Minimally invasive approaches:**
- Stereotactic catheter-based clot aspiration (MISTIE III): reduced hematoma volume but did not achieve primary endpoint of improved functional outcome; post-hoc analysis showed benefit when >70% of clot removed
- Endoscopic evacuation: emerging evidence (ENRICH trial — lobar and anterior basal ganglia ICH)

**Contraindications to surgery:**
- Deep-seated hemorrhages (basal ganglia, thalamus) — craniotomy causes more harm than benefit (STICH I)
- Devastating hemorrhage with brainstem reflexes absent and GCS 3-4 (unless cerebellar)
- Severe coagulopathy (correct before OR)

### ICP Management

- Head of bed elevation to 30 degrees
- Osmotic therapy for acute herniation: **mannitol 1-1.5 g/kg IV** bolus (20% solution) OR **hypertonic saline 23.4% 30 mL IV** bolus through central line (osmolarity 8,000 mOsm/L — must use CVC)
- EVD for intraventricular hemorrhage with hydrocephalus (target ICP <22 mmHg, CPP >60 mmHg)
- Avoid hyperthermia (target normothermia; acetaminophen 1000 mg IV/PO q6h for temp >38C; cooling blanket if refractory)
- Avoid hyperglycemia (insulin drip for glucose >180 mg/dL; target 140-180 mg/dL)
- Seizure treatment (not prophylaxis): levetiracetam 1500 mg IV load, then 1000 mg IV q12h

### VTE Prophylaxis

- Pneumatic compression devices from admission (mechanical prophylaxis)
- Subcutaneous heparin (UFH 5000 units SC q8h or enoxaparin 40 mg SC daily) — initiate 24-48 hours after hemorrhage if stable imaging (no expansion on repeat CT at 24h). AHA 2022 recommends starting within 48 hours.

## Disposition

**Neurocritical care ICU (all ICH patients):**
- Continuous arterial BP monitoring (arterial line)
- Neurological checks q1h (GCS, pupil reactivity, motor exam)
- Repeat NCCT at 6 hours and 24 hours (detect hematoma expansion)
- ICP monitoring if EVD placed or clinical concern for herniation
- Minimum 24-48 hours ICU monitoring

**Neurosurgery OR:**
- Cerebellar hemorrhage >3 cm — emergent posterior fossa decompression
- Lobar hemorrhage with progressive deterioration
- EVD placement for obstructive hydrocephalus

**Transfer to neurocritical care facility:**
- If presenting hospital lacks neurosurgery and neurocritical care
- Initiate BP control, anticoagulation reversal, and airway management before transfer
- Do NOT delay reversal agents or BP management for transfer

**Palliative care consultation:**
- ICH Score >=4 (97-100% 30-day mortality)
- Discuss goals of care early — avoid premature withdrawal of care in the first 24-48 hours (self-fulfilling prophecy of DNR orders in ICH is well documented)

## Pitfalls

1. **Administering tPA to a hemorrhagic stroke.** Non-contrast CT MUST precede thrombolysis. Clinical examination cannot distinguish hemorrhagic from ischemic stroke. tPA in ICH is catastrophic — converts a contained hemorrhage into a rapidly expanding one.

2. **Delaying anticoagulation reversal while waiting for INR results.** If a patient on warfarin or a DOAC presents with ICH, administer the appropriate reversal agent immediately based on known medication history. Do NOT wait for coagulation studies to return. PCC for warfarin; idarucizumab for dabigatran; andexanet alfa or PCC for factor Xa inhibitors.

3. **Using FFP instead of PCC for warfarin reversal.** FFP requires 10-15 mL/kg (3-4 units, 30-60 minutes to thaw and infuse), achieves incomplete INR reversal, and causes volume overload. PCC reverses INR within 10-15 minutes with a concentrated bolus. The INCH trial demonstrated superiority of PCC over FFP for ICH. FFP is acceptable only when PCC is unavailable.

4. **Lowering SBP below 130 mmHg.** ATACH-2 showed that targeting SBP 110-139 did not improve outcomes compared to 140-179 and increased renal adverse events. The sweet spot is SBP 130-150. Aggressive lowering below 130 risks end-organ hypoperfusion.

5. **Not obtaining CTA with the initial CT.** The spot sign on CTA (active contrast extravasation) predicts hematoma expansion with 91% sensitivity and identifies patients who benefit most from aggressive BP control and surgical evaluation. Omitting CTA misses actionable prognostic information and potentially treatable vascular lesions (AVM, aneurysm).

6. **Prophylactic antiepileptic drugs.** AHA 2022 guidelines recommend against routine seizure prophylaxis in ICH. Prophylactic antiepileptics do not improve outcomes and have side effects (sedation obscures neurological exam). Treat clinical seizures or continuous EEG-confirmed subclinical seizures only.

7. **Early aggressive goals-of-care discussions leading to premature withdrawal.** ICH Score and initial clinical severity overestimate mortality when aggressive care is not provided. The "self-fulfilling prophecy" of early DNR orders in ICH is well documented — patients given DNR within 24 hours have higher mortality independent of severity. Allow 24-48 hours of maximal medical therapy before prognosticating.

8. **Failing to identify cerebellar hemorrhage as a surgical emergency.** Cerebellar hemorrhage >3 cm with brainstem compression or hydrocephalus requires emergent posterior fossa decompression. Unlike supratentorial hemorrhage, where surgical benefit is debated, cerebellar evacuation is life-saving and can result in good functional recovery.
