---
id: disseminated-intravascular-coagulation
condition: Disseminated Intravascular Coagulation
aliases: [DIC, consumptive coagulopathy, defibrination syndrome]
icd10: [D65]
esi: 1
time_to_harm:
  irreversible_injury: "< 6 hours (multi-organ microthrombosis)"
  death: "< 24 hours (hemorrhagic or thrombotic complications)"
  optimal_intervention_window: "< 2 hours (treat underlying cause)"
category: hematologic
track: tier1
sources:
  - type: guideline
    ref: "British Committee for Standards in Haematology: Guidelines for the Diagnosis and Management of DIC, 2009"
  - type: guideline
    ref: "International Society on Thrombosis and Haemostasis (ISTH): DIC Scoring System and Management, 2017"
  - type: guideline
    ref: "Clinical Practice Guidelines for Management of DIC in Japan, 2024"
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
# Disseminated Intravascular Coagulation

## Recognition

**Presentation:**
- Bleeding from multiple sites simultaneously (venipuncture sites, surgical wounds, mucosal surfaces, catheter sites)
- Petechiae, purpura, ecchymoses
- Oozing from IV sites, drains
- Microvascular thrombosis: end-organ dysfunction (renal failure, hepatic dysfunction, ARDS, altered mental status)
- Acrocyanosis, digital ischemia, skin necrosis (purpura fulminans)
- Hemodynamic instability

**Underlying causes (DIC is NEVER a primary diagnosis):**
- **Sepsis** (most common cause — 30-50% of sepsis patients develop DIC)
- **Trauma** (especially head injury, fat embolism, crush injury)
- **Obstetric:** Placental abruption, amniotic fluid embolism, HELLP, retained dead fetus, eclampsia
- **Malignancy:** Acute promyelocytic leukemia (APL), mucin-secreting adenocarcinomas
- **Vascular:** Large aortic aneurysm, giant hemangioma (Kasabach-Merritt)
- **Toxic:** Snake envenomation, transfusion reactions, severe burns

**ISTH DIC Scoring System (>= 5 = overt DIC):**
- Platelet count: > 100k (0), 50-100k (1), < 50k (2)
- D-dimer: No increase (0), moderate (2), strong increase (3)
- Prolonged PT: < 3 sec (0), 3-6 sec (1), > 6 sec (2)
- Fibrinogen: > 1 g/L (0), < 1 g/L (1)

## Critical Actions

1. **Identify and treat the underlying cause** — this is the single most important intervention
2. **Sepsis: broad-spectrum antibiotics and source control**
3. **Obstetric: deliver the fetus/placenta**
4. **Trauma: damage control surgery, hemorrhage control**
5. **Transfuse actively bleeding patients** — platelets, FFP, cryoprecipitate (see Treatment)
6. **Do NOT anticoagulate** unless thrombosis predominates and bleeding is controlled (e.g., purpura fulminans, large vessel thrombosis)
7. **Repeat coagulation studies q4-6h** to trend

## Differential Diagnosis

- Thrombotic thrombocytopenic purpura (TTP) — MAHA with normal coags, ADAMTS13 activity < 10%
- Hemolytic uremic syndrome (HUS) — renal failure predominates, bloody diarrhea if typical HUS
- Heparin-induced thrombocytopenia (HIT) — thrombosis + thrombocytopenia, temporal relation to heparin
- Liver failure — similar coagulation derangements but different clinical context; factor VIII may be elevated (depressed in DIC)
- ITP — isolated thrombocytopenia without coagulopathy
- Vitamin K deficiency — prolonged PT corrected with vitamin K, normal D-dimer
- Factor inhibitors (acquired hemophilia) — isolated prolonged aPTT, mixing study shows inhibitor

## Workup

- **CBC with platelet count** — thrombocytopenia (progressive decline is key)
- **PT/INR, aPTT** — prolonged
- **Fibrinogen** — low (< 150 mg/dL is concerning; < 100 mg/dL in DIC)
- **D-dimer** — markedly elevated (most sensitive but least specific)
- **Peripheral blood smear** — schistocytes (microangiopathic hemolytic anemia)
- **LDH** — elevated (hemolysis)
- **Haptoglobin** — decreased
- **Factor VIII activity** — decreased in DIC (elevated in liver failure — useful distinction)
- **Calculate ISTH DIC score** — repeat serially (trending is more useful than a single value)
- **Type and screen/crossmatch** — anticipate massive transfusion
- **BMP, hepatic panel** — assess end-organ damage
- **Lactate** — indicator of tissue hypoperfusion
- **Blood cultures** if sepsis suspected

## Treatment

### Treat the Underlying Cause (Top Priority)
- Sepsis: Antibiotics + source control
- Obstetric: Delivery
- Trauma: Hemorrhage control, damage control surgery
- Malignancy: Chemotherapy (APL: all-trans retinoic acid + arsenic trioxide)

### Transfusion Support (For Active Bleeding)
- **Platelets:** Transfuse if < 50,000/mm3 with active bleeding (or < 20,000/mm3 prophylactically)
- **Fresh Frozen Plasma (FFP):** 15-20 mL/kg if PT/INR > 1.5 with active bleeding
- **Cryoprecipitate:** 10 units (1 pooled dose) if fibrinogen < 150 mg/dL; target fibrinogen > 150 mg/dL
- **PRBCs:** Transfuse for Hgb < 7 g/dL (or < 9 g/dL with active hemorrhage or cardiac disease)
- **Massive transfusion protocol:** Activate if hemorrhagic DIC with hemodynamic instability (1:1:1 PRBC:FFP:platelets)

### Anticoagulation (ONLY for Thrombosis-Predominant DIC)
- **Heparin:** Unfractionated heparin 10 units/kg/hr IV (low-dose) — ONLY if:
  - Large vessel thrombosis or purpura fulminans WITH bleeding controlled
  - Fibrinogen > 100 mg/dL and platelets > 50,000
- **Purpura fulminans:** Protein C concentrate 100 IU/kg IV if available; otherwise FFP + heparin

### What NOT to Do
- Do NOT use antifibrinolytics (TXA, aminocaproic acid) in DIC — blocks compensatory fibrinolysis, worsens microthrombosis. Exception: hyperfibrinolytic DIC (APL, certain obstetric causes) under hematology guidance.
- Do NOT transfuse to normalize labs in non-bleeding patients (transfusion is not without risk and may "fuel the fire")

## Disposition

- **All DIC patients:** ICU admission
- **Serial labs:** CBC, coags, fibrinogen q4-6h initially; trending is essential
- **Hematology consultation** — especially for APL-associated DIC, thrombosis-predominant DIC, or refractory coagulopathy
- **Obstetric DIC:** Co-manage with OB; delivery is definitive treatment
- **Isolation:** Standard precautions
- **Reportable:** Not a reportable disease

## Pitfalls

1. **Treating DIC without addressing the underlying cause.** Transfusion and supportive care alone will not resolve DIC. The underlying trigger (sepsis, obstetric cause, trauma) must be identified and treated urgently.

2. **Using antifibrinolytics (TXA) in DIC.** TXA blocks fibrinolysis, which is a compensatory mechanism in DIC. Administration can worsen microvascular thrombosis and cause fatal organ failure. Exception only under hematology guidance for hyperfibrinolytic DIC.

3. **Confusing DIC with TTP.** Both cause thrombocytopenia and schistocytes. In TTP, coagulation studies (PT, fibrinogen) are typically NORMAL, and ADAMTS13 is severely deficient. In DIC, coags are deranged. This distinction changes management completely (plasma exchange for TTP, not DIC).

4. **Transfusing to normalize labs in the non-bleeding patient.** Transfusion is indicated for active bleeding or imminent procedures, not for laboratory values alone. Prophylactic platelet transfusion only if < 20,000/mm3.

5. **Missing APL as the underlying cause.** Acute promyelocytic leukemia classically presents with severe DIC. Auer rods and promyelocytes on peripheral smear are diagnostic clues. ATRA therapy is life-saving and must be started emergently.

6. **Not trending labs serially.** A single set of coagulation labs can be misleading. The trend (rising D-dimer, falling fibrinogen and platelets) is more diagnostic than any single value.
