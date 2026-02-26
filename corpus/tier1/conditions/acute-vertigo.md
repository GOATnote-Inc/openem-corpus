---
id: acute-vertigo
condition: Acute Vertigo
aliases: [vertigo, dizziness, acute vestibular syndrome, AVS, BPPV, benign paroxysmal positional vertigo, vestibular neuritis]
icd10: [R42, H81.10]
esi: 3
time_to_harm: "< 24 hours (posterior circulation stroke misdiagnosed as peripheral vertigo)"
mortality_if_delayed: "Posterior circulation stroke: up to 40% mortality if missed; cerebellar hemorrhage with herniation near 100% without surgical decompression"
category: neurological
track: tier1
sources:
  - type: guideline
    ref: "Edlow JA, et al. Guidelines for reasonable and appropriate care in the emergency department 3 (GRACE-3): Acute dizziness and vertigo in the emergency department. Acad Emerg Med. 2023;30(5):442-486"
    pmid: "37166022"
  - type: pubmed
    ref: "Kattah JC, Talkad AV, Wang DZ, et al. HINTS to diagnose stroke in the acute vestibular syndrome: three-step bedside oculomotor examination more sensitive than early MRI diffusion-weighted imaging. Stroke. 2009;40(11):3504-3510"
    pmid: "19762709"
  - type: review
    ref: "Edlow JA, Gurley KL, Newman-Toker DE. A new diagnostic approach to the adult patient with acute dizziness. J Emerg Med. 2018;54(4):469-483"
    pmid: "29395695"
  - type: meta-analysis
    ref: "Hilton MP, Pinder DK. The Epley (canalith repositioning) manoeuvre for benign paroxysmal positional vertigo. Cochrane Database Syst Rev. 2014;(12):CD003162"
    pmid: "25485940"
  - type: pubmed
    ref: "Newman-Toker DE, Moy E, Valente E, et al. Missed diagnosis of stroke in the emergency department: a cross-sectional analysis of a large population-based sample. Diagnosis (Berl). 2014;1(2):155-166"
    pmid: "28344918"
last_updated: "2026-02-19"
compiled_by: agent
risk_tier: C
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

## Recognition

### Why This Condition Matters

Acute vertigo is the highest-stakes ESI-3 condition. Approximately 3-5% of ED visits involve dizziness or vertigo. The central challenge: peripheral causes (benign) vastly outnumber central causes (dangerous), but missed posterior circulation stroke carries catastrophic consequences. CT has only 7-16% sensitivity for posterior fossa stroke in the first 24 hours. An estimated 15,000-165,000 cerebrovascular events are misdiagnosed annually in US EDs, with dizziness as a leading presenting symptom.

### Timing-and-Triggers Framework (GRACE-3)

Classify by onset pattern before attempting a specific diagnosis:

| Syndrome | Timing | Triggers | Key Diagnoses |
|----------|--------|----------|---------------|
| **Acute vestibular syndrome (AVS)** | Acute onset, continuous >24h | Spontaneous (not positional) | Vestibular neuritis, posterior circulation stroke |
| **Spontaneous episodic vestibular syndrome (s-EVS)** | Recurrent episodes, minutes to hours | Spontaneous | Vestibular migraine, Meniere disease, TIA |
| **Triggered episodic vestibular syndrome (t-EVS)** | Brief episodes <1 min | Head position change | BPPV, central positional vertigo |

### Red Flags for Central (Dangerous) Cause
- Acute onset with vascular risk factors (age >60, hypertension, diabetes, atrial fibrillation, prior stroke)
- Inability to walk (severe gait ataxia out of proportion to vertigo severity)
- Severe headache (especially occipital) with vertigo
- New-onset vertical diplopia or visual field deficit
- Limb dysmetria, dysphagia, dysarthria, Horner syndrome
- HINTS central pattern (see Critical Actions)
- Direction-changing nystagmus
- Skew deviation on alternate cover test

## Critical Actions

### The HINTS Exam (Acute Vestibular Syndrome Only)

HINTS is validated only for patients with acute vestibular syndrome (acute onset, continuous vertigo, nystagmus, nausea/vomiting, head-motion intolerance, gait instability lasting >24 hours). Do NOT apply HINTS to episodic or triggered vertigo.

When performed by a trained examiner in AVS, HINTS has >98% sensitivity and ~96% specificity for central cause (stroke), outperforming early MRI-DWI (sensitivity ~80% in first 48 hours).

**The three components:**

#### 1. Head Impulse Test (HI)
- Patient fixates on examiner's nose
- Examiner delivers small-amplitude, high-velocity, unpredictable horizontal head thrust
- **Normal (no corrective saccade) = DANGEROUS** -- suggests central lesion (stroke). The vestibulo-ocular reflex is intact because the vestibular nerve is intact; the problem is in the brainstem/cerebellum
- **Abnormal (corrective saccade back to target) = peripheral** -- vestibular nerve or labyrinth is damaged

#### 2. Nystagmus Type (N)
- Observe in primary gaze, then with gaze to left and right
- **Unidirectional, horizontal nystagmus** (fast phase away from lesion, intensifies with gaze toward fast phase) = peripheral
- **Direction-changing nystagmus** (changes direction with gaze direction) = DANGEROUS, central
- **Purely vertical or purely torsional nystagmus** = DANGEROUS, always central

#### 3. Test of Skew (TS)
- Alternate cover test: cover one eye, uncover, observe for vertical corrective movement
- **Positive skew deviation (vertical realignment on uncovering)** = DANGEROUS, central (brainstem lesion disrupting otolith-ocular pathways)
- **No skew** = peripheral (or central, so skew alone is not sufficient)

**Interpretation summary:**

| HINTS Finding | Pattern | Interpretation |
|---------------|---------|---------------|
| Head impulse **normal** | Central | DANGEROUS -- arrange urgent MRI, neurology consult |
| Nystagmus **direction-changing** | Central | DANGEROUS |
| Test of skew **positive** | Central | DANGEROUS |
| Head impulse **abnormal** + nystagmus **unidirectional** + skew **negative** | Peripheral | Consistent with vestibular neuritis |

Any single central sign = treat as central until proven otherwise.

### HINTS-Plus
- Add **acute unilateral hearing loss** (finger rub at each ear): new hearing loss on one side in AVS suggests AICA stroke (anterior inferior cerebellar artery), even if other HINTS components appear peripheral
- AICA stroke can mimic peripheral vertigo because AICA supplies both the labyrinth and brainstem

### Dix-Hallpike Maneuver (Triggered Episodic Vertigo)
For suspected BPPV (brief positional episodes, <1 min):
1. Patient seated on exam table, head turned 45 degrees to side being tested
2. Rapidly lay patient supine with head hanging 20 degrees below table edge
3. Observe eyes for 30 seconds
4. **Positive**: upbeating, torsional (geotropic) nystagmus with 2-5 second latency, crescendo-decrescendo pattern, fatiguing with repetition, lasting <60 seconds
5. Test both sides; the affected side is the side that provokes nystagmus
6. **Atypical nystagmus** (no latency, non-fatiguing, downbeating, purely vertical) = consider central positional vertigo (posterior fossa lesion)

### Immediate Actions
1. Assess ABCs, hemodynamic stability
2. Apply timing-and-triggers framework to classify the vertigo syndrome
3. For AVS: perform HINTS exam -- do NOT order CT head as a screening test (inadequate sensitivity for posterior fossa stroke)
4. For triggered episodic: perform Dix-Hallpike
5. Obtain fingerstick glucose (hypoglycemia mimics vertigo/dizziness)
6. Cardiac monitor if syncope or presyncope component
7. IV access if central cause suspected or persistent vomiting
8. Antiemetic for symptom control (ondansetron 4 mg IV preferred -- does not sedate or mask neurological exam)

## Differential Diagnosis

| Condition | Key Features | Duration | HINTS/Exam Pattern |
|-----------|-------------|----------|-------------------|
| **BPPV** | Positional brief episodes, Dix-Hallpike positive, upbeating torsional nystagmus with latency | Seconds (<1 min per episode) | Not applicable (triggered, not AVS) |
| **Vestibular neuritis** | Acute onset, constant vertigo, unidirectional horizontal nystagmus, positive head impulse test (abnormal), often post-viral | Days to weeks (peak 24-72h) | Peripheral HINTS pattern |
| **Meniere disease** | Episodic vertigo + fluctuating low-frequency hearing loss + tinnitus + aural fullness; attacks last 20 min to 12 hours | Hours per episode | Not applicable (episodic, not AVS) |
| **Posterior circulation stroke** | Acute onset, vascular risk factors, gait ataxia disproportionate to vertigo, HINTS central pattern, may have brainstem signs | Persistent | Central HINTS pattern: normal head impulse, direction-changing nystagmus, or skew deviation |
| **Cerebellar hemorrhage** | Sudden severe headache, inability to walk, vomiting, may deteriorate rapidly to obtundation; neurosurgical emergency | Persistent, progressive | Central pattern; CT head will show hemorrhage (unlike ischemic stroke) |
| **Multiple sclerosis** | Young adult, prior neurological episodes (optic neuritis, myelitis), internuclear ophthalmoplegia; MRI shows demyelination | Variable | Central pattern possible |
| **Vestibular migraine** | Episodic vertigo with migrainous features (headache, photophobia, phonophobia, visual aura), personal/family migraine history | Minutes to 72 hours per episode | Not applicable (episodic) |
| **Vertebrobasilar TIA** | Brief episodes of vertigo with vascular risk factors, often with other posterior circulation symptoms | Minutes (typically <1 hour) | May have transient central signs |
| **Labyrinthitis** | Same as vestibular neuritis PLUS acute hearing loss (sensorineural); if hearing loss present in AVS also consider AICA stroke | Days to weeks | Peripheral pattern but hearing loss requires AICA stroke exclusion |
| **Superior canal dehiscence** | Vertigo and oscillopsia triggered by loud sounds (Tullio phenomenon) or Valsalva/pressure changes; autophony; conductive hearing loss pattern with intact acoustic reflexes | Seconds per trigger | Not applicable (triggered) |

## Workup

### For Acute Vestibular Syndrome (AVS) -- Central Suspected
- **MRI brain with DWI sequences**: Required if HINTS central pattern or any red flag. CT is inadequate (7-16% sensitivity for posterior fossa ischemic stroke in first 24 hours). If initial MRI-DWI is negative but clinical suspicion is high, repeat MRI at 48-72 hours (false-negative rate up to 20% in first 24 hours for small brainstem strokes)
- **CTA head and neck or MRA**: If stroke suspected, evaluate vertebrobasilar circulation for dissection, stenosis, or occlusion
- **CT head without contrast**: Useful only to exclude cerebellar hemorrhage (CT is sensitive for hemorrhage). Do NOT rely on CT to exclude ischemic posterior fossa stroke
- **ECG**: Atrial fibrillation as embolic source
- **Basic labs**: CBC, BMP (glucose, electrolytes), coagulation studies if anticoagulated
- **Fingerstick glucose**: Immediate at bedside

### For BPPV (Triggered Episodic)
- **No imaging required** if classic Dix-Hallpike positive (upbeating torsional nystagmus with latency and fatigability)
- Imaging only if atypical nystagmus, persistent vertigo between positional triggers, or neurological signs

### For Vestibular Neuritis (Peripheral AVS Pattern)
- **No imaging required** if HINTS exam is convincingly peripheral in a low-risk patient
- Consider MRI if any diagnostic uncertainty, incomplete HINTS exam, or patient has significant vascular risk factors

### For Meniere Disease
- Audiometry (outpatient) showing fluctuating low-frequency sensorineural hearing loss
- MRI to exclude vestibular schwannoma or posterior fossa lesion (outpatient)

## Treatment

### Symptomatic Control

**Antiemetics (first-line for acute vomiting):**
- Ondansetron 4 mg IV/IM -- preferred in ED; does not cause sedation or mask neurological exam
- Ondansetron 4-8 mg ODT sublingual if no IV access

**Vestibular suppressants (short-term use only, max 3 days for peripheral causes):**
- Meclizine 25 mg PO q6h PRN -- first-line oral vestibular suppressant
- Dimenhydrinate 50 mg IV/PO q6h PRN -- alternative
- Diazepam 2-5 mg PO/IV q6-8h -- severe acute vestibular neuritis, use sparingly (impairs central compensation)

**Do NOT prescribe prolonged vestibular suppressants**: beyond 48-72 hours, vestibular suppressants delay central compensation and prolong recovery.

### BPPV-Specific: Epley Maneuver (Canalith Repositioning)

Perform immediately in ED for posterior canal BPPV (Dix-Hallpike positive):

1. Start with patient seated, head turned 45 degrees toward affected ear
2. Rapidly lay patient supine with head hanging 20 degrees below table (Dix-Hallpike position) -- hold 30 seconds or until nystagmus stops
3. Turn head 90 degrees to opposite side (still hanging) -- hold 30 seconds
4. Roll patient onto the shoulder of the side now facing down, turning head another 90 degrees (now facing floor) -- hold 30 seconds
5. Bring patient to seated position with chin tucked

**Efficacy**: Resolution of vertigo in 80% after single treatment; NNT = 2-3 (Cochrane review). May repeat 2-3 times in one session if first attempt unsuccessful. Recurrence rate approximately 36% over 1 year.

**Horizontal canal BPPV** (identified by horizontal nystagmus on supine roll test): treat with Lempert (BBQ roll) maneuver or Gufoni maneuver, not Epley.

### Vestibular Neuritis-Specific
- Short-course oral corticosteroids (controversial, modest evidence): methylprednisolone 100 mg PO/IV day 1, tapered over 3 weeks; or prednisone 60 mg PO daily x 5 days then taper. Most effective if started within 72 hours of symptom onset
- Early vestibular rehabilitation referral (strong evidence for improved recovery)
- Limit vestibular suppressants to 48-72 hours maximum

### Posterior Circulation Stroke
- Manage per acute ischemic stroke protocol (see acute-ischemic-stroke.md)
- IV alteplase 0.9 mg/kg (max 90 mg) if within window and eligible
- Emergent neurology and neurointerventional consultation
- BP management per stroke guidelines

### Cerebellar Hemorrhage
- Emergent neurosurgery consult for possible suboccipital decompression
- ICP management, airway protection
- Reverse anticoagulation if applicable

## Disposition

### Admit / ICU
- **Central pattern on HINTS**: admit for MRI, stroke workup, neurology consultation
- **Cerebellar hemorrhage**: ICU, neurosurgery
- **Posterior circulation stroke**: stroke unit or neuro-ICU per stroke protocol
- **Intractable vomiting** with dehydration unresponsive to ED treatment
- **Inability to ambulate safely** with no identified peripheral cause
- **Diagnostic uncertainty** in patient with vascular risk factors

### Discharge (Peripheral Cause Confirmed)
- **BPPV** after successful Epley: discharge with return precautions, ENT or vestibular therapy follow-up if recurrent
- **Vestibular neuritis** (HINTS peripheral, low-risk patient): discharge with meclizine 25 mg PO q6h PRN (max 3 days), vestibular rehabilitation referral, PCP follow-up in 1-2 weeks
- **Discharge instructions must include**: return immediately for new headache, focal weakness, numbness, speech difficulty, vision changes, inability to walk, or worsening symptoms

### Observation
- Moderate-risk patients where peripheral cause is likely but not certain -- observe 6-12 hours, reassess, trend exam

## Pitfalls

1. **Ordering CT to "rule out stroke" in acute vertigo.** CT has only 7-16% sensitivity for posterior fossa ischemic stroke in the first 24 hours. A normal CT provides false reassurance. MRI with DWI is the required imaging modality. CT is only useful for ruling out hemorrhage.

2. **Applying HINTS to the wrong patient.** HINTS is validated only in acute vestibular syndrome (continuous vertigo >24 hours with nystagmus). Using HINTS on patients with brief positional episodes (BPPV) or episodic spontaneous vertigo (Meniere, vestibular migraine) produces unreliable results.

3. **Attributing vertigo with hearing loss to labyrinthitis without excluding AICA stroke.** Anterior inferior cerebellar artery (AICA) supplies the labyrinth and lateral pons. AICA stroke presents with vertigo + acute unilateral hearing loss and can mimic labyrinthitis. HINTS-Plus (adding hearing assessment) catches this. New hearing loss in AVS requires vascular imaging.

4. **Prescribing vestibular suppressants beyond 72 hours for peripheral vertigo.** Meclizine, dimenhydrinate, and benzodiazepines suppress the central compensation process that is essential for recovery from vestibular neuritis. Limit to 48-72 hours. Prescribe vestibular rehabilitation instead.

5. **Discharging a patient who cannot walk without thorough central-cause exclusion.** Severe gait ataxia disproportionate to the degree of vertigo is a red flag for cerebellar stroke. Patients with peripheral vertigo may be unsteady but can generally walk with assistance. Inability to sit upright or stand suggests central pathology.

6. **Performing the Dix-Hallpike incorrectly and missing BPPV.** The head must hang below the table edge (at least 20 degrees of extension). Insufficient head extension produces false-negative results. Each side must be tested separately. Wait at least 30 seconds per position -- latency of nystagmus onset is a defining feature.

7. **Anchoring on "benign" diagnosis in a patient with vascular risk factors.** A 65-year-old with hypertension, diabetes, and atrial fibrillation presenting with acute continuous vertigo has posterior circulation stroke until proven otherwise. Even if the HINTS exam appears peripheral, the threshold for MRI should be low in high-risk patients. HINTS sensitivity, while excellent, is operator-dependent.

8. **Failing to reassess after antiemetic treatment.** Ondansetron controls nausea but does not treat the underlying cause. A patient who "feels better" after antiemetics may still have central vertigo. Always perform the neurological exam and HINTS assessment before and after symptomatic treatment, and base disposition on the exam, not symptom resolution.

9. **Missing a negative initial MRI-DWI in posterior fossa stroke.** MRI-DWI has a false-negative rate of up to 20% for small brainstem infarcts in the first 24 hours. If clinical suspicion for central cause remains high despite a negative initial MRI, the patient requires repeat MRI at 48-72 hours or inpatient observation with serial neurological exams.

10. **Confusing central positional vertigo with BPPV.** Central positional vertigo (from posterior fossa lesion) produces nystagmus on Dix-Hallpike that is atypical: no latency, non-fatiguing, downbeating, or purely vertical. Any atypical Dix-Hallpike response requires brain imaging.
