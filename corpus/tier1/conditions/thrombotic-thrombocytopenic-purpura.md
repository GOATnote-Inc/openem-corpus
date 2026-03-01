---
id: thrombotic-thrombocytopenic-purpura
condition: Thrombotic Thrombocytopenic Purpura
aliases: [TTP, immune TTP, iTTP, acquired TTP, Moschcowitz syndrome]
icd10: [M31.1]
esi: 1
time_to_harm:
  irreversible_injury: "< 24 hours (stroke, myocardial ischemia)"
  death: "< 48 hours without plasma exchange (historical mortality 90%)"
  optimal_intervention_window: "< 4-8 hours (plasma exchange initiation)"
category: hematologic
track: tier1
sources:
  - type: guideline
    ref: "ISTH Guidelines for Treatment of Thrombotic Thrombocytopenic Purpura, 2020"
  - type: guideline
    ref: "2025 Focused Update of the 2020 ISTH Guidelines for Management of TTP. J Thromb Haemost, 2025"
  - type: guideline
    ref: "ASH 2020 Guidelines on Management of Thrombotic Thrombocytopenic Purpura"
  - type: guideline
    ref: "British Society for Haematology: Guidelines on the Diagnosis and Management of TTP, 2012 (updated 2023)"
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
# Thrombotic Thrombocytopenic Purpura

## Recognition

**Classic pentad (full pentad present in < 10% at presentation):**
- Microangiopathic hemolytic anemia (MAHA) — schistocytes, elevated LDH, low haptoglobin
- Thrombocytopenia (often < 30,000/mm3)
- Neurologic symptoms (confusion, headache, stroke, seizures, coma)
- Renal impairment (usually mild; creatinine < 2 mg/dL)
- Fever

**Practical diagnostic approach — suspect TTP when:**
- MAHA (schistocytes on smear) + thrombocytopenia WITHOUT an alternative explanation
- Do NOT wait for the full pentad — the diagnosis is clinical

**PLASMIC score (predicts ADAMTS13 deficiency):**
- Platelet count < 30,000 (+1)
- Hemolysis (reticulocytes > 2.5%, haptoglobin undetectable, indirect bilirubin > 2) (+1)
- No active cancer (+1)
- No organ transplant (+1)
- MCV < 90 fL (+1)
- INR < 1.5 (+1)
- Creatinine < 2.0 mg/dL (+1)
- Score >= 5: high probability of ADAMTS13 deficiency

**Triggers/associations:**
- Autoimmune (most common: autoantibody against ADAMTS13)
- Pregnancy/postpartum
- HIV infection
- Medications (quinine, ticlopidine, clopidogrel, cyclosporine, tacrolimus)
- Hematopoietic stem cell transplant

## Critical Actions

1. **Initiate plasma exchange (TPE) within 4-8 hours** of suspected TTP — mortality drops from 90% to 10-20% with timely TPE
2. **Start corticosteroids immediately:** Methylprednisolone 1 g IV daily x 3 days (pulse), then prednisone 1 mg/kg/day
3. **Send ADAMTS13 activity level** BEFORE initiating plasma exchange (results take days but drawn before treatment)
4. **Administer caplacizumab** 11 mg IV bolus, then 11 mg SC daily (anti-vWF antibody fragment)
5. **Do NOT transfuse platelets** unless life-threatening hemorrhage or emergent invasive procedure — platelet transfusion may worsen thrombosis
6. **Hematology consultation immediately**

## Differential Diagnosis

- Disseminated intravascular coagulation (DIC) — prolonged PT, low fibrinogen (TTP has NORMAL coags)
- Hemolytic uremic syndrome (HUS) — renal failure predominates, diarrhea if STEC-HUS, normal ADAMTS13
- Evans syndrome — autoimmune hemolytic anemia + ITP; positive DAT
- HELLP syndrome — pregnant, elevated liver enzymes, right upper quadrant pain
- Malignant hypertension — severely elevated BP, MAHA secondary to endothelial damage
- Autoimmune hemolytic anemia — positive Coombs/DAT, no schistocytes
- Catastrophic antiphospholipid syndrome — thrombosis + thrombocytopenia + multi-organ failure

## Workup

- **CBC with platelet count** — severe thrombocytopenia (often < 30,000)
- **Peripheral blood smear** — schistocytes (> 1% or > 2 per HPF); confirm MAHA
- **Reticulocyte count** — elevated (appropriate marrow response to hemolysis)
- **LDH** — markedly elevated (hemolysis marker)
- **Haptoglobin** — undetectable or very low
- **Indirect bilirubin** — elevated
- **Direct Coombs test (DAT)** — negative (excludes autoimmune hemolytic anemia)
- **PT/INR, aPTT, fibrinogen** — NORMAL (critical distinction from DIC)
- **ADAMTS13 activity** — < 10% confirms acquired TTP (send BEFORE plasma exchange)
- **ADAMTS13 inhibitor titer** — present in immune TTP
- **BMP** — creatinine usually < 2 mg/dL (if > 3, consider HUS)
- **Troponin** — elevated in cardiac involvement (subclinical myocardial ischemia common)
- **Hepatic panel** — to exclude HELLP
- **Pregnancy test**
- **HIV test**
- **Blood type and crossmatch** — anticipate need for plasma products

## Treatment

### Plasma Exchange (TPE) — Life-Saving
- **1.0-1.5 plasma volumes exchanged daily** with fresh frozen plasma as replacement fluid
- Continue daily until platelet count > 150,000 for 2 consecutive days + normalizing LDH
- If TPE unavailable, transfuse FFP 15-30 mL/kg as temporizing bridge during transfer

### Corticosteroids
- **Methylprednisolone 1 g IV daily x 3 days** (pulse therapy)
- Then prednisone 1 mg/kg/day PO, taper over 2-4 weeks after remission

### Caplacizumab
- **11 mg IV bolus** before first TPE
- Then **11 mg SC daily** during TPE and for 30 days after last TPE
- Reduces time to platelet response, decreases risk of exacerbation, TTP-related death, and thromboembolic events
- Bleeding risk: monitor and adjust anticoagulation

### Rituximab
- **375 mg/m2 IV weekly x 4 weeks** — recommended for refractory TTP or early in disease to reduce autoantibody production
- Increasingly used as first-line adjunctive therapy

### Platelet Transfusion
- **Generally CONTRAINDICATED** — may worsen microvascular thrombosis ("fueling the fire")
- Exceptions: Life-threatening hemorrhage (e.g., intracranial hemorrhage), before emergent surgery/procedures

### VTE Prophylaxis
- Withhold until platelet count recovering (> 50,000); then start pharmacologic DVT prophylaxis

## Disposition

- **All TTP patients:** ICU admission; daily plasma exchange
- **Transfer immediately** if facility cannot perform therapeutic plasma exchange; start FFP infusion before transport
- **Hematology consultation** is mandatory
- **Monitoring:** Daily CBC, LDH, reticulocyte count, renal function
- **Isolation:** Standard precautions
- **Reportable:** Not a reportable disease

## Pitfalls

1. **Waiting for ADAMTS13 results before starting plasma exchange.** ADAMTS13 levels take days to return. TTP is a clinical diagnosis — MAHA + thrombocytopenia = start TPE now. ADAMTS13 confirms the diagnosis retrospectively.

2. **Transfusing platelets.** Platelet transfusion in TTP provides substrate for vWF-mediated microthrombosis. It is associated with clinical deterioration. Only transfuse for life-threatening hemorrhage.

3. **Confusing TTP with DIC and ordering FFP/cryoprecipitate instead of TPE.** Check PT/INR and fibrinogen — these are NORMAL in TTP and prolonged/low in DIC. This distinction is critical.

4. **Missing cardiac involvement.** Troponin elevation occurs in 25-60% of TTP episodes due to coronary microthrombosis. Check troponin and ECG. Cardiac death is a leading cause of TTP mortality.

5. **Discharging a patient with MAHA and thrombocytopenia without a diagnosis.** Any patient with schistocytes + low platelets + normal coags needs emergent hematology evaluation. This combination is TTP until proven otherwise.

6. **Not starting corticosteroids concurrently.** Steroids are part of first-line therapy alongside TPE. Delaying steroids reduces the effectiveness of initial management.
