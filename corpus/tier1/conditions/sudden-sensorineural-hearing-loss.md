---
id: sudden-sensorineural-hearing-loss
condition: Sudden Sensorineural Hearing Loss
aliases: [SSNHL, sudden deafness, idiopathic sudden hearing loss, sudden unilateral hearing loss]
icd10: [H91.20, H91.21, H91.22, H91.23]
esi: 2
time_to_harm: "< 72 hours — hearing recovery depends on early steroid treatment; beyond 2 weeks, recovery unlikely"
category: neurological
track: tier1
confusion_pairs:
  - condition: acute-ischemic-stroke
    differentiators:
      - "SSNHL: isolated unilateral hearing loss without focal neurological deficits, Weber lateralizes to unaffected ear, no limb weakness or facial droop"
      - "AICA stroke: hearing loss accompanied by vertigo, ipsilateral facial weakness, cerebellar signs (ataxia, dysmetria, nystagmus), Horner syndrome"
      - "SSNHL: normal neurological exam; AICA stroke: crossed findings, gait instability, inability to perform finger-to-nose"
      - "Isolated sudden hearing loss with vertigo and no other neuro findings can still be AICA territory — MRI with DWI required to exclude"
  - condition: bacterial-meningitis
    differentiators:
      - "SSNHL: afebrile, isolated unilateral hearing loss, no meningeal signs, non-toxic appearance"
      - "Bacterial meningitis: fever, headache, neck stiffness, photophobia, altered mental status, may have bilateral hearing loss"
      - "SSNHL: normal WBC, normal CSF if sampled; meningitis: leukocytosis, CSF pleocytosis with elevated protein and low glucose"
sources:
  - type: guideline
    ref: "Chandrasekhar SS et al. Clinical Practice Guideline: Sudden Hearing Loss (Update). Otolaryngol Head Neck Surg 2019;161(1_suppl):S1-S45"
    pmid: "31369359"
  - type: pubmed
    ref: "Stachler RJ et al. Clinical Practice Guideline: Sudden Hearing Loss. Otolaryngol Head Neck Surg 2012;146(3_suppl):S1-S35"
    pmid: "22383545"
  - type: review
    ref: "Rauch SD. Idiopathic Sudden Sensorineural Hearing Loss. N Engl J Med 2008;359:833-840"
    pmid: "18716300"
  - type: pubmed
    ref: "Kuhn M et al. Sudden Sensorineural Hearing Loss: A Review of Diagnosis, Treatment, and Prognosis. Trends Amplif 2011;15:91-105"
    pmid: "21606048"
last_updated: "2026-03-06"
compiled_by: agent
risk_tier: B
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
# Sudden Sensorineural Hearing Loss

## Recognition

**Definition:** Sensorineural hearing loss of at least 30 dB over at least 3 contiguous audiometric frequencies occurring within 72 hours. Most commonly unilateral (bilateral in < 5%). Annual incidence: 5-27 per 100,000. Peak age: 43-53 years, equal sex distribution. Approximately 85% of cases are idiopathic; identifiable causes include vascular (AICA stroke), infectious (viral cochleitis), autoimmune (Cogan syndrome), neoplastic (vestibular schwannoma), and traumatic (perilymphatic fistula).

**Clinical Features:**
- Sudden unilateral hearing loss — often noticed upon waking or as a single discrete event
- Aural fullness (sensation of ear blockage or pressure)
- Tinnitus (present in 70-80% of cases)
- Vertigo or disequilibrium (present in 30-40%, associated with worse prognosis)
- No otalgia, no otorrhea, no fever
- Normal otoscopic exam (tympanic membrane intact, no middle ear effusion)

**Red Flags for Underlying Cause:**
- Hearing loss with vertigo, facial weakness, or cerebellar signs — AICA stroke until proven otherwise
- Bilateral SSNHL — consider autoimmune inner ear disease, meningitis, syphilis, or bilateral vascular event
- Progressive (not sudden) hearing loss with unilateral tinnitus — vestibular schwannoma (acoustic neuroma)
- History of recent head trauma or barotrauma — perilymphatic fistula

## Critical Actions

1. **Perform bedside hearing assessment** — Weber and Rinne tuning fork tests (512 Hz). Weber: sound lateralizes to the unaffected ear in sensorineural loss (lateralizes to affected ear in conductive loss). Rinne: air conduction > bone conduction on the affected side (abnormal Rinne = bone > air = conductive loss, not SSNHL).
2. **Rule out conductive causes** — inspect the ear canal for cerumen impaction, foreign body, otitis externa. Examine the TM for perforation, hemotympanum, middle ear effusion. Conductive causes are far more common than SSNHL in the ED.
3. **Perform a complete neurological exam** — focused on cranial nerves (especially V, VII, VIII), cerebellar function (finger-to-nose, heel-to-shin, gait), and nystagmus assessment. Any focal neurological deficit = emergent MRI to rule out AICA stroke.
4. **Initiate corticosteroids** — oral prednisone 60 mg/day (or 1 mg/kg/day, max 60 mg) for 10-14 days with taper. Treatment within 72 hours is associated with significantly better hearing recovery. Do not delay steroids waiting for audiogram.
5. **Urgent ENT referral** — audiogram within 24-48 hours to confirm diagnosis and quantify loss. ENT follow-up within 1-2 weeks for repeat audiometry and consideration of intratympanic steroid salvage therapy.
6. **Order MRI with gadolinium** — to rule out vestibular schwannoma (retrocochlear pathology). Not emergent unless focal neurological findings are present, but should be obtained within 4-6 weeks.
7. **If stroke suspected (hearing loss + vertigo + neuro findings)** — emergent MRI with DWI. Do not rely on CT (insufficient sensitivity for posterior fossa ischemia). Activate stroke protocol if within treatment window.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Cerumen impaction | Conductive loss, visible cerumen on otoscopy, Weber lateralizes to affected ear, Rinne: bone > air |
| Otitis media with effusion | Conductive loss, TM retracted or with effusion, recent URI, Weber to affected ear |
| Otitis externa | Ear pain, canal edema/erythema, tragal tenderness, hearing loss from canal obstruction |
| AICA stroke | Hearing loss + vertigo + facial weakness + cerebellar signs, acute onset, MRI DWI positive |
| Vestibular schwannoma | Gradual unilateral hearing loss (not sudden), tinnitus, MRI shows CPA mass; 1-3% of SSNHL cases |
| Meniere disease | Episodic hearing loss (fluctuating, low-frequency initially), vertigo attacks lasting hours, aural fullness, tinnitus |
| Autoimmune inner ear disease | Bilateral progressive sensorineural hearing loss over weeks-months, may respond to steroids, associated with systemic autoimmune disease |
| Perilymphatic fistula | History of barotrauma, straining, or head trauma; hearing loss + vertigo; positive fistula test (nystagmus with pneumatic otoscopy) |
| Ototoxic medications | Bilateral, often gradual; history of aminoglycosides, cisplatin, loop diuretics, high-dose aspirin |

## Workup

**Bedside:**
- Otoscopy — exclude external and middle ear pathology (cerumen, TM perforation, effusion)
- 512 Hz tuning fork — Weber test (lateralizes to unaffected ear in SSNHL) and Rinne test (air > bone bilaterally in SSNHL)
- Finger rub test — gross assessment of unilateral hearing loss at bedside
- Complete cranial nerve exam including corneal reflex (V), facial symmetry (VII), vestibular function (VIII)
- HINTS exam if vertigo present — Head Impulse, Nystagmus, Test of Skew (differentiates peripheral from central vertigo)

**Labs:**
- CBC, BMP — baseline
- ESR, CRP — if autoimmune etiology suspected
- RPR/VDRL — syphilis screening (treatable cause of SSNHL)
- Lyme serology — in endemic areas
- ANA, RF — if bilateral or autoimmune disease suspected
- TSH — hypothyroidism associated with hearing loss

**Imaging:**
- MRI brain and IAC (internal auditory canal) with gadolinium — gold standard for excluding vestibular schwannoma and retrocochlear pathology. Order for all confirmed SSNHL (within 4-6 weeks unless neurological findings present)
- Emergent MRI with DWI — if any neurological deficits suggest AICA stroke
- CT temporal bone — only if concern for bony pathology (fracture, cholesteatoma, superior semicircular canal dehiscence)

**Audiometry:**
- Formal audiogram within 24-48 hours — confirms diagnosis (>= 30 dB sensorineural loss over >= 3 contiguous frequencies), quantifies severity, establishes baseline for monitoring recovery

## Treatment

**Corticosteroids (first-line, time-critical):**
- Oral prednisone 60 mg/day (or 1 mg/kg/day, max 60 mg) for 10-14 days, followed by 5-day taper
- If diabetes: coordinate with PCP, monitor blood glucose closely, may require insulin adjustment
- If oral steroids contraindicated (uncontrolled diabetes, active GI bleeding, psychosis): intratympanic dexamethasone 10 mg/mL (performed by ENT) — direct steroid delivery to the round window membrane

**Salvage therapy (if no improvement after 2-4 weeks of oral steroids):**
- Intratympanic dexamethasone 10 mg/mL or methylprednisolone 40 mg/mL — 3-4 injections over 2 weeks (ENT procedure)
- Combined oral + intratympanic steroids may be offered as initial therapy for severe loss (>= 70 dB) or profound loss

**Hyperbaric oxygen (adjunctive, limited evidence):**
- AAO-HNS guideline: may offer within 2-4 weeks of onset as adjunct to steroids in patients with incomplete recovery
- Typical protocol: 100% O2 at 2.0-2.4 ATA for 90 minutes daily x 10-20 sessions
- Limited availability, evidence quality low-moderate

**Antivirals:**
- No evidence supporting routine antiviral therapy (acyclovir, valacyclovir) in idiopathic SSNHL
- AAO-HNS guideline recommends against routine antiviral use

**Treat Underlying Cause (if identified):**
- AICA stroke: standard acute stroke management (thrombolytics if within window, antiplatelet, statin)
- Syphilis: penicillin G
- Autoimmune: immunosuppressive therapy under rheumatology
- Perilymphatic fistula: bed rest, head elevation, avoid straining; surgical repair if persistent

## Disposition

**Discharge with urgent outpatient follow-up (most SSNHL patients):**
- Initiate oral prednisone before discharge — do not defer to outpatient ENT
- Urgent ENT referral: audiogram and ENT evaluation within 24-48 hours
- MRI IAC with gadolinium: schedule within 4-6 weeks
- Syphilis screening sent from ED
- Return precautions: new neurological symptoms (facial weakness, vertigo, ataxia, diplopia, limb weakness), worsening hearing loss in contralateral ear

**Admit:**
- AICA stroke confirmed or strongly suspected — admit to stroke unit
- Bilateral sudden hearing loss — admit for workup (meningitis, autoimmune, bilateral vascular event)
- Severe vertigo with inability to ambulate safely
- Suicidal ideation related to sudden deafness (acute adjustment disorder — uncommon but real)

**ENT Follow-up:**
- All confirmed SSNHL patients require serial audiometry to track recovery
- If no improvement at 2-4 weeks, salvage intratympanic steroids
- If MRI shows vestibular schwannoma — neurosurgery/ENT co-management

## Pitfalls

1. **Diagnosing "ear infection" or "Eustachian tube dysfunction" without performing tuning fork tests.** Weber and Rinne take 30 seconds and differentiate sensorineural from conductive loss at bedside. A patient with sudden unilateral hearing loss and a normal ear exam has SSNHL until proven otherwise.

2. **Delaying steroid treatment.** Every day of delay reduces the probability of hearing recovery. Patients treated within 72 hours have significantly better outcomes than those treated after 1 week. Steroids should be started in the ED — do not wait for an audiogram to confirm the diagnosis.

3. **Missing AICA stroke.** Sudden hearing loss with vertigo can be the sole presentation of anterior inferior cerebellar artery ischemia. If any neurological findings accompany hearing loss (facial weakness, cerebellar signs, gaze-evoked nystagmus, limb ataxia), obtain emergent MRI with DWI. CT is inadequate for posterior fossa stroke.

4. **Failing to counsel on prognosis and urgency.** Patients may not perceive sudden hearing loss as an emergency. Clearly communicate that this is a time-sensitive condition with a narrow treatment window — hearing recovery is unlikely if treatment is delayed beyond 2 weeks.

5. **Not screening for vestibular schwannoma.** Approximately 1-3% of patients presenting with SSNHL have a vestibular schwannoma (acoustic neuroma). MRI with gadolinium of the internal auditory canals is required for all confirmed SSNHL to exclude this diagnosis.

6. **Assuming bilateral sudden hearing loss is a benign process.** Bilateral SSNHL is rare and warrants an aggressive workup for systemic causes: bacterial meningitis, autoimmune inner ear disease, neurosyphilis, Cogan syndrome, or bilateral vascular events. Admit for expedited evaluation.

7. **Prescribing ototoxic medications without audiometric monitoring.** In a patient with SSNHL, avoid aminoglycosides, high-dose loop diuretics, and cisplatin if at all possible. If these are medically necessary, coordinate with ENT for serial audiometry.
