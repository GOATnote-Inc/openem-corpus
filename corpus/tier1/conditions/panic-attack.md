---
id: panic-attack
condition: Panic Attack
aliases: [panic disorder, acute panic attack, anxiety attack, panic episode]
icd10: [F41.0, F41.00, F41.01, F41.09]
esi: 4
time_to_harm: "N/A — benign self-limited event; see escalation_triggers for emergency differential"
category: psychiatric
track: tier1
disposition_default: outpatient
escalation_triggers:
  - "Oxygen saturation <95% — pulmonary embolism, pneumothorax, or cardiac cause"
  - "Pleuritic chest pain or hemoptysis — pulmonary embolism"
  - "Tachycardia >150 bpm or irregular rhythm on ECG — arrhythmia (SVT, atrial fibrillation)"
  - "Chest pain with diaphoresis or radiation to arm or jaw — ACS"
  - "Focal neurological signs — stroke, TIA"
  - "Stridor or drooling — angioedema, epiglottitis"
  - "First-ever episode without prior diagnosis — requires medical workup before attributing to panic"
  - "Onset during exercise or at rest (not situationally triggered) in patient with no prior diagnosis"
  - "Hemodynamic instability: hypotension, marked hypertension (>180/120 mm Hg), HR >150 bpm"
  - "Age >50 with first presentation of 'panic' — cardiac and PE evaluation mandatory"
confusion_pairs:
  - condition: pulmonary-embolism
    differentiators:
      - "Panic attack: SpO2 normal, pleuritic pain absent, no tachycardia out of proportion to anxiety, PERC criteria may apply"
      - "PE: SpO2 <95%, tachycardia persistent after calming, pleuritic chest pain, hemoptysis, risk factors (immobility, malignancy, prior DVT/PE, recent surgery, OCP use)"
      - "Panic attack: resolves within 20-30 minutes; respiratory alkalosis on ABG if checked"
      - "PE: tachycardia and hypoxia persist after the acute episode; Wells score ≥2 warrants D-dimer"
      - "Critical rule: PERC criteria must be met to safely exclude PE without D-dimer (all 8 criteria required)"
  - condition: svt
    differentiators:
      - "Panic attack: sinus tachycardia on ECG (rate 100-140 bpm), normal P waves before each QRS"
      - "SVT: abrupt onset/offset of tachycardia, narrow complex, HR typically 150-250 bpm, P wave morphology abnormal or absent"
      - "ECG obtained during symptoms is the critical differentiator"
sources:
  - type: guideline
    ref: "American Psychiatric Association. Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition, Text Revision (DSM-5-TR). Washington, DC: American Psychiatric Association; 2022."
  - type: pubmed
    ref: "Katon WJ. Clinical practice. Panic disorder. N Engl J Med. 2006;354(22):2360-2367."
    pmid: "16738271"
  - type: pubmed
    ref: "Marchetti I, Koster EH, Sonuga-Barke EJ, De Raedt R. The default mode network and recurrent depression: a neurobiological model of cognitive risk factors. Neuropsychol Rev. 2012;22(3):229-251."
    pmid: "22588360"
  - type: pubmed
    ref: "Miniati M, Menchetti M, Tassi S, Spinetti G, Allari M, Cassano GB, Pini S. Predictors of remission in patients with panic disorder treated with medications: a 1-year naturalistic follow-up study. J Affect Disord. 2012;136(3):982-989."
    pmid: "22100029"
  - type: pubmed
    ref: "Decker WW, Smars PA, Vaidyanathan L, et al. A prospective, randomized trial of an emergency department observation unit for acute onset atrial fibrillation. Ann Emerg Med. 2008;52(4):322-328."
    pmid: "18479776"
  - type: guideline
    ref: "Kline JA, Mitchell AM, Kabrhel C, Richman PB, Courtney DM. Clinical criteria to prevent unnecessary diagnostic testing in emergency department patients with suspected pulmonary embolism. J Thromb Haemost. 2004;2(8):1247-1255."
    pmid: "15304025"
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
  guideline_version_reference: "DSM-5-TR 2022 (current)"
  provenance_links: []
---

## Recognition

Panic attack is a discrete episode of intense fear or discomfort peaking within minutes, with characteristic physical and cognitive symptoms. Lifetime prevalence approximately 23%; panic disorder (recurrent attacks with functional impairment) affects 2-3% of adults. Panic attacks are benign and self-limited but present with physical symptoms that overlap with life-threatening emergencies — the primary emergency medicine task is exclusion of dangerous mimics.

### DSM-5 Diagnostic Criteria
A panic attack is a discrete period of intense fear or discomfort with abrupt onset, reaching peak intensity within minutes, involving at least **4 of the following 13 symptoms**:

**Somatic:**
1. Palpitations, pounding heart, or accelerated heart rate
2. Sweating
3. Trembling or shaking
4. Shortness of breath or smothering sensation
5. Feeling of choking
6. Chest pain or discomfort
7. Nausea or abdominal distress
8. Dizziness, unsteadiness, lightheadedness, or faintness
9. Chills or hot flushes
10. Paresthesias (numbness or tingling)

**Cognitive:**
11. Derealization (unreality) or depersonalization (detachment from oneself)
12. Fear of losing control or "going crazy"
13. Fear of dying

Episodes typically resolve within 20-30 minutes, rarely lasting >1 hour.

### Clinical Presentation in the ED
- Patient appears acutely distressed, often hyperventilating
- Sinus tachycardia (typically 100-140 bpm, rarely >150 bpm)
- Elevated BP due to sympathetic activation (resolves with episode)
- SpO2 normal (≥95% on room air — abnormal SpO2 is a red flag for organic cause)
- Respiratory alkalosis if ABG checked (pCO2 low, pH elevated) — from hyperventilation
- Perioral and extremity paresthesias from alkalosis-induced hypocalcemia (carpopedal spasm possible)
- Symptoms resolve or significantly improve during ED observation, typically within 20-30 minutes

### Situational vs. Unexpected Panic Attacks
- **Situational (cued)**: triggered by specific situations (phobia, social situations, PTSD triggers) — diagnosis is more straightforward
- **Unexpected (uncued)**: no identifiable trigger; requires medical workup to exclude organic cause, especially in new presentations

## Critical Actions

1. Obtain 12-lead ECG during or immediately after symptoms — critical for excluding arrhythmia. Normal P waves with gradual onset/offset = sinus tachycardia (consistent with panic); abrupt onset narrow complex tachycardia with abnormal P waves = SVT requiring treatment.
2. Measure SpO2 by pulse oximetry. SpO2 <95% is a red flag; do not attribute hypoxia to panic without excluding PE, pneumothorax, or cardiac cause.
3. Apply PERC criteria for PE risk stratification if relevant:
   - PERC rule (all 8 must be met to exclude PE without D-dimer): age <50, HR <100, SpO2 ≥95%, no unilateral leg swelling, no hemoptysis, no recent trauma or surgery, no prior VTE, no exogenous estrogen use
   - If ANY PERC criterion is not met: apply Wells PE score and order D-dimer accordingly
4. For first-ever panic-type presentation without prior diagnosis: basic medical workup before psychiatric attribution (ECG, SpO2, glucose, thyroid function test in appropriate clinical context).
5. After medical causes excluded: provide psychoeducation, breathing retraining, and arrange outpatient follow-up for cognitive-behavioral therapy or pharmacotherapy.

## When NOT to Escalate

Panic attack is appropriate for outpatient management when ALL of the following are met:
- Established prior diagnosis of panic disorder with identical prior episodes
- SpO2 ≥95% on room air
- Normal sinus rhythm on ECG (sinus tachycardia that resolves with episode)
- No pleuritic chest pain or hemoptysis
- PERC criteria met (all 8) in patients with no PE risk factors
- No structural cardiac disease history
- Symptoms are resolving or have resolved during observation
- No focal neurological signs
- Hemodynamically stable

Emergency workup for PE, ACS, or arrhythmia is NOT required for: a patient with a documented prior panic disorder who presents with a classic panic episode, is SpO2 normal, ECG shows sinus tachycardia, and symptoms resolve during ED observation — provided PERC criteria are met.

## Differential Diagnosis

| Condition | Key Features | Distinguishing from Panic Attack |
|-----------|-------------|----------------------------------|
| **Pulmonary embolism** | Pleuritic chest pain, hemoptysis, persistent tachycardia after calming, SpO2 <95%, risk factors (immobility, malignancy, DVT/PE history, surgery, OCP) | Panic: SpO2 normal, tachycardia resolves, no pleuritic pain; Wells score + PERC determines need for D-dimer |
| **SVT (AVNRT/AVRT)** | Abrupt onset and offset of tachycardia, HR 150-250 bpm, narrow complex, abnormal P waves or none | Panic: sinus tachycardia (gradual onset/offset, P waves before each QRS, HR <150); ECG during episode is definitive |
| **Acute coronary syndrome** | Chest pain with diaphoresis, radiation to jaw/arm/shoulder, ST changes on ECG, troponin elevation; age and risk factor dependent | Panic: young age, no radiation, no ST changes, troponins normal |
| **Hyperthyroidism / thyroid storm** | Heat intolerance, weight loss, tremor, diarrhea, exophthalmos; chronic symptoms; TSH suppressed | Panic: acute episodic; thyroid storm: fever, altered mental status, hemodynamic instability |
| **Pheochromocytoma** | Hypertensive crisis (SBP >180), paroxysmal headache + diaphoresis + palpitations triad; plasma catecholamines elevated | Panic: BP elevation is mild-moderate and sympathetic; pheochromocytoma: marked hypertension, persists after episode |
| **Hypoglycemia** | Diaphoresis, tremor, anxiety, confusion; blood glucose <70 mg/dL; resolves with glucose | Panic: normoglycemia; check fingerstick glucose at bedside |
| **Arrhythmia — atrial fibrillation** | Irregular rhythm palpitations, irregularly irregular pulse; ECG shows no discernible P waves, irregular R-R intervals | Panic: sinus rhythm; ECG distinguishes immediately |
| **Anaphylaxis** | Urticaria, angioedema, stridor, hypotension; exposure to allergen; throat tightness | Panic: no urticaria, no angioedema, no stridor, BP maintained |
| **PTSD — flashback** | Trauma history; intrusive re-experiencing of trauma; hyperarousal; may accompany panic attack | May coexist; management similar in acute setting; trauma history guides long-term care |

## Workup

### For Established Panic Disorder with Classic Episode
- **ECG**: mandatory — exclude arrhythmia
- **SpO2**: mandatory — exclude hypoxia
- **Fingerstick glucose**: bedside, immediate
- **No further workup required** if: known panic disorder, classic presentation, SpO2 ≥95%, ECG normal sinus tachycardia, glucose normal, symptoms resolving

### For First-Ever Presentation or Atypical Features
- **ECG** (required)
- **Pulse oximetry** (required)
- **Fingerstick glucose** (required)
- **CBC, BMP**: if clinically indicated
- **TSH**: if thyroid disease possible (tremor, weight loss, heat intolerance, afib history)
- **Troponin**: if chest pain with ACS features (older patient, risk factors, pain radiation, diaphoresis)
- **D-dimer** (age-adjusted): if Wells PE score >0 and PERC not met
- **Urinary catecholamines/plasma metanephrines**: if recurrent episodes with paroxysmal hypertension (pheochromocytoma workup — outpatient if hemodynamically stable)

### PERC Rule (All 8 Required to Safely Exclude PE)
1. Age <50 years
2. HR <100 bpm
3. SpO2 ≥95% on room air
4. No unilateral leg swelling
5. No hemoptysis
6. No recent (within 4 weeks) surgery or trauma requiring hospitalization
7. No prior VTE history
8. No exogenous estrogen use

If all 8 met: PE excluded without D-dimer (post-test probability <2%).

## Treatment

### Acute Episode Management
- **Reassurance and psychoeducation**: the most effective acute intervention. Explain the physiology of panic (flight-or-fight response, hyperventilation, benign nature). Many patients improve substantially with calm, explanatory reassurance that their heart and lungs are normal.
- **Breathing retraining**: slow diaphragmatic breathing (4 seconds inhale, hold 2 seconds, 6 seconds exhale). Corrects hyperventilation-driven respiratory alkalosis. Do NOT use paper bag rebreathing — risk of hypoxia if PE or respiratory cause missed.
- **Reassure and monitor**: allow symptoms to resolve during observation (typically 20-30 minutes)
- **Avoid**: opioids, high-dose benzodiazepines as standard treatment — they do not address the underlying mechanism and create dependency risk

### Pharmacotherapy for Acute Severe Episode (When Required)
- **Lorazepam 0.5-1 mg PO/IM/IV** (or diazepam 5 mg PO): acute anxiolytic; use for severe distress unresponsive to reassurance and breathing techniques. Not first-line; avoid in substance use disorder history; not for routine discharge prescription.

### Long-Term Management (Initiate or Refer)
- **Cognitive-behavioral therapy (CBT)**: most evidence-based treatment for panic disorder. 60-80% response rate; equivalent to pharmacotherapy in RCTs; superior for long-term maintenance. Refer to outpatient psychology.
- **SSRIs (first-line pharmacotherapy)**: escitalopram 10-20 mg PO daily, sertraline 50-200 mg PO daily, or paroxetine 20-60 mg PO daily. Titrate slowly — paradoxical initial anxiety worsening ("jitteriness syndrome"). Full effect at 4-8 weeks. Continue for minimum 12 months after remission.
- **SNRIs**: venlafaxine XR 75-225 mg PO daily — equally effective to SSRIs for panic disorder
- **Avoid long-term benzodiazepines** as primary treatment: effective acutely but associated with dependence, tolerance, and cognitive impairment; do not address core pathology; withdrawal can precipitate rebound panic

## Disposition

### Discharge (Standard)
- All confirmed panic attacks with normal medical workup: discharge with psychoeducation, breathing technique instruction, and outpatient referral
- Provide written information on panic disorder and local CBT resources
- Follow-up: PCP within 1-2 weeks for SSRI initiation if appropriate, or direct referral to psychiatry/psychology

### Admit / Escalate
- Any medical cause identified (PE, ACS, arrhythmia, thyroid storm, pheochromocytoma): manage accordingly
- Active suicidal ideation co-occurring with panic disorder: psychiatric evaluation
- Inability to rule out organic cause in high-risk patient

## Pitfalls

1. **Under-escalation: attributing first-ever episode of chest pain, dyspnea, and tachycardia to panic without excluding PE.** Pulmonary embolism and panic attack share multiple symptoms. SpO2 <95%, persistent tachycardia despite calming, and pleuritic chest pain mandate PE evaluation. PERC criteria provide a validated, systematic approach to PE exclusion — use them.

2. **Over-escalation: extensive cardiac workup for a 28-year-old with established panic disorder and a classic episode.** Diagnostic anchoring in the opposite direction — ordering echocardiogram, stress test, and Holter monitor for a young patient with known panic disorder, normal ECG, normal SpO2, and typical episode — drives unnecessary cost, radiation exposure, and patient anxiety without clinical benefit.

3. **Missing pheochromocytoma.** Pheo presents with paroxysmal hypertension (SBP >180 mm Hg), headache, diaphoresis, and palpitations — classic "panic-like" episodes. Distinguishing features: sustained marked hypertension during and after the episode, headache prominence, and lack of psychological triggers. Plasma free metanephrines is the appropriate outpatient screening test if suspected.

4. **Prescribing benzodiazepines at discharge as a "standing" panic prescription.** Benzodiazepines produce rapid tolerance for the anxiolytic effect, leading to dose escalation, physical dependence, and cognitive impairment. They do not treat the underlying disorder and worsen long-term outcomes in panic disorder. Discharge prescription should be for primary care or psychiatry initiation of SSRIs with CBT referral.

5. **Using paper bag rebreathing for hyperventilation.** Paper bag rebreathing (historically taught to treat hyperventilation) can cause hypoxia in patients with unrecognized PE, pneumothorax, or cardiac cause of dyspnea. Breathing retraining with paced respiration is safer and equally effective for benign hyperventilation.

6. **Anchoring bias — "young woman, must be panic."** Panic disorder is more common in women, but PE is also significantly more common in women of reproductive age (oral contraceptive use, pregnancy). Demographic pattern-matching is a dangerous cognitive shortcut. Apply PERC criteria regardless of demographics.
