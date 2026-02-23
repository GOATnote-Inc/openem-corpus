---
id: cerebral-malaria
condition: Cerebral Malaria
aliases: [severe malaria, Plasmodium falciparum cerebral malaria, complicated malaria]
icd10: [B50.0, B50.8]
esi: 1
time_to_harm:
  irreversible_injury: "< 6 hours"
  death: "< 24 hours without treatment"
  optimal_intervention_window: "Immediate IV artesunate within 1 hour of presentation"
category: infectious
track: tier1
sources:
  - type: guideline
    ref: "World Health Organization. Management of Severe Malaria: A Practical Handbook. 3rd ed. WHO Press, 2012. ISBN 9789241548526"
    url: "https://apps.who.int/iris/handle/10665/79317"
  - type: pubmed
    ref: "Dondorp AM et al. Artesunate versus quinine in the treatment of severe falciparum malaria in African children (AQUAMAT): an open-label, randomised trial. Lancet 2010;376(9753):1647-1657"
    pmid: "21062666"
  - type: pubmed
    ref: "Dondorp AM et al. Artesunate versus quinine for treatment of severe falciparum malaria: a randomised trial. Lancet 2005;366(9487):717-725"
    pmid: "16125588"
  - type: pubmed
    ref: "Idro R et al. Cerebral malaria: mechanisms of brain injury and strategies for improved neurocognitive outcome. Pediatr Res 2010;68(4):267-274"
    pmid: "20606600"
  - type: guideline
    ref: "CDC Treatment Guidelines for Severe Malaria in the United States. Centers for Disease Control and Prevention. Updated 2023."
    url: "https://www.cdc.gov/malaria/hcp/treatment/index.html"
last_updated: "2026-02-23"
compiled_by: agent
risk_tier: A
validation:
  schema_version: "2.0"
  outlier_detection_flag: clear
  automated_consistency_check: null
  dose_range_validator: null
  unit_normalization_check: null
  cross_file_consistency_check: null
  citation_presence_check: null
  duplicate_content_check: null
  guideline_version_reference: null
  provenance_links: []
---
# Cerebral Malaria

## Recognition

**Definition:** WHO criteria — unarousable coma (Blantyre Coma Scale ≤2 in children, GCS <11 in adults) in a patient with confirmed Plasmodium falciparum infection, with no other explanation for the coma.

**Epidemiology:** Primarily affects travelers returning from sub-Saharan Africa, Southeast Asia, and South Asia. In endemic regions, predominantly affects children under 5. US cases (~2,000/year) are predominantly falciparum imported from West Africa. Mortality 15-25% with treatment; ~100% without.

**Pathophysiology:** Sequestration of parasitized RBCs in cerebral microvasculature via cytoadherence to endothelial receptors (PfEMP1-ICAM1 binding). Results in mechanical obstruction, endothelial activation, neuroinflammation, impaired cerebral autoregulation, and blood-brain barrier disruption.

**Clinical Presentation:**
- **Classic triad:** fever, impaired consciousness, seizures
- Fever (often >39°C), rigors, diaphoresis
- Altered mental status ranging from confusion to deep coma
- Generalized tonic-clonic seizures (50-80% of pediatric cases; less common in adults)
- Posturing (decerebrate or decorticate)
- Conjugate gaze deviation, abnormal eye movements
- Hypoglycemia-driven obtundation (especially with quinine or pregnancy)
- Anemia (hemolytic), jaundice, hemoglobinuria (blackwater fever)
- Respiratory distress (acidosis, concurrent pulmonary edema)
- Abnormal bleeding in severe thrombocytopenia

**Other WHO Criteria for Severe Malaria (any = treat as severe):**
- Prostration (unable to sit, stand, or feed self)
- Respiratory distress or acidosis (pH <7.25, bicarbonate <15 mmol/L)
- Hypoglycemia (glucose <2.2 mmol/L / <40 mg/dL)
- Severe anemia (Hgb <7 g/dL, HCT <20%)
- Renal failure (creatinine >3.0 mg/dL)
- Pulmonary edema (radiographic or SpO2 <92% on room air)
- Abnormal bleeding, hyperparasitemia (>5% infected RBCs), circulatory collapse

**Travel History:** Every febrile returning traveler from malaria-endemic region is malaria until proven otherwise. Incubation 7-30 days for falciparum (can be up to 1 year for P. vivax/ovale).

## Critical Actions

1. **Initiate IV artesunate immediately** — do not wait for specialist consultation. IV artesunate 2.4 mg/kg IV at 0, 12, and 24 hours, then every 24 hours until oral therapy tolerated. Available in US via CDC drug service (770-488-7788, 24/7) and increasingly stocked at major centers. If artesunate unavailable, IV quinidine gluconate 10 mg/kg loading dose over 1-2 hours, then 0.02 mg/kg/min continuous infusion (requires continuous cardiac monitoring).

2. **Confirm diagnosis with thick and thin blood smears AND rapid diagnostic test (RDT)** simultaneously. Smear: parasitemia %, species identification, morphology. RDT detects HRP-2 antigen (P. falciparum). If initial smear negative and clinical suspicion high, repeat every 12-24 hours for 72 hours.

3. **Glucose every 1 hour** — hypoglycemia is common (>50% in children) and worsens coma independently of malaria. Treat with dextrose 0.5 g/kg IV (1 mL/kg D50W or 5 mL/kg D10W). Hypoglycemia is further potentiated by IV quinine/quinidine.

4. **Treat seizures** — benzodiazepines for active seizures (lorazepam 0.1 mg/kg IV, max 4 mg per dose). Phenobarbital prophylaxis for children with high seizure burden (controversial — increases respiratory mortality; use only with airway backup).

5. **Manage elevated ICP** — elevate head of bed to 30 degrees. Avoid hypotonic fluids. Mannitol 0.5-1 g/kg IV for clinical herniation signs; evidence base weak for routine use. Do NOT give dexamethasone (increases coma duration and GI bleeding; prospective RCT showed harm).

6. **Assess for exchange transfusion** — consider if parasitemia >10% with clinical deterioration, or >30% regardless. No RCT data; case series suggest benefit. Consult hematology and CDC for guidance.

7. **Treat fever aggressively** — high temperatures worsen neuronal injury. Acetaminophen 15 mg/kg IV/PO, cooling blankets; avoid NSAIDs (thrombocytopenia and renal dysfunction).

8. **Contact CDC Malaria Hotline (770-488-7788)** for IV artesunate access, dosing guidance, and exchange transfusion consultation.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Bacterial meningitis | Meningismus, CSF pleocytosis, no parasites on smear |
| Viral encephalitis | CSF lymphocytosis, specific viral PCR, no parasitemia |
| Typhoid fever with encephalopathy | Rose spots, positive blood/stool culture for Salmonella typhi, lower fever pattern |
| Septic shock with encephalopathy | Source-directed findings, no parasitemia, cultures positive |
| Hypoglycemia (non-malaria) | Rapid glucose reversal, no parasitemia — check glucose first |
| Status epilepticus | Resolves with antiepileptics; check smear in travelers |
| Viral hemorrhagic fever | Additional hemorrhagic features, travel to VHF-endemic areas, specific ELISA |
| African trypanosomiasis | Lymphadenopathy (Winterbottom sign), trypanosomes on blood smear |

## Workup

**Emergency Labs:**
- **Thick and thin blood smears** — stat, read by experienced microscopist. Report parasitemia percentage and species.
- **Rapid diagnostic test (RDT)** — HRP-2 antigen test for P. falciparum (high sensitivity for falciparum; some false negatives with gene deletions)
- Blood glucose (point-of-care, immediately)
- CBC — hemolytic anemia, thrombocytopenia (nearly universal)
- Metabolic panel — creatinine, bicarbonate, BUN (renal failure common)
- LFTs — elevated bilirubin (hemolysis), transaminases
- Lactate — elevated in severe disease; guides resuscitation
- Coagulation panel (PT, PTT, fibrinogen, D-dimer) — DIC screen
- Blood cultures — co-infection with bacteremia in pediatric cerebral malaria
- Urinalysis — hemoglobinuria (black urine = poor prognostic sign)
- Blood type and screen — if exchange transfusion being considered

**Imaging:**
- CT head without contrast — rule out space-occupying lesion before LP if signs of elevated ICP (papilledema, posturing, midline shift risk). MRI more sensitive but do not delay treatment.
- Chest X-ray — pulmonary edema (ARDS) in severe falciparum

**Lumbar Puncture:**
- Consider after CT if bacterial meningitis cannot be excluded. CSF in cerebral malaria: typically clear, modest protein elevation, normal glucose (relative), minimal pleocytosis. LP can confirm or exclude bacterial meningitis.

**Monitoring:**
- Continuous cardiac monitoring if using quinidine (QTc prolongation, ventricular arrhythmia)
- Glucose every 60 minutes during IV quinine/quinidine or in hypoglycemic patient
- Serial parasitemia every 12-24 hours until <1%

## Treatment

**Antimalaria Therapy:**

*IV Artesunate (first-line for severe/cerebral malaria):*
- 2.4 mg/kg IV at 0, 12, and 24 hours, then every 24 hours
- Continue until patient can tolerate oral therapy, then complete full oral course with artemisinin combination therapy (ACT): artemether-lumefantrine (Coartem) 4 tablets PO twice daily x 3 days (adult ≥35 kg) OR atovaquone-proguanil (Malarone) 4 adult tablets daily x 3 days
- Artesunate superiority over quinine: 39% reduction in mortality in African children (AQUAMAT), 35% in Southeast Asian adults (SEAQUAMAT)
- Post-artesunate delayed hemolysis (PADH): monitor CBC weekly for 4 weeks after high parasitemia treatment

*If artesunate unavailable:*
- IV quinidine gluconate 10 mg/kg (max 600 mg) in 250 mL NS over 1-2 hours, then 0.02 mg/kg/min continuous infusion
- Add doxycycline 100 mg IV/PO twice daily (or clindamycin 10 mg/kg loading then 5 mg/kg q8h for pregnant patients)
- Continuous cardiac monitoring for QTc prolongation and hypotension

**Supportive Care:**

*Hypoglycemia:*
- D50W 1 mL/kg IV (or D10W 5 mL/kg) for glucose <60 mg/dL or symptomatic
- Continuous dextrose infusion (D10W at maintenance) during quinine/quinidine treatment

*Anemia:*
- Packed RBC transfusion if Hgb <7 g/dL (or <10 g/dL with respiratory compromise or impaired consciousness) using leukoreduced, CMV-negative blood if available

*Fluid Management:*
- Cautious fluid resuscitation — adults with cerebral malaria are prone to pulmonary edema with aggressive fluids
- Pediatric exception: fluid bolus for circulatory compromise (10-20 mL/kg NS), but FEAST trial showed harm with large boluses in febrile African children — titrate carefully

*Seizure Management:*
- Lorazepam 0.1 mg/kg IV (max 4 mg) or diazepam 0.3 mg/kg IV (max 10 mg) for active seizures
- Rectal diazepam 0.5 mg/kg if no IV access (prehospital/resource-limited)

*Antipyretics:*
- Acetaminophen 15 mg/kg (max 1g) IV or PO q6h; passive and active cooling

**Do NOT administer:**
- Corticosteroids (dexamethasone, hydrocortisone) — prospective RCT demonstrated increased mortality and GI bleeding
- Antipyretics with NSAID mechanism in thrombocytopenic patients (platelet <50,000)
- Hypotonic fluids (exacerbate cerebral edema)

## Disposition

**All cerebral malaria patients: ICU admission.**

**ICU-level care required:**
- All patients with impaired consciousness (GCS <11)
- Seizures or posturing
- Parasitemia >5%
- Respiratory distress, pulmonary edema
- Renal failure, severe acidosis, hypoglycemia requiring infusion
- Hemodynamic instability

**Isolation:** Standard precautions. Malaria is NOT transmitted person-to-person in hospital settings; no airborne/droplet precautions required. Notify infection control per institutional protocol.

**Subspecialty Consults:**
- Infectious disease (primary management partner)
- Neurology (seizure management, neuro-monitoring)
- Nephrology if AKI (dialysis for severe renal failure)
- Hematology/blood bank if exchange transfusion considered
- CDC Malaria Hotline for artesunate access and complex management

**Prognosis:**
- Mortality with IV artesunate: 15-25% in adults, 10-15% in children (Africa)
- Neurological sequelae in surviving pediatric patients: ~25% (cognitive impairment, epilepsy, behavioral disorders)
- Survivors should complete full oral ACT course and undergo ophthalmologic evaluation (retinal changes)

## Pitfalls

1. **Waiting for specialist before starting IV artesunate.** Every hour of delay increases mortality. IV artesunate must start the moment the diagnosis is suspected in an obtunded returning traveler. Call the CDC hotline (770-488-7788) simultaneously — they can facilitate drug access and provide guidance while you treat.

2. **Relying on a single negative blood smear to exclude malaria.** Parasitemia in early cerebral malaria can be low and missed by a single read. Repeat smears every 12-24 hours for 72 hours if clinical suspicion persists. Use RDT in parallel; neither test alone is sufficient.

3. **Administering corticosteroids.** The instinct to treat cerebral edema with dexamethasone is wrong for cerebral malaria. The 1982 Warrell RCT (NEJM) showed dexamethasone increased coma duration and GI bleeding with no survival benefit. Do not give steroids.

4. **Missing hypoglycemia as a contributor to coma.** Glucose must be checked immediately and rechecked every 60 minutes during IV quinine/quinidine therapy. A patient in malarial coma may have a glucose of 20 mg/dL. Treat hypoglycemia even if parasitemia is being treated — hypoglycemia causes independent neuronal injury.

5. **Undertreating fever.** Fever is not just a symptom — high temperatures worsen neurological injury and prolong coma duration. Aggressive antipyresis with acetaminophen and physical cooling measures is a specific treatment, not comfort care.

6. **Not completing oral ACT after IV artesunate.** IV artesunate rapidly clears parasitemia but must be followed by a full 3-day oral ACT course for definitive cure. Failure to complete oral therapy leads to recrudescence.

7. **Using quinidine without cardiac monitoring.** IV quinidine causes QTc prolongation and can precipitate torsades de pointes. Continuous telemetry and QTc monitoring every 8 hours is mandatory. Stop quinidine if QTc >600 ms or QRS widens >50%.