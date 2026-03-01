---
id: prosthetic-valve-emergency
condition: Prosthetic Valve Emergency
aliases: [prosthetic valve thrombosis, stuck valve, mechanical valve malfunction, prosthetic valve dysfunction, prosthetic valve dehiscence]
icd10: [T82.09XA, T82.01XA, T82.02XA, T82.03XA]
esi: 1
time_to_harm:
  irreversible_injury: "< 2 hours"
  death: "< 6 hours"
  optimal_intervention_window: "< 1 hour"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "2020 ACC/AHA Guideline for the Management of Patients With Valvular Heart Disease. J Am Coll Cardiol. 2021;77(4):e25-e197."
  - type: review
    ref: "Dangas GD, et al. Management of Mechanical Prosthetic Heart Valve Thrombosis: JACC Review Topic of the Week. J Am Coll Cardiol. 2023;81(20):2004-2016."
  - type: guideline
    ref: "2021 ESC/EACTS Guidelines for the Management of Valvular Heart Disease. Eur Heart J. 2022;43(7):561-632."
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
# Prosthetic Valve Emergency

## Recognition

**Valve thrombosis (mechanical valves):**
- Acute dyspnea, heart failure, or cardiogenic shock
- Muffled or absent mechanical valve clicks on auscultation (normally audible, metallic clicks)
- New or changed murmur (regurgitant or obstructive)
- Subtherapeutic INR — most common precipitant
- Systemic embolization (stroke, limb ischemia) with thrombotic valve

**Valve dehiscence:**
- Acute severe regurgitation → flash pulmonary edema, cardiogenic shock
- New rocking motion of valve on echocardiography
- Often caused by endocarditis or surgical technical failure
- Paravalvular leak → hemolytic anemia (chronic LDH elevation, schistocytes)

**Structural valve deterioration (bioprosthetic valves):**
- Gradual valve stenosis or regurgitation (years after implantation)
- Acute decompensation when critical stenosis/regurgitation reached
- Typically 10-20 years post-implantation

**Prosthetic valve endocarditis (PVE):**
- Fever, new regurgitant murmur, embolic phenomena
- Early PVE (< 60 days post-surgery): S. aureus, coagulase-negative staph, gram-negatives
- Late PVE (> 60 days): Streptococci, enterococci, S. aureus

## Critical Actions

| Action | Target |
|---|---|
| Auscultation for valve clicks | Immediate |
| Echocardiography (TTE then TEE) | < 30 minutes |
| INR level | < 15 minutes |
| Cardiac surgery consultation | Immediate |

1. **Stabilize hemodynamics** — IV fluids (cautious in acute MR/obstructive lesions), vasopressors as needed
2. **Urgent echocardiography** — TTE first, then TEE for better prosthetic valve visualization. Assess valve motion, gradient, regurgitation, thrombus, vegetation.
3. **Check INR immediately** — subtherapeutic INR is the most common cause of mechanical valve thrombosis
4. **Fluoroscopy** — assess mechanical leaflet motion (tilting disc or bileaflet). Restricted motion = obstruction.
5. **Cardiac surgery consultation STAT** for all prosthetic valve emergencies
6. **For suspected PVE:** Blood cultures x 3 from separate sites BEFORE antibiotics, then empiric antibiotics immediately
7. **Anticoagulation management:** UFH bridge for subtherapeutic INR (heparin 60 units/kg IV bolus, then 12 units/kg/hr)

## Differential Diagnosis

- **Acute decompensated heart failure** (non-valvular) — prior valve replacement may coexist with ischemic or hypertensive HF
- **Prosthetic valve endocarditis** — fever, embolic phenomena; overlaps with thrombosis
- **Pannus ingrowth** — gradual valve obstruction by fibrous tissue, NOT thrombosis; does not respond to anticoagulation/thrombolysis
- **Patient-prosthesis mismatch** — effective orifice area too small for body size; high gradients but no acute change
- **Acute MI** — may coexist; coronary embolism from valve thrombus
- **Pulmonary embolism** — dyspnea with prosthetic valve; check for valve dysfunction on echo

## Workup

- **Transthoracic echocardiography (TTE):** Valve gradients, regurgitation, leaflet motion, LV function, pericardial effusion
- **Transesophageal echocardiography (TEE):** Superior for prosthetic valves — detects small thrombi, vegetations, paravalvular abscess, dehiscence. Mandatory for mitral prostheses.
- **Fluoroscopy:** Real-time assessment of mechanical leaflet motion — restricted = thrombosis or pannus
- **CT angiography (cardiac gated):** Delineates thrombus vs pannus, measures thrombus volume
- **Labs:** INR, aPTT, CBC (anemia from hemolysis, leukocytosis), LDH, haptoglobin, reticulocyte count (hemolytic anemia), blood cultures x 3
- **ECG:** Rhythm, ischemia
- **Chest X-ray:** Pulmonary edema, prosthetic valve position

## Treatment

### Obstructive Valve Thrombosis — Hemodynamically Stable
- **Small thrombus (< 0.8 cm2):** IV heparin followed by slow-dose thrombolysis
  - tPA 25 mg IV over 25 hours, repeat if needed (max 200 mg total); OR
  - Streptokinase 250,000 IU IV over 30 min, then 100,000 IU/hr for 24-72 hours
- Serial echo monitoring during thrombolysis
- Optimize warfarin anticoagulation

### Obstructive Valve Thrombosis — NYHA III-IV or Large Thrombus (>= 0.8 cm2)
- **Emergent surgery** (valve replacement or thrombectomy) — preferred
- Thrombolysis as alternative if surgery unavailable or high surgical risk
- tPA 10 mg IV bolus, then 90 mg over 90 min (accelerated regimen for critical obstruction)

### Non-obstructive Valve Thrombosis
- IV heparin bridge, optimize warfarin (target INR per valve position)
- Aortic mechanical valve: target INR 2.5 (range 2.0-3.0)
- Mitral mechanical valve: target INR 3.0 (range 2.5-3.5)
- Serial echo to confirm resolution

### Valve Dehiscence
- Emergent surgical repair or replacement
- Hemodynamic support: vasopressors, inotropes, IABP as bridge to surgery
- If endocarditis-related: antibiotics first, then surgery within 48 hours

### Prosthetic Valve Endocarditis
- Empiric antibiotics (native vs prosthetic protocol):
  - Vancomycin 15-20 mg/kg IV q8-12h + gentamicin 1 mg/kg IV q8h + rifampin 300 mg PO q8h (for prosthetic valve)
- Blood cultures before antibiotics
- Surgery indications: heart failure, uncontrolled infection, large vegetation (> 10 mm), abscess, embolic events

## Disposition

- **ICU admission:** All hemodynamically unstable prosthetic valve emergencies, post-thrombolysis, post-surgery
- **Cardiac surgery monitoring:** Stable valve thrombosis on heparin pending definitive management
- **Transfer:** Facilities without cardiac surgery must transfer immediately — do not attempt thrombolysis without surgical backup
- **Never discharge:** Any suspected prosthetic valve malfunction requires inpatient workup and cardiac surgery consultation

## Pitfalls

1. **Failing to auscultate for mechanical valve clicks.** Absent or muffled metallic clicks in a patient with a mechanical valve is the quickest bedside clue to valve thrombosis or malfunction. This finding should immediately trigger echocardiography and surgical consultation.

2. **Attributing dyspnea in a prosthetic valve patient to a non-cardiac cause.** Any new dyspnea, exercise intolerance, or heart failure symptoms in a patient with a prosthetic valve must be presumed to be valve-related until proven otherwise. Echo is mandatory.

3. **Attempting thrombolysis without surgical backup.** Thrombolysis of prosthetic valve thrombus carries risk of systemic embolization (~10%), incomplete lysis, and hemodynamic deterioration. Cardiac surgery must be immediately available.

4. **Missing subtherapeutic INR as the precipitant.** The most common cause of mechanical valve thrombosis is inadequate anticoagulation. Always check INR immediately and initiate heparin bridge while investigating.

5. **Confusing pannus with thrombus.** Pannus (fibrous ingrowth) causes valve obstruction but does NOT respond to anticoagulation or thrombolysis. CT and TEE can help differentiate. Pannus requires surgical intervention. Treating pannus with prolonged thrombolysis wastes time and exposes the patient to bleeding risk.
