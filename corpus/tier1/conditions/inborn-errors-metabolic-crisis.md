---
id: inborn-errors-metabolic-crisis
condition: "Inborn Errors of Metabolism \u2014 Acute Crisis"
aliases: [IEM crisis, metabolic crisis, inborn metabolic emergency, urea cycle crisis, organic acidemia crisis]
icd10: [E72.20, E71.118, E71.120, E72.4, E74.04]
esi: 1
time_to_harm:
  irreversible_injury: "< 4 hours (cerebral edema in urea cycle defects; irreversible neurological damage)"
  death: "< 12 hours without emergent intervention in neonatal-onset disease"
  optimal_intervention_window: "< 2 hours from presentation — stop catabolism, start anabolism"
category: pediatric
track: tier1
sources:
  - type: review
    ref: "Saudubray JM, Sedel F, Walter JH. Clinical approach to treatable inborn metabolic diseases: an introduction. J Inherit Metab Dis. 2006;29(2-3):261-274."
    pmid: "16763886"
  - type: guideline
    ref: "Häberle J et al. Suggested guidelines for the diagnosis and management of urea cycle disorders: first revision. J Inherit Metab Dis. 2019;42(6):1192-1230."
    pmid: "30982989"
  - type: pubmed
    ref: "Enns GM et al. Survival after treatment with phenylacetate and benzoate for urea-cycle disorders. N Engl J Med. 2007;356(22):2282-2292."
    pmid: "17538087"
  - type: review
    ref: "Chakrapani A et al. Metabolic emergencies in the pediatric emergency department. Emerg Med Clin North Am. 2018;36(2):427-446."
  - type: guideline
    ref: "British Inherited Metabolic Disease Group (BIMDG). Emergency guidelines for inherited metabolic diseases. 2021."
    url: "https://www.bimdg.org.uk"
last_updated: "2026-02-26"
compiled_by: agent
risk_tier: A
confusion_pairs:
  - condition: sepsis
    differentiators:
      - "IEM crisis often has no infectious source"
      - "Hyperammonemia > 200 mcmol/L in neonate strongly suggests IEM"
      - "Family history of consanguinity or unexplained neonatal deaths"
  - condition: diabetic-ketoacidosis
    differentiators:
      - "IEM organic acidemias cause ketoacidosis without hyperglycemia"
      - "Neonatal or infant age group vs typical DKA in older children"
      - "Specific organic acid profile on urine organic acids"
validation:
  schema_version: "2.0"
  automated_consistency_check: null
  dose_range_validator: null
  unit_normalization_check: null
  cross_file_consistency_check: null
  citation_presence_check: null
  duplicate_content_check: null
  outlier_detection_flag: clear
  guideline_version_reference: null
  provenance_links: []
---
# Inborn Errors of Metabolism — Acute Crisis

## Recognition

**Definition:** Inborn errors of metabolism (IEM) are inherited enzyme deficiencies that cause acute metabolic decompensation when catabolic stress overwhelms residual enzyme capacity. Acute crises present as encephalopathy, metabolic acidosis, hyperammonemia, or hypoglycemia — often indistinguishable from sepsis until specific labs return.

**Major IEM Categories Presenting as Emergencies:**

| Category | Examples | Key Metabolite |
|----------|----------|----------------|
| **Urea cycle defects** | OTC deficiency, citrullinemia, argininosuccinic aciduria | Hyperammonemia (NH3 > 150 mcmol/L) |
| **Organic acidemias** | Methylmalonic acidemia, propionic acidemia, isovaleric acidemia | Metabolic acidosis with elevated anion gap, ketosis |
| **Maple syrup urine disease** | MSUD | Leucine elevation, sweet/burnt sugar urine odor |
| **Fatty acid oxidation defects** | MCAD, VLCAD, LCHAD | Hypoketotic hypoglycemia, cardiomyopathy |
| **Glycogen storage disease** | GSD type I (von Gierke) | Severe hypoglycemia, lactic acidosis, hepatomegaly |

**Triggers for Acute Decompensation:**
- Intercurrent illness (URI, gastroenteritis)
- Fasting or poor oral intake
- Surgery, anesthesia, physiologic stress
- High-protein meal (urea cycle defects, organic acidemias)
- Newborn transition (cessation of placental clearance)

**Red Flags for IEM in Neonates/Infants:**

| Finding | Significance |
|---------|-------------|
| **Encephalopathy in a previously well neonate (day 2-5)** | Classic timing for urea cycle defects and organic acidemias |
| **Metabolic acidosis with elevated anion gap** | Organic acidemias, MSUD, mitochondrial disease |
| **Hyperammonemia > 150 mcmol/L** | Urea cycle defect until proven otherwise |
| **Hypoketotic hypoglycemia** | Fatty acid oxidation defect |
| **Unusual odor** | MSUD (maple syrup), isovaleric acidemia (sweaty feet), glutaric aciduria (sweaty) |
| **Consanguinity or unexplained sibling deaths** | Strongly increases IEM probability |
| **Reye-like syndrome in infant** | Fatty acid oxidation defect or urea cycle defect |

## Critical Actions

1. **Stop catabolism immediately.** Start D10 0.45NS at 1.5x maintenance rate IV. Goal: provide glucose delivery of 8-10 mg/kg/min in neonates, 5-8 mg/kg/min in older children. Add insulin 0.05-0.1 units/kg/hr IV if glucose > 200 mg/dL on high dextrose infusion (promotes anabolism).

2. **Stop all protein intake.** NPO for protein for 24-48 hours maximum during acute crisis. Protein restriction is temporary — prolonged protein deprivation causes endogenous catabolism and worsens hyperammonemia.

3. **Draw critical labs BEFORE treatment.** Blood: ammonia (on ice, processed within 15 minutes), blood gas, glucose, lactate, electrolytes, LFTs, uric acid, acylcarnitine profile, amino acids. Urine: organic acids, ketones, reducing substances. These samples are irreplaceable — they define the diagnosis.

4. **Treat hyperammonemia aggressively.** If NH3 > 200 mcmol/L: sodium benzoate 250 mg/kg IV loading dose over 90 minutes, then 250 mg/kg/day continuous infusion + sodium phenylacetate 250 mg/kg IV loading dose over 90 minutes, then 250 mg/kg/day continuous infusion (available as Ammonul). If NH3 > 500 mcmol/L or rising despite medical therapy: emergent hemodialysis (not peritoneal dialysis — too slow for ammonia clearance).

5. **Correct metabolic acidosis.** Sodium bicarbonate 1-2 mEq/kg IV over 30-60 minutes if pH < 7.1 or bicarbonate < 10 mEq/L. Do not fully correct — target pH > 7.2. Excessive alkalization worsens ammonia toxicity (shifts NH4+ to lipid-soluble NH3 which crosses blood-brain barrier).

6. **L-carnitine 100 mg/kg IV loading dose (max 6 g), then 50 mg/kg/day divided q6h.** Replenishes carnitine stores depleted by organic acid conjugation. Indicated in all organic acidemias and suspected fatty acid oxidation defects.

7. **Contact metabolic specialist immediately.** IEM management requires subspecialist guidance for specific cofactor therapy, dietary management, and dialysis decisions. If no metabolic specialist on site, call the nearest children's hospital metabolic team.

8. **Treat concurrent sepsis empirically.** IEM crises are frequently triggered by infection and are clinically indistinguishable from sepsis. Start ampicillin + gentamicin (neonates) or ceftriaxone (older infants/children) after blood cultures.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **Neonatal sepsis** | Positive blood cultures, maternal risk factors; ammonia typically < 150 mcmol/L; no specific organic acid pattern |
| **Diabetic ketoacidosis** | Hyperglycemia present; typically older children; no hyperammonemia |
| **Non-accidental trauma** | Subdural hematoma, retinal hemorrhages; may co-present with metabolic derangement — always check ammonia and organic acids |
| **Pyloric stenosis** | Hypochloremic metabolic alkalosis (not acidosis); projectile non-bilious vomiting at 3-6 weeks |
| **Congenital adrenal hyperplasia** | Ambiguous genitalia, hyperkalemia, hyponatremia; 17-hydroxyprogesterone elevated on newborn screen |
| **Intussusception** | Intermittent colicky pain, bloody stool; no metabolic acidosis or hyperammonemia |
| **Hepatic failure** | Elevated transaminases and coagulopathy predominate; may have secondary hyperammonemia but typically < 200 mcmol/L |

## Workup

**Immediate Labs (BEFORE any treatment):**
- Ammonia (collect on ice, analyze within 15 min — free-flowing venous, no tourniquet/crying)
- Blood gas with lactate
- Glucose (bedside + serum)
- BMP (anion gap calculation)
- LFTs, uric acid, CK
- CBC with differential
- Coagulation studies (PT/INR, fibrinogen)
- Blood culture

**Metabolic Workup (send before treatment, results guide long-term management):**
- Plasma amino acids
- Plasma acylcarnitine profile
- Urine organic acids
- Urine ketones and reducing substances
- Total and free carnitine

**Interpretation Patterns:**

| Pattern | Likely IEM Category |
|---------|-------------------|
| NH3 > 200, normal AG, respiratory alkalosis | Urea cycle defect |
| NH3 elevated, AG metabolic acidosis, ketonuria | Organic acidemia |
| Hypoketotic hypoglycemia, elevated acylcarnitines | Fatty acid oxidation defect |
| AG acidosis, ketosis, sweet odor, leucine elevated | MSUD |
| Severe hypoglycemia, lactic acidosis, hepatomegaly | GSD type I |

**Imaging:**
- Head CT/MRI if encephalopathic (evaluate for cerebral edema — common in hyperammonemia)
- No specific imaging diagnostic for IEM

## Treatment

**Phase 1: Stop Catabolism (0-2 hours)**
- D10 0.45NS at 1.5x maintenance IV
- NPO for protein
- L-carnitine 100 mg/kg IV load
- Ammonia scavengers if NH3 > 150 mcmol/L (sodium benzoate + sodium phenylacetate as above)

**Phase 2: Specific Therapy (guided by metabolic specialist)**
- **Urea cycle defects:** Arginine HCl 200-600 mg/kg/day IV (except arginase deficiency). Nitrogen scavengers. Emergent hemodialysis for NH3 > 500 or rising despite medical therapy.
- **Organic acidemias:** L-carnitine, biotin 10 mg/day PO/IV (for holocarboxylase synthetase deficiency), hydroxocobalamin 1 mg IM (for methylmalonic acidemia — diagnostic and therapeutic).
- **MSUD:** Thiamine 100 mg IV (responsive variants). BCAA-free formula when feeds resume. Dialysis for leucine > 1500 mcmol/L.
- **Fatty acid oxidation defects:** Avoid fasting. D10 to maintain glucose > 70 mg/dL. Medium-chain triglyceride oil supplementation for LCHAD/VLCAD. Avoid carnitine supplementation in carnitine palmitoyltransferase II deficiency (controversial).
- **GSD type I:** Continuous glucose infusion, uncooked cornstarch when stable (1.5-2.5 g/kg q4-6h).

**Cerebral Edema Management (hyperammonemia):**
- Hypertonic saline 3% 5 mL/kg IV over 10-15 minutes for clinical herniation
- Head of bed elevation 30 degrees
- Avoid hyperventilation (worsens ammonia diffusion into CNS)

## Disposition

**All IEM in acute crisis require PICU admission** at a facility with:
- Pediatric metabolic specialist (on-site or telemedicine)
- Hemodialysis capability (for neonates: continuous venovenous hemodiafiltration)
- NICU if neonatal age

**Transfer Criteria:**
- Any hyperammonemia > 150 mcmol/L in neonate
- Any metabolic encephalopathy with suspected IEM
- Need for hemodialysis not available at referring facility
- Stabilize glucose, start ammonia scavengers, and secure airway before transport

## Pitfalls

1. **Attributing neonatal encephalopathy to sepsis without checking an ammonia level.** A well-appearing neonate who deteriorates on day 2-5 of life with lethargy, poor feeding, and respiratory alkalosis has a urea cycle defect until proven otherwise. Ammonia must be part of the initial workup for any encephalopathic neonate — it is not part of a standard BMP. Delay in diagnosis of hyperammonemia by 12 hours correlates with irreversible neurological damage.

2. **Misinterpreting a "normal" ammonia level drawn incorrectly.** Ammonia samples must be collected on ice, from a free-flowing venous draw (no tourniquet, no fist clenching), and analyzed within 15 minutes. A room-temperature sample transported slowly will have a falsely elevated level. A hemolyzed sample may be falsely low. If clinical suspicion is high, repeat the level with proper technique.

3. **Overcorrecting metabolic acidosis with bicarbonate in hyperammonemia.** Alkalinization shifts ammonium (NH4+, charged, cannot cross BBB) to ammonia (NH3, lipid-soluble, crosses BBB freely). In urea cycle defects, aggressive bicarbonate correction accelerates cerebral ammonia toxicity. Target pH > 7.2, not normalization.

4. **Prolonged protein restriction causing worsening hyperammonemia.** Protein-free parenteral nutrition is a temporizing measure (24-48 hours maximum). After this window, the absence of dietary protein forces endogenous protein catabolism, which generates ammonia. Protein must be reintroduced at minimum safe intake (0.5-1 g/kg/day) under metabolic specialist guidance.

5. **Choosing peritoneal dialysis for ammonia clearance.** Peritoneal dialysis clears ammonia at approximately 10% the rate of hemodialysis. For neonatal hyperammonemia > 500 mcmol/L, continuous venovenous hemodiafiltration (CVVHDF) is the modality of choice. Peritoneal dialysis delays definitive ammonia removal and allows ongoing neurological injury.
