---
id: spinal-cord-injury
condition: Traumatic Spinal Cord Injury
aliases: [SCI, spinal cord trauma, cord injury, traumatic myelopathy, spinal shock, neurogenic shock]
icd10: [S14.109A, S24.109A, S34.109A]
esi: 1
time_to_harm: "< 60 minutes"
mortality_if_delayed: "Permanent neurological deficit; neurogenic shock mortality 7-10% without hemodynamic support"
category: traumatic
track: tier1
sources:
  - type: guideline
    ref: "Kwon BK, Tetreault LA, Martin AR, et al. A Clinical Practice Guideline for the Management of Patients With Acute Spinal Cord Injury: Recommendations on Hemodynamic Management. Global Spine J. 2024;14(3_suppl):187S-211S"
    pmid: "38526923"
  - type: guideline
    ref: "Fehlings MG, Wilson JR, Tetreault LA, et al. A Clinical Practice Guideline for the Management of Patients With Acute Spinal Cord Injury: Recommendations on the Use of Methylprednisolone Sodium Succinate. Global Spine J. 2017;7(3 Suppl):203S-211S"
    pmid: "29164025"
  - type: review
    ref: "Wang TY, Park C, Zhang H, et al. Management of Acute Traumatic Spinal Cord Injury: A Review of the Literature. Front Surg. 2021;8:698736"
    pmid: "34966774"
  - type: review
    ref: "Roberts TT, Leonard GR, Cepela DJ. Classifications In Brief: American Spinal Injury Association (ASIA) Impairment Scale. Clin Orthop Relat Res. 2017;475(5):1499-1504"
    pmid: "27815685"
  - type: guideline
    ref: "ATLS Advanced Trauma Life Support, 10th Edition. American College of Surgeons. 2018"
last_updated: "2026-02-19"
compiled_by: agent
risk_tier: A
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

# Traumatic Spinal Cord Injury

> **Scope note:** This file covers TRAUMATIC spinal cord injury. For oncologic/non-traumatic cord compression (metastatic epidural compression, degenerative myelopathy, epidural abscess, epidural hematoma), see `spinal-cord-compression.md`. For cauda equina syndrome, see `cauda-equina-syndrome.md`.

## Recognition

### Mechanism
- Motor vehicle collision (most common), falls, sports (diving, football), violence (penetrating trauma, assault)
- Cervical spine injuries most common (55%); thoracic (15%); thoracolumbar junction (15%); lumbar (15%)
- Always assume spinal cord injury in multi-system trauma with altered consciousness until cleared

### Primary Survey Findings
- **Neurogenic shock:** Hypotension + BRADYCARDIA + warm/dry skin (loss of sympathetic tone below lesion level; vasodilation). Occurs with injuries at T6 or above.
- **Spinal shock:** Transient loss of all spinal cord function below the level of injury (flaccidity, areflexia, loss of bulbocavernosus reflex). NOT a hemodynamic state. Resolves over hours to weeks; return of bulbocavernosus reflex marks end of spinal shock.
- **Respiratory failure:** C3-C5 lesions compromise diaphragm (phrenic nerve). C1-C2 lesions cause apnea. Thoracic lesions lose intercostal muscle function; preserved diaphragm but reduced cough, tidal volume.
- **Priapism:** Indicates loss of sympathetic tone; sign of complete cord injury.

### Distinguishing Neurogenic Shock from Hemorrhagic Shock

| Feature | Neurogenic Shock | Hemorrhagic Shock |
|---------|-----------------|-------------------|
| Heart rate | Bradycardia | Tachycardia |
| Skin | Warm, dry, flushed (below level) | Cool, clammy, pale |
| Blood pressure | Hypotension | Hypotension |
| Response to fluids | Partial | Improves with volume |
| Vasopressors | Often required | Last resort after volume |
| Key clue | Neurological deficit present | Signs of blood loss |

**In polytrauma, hemorrhagic shock must be excluded FIRST.** Do not attribute hypotension to neurogenic shock until hemorrhage is ruled out. Both can coexist.

### ASIA Impairment Scale (AIS)

Perform after spinal shock resolves (bulbocavernosus reflex returns) for accurate prognostication.

| Grade | Classification | Definition |
|-------|---------------|------------|
| A | Complete | No motor or sensory function in sacral segments S4-S5 |
| B | Sensory incomplete | Sensory but not motor function preserved below neurological level, including S4-S5 |
| C | Motor incomplete | Motor function preserved below level; majority of key muscles grade < 3/5 |
| D | Motor incomplete | Motor function preserved below level; majority of key muscles grade >= 3/5 |
| E | Normal | Motor and sensory function normal |

### Incomplete Spinal Cord Injury Patterns

| Syndrome | Mechanism | Motor | Sensory | Prognosis |
|----------|-----------|-------|---------|-----------|
| **Central cord** | Hyperextension in elderly with cervical spondylosis | Upper extremity > lower extremity weakness ("man in a barrel") | Variable; cape-like distribution | Best prognosis of incomplete syndromes; ~75% recover ambulatory function |
| **Brown-Sequard** | Penetrating trauma (hemicord) | Ipsilateral motor loss below level | Ipsilateral proprioception/vibration loss; contralateral pain/temperature loss | Best overall prognosis; >90% ambulate |
| **Anterior cord** | Flexion injury, anterior spinal artery occlusion, burst fracture with retropulsion | Bilateral motor paralysis below level | Bilateral pain/temperature loss; PRESERVED proprioception/vibration (posterior columns intact) | Worst prognosis of incomplete syndromes; ~10-20% motor recovery |
| **Posterior cord** | Rare; hyperextension | Motor preserved | Loss of proprioception/vibration; pain/temperature intact | Good prognosis |
| **Cauda equina** | L1-L2 and below (not true cord injury — peripheral nerve roots) | Asymmetric lower extremity LMN weakness | Saddle anesthesia, asymmetric radiculopathy | Variable; depends on surgical timing |

## Critical Actions

| Action | Target |
|--------|--------|
| Inline cervical spine stabilization | Immediate (on scene / primary survey) |
| Airway with cervical spine precautions | GCS <= 8 or C3-C5 injury with respiratory compromise |
| Differentiate neurogenic vs hemorrhagic shock | Within primary survey |
| CT spine (whole spine if obtunded) | < 30 minutes |
| MRI spine | Within 24 hours (or emergent if neurological deterioration) |
| Hemodynamic augmentation (MAP target) | Initiate within 1 hour of ED arrival |
| Spine surgery consultation | Within 1 hour |

1. **Immobilize the spine.** Rigid cervical collar + spine board for transport. Log-roll technique for all movements. Maintain neutral alignment. Remove from backboard as soon as possible (skin breakdown risk).
2. **Secure airway with inline stabilization** if GCS <= 8, C-spine injury with respiratory failure, or ascending deficit. Use video laryngoscopy or fiberoptic intubation. Avoid neck extension. RSI: use agents that avoid fasciculations (rocuronium 1.2 mg/kg IV preferred over succinylcholine in subacute SCI due to hyperkalemia risk; succinylcholine is safe in the first 48 hours).
3. **Volume resuscitate first.** Start with crystalloid (LR or NS) 1-2 L IV bolus. If hypotension persists after ruling out hemorrhage, this is neurogenic shock — start vasopressors.
4. **Vasopressor for neurogenic shock:** Norepinephrine 0.05-0.3 mcg/kg/min IV (first-line — provides both alpha vasoconstriction and beta chronotropy). Phenylephrine 0.5-5 mcg/kg/min if isolated vasodilation without bradycardia. Atropine 0.5 mg IV for symptomatic bradycardia (repeat q3-5min, max 3 mg).
5. **MAP target 75-90 mmHg for 3-7 days** (AO Spine/Praxis 2024 guideline). Invasive arterial line for continuous monitoring. ICU admission mandatory.
6. **CT of entire spine** in obtunded/unreliable patients. CT angiography if vertebral artery injury suspected (cervical fracture extending into transverse foramen).
7. **MRI spine** within 24 hours to assess cord edema, hemorrhage, compression, and guide surgical timing.
8. **Emergent spine surgery consultation.** Early decompression (< 24 hours) is associated with improved neurological outcomes (AO Spine guideline).

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **Hemorrhagic shock (in polytrauma)** | Tachycardia (not bradycardia), cool/clammy skin, source of hemorrhage identified, responds to volume; MUST exclude before attributing hypotension to neurogenic shock |
| **Spinal cord compression (non-traumatic)** | No acute trauma mechanism; progressive rather than acute onset; malignancy, abscess, or degenerative etiology; see `spinal-cord-compression.md` |
| **Transverse myelitis** | No trauma; inflammatory; subacute onset over hours to days; MRI shows intramedullary T2 signal without structural compression |
| **Spinal cord infarction** | Acute onset, often after aortic surgery or aortic dissection; anterior cord syndrome pattern; no fracture on imaging |
| **Aortic dissection** | Tearing chest/back pain, pulse deficits, widened mediastinum; may cause cord ischemia via intercostal artery compromise |
| **Guillain-Barre syndrome** | Ascending paralysis, areflexia, no sensory level; post-infectious; CSF albuminocytologic dissociation |
| **Conversion disorder** | Inconsistent exam, give-way weakness, nonanatomic sensory loss, normal imaging |
| **Bilateral hip fractures (in elderly fall)** | Bilateral lower extremity pain/immobility mimicking paraplegia; pelvic X-ray/CT distinguishes |

## Workup

### Imaging
- **CT spine (whole spine):** First-line for bony injury in all trauma patients with suspicion. Obtain entire spine in obtunded/unreliable patients (non-contiguous fractures in 10-15%).
- **CT angiography of neck:** If cervical fracture involves transverse foramen (vertebral artery injury risk).
- **MRI spine:** Within 24 hours. Defines cord edema, hemorrhage, disc herniation, ligamentous injury, epidural hematoma. Intramedullary hemorrhage on MRI predicts poor neurological recovery.
- **Chest X-ray/CT chest:** Evaluate for pneumothorax, pulmonary contusion, hemothorax (associated injuries).
- **FAST/CT abdomen-pelvis:** Rule out intra-abdominal hemorrhage in polytrauma.

### Labs
- **CBC, BMP, coagulation panel, type and screen:** Baseline for trauma and surgical planning.
- **Lactate:** Evaluate for occult hemorrhage and tissue hypoperfusion.
- **ABG:** Baseline respiratory function; monitor for hypoventilation (especially cervical injuries).
- **Troponin:** Neurogenic cardiac injury (sympathetic surge/denervation can cause myocardial stunning).
- **Ethanol level, urine drug screen:** Common confounders in trauma.
- **Urinalysis:** Baseline; catheterize if urinary retention (neurogenic bladder).

### Monitoring
- **Invasive arterial line:** Required for continuous MAP monitoring during hemodynamic augmentation.
- **Central venous access:** For vasopressor administration.
- **Continuous telemetry:** Arrhythmia risk from autonomic dysfunction (bradycardia, asystole in high cervical injuries).
- **Pulse oximetry and capnography:** Serial respiratory monitoring; cervical injuries may have insidious respiratory decline.
- **Foley catheter:** Neurogenic bladder is universal in acute SCI; monitor urine output.

## Treatment

### Hemodynamic Management
- **MAP goal 75-90 mmHg for 3-7 days** (AO Spine/Praxis 2024 CPG; evidence quality low but consistently recommended).
- Arterial line monitoring in ICU.
- First-line vasopressor: **norepinephrine 0.05-0.3 mcg/kg/min IV** (addresses both vasodilation and bradycardia).
- Second-line: **dopamine 5-20 mcg/kg/min IV** (provides chronotropy if persistent bradycardia).
- **Atropine 0.5 mg IV** for symptomatic bradycardia (repeat q3-5min, max 3 mg). If refractory, consider temporary transcutaneous/transvenous pacing.
- Avoid pure vasoconstrictors (phenylephrine) as sole agent in neurogenic shock with bradycardia — reflex bradycardia worsens.

### Methylprednisolone — NOT Recommended by Most Current Guidelines
- NASCIS II (1990) suggested benefit of 24-hour high-dose MPSS if started within 8 hours: 30 mg/kg IV bolus then 5.4 mg/kg/hr for 23 hours.
- NASCIS III (1997) extended to 48 hours if started 3-8 hours post-injury.
- **AO Spine 2017 CPG:** 24-hour MPSS infusion within 8 hours is an option (weak recommendation). NOT recommended after 8 hours. 48-hour protocol NOT recommended (increased pneumonia and sepsis risk).
- **AANS/CNS 2013:** Recommended AGAINST routine use of MPSS.
- **Current consensus:** Most trauma centers do NOT administer MPSS. If used at all, must be within 8 hours and only after careful risk-benefit discussion. Complications include GI hemorrhage, wound infection, hyperglycemia, and pneumonia.

### Surgical Management
- **Early decompressive surgery (< 24 hours)** is recommended for incomplete SCI with ongoing cord compression (AO Spine 2024).
- Indications: unstable fracture, progressive neurological deficit, cord compression on MRI, bilateral facet dislocation.
- Closed reduction of cervical facet dislocations under fluoroscopy may be attempted in alert patients; MRI before reduction if patient unreliable or obtunded (to exclude disc herniation that could worsen cord injury during reduction).

### Respiratory Management
- Cervical SCI patients: high risk for respiratory failure (reduced FVC, impaired cough, retained secretions).
- Serial FVC monitoring (intubate if FVC < 15 mL/kg or declining trajectory).
- Aggressive pulmonary toilet: incentive spirometry, assisted cough techniques, chest physiotherapy.
- Early tracheostomy consideration for C1-C4 injuries (prolonged ventilator dependence likely).

### DVT Prophylaxis — MANDATORY
- Extremely high VTE risk (DVT in up to 80% without prophylaxis).
- **Enoxaparin 30 mg SC q12h** (initiated within 72 hours when hemostasis secured). If CrCl < 30: heparin 5000 units SC q8h.
- Sequential compression devices from admission.
- Duration: minimum 8-12 weeks for motor complete SCI.

### Other Supportive Care
- **Foley catheter** for neurogenic bladder; transition to intermittent catheterization when stable.
- **Stress ulcer prophylaxis:** Famotidine 20 mg IV q12h (GI hemorrhage risk elevated in SCI).
- **Temperature management:** Poikilothermia below the lesion level; external warming/cooling as needed.
- **Bowel regimen:** Neurogenic bowel; senna + docusate; digital stimulation protocol.
- **Skin:** Pressure injury prevention; off backboard within 2 hours; position changes q2h.
- **Pain:** Gabapentin 300 mg PO TID (titrate to 1200 mg TID) for neuropathic pain. Opioids for acute traumatic pain: morphine 2-4 mg IV q4h PRN.

### Autonomic Dysreflexia (Subacute/Chronic — Injuries at T6 or Above)
- Massive sympathetic response below the level of injury triggered by noxious stimulus (distended bladder, fecal impaction, skin irritation).
- **Presentation:** Severe hypertension (SBP > 200 mmHg), pounding headache, diaphoresis/flushing above level, bradycardia.
- **Treatment:** Sit patient upright. Identify and remove trigger (catheterize bladder, disimpact). If SBP remains > 150 mmHg: nifedipine 10 mg PO (bite and swallow) or nitropaste 1 inch topical. Short-acting agents only — blood pressure drops rapidly once trigger removed.
- **This is a hypertensive emergency** that can cause intracranial hemorrhage, seizure, or death if untreated.

## Disposition

### Operating Room (Emergent)
- Unstable spinal fracture with cord compression
- Progressive neurological deficit
- Bilateral locked facets requiring reduction
- Epidural hematoma or disc herniation causing cord compression

### ICU (All Acute Traumatic SCI)
- ALL patients with acute traumatic SCI require ICU admission for:
  - Continuous MAP monitoring and hemodynamic augmentation (3-7 days)
  - Respiratory monitoring (especially cervical injuries)
  - Cardiac telemetry (arrhythmia risk)
  - Serial neurological exams
- High cervical injuries (C1-C4): anticipate ventilator dependence

### Transfer
- If facility lacks spine surgery capability, MRI, or ICU with invasive hemodynamic monitoring.
- Immobilize, stabilize hemodynamics, and transfer to Level I/II trauma center.
- Do NOT delay transfer for MRI if definitive surgical care is not available locally.

### Discharge
- NOT appropriate from the ED for any confirmed acute traumatic SCI.

## Pitfalls

1. **Attributing hypotension to neurogenic shock without excluding hemorrhage.** In polytrauma, hemorrhagic shock is far more common and more immediately lethal. Neurogenic shock is a diagnosis of exclusion. A tachycardic hypotensive polytrauma patient has hemorrhagic shock until proven otherwise, even with a known spinal cord injury. Perform FAST, pelvic X-ray, and chest X-ray before attributing hypotension to neurogenic shock.

2. **Using succinylcholine for RSI beyond 48 hours post-SCI.** Denervation supersensitivity causes proliferation of extrajunctional acetylcholine receptors. Succinylcholine triggers massive potassium release, potentially causing fatal hyperkalemia. Safe only within the first 48 hours. After that, use rocuronium 1.2 mg/kg IV.

3. **Confusing spinal shock with neurogenic shock.** Spinal shock is a neurological phenomenon (areflexia, flaccidity below the lesion) — NOT a hemodynamic state. Neurogenic shock is a circulatory failure (hypotension + bradycardia from loss of sympathetic tone). They coexist but require different management: neurogenic shock needs vasopressors; spinal shock is observed until it resolves.

4. **Missing non-contiguous spinal fractures.** 10-15% of spinal fractures are non-contiguous. Imaging only the symptomatic level misses additional injuries. CT the entire spine in any patient with one identified fracture, altered mental status, or distracting injury.

5. **Not maintaining MAP targets.** Failure to augment MAP to 75-90 mmHg worsens secondary ischemic injury to the cord. This requires an arterial line and ICU admission — do not manage acute SCI hemodynamics on a floor bed with intermittent NIBP cuffs.

6. **Giving methylprednisolone reflexively.** NASCIS trials had significant methodological flaws, and secondary analysis driving the "8-hour window" was post-hoc. Most current guidelines (AANS/CNS, AO Spine) recommend against routine use. MPSS increases GI hemorrhage, wound infection, and pneumonia risk. If it is given, it must be within 8 hours; the 48-hour protocol is harmful.

7. **Failing to anticipate respiratory decline in cervical SCI.** Patients with C3-C5 injuries may present with adequate respirations but decompensate over hours as cord edema progresses (ascending edema). Serial FVC measurements are mandatory. A patient breathing comfortably on arrival may require intubation 6 hours later.

8. **Leaving the patient on a backboard.** Backboards cause pressure ulcers within 2 hours. SCI patients have no sensation below the lesion. Remove the patient from the backboard as soon as possible using log-roll technique while maintaining spinal alignment.

9. **Not recognizing autonomic dysreflexia in the ED.** Patients with chronic SCI at T6 or above presenting with severe hypertension and headache may be experiencing autonomic dysreflexia. The trigger is almost always a distended bladder or fecal impaction. Catheterize the bladder immediately. Treating the hypertension without removing the trigger leads to recurrence.

10. **Assuming a "complete" injury in the setting of spinal shock.** The ASIA exam performed during spinal shock (absent bulbocavernosus reflex) is unreliable. A patient who appears to have ASIA A (complete) injury during spinal shock may convert to incomplete (ASIA B-D) once spinal shock resolves. Accurate prognostication requires re-examination at 72 hours.
