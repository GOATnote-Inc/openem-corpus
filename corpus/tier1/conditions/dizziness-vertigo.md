---
id: dizziness-vertigo
condition: "Dizziness and Vertigo — Emergency Evaluation"
aliases: [dizziness, vertigo, lightheadedness, room spinning, unsteady, off balance, disequilibrium]
icd10: [R42, R42.0, H81.10, H81.30]
esi: 3
time_to_harm:
  irreversible_injury: "< 4.5 hours (posterior circulation stroke)"
  death: "< 6 hours (basilar artery occlusion, cerebellar hemorrhage with herniation)"
  optimal_intervention_window: "< 4.5 hours (tPA for posterior circulation stroke)"
category: presentations
condition_type: presentation
chief_complaint: "Dizziness/Vertigo"
differential_categories:
  - category: life-threatening
    conditions:
      - acute-ischemic-stroke
      - hemorrhagic-stroke
      - subarachnoid-hemorrhage
  - category: emergent
    conditions:
      - acute-coronary-syndrome-nstemi
      - pulmonary-embolism
      - cardiac-tamponade
      - complete-heart-block
      - hypertensive-emergency
      - carbon-monoxide-poisoning
      - hypoglycemia
  - category: urgent
    conditions:
      - acute-vertigo
      - atrial-fibrillation-rvr
      - svt
  - category: non-emergent
    conditions:
      - benign-positional-vertigo
red_flags:
  - "Acute onset vertigo with inability to walk (cerebellar stroke)"
  - "Vertical or direction-changing nystagmus (central cause)"
  - "Skew deviation on alternate cover test"
  - "New headache with vertigo"
  - "Focal neurological deficit (dysarthria, diplopia, dysphagia, facial weakness)"
  - "Severe gait ataxia disproportionate to nystagmus"
  - "Vascular risk factors (diabetes, HTN, atrial fibrillation) with acute vertigo"
  - "Inability to sit up or stand due to vertigo severity (may suggest central)"
  - "Hearing loss with vertigo and facial weakness (cerebellopontine angle lesion)"
  - "Recent cervical manipulation"
decision_rules:
  - name: "HINTS Exam (Head Impulse, Nystagmus, Test of Skew)"
    citation: "Kattah JC et al. HINTS to diagnose stroke in the acute vestibular syndrome. Stroke. 2009;40(11):3504-3510."
    pmid: "19762709"
  - name: "ABCD2 Score (if TIA component)"
    citation: "Johnston SC et al. Validation and refinement of scores to predict very early stroke risk after transient ischaemic attack. Lancet. 2007;369(9558):283-292."
    pmid: "17258668"
  - name: "Dix-Hallpike Maneuver"
    citation: "Dix MR, Hallpike CS. The pathology, symptomatology and diagnosis of certain common disorders of the vestibular system. Ann Otol Rhinol Laryngol. 1952;61(4):987-1016."
    pmid: "13008328"
track: tier1
sources:
  - type: pubmed
    ref: "Kattah JC et al. HINTS to diagnose stroke in the acute vestibular syndrome: three-step bedside oculomotor examination more sensitive than early MRI diffusion-weighted imaging. Stroke. 2009;40(11):3504-3510."
    pmid: "19762709"
  - type: pubmed
    ref: "Edlow JA et al. A new diagnostic approach to the adult patient with acute dizziness. J Emerg Med. 2018;54(4):469-483."
    pmid: "29395695"
  - type: guideline
    ref: "AAO-HNS Clinical Practice Guideline: Benign Paroxysmal Positional Vertigo (Update). Otolaryngol Head Neck Surg. 2017;156(3_suppl):S1-S47."
    pmid: "28248609"
  - type: review
    ref: "Edlow JA. Diagnosing dizziness: we are teaching the wrong paradigm. Acad Emerg Med. 2013;20(10):1064-1066."
    pmid: "24127712"
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
# Dizziness and Vertigo — Emergency Evaluation

## Recognition

Dizziness accounts for 3-5% of ED visits. The traditional approach of categorizing dizziness into vertigo, presyncope, disequilibrium, and lightheadedness based on symptom type is unreliable — patients use these terms inconsistently and often change their description on re-questioning. The modern approach focuses on timing and triggers rather than symptom type.

**TiTrATE framework (Timing, Triggers, And Targeted Exam):**

**Timing:**
- **Episodic, triggered:** seconds-minutes, reproducible trigger → BPPV (positional), orthostatic (standing), cardiac (exertional)
- **Episodic, spontaneous:** minutes-hours, no clear trigger → vestibular migraine, Meniere disease, TIA, arrhythmia, panic
- **Acute, continuous (acute vestibular syndrome):** hours-days of constant vertigo, nausea, nystagmus, gait instability → vestibular neuritis (peripheral) vs cerebellar/brainstem stroke (central). THIS IS THE HIGH-STAKES CATEGORY.
- **Chronic, progressive:** weeks-months → acoustic neuroma, medication effect, anxiety, multisensory deficit in elderly

**The critical question:** In acute vestibular syndrome (continuous vertigo > 24 hours with nystagmus and gait instability), is this peripheral (vestibular neuritis, benign) or central (posterior circulation stroke, dangerous)?

**Demographic risk factors for central cause:**
- Age > 60
- Vascular risk factors: HTN, diabetes, atrial fibrillation, hyperlipidemia, smoking
- Prior stroke/TIA
- Recent cervical trauma or chiropractic manipulation (vertebral artery dissection)
- Anticoagulation use

## Critical Actions

| Action | Target |
|---|---|
| Neurological exam including gait | < 15 minutes |
| HINTS exam (acute vestibular syndrome) | < 15 minutes |
| Fingerstick glucose | < 5 minutes |
| ECG | < 10 minutes |
| CT head if central cause suspected | < 25 minutes |

**Evaluation algorithm:**

1. **Classify by timing and trigger pattern** (TiTrATE — see above). Acute vestibular syndrome (continuous vertigo > 24 hours) is the most dangerous category.

2. **For episodic, triggered dizziness:**
   - Positional → Dix-Hallpike maneuver. Positive: after brief latency, geotropic (toward ground) torsional/upbeating nystagmus that fatigues within 30-60 seconds and reverses on sitting. This is BPPV → treat with Epley maneuver.
   - Orthostatic → check orthostatic vitals (see `syncope`)
   - Exertional → cardiac evaluation, ECG

3. **For acute vestibular syndrome → perform HINTS exam:**
   - **H** — Head Impulse test: normal (eyes move OFF target, then correct with saccade = abnormal = peripheral; eyes stay on target = normal = CENTRAL and dangerous). A "normal" head impulse test in acute vestibular syndrome suggests stroke, not a benign process.
   - **IN** — Nystagmus type: unidirectional, horizontal nystagmus = peripheral; direction-changing, vertical, or purely torsional nystagmus = CENTRAL
   - **TS** — Test of Skew: vertical skew deviation on alternate cover test = CENTRAL

   **HINTS interpretation:**
   - All three peripheral pattern (abnormal HIT + unidirectional nystagmus + no skew) = vestibular neuritis. Sensitivity 98% and specificity 96% for peripheral cause — BETTER than early MRI.
   - ANY one central sign (normal HIT, direction-changing nystagmus, or skew deviation) = posterior circulation stroke until proven otherwise → MRI DWI (not CT — CT misses 50% of posterior fossa strokes in first 24-48 hours).

4. **Assess gait.** Severe gait ataxia (inability to walk unassisted) disproportionate to the degree of nystagmus → cerebellar pathology. Isolated gait ataxia without nystagmus in elderly → consider posterior fossa mass, normal pressure hydrocephalus, medication effect.

5. **Do NOT rely on CT to rule out posterior fossa stroke.** CT sensitivity for acute posterior fossa stroke is approximately 40-50%. MRI with DWI is the appropriate imaging modality. If MRI is unavailable and clinical suspicion for stroke is high, admit for observation and obtain MRI within 24-48 hours.

## Differential Diagnosis

### Life-Threatening
- **Posterior circulation stroke** (`acute-ischemic-stroke`): acute vestibular syndrome with central HINTS pattern (normal HIT, direction-changing nystagmus, skew deviation). Cerebellar infarction can cause herniation. PICA, AICA, SCA territory strokes present as isolated vertigo in up to 25% of cases.
- **Cerebellar hemorrhage** (`hemorrhagic-stroke`): sudden vertigo, headache, inability to walk, vomiting. Can cause obstructive hydrocephalus and herniation requiring emergent posterior fossa decompression.
- **Subarachnoid hemorrhage** (`subarachnoid-hemorrhage`): vertigo/dizziness can accompany thunderclap headache, especially with posterior fossa aneurysm
- **Vertebral artery dissection:** neck pain, vertigo, ataxia, Horner syndrome (partial — miosis and ptosis without anhidrosis). History of trauma or cervical manipulation. CTA neck to diagnose. [No standalone corpus entry — see `aortic-dissection` for dissection principles]

### Emergent
- **ACS** (`acute-coronary-syndrome-nstemi`): dizziness as anginal equivalent, especially in elderly and diabetics
- **Pulmonary embolism** (`pulmonary-embolism`): dizziness with dyspnea and tachycardia, pre-syncopal
- **Cardiac tamponade** (`cardiac-tamponade`): dizziness with hypotension, JVD
- **Complete heart block** (`complete-heart-block`): dizziness/near-syncope with bradycardia
- **Hypertensive emergency** (`hypertensive-emergency`): dizziness with severe HTN and end-organ dysfunction
- **CO poisoning** (`carbon-monoxide-poisoning`): dizziness, headache, nausea, multiple household members
- **Hypoglycemia** (`hypoglycemia`): dizziness, diaphoresis, confusion

### Urgent
- **Acute vertigo/vestibular neuritis** (`acute-vertigo`): peripheral HINTS pattern, continuous vertigo lasting days, post-viral. Most common cause of acute vestibular syndrome. Self-limited.
- **Atrial fibrillation with RVR** (`atrial-fibrillation-rvr`): irregular tachycardia causing dizziness/presyncope
- **SVT** (`svt`): paroxysmal tachycardia with dizziness, palpitations
- **Meniere disease:** episodic vertigo (minutes-hours) + unilateral hearing loss + tinnitus + aural fullness [No standalone corpus entry]
- **Vestibular migraine:** episodic vertigo with headache, photophobia, phonophobia, prior migraine history [No standalone corpus entry]

### Non-Emergent
- **BPPV** (`benign-positional-vertigo`): brief episodes (< 60 seconds) triggered by head position changes (rolling over, looking up, bending), positive Dix-Hallpike, treated with Epley maneuver. Most common cause of vertigo overall.
- **Medication-induced:** anticonvulsants, antihypertensives, sedatives, aminoglycosides (vestibulotoxic)
- **Anxiety/hyperventilation:** diagnosis of exclusion, typically with other somatic symptoms

## Workup

**All dizzy patients:**
- Comprehensive neurological exam including cranial nerves, cerebellar testing (finger-nose-finger, heel-shin, rapid alternating movements), gait assessment
- Orthostatic vital signs
- Fingerstick glucose
- ECG (arrhythmia screen)

**For acute vestibular syndrome (continuous vertigo > 24 hours):**
- HINTS exam (must be performed by trained clinician — sensitivity > MRI in first 48 hours)
- MRI with DWI if any central sign on HINTS or high vascular risk (NOT CT — CT misses most posterior fossa strokes early)
- CTA head/neck if dissection suspected
- Consider CTA if MRI unavailable and stroke concern is high

**For episodic triggered dizziness:**
- Dix-Hallpike maneuver (BPPV)
- Orthostatic vitals (orthostatic hypotension)
- ECG and cardiac monitoring (arrhythmia)
- Echocardiography if structural heart disease suspected (aortic stenosis → exertional dizziness)

**Additional labs (based on suspicion):**
- CBC (anemia)
- BMP (electrolytes, glucose, renal function)
- Troponin (if cardiac ischemia suspected)
- Carboxyhemoglobin (CO poisoning)
- TSH (thyroid disease)

**What NOT to order:**
- CT head as the sole imaging for suspected posterior fossa stroke (sensitivity ~40-50%)
- Routine carotid ultrasound (carotid disease causes hemispheric symptoms, not vertigo — unless dissection suspected, in which case CTA is superior)
- Routine EEG (vertigo is not a seizure manifestation)

## Treatment

Treatment targets the underlying cause:

- **BPPV:** Epley maneuver (posterior canal). Effective in 70-90% with single treatment. Can repeat x 2-3 in same session. Log roll maneuver for horizontal canal BPPV. Meclizine is NOT effective for BPPV — it masks symptoms without treating the cause.
- **Vestibular neuritis:** Symptomatic relief with diazepam 2-5 mg PO/IV q8h PRN or meclizine 25 mg PO q8h x 3-5 days ONLY. Limit vestibular suppressant use to < 3 days to allow central compensation. Methylprednisolone taper may improve recovery (evidence moderate).
- **Posterior circulation stroke:** See `acute-ischemic-stroke`. tPA if within 4.5 hours. Thrombectomy for basilar artery occlusion.
- **Cerebellar hemorrhage:** Neurosurgical consultation — suboccipital decompression if > 3 cm or hydrocephalus present. Reverse anticoagulation.
- **Arrhythmia-related:** Rate or rhythm control per specific condition
- **Orthostatic:** IV fluids, identify and treat underlying cause (hemorrhage, dehydration, medication)

**Antiemetics for symptomatic relief:**
- Ondansetron 4 mg IV/PO
- Do NOT use promethazine IV (risk of tissue necrosis)

## Disposition

- **ICU/neurocritical care:** Cerebellar hemorrhage > 3 cm or with hydrocephalus, large posterior circulation stroke, basilar artery occlusion
- **Telemetry/stroke unit:** Posterior circulation stroke (smaller), TIA with posterior circulation symptoms, arrhythmia-related dizziness
- **Observation:** Acute vestibular syndrome with equivocal HINTS and pending MRI, persistent symptoms with inability to ambulate safely
- **Discharge with follow-up:**
  - BPPV after successful Epley maneuver
  - Vestibular neuritis (peripheral HINTS) with symptoms controlled, able to ambulate, reliable follow-up with ENT/neurology
  - Orthostatic dizziness resolved with fluids/medication adjustment
  - Benign arrhythmia (PACs/PVCs) with normal ECG
  - Return precautions: "Return immediately for new headache, weakness, numbness, vision changes, difficulty speaking or swallowing, or inability to walk"
- **Neurology/ENT follow-up:** All new vertigo diagnoses, recurrent vertigo, audiology evaluation if hearing loss

## Pitfalls

1. **"CT was negative, so it's not a stroke."** CT misses approximately 50% of posterior fossa strokes in the first 24-48 hours. This is the most dangerous pitfall in dizziness evaluation. If acute vestibular syndrome with central HINTS features → MRI with DWI is required, NOT CT.

2. **Diagnosing BPPV without performing Dix-Hallpike.** BPPV is a specific diagnosis with specific diagnostic criteria (latent-onset, geotropic torsional nystagmus that fatigues on Dix-Hallpike). "Dizziness with position change" is NOT sufficient. Posterior fossa stroke also worsens with position changes.

3. **Prescribing meclizine for all vertigo.** Meclizine is a vestibular suppressant that provides modest symptomatic relief but does NOT treat BPPV (Epley is the treatment) and delays central compensation in vestibular neuritis. It is appropriate only for short-term symptomatic relief (< 3 days) in acute vestibular neuritis.

4. **Dismissing dizziness in patients with vascular risk factors.** A 65-year-old with diabetes, hypertension, and atrial fibrillation presenting with "dizziness" has a posterior circulation stroke until proven otherwise. Vascular risk factors dramatically increase the pretest probability of central causes.

5. **Missing vertebral artery dissection.** Neck pain + vertigo/ataxia, especially after trauma or cervical manipulation, should prompt CTA of the neck. Vertebral artery dissection is a treatable cause of posterior circulation stroke and is easily missed if not considered.

6. **Ignoring the HINTS exam or performing it incorrectly.** The HINTS exam has > 98% sensitivity for stroke in acute vestibular syndrome when performed correctly by trained clinicians. Incorrect technique (performing on episodic rather than continuous vertigo, misinterpreting head impulse test) renders it useless. HINTS is valid ONLY in acute vestibular syndrome (continuous symptoms with nystagmus).

7. **Failing to assess gait.** Every dizzy patient must have gait evaluated. Severe truncal ataxia (inability to sit or stand unassisted) with mild nystagmus suggests cerebellar pathology. Patients who "cannot walk" due to dizziness need imaging.
