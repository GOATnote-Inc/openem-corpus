---
id: coagulopathy-of-trauma
condition: Coagulopathy of Trauma
aliases: [trauma-induced coagulopathy, TIC, acute traumatic coagulopathy, ATC, trauma coagulopathy]
icd10: [D68.9, T79.A19A]
esi: 1
time_to_harm:
  irreversible_injury: "< 1 hour (exsanguination)"
  death: "< 2 hours (lethal triad: hypothermia, acidosis, coagulopathy)"
  optimal_intervention_window: "< 3 hours (TXA administration)"
category: hematologic
track: tier1
sources:
  - type: guideline
    ref: "AAST/AANS Practice Guidelines: Damage Control Resuscitation in Patients with Severe Traumatic Hemorrhage, 2024"
  - type: guideline
    ref: "ACS TQIP Massive Transfusion in Trauma Guidelines"
  - type: guideline
    ref: "European Guideline on Management of Major Bleeding and Coagulopathy Following Trauma, 5th Edition, 2019"
  - type: review
    ref: "CRASH-2: Effects of Tranexamic Acid on Death in Bleeding Trauma Patients. Lancet, 2010"
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
# Coagulopathy of Trauma

## Recognition

**Presentation:**
- Ongoing hemorrhage from wounds, body cavities, or surgical sites despite mechanical hemostasis
- Non-surgical bleeding from mucosal surfaces, venipuncture sites, line insertion sites
- Diffuse oozing without identifiable surgical bleeding source
- Hemodynamic instability disproportionate to visible blood loss
- Hypothermia (< 35°C)
- Metabolic acidosis (pH < 7.2, base deficit > 6, lactate > 4 mmol/L)

**Lethal triad of trauma:**
- Hypothermia
- Acidosis
- Coagulopathy
- These three are synergistic — each worsens the others; breaking the cycle requires simultaneous correction

**Pathophysiology (trauma-induced coagulopathy is NOT just dilutional):**
- Tissue injury activates protein C → anticoagulant state
- Hypoperfusion/shock → endothelial glycocalyx shedding → autoheparinization
- Platelet dysfunction from hypothermia and acidosis
- Hyperfibrinolysis
- Factor consumption and dilution from crystalloid resuscitation

**Risk factors for TIC:**
- Injury Severity Score (ISS) > 25
- Base deficit > 6 mEq/L
- Systolic BP < 70 mmHg
- pH < 7.1
- Temperature < 34°C
- Massive transfusion requirement (>= 10 units PRBCs in 24h)

## Critical Actions

1. **Activate massive transfusion protocol (MTP)** — immediately upon recognition of hemorrhagic shock
2. **Tranexamic acid (TXA) 1 g IV over 10 minutes** — administer within 3 hours of injury (ideally prehospital); follow with 1 g IV over 8 hours
3. **Damage control resuscitation:** Balanced transfusion 1:1:1 (PRBC:FFP:platelets)
4. **Permissive hypotension:** Target SBP 80-90 mmHg (MAP 50-60) until hemorrhage controlled. Exception: traumatic brain injury (maintain SBP > 100)
5. **Damage control surgery:** Hemorrhage control and contamination control; definitive repair deferred
6. **Prevent/treat hypothermia** — active warming, warm fluids, bear hugger, warm environment
7. **Correct acidosis** through perfusion restoration, not bicarbonate

## Differential Diagnosis

- Pre-existing coagulopathy (anticoagulant use — warfarin, DOACs, heparin)
- Pre-existing bleeding disorder (hemophilia, von Willebrand disease)
- Dilutional coagulopathy (from crystalloid-heavy resuscitation)
- DIC from non-traumatic cause (sepsis, malignancy, obstetric)
- Massive transfusion complications (citrate toxicity → hypocalcemia → impaired coagulation)
- Hypothermia-induced coagulopathy (cold impairs enzymatic clotting cascade)

## Workup

- **Point-of-care testing (preferred):**
  - **Viscoelastic testing (TEG/ROTEM)** — provides real-time assessment of clot formation, strength, and lysis; guides targeted component therapy
  - **iSTAT or point-of-care INR/aPTT**
  - **Point-of-care lactate and base deficit**
- **Standard labs (send simultaneously but do NOT wait for results):**
  - PT/INR, aPTT, fibrinogen
  - CBC with platelet count
  - ABG/VBG (pH, base deficit, lactate)
  - Ionized calcium (critical — hypocalcemia from citrated blood products impairs clotting)
  - Type and crossmatch (use O-negative/O-positive uncrossmatched blood until available)
- **Fibrinogen** — target > 150-200 mg/dL (trauma guidelines)
- **Ionized calcium** — target > 1.1 mmol/L; hypocalcemia is common with massive transfusion
- **Temperature** — core temperature; hypothermia impairs coagulation at any temperature < 35°C
- **FAST exam** — identify intra-abdominal, pericardial hemorrhage
- **CXR** — hemothorax
- **Pelvic X-ray** — pelvic fracture (high-volume hemorrhage source)

## Treatment

### Massive Transfusion Protocol (MTP)
- **1:1:1 ratio** of PRBCs : FFP : platelets (or as close as feasible)
- **Initial release:** 6 units PRBCs + 6 units FFP + 1 apheresis platelet (or equivalent)
- Repeat cycles until hemorrhage controlled
- **O-negative PRBCs** for women of childbearing age; O-positive for others until type-specific available
- **AB plasma** until type-specific available (universal donor plasma)

### Tranexamic Acid (TXA)
- **1 g IV over 10 minutes** — give as early as possible (ideally prehospital)
- **1 g IV over 8 hours** — maintenance infusion
- **Must be given within 3 hours of injury** — after 3 hours, TXA may increase mortality (CRASH-2)
- Do NOT give TXA > 3 hours post-injury unless isolated hyperfibrinolysis on TEG/ROTEM

### Fibrinogen Replacement
- **Cryoprecipitate** 10 units (1 pooled dose) if fibrinogen < 150 mg/dL
- **OR Fibrinogen concentrate (RiaSTAP)** 70 mg/kg IV (where available; more rapid, no crossmatch needed)
- Target fibrinogen > 150-200 mg/dL

### Calcium Replacement
- **Calcium chloride 1 g IV** (or calcium gluconate 3 g IV) for every 4-6 units of blood products
- Monitor ionized calcium q30 min during MTP; target iCa > 1.1 mmol/L
- Hypocalcemia impairs clotting AND myocardial contractility

### Hypothermia Prevention/Treatment
- **Active warming:** Forced-air warming blanket, warm IV fluids (Level 1 rapid infuser with warmer), warm environment (target room temp 28°C)
- **Remove wet clothing immediately**
- Target core temperature > 36°C

### Acidosis Correction
- Correct through hemorrhage control and perfusion restoration
- Sodium bicarbonate 1 mEq/kg IV only if pH < 7.1 and refractory to volume resuscitation
- Acidosis (pH < 7.2) impairs Factor VIIa and other clotting factor activity by 50-90%

### TEG/ROTEM-Guided Therapy
- **Prolonged R-time/CT (clotting time):** Give FFP
- **Low MA/MCF (clot strength):** Give platelets
- **Low fibrinogen contribution:** Give cryoprecipitate/fibrinogen concentrate
- **Hyperfibrinolysis (LY30 > 3%):** Give TXA (additional dose if already given)

### Reversal of Anticoagulants (If Applicable)
- **Warfarin:** 4-factor PCC 25-50 units/kg IV + vitamin K 10 mg IV
- **DOACs (rivaroxaban, apixaban):** Andexanet alfa 400-800 mg IV bolus (if available); otherwise 4-factor PCC 50 units/kg
- **Dabigatran:** Idarucizumab 5 g IV
- **Heparin:** Protamine 1 mg per 100 units of heparin given

## Disposition

- **All trauma coagulopathy patients:** Trauma ICU, operating room, or interventional radiology suite
- **Damage control sequence:** OR for hemorrhage control → ICU for resuscitation → return to OR for definitive repair in 24-72h
- **Blood bank communication:** Keep MTP active until hemorrhage controlled; communicate product needs continuously
- **Interventional radiology:** For non-compressible hemorrhage (pelvic fractures, solid organ injury)
- **Isolation:** Standard precautions
- **Reportable:** Not a reportable disease (individual trauma events may have reporting requirements depending on mechanism)

## Pitfalls

1. **Administering TXA > 3 hours after injury.** CRASH-2 data shows increased mortality with late TXA administration (> 3 hours). Give early or not at all (unless TEG/ROTEM shows active hyperfibrinolysis).

2. **Resuscitating with crystalloid instead of blood products.** Crystalloid-heavy resuscitation dilutes clotting factors, worsens hypothermia, and contributes to the lethal triad. Damage control resuscitation prioritizes balanced blood product transfusion.

3. **Ignoring ionized calcium.** Citrated blood products chelate calcium. Hypocalcemia impairs both clotting factor activity and myocardial contractility. Replace calcium proactively during MTP.

4. **Waiting for lab results to transfuse.** Standard coagulation labs take 30-60 minutes. In hemorrhagic shock, activate MTP and transfuse empirically. Use point-of-care testing (TEG/ROTEM) for real-time guidance when available.

5. **Targeting normal blood pressure.** Permissive hypotension (SBP 80-90 mmHg) reduces ongoing hemorrhage before surgical control. Exception: traumatic brain injury requires SBP > 100 mmHg.

6. **Failure to actively rewarm.** Coagulation factor activity drops significantly below 35°C. Warm the room, use fluid warmers, and apply forced-air blankets. This is as important as any transfusion.
