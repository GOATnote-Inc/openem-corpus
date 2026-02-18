---
id: massive-transfusion
condition: Massive Transfusion
aliases: [MTP, massive transfusion protocol, massive hemorrhage protocol]
icd10: [T45.8X5A, D68.9, R58]
esi: 1
time_to_harm: "< 30 minutes"
mortality_if_delayed: "40-60% with uncontrolled hemorrhage"
category: hematologic
track: tier1
sources:
  - type: guideline
    ref: "ATLS Advanced Trauma Life Support, 10th Edition (2018)"
  - type: guideline
    ref: "Eastern Association for the Surgery of Trauma (EAST) Practice Management Guidelines for Hemorrhage in Pelvic Fracture (2021)"
  - type: pubmed
    ref: "Holcomb JB et al. Transfusion of Plasma, Platelets, and Red Blood Cells in a 1:1:1 vs a 1:1:2 Ratio and Mortality in Patients with Severe Trauma: The PROPPR Randomized Clinical Trial. JAMA 2015;313(5):471-482"
    pmid: "25647203"
  - type: pubmed
    ref: "Cannon JW et al. Damage Control Resuscitation in Patients with Severe Traumatic Hemorrhage: A Practice Management Guideline from the Eastern Association for the Surgery of Trauma. J Trauma Acute Care Surg 2017;82(3):605-617"
    pmid: "28225743"
  - type: guideline
    ref: "ACS TQIP Massive Transfusion in Trauma Guidelines (2014)"
last_updated: "2026-02-18"
compiled_by: agent
reviewed_by: null
verification:
  pmids_verified: "2026-02-18"
  audit_completed: "2026-02-18"
---

# Massive Transfusion

## Recognition

**Definition:** Replacement of one total blood volume (approximately 70 mL/kg) within 24 hours, or transfusion of >10 units pRBC in 24 hours, or transfusion of >4 units pRBC in 1 hour with ongoing hemorrhage anticipated.

**Classic Presentation:**
- Hemorrhagic shock (tachycardia, hypotension, altered mental status)
- Visible or suspected major hemorrhage (trauma, GI, obstetric, surgical)
- Failed response to initial 1-2 unit pRBC transfusion
- Persistent hemodynamic instability despite volume resuscitation

**Triggers for MTP Activation:**
- Assessment of Blood Consumption (ABC) score >=2 (penetrating mechanism, SBP <=90, HR >=120, positive FAST)
- Shock Index >1.0 (HR/SBP)
- Clinical judgment: uncontrolled hemorrhage with hemodynamic instability
- Base deficit > -6 or lactate > 4 mmol/L with active bleeding

**Lethal Triad of Trauma:**
- Hypothermia (core temp < 35°C)
- Acidosis (pH < 7.2, base deficit > -6)
- Coagulopathy (INR > 1.5, fibrinogen < 150 mg/dL)

Each component worsens the others. Interrupting the cycle is the goal of damage control resuscitation.

## Critical Actions

1. **Activate MTP** — call blood bank with single activation code. Do not wait for lab confirmation. First cooler should arrive within 10 minutes.
2. **Transfuse 1:1:1 ratio** — pRBC:FFP:platelets per PROPPR trial data. Start with uncrossmatched type O blood (O-negative for females of childbearing age, O-positive acceptable for males).
3. **Administer tranexamic acid (TXA) 1g IV over 10 minutes** within 3 hours of injury, followed by 1g IV over 8 hours. No benefit and potential harm if given >3 hours post-injury (CRASH-2).
4. **Correct the lethal triad** — aggressive rewarming (target >36°C), calcium replacement (calcium chloride 1g IV per 4 units blood products), serial ABGs.
5. **Obtain surgical hemorrhage control** — resuscitation without source control is futile. Activate trauma surgery, IR, or GI depending on source.
6. **Monitor with serial POC testing** — TEG/ROTEM if available to guide component therapy. Check ionized calcium, fibrinogen, INR, platelet count every 30-60 minutes.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Hemorrhagic shock without MTP threshold | Responds to 1-2 units pRBC, bleeding controlled |
| Coagulopathy of trauma (acute) | Coagulopathy precedes transfusion, driven by tissue injury and hypoperfusion |
| DIC | Elevated D-dimer, low fibrinogen, schistocytes, underlying sepsis or malignancy |
| Dilutional coagulopathy | Excessive crystalloid resuscitation without balanced blood products |
| Non-hemorrhagic shock | Cardiogenic, obstructive, distributive — no evidence of bleeding, different hemodynamic profiles |
| Transfusion reactions (acute) | Fever, urticaria, hypotension temporally related to transfusion, not hemorrhage |

## Workup

**Labs (draw before and during transfusion):**
- CBC — serial hemoglobin trending (single value unreliable in acute hemorrhage)
- Coagulation panel: INR, PTT, fibrinogen
- ABG/VBG with lactate — monitor acidosis, base deficit
- Ionized calcium — drops rapidly with citrated blood products; hypocalcemia causes further coagulopathy and cardiac dysfunction
- TEG/ROTEM — point-of-care viscoelastic testing guides targeted component therapy
- Type and crossmatch — send early but do not wait; use uncrossmatched blood
- BMP, LFTs — baseline organ function
- Pregnancy test (females of childbearing age) — determines Rh-negative blood requirement

**Imaging:**
- FAST exam — identifies intraperitoneal, pericardial, or thoracic hemorrhage
- CXR — hemothorax
- Pelvic XR — pelvic fracture with hemorrhage risk
- CT with contrast — identify source after initial stabilization if source unclear
- CT angiography — for vascular injury or embolization planning

## Treatment

**Damage Control Resuscitation:**
- Permissive hypotension: target SBP 80-90 mmHg (MAP 50-60) until surgical hemorrhage control. Exception: traumatic brain injury requires SBP >100.
- Minimize crystalloid. Balanced blood product resuscitation is the volume strategy.
- 1:1:1 pRBC:FFP:platelets — each MTP cooler typically contains 6 units pRBC, 6 units FFP, 1 apheresis platelet unit.

**Adjuncts:**
- TXA 1g IV over 10 minutes, then 1g IV over 8 hours (within 3 hours of injury)
- Calcium chloride 1g IV (10 mL of 10% solution via central line) or calcium gluconate 3g IV (peripheral OK) per every 4 units blood products. Target ionized Ca >1.1 mmol/L.
- Cryoprecipitate 10 units IV if fibrinogen < 150 mg/dL
- Prothrombin complex concentrate (PCC) 25-50 units/kg IV for warfarin reversal or refractory coagulopathy
- DDAVP 0.3 mcg/kg IV for uremic or platelet dysfunction

**Temperature Management:**
- Rapid infuser with in-line warmer for all blood products
- Forced-air warming blanket (Bair Hugger)
- Warm IV fluids to 39°C
- Increase room temperature
- Target core temp > 36°C

**Hemorrhage Control (parallel with resuscitation):**
- Direct pressure, tourniquet for extremity hemorrhage
- Pelvic binder for pelvic fractures
- Resuscitative thoracotomy for penetrating thoracic trauma with PEA/asystole <15 min
- REBOA for infradiaphragmatic hemorrhage (bridge to OR/IR)
- Surgical exploration/damage control surgery
- Interventional radiology embolization

## Disposition

**ICU Admission (all patients receiving MTP):**
- Ongoing monitoring of coagulation, hemodynamics, and organ function
- Serial labs every 2-4 hours until hemorrhage controlled and coagulopathy corrected
- Ventilator management — ARDS is common after massive transfusion

**Surgical/IR:**
- All patients with uncontrolled hemorrhage require emergent source control
- Damage control surgery with planned second-look laparotomy in 24-48 hours for severe abdominal trauma

**Transfusion Medicine Consultation:**
- Persistent coagulopathy despite balanced resuscitation
- Unusual antibodies complicating crossmatch
- Refractory thrombocytopenia

**Never discharge a patient requiring MTP from the ED.**

## Pitfalls

1. **Delaying MTP activation waiting for lab results.** Hemoglobin and coags lag behind clinical hemorrhage by 30-60 minutes. Activate based on clinical assessment (ABC score, shock index), not lab values.

2. **Forgetting calcium replacement.** Citrate in blood products chelates ionized calcium. Hypocalcemia causes myocardial depression, vasodilation, and worsened coagulopathy. Replace empirically: calcium chloride 1g IV per 4 units transfused.

3. **Excessive crystalloid resuscitation.** Crystalloid dilutes clotting factors and platelets, worsens hypothermia, causes abdominal compartment syndrome. Use balanced blood products as the primary volume strategy.

4. **Administering TXA beyond 3 hours post-injury.** CRASH-2 showed increased mortality with late TXA administration. The clock starts at time of injury, not ED arrival.

5. **Targeting normal blood pressure before hemorrhage control.** Permissive hypotension (SBP 80-90) reduces ongoing hemorrhage. Aggressive fluid resuscitation before source control dislodges clots and worsens bleeding. Exception: TBI requires SBP >100.

6. **Neglecting hypothermia.** Every degree below 36°C worsens enzymatic coagulation cascade function. Blood products must go through a warmer. Cold patients do not clot.

7. **Failing to obtain surgical hemorrhage control.** Resuscitation buys time but does not stop bleeding. Parallel-track surgical/IR consultation from the moment MTP is activated.

8. **Overlooking fibrinogen depletion.** Fibrinogen is the first clotting factor to reach critically low levels in massive hemorrhage. Check levels every 30-60 minutes; administer cryoprecipitate 10 units when fibrinogen < 150 mg/dL.

9. **Not monitoring ionized calcium on ABG.** Total calcium is unreliable in massive transfusion. Ionized calcium from ABG is the measurement that matters. Cardiac arrest can result from uncorrected hypocalcemia.

10. **Using Rh-positive blood in Rh-negative women of childbearing age.** Can cause Rh alloimmunization. Use O-negative pRBCs for females of childbearing potential. If O-negative supply is depleted, switch to O-positive and document for later RhoGAM administration.
