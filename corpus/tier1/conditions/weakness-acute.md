---
id: weakness-acute
condition: "Acute Weakness — Emergency Evaluation"
aliases: [weakness, acute weakness, motor deficit, can't move, paralysis, paresis, generalized weakness]
icd10: [R53.1, R53.81, M62.81, G83.9]
esi: 2
time_to_harm:
  irreversible_injury: "< 4.5 hours (ischemic stroke tPA window)"
  death: "< 2 hours (posterior circulation stroke with basilar occlusion, ascending GBS with respiratory failure)"
  optimal_intervention_window: "< 4.5 hours (tPA), < 24 hours (thrombectomy for large vessel occlusion)"
category: presentations
condition_type: presentation
chief_complaint: "Weakness"
differential_categories:
  - category: life-threatening
    conditions:
      - acute-ischemic-stroke
      - hemorrhagic-stroke
      - subarachnoid-hemorrhage
      - spinal-cord-compression
      - spinal-cord-injury
      - cauda-equina-syndrome
      - guillain-barre-syndrome
      - hyperkalemia
      - sepsis
      - aortic-dissection
      - acute-limb-ischemia
      - epidural-hematoma
      - subdural-hematoma
  - category: emergent
    conditions:
      - spinal-epidural-abscess
      - hypoglycemia
      - acute-coronary-syndrome-nstemi
      - acute-heart-failure
      - transient-ischemic-attack
  - category: urgent
    conditions:
      - rhabdomyolysis
      - adrenal-crisis
      - hypothermia
  - category: non-emergent
    conditions: []
red_flags:
  - "Sudden onset (stroke until proven otherwise)"
  - "Unilateral weakness with speech or facial droop"
  - "Ascending bilateral weakness (GBS)"
  - "Bilateral lower extremity weakness with bladder dysfunction (cord compression)"
  - "Weakness with respiratory distress (myasthenic crisis, GBS)"
  - "Weakness with chest or back pain (dissection, cord compression)"
  - "Weakness with hyperkalemia (ECG changes present)"
  - "Weakness after recent infection or vaccination (GBS)"
  - "Weakness with dysarthria or dysphagia (posterior circulation)"
decision_rules:
  - name: "NIHSS (NIH Stroke Scale)"
    citation: "Brott T et al. Measurements of acute cerebral infarction: a clinical examination scale. Stroke. 1989;20(7):864-870."
    pmid: "2749846"
  - name: "BE-FAST Stroke Screening"
    citation: "Extension of FAST mnemonic: Balance, Eyes, Face, Arms, Speech, Time."
  - name: "ABCD2 Score (TIA risk)"
    citation: "Johnston SC et al. Validation and refinement of scores to predict very early stroke risk after transient ischaemic attack. Lancet. 2007;369(9558):283-292."
    pmid: "17258668"
track: tier1
sources:
  - type: guideline
    ref: "2019 AHA/ASA Guidelines for the Early Management of Patients With Acute Ischemic Stroke"
    doi: "10.1161/STR.0000000000000211"
  - type: guideline
    ref: "2019 AHA/ASA Guidelines for the Management of Patients With Spontaneous Intracerebral Hemorrhage"
  - type: guideline
    ref: "2019 AANS/CNS Joint Guidelines for the Management of Acute Spinal Cord Injury"
  - type: pubmed
    ref: "Edlow JA et al. Diagnosis of acute neurological emergencies in the emergency department. Lancet Neurol. 2019;18(12):1123-1133."
    pmid: "31326308"
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
# Acute Weakness — Emergency Evaluation

## Recognition

"Weakness" is one of the most diagnostically challenging chief complaints because patients use the word to describe fundamentally different phenomena: true motor deficit (neurological), fatigue/malaise (systemic illness), or functional limitation (generalized deconditioning). The first task is distinguishing these categories.

**Clarifying the complaint:**
- **True motor weakness:** inability to perform a previously possible motor task (e.g., cannot lift arm, cannot stand from chair, foot drop). This implies neuromuscular pathology.
- **Fatigue/malaise:** generalized lack of energy, exhaustion, "I feel weak all over." This implies systemic illness (infection, anemia, metabolic, cardiac, malignancy).
- **Functional limitation:** cannot perform ADLs due to pain, dizziness, dyspnea, or deconditioning. This requires identifying the underlying cause.

**Localization of true weakness (anatomic approach):**
- **Upper motor neuron (UMN):** brain or spinal cord. Contralateral hemiparesis (cortical/subcortical), ipsilateral weakness below lesion (spinal cord). Hyperreflexia, spasticity (may be absent acutely — "spinal shock"), Babinski sign, no fasciculations.
- **Lower motor neuron (LMN):** anterior horn cell, nerve root, peripheral nerve, neuromuscular junction (NMJ), muscle. Flaccid weakness, hyporeflexia, atrophy, fasciculations (anterior horn/nerve), fatiguable weakness (NMJ).
- **Patterns:**
  - Hemiparesis → stroke (contralateral cortex/subcortex), cord lesion (ipsilateral, Brown-Sequard)
  - Paraparesis → cord compression/myelopathy, GBS, bilateral cortical (parasagittal lesion)
  - Quadriparesis → cervical cord, brainstem, GBS, myasthenic crisis, bilateral cortical
  - Monoparesis → stroke, radiculopathy, peripheral nerve, plexopathy
  - Ascending symmetric weakness → GBS
  - Fluctuating/fatiguable weakness → myasthenia gravis
  - Proximal > distal → myopathy, endocrine, electrolyte
  - Distal > proximal → peripheral neuropathy

**Key history elements:**
- Onset: sudden (stroke), minutes-hours (metabolic, toxin, vascular), days (GBS, cord compression), weeks (myopathy, neuropathy)
- Distribution: unilateral vs bilateral, proximal vs distal, symmetric vs asymmetric
- Associated symptoms: speech changes, vision changes, headache, back pain, sensory changes, bowel/bladder dysfunction, dysphagia, respiratory difficulty
- Preceding illness: recent viral infection (GBS), diarrheal illness (Campylobacter → GBS)
- Medications: statins (myopathy), steroids (myopathy), diuretics (hypokalemia)
- Last known normal time (stroke window determination)

## Critical Actions

| Action | Target |
|---|---|
| Assess for stroke (BE-FAST screening) | < 5 minutes |
| Fingerstick glucose | < 5 minutes |
| ECG (hyperkalemia) | < 10 minutes |
| CT head if stroke suspected | < 25 minutes |
| Activate stroke team if appropriate | < 10 minutes from recognition |

**Evaluation algorithm:**

1. **Is this stroke?** Acute unilateral weakness (face, arm, and/or leg) with or without speech changes → activate stroke protocol immediately. Last known normal time determines treatment eligibility (tPA < 4.5h, thrombectomy < 24h for large vessel occlusion).

2. **Assess airway and breathing.** Weakness with respiratory distress → neuromuscular respiratory failure (GBS, myasthenic crisis). Measure negative inspiratory force (NIF) and forced vital capacity (FVC). NIF > -30 cmH2O or FVC < 20 mL/kg → impending respiratory failure → intubate.

3. **Check glucose and potassium.**
   - Hypoglycemia → D50 IV
   - Hyperkalemia (K+ > 6.0 with ECG changes) → calcium gluconate 1-3 g IV, insulin 10 units IV + D50, sodium bicarbonate (see `hyperkalemia`)
   - Hypokalemia (K+ < 2.5) → IV potassium replacement (risk of respiratory muscle weakness, rhabdomyolysis)

4. **Localize the lesion:**
   - Facial droop + arm/leg weakness (same side) → cortical/subcortical stroke → CT head → tPA/thrombectomy if eligible
   - Bilateral ascending weakness + areflexia → GBS → LP (albuminocytologic dissociation), NCS/EMG, admit for monitoring
   - Bilateral leg weakness + sensory level + bladder dysfunction → cord compression → emergent MRI spine
   - Back pain + fever + progressive deficit → epidural abscess → emergent MRI spine + IV antibiotics

5. **Assess for "weakness mimics" requiring immediate treatment:**
   - Aortic dissection with limb malperfusion → pulse deficit, BP differential
   - Acute limb ischemia → 6 Ps (pain, pallor, pulselessness, poikilothermia, paresthesias, paralysis)
   - Sepsis presenting as generalized weakness in elderly

## Differential Diagnosis

### Life-Threatening
- **Acute ischemic stroke** (`acute-ischemic-stroke`): sudden focal deficit, NIHSS scoring, CT to rule out hemorrhage, CTA for large vessel occlusion. tPA within 4.5 hours, thrombectomy within 24 hours for LVO.
- **Hemorrhagic stroke** (`hemorrhagic-stroke`): sudden deficit + headache, hypertension. CT shows acute hemorrhage. Reverse anticoagulation if applicable.
- **Subarachnoid hemorrhage** (`subarachnoid-hemorrhage`): sudden weakness can accompany thunderclap headache, particularly with large hemorrhage
- **Spinal cord compression** (`spinal-cord-compression`): bilateral weakness below lesion level, sensory level, bladder dysfunction. Malignancy, trauma, epidural hematoma, or abscess. Dexamethasone 10 mg IV for malignant compression.
- **Spinal cord injury** (`spinal-cord-injury`): trauma mechanism, immobilize, MRI
- **Cauda equina syndrome** (`cauda-equina-syndrome`): bilateral lower extremity weakness, saddle anesthesia, urinary retention, decreased rectal tone
- **Guillain-Barre syndrome** (`guillain-barre-syndrome`): ascending symmetric weakness over days, areflexia, preceding infection (often Campylobacter, CMV, EBV). Monitor respiratory function closely — 30% require intubation. LP: elevated protein, normal WBC. IVIG 0.4 g/kg/day x 5 days or plasmapheresis.
- **Hyperkalemia** (`hyperkalemia`): generalized weakness progressing to flaccid paralysis, ECG changes (peaked T, widened QRS, sine wave)
- **Sepsis** (`sepsis`): elderly present with "generalized weakness" as the chief complaint of sepsis. Check lactate and obtain blood cultures.
- **Aortic dissection** (`aortic-dissection`): acute limb weakness from branch vessel compromise, acute paraplegia from spinal artery occlusion (anterior spinal artery syndrome)
- **Acute limb ischemia** (`acute-limb-ischemia`): sudden unilateral limb weakness/paralysis with absent pulses, pallor, pain. Time-critical revascularization.
- **Epidural/subdural hematoma** (`epidural-hematoma`, `subdural-hematoma`): post-traumatic, progressive weakness, herniation signs

### Emergent
- **Spinal epidural abscess** (`spinal-epidural-abscess`): IVDU or immunocompromised, fever + back pain → progressive weakness. MRI urgent.
- **Hypoglycemia** (`hypoglycemia`): generalized weakness, confusion, tremor, diaphoresis. Glucose < 60 mg/dL. Focal deficits can mimic stroke.
- **ACS** (`acute-coronary-syndrome-nstemi`): elderly/diabetic patients may present with weakness as anginal equivalent
- **Acute heart failure** (`acute-heart-failure`): exertional weakness from low cardiac output
- **TIA:** Transient weakness resolving within minutes-hours. Requires urgent workup as 10-15% stroke risk within 90 days.

### Urgent
- **Rhabdomyolysis** (`rhabdomyolysis`): muscle weakness/pain, dark urine, CK > 5x ULN, risk of AKI
- **Adrenal crisis** (`adrenal-crisis`): profound weakness, hypotension, hyponatremia, hyperkalemia
- **Hypothermia** (`hypothermia`): generalized weakness with cold exposure, altered mentation

## Workup

**All patients with true motor weakness:**
- Fingerstick glucose (immediate)
- CBC, BMP (electrolytes, calcium, magnesium, phosphorus, BUN/Cr)
- ECG (hyperkalemia, arrhythmia, ACS)
- Continuous monitoring

**Stroke evaluation:**
- Non-contrast CT head (rule out hemorrhage) → CTA head/neck (large vessel occlusion) → CT perfusion (if within thrombectomy window and timing uncertain)
- NIHSS scoring
- CBC, BMP, coagulation studies, troponin, glucose
- Type and screen if thrombolysis anticipated

**Spinal cord evaluation:**
- MRI spine with gadolinium (cord compression, myelitis, abscess, hemorrhage)
- CT spine if MRI unavailable or contraindicated

**Neuromuscular evaluation:**
- CK (rhabdomyolysis, myopathy)
- TSH (hypothyroid myopathy)
- LP (GBS: elevated protein with normal WBC — albuminocytologic dissociation)
- Acetylcholine receptor antibodies (myasthenia — send but do not wait for result)
- NIF and FVC for respiratory monitoring in GBS or myasthenic crisis
- NCS/EMG (urgent, not ED-performed, but arrange)

**Generalized weakness without focal deficit:**
- CBC (anemia, leukocytosis)
- BMP + calcium, magnesium, phosphorus
- TSH
- Lactate (sepsis screen)
- Urinalysis (UTI as precipitant in elderly)
- CXR
- Consider cortisol if adrenal crisis suspected

## Treatment

Treatment is etiology-specific. Stabilization:

- **Stroke:** tPA 0.9 mg/kg IV (10% bolus, remainder over 60 min) if within 4.5 hours and no contraindications. Thrombectomy for LVO up to 24 hours with favorable perfusion imaging. (See `acute-ischemic-stroke`.)
- **ICH:** BP reduction (nicardipine 5-15 mg/hr IV, target SBP < 140). Reverse anticoagulation emergently. Neurosurgical consultation.
- **Cord compression (malignant):** Dexamethasone 10 mg IV bolus → 4 mg q6h. Emergent radiation oncology + neurosurgery.
- **GBS:** IVIG 0.4 g/kg/day x 5 days OR plasmapheresis x 5 sessions. Monitor NIF/FVC q4-6h. Intubate if NIF > -30 cmH2O or FVC < 20 mL/kg (the "20/30/40 rule": FVC < 20, NIF > -30, > 30% decline from baseline in either).
- **Hyperkalemia:** Calcium gluconate 1-3 g IV (membrane stabilization) → insulin 10 units IV + D50 (intracellular shift) → albuterol 10-20 mg nebulized → sodium polystyrene or patiromer → dialysis for refractory.
- **Hypoglycemia:** D50 25-50 mL IV (1 amp)
- **Epidural abscess:** Vancomycin 25-30 mg/kg IV + cefepime 2 g IV + emergent neurosurgical decompression

## Disposition

- **ICU/neurocritical care:** Acute stroke (post-tPA or thrombectomy), ICH, GBS (respiratory monitoring), spinal cord injury, cord compression post-operative
- **Telemetry/step-down:** TIA (urgent workup), new-onset GBS (mild, respiratory stable), stroke not requiring ICU, hyperkalemia requiring ongoing monitoring
- **Floor admission:** Rhabdomyolysis for IV hydration and CK trending, adrenal crisis on stress-dose steroids
- **Discharge:** ONLY if cause of weakness fully identified and benign (e.g., dehydration with resolved symptoms, medication side effect with drug discontinued). True motor weakness is almost never discharged directly from the ED.
- **Neurology consultation:** All patients with new focal motor deficit, suspected GBS, myasthenic crisis, or myelopathy

## Pitfalls

1. **Treating "generalized weakness" as a non-emergency.** In the elderly, "weakness" is the chief complaint of sepsis, MI, PE, stroke, and hyperkalemia. It is one of the most dangerous chief complaints precisely because it is nonspecific. Full workup is required.

2. **Missing posterior circulation stroke.** Posterior fossa strokes (brainstem, cerebellum) cause weakness patterns that do not fit the classic "face-arm-leg" hemiparesis. Dysarthria, dysphagia, ataxia, diplopia, vertigo + weakness → posterior circulation until proven otherwise. CTA must include the posterior circulation.

3. **Assuming bilateral weakness is not stroke.** Basilar artery occlusion causes bilateral weakness, cranial nerve palsies, and obtundation. This is one of the most devastating strokes and is frequently misdiagnosed. Any acute bilateral weakness with brainstem signs → emergent CTA.

4. **Failure to monitor respiratory function in GBS.** GBS ascends over days. A patient admitted with leg weakness may develop diaphragmatic paralysis. Serial NIF and FVC measurements q4-6h are mandatory. Do NOT rely on SpO2 — hypoxia is a late finding in neuromuscular respiratory failure.

5. **Hypoglycemia mimicking stroke.** Hypoglycemia can cause hemiparesis, aphasia, and virtually any focal neurological deficit. Always check glucose BEFORE CT. Treating hypoglycemia may completely resolve the "stroke."

6. **Missing acute limb ischemia.** A "weak" or "numb" extremity with absent pulses and pallor is acute limb ischemia, not a neurological problem. Check pulses in every patient with unilateral limb weakness. Limb viability depends on rapid revascularization (< 6 hours).

7. **Dismissing "weakness" in a young patient.** GBS, myasthenic crisis, transverse myelitis, spinal cord infarction, and vertebral artery dissection all affect young patients. Age alone does not exclude serious pathology.
