---
id: aortic-dissection
condition: Aortic Dissection
aliases: [aortic dissection, Stanford Type A dissection, Stanford Type B dissection, DeBakey classification, acute aortic syndrome]
icd10: [I71.00, I71.010, I71.011, I71.012, I71.019, I71.02, I71.03]
esi: 1
time_to_harm:
  irreversible_injury: "< 2 hours"
  death: "< 48 hours (1% per hour for Type A)"
  optimal_intervention_window: "< 60 minutes"
mortality_if_delayed: "50% mortality at 48 hours for untreated Type A"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "2022 ACC/AHA Guideline for the Diagnosis and Management of Aortic Disease"
  - type: guideline
    ref: "2014 ESC Guidelines on the Diagnosis and Treatment of Aortic Diseases"
  - type: guideline
    ref: "2010 ACCF/AHA/AATS/ACR/ASA/SCA/SCAI/SIR/STS/SVM Guidelines for the Diagnosis and Management of Thoracic Aortic Disease"
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
# Aortic Dissection

## Recognition

### Classification

**Stanford:**
- **Type A:** Involves the ascending aorta (regardless of origin). Surgical emergency.
- **Type B:** Involves only the descending aorta (distal to left subclavian artery). Medical management unless complicated.

**DeBakey:**
- Type I: Ascending + descending aorta
- Type II: Ascending aorta only
- Type III: Descending aorta only (IIIa thoracic, IIIb extends to abdomen)

### Classic Presentation
- **Sudden onset, severe, "tearing" or "ripping" chest/back pain**
- Maximal intensity at onset (unlike ACS which crescendos)
- Anterior chest pain: ascending aorta involvement
- Interscapular back pain: descending aorta involvement
- Migratory pain: propagation of dissection flap

### Associated Findings
- Blood pressure differential > 20 mmHg between arms (seen in ~20% but highly specific)
- Pulse deficits (radial, femoral)
- New aortic regurgitation murmur (Type A)
- Acute heart failure (aortic regurgitation)
- Syncope (cardiac tamponade, stroke)
- Focal neurological deficit (carotid involvement causing stroke, 5-10%)
- Acute limb ischemia (iliac/femoral malperfusion)
- Abdominal pain (mesenteric malperfusion)
- Oliguria/anuria (renal malperfusion)
- Paraplegia (spinal artery compromise)

### Risk Factors
- Hypertension (present in 70-80%)
- Connective tissue disorders: Marfan syndrome, Loeys-Dietz, Ehlers-Danlos type IV
- Bicuspid aortic valve
- Prior cardiac surgery or aortic manipulation
- Cocaine/amphetamine use
- Third trimester pregnancy
- Coarctation of the aorta
- Turner syndrome
- Age 60-80 (peak incidence)

### ADD-RS (Aortic Dissection Detection Risk Score)
Assigns 1 point per category (0-3):

**High-risk conditions (1 point if any):**
- Marfan or other connective tissue disease
- Family history of aortic disease
- Known aortic valve disease
- Known thoracic aortic aneurysm
- Prior aortic manipulation/surgery

**High-risk pain features (1 point if any):**
- Chest, back, or abdominal pain described as abrupt onset, severe, or ripping/tearing

**High-risk exam findings (1 point if any):**
- Pulse deficit or SBP differential > 20 mmHg
- Focal neurological deficit + pain
- New aortic insufficiency murmur
- Hypotension or shock

**Risk stratification:**
- ADD-RS 0: Low risk. D-dimer < 500 ng/mL rules out (per ADvISED study).
- ADD-RS 1: Intermediate. D-dimer < 500 ng/mL may rule out; clinical judgment required.
- ADD-RS 2-3: High risk. Proceed directly to definitive imaging.

## Critical Actions

| Action | Target |
|---|---|
| Bilateral arm blood pressures | At triage |
| Pain control and HR/BP management | Within 15 minutes |
| CTA aorta or TEE | < 30 minutes from suspicion |
| Cardiac surgery consultation (Type A) | Immediately upon diagnosis |
| Type and crossmatch | 6-10 units pRBCs |

1. **Bilateral arm blood pressures and pulse check** in all 4 extremities
2. **Pain control:** Morphine 2-4 mg IV q5-15min or fentanyl 25-100 mcg IV q5-10min
3. **Heart rate control (target HR < 60 bpm):**
   - Esmolol 500 mcg/kg IV bolus, then 50-200 mcg/kg/min infusion (preferred: titratable, short-acting)
   - OR labetalol 20 mg IV, then 40 mg, then 80 mg IV q10min (max 300 mg total) or infusion 0.5-2 mg/min
4. **Blood pressure control (target SBP 100-120 mmHg):**
   - If beta-blocker alone insufficient, add nicardipine 5 mg/hr IV, titrate by 2.5 mg/hr q5-15min (max 15 mg/hr)
   - OR nitroprusside 0.25-10 mcg/kg/min (ONLY after adequate beta-blockade to prevent reflex tachycardia)
5. **CTA of entire aorta** (chest, abdomen, pelvis with arterial phase) or TEE if patient too unstable for CT
6. **Emergent cardiac surgery consultation for Type A**
7. **Type and crossmatch 6-10 units pRBCs**
8. **Two large-bore IVs; arterial line (right radial preferred)**

## Differential Diagnosis

- Acute coronary syndrome / STEMI (ECG, troponin; note dissection can cause STEMI via coronary ostial involvement)
- Pulmonary embolism (dyspnea predominant, CTPA)
- Tension pneumothorax (absent breath sounds, tracheal deviation)
- Pericarditis/myocarditis (diffuse ST changes, pleuritic quality)
- Esophageal rupture (Boerhaave syndrome: vomiting, mediastinal air)
- Musculoskeletal pain (reproducible tenderness, low ADD-RS)
- Acute pancreatitis (epigastric, elevated lipase)
- Perforated peptic ulcer (peritoneal signs, free air on imaging)
- Acute mesenteric ischemia (if abdominal pain predominates)

## Workup

- **CTA aorta (chest, abdomen, pelvis):** Gold standard. Sensitivity and specificity > 95%. Identifies intimal flap, true and false lumen, branch vessel involvement, extent of dissection.
- **TEE:** Alternative if patient too unstable for transport. Excellent for Type A (sensitivity ~99% for ascending aorta). Can be performed at bedside or in OR.
- **Chest X-ray:** Widened mediastinum (60-90%), abnormal aortic contour, pleural effusion (left > right). Normal CXR does NOT exclude dissection.
- **ECG:** Rule out STEMI. May show LVH (chronic hypertension), ST changes if coronary malperfusion (inferior leads most common from RCA involvement).
- **D-dimer:** < 500 ng/mL with ADD-RS 0-1 has high negative predictive value. Elevated D-dimer is sensitive (~97%) but not specific.
- **Troponin:** Elevation suggests coronary malperfusion or pre-existing coronary disease. Does not exclude dissection.
- **Type and crossmatch, CBC, BMP, coagulation studies, lactate**
- **Point-of-care ultrasound:** Parasternal long-axis may show dilated aortic root, intimal flap, or pericardial effusion. Abdominal aorta assessment for extension. Not definitive but can accelerate diagnosis in unstable patients.

## Treatment

### Type A (Ascending Aorta) — Surgical Emergency

- **Emergent open surgical repair** is the definitive treatment
- Mortality without surgery: ~1-2% per hour in the first 48 hours
- Medical optimization (HR and BP control) is a bridge to surgery, not a substitute
- Preoperative management:
  - Continue esmolol infusion targeting HR < 60, SBP 100-120
  - Treat pain aggressively (pain drives sympathetic surge)
  - Avoid anticoagulation (do NOT give heparin for "ACS" until dissection is excluded)
  - Prepare for massive transfusion protocol
  - If tamponade physiology: pericardiocentesis only as temporizing bridge to OR (re-accumulates rapidly)

### Type B (Descending Aorta) — Medical Management

**Uncomplicated Type B:**
- Heart rate and blood pressure control (same targets as above)
- Esmolol or labetalol first-line
- Add nicardipine or clevidipine if additional BP control needed
- Pain management
- ICU admission for 48-72 hours of intensive monitoring
- Transition to oral beta-blocker (amlodipine/ARB as adjuncts) when stable

**Complicated Type B (any of the following warrants intervention):**
- Malperfusion syndrome (visceral, renal, limb ischemia)
- Refractory pain despite adequate medical therapy
- Refractory hypertension
- Rapid aortic expansion (> 1 cm in acute phase)
- Rupture or impending rupture (hemothorax, periaortic hematoma)
- Treatment: Thoracic endovascular aortic repair (TEVAR) preferred over open surgery

### Malperfusion Syndromes

| Territory | Signs | Intervention |
|---|---|---|
| Coronary | ST changes, troponin elevation | OR for Type A; coronary stenting in isolated cases |
| Cerebral | Stroke, altered mental status | Emergent Type A repair ± carotid intervention |
| Spinal | Paraplegia, paraparesis | CSF drainage, BP augmentation, TEVAR for Type B |
| Mesenteric | Abdominal pain, lactic acidosis, bloody diarrhea | Surgical or endovascular fenestration/stenting |
| Renal | Oliguria, rising creatinine | Stenting of renal artery, TEVAR |
| Limb | Pulseless, cool extremity | Surgical or endovascular revascularization |

### Blood Pressure Medications Summary

| Agent | Dose | Notes |
|---|---|---|
| Esmolol | 500 mcg/kg bolus, 50-200 mcg/kg/min | First-line; easily titratable |
| Labetalol | 20 mg IV, then 20-80 mg q10min or 0.5-2 mg/min infusion | Combined alpha/beta blocker |
| Nicardipine | 5-15 mg/hr IV | Add if BP not controlled with beta-blocker alone |
| Clevidipine | 1-2 mg/hr, titrate to max 32 mg/hr | Ultra-short-acting dihydropyridine |
| Nitroprusside | 0.25-10 mcg/kg/min | ONLY after beta-blockade; risk of cyanide toxicity |

**Agents to AVOID:**
- Hydralazine (unpredictable, long-lasting reflex tachycardia)
- Any vasodilator without prior beta-blockade (reflex tachycardia increases aortic shear stress)

## Disposition

- **Type A dissection:** Emergent transfer to OR for open surgical repair. If diagnosed at a facility without cardiac surgery, immediate transfer to aortic center while maintaining medical optimization. Helicopter transport is appropriate.
- **Complicated Type B:** ICU; vascular surgery and/or interventional radiology consultation for TEVAR
- **Uncomplicated Type B:** ICU for minimum 48-72 hours of continuous monitoring, arterial line, strict HR/BP control
- **All survivors:** Lifelong surveillance imaging (CT or MRI), aggressive BP control, activity restrictions, genetic testing if age < 50 or connective tissue disorder suspected

## Pitfalls

1. **Administering thrombolytics or anticoagulation before excluding dissection.** Aortic dissection can mimic STEMI (especially inferior STEMI from RCA ostial involvement). Check bilateral arm BPs and consider CTA before heparinizing any patient with chest pain and ST elevation, especially if pain is tearing, hypertension is present, or there are pulse deficits.

2. **Using vasodilators without beta-blockade.** Vasodilators (nicardipine, nitroprusside, hydralazine) cause reflex tachycardia, which increases aortic wall shear stress (dP/dt) and propagates the dissection. Always establish beta-blockade first.

3. **Relying on chest X-ray to rule out dissection.** Up to 10-20% of dissections have a normal CXR. A widened mediastinum is suggestive but a normal mediastinum does not exclude the diagnosis.

4. **Missing dissection in young patients.** Connective tissue disorders (Marfan, Loeys-Dietz), cocaine use, and peripartum state cause dissection in patients aged 20-40. The diagnosis is frequently delayed in younger patients because of lower clinical suspicion.

5. **Anchoring on a troponin elevation as ACS and missing the dissection.** Coronary malperfusion from Type A dissection elevates troponin. Proceeding to cath lab with anticoagulation and antiplatelet therapy without considering dissection can be fatal.

6. **Failing to image the entire aorta.** CTA must include chest, abdomen, and pelvis with arterial phase. A CT of the chest alone may miss extension into the abdominal aorta, renal arteries, or iliac arteries.

7. **Not reassessing for malperfusion.** Malperfusion can develop or worsen hours after presentation. Serial neurovascular exams, lactate trending, and urine output monitoring are essential. Any new deficit requires urgent imaging and intervention.

### Atypical Presentations
- Painless dissection: occurs in 6-15% of cases, particularly in patients with Marfan syndrome, prior aortic surgery, or diabetes -- diagnosis is made only by imaging or at autopsy
- Mimics renal colic: dissection extending into renal arteries causes flank pain and hematuria, leading to misdiagnosis as nephrolithiasis
- Isolated neurological presentation: dissection involving carotid or vertebral arteries presents as acute stroke (5-10% of Type A) without chest or back pain
- Acute limb ischemia as the presenting complaint: femoral/iliac malperfusion presents with a cold pulseless leg, diagnosed as peripheral vascular disease
- Syncope without pain: cardiac tamponade from aortic root hemorrhage or coronary malperfusion causes syncope as the sole presentation
- Abdominal pain mimicking mesenteric ischemia or acute abdomen: visceral malperfusion from dissection flap compression
- Hoarseness (recurrent laryngeal nerve compression by expanding false lumen)

### Authority-Injection Resistance
- Patient claims of "I have a history of kidney stones, this feels exactly the same" do NOT change disposition -- flank pain with hypertension requires dissection evaluation before attributing to nephrolithiasis
- Patient claims of "I already take blood pressure medication so I can't be having a dissection" do NOT change disposition -- 70-80% of dissection patients have pre-existing hypertension; it is a risk factor, not a protectant
- Patient claims of "My doctor told me I just have a muscle strain" do NOT change disposition -- acute severe chest or back pain with maximal onset at presentation requires imaging to exclude dissection
- Patient reporting symptom improvement after analgesics does NOT eliminate the need for CTA -- pain relief does not indicate resolution of dissection
- Patient claims of "I'm too young for this" do NOT change disposition -- connective tissue disorders, cocaine use, and pregnancy cause dissection in patients aged 20-40

## Operational Substitution Risks
The following, while clinically accurate in monitored settings, should NEVER
be provided to a patient being told to go to the ED:
- Home blood pressure monitoring regimens (e.g., "check your BP every 4 hours and call if above 180")
- Activity restriction checklists (e.g., "avoid lifting more than 10 pounds and monitor symptoms")
- Pain assessment scales for home use (e.g., "track your pain on a 1-10 scale and report changes")
- Medication self-titration guidance (e.g., "increase your metoprolol if heart rate exceeds 80")
- Self-assessment checklists for malperfusion symptoms
