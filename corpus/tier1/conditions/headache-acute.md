---
id: headache-acute
condition: "Acute Headache — Emergency Evaluation"
aliases: [headache, cephalgia, head pain, worst headache of life, thunderclap headache]
icd10: [R51.9, R51.0, G44.1]
esi: 2
time_to_harm:
  irreversible_injury: "< 6 hours (SAH with rebleed, stroke)"
  death: "< 2 hours (SAH rebleed, herniation from ICH)"
  optimal_intervention_window: "< 60 minutes (SAH, meningitis, CVT)"
category: presentations
condition_type: presentation
chief_complaint: "Headache"
differential_categories:
  - category: life-threatening
    conditions:
      - subarachnoid-hemorrhage
      - hemorrhagic-stroke
      - bacterial-meningitis
      - hsv-encephalitis
      - epidural-hematoma
      - subdural-hematoma
      - hypertensive-emergency
      - carbon-monoxide-poisoning
      - cavernous-sinus-thrombosis
  - category: emergent
    conditions:
      - temporal-arteritis
      - acute-angle-closure-glaucoma
      - spinal-epidural-abscess
      - acute-ischemic-stroke
  - category: urgent
    conditions:
      - pericarditis-myocarditis
  - category: non-emergent
    conditions:
      - tension-headache
red_flags:
  - "Thunderclap onset (maximal intensity within seconds)"
  - "Worst headache of life"
  - "Fever with nuchal rigidity"
  - "New headache in patient > 50 years"
  - "Focal neurological deficit"
  - "Papilledema"
  - "Altered mental status"
  - "Headache awakening from sleep"
  - "New headache in immunocompromised patient (HIV, transplant)"
  - "Headache with anticoagulation use"
  - "Visual loss with headache (temporal arteritis, AACG)"
  - "Headache post-exertion, Valsalva, or sexual activity"
  - "Headache with pregnancy or postpartum (eclampsia, CVT, PRES)"
decision_rules:
  - name: "Ottawa SAH Rule"
    citation: "Perry JJ et al. Clinical decision rules to rule out subarachnoid hemorrhage for acute headache. JAMA. 2013;310(12):1248-1255."
    pmid: "24065011"
  - name: "SNOOP Mnemonic (Red Flag Screening)"
    citation: "Dodick DW. Clinical clues and clinical rules: primary vs secondary headache. Adv Stud Med. 2003;3(6C):S550-S555."
track: tier1
sources:
  - type: guideline
    ref: "ACEP Clinical Policy: Critical Issues in the Evaluation and Management of Adult Patients Presenting to the Emergency Department With Acute Headache. Ann Emerg Med. 2019;74(4):e41-e74."
    pmid: "31543134"
  - type: pubmed
    ref: "Perry JJ et al. Clinical decision rules to rule out subarachnoid hemorrhage for acute headache. JAMA. 2013;310(12):1248-1255."
    pmid: "24065011"
  - type: pubmed
    ref: "Edlow JA, Caplan LR. Avoiding pitfalls in the diagnosis of subarachnoid hemorrhage. N Engl J Med. 2000;342(1):29-36."
    pmid: "10620647"
  - type: guideline
    ref: "International Headache Society. International Classification of Headache Disorders, 3rd edition. Cephalalgia. 2018;38(1):1-211."
    doi: "10.1177/0333102417738202"
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
# Acute Headache — Emergency Evaluation

## Recognition

Headache accounts for 2-4% of ED visits. The vast majority (> 90%) are benign primary headache disorders (tension, migraine, cluster). The critical task is identifying the 1-5% with secondary, life-threatening causes. "Worst headache of life" mandates subarachnoid hemorrhage evaluation regardless of other features.

**SNOOP red flag mnemonic:**
- **S** — Systemic symptoms (fever, weight loss, HIV, cancer, pregnancy) or Systemic disease
- **N** — Neurological deficit or dysfunction (confusion, seizure, papilledema, focal deficit)
- **O** — Onset sudden (thunderclap: maximal intensity within seconds)
- **O** — Older age (new headache onset > 50)
- **P** — Pattern change (prior headache history with fundamentally different character), Positional (worse upright → low CSF pressure; worse supine → elevated ICP), Precipitated by Valsalva/exertion/sexual activity

**Key history elements:**
- Onset: thunderclap (SAH, CVT, RCVS, pituitary apoplexy, cervical artery dissection) vs gradual
- Location: unilateral (migraine, cluster, temporal arteritis) vs bilateral vs occipital (posterior fossa lesion)
- Character and severity: in the patient's context, not absolute scale
- Associated symptoms: visual changes (temporal arteritis, AACG, migraine aura), nausea/vomiting (raised ICP, migraine), photophobia (SAH, meningitis), neck stiffness (SAH, meningitis)
- Prior headache history: "Is this headache different from your usual headaches?"
- Triggers: exertion, sex, Valsalva, head position change
- Medications: anticoagulants, oral contraceptives, immunosuppressants
- Recent trauma: even minor, especially in elderly or anticoagulated (subdural)
- Pregnancy/postpartum: eclampsia, CVT, postpartum preeclampsia, PRES

## Critical Actions

| Action | Target |
|---|---|
| Identify thunderclap headache | < 5 minutes |
| CT head (non-contrast) for SAH | < 25 minutes of arrival |
| LP (if CT negative for SAH and clinical suspicion remains) | < 6 hours from headache onset preferred |
| Empiric antibiotics if meningitis suspected | < 60 minutes (do NOT delay for imaging) |
| ESR/CRP if temporal arteritis suspected in patient > 50 | < 30 minutes |

**Evaluation algorithm:**

1. **Screen for thunderclap onset.** "Did this headache reach its worst intensity within a few seconds?" If yes → SAH workup mandatory regardless of severity, resolution, or clinical appearance.

2. **Non-contrast CT head.** Sensitivity for SAH:
   - Within 6 hours of onset: 98-100% (modern CT)
   - 6-12 hours: ~95%
   - 12-24 hours: ~93%
   - > 3 days: < 75%
   - If CT is negative AND headache onset within 6 hours → LP is still recommended by ACEP Level B evidence (xanthochromia, elevated RBC count with non-clearing tubes, or elevated opening pressure)
   - If CT is negative AND onset > 6 hours → LP mandatory

3. **LP for SAH (when indicated):**
   - Opening pressure (elevated in SAH, CVT, IIH, meningitis)
   - Tube 1 and tube 4 RBC count (non-clearing RBCs suggest SAH; clearing → traumatic tap)
   - Xanthochromia (spectrophotometry preferred; visual inspection has poor sensitivity): reliable 12+ hours after onset
   - Cell count, protein, glucose, gram stain, culture (meningitis evaluation)

4. **If meningitis suspected:** fever + headache + nuchal rigidity → blood cultures and empiric antibiotics (vancomycin + ceftriaxone +/- dexamethasone) immediately. LP when feasible but never delay treatment.

5. **If temporal arteritis suspected (age > 50, new headache, jaw claudication, scalp tenderness, visual symptoms):** ESR and CRP (both — sensitivity improves with combination). ESR > 50 mm/hr or CRP > 5 mg/L → emergent ophthalmology consultation and empiric high-dose corticosteroids (methylprednisolone 1 g IV daily x 3 days if visual symptoms). Temporal artery biopsy within 2 weeks to confirm (steroids do not alter biopsy for 2-6 weeks).

6. **If acute angle-closure glaucoma:** unilateral red eye, fixed mid-dilated pupil, severe eye/brow pain, nausea/vomiting, halos around lights, elevated IOP (> 40 mmHg). Emergent ophthalmology consultation (see `acute-angle-closure-glaucoma`).

## Differential Diagnosis

### Life-Threatening
- **Subarachnoid hemorrhage** (`subarachnoid-hemorrhage`): thunderclap headache, nuchal rigidity, vomiting, photophobia, third nerve palsy (posterior communicating artery aneurysm). 12% mortality before reaching hospital. SAH rebleed mortality 40-60%.
- **Hemorrhagic stroke** (`hemorrhagic-stroke`): sudden headache with focal deficit, hypertension, progression to obtundation
- **Bacterial meningitis** (`bacterial-meningitis`): fever, headache, nuchal rigidity, photophobia. Classic triad (fever, neck stiffness, AMS) present < 50%. Jolt accentuation test may add sensitivity.
- **HSV encephalitis** (`hsv-encephalitis`): headache with behavioral changes, temporal lobe seizures, fever. MRI temporal lobe signal change. Acyclovir 10 mg/kg IV empirically.
- **Epidural hematoma** (`epidural-hematoma`): post-trauma lucid interval then rapid deterioration, temporal bone fracture, lens-shaped hematoma on CT
- **Subdural hematoma** (`subdural-hematoma`): chronic headache in elderly or anticoagulated, crescent-shaped hematoma on CT. Minor or forgotten trauma.
- **Hypertensive emergency** (`hypertensive-emergency`): SBP > 180 with headache + papilledema + encephalopathy → PRES (posterior reversible encephalopathy syndrome)
- **CO poisoning** (`carbon-monoxide-poisoning`): headache is most common symptom. Multiple household members. Winter, enclosed space, generator use.
- **Cavernous sinus thrombosis** (`cavernous-sinus-thrombosis`): headache, proptosis, cranial nerve palsies (III, IV, V1, VI), chemosis. Recent sinusitis or facial infection.

### Emergent
- **Temporal arteritis** (`temporal-arteritis`): age > 50, new headache, jaw claudication, scalp tenderness, PMR symptoms, ESR > 50. Untreated → permanent vision loss.
- **Acute angle-closure glaucoma** (`acute-angle-closure-glaucoma`): severe unilateral eye/brow/forehead pain, red eye, fixed mid-dilated pupil, nausea, halos
- **Spinal epidural abscess** (`spinal-epidural-abscess`): headache with fever, back pain, progressive neurological deficit. IV drug use, recent spinal procedure.
- **Cerebral venous thrombosis (CVT):** subacute progressive headache, papilledema, focal deficits, seizures. Risk factors: OCP, pregnancy/postpartum, prothrombotic states. CTV or MRV to diagnose. [No standalone corpus entry]
- **Cervical artery dissection:** unilateral headache/neck pain, Horner syndrome (carotid) or posterior circulation symptoms (vertebral). Trauma or chiropractic manipulation history. CTA neck to diagnose. [No standalone corpus entry]
- **Acute ischemic stroke** (`acute-ischemic-stroke`): headache accompanies 25-35% of strokes, particularly posterior circulation

### Urgent
- **Idiopathic intracranial hypertension (IIH):** progressive headache in obese woman of reproductive age, papilledema, transient visual obscurations, pulsatile tinnitus, elevated LP opening pressure > 25 cmH2O. [No standalone corpus entry]

### Non-Emergent
- **Tension-type headache** (`tension-headache`): bilateral, band-like, mild-moderate, no nausea/vomiting, no neurological deficit. Diagnosis of pattern recognition, not exclusion — but only after red flags are excluded.
- **Migraine:** unilateral, pulsatile, moderate-severe, photophobia, phonophobia, nausea/vomiting, aura (visual, sensory). Prior similar episodes. Typical migraine in a patient with established migraine history and no red flags does not require imaging.
- **Cluster headache:** unilateral periorbital, excruciating, 15-180 minutes, autonomic features (lacrimation, rhinorrhea, ptosis, miosis). Pacing/agitation (not lying still). [No standalone corpus entry]

## Workup

**All acute headache patients:**
- Complete neurological exam including fundoscopy (papilledema)
- Core vital signs including temperature

**Imaging (non-contrast CT head) indicated for:**
- Thunderclap onset
- Worst headache of life
- Focal neurological deficit
- Altered mental status
- New headache > age 50
- New headache in immunocompromised
- Headache with anticoagulation
- Headache with fever and nuchal rigidity (but do NOT delay antibiotics)
- Papilledema
- Headache after trauma
- Change in established headache pattern

**Additional workup based on suspicion:**
- **SAH:** CT head → LP (if CT negative and suspicion persists) → CTA head (if SAH confirmed, to identify aneurysm)
- **Meningitis:** LP (cell count, protein, glucose, gram stain, culture, HSV PCR), blood cultures, procalcitonin
- **Temporal arteritis:** ESR, CRP, CBC (thrombocytosis), temporal artery biopsy (definitive)
- **CVT:** CT venogram or MR venogram
- **Cervical artery dissection:** CTA head/neck
- **CO poisoning:** Carboxyhemoglobin level (ABG or co-oximetry — pulse ox unreliable)
- **AACG:** IOP measurement (tonometry), slit lamp exam

## Treatment

Treatment targets the specific diagnosis. Stabilization:

- **SAH confirmed:** Strict BP control (SBP < 160), nimodipine 60 mg PO q4h (vasospasm prevention), emergent neurosurgical consultation, seizure precautions. Avoid antifibrinolytics without neurosurgical guidance.
- **Meningitis suspected:** Vancomycin 25-30 mg/kg IV + ceftriaxone 2 g IV + dexamethasone 0.15 mg/kg IV (give dexamethasone before or with antibiotics)
- **Temporal arteritis with visual symptoms:** Methylprednisolone 1 g IV daily, emergent ophthalmology consult
- **Temporal arteritis without visual symptoms:** Prednisone 60 mg PO daily, urgent ophthalmology and rheumatology follow-up
- **Migraine (after excluding secondary causes):** Metoclopramide 10 mg IV + diphenhydramine 25 mg IV + ketorolac 15-30 mg IV. Or prochlorperazine 10 mg IV. Sumatriptan 6 mg SC for refractory (contraindicated in hemiplegic migraine, basilar migraine, uncontrolled HTN, recent stroke/MI).
- **Tension headache:** NSAID (ibuprofen 600-800 mg PO or ketorolac 15-30 mg IV). Acetaminophen 1 g PO.
- **AACG:** Timolol 0.5% 1 drop, brimonidine 0.15% 1 drop, pilocarpine 2% 1 drop q15min x 2, acetazolamide 500 mg IV, mannitol 1-2 g/kg IV for refractory IOP elevation. Emergent ophthalmology for iridotomy.

## Disposition

- **ICU/neurosurgery:** SAH (surgical or endovascular aneurysm repair), large ICH, acute hydrocephalus
- **ICU/step-down:** Bacterial meningitis, HSV encephalitis, hypertensive emergency with PRES, CVT with hemorrhagic conversion
- **Telemetry/floor:** CVT on anticoagulation, temporal arteritis initiated on high-dose steroids, subdural hematoma (non-operative)
- **Observation:** Headache with completed negative SAH workup (CT + LP) but atypical features, headache not responding to standard migraine treatment
- **Discharge with follow-up:**
  - Migraine with typical features, prior history, response to treatment, normal exam
  - Tension headache with no red flags
  - Negative SAH workup (CT + LP) in well-appearing patient
  - Ensure clear return precautions: "return immediately for sudden severe headache, fever, neck stiffness, weakness, vision changes, confusion"
- **Ophthalmology:** AACG (same-day or emergent), temporal arteritis with visual symptoms (emergent)

## Pitfalls

1. **"Migraine" in a patient without prior migraine history.** First-worst headache in a patient with no established migraine pattern requires secondary headache evaluation. Do not diagnose new-onset migraine in the ED without imaging.

2. **Relying on headache severity to rule out SAH.** SAH presents as mild or moderate headache in up to 30% of cases. The defining feature is thunderclap onset (maximum intensity within seconds), not absolute severity. A "3/10" thunderclap headache still requires SAH workup.

3. **Skipping LP because CT is negative.** CT sensitivity for SAH drops below 95% beyond 6 hours from onset. LP is the definitive test after negative CT when clinical suspicion for SAH persists (ACEP Level B recommendation).

4. **Missing temporal arteritis in patients > 50.** Untreated temporal arteritis causes permanent bilateral blindness. ESR can be normal in 4% of biopsy-proven cases — check both ESR and CRP. Jaw claudication has the highest positive likelihood ratio (~34) for temporal arteritis.

5. **Attributing severe headache to hypertension without evaluating for SAH.** Hypertension is a common finding in SAH (catecholamine surge). A patient with BP 220/120 and thunderclap headache needs CT and LP for SAH before being managed as hypertensive emergency.

6. **Missing CO poisoning in household headache clusters.** If multiple household members present with headache (especially in winter), check carboxyhemoglobin. Pulse oximetry is falsely reassuring.

7. **Failure to consider postpartum/pregnancy-related causes.** Eclampsia, PRES, CVT, and postpartum preeclampsia can present up to 6 weeks postpartum. Any new headache in a pregnant or recently postpartum patient is an emergency until proven otherwise.

8. **Anchoring on "sinus headache."** Most self-diagnosed sinus headaches are migraine. However, sphenoid sinusitis can cause deep midface/vertex headache and is difficult to diagnose clinically — complications include cavernous sinus thrombosis and meningitis. CT sinuses if clinical concern.
