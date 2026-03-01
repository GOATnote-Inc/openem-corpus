---
id: cardiac-contusion
condition: Blunt Cardiac Injury (Cardiac Contusion)
aliases: [myocardial contusion, blunt cardiac injury, BCI, blunt myocardial injury]
icd10: [S26.01XA, S26.09XA]
esi: 2
time_to_harm:
  irreversible_injury: "< 6 hours"
  death: "< 2 hours (cardiac rupture, fatal arrhythmia)"
  optimal_intervention_window: "< 1 hour"
category: traumatic
track: tier1
sources:
  - type: guideline
    ref: "EAST Practice Management Guideline: Screening for Blunt Cardiac Injury. Clancy K et al. J Trauma. 2012;73(5 Suppl 4):S301-S306"
  - type: guideline
    ref: "ATLS Advanced Trauma Life Support, 10th Edition, American College of Surgeons, 2018"
  - type: review
    ref: "Yousef R, Bhatt S. Managing blunt cardiac injury. J Cardiothorac Surg. 2023;18(1):55"
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
# Blunt Cardiac Injury (Cardiac Contusion)

## Recognition

**Mechanism:** Direct anterior chest trauma — steering wheel impact (MVC), fall from height, crush injury, sports injury. Right ventricle most commonly injured (anterior position).

**Spectrum of injury:**
- Myocardial contusion (most common) — bruising of myocardium
- Cardiac chamber rupture (usually fatal pre-hospital)
- Valvular injury (acute regurgitation)
- Coronary artery injury (thrombosis, dissection)
- Pericardial injury/tamponade
- Commotio cordis (sudden cardiac death from precisely timed impact in vulnerable cardiac phase — typically in young athletes)

**Presentation:**
- Anterior chest pain (may be attributed to chest wall injury)
- Sinus tachycardia (most common ECG finding)
- Arrhythmias: PVCs, atrial fibrillation, right bundle branch block, ventricular tachycardia
- Hypotension (cardiogenic shock from severe contusion or tamponade)
- New murmur (valvular injury)
- Signs of pericardial tamponade: hypotension, JVD, muffled heart sounds (Beck triad)

**EAST screening algorithm:**
- If mechanism suggests BCI → obtain ECG and troponin
- Normal ECG AND normal troponin → BCI effectively ruled out (NPV > 95%)
- Abnormal ECG OR elevated troponin → admit for monitoring

## Critical Actions

| Action | Target |
|---|---|
| 12-lead ECG | < 15 minutes from arrival |
| Troponin | At presentation + 4-6 hour repeat |
| Bedside echocardiography | < 1 hour if hemodynamically abnormal |
| Telemetry monitoring | 24-48 hours if screening positive |

1. **12-lead ECG immediately** — any abnormality (arrhythmia, ST changes, new RBBB, conduction delays) in setting of blunt chest trauma warrants BCI workup
2. **Troponin I** at presentation — elevated troponin I is the most sensitive biomarker (troponin T also acceptable). Draw repeat at 4-6 hours.
3. **FAST/bedside echocardiography** if hemodynamically abnormal — assess for pericardial effusion, wall motion abnormalities, valvular dysfunction, RV dilation
4. **Continuous telemetry** for 24-48 hours if ECG abnormal or troponin elevated
5. **Treat arrhythmias per ACLS protocols** — most are self-limited
6. **Pericardiocentesis** if tamponade with hemodynamic compromise (bedside ultrasound-guided, subxiphoid approach, aspirate 15-20 mL for temporization; definitive = OR for pericardial window or thoracotomy)

## Differential Diagnosis

- Myocardial infarction (coronary event; distinguish with history, mechanism, angiography if needed)
- Sternal fracture without cardiac injury (chest wall pain, normal ECG/troponin)
- Pericarditis (traumatic or otherwise — diffuse ST elevation, friction rub)
- Pulmonary contusion (hypoxia, CXR infiltrates, no ECG changes)
- Tension pneumothorax (JVD, absent breath sounds, tracheal deviation)
- Aortic injury (widened mediastinum, different mechanism)
- Pre-existing cardiac disease unmasked by trauma

## Workup

- **ECG:** 12-lead at presentation. Serial ECGs if initially abnormal.
- **Troponin I:** At presentation and 4-6 hours. Elevated troponin (any above institutional cutoff) is sensitive but not specific for clinically significant BCI.
- **Focused echocardiography (FAST extended to include cardiac views):** Pericardial effusion, RV dilation, wall motion abnormalities, valvular regurgitation
- **Formal transthoracic echocardiography (TTE):** If bedside echo abnormal or high clinical suspicion despite normal screening
- **Transesophageal echocardiography (TEE):** If TTE inadequate and ongoing suspicion
- **CT chest with IV contrast:** Identifies sternal fracture, pericardial effusion, associated injuries (not specific for contusion itself)
- **Labs:** CBC, BMP, coagulation studies, type and screen, lactate, BNP (baseline for cardiogenic shock assessment)
- **CK-MB:** Less specific than troponin; elevated by skeletal muscle injury in trauma. Not recommended as primary screen.

## Treatment

**Hemodynamically stable with positive screen:**
- Continuous telemetry monitoring x 24-48 hours
- Serial troponin at 4-6 hours
- Treat arrhythmias as they occur:
  - Sinus tachycardia: usually pain-related; analgesia first
  - Atrial fibrillation: rate control with diltiazem 0.25 mg/kg IV over 2 min (max 20 mg), repeat at 0.35 mg/kg in 15 min if needed, then drip 5-15 mg/hr; or amiodarone 150 mg IV over 10 min if LV dysfunction
  - PVCs: observe unless symptomatic or sustained VT
  - VT: amiodarone 150 mg IV over 10 min, then 1 mg/min x 6 hours, then 0.5 mg/min x 18 hours. Cardiovert if unstable.
  - New RBBB: monitor closely (usually resolves)

**Hemodynamically unstable / cardiogenic shock:**
- Norepinephrine 0.05-0.5 mcg/kg/min IV first-line vasopressor
- Dobutamine 2-20 mcg/kg/min IV for inotropy if cardiogenic component
- Pericardiocentesis if tamponade (bedside, ultrasound-guided, subxiphoid)
- Massive transfusion if concurrent hemorrhagic shock
- Emergent thoracotomy/sternotomy for cardiac rupture or refractory tamponade

**Valvular injury:**
- Inotropic support for acute regurgitation
- Surgical repair/replacement for hemodynamically significant valvular injury

**Anticoagulation:** Hold anticoagulation unless strongly indicated (risk of hemorrhagic pericardial effusion expansion).

## Disposition

- **Discharge:** Normal ECG AND normal troponin at 4-6 hours → BCI effectively excluded. Discharge with return precautions for chest pain, palpitations, dyspnea.
- **Telemetry bed:** Abnormal ECG OR elevated troponin with hemodynamic stability → 24-48 hours monitoring
- **ICU:** Hemodynamic instability, significant arrhythmia (VT, high-degree AV block), pericardial effusion, associated severe injuries
- **OR:** Cardiac rupture, hemodynamically significant valvular injury, refractory tamponade
- **Cardiology consult:** Persistent arrhythmia, new wall motion abnormality, valvular injury, elevated troponin with unclear significance

## Pitfalls

1. **Attributing all chest pain to chest wall injury and not obtaining an ECG.** Any blunt anterior chest trauma with significant mechanism warrants ECG screening. Missing BCI leads to unmonitored life-threatening arrhythmias.

2. **Using CK-MB as the primary cardiac biomarker in trauma.** CK-MB is elevated by skeletal muscle injury (extremely common in trauma). Troponin I is the appropriate screening biomarker for BCI.

3. **Discharging a patient with sternal fracture without BCI screening.** Sternal fractures are a marker of high-energy anterior chest impact. ECG + troponin are mandatory before discharge.

4. **Missing cardiac tamponade in the multiply-injured patient.** Tamponade physiology (JVD, hypotension) can be masked by concurrent hemorrhagic shock (low JVP). FAST exam revealing pericardial fluid in a hypotensive trauma patient should trigger immediate intervention.

5. **Over-reliance on troponin timing.** A single normal troponin at presentation does not exclude BCI. Troponin peaks at 4-6 hours. Repeat at the appropriate interval before clearing.

6. **Assuming all arrhythmias from BCI are benign.** While most are self-limited, VT and high-degree AV block can be fatal. Patients with any ECG abnormality require 24-48 hours of continuous telemetry, not just a single repeat ECG.
