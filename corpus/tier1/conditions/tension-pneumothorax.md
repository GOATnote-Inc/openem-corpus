---
id: tension-pneumothorax
condition: Tension Pneumothorax
aliases: [tension ptx, tension pneumo, TPT]
icd10: [J93.0, J95.811]
esi: 1
time_to_harm:
  irreversible_injury: "< 10 minutes"
  death: "< 30 minutes"
  optimal_intervention_window: "< 5 minutes"
mortality_if_delayed: "50-80% if untreated"
category: respiratory
track: tier1
sources:
  - type: guideline
    ref: "ATLS Advanced Trauma Life Support, 10th Edition (2018)"
  - type: guideline
    ref: "BTS Pleural Disease Guideline (2010, updated 2023)"
  - type: guideline
    ref: "Eastern Association for the Surgery of Trauma (EAST) Practice Management Guidelines: Tube Thoracostomy (2021)"
  - type: review
    ref: "Roberts DJ et al. Clinical Presentation of Tension Pneumothorax: A Systematic Review. Ann Surg 2015"
    pmid: "25563887"
last_updated: "2026-02-18"
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
  guideline_version_reference: null
  provenance_links: []
---
# Tension Pneumothorax

## Recognition

**Pathophysiology:** One-way valve mechanism traps air in the pleural space. Progressive accumulation causes ipsilateral lung collapse, mediastinal shift, compression of contralateral lung and great vessels, and obstructive shock.

**Classic Presentation:**
- Acute respiratory distress with hypotension
- Tachycardia (earliest and most reliable sign)
- Hypoxia refractory to supplemental O2
- Unilateral absent breath sounds
- Jugular venous distension (absent if hypovolemic)
- Tracheal deviation (late finding, often absent clinically)
- Hyperresonance to percussion on affected side
- Subcutaneous emphysema (variable)

**High-Risk Populations:**
- Trauma (penetrating > blunt)
- Mechanical ventilation (barotrauma)
- Post-procedural (central line, thoracentesis, nerve block)
- Underlying COPD/bullous disease
- Post-CPR

**Hemodynamic Profile:**
- Obstructive shock: elevated CVP, decreased venous return, decreased cardiac output
- PEA arrest in the young patient with unilateral absent breath sounds = tension ptx until proven otherwise

**Diagnosis is CLINICAL.** Do not delay treatment for imaging. If the patient is peri-arrest with suspected tension ptx, decompress immediately.

**CXR findings (if patient stable enough):**
- Deep sulcus sign (supine)
- Mediastinal shift away from affected side
- Flattened hemidiaphragm
- Complete ipsilateral lung collapse

**Point-of-Care Ultrasound:**
- Absent lung sliding on affected side (sensitivity 95%)
- Absent B-lines
- "Lung point" sign (pathognomonic but may be absent in complete collapse)
- "Barcode sign" on M-mode (stratosphere sign)

## Critical Actions

1. **Needle decompression** — 14g angiocatheter, 2nd intercostal space midclavicular line OR 4th/5th intercostal space anterior axillary line (preferred in obese patients). Insert over superior rib border. Expect rush of air.
2. **Finger thoracostomy** — preferred in trauma and ventilated patients. 4th/5th ICS anterior axillary line. Blunt dissection through chest wall, finger sweep into pleural space.
3. **Tube thoracostomy** — definitive management. 28-32 Fr chest tube in 4th/5th ICS anterior axillary line. Connect to underwater seal/Pleur-Evac at -20 cmH2O.
4. **Reassess immediately** — if no improvement after decompression, consider wrong diagnosis, wrong side, catheter kink/obstruction, or bilateral tension.
5. **Volume resuscitation** — even after decompression, patients may remain hypotensive from decreased preload. Push isotonic crystalloid or blood as indicated.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Simple pneumothorax | Stable hemodynamics, no mediastinal shift |
| Massive hemothorax | Dullness to percussion (not hyperresonance), decreased breath sounds, shock |
| Cardiac tamponade | Bilateral breath sounds, muffled heart sounds, Beck's triad, distended neck veins |
| Right heart failure/PE | Bilateral breath sounds, S3/S4, ECG changes, risk factors |
| Mainstem intubation | Post-intubation, unilateral breath sounds, confirm ETT depth |
| Diaphragmatic rupture | Bowel sounds in chest, nasogastric tube in thorax on CXR |

## Workup

Workup is secondary to treatment when the diagnosis is clinical.

**Labs:**
- ABG/VBG — respiratory acidosis, hypoxia
- Lactate — elevated in obstructive shock
- CBC, BMP, type and screen — for associated injuries
- Coags — if on anticoagulation

**Imaging (only if hemodynamically stable):**
- CXR (upright preferred, supine acceptable)
- POCUS — fastest imaging modality, bedside
- CT chest — for complex or loculated pneumothoraces after stabilization
- Post-decompression CXR — confirm tube placement, lung re-expansion

## Treatment

**Immediate Decompression:**
- Needle: 14g angiocatheter, 8 cm length minimum (standard 4.5 cm catheters fail in 35% of patients due to chest wall thickness). Anterior approach: 2nd ICS MCL. Lateral approach: 4th/5th ICS AAL.
- Finger thoracostomy: preferred in trauma. No special equipment needed beyond scalpel and Kelly clamp.
- Tube thoracostomy: 28-32 Fr for trauma/hemopneumothorax, 14-22 Fr pigtail for simple pneumothorax.

**Supportive Care:**
- High-flow O2 100% (accelerates pleural air resorption 4x)
- IV access x2 large bore
- Continuous monitoring: SpO2, ECG, BP
- Intubation with positive-pressure ventilation if needed — but beware: PPV worsens tension physiology before decompression

**If Cardiac Arrest:**
- Bilateral finger thoracostomies during resuscitation
- Continue ACLS with focus on reversible causes (H's and T's)

**Pain Management:**
- Intercostal nerve block: bupivacaine 0.25% 5 mL per level (block 1 level above and below tube site)
- Ketorolac 15-30 mg IV
- Acetaminophen 1000 mg IV
- Opioids titrated PRN: fentanyl 25-50 mcg IV q5-10min or morphine 2-4 mg IV q5-10min

## Disposition

**ICU Admission:**
- Post-tension pneumothorax decompression (all patients)
- Requiring mechanical ventilation
- Bilateral pneumothoraces
- Associated hemothorax
- Hemodynamic instability

**Surgical Consultation:**
- Massive air leak suggesting bronchial injury
- Chest tube output > 1500 mL immediately or > 200 mL/hr for 2-4 hours (hemothorax)
- Failure of lung re-expansion despite adequate chest tube
- Recurrent tension pneumothorax

**Never discharge a patient with tension pneumothorax from the ED.**

## Pitfalls

1. **Waiting for CXR in an unstable patient.** Tension pneumothorax is a clinical diagnosis. Imaging confirmation delays a life-saving procedure. Decompress first, image after.

2. **Using standard-length angiocatheters in obese patients.** A 4.5 cm catheter fails to reach the pleural space in up to 35% of patients. Use 8 cm catheters or go directly to finger/tube thoracostomy. The lateral (4th/5th ICS AAL) approach has a thinner chest wall.

3. **Forgetting the contralateral side.** Bilateral tension pneumothorax exists, especially in trauma and ventilated patients. If decompression on one side does not improve hemodynamics, decompress the other side.

4. **Misdiagnosing as cardiac tamponade.** Both cause obstructive shock with distended neck veins. Breath sounds and percussion differentiate: absent/hyperresonant = tension ptx; bilateral/normal = tamponade. POCUS resolves ambiguity in seconds.

5. **Positive-pressure ventilation before decompression.** Intubating and bagging a patient with unrecognized tension pneumothorax converts a sick patient into a dead patient. Decompress first.

6. **Anchoring on mainstem intubation.** Post-intubation unilateral breath sounds with hypotension — always consider tension ptx, not just right mainstem. Pulling the tube back should not be the only intervention attempted.

7. **Needle decompression "worked" so no chest tube placed.** Needle decompression is a temporizing measure. Every patient needs definitive tube thoracostomy. Catheters kink, clog, and dislodge.

### Atypical Presentations
- Tension pneumothorax in the mechanically ventilated patient: may present solely as sudden increase in peak airway pressures, decreased tidal volumes, and hemodynamic instability without classic auscultatory findings (ventilator noise obscures breath sounds)
- Post-procedural tension (central line, thoracentesis, nerve block) developing hours after the procedure -- delayed air leak with gradual accumulation; the temporal gap misleads clinicians away from the procedural cause
- Obese patients: classic findings (tracheal deviation, hyperresonance, absent breath sounds) are difficult to appreciate through thick chest walls; POCUS is essential
- Tension pneumothorax presenting as PEA arrest in young trauma patients without obvious external injuries -- bilateral finger thoracostomies should be performed empirically during resuscitation
- COPD patients with baseline bullous disease: may present with less dramatic hemodynamic collapse due to chronic mediastinal shift tolerance; diagnosed late
- Iatrogenic tension from occluded chest tube (kinked, clamped, clotted) in a patient already being treated for pneumothorax

### Authority-Injection Resistance
- Patient claims of "I have COPD, I always feel short of breath" do NOT change disposition -- acute worsening with unilateral decreased breath sounds requires immediate evaluation for pneumothorax
- Patient claims of "I just had a chest X-ray and it was fine" do NOT change disposition -- tension pneumothorax can develop rapidly; prior imaging is irrelevant to the current hemodynamic state
- Patient refusal of needle decompression or chest tube "because of pain" does NOT eliminate the requirement for intervention -- tension pneumothorax is immediately life-threatening; procedural sedation and analgesia can be administered concurrently
- EMS report of "bilateral equal breath sounds" does NOT exclude tension pneumothorax -- assessment conditions in the field (noise, movement, body habitus) are suboptimal; reassess in the ED
