---
id: tension-headache
condition: Tension-Type Headache
aliases: [tension headache, TTH, muscle contraction headache, episodic tension-type headache, chronic tension-type headache]
icd10: [G44.20, G44.201, G44.209, G44.21, G44.219, G44.22, G44.229]
esi: 4
time_to_harm: "N/A — benign primary headache; see escalation_triggers for emergency differential"
category: neurological
track: tier1
disposition_default: outpatient
escalation_triggers:
  - "Thunderclap onset: headache reaching maximal intensity within 60 seconds — SAH until proven otherwise"
  - "Worst headache of life — evaluate for SAH regardless of prior similar headaches"
  - "Fever with headache and meningeal signs (neck stiffness, photophobia, Kernig, Brudzinski) — bacterial meningitis"
  - "Focal neurological deficits (hemiparesis, aphasia, visual field loss, diplopia) — stroke or intracranial lesion"
  - "New headache in patient with HIV, malignancy, or immunocompromise — opportunistic infection or metastasis"
  - "Papilledema on fundoscopy — elevated intracranial pressure"
  - "Positional headache: worse lying flat and relieved by sitting (↑ICP), or worse upright and relieved by recumbent (intracranial hypotension/CSF leak)"
  - "Headache with jaw claudication or scalp tenderness in patient >50 years — temporal arteritis"
  - "New headache in patient with known malignancy or hypercoagulable state"
  - "Headache following head trauma — intracranial hemorrhage"
confusion_pairs:
  - condition: subarachnoid-hemorrhage
    differentiators:
      - "TTH: gradual onset over minutes to hours; bilateral, pressing, tightening quality; mild-moderate intensity"
      - "SAH: thunderclap onset (peak intensity <60 seconds); often occipital-nuchal; 'worst headache of life'; nausea/vomiting common; may have transient LOC"
      - "TTH: no meningeal signs, no focal deficits, neurologically intact, hemodynamically stable"
      - "SAH: meningeal irritation within hours (may be absent in first hour); photophobia; may have oculomotor palsy (posterior communicating artery aneurysm)"
      - "Critical rule: any first thunderclap headache requires CT head then LP if CT negative — do not attribute to TTH without ruling out SAH"
sources:
  - type: guideline
    ref: "Headache Classification Committee of the International Headache Society (IHS). The International Classification of Headache Disorders, 3rd edition. Cephalalgia. 2018;38(1):1-211."
    pmid: "29368949"
  - type: guideline
    ref: "Silberstein SD, Holland S, Freitag F, et al. Evidence-based guideline update: pharmacological treatment for episodic migraine prevention in adults: report of the Quality Standards Subcommittee of the American Academy of Neurology and the American Headache Society. Neurology. 2012;78(17):1337-1345."
    pmid: "22529202"
  - type: pubmed
    ref: "Jensen R, Stovner LJ. Epidemiology and comorbidity of headache. Lancet Neurol. 2008;7(4):354-361."
    pmid: "18339350"
  - type: pubmed
    ref: "Perry JJ, Stiell IG, Sivilotti ML, et al. Sensitivity of computed tomography performed within six hours of onset of headache for diagnosis of subarachnoid haemorrhage: prospective cohort study. BMJ. 2011;343:d4277."
    pmid: "21791735"
  - type: pubmed
    ref: "Bendtsen L, Evers S, Linde M, et al. EFNS guideline on the treatment of tension-type headache — report of an EFNS task force. Eur J Neurol. 2010;17(11):1318-1325."
    pmid: "20482606"
  - type: review
    ref: "Loder E, Weizenbaum E, Frishberg B, Silberstein S. Choosing wisely in headache medicine: the American Headache Society's list of five things physicians and patients should question. Headache. 2013;53(10):1651-1659."
    pmid: "24107253"
last_updated: "2026-02-23"
compiled_by: agent
risk_tier: C
validation:
  schema_version: "2.0"
  automated_consistency_check: null
  dose_range_validator: null
  unit_normalization_check: null
  cross_file_consistency_check: null
  citation_presence_check: null
  duplicate_content_check: null
  outlier_detection_flag: clear
  guideline_version_reference: "ICHD-3 2018 (current)"
  provenance_links: []
---

## Recognition

Tension-type headache (TTH) is the most prevalent headache disorder globally, with a lifetime prevalence of 30-78%. It is a clinical diagnosis based on ICHD-3 criteria — no diagnostic testing required for typical presentation with a prior established pattern.

### ICHD-3 Diagnostic Criteria for Episodic Tension-Type Headache
Must fulfill ALL of the following:
- **A**: At least 10 headache episodes; frequency defines subtype:
  - Infrequent episodic: <1 day/month (<12 days/year)
  - Frequent episodic: 1-14 days/month (12-179 days/year)
  - Chronic: ≥15 days/month for >3 months
- **B**: Duration 30 minutes to 7 days
- **C**: At least TWO of the following pain characteristics:
  - Bilateral location
  - Pressing or tightening quality (non-pulsating)
  - Mild to moderate intensity (does not prohibit activity)
  - Not aggravated by routine physical activity (walking, climbing stairs)
- **D**: BOTH of the following:
  - No nausea or vomiting
  - No more than one of: photophobia or phonophobia (but not both)
- **E**: Not better accounted for by another ICHD-3 diagnosis

### Typical Clinical Presentation
- Bilateral, band-like or "hatband" pressure around the head
- Mild-to-moderate intensity (patient can continue activities despite headache)
- Non-throbbing (distinguish from migraine's pulsatile quality)
- No phonophobia + photophobia simultaneously (may have one, not both)
- No nausea or vomiting (nausea = migraine until proven otherwise)
- May have pericranial muscle tenderness (temporalis, trapezius, sternocleidomastoid)
- Duration 30 minutes to days; resolves with rest, sleep, or analgesics
- Typically associated with stress, poor sleep, dehydration, or prolonged screen time

### Key Features That Distinguish TTH from SAH
- TTH builds gradually (minutes to hours); SAH is thunderclap (peak <60 seconds)
- TTH: neurologically intact; no meningeal signs; no fever; hemodynamically stable
- TTH in a patient with established, identical prior headaches: diagnostic confidence is higher — but first-ever thunderclap must always be evaluated for SAH

## Critical Actions

Outpatient management — primary headache disorder not requiring emergency intervention.

1. Apply "SNOOP4" red flag screen to every headache presentation before attributing to TTH:
   - **S**ystemic symptoms (fever, weight loss, HIV/malignancy)
   - **N**eurological deficits (focal signs, altered consciousness)
   - **O**nset sudden (thunderclap — must evaluate for SAH)
   - **O**nset after age 50 (new headache — evaluate for temporal arteritis, malignancy)
   - **P**ositional (worse lying flat = ↑ICP; worse upright = CSF leak)
   - **P**rogressive headache pattern (worsening over weeks)
   - **P**apilledema
   - **P**recipitated by Valsalva (cough, sneeze, exertion — suggests ICP or vascular)
2. For confirmed TTH with prior established pattern: treat with simple analgesics and address precipitating factors.
3. For new-onset thunderclap headache: CT head immediately, then LP (>12 hours after onset for xanthochromia) if CT negative. Do not attribute to TTH without excluding SAH.
4. Arrange primary care follow-up for headache diary, identification of triggers, and preventive therapy if episodic headaches occur ≥4 days/month.

## When NOT to Escalate

TTH is appropriate for outpatient management when ALL of the following are met:
- Gradual onset (NOT thunderclap)
- Prior established identical headache pattern
- Bilateral, pressing/tightening quality, mild-to-moderate intensity
- Normal neurological examination
- No fever, no meningeal signs
- No focal neurological deficits
- Headache improves with analgesics
- No papilledema on fundoscopy
- Not "worst headache of life"

Emergency workup is NOT required for: chronic TTH with identical pattern responding to OTC analgesics, patient requesting refill of preventive medications, or headache in a low-risk patient without any SNOOP4 red flags.

## Differential Diagnosis

| Condition | Onset | Quality | Severity | Key Distinguishing Features |
|-----------|-------|---------|----------|----------------------------|
| **Tension-type headache** | Gradual (hours) | Pressing, bilateral, band-like | Mild-moderate | No nausea/vomiting, no photophobia + phonophobia together, not aggravated by activity |
| **Subarachnoid hemorrhage** | Thunderclap (<60 seconds to peak) | Severe, often occipital | Worst of life | Meningeal signs (may take hours), nausea/vomiting, possible LOC, oculomotor palsy |
| **Migraine without aura** | Gradual (1-72 hours) | Unilateral, pulsating | Moderate-severe | Nausea/vomiting, photophobia + phonophobia, aggravated by activity, may have prodrome |
| **Cervicogenic headache** | Variable | Unilateral, neck-referred | Mild-moderate | Neck tenderness, restricted ROM, headache provoked by neck movement or palpation |
| **Temporal arteritis** | Subacute | Temporal, aching | Moderate-severe | Age >50, ESR >50, tender temporal artery, jaw claudication, visual disturbance |
| **Idiopathic intracranial hypertension (IIH)** | Progressive | Diffuse, worse lying flat | Moderate-severe | Obese female, papilledema, visual disturbance, pulsatile tinnitus |
| **Medication-overuse headache** | Daily or near-daily | Variable, blends with baseline | Moderate | Analgesic or triptan use >10-15 days/month; headache improves with medication withdrawal |
| **Bacterial meningitis** | Hours | Diffuse, severe | Severe | Fever, neck stiffness, photophobia, Kernig/Brudzinski, altered mental status, purpuric rash |
| **Carbon monoxide poisoning** | Onset with exposure | Diffuse, bilateral | Moderate | Multiple affected household members, CO source, carboxyhemoglobin elevated |

## Workup

### No Workup Required (Typical TTH)
- Clinical diagnosis based on ICHD-3 criteria
- No neuroimaging required for: typical TTH with prior established pattern, normal neurological exam, no red flags
- American Headache Society Choosing Wisely: "Don't perform neuroimaging studies in patients with stable headaches that meet criteria for migraine/tension-type headache"

### When to Image
- **Non-contrast CT head**: thunderclap headache (>97% sensitivity within 6 hours if interpreted by experienced radiologist); trauma; suspected IIH with papilledema
- **MRI brain with and without contrast**: if progressive pattern, focal deficits, new-onset after age 50, HIV/immunocompromise, or prior malignancy
- **CT angiography**: if CT negative for thunderclap headache and clinical suspicion for aneurysm (lumbar puncture is the next step, but CTA may be performed simultaneously)

### SAH Exclusion Protocol (Thunderclap Headache)
1. Non-contrast CT head within 6 hours of onset (>97% sensitivity)
2. If CT negative: LP >12 hours after headache onset — sample tubes 1 and 4 for cell count; centrifuge for xanthochromia (spectrophotometry preferred; visual inspection adequate if spectrophotometry unavailable)
3. If LP xanthochromia positive or CT positive: neurosurgery consult, CTA for aneurysm location

### For Chronic Headache Pattern
- Thyroid function tests: hypothyroidism causes headache
- CBC, metabolic panel: anemia, uremia, hepatic encephalopathy
- Headache diary: document frequency, duration, severity, triggers for preventive therapy decision

## Treatment

### Acute (Episodic TTH — Abortive)
- **Aspirin 650-1000 mg PO**: first-line for acute TTH; NNT approximately 5 for complete headache relief at 2 hours
- **Ibuprofen 400-800 mg PO**: first-line; similar efficacy to aspirin
- **Acetaminophen 1000 mg PO**: slightly less effective than NSAIDs but useful when NSAIDs contraindicated
- **Combination analgesic** (aspirin 500 mg + acetaminophen 500 mg + caffeine 130 mg): superior to single agents; caffeine potentiates analgesic effect — limit to 2 doses/week to avoid medication-overuse headache

Avoid: opioids, barbiturates, butalbital-containing compounds — all have high medication-overuse potential and worsen long-term headache burden.

### Preventive (Chronic TTH or Frequent Episodic — ≥4 days/month)
- **Amitriptyline 10-75 mg PO at bedtime**: most evidence-based preventive for TTH; start 10 mg, titrate every 2-4 weeks; response seen at 4-8 weeks; NNT approximately 3 for 50% headache reduction
- **Mirtazapine 15-30 mg PO at bedtime**: alternative, especially if amitriptyline poorly tolerated
- **Venlafaxine 75-150 mg PO daily**: SNRI option; evidence for TTH prevention

### Non-Pharmacologic (Strong Evidence)
- Cognitive-behavioral therapy (CBT): effective for chronic TTH; addresses stress and pain catastrophizing
- Relaxation training / biofeedback: comparable to amitriptyline in randomized trials for chronic TTH
- Physical therapy: pericranial muscle stretching, postural correction, cervicothoracic strengthening
- Sleep hygiene, hydration, regular meals, stress reduction — address precipitating factors

### Medication-Overuse Prevention
Any abortive medication used >10-15 days/month (NSAIDs >15 days; opioids/triptans >10 days) causes medication-overuse headache (MOH). Educate all TTH patients at every visit about MOH risk. Limit abortive medications to 2 days/week maximum.

## Disposition

### Discharge (Standard)
- All confirmed TTH without red flags: discharge with acute analgesic prescription, trigger identification, return precautions
- Chronic TTH: initiate or continue preventive therapy, schedule primary care or neurology follow-up in 4-6 weeks

### Return Precautions
- Thunderclap headache at any time
- Headache with fever and stiff neck
- Headache with focal neurological symptoms
- Worst headache of life
- Headache after trauma

### Follow-up
- Primary care: headache diary review, preventive therapy titration, behavioral interventions
- Neurology: chronic TTH unresponsive to amitriptyline, diagnostic uncertainty, or coexisting migraine

## Pitfalls

1. **Under-escalation: attributing a first thunderclap headache to tension headache.** Thunderclap headache (peak intensity <60 seconds) is SAH until proven otherwise. CT head within 6 hours has >97% sensitivity; LP >12 hours after onset provides definitive exclusion. A patient with classic BPPV, known anxiety, or chronic TTH who presents with a thunderclap event requires SAH exclusion regardless of history. The error of "sentinel bleed attributed to TTH" is one of the most litigation-generating missed diagnoses in emergency medicine.

2. **Over-escalation: neuroimaging for stable, typical TTH with established pattern.** Neuroimaging in patients with stable headaches meeting primary headache criteria and a normal neurological exam has a yield of <1% for clinically significant findings and does not reduce re-presentation or anxiety in the long term. Choosing Wisely guidelines explicitly caution against this practice.

3. **Failing to diagnose medication-overuse headache.** Patients with chronic daily headache who use NSAIDs, triptans, or opioids >10-15 days/month have medication-overuse headache as a perpetuating factor. Prescribing more analgesics worsens the condition. The key question: "How many days per month do you take pain medication for your headaches?" Withdrawal and preventive therapy are the treatment.

4. **Prescribing opioids for TTH.** Opioids are inferior to NSAIDs for acute headache, accelerate the transition to chronic daily headache, and carry substantial addiction risk. They are not appropriate for TTH management at any stage. If the headache cannot be controlled with NSAIDs + caffeine, reconsider the diagnosis.

5. **Missing temporal arteritis in patients >50 years with new headache.** New headache after age 50 is temporal arteritis until proven otherwise (ESR, CRP, temporal artery biopsy). Giant cell arteritis causes permanent vision loss in 15-20% of untreated cases. Empiric steroids while awaiting biopsy are appropriate when clinical suspicion is high.

6. **Anchoring on "tension" when meningismus is subtle.** Early bacterial meningitis may present with mild neck discomfort misattributed to muscle tension. Any headache with fever warrants careful assessment for meningeal signs. Jolt accentuation (worsening headache with horizontal head rotation at 2-3 Hz) has been described as a sensitive sign; absence does not exclude meningitis.
