---
id: pheochromocytoma-crisis
condition: Pheochromocytoma / Catecholamine Crisis
aliases: [pheo crisis, catecholamine storm, paraganglioma crisis, adrenal crisis hypertensive]
icd10: [D35.00, D35.01, E27.5, I10]
esi: 1
time_to_harm:
  irreversible_injury: "< 30 minutes (hypertensive encephalopathy, myocardial injury, aortic dissection)"
  death: "< 2 hours (catecholamine-induced cardiomyopathy, stroke, aortic rupture)"
  optimal_intervention_window: "Immediate alpha-blockade — phentolamine within minutes of recognition"
category: endocrine-metabolic
track: tier1
sources:
  - type: guideline
    ref: "Lenders JWM et al. Pheochromocytoma and paraganglioma: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab. 2014;99(6):1915-1942."
    pmid: "24893135"
  - type: pubmed
    ref: "Whitelaw BC et al. Phaeochromocytoma crisis. Clin Endocrinol. 2014;80(1):13-22."
    pmid: "23980724"
  - type: review
    ref: "Pacak K. Preoperative management of the pheochromocytoma patient. J Clin Endocrinol Metab. 2007;92(11):4069-4079."
    pmid: "17989126"
  - type: pubmed
    ref: "Zuber SM, Kantorovich V, Pacak K. Hypertension in pheochromocytoma: characteristics and treatment. Endocrinol Metab Clin North Am. 2011;40(2):295-311."
    pmid: "21565668"
  - type: review
    ref: "Neumann HPH et al. Pheochromocytoma and paraganglioma. N Engl J Med. 2019;381(6):552-565."
    pmid: "31390501"
last_updated: "2026-02-26"
compiled_by: agent
risk_tier: A
confusion_pairs:
  - condition: aortic-dissection
    differentiators:
      - "Pheo crisis: paroxysmal with diaphoresis, pallor, palpitations (classic triad)"
      - "Aortic dissection: tearing/ripping pain with pulse differential"
      - "Pheo may cause secondary dissection — always check for both"
  - condition: thyroid-storm
    differentiators:
      - "Thyroid storm: fever, tachycardia, and altered mental status dominate"
      - "Pheo: episodic hypertension with pallor (not flushing)"
      - "Thyroid function tests differentiate"
validation:
  schema_version: "2.0"
  automated_consistency_check: null
  dose_range_validator: null
  unit_normalization_check: null
  cross_file_consistency_check: null
  citation_presence_check: null
  duplicate_content_check: null
  outlier_detection_flag: clear
  guideline_version_reference: null
  provenance_links: []
---
# Pheochromocytoma / Catecholamine Crisis

## Recognition

**Definition:** Pheochromocytoma crisis is a life-threatening surge of catecholamines (epinephrine, norepinephrine, dopamine) from a chromaffin cell tumor, causing severe hypertension, cardiac injury, and multi-organ failure. The tumor is adrenal in 85% of cases (pheochromocytoma) and extra-adrenal in 15% (paraganglioma).

**Classic Triad (present in ~40% of patients):**
1. Episodic headache (severe, throbbing)
2. Diaphoresis (profuse, unprovoked)
3. Palpitations/tachycardia

**Crisis Triggers:**
- Tumor manipulation (surgery, biopsy, abdominal palpation)
- Anesthetic induction without alpha-blockade
- Medications: metoclopramide, glucocorticoids, opioids, tricyclic antidepressants, beta-blockers (unopposed alpha stimulation)
- Tyramine-rich foods, emotional stress
- Pregnancy (uterine contractions compress tumor)
- Spontaneous (no identifiable trigger in many cases)

**Clinical Features of Catecholamine Crisis:**

| Feature | Notes |
|---------|-------|
| **Severe hypertension** | SBP > 200 mmHg, often > 250 mmHg; paroxysmal or sustained |
| **Tachycardia or reflex bradycardia** | Heart rate may be paradoxically normal with pure norepinephrine-secreting tumors |
| **Pallor** | Catecholamine-mediated vasoconstriction — patients are pale, NOT flushed |
| **Diaphoresis** | Profuse; may be presenting complaint |
| **Chest pain** | Catecholamine-induced myocardial injury, coronary vasospasm, or aortic dissection |
| **Pulmonary edema** | Flash pulmonary edema from acute LV failure or severe afterload |
| **Encephalopathy** | Hypertensive encephalopathy with seizures, visual changes, altered mental status |
| **Takotsubo-like cardiomyopathy** | Reversible LV dysfunction from catecholamine cardiotoxicity |
| **Fever** | Excess catecholamines increase thermogenesis |

**Associations:**
- MEN2A/2B (medullary thyroid carcinoma, hyperparathyroidism)
- Von Hippel-Lindau disease, neurofibromatosis type 1
- Familial paraganglioma syndromes (SDH mutations)
- 40% of pheochromocytomas have germline mutations

## Critical Actions

1. **Phentolamine 5 mg IV bolus, repeat q2-5 minutes until BP controlled.** This is the first-line antihypertensive for catecholamine crisis. Non-selective alpha-blocker with rapid onset (1-2 minutes). Prepare 5-10 mg doses for repeated boluses. Transition to phentolamine infusion 1-5 mg/hr if repeated boluses needed.

2. **Do NOT give beta-blockers before adequate alpha-blockade.** Beta-blockade in the setting of unopposed alpha-receptor stimulation causes paradoxical hypertension and coronary vasospasm. This is the single most dangerous prescribing error in pheochromocytoma. Only add esmolol or labetalol AFTER alpha-blockade is established and tachycardia persists.

3. **Nicardipine 5-15 mg/hr IV infusion as adjunctive BP control.** Calcium channel blockers are safe in pheochromocytoma crisis (no risk of unopposed alpha stimulation). Clevidipine 1-2 mg/hr IV is an alternative. Nitroprusside 0.5-3 mcg/kg/min IV for refractory hypertension.

4. **Volume resuscitation.** Pheochromocytoma patients are chronically volume-depleted from catecholamine-mediated venoconstriction. NS 500-1000 mL IV bolus. Anticipate severe hypotension after alpha-blockade or tumor removal — vasopressor-dependent hypotension may require 3-5 L crystalloid replacement.

5. **12-lead ECG and troponin.** Catecholamine crisis causes myocardial injury (ST changes, troponin elevation), takotsubo cardiomyopathy, and arrhythmias. Bedside echo to evaluate LV function.

6. **CT abdomen/pelvis with contrast if diagnosis unconfirmed.** Adrenal mass on CT, elevated plasma free metanephrines (sensitivity > 97%). Do NOT biopsy the mass — needle manipulation can trigger fatal catecholamine release.

7. **Control arrhythmias.** Esmolol 500 mcg/kg IV bolus then 50-200 mcg/kg/min ONLY after alpha-blockade achieved. Lidocaine 1-1.5 mg/kg IV for ventricular tachycardia. Magnesium sulfate 2 g IV for refractory ventricular arrhythmias.

8. **Assess for end-organ damage.** CT head for encephalopathy/stroke. CTA chest for aortic dissection. Troponin trending for myocardial injury. Urinalysis for hematuria (renal damage). Fundoscopy for hypertensive retinopathy.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **Essential hypertensive emergency** | Sustained (not paroxysmal); no triad of headache/diaphoresis/palpitations; no adrenal mass; normal metanephrines |
| **Thyroid storm** | Fever, goiter, lid lag, tremor; flushed (not pale); TSH suppressed, free T4 elevated |
| **Cocaine/amphetamine toxicity** | Drug use history; mydriasis; agitation; positive toxicology screen |
| **Serotonin syndrome** | Serotonergic medication history; clonus, hyperreflexia, agitation; no adrenal mass |
| **Malignant hypertension (renovascular)** | Renal bruit, elevated renin/aldosterone; gradual onset; no episodic symptoms |
| **Aortic dissection** | Tearing chest/back pain, pulse differential; pheochromocytoma CAN cause secondary dissection |
| **STEMI** | Chest pain, ECG changes, troponin elevation — note that pheo crisis also elevates troponin; adrenal imaging differentiates |
| **Autonomic dysreflexia** | Spinal cord injury at T6 or above; triggered by bladder distension or noxious stimulus below lesion level |

## Workup

**Immediate:**
- 12-lead ECG
- Troponin I or T (serial)
- BMP (hypokalemia from catecholamine-driven potassium shift)
- CBC, LFTs, lipase
- Blood gas with lactate
- Urinalysis

**Diagnostic (for suspected pheochromocytoma):**
- Plasma free metanephrines (sensitivity 97-99% — best screening test)
- 24-hour urine catecholamines and metanephrines (if plasma unavailable)
- CT abdomen/pelvis with IV contrast (adrenal protocol)
- MRI abdomen if CT equivocal (pheo is characteristically T2-bright)
- MIBG scan for metastatic or extra-adrenal disease

**End-Organ Assessment:**
- Bedside echocardiography (LV function, wall motion abnormalities)
- CT head if neurological symptoms
- CTA chest if aortic dissection suspected
- Chest X-ray (pulmonary edema)

## Treatment

**Acute Crisis (first 1-2 hours):**
- Phentolamine 5 mg IV bolus q2-5 min (primary agent)
- Nicardipine 5-15 mg/hr IV infusion (adjunctive)
- NS 500-1000 mL IV bolus (volume expansion)
- Esmolol ONLY after alpha-blockade for persistent tachycardia > 120 bpm
- Magnesium sulfate 2 g IV over 20 min (antiarrhythmic, vasodilator)

**Transition to Oral Alpha-Blockade (after crisis stabilized):**
- Phenoxybenzamine 10 mg PO BID, titrate to 20-40 mg PO BID over 7-14 days (irreversible alpha-blocker)
- Alternative: doxazosin 2-8 mg PO daily (selective alpha-1 blocker)
- Calcium channel blocker (amlodipine 5-10 mg PO daily) as adjunctive
- Beta-blocker added ONLY after 2-3 days of alpha-blockade: propranolol 10-40 mg PO TID or atenolol 25-50 mg PO daily

**Preoperative Optimization (7-14 days before surgical resection):**
- Alpha-blockade → add beta-blocker → high-sodium diet → IV fluids day before surgery
- Target: sitting BP < 130/80 with orthostatic drop > 15 mmHg (confirms adequate alpha-blockade)
- Metyrosine 250-500 mg PO QID (catecholamine synthesis inhibitor) for refractory cases

**Flash Pulmonary Edema:**
- Nitroglycerin 5-200 mcg/min IV infusion
- BiPAP for respiratory distress
- Avoid furosemide initially — patients are volume-depleted despite pulmonary edema (afterload-driven, not volume-driven)

## Disposition

**All pheochromocytoma crisis patients require ICU admission** with:
- Continuous arterial line BP monitoring
- Telemetry for arrhythmia detection
- Serial troponin trending q6h until stable
- Endocrinology consultation for preoperative alpha-blockade protocol
- Surgery consultation for definitive tumor resection (laparoscopic adrenalectomy preferred)

**Transfer if:**
- No ICU capability
- No endocrine surgery expertise
- Stabilize BP with phentolamine before transport

## Pitfalls

1. **Giving a beta-blocker as first-line for tachycardia and hypertension without checking for pheochromocytoma.** Beta-blockade without prior alpha-blockade removes the vasodilatory effect of beta-2 receptors, leaving alpha-1 vasoconstriction unopposed. The result is paradoxical hypertension, coronary vasospasm, and potential cardiac arrest. This error occurs when pheo is not in the differential and labetalol is reflexively chosen for hypertensive emergency.

2. **Biopsying an adrenal mass without biochemical workup.** CT-guided biopsy of an adrenal pheochromocytoma can trigger fatal catecholamine release. ALL adrenal incidentalomas > 1 cm require plasma free metanephrines before any invasive procedure. This applies to any adrenal mass found incidentally on imaging obtained for other reasons.

3. **Attributing paroxysmal hypertension with pallor and diaphoresis to anxiety or panic attacks.** Pheochromocytoma mimics panic disorder — episodic tachycardia, diaphoresis, anxiety, and sense of doom. The distinguishing feature is severe hypertension during episodes (panic attacks rarely cause SBP > 180) and pallor rather than flushing.

4. **Failing to volume-resuscitate after alpha-blockade.** Pheochromocytoma patients maintain pseudo-normovolemia through catecholamine-driven venoconstriction. When alpha-blockade relaxes venous tone, the true volume deficit is unmasked — precipitous hypotension and cardiovascular collapse occur. Pre-load with NS and have vasopressors at bedside.

5. **Administering metoclopramide to a patient with undiagnosed pheochromocytoma.** Metoclopramide directly stimulates catecholamine release from chromaffin cells. It has triggered fatal pheochromocytoma crises when given for nausea. Ondansetron 4 mg IV is the safe antiemetic.
