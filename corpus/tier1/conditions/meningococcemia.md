---
id: meningococcemia
condition: Meningococcemia
aliases: [meningococcal septicemia, Neisseria meningitidis bacteremia, Waterhouse-Friderichsen syndrome, meningococcal disease]
icd10: [A39.2, A39.3, A39.4]
esi: 1
time_to_harm:
  irreversible_injury: "< 2 hours"
  death: "< 12 hours from symptom onset"
  optimal_intervention_window: "< 1 hour (antibiotics)"
mortality_if_delayed: "10-15% overall; 40-50% in fulminant purpura fulminans"
category: pediatric
track: tier1
sources:
  - type: guideline
    ref: "AAP Red Book: Report of the Committee on Infectious Diseases, 2021-2024"
  - type: cdc
    ref: "CDC. Meningococcal Disease: Clinical Information. Updated 2023"
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
# Meningococcemia

## Recognition

**Fulminant presentation (hours):**
- Fever, rigors, malaise (may mimic viral illness initially)
- Petechiae → purpura → purpura fulminans (rapidly expanding, non-blanching, geographic purple patches)
- Petechiae that DO NOT blanch with pressure (glass test)
- Hypotension, tachycardia, altered mental status
- DIC: bleeding from IV sites, mucosal hemorrhage
- Waterhouse-Friderichsen syndrome: bilateral adrenal hemorrhagic necrosis → refractory shock

**Key warning signs that distinguish from viral exanthem:**
- Petechiae below the nipple line (axial distribution)
- Petechiae appearing or expanding DURING observation
- Ill-appearing child with petechiae and fever
- Rapid clinical deterioration over hours

**Populations at risk:**
- Children < 5 years (peak: infants < 1 year)
- Adolescents 16-21 years (college dormitories, military barracks)
- Asplenic or complement-deficient patients
- Unvaccinated individuals
- Close contacts of confirmed cases

**Meningococcal disease spectrum:**
- Meningococcemia without meningitis (most lethal form)
- Meningitis with or without meningococcemia
- Combined meningitis + meningococcemia

## Critical Actions

| Action | Target |
|---|---|
| IV/IO access | < 5 minutes |
| Blood cultures | Before antibiotics (but do NOT delay antibiotics) |
| Empiric ceftriaxone | < 30 minutes from suspicion |
| Aggressive fluid resuscitation | Immediately |
| Droplet isolation | Immediately |

1. **IV or IO access** — do not delay; IO if peripheral access fails within 2 minutes
2. **Ceftriaxone 100 mg/kg IV (max 4 g)** — give IMMEDIATELY upon clinical suspicion; do NOT wait for LP or cultures
3. **Aggressive fluid resuscitation:** NS 20 mL/kg bolus, repeat up to 60 mL/kg in first hour
4. **Vasopressors** if fluid-refractory: norepinephrine 0.05-0.3 mcg/kg/min or epinephrine 0.05-0.3 mcg/kg/min
5. **Blood cultures x 2** — draw before antibiotics if possible but NEVER delay antibiotics
6. **Droplet precautions** — until 24 hours of effective antibiotic therapy
7. **Stress-dose steroids** — hydrocortisone 2 mg/kg IV (max 100 mg) if suspected adrenal insufficiency (Waterhouse-Friderichsen) or refractory shock
8. **Notify public health** — reportable disease; close contacts need chemoprophylaxis

## Differential Diagnosis

- Henoch-Schonlein purpura (palpable purpura, normal platelets, non-toxic appearance)
- Rocky Mountain spotted fever (tick exposure, centripetal spread, headache)
- Immune thrombocytopenic purpura (isolated thrombocytopenia, well-appearing)
- Hemolytic uremic syndrome (bloody diarrhea, anemia, thrombocytopenia, AKI)
- Disseminated intravascular coagulation from other causes (sepsis, malignancy)
- Viral exanthem (blanching, non-petechial, well-appearing)
- Child abuse (inconsistent history, varying ages of bruises)
- Leukemia (pancytopenia, hepatosplenomegaly, bone pain)
- Gonococcemia (adolescents, pustular skin lesions, tenosynovitis, sexually active)

## Workup

- **Blood cultures x 2** — before antibiotics if feasible
- **CBC with differential:** leukocytosis or leukopenia (ominous); thrombocytopenia
- **BMP:** electrolytes, creatinine (AKI)
- **Coagulation studies:** PT, INR, fibrinogen, D-dimer (DIC panel)
- **Lactate:** elevated = tissue hypoperfusion
- **Blood gas:** metabolic acidosis
- **CRP, procalcitonin:** markedly elevated
- **Cortisol level:** if adrenal insufficiency suspected (random cortisol < 18 mcg/dL is concerning)
- **Lumbar puncture:** ONLY if patient is hemodynamically stable and no contraindications (do NOT delay antibiotics for LP; LP is contraindicated if coagulopathic, hemodynamically unstable, or signs of raised ICP)
- **CSF analysis (if obtained):** Gram stain (gram-negative diplococci), culture, cell count, protein, glucose, meningococcal PCR
- **Skin biopsy of purpuric lesion:** Gram stain shows gram-negative diplococci; can confirm diagnosis when blood cultures are negative

## Treatment

### Antibiotics
- **Ceftriaxone 100 mg/kg IV q24h (max 4 g/day)** — first-line
- OR **cefotaxime 75 mg/kg IV q6h (max 12 g/day)**
- **Penicillin G 300,000 units/kg/day IV divided q4-6h (max 24 million units/day)** if confirmed susceptible
- Duration: 7 days IV

### Shock Management
- **IV NS 20 mL/kg bolus** — repeat up to 60 mL/kg in first hour
- **Norepinephrine 0.05-0.5 mcg/kg/min IV** — first-line vasopressor
- **Epinephrine 0.05-0.3 mcg/kg/min IV** — if cold shock phenotype
- **Vasopressin 0.0003-0.002 units/kg/min IV** — catecholamine-resistant shock

### DIC Management
- **Fresh frozen plasma 15 mL/kg IV** if active bleeding + prolonged PT/INR
- **Cryoprecipitate 5-10 mL/kg IV** if fibrinogen < 100 mg/dL
- **Platelet transfusion 10 mL/kg IV** if platelets < 20,000 or active bleeding
- **Protein C concentrate** — investigational; case reports of benefit in purpura fulminans

### Adrenal Crisis (Waterhouse-Friderichsen Syndrome)
- **Hydrocortisone 2 mg/kg IV bolus (max 100 mg)** then 1-2 mg/kg IV q6-8h
- Empiric treatment in any patient with refractory shock

### Chemoprophylaxis for Close Contacts
- **Rifampin:** children < 1 month: 5 mg/kg PO BID x 2 days; children >= 1 month: 10 mg/kg PO BID (max 600 mg) x 2 days; adults: 600 mg PO BID x 2 days
- **Ciprofloxacin 500 mg PO x 1** (adults only; not for pregnant women or children)
- **Ceftriaxone 250 mg IM x 1** (adults); 125 mg IM x 1 (children < 15 years) — preferred in pregnancy
- Close contacts: household members, daycare contacts, anyone with direct exposure to oral secretions

## Disposition

- **All cases:** ICU admission; continuous monitoring; arterial and central venous access
- **Purpura fulminans:** may require surgical debridement or amputation for necrotic extremities
- **Transfer:** if no PICU capability, stabilize with antibiotics, fluids, and vasopressors; transfer immediately
- **Reportable disease:** mandatory public health notification within 24 hours

## Pitfalls

1. **Dismissing petechiae in a febrile child as viral.** A febrile child with non-blanching petechiae must be treated as meningococcemia until proven otherwise. Viral petechiae (from coughing/vomiting) are typically above the nipple line; meningococcal petechiae involve the trunk and extremities.

2. **Delaying antibiotics for lumbar puncture.** CSF can yield organisms for hours after antibiotics, but every hour of antibiotic delay increases mortality. Give ceftriaxone immediately upon clinical suspicion.

3. **Failure to recognize meningococcemia without meningitis.** Meningococcemia presents as septic shock with purpura; meningeal signs may be absent. This is the most rapidly fatal form of meningococcal disease.

4. **Not considering Waterhouse-Friderichsen syndrome in refractory shock.** Bilateral adrenal hemorrhage causes refractory hypotension despite fluids and vasopressors. Empiric hydrocortisone 2 mg/kg IV is indicated in any meningococcemia patient with refractory shock.

5. **Failing to initiate chemoprophylaxis for close contacts.** Meningococcal disease has a secondary attack rate of 500-800x baseline in household contacts. Rifampin, ciprofloxacin, or ceftriaxone prophylaxis must be started within 24 hours of case identification.
