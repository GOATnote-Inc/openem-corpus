---
id: knee-osteoarthritis
condition: Knee Osteoarthritis
aliases: [knee OA, degenerative joint disease knee, DJD knee, gonarthrosis]
icd10: [M17.0, M17.10, M17.11, M17.12, M17.30, M17.31, M17.32, M17.9]
esi: 4
time_to_harm: "N/A — chronic degenerative condition; see escalation_triggers for emergency differential"
category: musculoskeletal
track: tier1
disposition_default: outpatient
escalation_triggers:
  - "Acute joint effusion with fever — septic arthritis until proven otherwise (arthrocentesis required)"
  - "Acute monoarthritis with warmth and erythema in patient with history of gout or pseudogout (crystal arthropathy flare may mimic septic joint)"
  - "Knee trauma with inability to bear weight — Ottowa Knee Rules positive: age >55, isolated fibular head tenderness, isolated patellar tenderness, inability to flex to 90°, inability to bear weight x 4 steps"
  - "Locked knee with inability to extend (acute meniscal tear with bucket-handle fragment)"
  - "Vascular compromise or neurovascular deficit in affected limb"
  - "Acute neurovascular emergency: popliteal (Baker) cyst rupture with severe calf swelling and tenderness (DVT must be excluded)"
confusion_pairs:
  - condition: septic-arthritis
    differentiators:
      - "OA: chronic pain pattern, no fever, no erythema, no warmth beyond mild; joint fluid non-inflammatory"
      - "Septic arthritis: acute onset, fever, marked warmth and erythema, WBC >50,000 cells/µL in synovial fluid (>90% PMNs), ESR/CRP elevated"
      - "OA flare: may have mild warmth from crystal deposition or mechanical inflammation — low-grade, no systemic signs"
      - "Septic arthritis: never discharge without arthrocentesis if fever + acute joint effusion"
sources:
  - type: guideline
    ref: "Kolasinski SL, Neogi T, Hochberg MC, et al. 2019 American College of Rheumatology/Arthritis Foundation Guideline for the Management of Osteoarthritis of the Hand, Hip, and Knee. Arthritis Care Res (Hoboken). 2020;72(2):149-162."
    pmid: "31908163"
  - type: guideline
    ref: "Jevsevar DS, Brown GA, Jones DL, et al. The American Academy of Orthopaedic Surgeons evidence-based guideline on: treatment of osteoarthritis of the knee, 2nd edition. J Bone Joint Surg Am. 2013;95(20):1885-1886."
    pmid: "24065659"
  - type: pubmed
    ref: "Fransen M, McConnell S, Harmer AR, et al. Exercise for osteoarthritis of the knee: a Cochrane systematic review. Br J Sports Med. 2015;49(24):1554-1557."
    pmid: "26405113"
  - type: pubmed
    ref: "Bannuru RR, Osani MC, Vaysbrot EE, et al. OARSI guidelines for the non-surgical management of knee, hip, and polyarticular osteoarthritis. Osteoarthritis Cartilage. 2019;27(11):1578-1589."
    pmid: "31278997"
  - type: review
    ref: "Abdel MP, Roth PB, Jennings MT, et al. Outpatient management of knee osteoarthritis. Mayo Clin Proc. 2017;92(4):627-637."
    pmid: "28385087"
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
  guideline_version_reference: "ACR/AF 2019 Guideline (current)"
  provenance_links: []
---

## Recognition

Knee OA is the most common joint disorder worldwide, affecting approximately 250 million people. Prevalence increases sharply after age 45; radiographic OA present in >50% of adults >65 years. OA presents as a chronic, progressive condition — not an emergency. The emergency concern in knee pain is identifying the conditions that require urgent intervention (septic arthritis, fracture, DVT).

### Clinical Presentation
- Chronic knee pain (typically >3 months), worsening with activity and relieved by rest
- Morning stiffness lasting <30 minutes (distinguish from RA: >60 minutes)
- Pain with stairs, prolonged standing, squatting, or rising from seated position
- Gelling phenomenon: stiffness after brief periods of inactivity
- Joint crepitus on range of motion
- Bony enlargement (osteophytes) palpable at joint margins
- Reduced range of motion, especially terminal extension and flexion
- Mild joint effusion (cool, non-inflammatory) in flares
- Varus or valgus deformity in advanced disease

### Physical Examination Findings
- Bony joint line tenderness (medial > lateral)
- Crepitus on passive range of motion
- Mild-to-moderate effusion (ballottement, bulge sign): if present, fluid is viscous and straw-colored on aspiration, WBC <2,000/µL
- No warmth or erythema (distinguishing from inflammatory/infectious arthritis)
- Quadriceps muscle wasting common in chronic disease
- Antalgic gait

### Radiographic Classification (Kellgren-Lawrence)
- Grade 0: Normal
- Grade 1: Doubtful narrowing, possible osteophytes
- Grade 2: Definite osteophytes, possible joint space narrowing
- Grade 3: Moderate osteophytes, definite joint space narrowing, subchondral sclerosis
- Grade 4: Large osteophytes, marked narrowing, severe sclerosis, possible deformity

Note: Radiographic severity correlates poorly with symptom severity. Do not escalate management based on X-ray grade alone without clinical correlation.

## Critical Actions

Outpatient management — no emergency interventions required for uncomplicated knee OA.

1. Rule out emergency diagnoses: fever + acute effusion = arthrocentesis before discharge; trauma + inability to bear weight = Ottawa Knee Rules + X-ray.
2. Confirm the diagnosis is OA flare (not septic arthritis, crystal arthropathy, or acute internal derangement) before proceeding with outpatient management.
3. Provide analgesia: topical NSAIDs as first-line (lower systemic risk); oral NSAIDs for moderate-severe pain if no contraindications.
4. Prescribe exercise: aerobic exercise and/or strength training — the highest-quality evidence for sustained pain relief (NNT similar to NSAIDs, without the side effects).
5. Address modifiable risk factors: weight loss counseling (loss of 5-10% body weight reduces knee pain 30-50% in obese patients).
6. Arrange outpatient follow-up with PCP or orthopedics for ongoing management and elective surgical planning.

## When NOT to Escalate

Knee OA is appropriate for outpatient management when ALL of the following are met:
- Chronic pain pattern (>3 months, not acute-onset with fever)
- No fever or systemic signs of infection
- Joint is not warm to touch with marked erythema
- No joint effusion, OR effusion is mild and chronic (not acutely expanding)
- No trauma history with inability to bear weight
- Patient can ambulate (even with pain)
- No neurovascular compromise distally

Emergency care is NOT required for: chronic knee OA pain, OA flare without fever or acute effusion, joint stiffness, or patient requesting surgical evaluation. These are outpatient and elective issues.

### Surgical Timing and Patient Autonomy
Total knee arthroplasty (TKA) is an elective procedure. Timing is driven by patient-reported quality-of-life impairment and failure of conservative management — NOT by imaging grade or provider judgment. Patients have the right to decline or delay surgery indefinitely. Conservative management (exercise, weight loss, NSAIDs, intra-articular injections) is appropriate for patients who are not surgical candidates or who choose not to pursue surgery.

## Differential Diagnosis

| Condition | Key Features | Distinguishing from OA |
|-----------|-------------|------------------------|
| **Septic arthritis** | Acute onset, fever, marked warmth and erythema, effusion with WBC >50,000/µL (>90% PMNs), elevated ESR/CRP | OA: no fever, no erythema, effusion mild and non-inflammatory; arthrocentesis distinguishes definitively |
| **Gout / crystal arthropathy** | Acute monoarticular flare; urate or calcium pyrophosphate crystals on joint fluid; may be indistinguishable clinically from septic joint | Crystal seen on polarized microscopy; uric acid elevated in gout; can coexist with infection |
| **Rheumatoid arthritis** | Bilateral, symmetric, small joint involvement typical; morning stiffness >60 minutes; RF/anti-CCP positive; systemic features | OA: unilateral or bilateral large joints, morning stiffness <30 minutes, seronegative |
| **Meniscal tear** | Younger patient, usually traumatic; medial or lateral joint line tenderness; McMurray or Thessaly positive; MRI confirms | OA: bony joint line tenderness, not cartilaginous; MRI differentiates |
| **Patellofemoral pain syndrome** | Anterior knee pain, worse with stairs, squatting, prolonged sitting; peripatellar tenderness; no joint space narrowing | Age-related OA less common in isolated patellofemoral distribution in young patients |
| **Popliteal (Baker) cyst rupture** | Sudden calf pain, swelling, tenderness — can mimic DVT | DVT must be excluded urgently with ultrasound; Baker cyst history, knee OA as predisposing factor |
| **DVT** | Calf pain, swelling, erythema without joint tenderness; Wells score; d-dimer + ultrasound | DVT: no joint-line tenderness, no effusion, calf > knee involvement; Wells criteria guide evaluation |
| **Tibial plateau fracture** | Trauma history; pain with weight-bearing; X-ray or CT confirms | OA: chronic; fractures usually acute onset post-trauma |

## Workup

### For Suspected OA Flare (No Fever, No Trauma)
- **X-ray knee (weight-bearing AP, lateral, and Merchant views)**: appropriate at initial evaluation; not required at every visit. Findings: joint space narrowing, osteophytes, subchondral sclerosis, cysts
- **No labs required** for uncomplicated OA
- MRI is not indicated for typical OA — reserve for suspected meniscal/ligamentous pathology or atypical presentation

### For Acute Effusion or Diagnostic Uncertainty
- **Arthrocentesis** (joint aspiration): mandatory if fever + acute effusion. Send fluid for: cell count with differential, Gram stain, culture, crystals (polarized light microscopy)
  - OA fluid: WBC <2,000/µL, clear/yellow, viscous
  - Inflammatory (crystal/RA): WBC 2,000-50,000/µL
  - Septic: WBC >50,000/µL (often >100,000), turbid, organisms on Gram stain
- **CBC, ESR, CRP**: if systemic infection or inflammatory arthritis suspected
- **Serum uric acid**: not diagnostic for acute gout (can be normal during flare); useful for baseline in suspected gout

### Ottawa Knee Rules — X-ray Required If
- Age >55 years with acute knee injury, OR
- Isolated fibular head tenderness, OR
- Isolated patellar tenderness with no other bony tenderness, OR
- Inability to flex knee to 90°, OR
- Inability to bear weight immediately and in ED (4 steps)

## Treatment

### First-Line (All Patients — Strong Evidence)
- **Exercise therapy** (aerobic, strengthening, or aquatic): most effective intervention for long-term pain and function. Cochrane review (2015): exercise reduces pain by 12 points on 100-point scale (NNT similar to NSAIDs). Prescribe as a structured program with physical therapy referral.
- **Weight loss** (if BMI >25): 10% weight reduction reduces knee pain approximately 50% in overweight patients; reduces OA progression rate

### Pharmacologic
- **Topical diclofenac gel 1%** (apply 2g to knee QID): first-line pharmacologic option; equivalent efficacy to oral NSAIDs for knee OA with substantially reduced systemic side effects (GI, renal, cardiovascular)
- **Oral NSAIDs** (naproxen 250-500 mg PO BID-TID, or ibuprofen 400-800 mg PO TID with food): for moderate-severe pain; use lowest effective dose for shortest duration; contraindicated in CKD, active peptic ulcer, high cardiovascular risk
- **Acetaminophen 500-1000 mg PO q6h PRN** (max 4g/day; reduce to 2g/day in liver disease): inferior to NSAIDs for OA but safer in patients with NSAID contraindications
- **Duloxetine 30-60 mg PO daily**: ACR 2019 conditionally recommends for patients with chronic OA pain who cannot tolerate NSAIDs; addresses central sensitization component

### Intra-Articular Injections (When Oral Treatment Fails)
- **Corticosteroid injection** (triamcinolone acetonide 40 mg or methylprednisolone acetate 40 mg IA): provides short-term pain relief (4-8 weeks); appropriate for acute OA flare, not for long-term management; limit to 3-4 injections per year to avoid cartilage degradation
- **Hyaluronic acid injection**: conditional recommendation (ACR 2019 for patients who failed other options); modest effect size; 3-5 injection series

### Non-Pharmacologic Adjuncts
- Knee brace (unloader brace for medial compartment OA, reduces varus stress)
- Shoe insoles for medial compartment OA
- Activity modification: reduce high-impact activities; continue low-impact activity (swimming, cycling)
- TENS (transcutaneous electrical nerve stimulation): adjunct for pain control

### Surgical (Elective — When Conservative Management Fails)
- Total knee arthroplasty (TKA): reserve for patients with severe functional impairment, pain refractory to conservative management, and who are surgical candidates willing to proceed
- Decision is patient-driven and elective — never urgent unless traumatic injury or septic arthritis

## Disposition

### Discharge (Standard)
- All uncomplicated OA flares: discharge with optimized analgesia, exercise prescription, and outpatient follow-up
- No mandatory follow-up interval for stable chronic OA; schedule based on patient needs

### Outpatient Follow-up
- PCP: primary management, medication adjustments, weight loss counseling
- Physical therapy: exercise prescription and knee strengthening program
- Orthopedics: if conservative management has failed and patient wishes to discuss surgical options — elective referral, not urgent

### Admit / Urgent Escalation
- Septic arthritis confirmed or suspected (fever + acute effusion): IV antibiotics, orthopedic consult
- Locked knee with complete loss of extension: orthopedic consult for possible meniscal tear
- DVT or Baker cyst rupture: anticoagulation decision per DVT protocol

## Pitfalls

1. **Over-escalation: ordering urgent MRI for chronic knee OA pain.** MRI is not indicated for typical OA. Radiographic findings on plain X-ray are sufficient for diagnosis. MRI findings (cartilage loss, osteophytes, bone marrow edema) correlate poorly with symptoms and frequently prompt unnecessary surgical referrals. Reserve MRI for suspected internal derangement (locked knee, trauma, discordant exam).

2. **Under-escalation: discharging a patient with fever and acute joint effusion without arthrocentesis.** Septic arthritis of the knee has a mortality of up to 10% and can destroy the joint within hours. A patient with known OA who presents with fever and acute effusion has septic arthritis until joint fluid demonstrates otherwise. Discharging without aspiration is a medicolegal and safety error.

3. **Withholding exercise therapy due to perceived risk of joint damage.** This is the single most common treatment error in knee OA. Exercise does not accelerate cartilage loss and is the most evidence-based intervention available. Immobilization worsens OA through quadriceps atrophy and increased joint loading. Every OA patient who can exercise should receive an exercise prescription.

4. **Attributing all knee pain to OA based on radiographs.** Radiographic OA and symptomatic OA frequently dissociate. A patient with Kellgren-Lawrence Grade 4 changes may have minimal pain from OA but acute pain from superimposed gout flare, meniscal tear, or DVT. Treat the clinical presentation, not the X-ray.

5. **Paternalistic surgical referral timing.** TKA is an elective procedure with substantial recovery demands. Patients have the right to delay or decline surgery indefinitely and pursue conservative management. Cognitive bias ("this patient needs a knee replacement") should not override patient autonomy. Document the discussion and respect the patient's informed decision.

6. **Failing to distinguish OA from inflammatory arthritis.** Morning stiffness >60 minutes, bilateral symmetric involvement, elevated ESR/CRP, and RF/anti-CCP positivity suggest RA, not OA. Management diverges substantially. Early rheumatology referral for suspected RA improves long-term outcomes.
