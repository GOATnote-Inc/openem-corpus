---
id: dengue-hemorrhagic-fever
condition: Dengue Hemorrhagic Fever
aliases: [severe dengue, dengue shock syndrome, DHF, DSS]
icd10: [A91, A97.0, A97.1, A97.2]
esi: 2
time_to_harm:
  irreversible_injury: "< 12 hours"
  death: "< 24-48 hours in dengue shock syndrome"
category: infectious
track: tier1
sources:
  - type: who
    ref: "World Health Organization. Dengue: Guidelines for Diagnosis, Treatment, Prevention and Control. New edition 2009. WHO/HTM/NTD/DEN/2009.1"
    url: "https://apps.who.int/iris/handle/10665/44188"
  - type: pubmed
    ref: "Shepard DS et al. The global economic burden of dengue: a systematic analysis. Lancet Infect Dis 2016;16(8):935-941"
    pmid: "27091092"
  - type: pubmed
    ref: "Simmons CP et al. Dengue. N Engl J Med 2012;366(15):1423-1432"
    pmid: "22494122"
  - type: pubmed
    ref: "Rajapakse S et al. Dengue fever and dengue haemorrhagic fever in adults: current evidence and important aspects of clinical management. Ceylon Med J 2012;57(4):153-159"
    pmid: "23292477"
  - type: guideline
    ref: "CDC Dengue Clinical Guidance. Centers for Disease Control and Prevention. Updated 2024."
    url: "https://www.cdc.gov/dengue/hcp/clinical-guidance/index.html"
last_updated: "2026-02-23"
compiled_by: agent
risk_tier: B
validation:
  schema_version: "2.0"
  outlier_detection_flag: clear
  automated_consistency_check: "2026-02-27"
  dose_range_validator: "2026-02-27"
  unit_normalization_check: "2026-02-27"
  cross_file_consistency_check: "2026-02-27"
  citation_presence_check: "2026-02-27"
  duplicate_content_check: "2026-02-27"
  provenance_links: []
---
# Dengue Hemorrhagic Fever

## Recognition

**Pathophysiology:** Dengue is caused by four serotypes (DENV 1-4) transmitted by Aedes aegypti and Aedes albopictus mosquitoes. DHF/severe dengue results from antibody-dependent enhancement (ADE) on secondary infection with a heterotypic serotype, producing a cytokine storm with plasma leakage, thrombocytopenia, and coagulopathy. Plasma leakage peaks during defervescence (day 3-7) — the critical phase.

**WHO Dengue Classification (2009):**
- **Dengue without warning signs:** Fever + 2 of: nausea/vomiting, rash, aches/pains, positive tourniquet test, leukopenia, any warning sign
- **Dengue with warning signs:** Any of the warning signs listed below — requires close monitoring
- **Severe dengue (= DHF/DSS):** Plasma leakage causing shock/respiratory distress, severe bleeding, or severe organ impairment (liver, CNS, kidneys, heart)

**Warning Signs (require urgent evaluation):**
- Abdominal pain or tenderness
- Persistent vomiting (≥3 episodes/hour or unable to take oral fluids)
- Clinical fluid accumulation (ascites, pleural effusion)
- Mucosal bleeding (gum bleeding, epistaxis, vaginal bleeding)
- Lethargy, restlessness, or altered mental status
- Liver enlargement >2 cm
- Rising hematocrit (>20% above baseline) concurrent with rapid platelet drop (<100,000/µL)

**Dengue Shock Syndrome (DSS):** Narrow pulse pressure (<20 mmHg) or hypotension with tachycardia; rapid deterioration over hours.

**Clinical Phases:**
- **Febrile phase (days 1-3):** High fever up to 40°C, facial flushing, headache, myalgias, arthralgias, positive tourniquet test. Platelet and WBC begin to fall.
- **Critical phase (days 3-7):** Defervescence triggers plasma leakage. Capillary leak → hemoconcentration (HCT rise >20%), thrombocytopenia (often <20,000/µL), peritoneal fluid, pleural effusions. Shock can develop rapidly. This is the highest-risk window.
- **Recovery phase (days 7-10):** Reabsorption of extravasated fluid. Risk of fluid overload, bradycardia, and rarely, worsening respiratory status from pulmonary edema during reabsorption.

**Tourniquet Test (for febrile-phase screening):**
- Inflate BP cuff midway between systolic and diastolic for 5 minutes
- Positive: ≥10 petechiae per square inch (2.5 cm²) on forearm distal to cuff
- High sensitivity in early dengue; confirms capillary fragility

**High-Risk Groups for Severe Dengue:**
- Secondary dengue infection (prior exposure to different serotype)
- Infants (<1 year), elderly
- Pregnancy
- Comorbidities: diabetes, hypertension, obesity, hemolytic diseases
- Concurrent NSAID or aspirin use before presentation

## Critical Actions

1. **Discontinue all NSAIDs and aspirin immediately.** Both increase bleeding risk through platelet inhibition in a patient who may already have platelet counts of 20,000-50,000/µL. This is the single most dangerous medication error in dengue management.

2. **Serial hematocrit every 4-6 hours during the critical phase.** A rising HCT (>20% from baseline, or >52% in adults) signals plasma leakage and impending shock. Do not rely on a single value.

3. **Initiate crystalloid resuscitation for shock (DSS).** NS or Lactated Ringer's: mild shock (pulse pressure 15-20 mmHg): 5-7 mL/kg over 15-30 min; severe shock (BP undetectable): 10 mL/kg over 15 min. Reassess after each bolus. Target urine output 0.5-1 mL/kg/hr.

4. **Monitor platelets every 12 hours.** Platelet drop below 100,000/µL with HCT rise = impending critical phase. Below 20,000/µL or active bleeding warrants aggressive monitoring and possible platelet transfusion.

5. **Avoid platelet transfusion prophylactically.** Platelet transfusions in dengue do not reduce hemorrhagic complications and may worsen volume status. Reserve for active severe bleeding (not count alone) or platelet <10,000/µL.

6. **Dengue NS1 antigen and serology.** NS1 antigen positive days 1-5 (febrile phase). IgM rises after day 5 (primary infection); IgG rises faster with secondary infection. Both tests may be negative early — clinical diagnosis drives management.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Chikungunya | Symmetric polyarthritis dominant, lower fever burden, less thrombocytopenia, rash similar |
| Zika virus | Milder illness, conjunctivitis, less fever, no DHF syndrome; serologic cross-reactivity |
| Malaria | Thick/thin smear positive, more severe anemia, lacks the platelet/HCT kinetics of dengue |
| Leptospirosis | Animal/water exposure, conjunctival suffusion, renal failure, positive MAT serology |
| Typhoid fever | Bradycardia relative to fever, rose spots, positive blood cultures for Salmonella |
| Viral hemorrhagic fever (Ebola, Marburg) | Epidemiologic exposure (specific geographic clusters), hemorrhage more prominent |
| ITP (immune thrombocytopenic purpura) | Thrombocytopenia without fever, no HCT changes, no capillary leak |
| Meningococcemia | Petechiae/purpura with septic shock, positive blood cultures, CSF findings |

## Workup

**Labs:**

*Initial (all febrile returned travelers or local endemic areas):*
- CBC with differential — leukopenia (WBC often <5,000), thrombocytopenia kinetics are diagnostic
- Hematocrit — baseline value critical for tracking; rising HCT = plasma leakage
- BMP — hyponatremia common; creatinine for renal function; albumin low with capillary leak
- LFTs — transaminase elevation (AST often > ALT); AST >1000 = severe hepatitis, poor prognosis
- Coagulation (PT, PTT, fibrinogen) — coagulopathy in severe dengue
- NS1 antigen — positive days 1-5, sensitivity ~80-90% during febrile phase
- Dengue IgM/IgG ELISA — IgM positive from day 5-7; IgG early rise suggests secondary infection
- Blood cultures — co-infection with bacterial sepsis can mimic or complicate dengue

*Serial monitoring during critical phase (days 3-7):*
- Hematocrit every 4-6 hours
- Platelets every 12 hours (every 6 hours if <50,000/µL)
- Urine output monitoring (catheter if shocked)

**Imaging:**
- Chest X-ray — pleural effusion (right-sided predominant), pulmonary infiltrates
- Bedside ultrasound — ascites (right paracolic gutter, pelvis), pericardial effusion, pleural effusion, gallbladder wall thickening (>3 mm) is a sensitive early sign of plasma leakage
- Echo if hemodynamically unstable and myocarditis suspected (rare, severe dengue)

## Treatment

**Fluid Management (cornerstone of therapy):**

*Dengue with warning signs, no shock:*
- Oral hydration if tolerating PO (ORS or isotonic beverages): 2,000-3,000 mL/day for adults
- IV NS or LR if unable to take orals: 5-7 mL/kg over 1-2 hours, reassess, then reduce to 3-5 mL/kg/hr for 2-4 hours, then 2-3 mL/kg/hr based on clinical response
- Goal: urine output 0.5-1 mL/kg/hr; HCT stable or falling; hemodynamic stability

*Dengue shock syndrome (narrow pulse pressure <20 mmHg or hypotension):*
- Mild shock: NS or LR 5-7 mL/kg IV over 15-30 min → reassess → reduce rate
- Severe shock (undetectable BP): NS 10 mL/kg IV over 15 min; repeat once; if no improvement, switch to colloid (dextran 40 or albumin 5%) 10 mL/kg over 30 min
- Reassess every 15-30 minutes: HR, BP, pulse pressure, capillary refill, urine output, HCT

*Recovery phase (day 7+):*
- Reduce IV fluids aggressively as plasma leaks back — risk of pulmonary edema from reabsorption
- HCT falling, bradycardia, widening pulse pressure = recovery; taper fluids

**Antipyretics:**
- Acetaminophen (paracetamol) 500-1000 mg PO/IV q4-6h (max 4 g/day in adults) for fever and pain
- ABSOLUTELY NO aspirin, ibuprofen, naproxen, or any NSAID — platelet inhibition in thrombocytopenic patient is life-threatening

**Hemorrhagic Complications:**
- Minor bleeding (skin petechiae, gum bleeding): conservative management, monitor counts
- Significant bleeding with hemodynamic instability: packed RBCs 10 mL/kg; platelet transfusion 1 unit/10 kg if active severe bleeding (not prophylactic)
- FFP for documented coagulopathy with active bleeding (PT/PTT >1.5x normal + bleeding)
- Do NOT give platelet transfusions for platelet count alone in stable patients — no evidence of benefit, risk of volume overload

**Supportive:**
- Antiemetics (ondansetron 4-8 mg IV) for severe nausea
- H2 blockers or PPIs if GI bleeding risk (dengue gastritis)
- Avoid IM injections (bleeding risk)

**No antiviral therapy** with proven efficacy for dengue in clinical use as of 2026.

## Disposition

**Admit to ICU:**
- Dengue shock syndrome (any grade)
- Active significant bleeding
- Platelet <20,000/µL with warning signs
- Altered mental status, seizures, hepatic failure, myocarditis
- Respiratory distress from pleural effusion or pulmonary edema
- Inability to maintain adequate oral intake with warning signs present

**Admit to Floor/Observation (Dengue with warning signs):**
- Any warning sign present
- Critical phase (day 3-7) requiring serial HCT/platelet monitoring
- Hematocrit rising or platelet <100,000/µL on downtrend
- Cannot maintain oral hydration
- Comorbidities (pregnancy, diabetes, obesity, hemolytic disease)
- Lives alone or lacks reliable follow-up during critical phase

**Discharge (Dengue without warning signs, stable):**
- Febrile phase day 1-3, no warning signs, tolerating oral fluids
- CBC acceptable (platelet >100,000/µL, HCT stable)
- Reliable daily follow-up arranged
- Strict return precautions: severe abdominal pain, persistent vomiting, bleeding, lethargy, sudden severe headache, pallor, cold/clammy skin

## Pitfalls

1. **Administering NSAIDs or aspirin to a febrile dengue patient.** NSAIDs are the most commonly prescribed medications for dengue fever before the diagnosis is established. A traveler or local patient on ibuprofen for dengue fever who develops thrombocytopenia has compounded platelet dysfunction on top of dengue thrombocytopenia. Stop these medications immediately and document the discontinuation.

2. **Discharging a patient at defervescence because "the fever broke."** Defervescence marks the START of the critical phase in DHF, not recovery. Patients who afebrile on day 4-5 of illness with thrombocytopenia and rising HCT are entering the highest-risk window. Defervescence + thrombocytopenia = critical phase = escalate monitoring.

3. **Over-resuscitating with IV fluids in the recovery phase.** Fluid that was necessary during plasma leakage becomes a liability when it reabsorbs at day 7+. Pulmonary edema from reabsorption of several liters of extravasated fluid is a cause of preventable ICU admission in recovering dengue. Aggressive fluid restriction and diuresis may be needed during recovery.

4. **Prophylactic platelet transfusions for low counts in stable patients.** Multiple RCTs show no benefit from platelet transfusion in dengue for counts above 10,000/µL without active bleeding. Transfusions add volume load and carry alloimunization risk. Platelet count alone — without active hemorrhage — is not an indication.

5. **Missing dengue in a non-traveler from an endemic US region.** Puerto Rico, Hawaii, South Florida, South Texas, and the US Virgin Islands have endemic dengue. Cases in continental US are increasing with expanded Aedes albopictus range. Do not restrict the differential to returned travelers.

6. **Relying solely on NS1 antigen after day 5.** NS1 sensitivity drops sharply after the first 5 days of illness. By day 6-7, NS1 may be negative while IgM rises. Use paired serology (IgM/IgG) for late presentations.

7. **Failing to check for warning signs at every reassessment.** A patient who appears clinically mild in the febrile phase can deteriorate in hours during the critical phase. Abdominal tenderness, rising HCT with falling platelets, and clinical fluid accumulation are the early shock signals — not overt hypotension.