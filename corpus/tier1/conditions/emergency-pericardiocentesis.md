---
id: emergency-pericardiocentesis
condition: Emergency Pericardiocentesis
aliases: [pericardiocentesis, pericardial drainage, pericardial tap, needle pericardiocentesis]
icd10: [I31.9, I30.9, S26.01XA]
esi: 1
time_to_harm:
  irreversible_injury: "< 10 minutes (cardiac arrest from obstructive shock)"
  death: "< 15 minutes without drainage in acute tamponade"
  optimal_intervention_window: "Immediate upon hemodynamic compromise"
mortality_if_delayed: "Acute tamponade untreated: near 100% mortality; drainage of as little as 20-50 mL can restore cardiac output"
category: procedural
track: tier1
sources:
  - type: guideline
    ref: "Adler Y, Charron P, Imazio M, et al. 2015 ESC Guidelines for the diagnosis and management of pericardial diseases. Eur Heart J. 2015;36(42):2921-2964."
    pmid: "26320112"
  - type: review
    ref: "Ainsworth CD, Salehian O. Echo-guided pericardiocentesis: let the bubbles show the way. Circulation. 2011;123(4):e210-e211."
    pmid: "21282503"
  - type: pubmed
    ref: "Tsang TS, Enriquez-Sarano M, Freeman WK, et al. Consecutive 1127 therapeutic echocardiographically guided pericardiocenteses: clinical profile, practice patterns, and outcomes spanning 21 years. Mayo Clin Proc. 2002;77(5):429-436."
    pmid: "12004993"
  - type: textbook
    ref: "Roberts JR, Custalow CB, Thomsen TW. Roberts and Hedges' Clinical Procedures in Emergency Medicine and Acute Care, 7th Edition. Elsevier. 2019."
  - type: guideline
    ref: "ATLS Advanced Trauma Life Support, 10th Edition. American College of Surgeons. 2018."
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
# Emergency Pericardiocentesis

## Recognition

**Indications:**
- Cardiac tamponade with hemodynamic instability (hypotension, tachycardia, elevated JVP, muffled heart sounds)
- Echocardiographic evidence of tamponade physiology: pericardial effusion with right atrial collapse in systole, right ventricular diastolic collapse, respiratory variation in mitral/tricuspid inflow (> 25% variation), dilated non-collapsible IVC
- Pulseless electrical activity (PEA) with pericardial effusion on bedside echo
- Large pericardial effusion causing hemodynamic compromise despite fluid resuscitation

**Clinical Features of Tamponade (Beck triad present in <10% acutely):**
- Hypotension (± pulsus paradoxus >10 mmHg)
- Elevated JVP (distended neck veins)
- Muffled/distant heart sounds
- Tachycardia
- Electrical alternans on ECG (swinging heart)
- Kussmaul sign (JVP rises with inspiration)

**Contraindications:**
- Traumatic tamponade with cardiac arrest or peri-arrest: pericardiocentesis is inadequate — proceed to resuscitative thoracotomy for definitive cardiac repair
- Aortic dissection as cause of tamponade: pericardiocentesis may worsen hemorrhage by decompressing the tamponade that is tamponading the aortic tear — emergent surgical consultation
- Myocardial rupture: temporize with pericardiocentesis if no OR available, but definitive management is surgical
- Small effusion without hemodynamic compromise (observe, serial echo)
- Relative: coagulopathy, thrombocytopenia (correct if possible but do not delay in hemodynamic compromise)

## Critical Actions

| Action | Target |
|--------|--------|
| Bedside echo confirming effusion | < 2 minutes |
| Needle in pericardial space | < 5 minutes from decision |
| Volume aspirated | As little as 20-50 mL may restore hemodynamics |
| Post-aspiration echo | Immediately to confirm decompression |

1. **Bedside echocardiography** — confirm pericardial effusion and tamponade physiology
2. **IV fluid bolus** — 500-1000 mL NS to temporize (augments preload)
3. **Avoid intubation if possible** — positive pressure ventilation worsens tamponade by reducing venous return
4. **Identify approach** — subxiphoid (traditional), parasternal (US-guided, often optimal), or apical
5. **Aspirate pericardial fluid** under US guidance
6. **Place pigtail catheter** for continuous drainage if re-accumulation anticipated
7. **Reassess with echo** — resolution of RV diastolic collapse and hemodynamic improvement

## Differential Diagnosis

**Other Causes of Obstructive Shock:**

| Condition | Distinguishing Features |
|-----------|----------------------|
| Tension pneumothorax | Absent breath sounds unilateral; tracheal deviation; no pericardial effusion on echo |
| Massive pulmonary embolism | RV dilation without pericardial effusion; D-sign on echo; CT angiography |
| Constrictive pericarditis | Chronic; thickened pericardium on echo/CT; no effusion |
| Restrictive cardiomyopathy | No pericardial effusion; thickened myocardium; diastolic dysfunction |
| Right ventricular MI | Inferior STEMI on ECG; RV dilation; no effusion |

**Etiology of Pericardial Effusion:**

| Category | Examples |
|----------|---------|
| Traumatic | Penetrating cardiac injury, blunt cardiac injury, aortic dissection |
| Infectious | Viral pericarditis, TB, bacterial, HIV |
| Malignant | Lung cancer, breast cancer, lymphoma, melanoma |
| Inflammatory | Uremic, post-MI (Dressler syndrome), lupus, post-pericardiotomy |
| Iatrogenic | Post-cardiac catheterization, post-pacemaker, post-cardiac surgery |
| Idiopathic | Up to 50% of large effusions |

## Workup

**Pre-Procedure Assessment:**
- Bedside echocardiography (POCUS): subxiphoid or parasternal long-axis view — confirm effusion, quantify size, identify optimal needle trajectory
- ECG: low voltage, electrical alternans, diffuse ST elevation (pericarditis)
- Vital signs: document degree of hemodynamic compromise
- Labs: CBC, coagulation, BMP, type and screen (if traumatic)
- Identify largest fluid pocket closest to skin surface (this determines the approach)

**Equipment:**

| Item | Specification |
|------|---------------|
| Ultrasound | Phased array or curvilinear probe; sterile cover |
| Needle/catheter | 18g spinal needle (8-12 cm) or pericardiocentesis kit with pigtail catheter (6-8 Fr) |
| Syringe | 20-60 mL syringe |
| Three-way stopcock | For controlled aspiration |
| Collection bag/bottles | For cytology, culture, cell count if indicated |
| Lidocaine | 1% lidocaine 5-10 mL for local anesthesia |
| Alligator clip + ECG cable | For ECG-guided technique (optional — US guidance preferred) |
| Monitoring | Continuous cardiac monitor, SpO2, BP |

## Treatment

### Ultrasound-Guided Parasternal Approach (Often Optimal)

**Step 1: Identify Optimal Window**
- Scan subxiphoid, parasternal long-axis, parasternal short-axis, and apical views
- Select the approach where the effusion is largest, closest to the skin, and avoids vital structures (liver, lung, internal mammary artery)
- The parasternal approach often provides the shortest needle path to the effusion

**Step 2: Prep**
- Elevate head of bed 30-45 degrees (fluid pools inferiorly and anteriorly)
- Chlorhexidine skin prep, sterile drape
- Lidocaine 1% 5-10 mL along anticipated needle track (skin to pericardium)

**Step 3: Needle Insertion (Parasternal)**
- Insert 18g spinal needle at the left 5th or 6th intercostal space, adjacent to the sternum (avoiding internal mammary artery 1-2 cm lateral to sternum)
- Advance under real-time US guidance, visualizing the needle tip
- Aspirate as you advance
- Pericardial entry: sudden aspiration of fluid (serous, bloody, or serosanguinous)

### Subxiphoid Approach (Traditional)

**Step 1: Position**
- Head of bed 30-45 degrees
- Subxiphoid window on US to visualize effusion anterior to the heart

**Step 2: Insert Needle**
- Entry point: 1-2 cm inferior and to the left of the xiphoid process
- Angle needle 45 degrees to skin, directed toward the left shoulder
- Advance under US guidance, aspirating continuously
- Needle passes through skin → subcutaneous tissue → rectus sheath → diaphragm → pericardium
- Typical depth: 6-8 cm in adults

**Step 3: Aspirate**
- Once fluid returns, stop advancing
- Aspirate slowly — even 20-50 mL can dramatically improve hemodynamics
- Monitor BP and heart rate during aspiration — expect improvement within seconds

### Confirmation

- **Agitated saline test:** inject 5-10 mL agitated saline through the needle; observe on echo — if bubbles appear in the pericardial space, needle is correctly positioned; if bubbles appear in the cardiac chambers, needle is intracardiac — withdraw immediately
- **Fluid analysis:** bloody fluid may be pericardial or intracardiac; pericardial blood does not clot (defibrinated); intracardiac blood will clot
- **Hemodynamic response:** BP improvement, HR decrease, resolution of pulsus paradoxus

### Pigtail Catheter Placement (For Ongoing Drainage)

- After confirming pericardial needle position, pass guidewire through the needle
- Dilate the tract and advance 6-8 Fr pigtail catheter over the wire into the pericardial space
- Connect to drainage bag
- Confirm catheter position with echo
- Secure to skin with suture

### Post-Procedure
- Repeat echocardiography to confirm reduction in effusion and resolution of tamponade physiology
- Send pericardial fluid for: cell count, protein, LDH, glucose, cytology, culture, AFB (based on clinical suspicion)
- Monitor for re-accumulation (serial echo)
- Ongoing hemodynamic monitoring
- Cardiology and/or cardiac surgery consultation

## Disposition

- **Successful pericardiocentesis with hemodynamic improvement:** ICU admission; pigtail drain if recurrent; cardiology consultation
- **Traumatic tamponade not responding to pericardiocentesis:** emergent thoracotomy
- **Recurrent tamponade despite drainage:** pericardial window (surgical — cardiothoracic surgery)
- **Malignant effusion:** oncology consultation; may require pericardial window or sclerotherapy
- **Transfer:** stabilize with pericardiocentesis, leave pigtail drain in place, transfer with monitoring

## Pitfalls

1. **Attempting pericardiocentesis for traumatic tamponade instead of thoracotomy.** Traumatic tamponade from penetrating injury involves active hemorrhage into the pericardial space. Pericardiocentesis removes blood but does not stop the source. The pericardium re-fills in seconds to minutes. Penetrating traumatic arrest requires resuscitative thoracotomy for direct cardiac repair.

2. **Intubating the patient with tamponade.** Positive pressure ventilation reduces venous return, which is already compromised in tamponade. This can precipitate cardiac arrest on induction. If intubation is unavoidable, prepare for immediate pericardiocentesis or thoracotomy simultaneously. Volume load with 500-1000 mL NS before induction.

3. **Advancing the needle without ultrasound guidance.** Blind subxiphoid pericardiocentesis has a 20% complication rate (myocardial perforation, coronary laceration, pneumothorax). US-guided technique reduces complications to < 2%. If US is available, it must be used.

4. **Stopping aspiration too soon.** Patients may initially improve with 20-50 mL aspirated, but tamponade can recur rapidly, especially in malignant or inflammatory effusions. Aspirate as completely as possible and place a pigtail drain for ongoing drainage if the effusion is > 200-300 mL.

5. **Misinterpreting bloody aspirate as cardiac chamber puncture.** Pericardial blood from chronic or subacute effusions is defibrinated and does NOT clot. Intracardiac blood WILL clot in the syringe. If in doubt, use the agitated saline echo test to confirm needle position.

6. **Not administering IV fluids before and during pericardiocentesis.** Volume loading (500-1000 mL NS bolus) augments cardiac preload and can temporarily improve hemodynamics while preparing for the procedure. Performing pericardiocentesis on a volume-depleted patient increases the risk of cardiovascular collapse during the procedure.
