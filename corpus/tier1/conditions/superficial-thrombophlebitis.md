---
id: superficial-thrombophlebitis
condition: Superficial Thrombophlebitis
aliases: [phlebitis, superficial venous thrombosis, SVT (venous)]
icd10: [I80.00, I80.01, I80.02, I80.03]
esi: 4
time_to_harm: "N/A — typically benign and self-limited; see escalation_triggers for DVT extension and malignancy-associated risk"
category: cardiovascular
track: tier1
disposition_default: outpatient
escalation_triggers:
  - "DVT cannot be excluded without duplex ultrasound — order duplex before discharge; 15-25% of superficial thrombophlebitis cases have concurrent DVT"
  - "Thrombus within 3 cm of saphenofemoral junction (SFJ) on duplex — high risk of propagation into femoral vein; anticoagulation and vascular/hematology consultation required"
  - "Bilateral or migratory phlebitis without IV catheter or trauma explanation — Trousseau syndrome (malignancy-associated hypercoagulability); cancer workup mandatory"
  - "Systemic symptoms: fever >38.5°C, tachycardia, hypotension — septic thrombophlebitis; IV antibiotics and vascular surgery consultation"
  - "Upper extremity phlebitis near an indwelling central or peripheral catheter with fever — catheter-related septic thrombophlebitis; remove catheter, blood cultures, IV antibiotics"
  - "Respiratory symptoms: dyspnea, pleuritic pain, tachycardia, hypoxia — pulmonary embolism; CT pulmonary angiography"
  - "Rapid progression along vein despite treatment — septic phlebitis or hypercoagulable state; vascular surgery and hematology referral"
confusion_pairs:
  - condition: deep-vein-thrombosis
    differentiators:
      - "Superficial thrombophlebitis: palpable, tender, cord-like thrombosed superficial vein; erythema overlying the vein; no significant limb swelling beyond local site; varicosities often involved"
      - "DVT: involves deep venous system (femoral, popliteal, tibial veins); limb swelling >3 cm asymmetry; Homan sign (unreliable); positive Wells DVT score (immobility, surgery, malignancy, prior DVT history); no palpable superficial cord"
      - "Superficial thrombophlebitis: duplex shows thrombus confined to superficial (saphenous) system, compressible deep veins; limited perivenous edema"
      - "DVT: duplex shows non-compressible deep vein with intraluminal thrombus; venous outflow obstruction; limb edema"
      - "Critical rule: duplex ultrasound is mandatory to exclude DVT in any lower extremity thrombophlebitis — clinical examination alone cannot reliably distinguish superficial from deep venous thrombosis"
  - condition: pulmonary-embolism
    differentiators:
      - "Superficial thrombophlebitis: localized limb symptoms; hemodynamically stable; SpO2 normal; no dyspnea or pleuritic chest pain"
      - "PE: dyspnea, pleuritic chest pain, tachycardia, oxygen desaturation; D-dimer elevated; CT pulmonary angiography confirms; risk of PE from isolated superficial thrombophlebitis (without DVT) is low but not zero, particularly with SFJ proximity"
      - "Superficial thrombophlebitis: if located remote from SFJ and no concurrent DVT on duplex, PE risk is low"
      - "PE: any respiratory symptoms in a patient with phlebitis require CT-PA; D-dimer will be elevated in active phlebitis and is not useful to screen for PE in this context"
      - "Critical rule: elevated D-dimer is expected in superficial thrombophlebitis — use CT-PA directly when PE is suspected, not D-dimer"
sources:
  - type: guideline
    ref: "Di Nisio M, Wichers IM, Middeldorp S. Treatment for superficial thrombophlebitis of the leg. Cochrane Database Syst Rev. 2018;2(2):CD004982."
    pmid: "29478266"
  - type: pubmed
    ref: "Decousus H, Prandoni P, Mismetti P, et al. Fondaparinux for the treatment of superficial-vein thrombosis in the legs. N Engl J Med. 2010;363(13):1222-1232."
    pmid: "20860504"
  - type: pubmed
    ref: "Frappé P, Buchmuller-Cordier A, Bertoletti L, et al. Annual diagnosis rate of superficial vein thrombosis of the lower limbs: the STEPH community-based study. J Thromb Haemost. 2014;12(6):831-838."
    pmid: "24674619"
  - type: pubmed
    ref: "Leon L, Giannoukas AD, Dodd D, Chan P, Labropoulos N. Clinical significance of superficial vein thrombosis. Eur J Vasc Endovasc Surg. 2005;29(1):10-17."
    pmid: "15570265"
  - type: guideline
    ref: "Kearon C, Akl EA, Ornelas J, et al. Antithrombotic therapy for VTE disease: CHEST guideline and expert panel report. Chest. 2016;149(2):315-352."
    pmid: "26867832"
  - type: pubmed
    ref: "Bauersachs RM. Treatment of deep vein thrombosis, superficial thrombophlebitis, and pulmonary embolism: a practical guide. Dtsch Arztebl Int. 2016;113(48):808-814."
    pmid: "27974097"
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
  guideline_version_reference: "CHEST 2016 guidelines; Cochrane Review 2018; CALISTO trial (fondaparinux) 2010"
  provenance_links: []
---

## Recognition

Superficial thrombophlebitis (ST) is thrombosis and inflammation of a superficial vein, most commonly the great saphenous vein (GSV) or small saphenous vein (SSV) of the lower extremity. It affects approximately 1 in 200 adults annually. While traditionally considered benign, concurrent DVT is found in 15-25% of cases and extension to the deep venous system occurs in up to 10% — making duplex ultrasound mandatory rather than optional.

Two main etiologic contexts:
- **Varicose vein-associated ST**: most common; thrombus in varicosities; localized to a specific varicose segment; associated with venous stasis
- **Non-varicosity ST**: in non-varicose veins — higher association with hypercoagulable states, malignancy (Trousseau syndrome), or IV catheter-related injury

### Typical Clinical Presentation
- Palpable, tender, cord-like induration along the course of a superficial vein
- Overlying erythema, warmth, and localized edema at the vein site
- Affects varicosities in the lower extremity (GSV distribution: medial thigh and calf; SSV distribution: posterior calf)
- Migratory or bilateral presentation: strongly associated with Trousseau syndrome (occult malignancy)
- IV catheter-related: upper extremity; at or distal to catheter site
- Afebrile or low-grade temperature; high fever suggests septic thrombophlebitis

### Risk Factors
- Varicose veins (primary risk factor)
- Pregnancy and postpartum state
- Oral contraceptives, hormone replacement therapy
- Recent IV catheter placement
- Prolonged standing (occupational)
- Obesity
- Prior DVT or superficial thrombophlebitis
- Malignancy (unexplained migratory ST = Trousseau sign of malignancy)
- Hypercoagulable states (antiphospholipid antibody syndrome, factor V Leiden, protein C/S deficiency)

### Trousseau Syndrome (Migratory Thrombophlebitis)
- Bilateral, migratory phlebitis affecting different venous segments over time
- Not explained by varicosities, IV catheter, or trauma
- Highly associated with mucin-secreting adenocarcinomas (pancreatic, gastric, lung, colorectal, ovarian)
- Workup: age-appropriate cancer screening, CT chest/abdomen/pelvis, tumor markers

## Critical Actions

1. Order duplex ultrasound of the affected limb before discharge — clinical exam cannot reliably exclude DVT. If DVT is found, manage as DVT.
2. Measure the distance between the thrombus tip and the saphenofemoral junction (SFJ) on duplex. Thrombus within 3 cm of the SFJ carries high extension risk and typically warrants anticoagulation (fondaparinux 2.5 mg SC daily × 45 days per CALISTO trial data).
3. Assess for systemic signs: fever >38.5°C, rigors, rapid pulse, or bacteremia signs — septic thrombophlebitis requires IV antibiotics and vascular surgery consultation (removal of source catheter).
4. Assess for migratory or bilateral pattern without catheter or trauma explanation — Trousseau syndrome screening.
5. Assess for respiratory symptoms: dyspnea, pleuritic chest pain, tachycardia, or O2 desaturation — CT-PA directly (D-dimer is not useful for PE exclusion in active phlebitis).

## When NOT to Escalate

Superficial thrombophlebitis is appropriate for outpatient management when ALL of the following are met:
- Duplex ultrasound confirms thrombus confined to superficial venous system (no DVT)
- Thrombus >3 cm from saphenofemoral junction on duplex
- No fever or systemic signs of infection
- Hemodynamically stable
- No respiratory symptoms (no dyspnea, no pleuritic chest pain, SpO2 ≥95%)
- Not associated with indwelling central venous catheter
- Not bilateral or migratory without explanation
- Unilateral, localized, and varicosity-associated

NSAIDs, leg elevation, compression, and outpatient follow-up are appropriate for confirmed isolated superficial thrombophlebitis remote from the SFJ with no concurrent DVT.

## Differential Diagnosis

| Condition | Key Features | Distinguishing from Superficial Thrombophlebitis |
|-----------|-------------|--------------------------------------------------|
| **DVT** | Deep vein non-compressible on duplex; limb swelling >3 cm asymmetry; risk factors (immobility, surgery, malignancy, prior DVT); Wells score positive | ST: superficial vein palpable cord; duplex shows compressible deep veins; limited edema |
| **Cellulitis** | Spreading poorly-demarcated erythema; fever; no palpable cord; tenderness without cord | ST: palpable linear cord along vein; erythema follows venous distribution; duplex confirms thrombus |
| **Pulmonary embolism** | Dyspnea, pleuritic chest pain, tachycardia, hypoxia; CT-PA confirms | ST: no respiratory involvement; SpO2 normal; hemodynamically stable; PE risk is low in isolated ST remote from SFJ without DVT |
| **Lymphangitis** | Red streak along lymphatics; high fever; regional lymphadenopathy; follows lymphatic not venous distribution | ST: cord along venous anatomy; fever absent or low-grade in uncomplicated ST |
| **Superficial hematoma / bruise** | No palpable cord; ecchymosis without induration; trauma history | ST: palpable cord; follows vein anatomy; duplex confirms thrombus |
| **Erythema nodosum** | Tender nodules on anterior shins; bilateral; elevated ESR; associated with sarcoidosis, IBD, streptococcal infection, drugs | ST: linear cord along vein; follows venous distribution; duplex shows intraluminal thrombus |
| **Lipoma or benign soft tissue mass** | Non-tender; non-linear; does not follow vein anatomy; no erythema | ST: linear, tender, follows vein; erythema present |

## Workup

### Mandatory
- **Duplex ultrasound of affected limb**: required before discharge to exclude concurrent DVT and measure distance from SFJ. Cannot be omitted based on clinical exam alone.

### When to Order Additional Labs
- **CBC, WBC**: if fever present or septic phlebitis suspected
- **Blood cultures (×2 sets)**: fever >38.5°C with phlebitis — septic thrombophlebitis
- **D-dimer**: not useful for PE exclusion in active phlebitis (will be elevated); not recommended
- **Hypercoagulable panel**: first-episode ST in a young patient without varicosities, bilateral or migratory ST, or recurrent ST — order outpatient: protein C, protein S, antithrombin III, factor V Leiden mutation, prothrombin G20210A, antiphospholipid antibodies (anticardiolipin IgG/IgM, anti-β2-glycoprotein I, lupus anticoagulant). Do NOT order during acute phase or while on anticoagulation — false results.
- **CT chest/abdomen/pelvis with contrast**: bilateral or migratory phlebitis in a patient >40 years without explanatory risk factors — malignancy screening (Trousseau syndrome)

### Imaging
- **CT pulmonary angiography**: if PE is clinically suspected (do not use D-dimer as a screening step in active phlebitis)

## Treatment

### NSAIDs (First-Line for Isolated Superficial Thrombophlebitis)
- **Diclofenac 75 mg PO twice daily** with food (adults): evidence-based for superficial thrombophlebitis; reduces pain, erythema, and thrombus extension; 10-14 days duration
- **Ibuprofen 400-600 mg PO three times daily** with food (adults; max 2400 mg/day): alternative NSAID; 10-14 days
- **Topical diclofenac 1% gel**: applied to affected area three to four times daily; reduces local symptoms with minimal systemic absorption; appropriate adjunct or primary therapy in patients with contraindications to oral NSAIDs

### Anticoagulation (Specific Indications)
- **Fondaparinux 2.5 mg SC once daily × 45 days**: the highest-level evidence (CALISTO trial — N=3,002) for isolated superficial thrombophlebitis of the GSV ≥5 cm in length; reduces symptomatic DVT and PE by 85% and recurrence by 73% vs. placebo. Preferred over LMWH or aspirin for SVT meeting CALISTO criteria.
  - Indicated for: SVT ≥5 cm length, no concurrent DVT, remote from SFJ (>3 cm), otherwise well patient without significant renal impairment (CrCl <20 mL/min is contraindication)
- **Thrombus within 3 cm of SFJ**: therapeutic-dose anticoagulation (enoxaparin 1 mg/kg SC twice daily or rivaroxaban 15 mg PO twice daily × 3 weeks then 20 mg PO daily) and vascular surgery or hematology consultation for management of SFJ extension risk
- **Aspirin**: not recommended as primary anticoagulant for SVT — insufficient evidence; use NSAIDs or fondaparinux instead

### Compression
- Graduated compression stockings (20-30 mmHg): reduces pain and edema; promotes venous return; appropriate for all lower extremity SVT
- Elevate affected limb when at rest

### Septic Thrombophlebitis (IV Catheter-Related)
- Remove the IV catheter immediately
- **Vancomycin 25-30 mg/kg IV every 8-12 hours** (target trough 15-20 mg/L or AUC/MIC-based dosing) — empiric coverage for Staphylococcus aureus (MRSA and MSSA), the predominant pathogen
- Blood cultures × 2 sets before antibiotics; catheter tip culture
- Vascular surgery consultation if septic thrombophlebitis does not respond to antibiotics within 48-72 hours (surgical excision of infected vein segment)

### Local Measures
- Warm compresses to the affected vein segment: reduces discomfort; supports local resolution
- Activity: encourage ambulation — immobility worsens venous stasis

## Disposition

### Discharge (Standard)
- Isolated superficial thrombophlebitis confirmed by duplex (no DVT), thrombus >3 cm from SFJ, afebrile, hemodynamically stable, no respiratory symptoms:
  - Prescribe fondaparinux 2.5 mg SC daily × 45 days (for SVT ≥5 cm length, teach SC injection technique before discharge) OR NSAIDs for shorter, milder presentations
  - Prescribe/recommend compression stocking
  - Arrange vascular surgery or PCP follow-up in 1-2 weeks with repeat duplex to confirm non-extension
  - Provide return precautions

### Urgent Vascular Surgery or Hematology Referral
- Thrombus within 3 cm of SFJ — extension into femoral vein is a vascular emergency
- Bilateral or migratory phlebitis — Trousseau workup and hematology evaluation

### Admit / Escalate
- Septic thrombophlebitis: IV antibiotics, vascular surgery
- Concurrent DVT: manage as DVT per CHEST guidelines
- PE identified: anticoagulation and admission

### Return Precautions
- Shortness of breath, chest pain, or coughing blood
- Worsening swelling of the entire leg (not just local)
- Fever >38.5°C
- Red streak spreading up the leg rapidly
- Pain not controlled with NSAIDs

### Follow-up
- Duplex ultrasound repeat in 1-2 weeks: confirm thrombus regression, not extension toward SFJ
- PCP or vascular surgery: anticoagulation duration, compression stocking prescription, varicosity treatment planning
- If Trousseau suspected: oncology and hematology referral

## Pitfalls

1. **Not ordering duplex ultrasound because the thrombus appears "obviously superficial."** Concurrent DVT is found in 15-25% of superficial thrombophlebitis cases, and extension into the femoral vein via the saphenofemoral junction occurs in an additional 10%. Clinical examination cannot reliably distinguish superficial from deep venous involvement. Duplex ultrasound is mandatory before discharge for all lower extremity thrombophlebitis — this is a zero-tolerance error.

2. **Missing Trousseau syndrome in a patient with bilateral or migratory phlebitis.** Migratory thrombophlebitis was first described as a paraneoplastic phenomenon. Bilateral phlebitis or phlebitis in multiple venous segments without varicosities, IV catheter, or identifiable hypercoagulable state is Trousseau syndrome until proven otherwise. The most common associated malignancies are pancreatic, gastric, lung, and ovarian adenocarcinomas. Order CT chest/abdomen/pelvis and age-appropriate cancer screening before attributing recurrent migratory phlebitis to "idiopathic" causes.

3. **Prescribing a 5-7 day NSAID course and discharging without anticoagulation for saphenous thrombophlebitis ≥5 cm.** The CALISTO trial (N=3,002, randomized controlled) demonstrated that fondaparinux 2.5 mg SC daily × 45 days significantly reduces symptomatic DVT/PE and clinical recurrence in isolated saphenous SVT ≥5 cm. Short-course NSAIDs alone do not prevent thrombus extension. For SVT meeting CALISTO criteria, fondaparinux × 45 days is the evidence-based treatment — prescribe it at discharge with injection teaching.

4. **Using D-dimer to screen for PE in a patient with active thrombophlebitis.** D-dimer is a fibrin degradation product — it is elevated in all active thromboembolic states, including superficial thrombophlebitis. A negative D-dimer is not achievable in a patient with active phlebitis, making it useless as a PE exclusion tool in this context. If PE is clinically suspected (tachycardia, dyspnea, pleuritic chest pain, hypoxia), proceed directly to CT pulmonary angiography.

5. **Failing to remove the IV catheter in catheter-related septic thrombophlebitis.** Catheter-related septic thrombophlebitis is a source of bacteremia and endovascular infection that persists until the source is removed. Systemic antibiotics without catheter removal result in prolonged bacteremia and complications (septic emboli, endocarditis). The catheter must be removed immediately; IV access should be re-established at a different site.
