---
id: subarachnoid-hemorrhage
condition: Subarachnoid Hemorrhage
aliases: [SAH, aneurysmal SAH, aSAH, thunderclap headache, ruptured cerebral aneurysm]
icd10: [I60.0, I60.1, I60.2, I60.7, I60.8, I60.9]
esi: 1
time_to_harm: "< 60 minutes"
mortality_if_delayed: "30-day mortality 35-50%; rebleeding mortality 70%"
category: neurological
track: tier1
sources:
  - type: guideline
    ref: "2023 AHA/ASA Guideline for the Management of Patients With Aneurysmal Subarachnoid Hemorrhage"
    doi: "10.1161/STR.0000000000000436"
  - type: pubmed
    ref: "Perry JJ et al. Clinical decision rules to rule out subarachnoid hemorrhage for acute headache. JAMA. 2013;310(12):1248-1255"
    pmid: "24065011"
  - type: pubmed
    ref: "Edlow JA et al. Clinical Policy: Critical Issues in the Evaluation and Management of Adult Patients Presenting to the Emergency Department With Acute Headache. Ann Emerg Med. 2019;74(4):e41-e74"
    pmid: "31543134"
  - type: pubmed
    ref: "Dubosh NM et al. Sensitivity of Early Brain Computed Tomography to Exclude Aneurysmal Subarachnoid Hemorrhage: A Systematic Review and Meta-Analysis. Stroke. 2016;47(3):750-755"
    pmid: "26797666"
last_updated: "2026-02-19"
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
  guideline_version_reference: "2023 AHA/ASA"
  provenance_links: []
---
# Subarachnoid Hemorrhage

## Recognition

**Classic presentation:**
- "Worst headache of my life" — sudden onset, maximal intensity within seconds to one minute (thunderclap headache)
- Nausea, vomiting, photophobia
- Neck stiffness/meningismus (may take hours to develop)
- Brief loss of consciousness at onset (up to 50% of cases)

**Associated findings:**
- Focal neurological deficits (cranial nerve III palsy — posterior communicating artery aneurysm)
- Seizure at onset (6-16%)
- Retinal/subhyaloid hemorrhages (Terson syndrome)
- Fever (chemical meningitis from subarachnoid blood)

**Atypical presentations (missed SAH):**
- Headache that has improved by ED arrival ("sentinel headache" from minor leak)
- Isolated neck pain or stiffness
- Syncope without headache
- Acute confusional state
- Headache with exertion, Valsalva, or coitus

**Hunt-Hess grading:**
- Grade I: Asymptomatic or mild headache
- Grade II: Moderate-severe headache, nuchal rigidity, cranial nerve palsy
- Grade III: Drowsiness, confusion, mild focal deficit
- Grade IV: Stupor, moderate-severe hemiparesis
- Grade V: Coma, decerebrate posturing

**Ottawa SAH Rule (sensitivity ~100% for ruling out SAH in alert patients):**
Any ONE of the following in patients >= 15 years with new severe headache reaching max intensity within 1 hour:
- Age >= 40 years
- Neck pain or stiffness
- Witnessed loss of consciousness
- Onset during exertion
- Thunderclap headache (instant peak)
- Limited neck flexion on exam

## Critical Actions

| Action | Target |
|---|---|
| Non-contrast CT head | < 25 minutes from presentation |
| Neurosurgery consultation | Immediately upon diagnosis |
| Blood pressure control | SBP < 160 mmHg before aneurysm secured |
| Aneurysm treatment (clip or coil) | Within 24 hours (ideally < 12 hours) |

1. **Non-contrast CT head:** Sensitivity ~98.7% within 6 hours of onset (Dubosh meta-analysis); sensitivity decreases to ~93% at 12 hours and ~85% at 24 hours
2. **If CT negative and clinical suspicion persists:** Lumbar puncture >= 6 hours after headache onset — look for xanthochromia (spectrophotometry preferred) and elevated RBCs that do not clear across tubes
3. **If CT negative and LP negative:** SAH excluded with high confidence. CT angiography only if very high pre-test probability despite negative CT/LP
4. **If CT positive or LP positive:** Immediate neurosurgery consultation and CTA to identify aneurysm
5. **SBP control:** Nicardipine 5-15 mg/hr IV targeting SBP < 160 mmHg (2023 AHA guideline) to reduce rebleeding risk
6. **Analgesia:** Acetaminophen 1 g IV q6h; fentanyl 25-50 mcg IV PRN for severe pain; avoid hypotension
7. **Seizure management if occurs:** Levetiracetam 1000-1500 mg IV (prophylactic anticonvulsants NOT routinely recommended per 2023 AHA guideline)

## Differential Diagnosis

- Migraine (gradual onset, aura, prior history — but SAH must be excluded in worst/first/different headache)
- Cerebral venous sinus thrombosis (headache, papilledema, focal deficits; CTV/MRV for diagnosis)
- Intracerebral hemorrhage (focal deficits, hypertension; CT shows parenchymal blood)
- Meningitis (fever, meningismus, toxic appearance; LP shows pleocytosis)
- Cervical artery dissection (neck pain, Horner syndrome, focal deficits)
- Hypertensive emergency with headache
- Reversible cerebral vasoconstriction syndrome (RCVS) — recurrent thunderclap headaches, vasoconstriction on angiography
- Pituitary apoplexy (sudden headache, visual field deficits, ophthalmoplegia)
- Acute angle-closure glaucoma (unilateral headache, red eye, fixed mid-dilated pupil)

## Workup

- **Non-contrast CT head:** First-line; obtain immediately
- **CT angiography (CTA):** Identifies aneurysm location and morphology; obtain simultaneously with CT head if SAH suspected
- **Lumbar puncture:** If CT negative and >= 6 hours from onset; send tube 1 and tube 4 for RBC count (failure to clear suggests SAH vs. traumatic tap); send supernatant for xanthochromia
- **CBC, BMP, coagulation studies (PT/INR, PTT), type and screen**
- **Troponin:** Neurogenic myocardial injury (stunned myocardium) occurs in up to 30% of SAH
- **ECG:** Deep T-wave inversions ("cerebral T waves"), QT prolongation, ST changes mimicking ACS
- **Cerebral angiography (DSA):** Gold standard for aneurysm identification; performed by neurosurgery/neurointerventional radiology
- **MRI/MRA:** If CT/LP equivocal; FLAIR sequence sensitive for subarachnoid blood
- **Transcranial Doppler:** Screening for vasospasm (post-admission, typically days 3-14)

## Treatment

### Blood Pressure Management (Pre-Aneurysm Securing)
- Target SBP < 160 mmHg (2023 AHA guideline)
- Nicardipine 5-15 mg/hr IV (preferred: titratable, no ICP effects)
- Labetalol 10-20 mg IV q10-20min as alternative
- Avoid nitroprusside (raises intracranial pressure)

### Rebleeding Prevention
- Aneurysm securing within 24 hours (endovascular coiling preferred over surgical clipping in most cases per ISAT trial)
- Bed rest, head of bed 30 degrees
- Stool softeners: docusate 100 mg PO BID (avoid Valsalva)
- Antiemetics: ondansetron 4 mg IV q6h PRN

### Vasospasm Prevention (Days 3-14)
- Nimodipine 60 mg PO/NG q4h for 21 days — the ONLY proven agent for improving neurological outcomes (reduces delayed cerebral ischemia)
- Maintain euvolemia (avoid hypovolemia; prophylactic hypervolemia NOT beneficial)
- If symptomatic vasospasm: induced hypertension and endovascular rescue (intra-arterial vasodilators, angioplasty)

### Hydrocephalus
- Occurs in 20-30% of SAH patients
- Emergent external ventricular drain (EVD) placement for acute obstructive hydrocephalus with declining consciousness

### Seizures
- Treat acute seizures with lorazepam 4 mg IV, then levetiracetam 1000-1500 mg IV
- Routine prophylactic anticonvulsants are NOT recommended (associated with worse outcomes per 2023 AHA guideline)

### Supportive
- Analgesics: acetaminophen 1 g IV q6h; fentanyl 25-50 mcg IV PRN (avoid NSAIDs — platelet inhibition)
- Normothermia: acetaminophen, cooling blankets for fever
- Glucose control: target 80-180 mg/dL; avoid hypoglycemia
- VTE prophylaxis: pneumatic compression devices immediately; pharmacologic prophylaxis after aneurysm secured

## Disposition

- **ICU/neuro-ICU:** All confirmed SAH patients — minimum 14-21 days ICU monitoring for vasospasm
- **Neurosurgery/neurointerventional radiology:** Emergent consultation for aneurysm treatment
- **Transfer:** If no neurosurgical capability, immediate transfer to comprehensive stroke center; stabilize BP before and during transport
- **Discharge from ED:** Only if SAH excluded (negative CT within 6 hours of a clearly defined headache onset, or negative CT + negative LP)

## Pitfalls

1. **Accepting a negative CT as excluding SAH beyond the 6-hour window.** CT sensitivity declines after 6 hours from symptom onset. A normal CT at 12 or 24 hours does NOT exclude SAH. Lumbar puncture is mandatory when CT is negative and clinical suspicion exists beyond the 6-hour window.

2. **Performing LP too early.** Xanthochromia from RBC lysis requires at least 6-12 hours to develop. LP performed within 6 hours of onset may show RBCs (indistinguishable from traumatic tap) without xanthochromia, yielding an indeterminate result.

3. **Dismissing headache as migraine because the patient has a history of migraines.** "First, worst, or different" headache in a migraine patient demands SAH workup. Sentinel leaks present as atypical headache in patients with prior headache history. 25-50% of missed SAH patients have a prior headache diagnosis.

4. **Attributing SAH-related ECG changes to acute coronary syndrome.** SAH causes neurogenic stunned myocardium with troponin elevation, T-wave inversions, and ST changes. Heparinizing or catheterizing these patients for presumed ACS while missing the SAH is catastrophic.

5. **Lowering blood pressure too aggressively before aneurysm is secured.** Cerebral perfusion depends on adequate MAP in SAH patients with elevated ICP. Target SBP < 160, not normalization. Hypotension causes cerebral ischemia.

6. **Failure to start nimodipine.** Nimodipine is the only agent proven to reduce poor outcomes from vasospasm. Initiate 60 mg PO/NG q4h immediately upon diagnosis and continue for 21 days. Administer PO/NG, NOT IV (IV nimodipine causes severe hypotension).

7. **Missing perimesencephalic SAH pattern.** Blood isolated to the perimesencephalic cisterns on CT has a much more benign prognosis (usually venous in origin, rarely aneurysmal). CTA is still required, but if negative, prognosis is excellent. Do not conflate this with aneurysmal SAH risk counseling.

8. **Discharging a patient with sentinel headache (warning leak).** Up to 50% of SAH patients report a preceding severe headache days to weeks before the catastrophic bleed. Any thunderclap headache requires full SAH workup regardless of spontaneous resolution.

9. **Using the "four-tube LP clearing" method alone to differentiate SAH from traumatic tap.** RBC clearing across tubes is unreliable. Xanthochromia (visual or spectrophotometric) is the key discriminator. Send fluid for spectrophotometry when available.
