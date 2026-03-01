---
id: stanford-b-aortic-dissection
condition: Stanford Type B Aortic Dissection
aliases: [type B dissection, descending aortic dissection, DeBakey type III dissection, TBAD]
icd10: [I71.01, I71.02, I71.03]
esi: 1
time_to_harm:
  irreversible_injury: "< 2 hours"
  death: "< 6 hours"
  optimal_intervention_window: "< 1 hour for anti-impulse therapy"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "2022 STS/AATS Clinical Practice Guidelines on the Management of Type B Aortic Dissection. Ann Thorac Surg. 2022;113(4):1073-1130."
  - type: guideline
    ref: "2024 EACTS/STS Guidelines for Diagnosing and Treating Acute and Chronic Syndromes of the Aortic Organ. Ann Thorac Surg. 2024."
  - type: guideline
    ref: "2014 ESC Guidelines on the Diagnosis and Treatment of Aortic Diseases. Eur Heart J. 2014;35(41):2873-2926."
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
# Stanford Type B Aortic Dissection

## Recognition

**Presentation:**
- Sudden severe "tearing" or "ripping" interscapular back pain (most common)
- Pain may migrate distally as dissection propagates
- Hypertension at presentation (> 70% of cases)
- Hypotension = complicated dissection (rupture, tamponade, or severe malperfusion)

**Complicated vs uncomplicated TBAD:**
- **Complicated (requires intervention):** Malperfusion syndrome (renal, mesenteric, limb), aortic rupture, refractory hypertension, refractory pain, rapid aortic expansion, contained rupture
- **Uncomplicated:** No malperfusion, stable hemodynamics, controlled pain — medical management

**Malperfusion signs:**
- Renal: oliguria, rising creatinine, flank pain
- Mesenteric: abdominal pain out of proportion to exam, bloody stools, lactic acidosis
- Lower extremity: pulse deficit, cool limb, motor/sensory changes
- Spinal cord: paraplegia or paraparesis (intercostal artery occlusion)

**Physical exam:**
- Blood pressure differential > 20 mmHg between arms (or arm vs leg)
- Aortic regurgitation murmur (if dissection extends to aortic root — reclassify as Type A)
- Pulse deficits in lower extremities
- Abdominal tenderness (mesenteric malperfusion)

## Critical Actions

| Action | Target |
|---|---|
| Anti-impulse therapy initiation | < 15 minutes |
| CT angiography | < 30 minutes of suspicion |
| Vascular surgery consultation | < 30 minutes |
| Heart rate target | < 60 bpm |
| SBP target | 100-120 mmHg |

1. **Anti-impulse therapy — IMMEDIATE** — reduce heart rate FIRST, then blood pressure:
   - Esmolol 500 mcg/kg IV bolus over 1 min, then 50-200 mcg/kg/min infusion (preferred — titratable)
   - OR labetalol 20 mg IV over 2 min, then 40-80 mg q10min (max 300 mg total) or infusion 0.5-2 mg/min
   - Target HR < 60 bpm, SBP 100-120 mmHg
2. **If beta-blocker insufficient for BP control:** Add nicardipine 5-15 mg/hr IV infusion or nitroprusside 0.25-10 mcg/kg/min IV (ONLY after HR controlled — nitroprusside alone increases aortic shear stress)
3. **If beta-blocker contraindicated:** Diltiazem 0.25 mg/kg IV bolus, then 5-15 mg/hr infusion
4. **Pain control:** Morphine 2-4 mg IV q5-15min or fentanyl 25-100 mcg IV (pain drives sympathetic response → worsens dissection)
5. **CT angiography** — full aorta (chest/abdomen/pelvis) with arterial phase — confirm diagnosis, classify, identify malperfusion
6. **Vascular surgery/cardiac surgery consultation** immediately
7. **Arterial line placement** for continuous BP monitoring
8. **Avoid excessive BP reduction** — maintain adequate end-organ perfusion

## Differential Diagnosis

- **Type A aortic dissection** — involves ascending aorta; requires emergent surgery. CTA differentiates.
- **Acute coronary syndrome** — may coexist if dissection involves coronary ostia (usually Type A)
- **Pulmonary embolism** — acute dyspnea, pleuritic pain; CT differentiates
- **Musculoskeletal back pain** — no hemodynamic changes, no malperfusion
- **Acute pancreatitis** — epigastric pain radiating to back; lipase elevated
- **Perforated viscus** — peritonitis, free air on imaging
- **Intramural hematoma** — variant of dissection; managed similarly

## Workup

- **CT angiography (aorta protocol):** Chest/abdomen/pelvis with arterial phase. Identifies intimal flap, true/false lumen, extent of dissection, malperfusion, branch vessel involvement.
- **Bilateral arm blood pressures:** > 20 mmHg difference suggests dissection
- **Labs:** CBC, BMP (creatinine for renal malperfusion), lactate (mesenteric malperfusion), troponin, type and crossmatch (4 units pRBC), coagulation studies, D-dimer (> 500 ng/mL has high sensitivity but poor specificity)
- **Chest X-ray:** Widened mediastinum (sensitivity ~60%), left pleural effusion, abnormal aortic contour — normal CXR does NOT exclude dissection
- **TEE:** If CTA not immediately available or patient too unstable for CT — sensitivity > 95% for Type B
- **ECG:** Rule out concurrent ACS (dissection can cause STEMI if involving coronaries)

## Treatment

### Uncomplicated TBAD — Optimal Medical Therapy
- Anti-impulse therapy as above (HR < 60, SBP 100-120)
- ICU monitoring for minimum 48-72 hours
- Transition to oral beta-blocker (metoprolol succinate 25-100 mg PO daily or amlodipine 5-10 mg PO daily if beta-blocker intolerant)
- Serial imaging: CTA at 1 week, 1 month, 3 months, 6 months, then annually
- In-hospital mortality ~10% with medical management alone

### Complicated TBAD — Thoracic Endovascular Aortic Repair (TEVAR)
- **Indications:** Malperfusion, rupture, rapid expansion, refractory pain/hypertension
- TEVAR is first-line intervention (preferred over open surgery — lower morbidity/mortality)
- Covers primary entry tear with stent graft
- May require adjunctive fenestration or branch vessel stenting for malperfusion

### Surgical Intervention (Open)
- Reserved for TEVAR failure, anatomy unsuitable for TEVAR, or complicated dissection with need for open repair
- Higher morbidity/mortality than TEVAR (25-50% vs 10-15%)

## Disposition

- **ICU admission:** All acute type B dissections — minimum 48-72 hours for hemodynamic monitoring and anti-impulse therapy
- **Stepdown:** After stabilization, continue telemetry and serial imaging
- **Transfer criteria:** All complicated TBAD requiring TEVAR should be transferred to a center with aortic surgery and endovascular capability
- **Outpatient follow-up:** Lifelong surveillance imaging, strict BP control, smoking cessation

## Pitfalls

1. **Administering vasodilators (nitroprusside, hydralazine) without first controlling heart rate.** Vasodilators cause reflex tachycardia, which increases aortic wall shear stress (dP/dt) and promotes dissection propagation. Always establish beta-blockade FIRST, then add vasodilators if needed for BP control.

2. **Giving thrombolytics or anticoagulants for suspected ACS before ruling out dissection.** Type B dissection can cause troponin elevation from hemodynamic stress. Anticoagulation and thrombolysis in aortic dissection cause hemorrhagic extension and death. If dissection is on the differential, obtain CTA before initiating ACS treatment.

3. **Diagnosing musculoskeletal back pain without imaging in a hypertensive patient with acute onset.** Sudden-onset interscapular pain in a hypertensive patient over 50 should prompt dissection workup. The location (between the scapulae) and quality (tearing, worst-ever) distinguish dissection from benign back pain.

4. **Relying on a normal chest X-ray to exclude dissection.** CXR sensitivity for aortic dissection is only ~60%. A normal mediastinal width does not exclude dissection. CTA is the definitive study.

5. **Failure to monitor for delayed malperfusion.** Even initially uncomplicated TBAD can develop malperfusion over 24-72 hours as the false lumen expands. Serial abdominal exams, renal function, lactate levels, and lower extremity pulses are essential during ICU stay.
