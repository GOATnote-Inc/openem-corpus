---
id: toxic-alcohol-ingestion
condition: Toxic Alcohol Ingestion
aliases: [methanol poisoning, ethylene glycol poisoning, toxic alcohol poisoning, methanol ingestion, ethylene glycol ingestion, antifreeze poisoning]
icd10: [T51.1X1A, T51.1X4A, T52.3X1A, T52.3X4A, T51.8X1A]
esi: 1
time_to_harm: "< 6-12 hours"
mortality_if_delayed: "Methanol: 20-50% mortality if untreated; Ethylene glycol: 80-90% mortality if untreated"
category: toxicologic
track: tier1
sources:
  - type: guideline
    ref: "AACT/EAPCCT Position Statement: Treatment of Methanol Poisoning. J Toxicol Clin Toxicol 2002;40(4):415-46"
    pmid: "12216995"
  - type: guideline
    ref: "AACT/EAPCCT Position Statement: Treatment of Ethylene Glycol Poisoning. J Toxicol Clin Toxicol 1999;37(5):537-60"
    pmid: "10497633"
  - type: pubmed
    ref: "Brent J et al. Fomepizole for the treatment of methanol poisoning. N Engl J Med 2001;344(6):424-9"
    pmid: "11172179"
  - type: pubmed
    ref: "Brent J et al. Fomepizole for the treatment of ethylene glycol poisoning. N Engl J Med 1999;340(11):832-8"
    pmid: "10080845"
  - type: review
    ref: "Kraut JA, Kurtz I. Toxic alcohol ingestions: clinical features, diagnosis, and management. Clin J Am Soc Nephrol 2008;3(1):208-25"
    pmid: "18045860"
  - type: review
    ref: "Barceloux DG et al. American Academy of Clinical Toxicology practice guidelines on the treatment of methanol poisoning. J Toxicol Clin Toxicol 2002;40(4):415-46"
    pmid: "12216995"
last_updated: "2026-02-18"
compiled_by: agent
risk_tier: A
validation:
  automated_consistency_check: "2026-02-18"
  dose_range_validator: "2026-02-19"
  unit_normalization_check: "2026-02-19"
  cross_file_consistency_check: "2026-02-19"
  citation_presence_check: "2026-02-19"
  duplicate_content_check: "2026-02-19"
  outlier_detection_flag: clear
  schema_version: "2.0"
  guideline_version_reference: null
  provenance_links: []
---
# Toxic Alcohol Ingestion

## Recognition

**The two major toxic alcohols:**
- **Methanol** (wood alcohol, windshield washer fluid, moonshine, industrial solvents)
- **Ethylene glycol** (antifreeze, coolant, brake fluid, industrial solvents)

Both are metabolized by alcohol dehydrogenase (ADH) to toxic metabolites. **The parent compounds are relatively non-toxic — the metabolites cause organ damage.**

**Methanol Toxicity Pathway:**
Methanol → (ADH) → formaldehyde → (aldehyde dehydrogenase) → **formic acid** → retinal toxicity, basal ganglia necrosis, death

**Ethylene Glycol Toxicity Pathway:**
Ethylene glycol → (ADH) → glycoaldehyde → glycolic acid → glyoxylic acid → **oxalic acid** → calcium oxalate crystals → renal tubular obstruction → renal failure

**Clinical Phases:**

*Methanol:*
- 0-12 hours: CNS depression (similar to ethanol intoxication), GI symptoms (nausea, vomiting, abdominal pain)
- 12-24 hours: visual disturbances (blurred vision, "snowfield" visual field, decreased acuity, afferent pupillary defect, blindness), severe metabolic acidosis
- >24 hours: seizures, coma, basal ganglia hemorrhagic necrosis on CT/MRI, death

*Ethylene glycol:*
- 0-12 hours: CNS depression, inebriation without alcohol odor, nausea, vomiting
- 12-24 hours: cardiopulmonary phase — tachycardia, hypertension, pulmonary edema, ARDS, hypocalcemia (calcium chelated by oxalate)
- 24-72 hours: renal failure — oliguria, flank pain, hematuria, calcium oxalate crystalluria

**Key Laboratory Findings:**
- **Elevated osmolar gap** (early, before metabolism) — calculated: 2(Na) + BUN/2.8 + Glucose/18 + EtOH/4.6. Measured serum osmolality - calculated osmolality. Normal <10 mOsm/kg. Elevated osmolar gap = unmetabolized parent compound present.
- **Anion gap metabolic acidosis** (later, after metabolism to acid metabolites) — AG = Na - (Cl + HCO3). Normal 8-12. Elevated AG indicates toxic metabolite accumulation.
- **Osmolar gap may normalize as anion gap rises** (parent compound is metabolized to acidic metabolites). A normal osmolar gap does NOT exclude toxic alcohol if sufficient time has passed.
- **Elevated lactate** — glycolic acid (ethylene glycol metabolite) cross-reacts with some lactate assays, producing a falsely elevated point-of-care lactate. A large gap between POC lactate and lab lactate suggests ethylene glycol.
- **Calcium oxalate crystals in urine** — pathognomonic for ethylene glycol (monohydrate = needle-shaped, dihydrate = envelope-shaped). Absence does not exclude diagnosis.
- **Hypocalcemia** — ethylene glycol; ionized calcium may be critically low → seizures, QT prolongation.

## Critical Actions

1. **Fomepizole 15 mg/kg IV loading dose** as first-line ADH inhibitor. Must be given **BEFORE acidosis develops** for best outcomes. Give empirically if clinical suspicion exists — do not wait for confirmatory levels.
2. **Draw simultaneous serum osmolality (measured, by freezing point depression) and BMP** to calculate osmolar gap and anion gap. Send toxic alcohol levels (methanol, ethylene glycol) but do NOT wait for results to treat.
3. **ABG/VBG** — assess pH and severity of acidosis. pH <7.25 is an indication for hemodialysis.
4. **Poison Control consultation** (1-800-222-1222) and/or medical toxicology consultation.
5. **Hemodialysis** — start emergently if any of: pH <7.25, renal failure, visual changes (methanol), serum toxic alcohol level >50 mg/dL, clinical deterioration despite fomepizole.
6. **Sodium bicarbonate** — for pH <7.1, give 1-2 mEq/kg IV bolus, then infusion (150 mEq in 1 L D5W). Maintain pH >7.2 to reduce formic acid penetration into tissues (methanol) and oxalic acid crystallization (ethylene glycol).
7. **Cofactor therapy** — begin immediately:
   - Methanol: **folinic acid (leucovorin) 50 mg IV q6h** (enhances formic acid metabolism to CO2 and water). Folic acid 50 mg IV q6h is an alternative if folinic acid unavailable.
   - Ethylene glycol: **thiamine 100 mg IV** + **pyridoxine 50 mg IV** (both q6h — shunt glyoxylic acid metabolism to non-toxic metabolites)
8. **Check ionized calcium** in ethylene glycol ingestion. Treat symptomatic hypocalcemia with calcium gluconate 3 g IV (or calcium chloride 1 g IV via central line).
9. **Correct hypomagnesemia** — magnesium is a cofactor for thiamine-dependent enzymes.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Ethanol intoxication | Elevated ethanol level, no osmolar gap (after accounting for ethanol), no anion gap acidosis |
| Diabetic ketoacidosis | Hyperglycemia, ketonuria/ketonemia, known diabetes, no elevated osmolar gap |
| Lactic acidosis (sepsis, shock, metformin) | Elevated lactate (true elevation), identifiable source, no osmolar gap |
| Isopropanol ingestion | Elevated osmolar gap, ketonemia/ketonuria (acetone), NO metabolic acidosis (non-toxic metabolite). Sweet breath. |
| Uremic acidosis | Elevated BUN/creatinine, chronic kidney disease history, no osmolar gap |
| Salicylate toxicity | Mixed respiratory alkalosis and metabolic acidosis, tinnitus, elevated salicylate level |
| Alcoholic ketoacidosis | History of chronic alcohol use, recent binge then cessation, mild acidosis, ketonemia, low-normal glucose |
| Propylene glycol toxicity | IV lorazepam/phenobarbital infusions, elevated osmolar gap, lactic acidosis |

## Workup

**Stat Labs:**
- BMP — calculate anion gap (Na - [Cl + HCO3]), glucose, BUN, creatinine, potassium
- Serum osmolality (MEASURED, by freezing point depression — NOT calculated). Must be freezing point depression method; vapor pressure method does not detect volatile alcohols.
- ABG or VBG — pH, pCO2, bicarbonate
- Serum ethanol level — must account for ethanol contribution to osmolar gap
- Serum methanol and ethylene glycol levels — send STAT but results often delayed 4-8 hours. Do NOT wait for levels to initiate treatment.
- Lactate — true lactate vs glycolic acid cross-reactivity artifact
- Ionized calcium — critically important in ethylene glycol
- CK — rhabdomyolysis
- Serum ketones — positive in isopropanol (acetone), may be mildly positive in starvation/AKA
- LFTs, lipase — co-ingestion evaluation
- Coagulation studies
- Urinalysis with microscopy — calcium oxalate crystals (ethylene glycol), urine fluorescence under Wood's lamp (unreliable but some antifreeze contains fluorescein)

**Osmolar Gap Calculation:**
Calculated osmolality = 2(Na) + BUN/2.8 + Glucose/18 + EtOH/4.6
Osmolar gap = Measured osmolality - Calculated osmolality
- Normal: <10 mOsm/kg
- Gap >10: suggests unmeasured osmoles (toxic alcohol, propylene glycol, contrast media, mannitol)
- **Normal osmolar gap does NOT exclude toxic alcohol** if sufficient time has elapsed for metabolism

**Imaging:**
- CT head — if altered mental status or concern for co-ingestion/trauma. Methanol causes basal ganglia hemorrhagic necrosis (putaminal hemorrhage) visible on CT/MRI.
- CXR — if concern for aspiration or pulmonary edema (ethylene glycol cardiopulmonary phase)

**ECG:**
- QTc prolongation from hypocalcemia (ethylene glycol)
- Dysrhythmia screening

## Treatment

**ADH Inhibition (First-Line: Fomepizole):**
- **Fomepizole (Antizol) 15 mg/kg IV loading dose** over 30 minutes
- Then 10 mg/kg IV q12h for 4 doses
- Then 15 mg/kg IV q12h until methanol/ethylene glycol level <20 mg/dL and patient asymptomatic with normal pH
- During hemodialysis: increase fomepizole frequency to q4h (dialyzable)
- Give BEFORE acidosis develops — once toxic metabolites have formed, organ damage is underway

**ADH Inhibition (Alternative: Ethanol):**
- Use ONLY if fomepizole unavailable
- Loading dose: ethanol 10% IV solution at 7.6 mL/kg (0.8 g/kg) over 30-60 min; OR 50 mL of 40% ethanol PO (if patient can swallow and protect airway)
- Maintenance: ethanol infusion titrated to target serum ethanol 100-150 mg/dL
- During hemodialysis: double the ethanol infusion rate (dialyzable)
- Monitor serum ethanol level q1-2h — significant risk of hypoglycemia, CNS depression, aspiration
- Far more difficult to manage than fomepizole; fomepizole is strongly preferred

**Hemodialysis Indications (any ONE):**
- pH <7.25 despite bicarbonate therapy
- Renal failure (oliguric or creatinine rising)
- Visual changes or blindness (methanol)
- Serum methanol or ethylene glycol level >50 mg/dL
- Severe or worsening metabolic acidosis despite fomepizole
- Clinical deterioration despite treatment
- Electrolyte abnormalities refractory to medical management

**Cofactor Therapy:**

*Methanol:*
- Folinic acid (leucovorin) 50 mg IV q6h (preferred) — enhances formate metabolism
- If folinic acid unavailable: folic acid 50 mg IV q6h
- Continue for 24-48 hours or until methanol level undetectable and acidosis resolved

*Ethylene glycol:*
- Thiamine 100 mg IV q6h — shunts glyoxylic acid to alpha-hydroxy-beta-ketoadipic acid
- Pyridoxine (vitamin B6) 50 mg IV q6h — shunts glyoxylic acid to glycine
- Continue for 24-48 hours or until ethylene glycol level undetectable

**Metabolic Acidosis Management:**
- Sodium bicarbonate 1-2 mEq/kg IV bolus for pH <7.1
- Bicarbonate infusion: 150 mEq NaHCO3 in 1 L D5W at 150-200 mL/hr
- Target pH >7.2 (reduces CNS penetration of formic acid, reduces oxalate crystallization)
- Monitor potassium closely (bicarbonate drives potassium intracellularly)

**Hypocalcemia (Ethylene Glycol):**
- Calcium gluconate 3 g (30 mL of 10%) IV over 10-20 min for symptomatic hypocalcemia (seizures, QT prolongation, tetany)
- Calcium chloride 1 g IV via central line for severe symptomatic hypocalcemia
- Do NOT correct asymptomatic hypocalcemia aggressively — exogenous calcium may increase calcium oxalate precipitation in renal tubules

**Seizure Management:**
- Benzodiazepines first-line: lorazepam 4 mg IV or diazepam 10 mg IV
- Check ionized calcium — seizures may be from hypocalcemia requiring calcium repletion

## Disposition

**ICU Admission (all confirmed toxic alcohol ingestions):**
- Any patient requiring fomepizole, ethanol drip, or hemodialysis
- Metabolic acidosis
- Altered mental status
- Visual changes (methanol)
- Renal failure (ethylene glycol)
- Hemodynamic instability

**Hemodialysis Unit/ICU:**
- Continue dialysis until: toxic alcohol level <20 mg/dL, pH normalized, symptoms resolving, osmolar gap <10

**Observation:**
- Accidental minimal exposure with normal labs (osmolar gap <10, normal pH, no anion gap), asymptomatic — observe 6-8 hours with repeat labs at 4 hours

**Discharge Criteria (rare in confirmed ingestion):**
- Asymptomatic exposure with serial normal labs over 6-8 hours
- Psychiatric evaluation before discharge for intentional ingestion
- Poison control follow-up arranged

**Ophthalmology Consultation:**
- All methanol ingestions — fundoscopic exam for optic disc hyperemia/edema
- Serial visual acuity monitoring

**Nephrology Consultation:**
- All cases requiring or potentially requiring hemodialysis
- Ethylene glycol with renal failure — may need prolonged or repeated dialysis

## Pitfalls

1. **Waiting for toxic alcohol levels to start fomepizole.** Serum methanol and ethylene glycol levels take 4-8 hours at most hospitals. Fomepizole must be given on clinical suspicion (osmolar gap, anion gap acidosis, history of ingestion, inebriation without ethanol). By the time levels return, irreversible organ damage has occurred.

2. **Interpreting a normal osmolar gap as excluding toxic alcohol.** The osmolar gap reflects the unmetabolized parent compound. Once the toxic alcohol is fully metabolized to acidic byproducts, the osmolar gap normalizes while the anion gap rises. Late presentations have a normal osmolar gap and a massive anion gap — this is MORE dangerous, not less.

3. **Relying on urine fluorescence to detect ethylene glycol.** Some antifreeze brands contain fluorescein, but many do not, and the test has poor sensitivity and specificity. Absence of urine fluorescence does not exclude ethylene glycol ingestion.

4. **Aggressively correcting asymptomatic hypocalcemia in ethylene glycol poisoning.** Exogenous calcium increases calcium oxalate deposition in renal tubules. Treat symptomatic hypocalcemia (seizures, QT prolongation, tetany) but do not normalize an asymptomatically low ionized calcium.

5. **Using ethanol drip without monitoring serum ethanol levels q1-2h.** Ethanol pharmacokinetics are unpredictable, especially in chronic drinkers. Subtherapeutic levels allow toxic metabolism to continue; supratherapeutic levels cause aspiration, hypoglycemia, and CNS depression. Fomepizole is the preferred agent specifically because it avoids this problem.

6. **Forgetting cofactor therapy.** Folinic acid (methanol) and thiamine + pyridoxine (ethylene glycol) enhance metabolism of toxic intermediates to non-toxic products. These are inexpensive, safe, and additive to ADH inhibition and dialysis. Omitting them is a missed opportunity to reduce organ damage.

7. **Not increasing fomepizole dosing frequency during hemodialysis.** Fomepizole is dialyzable. Standard q12h dosing allows toxic alcohol metabolism to resume during dialysis sessions. Dose fomepizole q4h during dialysis and give a supplemental dose after dialysis completion.

8. **Failing to recognize the POC lactate artifact in ethylene glycol.** Glycolic acid cross-reacts with L-lactate on some point-of-care analyzers, producing a falsely elevated lactate. A large discrepancy between POC lactate and central lab lactate (the "lactate gap") is a diagnostic clue for ethylene glycol ingestion.

9. **Discharging intentional ingestion without psychiatric evaluation.** Toxic alcohol ingestion as a suicide attempt carries high lethality and indicates severe psychiatric illness. Psychiatric evaluation is mandatory before discharge regardless of medical stabilization.
