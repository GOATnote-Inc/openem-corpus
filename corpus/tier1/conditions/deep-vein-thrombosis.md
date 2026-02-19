---
id: deep-vein-thrombosis
condition: Deep Vein Thrombosis
aliases: [DVT, deep venous thrombosis, proximal DVT, distal DVT, calf vein thrombosis, iliofemoral DVT, upper extremity DVT, Paget-Schroetter syndrome, phlegmasia cerulea dolens]
icd10: [I82.40, I82.409, I82.629]
esi: 3
time_to_harm: "Hours to days (proximal DVT may embolize to PE at any time)"
mortality_if_delayed: "1-5% from PE if untreated proximal DVT; phlegmasia cerulea dolens carries 20-40% mortality"
category: hematologic
track: tier1
sources:
  - type: guideline
    ref: "Kearon C et al. Antithrombotic therapy for VTE disease: CHEST guideline and expert panel report. Chest 2016;149(2):315-352"
    pmid: "26867832"
  - type: guideline
    ref: "Ortel TL et al. American Society of Hematology 2020 guidelines for management of venous thromboembolism: treatment of deep vein thrombosis and pulmonary embolism. Blood Adv 2020;4(19):4693-4738"
    pmid: "33007077"
  - type: pubmed
    ref: "Wells PS et al. Evaluation of D-dimer in the diagnosis of suspected deep-vein thrombosis. N Engl J Med 2003;349(13):1227-1235"
    pmid: "14507948"
  - type: pubmed
    ref: "Vedantham S et al. Pharmacomechanical catheter-directed thrombolysis for deep-vein thrombosis (ATTRACT trial). N Engl J Med 2017;377(23):2240-2252"
    pmid: "29211671"
  - type: meta-analysis
    ref: "Defined Clinical Validity of Wells Score for DVT. Wells criteria for DVT is a reliable clinical tool to assess the pretest probability. J Clin Med Res 2016;8(7):526-531"
    pmid: "27298662"
last_updated: "2026-02-19"
compiled_by: agent
risk_tier: C
validation:
  automated_consistency_check: null
  dose_range_validator: null
  unit_normalization_check: null
  cross_file_consistency_check: null
  citation_presence_check: null
  duplicate_content_check: null
  outlier_detection_flag: clear
  schema_version: "2.0"
  guideline_version_reference: null
  provenance_links: []
---
# Deep Vein Thrombosis

## Recognition

**Definition:** Thrombus formation within the deep venous system, most commonly the lower extremities. DVT is the precursor to pulmonary embolism (see pulmonary-embolism.md). Untreated proximal DVT carries a 40-50% risk of PE.

### Anatomic Classification
- **Proximal DVT:** Popliteal vein or above (femoral, common femoral, iliac veins). Higher PE risk. Always requires anticoagulation.
- **Distal (calf) DVT:** Confined to calf veins (posterior tibial, peroneal, soleal, gastrocnemius). Lower PE risk (~5%). Treatment is controversial -- serial ultrasound in 5-7 days vs. anticoagulation depending on risk factors and symptom severity.
- **Iliofemoral DVT:** Proximal DVT involving iliac and/or common femoral veins. Highest risk of PE, post-thrombotic syndrome, and phlegmasia. May warrant catheter-directed therapy.
- **Upper extremity DVT:** Subclavian, axillary, or brachial veins. Causes: effort-related (Paget-Schroetter syndrome -- thoracic outlet compression), central venous catheter, pacemaker leads, malignancy. PE risk 2-9%.

### Clinical Presentation
- Unilateral leg swelling (most sensitive finding)
- Calf or thigh pain, tenderness along deep venous system
- Warmth, erythema
- Pitting edema
- Dilated superficial veins
- Homan sign (calf pain with dorsiflexion) -- poor sensitivity and specificity, not reliable
- May be asymptomatic (up to 50% of DVTs are clinically silent)

### Phlegmasia (Limb-Threatening DVT)
- **Phlegmasia alba dolens:** Massive iliofemoral DVT with painful white swollen leg. Arterial inflow preserved but venous outflow completely obstructed. Precursor to cerulea dolens.
- **Phlegmasia cerulea dolens:** Massive venous occlusion with secondary arterial compromise. Cyanotic, tense, exquisitely painful limb. Compartment pressures elevated. Pulses may be absent. Venous gangrene imminent. **Surgical emergency** -- requires emergent thrombectomy or catheter-directed thrombolysis. Fasciotomy may be needed. Mortality 20-40%.

### Wells Score for DVT

| Criteria | Points |
|---|---|
| Active cancer (treatment within 6 months or palliative) | +1 |
| Paralysis, paresis, or recent cast immobilization of lower extremity | +1 |
| Bedridden > 3 days or major surgery within 12 weeks requiring general/regional anesthesia | +1 |
| Localized tenderness along distribution of deep venous system | +1 |
| Entire leg swollen | +1 |
| Calf swelling >= 3 cm compared to asymptomatic side (measured 10 cm below tibial tuberosity) | +1 |
| Pitting edema confined to symptomatic leg | +1 |
| Collateral superficial veins (non-varicose) | +1 |
| Previously documented DVT | +1 |
| Alternative diagnosis at least as likely as DVT | -2 |

**Interpretation:**
- Score >= 2: DVT **likely** -- proceed to compression ultrasonography
- Score < 2: DVT **unlikely** -- obtain D-dimer; if negative, DVT excluded; if positive, proceed to compression ultrasonography

## Critical Actions

| Action | Target |
|---|---|
| Wells score calculation | At presentation, before any testing |
| D-dimer (if Wells < 2) | Negative D-dimer excludes DVT (NPV > 99%) |
| Compression ultrasonography | Definitive imaging; obtain urgently for Wells >= 2 |
| Anticoagulation initiation | Same day as diagnosis; do not delay for hematology consultation |
| Evaluate for PE | Any DVT patient with dyspnea, tachycardia, chest pain, or hypoxia |

1. **Apply Wells score** systematically to determine pretest probability.
2. **D-dimer for low-probability patients** (Wells < 2). Negative high-sensitivity D-dimer (< 500 mcg/L FEU) safely excludes DVT without imaging.
3. **Compression ultrasonography** for Wells >= 2 or positive D-dimer. Whole-leg ultrasound preferred (identifies both proximal and distal DVT).
4. **Start anticoagulation on the day of diagnosis.** Do not delay for specialist consultation. First dose in the ED.
5. **Screen for PE** in any DVT patient with cardiopulmonary symptoms. DVT and PE are a single disease spectrum (see pulmonary-embolism.md).
6. **Identify phlegmasia immediately.** Tense, cyanotic, exquisitely painful limb = phlegmasia cerulea dolens. Emergent surgical/interventional consultation.
7. **Check renal function before choosing anticoagulant.** CrCl < 30 mL/min contraindicates LMWH and DOACs at standard doses.

## Differential Diagnosis

| Condition | Distinguishing Features |
|---|---|
| Cellulitis | Erythema, warmth, often with skin break or wound; bilateral warmth less common; no deep venous tenderness; no calf asymmetry on measurement |
| Ruptured Baker cyst | Posterior knee pain radiating to calf; history of knee arthritis/effusion; ultrasound shows popliteal cyst with surrounding fluid |
| Superficial thrombophlebitis | Palpable cord along superficial vein; localized erythema and tenderness directly over vein; no deep calf swelling |
| Muscle strain or tear | History of exertion or trauma; focal muscle tenderness; no pitting edema; bruising may develop |
| Lymphedema | Chronic, progressive, non-pitting edema; bilateral possible; no acute pain; Stemmer sign positive |
| Chronic venous insufficiency | History of prior DVT or varicose veins; stasis dermatitis; hemosiderin deposition; bilateral; gradual onset |
| Compartment syndrome | Tense compartment, pain with passive stretch, follows trauma or ischemia-reperfusion; pulses may be present initially |
| Acute limb ischemia | Pallor, pulselessness, paralysis, poikilothermia (see acute-limb-ischemia.md); opposite of DVT presentation |
| Heart failure | Bilateral symmetric edema; elevated JVP; dyspnea; BNP elevated |
| Nephrotic syndrome | Bilateral edema; proteinuria; hypoalbuminemia |

## Workup

### Diagnostic Algorithm
1. Calculate Wells score
2. Wells < 2 (unlikely): high-sensitivity D-dimer
   - D-dimer negative (< 500 mcg/L FEU): DVT excluded, no imaging needed
   - D-dimer positive: proceed to compression ultrasound
3. Wells >= 2 (likely): compression ultrasonography
   - Positive: diagnose DVT, start anticoagulation
   - Negative with high clinical suspicion: repeat ultrasound in 5-7 days or obtain D-dimer to further risk-stratify

### Imaging
- **Compression ultrasonography (CUS):** First-line diagnostic test. Sensitivity > 95% for proximal DVT, 70-75% for isolated calf DVT. Non-compressibility of the vein is diagnostic. Whole-leg ultrasound (proximal + distal) is preferred over 2-point (femoral + popliteal only).
- **CT venography:** Performed simultaneously with CTPA for PE. Adds radiation and contrast exposure; reserve for equivocal ultrasound or suspected iliac/IVC thrombosis.
- **MR venography:** Alternative for suspected iliac vein or IVC thrombosis. No radiation. Limited availability.
- **Contrast venography:** Historical gold standard. Rarely performed. Reserved for equivocal non-invasive studies or pre-procedural planning for catheter-directed therapy.

### Laboratory
- **D-dimer (high-sensitivity assay):** Only useful in the low-probability (Wells < 2) population. Age-adjusted cutoff for patients >= 50 years: age x 10 mcg/L FEU. Elevated in infection, malignancy, pregnancy, postoperative states, trauma -- low specificity.
- **CBC:** Baseline platelet count (needed for anticoagulation monitoring, HIT risk).
- **BMP/CMP:** Creatinine and eGFR to guide anticoagulant selection (renal dosing).
- **PT/INR, aPTT:** Baseline coagulation studies before anticoagulation.
- **Hepatic function panel:** If DOAC planned (hepatic metabolism).
- **Pregnancy test:** In women of childbearing age. DOACs and warfarin are contraindicated in pregnancy.
- **Thrombophilia workup:** NOT indicated acutely. Does not change ED management. Defer to outpatient hematology for unprovoked DVT in young patients.

## Treatment

### Anticoagulation -- First-Line Therapy

Anticoagulation is the cornerstone of DVT treatment. Start on the day of diagnosis.

**Direct oral anticoagulants (DOACs) -- preferred for most patients with acute DVT:**

- **Rivaroxaban:** 15 mg PO BID x 21 days, then 20 mg PO daily. Take with food. No parenteral lead-in required.
- **Apixaban:** 10 mg PO BID x 7 days, then 5 mg PO BID. No parenteral lead-in required.

DOACs are preferred over warfarin for non-cancer DVT (fewer drug interactions, no INR monitoring, lower bleeding risk). Contraindicated in pregnancy, severe renal impairment (CrCl < 25-30 mL/min depending on agent), active liver disease, and patients with antiphospholipid syndrome.

**Low-molecular-weight heparin (LMWH):**

- **Enoxaparin:** 1 mg/kg SC q12h (or 1.5 mg/kg SC daily for select patients)
- Use as bridge to warfarin (overlap for minimum 5 days AND until INR >= 2.0 for >= 24 hours), OR
- Use as definitive therapy in cancer-associated DVT and pregnancy
- Avoid if CrCl < 30 mL/min (use UFH instead)
- Monitor anti-Xa levels in obesity (> 150 kg), renal impairment, pregnancy

**Unfractionated heparin (UFH):**

- Bolus: 80 units/kg IV (max 10,000 units), then 18 units/kg/hr infusion
- Check aPTT at 6 hours, target 60-80 seconds (1.5-2.5x control)
- Reserve for: CrCl < 30 mL/min, patients who may need urgent surgery/procedures, phlegmasia requiring thrombolysis
- Cross-file consistent with dosing in pulmonary-embolism.md

**Fondaparinux (alternative):**

- < 50 kg: 5 mg SC daily
- 50-100 kg: 7.5 mg SC daily
- \> 100 kg: 10 mg SC daily
- Contraindicated if CrCl < 30 mL/min

**Warfarin (if DOACs contraindicated or unavailable):**

- Start 5 mg PO daily (lower dose 2-3 mg in elderly, liver disease, drug interactions)
- Overlap with parenteral anticoagulant (LMWH or UFH) for minimum 5 days AND until INR 2.0-3.0 for >= 24 hours
- Target INR 2.0-3.0

### Duration of Anticoagulation (initiated in ED, determined by follow-up)
- **Provoked DVT** (surgery, immobilization, estrogen): 3 months
- **Unprovoked DVT:** 3 months minimum, then reassess for extended therapy (indefinite in many patients, particularly proximal DVT)
- **Cancer-associated DVT:** Anticoagulation as long as cancer is active. LMWH or edoxaban/rivaroxaban.
- **Recurrent unprovoked DVT:** Indefinite anticoagulation

### Distal (Calf) DVT -- Controversial Management
- If low bleeding risk and symptomatic: anticoagulate (same regimen, 3 months)
- If high bleeding risk or minimally symptomatic: serial compression ultrasound in 5-7 days; anticoagulate only if proximal propagation

### Massive Iliofemoral DVT -- Catheter-Directed Therapy
- **Indications:** Acute iliofemoral DVT with severe symptoms, limb-threatening ischemia (phlegmasia), or young patients with low bleeding risk and high concern for post-thrombotic syndrome
- **Catheter-directed thrombolysis (CDT):** Alteplase 0.5-1 mg/hr infused directly into thrombus via catheter, typically over 12-24 hours
- **Pharmacomechanical thrombectomy:** Combination of catheter-directed lysis and mechanical clot disruption/aspiration
- **ATTRACT trial caveat:** Routine CDT for proximal DVT did not reduce post-thrombotic syndrome at 2 years and increased major bleeding. CDT should be reserved for severe, limb-threatening cases (phlegmasia, extensive iliofemoral clot with functional compromise), not used routinely.

### Phlegmasia Cerulea Dolens -- Surgical Emergency
- Emergent vascular surgery or interventional radiology consultation
- Systemic anticoagulation with UFH (bolus + infusion as above)
- Catheter-directed thrombolysis or surgical thrombectomy
- Fasciotomy if compartment syndrome develops
- IVC filter placement if PE risk during intervention
- Amputation if venous gangrene established

### IVC Filter
- **Indication:** Acute proximal DVT or PE with absolute contraindication to anticoagulation (active hemorrhage, recent neurosurgery, severe thrombocytopenia)
- NOT a substitute for anticoagulation
- Retrievable filter preferred; plan for retrieval once anticoagulation becomes feasible
- Does not treat the DVT itself -- anticoagulation still required once safe
- Complications: IVC thrombosis, filter migration, filter fracture, recurrent DVT

### Supportive Measures
- Elevation of affected extremity for comfort
- Early ambulation (does not increase PE risk; prolonged bedrest worsens outcomes)
- Compression stockings: no longer routinely recommended for prevention of post-thrombotic syndrome (SOX trial negative)
- Adequate analgesia: NSAIDs if no contraindication; acetaminophen; avoid IM injections if anticoagulated

## Disposition

**Discharge from ED (majority of DVT patients):**
- Hemodynamically stable, uncomplicated proximal or distal DVT
- Able to obtain and afford anticoagulation (DOAC preferred for outpatient management)
- No signs of PE
- No phlegmasia or limb-threatening features
- Reliable follow-up within 3-7 days (primary care or anticoagulation clinic)
- Adequate pain control
- Patient education on anticoagulation compliance, signs of PE, and bleeding precautions

**Admit to hospital:**
- Massive iliofemoral DVT requiring catheter-directed therapy
- Phlegmasia alba dolens or cerulea dolens
- Concurrent PE (see pulmonary-embolism.md for PE disposition)
- High bleeding risk requiring monitored anticoagulation initiation
- Severe renal impairment requiring UFH with aPTT monitoring
- Inability to obtain outpatient anticoagulation
- Significant comorbidities complicating management (active cancer with thrombocytopenia, recent surgery)
- Social factors precluding safe outpatient management

**Transfer:**
- Phlegmasia cerulea dolens if vascular surgery or interventional radiology not available on site. Start UFH before transfer.

## Pitfalls

1. **Ordering D-dimer in high-probability patients (Wells >= 2).** D-dimer has a high false-positive rate and adds no value when pretest probability is high. A negative D-dimer in a high-probability patient cannot reliably exclude DVT. Proceed directly to compression ultrasonography.

2. **Diagnosing bilateral cellulitis instead of DVT with bilateral edema.** True bilateral cellulitis is rare. Bilateral lower extremity edema with erythema warrants consideration of bilateral DVT (seen in IVC thrombosis, malignancy), heart failure, or nephrotic syndrome. Bilateral cellulitis is a commonly overcalled diagnosis that delays DVT recognition.

3. **Failing to evaluate for concurrent PE in DVT patients.** Up to 50% of patients with proximal DVT have concurrent (often asymptomatic) PE on imaging. Any DVT patient with new dyspnea, tachycardia, chest pain, hypoxia, or syncope requires PE evaluation per the pulmonary-embolism.md diagnostic pathway.

4. **Delaying anticoagulation for specialist consultation or additional testing.** DVT anticoagulation should begin on the day of diagnosis, in the ED, before discharge. Waiting for hematology consultation, thrombophilia testing, or next-day follow-up leaves the patient unprotected against PE during the highest-risk window.

5. **Missing upper extremity DVT.** Arm swelling, pain, or discoloration in a patient with a central venous catheter, PICC line, pacemaker, or history of repetitive upper extremity exertion (Paget-Schroetter syndrome) should prompt dedicated upper extremity ultrasound. Upper extremity DVT carries a 2-9% PE risk and requires anticoagulation.

6. **Sending a patient with phlegmasia home as "routine DVT."** A tense, cyanotic, exquisitely painful limb is not uncomplicated DVT. Phlegmasia cerulea dolens is a surgical emergency with 20-40% mortality. Absent pulses in a swollen leg should trigger immediate vascular surgery consultation, not outpatient anticoagulation.

7. **Using DOACs in contraindicated populations.** Rivaroxaban and apixaban are contraindicated in pregnancy (teratogenic), severe renal impairment (CrCl < 25-30 mL/min), active liver disease, and antiphospholipid syndrome (increased thrombosis risk with DOACs per TRAPS trial). These patients require LMWH or UFH.

8. **Discharging without confirmed follow-up or medication access.** DVT patients require anticoagulation follow-up within 3-7 days. Prescribing a DOAC without confirming the patient can afford and obtain it (prior authorization delays, cost) results in untreated DVT. Provide bridge anticoagulation (e.g., enoxaparin) if DOAC access is uncertain.

9. **Anchoring on negative ultrasound when clinical suspicion remains high.** Compression ultrasound sensitivity for isolated calf DVT is only 70-75%. A single negative ultrasound in a patient with Wells >= 2 and positive D-dimer warrants repeat imaging in 5-7 days. Early calf DVT can propagate proximally within days.
