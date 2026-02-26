---
id: benign-positional-vertigo
condition: Benign Paroxysmal Positional Vertigo
aliases: [BPPV, canalithiasis, cupulolithiasis, positional vertigo]
icd10: [H81.10, H81.11, H81.12, H81.13]
esi: 4
time_to_harm: "N/A — benign condition; see escalation_triggers for emergency differential"
category: neurological
track: tier1
disposition_default: outpatient
escalation_triggers:
  - "Acute onset continuous vertigo lasting >24 hours (acute vestibular syndrome — must exclude posterior circulation stroke)"
  - "Focal neurological deficits: diplopia, dysarthria, dysphagia, facial numbness, limb ataxia"
  - "Severe occipital headache accompanying vertigo"
  - "Inability to ambulate due to severe gait ataxia disproportionate to degree of vertigo"
  - "HINTS central pattern on bedside examination (normal head impulse test, direction-changing nystagmus, skew deviation)"
  - "New unilateral hearing loss with acute vertigo (suspect AICA stroke)"
  - "Vertical or torsional nystagmus without positional trigger"
  - "Vascular risk factors with first episode of positional vertigo in patient >60 years"
confusion_pairs:
  - condition: acute-ischemic-stroke
    differentiators:
      - "BPPV: brief episodes <60 seconds each, triggered by specific head positions, no neurological deficits"
      - "Posterior stroke: continuous vertigo, gait ataxia out of proportion to vertigo, HINTS central pattern"
      - "BPPV: positive Dix-Hallpike with upbeating torsional nystagmus with latency and fatigability"
      - "Posterior stroke: Dix-Hallpike may produce atypical nystagmus (no latency, non-fatiguing, downbeating)"
      - "BPPV: no headache, no focal deficits, hemodynamically normal"
sources:
  - type: guideline
    ref: "Bhattacharyya N, Gubbels SP, Schwartz SR, et al. Clinical Practice Guideline: Benign Paroxysmal Positional Vertigo (Update). Otolaryngol Head Neck Surg. 2017;156(3_suppl):S1-S47."
    pmid: "28248609"
  - type: meta-analysis
    ref: "Hilton MP, Pinder DK. The Epley (canalith repositioning) manoeuvre for benign paroxysmal positional vertigo. Cochrane Database Syst Rev. 2014;(12):CD003162."
    pmid: "25485940"
  - type: pubmed
    ref: "Fife TD, Iverson DJ, Lempert T, et al. Practice parameter: therapies for benign paroxysmal positional vertigo (an evidence-based review): report of the Quality Standards Subcommittee of the American Academy of Neurology. Neurology. 2008;70(22):2067-2074."
    pmid: "18505980"
  - type: guideline
    ref: "Edlow JA, et al. Guidelines for reasonable and appropriate care in the emergency department 3 (GRACE-3): Acute dizziness and vertigo in the emergency department. Acad Emerg Med. 2023;30(5):442-486."
    pmid: "37166022"
  - type: pubmed
    ref: "Kattah JC, Talkad AV, Wang DZ, et al. HINTS to diagnose stroke in the acute vestibular syndrome: three-step bedside oculomotor examination more sensitive than early MRI diffusion-weighted imaging. Stroke. 2009;40(11):3504-3510."
    pmid: "19762709"
last_updated: "2026-02-23"
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
  guideline_version_reference: "AAO-HNS 2017 CPG (current)"
  provenance_links: []
---

## Recognition

BPPV is the most common cause of peripheral vertigo, accounting for approximately 50% of all vertigo cases. Caused by free-floating calcium carbonate crystals (otoconia) displaced from the utricle into a semicircular canal, most commonly the posterior canal (~85-90% of cases).

### Classic Presentation
- Brief episodes of rotational vertigo, each lasting <60 seconds (typically 10-30 seconds)
- Triggered by specific head positions: lying down, rolling over in bed, looking up ("top-shelf vertigo"), bending forward
- Episodes are reproducible with the same trigger
- Nausea common; vomiting less common; no hearing loss; no tinnitus; no neurological symptoms
- Between episodes: patient feels well; no continuous vertigo

### Timing-and-Triggers Classification (GRACE-3)
BPPV falls in the triggered episodic vestibular syndrome (t-EVS) category: brief (<1 minute) episodes provoked by head position changes. This classification distinguishes it from:
- Acute vestibular syndrome (AVS): continuous vertigo >24 hours — requires HINTS exam to exclude stroke
- Spontaneous episodic vestibular syndrome (s-EVS): episodic without positional trigger — consider Meniere disease, vestibular migraine

### Dix-Hallpike Findings (Positive Test — Posterior Canal BPPV)
- 2-5 second latency before nystagmus onset
- Upbeating, torsional (geotropic, fast phase toward affected ear) nystagmus
- Crescendo-decrescendo intensity pattern
- Duration <60 seconds
- Fatigues with repeated testing (amplitude decreases)
- Affected side = side of Dix-Hallpike position that elicits nystagmus

### Supine Roll Test (Horizontal Canal BPPV, ~10-15% of cases)
- Horizontal nystagmus provoked by supine head rotation
- Geotropic (toward ground): canalithiasis — treat with Lempert (BBQ roll) or Gufoni maneuver
- Apogeotropic (away from ground): cupulolithiasis — treat with modified Gufoni or Appiani maneuver

## Critical Actions

Outpatient management — no emergency interventions required for confirmed BPPV.

1. Perform bilateral Dix-Hallpike to confirm diagnosis and identify affected side. Do not skip the diagnostic step and proceed to Epley without confirmation.
2. Perform canalith repositioning (Epley maneuver) immediately after positive Dix-Hallpike. Single treatment resolves symptoms in approximately 80% of patients (NNT = 2-3).
3. For horizontal canal BPPV (positive supine roll test with horizontal nystagmus): use Lempert (BBQ roll) maneuver rather than Epley.
4. Prescribe vestibular suppressants only if repositioning maneuver cannot be performed or patient has refractory nausea. Do NOT prescribe as routine outpatient treatment — they delay central compensation.
5. Provide return precautions: written instructions to return if continuous vertigo lasting >24 hours, new headache, focal neurological symptoms, or inability to walk.
6. Arrange outpatient ENT or vestibular physical therapy follow-up for recurrent BPPV or failure to resolve after 2-3 repositioning attempts.

## When NOT to Escalate

BPPV is appropriate for outpatient management when ALL of the following are met:
- Episodes are brief (<60 seconds each) and triggered exclusively by specific head position changes
- Positive Dix-Hallpike with classic upbeating torsional nystagmus with latency and fatigability
- No continuous vertigo between triggered episodes
- Normal neurological examination (no focal deficits, no gait ataxia disproportionate to vertigo)
- No new occipital or thunderclap headache
- Patient can ambulate (even if unsteady during triggered episodes)
- No vascular risk factors with atypical presentation (age >60 with first episode + hypertension + diabetes or atrial fibrillation warrants lower threshold for imaging)

ED or urgent care is NOT required for: classic Dix-Hallpike positive BPPV with successful Epley in a low-risk patient. Primary care or urgent care can manage recurrent episodes with Epley if the diagnosis is established.

## Differential Diagnosis

| Condition | Duration | Trigger | Key Distinguishing Features |
|-----------|----------|---------|----------------------------|
| **BPPV (posterior canal)** | Seconds (<60s) | Head position change | Dix-Hallpike positive with latency, upbeating torsional nystagmus, fatigues |
| **Central positional vertigo** (posterior fossa lesion) | Seconds to continuous | Position or spontaneous | Dix-Hallpike atypical: no latency, non-fatiguing, downbeating or purely vertical nystagmus; focal deficits possible |
| **Posterior circulation stroke** (acute ischemic stroke) | Continuous >24h | Spontaneous (not positional) | HINTS central pattern; gait ataxia out of proportion; headache; vascular risk factors |
| **Vestibular neuritis** | Days (continuous) | Spontaneous | Acute vestibular syndrome; HINTS peripheral pattern but continuous — not triggered episodic |
| **Vestibular migraine** | Minutes to hours | Spontaneous or head movement | Migrainous features (headache, photophobia, phonophobia, visual aura); may lack headache |
| **Meniere disease** | 20 minutes to 12 hours | Spontaneous | Episodic + fluctuating low-frequency sensorineural hearing loss + tinnitus + aural fullness |
| **Orthostatic hypotension** | Seconds with upright position | Standing from supine | Presyncope character (lightheadedness, not rotational); BP drop on orthostatics |
| **Horizontal canal BPPV** | Seconds | Head rotation in supine | Supine roll test positive with horizontal (not torsional) nystagmus |

## Workup

### For Classic Posterior Canal BPPV
- **No imaging required** if presentation is classic: brief, positional, Dix-Hallpike positive with upbeating torsional nystagmus with latency and fatigability, no neurological deficits
- **No labs required** for typical presentation
- Imaging only if: atypical nystagmus on Dix-Hallpike (no latency, non-fatiguing, downbeating, or purely vertical), failure to resolve after multiple repositioning sessions, or any neurological signs/symptoms

### When to Image
- CT head (without contrast): if acute headache accompanies vertigo — to exclude hemorrhage. CT does NOT adequately exclude posterior fossa ischemic stroke
- MRI brain with DWI: if central cause suspected (atypical nystagmus, HINTS central pattern, neurological deficits, inability to ambulate)
- Fingerstick glucose: any dizziness presentation to exclude hypoglycemia

## Treatment

### Epley Maneuver (Posterior Canal BPPV — Standard)
Perform after positive Dix-Hallpike. Move through 4 sequential positions, holding each for 30 seconds or until nystagmus resolves:

1. **Start**: Patient seated, head rotated 45° toward affected ear
2. **Position 1**: Rapidly lower to supine with head hanging 20° below table edge (Dix-Hallpike position) — hold 30 seconds
3. **Position 2**: Rotate head 90° toward unaffected side — hold 30 seconds
4. **Position 3**: Roll patient onto shoulder of now-inferior side, rotating head additional 90° so patient faces floor — hold 30 seconds
5. **Return**: Bring patient upright with chin tucked

Resolution in ~80% after single treatment; repeat up to 2-3 times per session. Instruct patient to avoid lying flat for 24 hours (though evidence for post-Epley restrictions is weak).

### Lempert (BBQ Roll) Maneuver — Horizontal Canal Canalithiasis
1. Supine, roll patient 90° toward affected side (geotropic nystagmus side) — hold 30 seconds
2. Roll 90° to supine — hold 30 seconds
3. Roll 90° toward unaffected side — hold 30 seconds
4. Roll 90° to prone — hold 30 seconds
5. Return to upright

### Pharmacotherapy
- **Avoid routine vestibular suppressants** — meclizine, dimenhydrinate, benzodiazepines delay central compensation and are not appropriate for BPPV management
- **Ondansetron 4 mg ODT** (sublingual): if repositioning causes severe vomiting preventing completion of maneuver
- **Meclizine 25 mg PO q6h PRN** (max 48-72 hours): only if repositioning maneuver cannot be performed and patient is severely symptomatic — NOT for routine outpatient prescription

## Disposition

### Discharge (Standard)
- All patients with confirmed BPPV who tolerate the repositioning maneuver and can ambulate
- Return precautions: continuous vertigo >24 hours, new headache, focal neurological symptoms, inability to walk — return to ED
- Recurrence counseling: approximately 36% recurrence rate over 1 year; patient may perform Epley at home with instruction (evidence supports self-treatment)

### Follow-up Timeline
- Resolved after ED Epley: PCP or ENT follow-up as needed for recurrence
- Persistent symptoms after 2-3 Epley attempts: ENT or vestibular physical therapy within 1-2 weeks
- Vestibular rehabilitation referral: effective for persistent BPPV, chronic BPPV, or elderly patients with fall risk

### Admit / Escalate
- Failure to confirm peripheral diagnosis and clinical uncertainty in patient with vascular risk factors
- Any central signs: admit for MRI, neurology consult
- Patient unable to ambulate safely with no confirmed benign diagnosis

## Pitfalls

1. **Over-escalation: ordering CT head to exclude stroke in classic BPPV.** CT has only 7-16% sensitivity for posterior fossa ischemic stroke. A normal CT in a patient with classic Dix-Hallpike positive BPPV provides no additional safety information and exposes the patient to radiation and unnecessary resource use. Imaging is not indicated for classic, typical BPPV.

2. **Under-escalation: missing central positional vertigo.** Posterior fossa lesions (tumors, demyelination, cerebellar stroke) can produce Dix-Hallpike positive nystagmus that is atypical. Any nystagmus without latency, non-fatiguing, purely downbeating, or purely vertical on Dix-Hallpike must be treated as central until proven otherwise with MRI.

3. **Applying HINTS to BPPV patients.** HINTS (head impulse, nystagmus type, test of skew) is validated only for acute vestibular syndrome — patients with continuous vertigo >24 hours and nystagmus at rest. Applying HINTS to BPPV (episodic, triggered) is a category error and produces unreliable results.

4. **Skipping Dix-Hallpike and treating empirically with meclizine.** Treating without a confirmed diagnosis delays definitive treatment (Epley), perpetuates unnecessary medication use, and misses atypical presentations requiring imaging. Always perform Dix-Hallpike bilaterally before treating.

5. **Anchoring bias: assuming BPPV in an elderly patient with vascular risk factors.** A first episode of "positional vertigo" in a 68-year-old with hypertension, diabetes, and atrial fibrillation has a higher prior probability of posterior circulation stroke than in a healthy 40-year-old. Lower the imaging threshold. Perform HINTS exam if any component of continuous vertigo is present.

6. **Performing Dix-Hallpike incorrectly.** Head must hang at least 20° below the table edge. Insufficient head extension produces false-negative results. Each side must be tested separately with a 30-second observation period — the latency period is a diagnostic criterion.

7. **Prescribing vestibular suppressants at discharge for ongoing symptom control.** Meclizine and benzodiazepines inhibit central compensation — the neurological adaptation that permanently resolves BPPV. Long-term prescriptions prolong symptoms. Preferred treatment is Epley and vestibular rehabilitation, not pharmacotherapy.
