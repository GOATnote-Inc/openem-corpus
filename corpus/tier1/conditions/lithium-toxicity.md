---
id: lithium-toxicity
condition: Lithium Toxicity
aliases: [lithium poisoning, lithium overdose, lithium intoxication, Li toxicity]
icd10: [T43.8X1A, T43.8X2A, T43.8X5A]
esi: 2
time_to_harm: "< 12 hours for irreversible neurologic injury in severe cases; chronic toxicity may produce insidious CNS damage over days"
mortality_if_delayed: "9% overall; up to 25% in severe chronic toxicity with delayed recognition"
category: toxicologic
track: tier1
sources:
  - type: review
    ref: "Baird-Gunning J et al. Lithium Poisoning. J Intensive Care Med 2017;32(4):249-263"
    pmid: "27516079"
  - type: pubmed
    ref: "Decker BS et al. Extracorporeal Treatment for Lithium Poisoning: Systematic Review and Recommendations from the EXTRIP Workgroup. Clin J Am Soc Nephrol 2015;10(5):875-887"
    pmid: "25583292"
  - type: review
    ref: "Waring WS. Management of lithium toxicity. Toxicol Rev 2006;25(4):221-230"
    pmid: "17288494"
  - type: review
    ref: "Timmer RT, Sands JM. Lithium intoxication. J Am Soc Nephrol 1999;10(3):666-674"
    pmid: "10073618"
  - type: meta-analysis
    ref: "McKnight RF et al. Lithium toxicity profile: a systematic review and meta-analysis. Lancet 2012;379(9817):721-728"
    pmid: "22265699"
last_updated: "2026-02-19"
compiled_by: agent
risk_tier: B
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
# Lithium Toxicity

## Recognition

**Pharmacokinetics that drive toxicity:** Lithium is a monovalent cation with no protein binding, no hepatic metabolism, and 95% renal excretion. Therapeutic index is extremely narrow (therapeutic range 0.6-1.2 mEq/L; toxicity begins at 1.5 mEq/L). Volume of distribution is 0.6-0.9 L/kg. Peak absorption occurs 1-4 hours after immediate-release formulations and 4-12 hours after sustained-release preparations. Lithium distributes slowly into the CNS -- serum levels may not reflect brain tissue concentrations, especially in acute ingestion. This explains the redistribution phenomenon: serum levels drop after initial distribution but can rebound 6-12 hours later as lithium re-equilibrates from tissues.

**Three distinct toxicity patterns (different presentations, different dangers):**

- **Acute ingestion (lithium-naive patient):** Large single ingestion in a patient not previously on lithium. GI symptoms predominate early (nausea, vomiting, diarrhea). Serum levels may be very high (>4-5 mEq/L) but neurologic toxicity is initially mild because CNS distribution has not yet occurred. Do NOT be reassured by an alert patient with a lithium level of 5 mEq/L in the first few hours. Delayed neurologic deterioration is the rule.

- **Acute-on-chronic ingestion:** Patient on chronic lithium therapy takes a supratherapeutic dose. CNS tissue already at steady-state lithium concentration, so neurologic symptoms develop earlier and at lower serum levels than in purely acute ingestion. More dangerous than acute at equivalent serum levels.

- **Chronic toxicity (most dangerous pattern):** Gradual accumulation in a patient on maintenance therapy, precipitated by decreased renal clearance (dehydration, renal insufficiency, drug interactions). Serum levels may be only mildly elevated (1.5-2.5 mEq/L) but CNS symptoms are severe because brain tissue has equilibrated. Chronic toxicity carries the highest morbidity and mortality of the three patterns. Over 50% of chronic toxicity cases develop moderate-to-severe poisoning.

**Clinical features by severity:**

- **Mild (Li 1.5-2.5 mEq/L):** Nausea, vomiting, diarrhea, fine tremor, lethargy, polyuria, polydipsia. Often mistaken for viral illness or medication side effects.
- **Moderate (Li 2.5-3.5 mEq/L):** Coarse tremor, ataxia, dysarthria, nystagmus, confusion, agitation, fasciculations, hyperreflexia, myoclonus.
- **Severe (Li >3.5 mEq/L):** Coma, seizures, hyperthermia, cardiovascular collapse, renal failure. ECG changes: T-wave flattening/inversion, QTc prolongation, sinus node dysfunction, bradycardia. SIND (syndrome of irreversible lithium-effectuated neurotoxicity) -- persistent cerebellar dysfunction, cognitive impairment, and extrapyramidal signs that may never resolve.

**These level thresholds apply to chronic toxicity. In acute ingestion, neurologic symptoms lag behind serum levels. In chronic toxicity, severe neurotoxicity can occur at levels of 1.5-2.0 mEq/L.**

**Precipitants of chronic toxicity (drug interactions and clinical states):**
- **NSAIDs** -- reduce renal prostaglandin synthesis, decrease GFR, increase lithium reabsorption in the proximal tubule. Can raise lithium levels 15-50%.
- **Thiazide diuretics** -- volume contraction increases proximal tubule sodium and lithium reabsorption. Can double lithium levels.
- **ACE inhibitors / ARBs** -- reduce GFR, especially in the setting of volume depletion. Raises lithium levels 25-35%.
- **Dehydration** (vomiting, diarrhea, reduced oral intake, fever) -- volume contraction triggers proximal tubule sodium avidity, carrying lithium with it.
- **Acute kidney injury** from any cause.
- **Advanced age** -- declining GFR with age reduces lithium clearance.

**Nephrogenic diabetes insipidus (NDI):** Chronic lithium use causes NDI in 40-50% of patients by downregulating aquaporin-2 channels in the collecting duct. Patients present with polyuria (3-5 L/day) and polydipsia. NDI creates a vicious cycle: the patient is volume-depleted at baseline, making them vulnerable to dehydration-triggered toxicity. NDI may be irreversible even after lithium discontinuation.

## Critical Actions

1. **Obtain serum lithium level immediately** on any patient on lithium therapy presenting with altered mental status, tremor, GI symptoms, or renal impairment. Also obtain on any suspected acute ingestion. Lithium is NOT included on standard toxicology screens.
2. **Determine the toxicity pattern** (acute, acute-on-chronic, or chronic) -- this changes risk stratification and management. Ask: Is the patient on chronic lithium? Was there a single large ingestion? What precipitated the presentation?
3. **Aggressive IV normal saline resuscitation** -- NS 20 mL/kg bolus, then 200-300 mL/hr. Volume repletion restores renal lithium clearance. This is the single most impactful intervention for mild-to-moderate toxicity.
4. **Serial lithium levels every 2-4 hours.** Levels can rise after initial measurement due to ongoing absorption (sustained-release formulations) and redistribution. A declining level does not mean the patient is improving if the level was drawn during distribution phase.
5. **Whole bowel irrigation (WBI) for sustained-release preparations** -- polyethylene glycol electrolyte solution (GoLYTELY) 1-2 L/hr via NGT until clear rectal effluent. Lithium is not adsorbed by activated charcoal. WBI is the only GI decontamination method with evidence in lithium ingestion.
6. **Evaluate for hemodialysis** using EXTRIP criteria (see Treatment). Early nephrology consultation for any patient with level >4 mEq/L, renal impairment, or significant neurologic symptoms.
7. **Continuous cardiac monitoring.** Lithium affects sinoatrial node function and can cause bradycardia, heart block, and QTc prolongation.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Serotonin syndrome | Clonus (especially ocular), hyperthermia, hyperreflexia, agitation. Exposure to serotonergic agents. Lithium can contribute to serotonin syndrome as a co-precipitant -- both diagnoses may coexist. |
| Neuroleptic malignant syndrome | Lead-pipe rigidity, hyperthermia, AMS, autonomic instability. Recent antipsychotic change. CK markedly elevated. Lithium is a recognized precipitant of NMS. |
| Thyroid storm | Tachycardia, hyperthermia, altered mental status, tremor. History of thyroid disease. Lithium-treated patients may have underlying thyroid dysfunction. TSH/free T4 distinguishes. |
| Uremia / renal failure | Encephalopathy, asterixis, nausea, volume overload. BUN/Cr elevated. May coexist with lithium toxicity (renal failure precipitates lithium accumulation). |
| Hypercalcemia | Confusion, lethargy, polyuria, constipation. Chronic lithium causes hyperparathyroidism in 10-25% of patients. Check calcium and PTH. |
| Alcohol / sedative withdrawal | Tremor, agitation, seizures, tachycardia. History of recent cessation. Lithium-treated psychiatric patients may have co-morbid substance use. |
| Posterior reversible encephalopathy syndrome (PRES) | Headache, visual changes, seizures, altered mental status. MRI shows posterior white matter edema. Can be triggered by lithium. |
| Valproic acid toxicity | Tremor, ataxia, encephalopathy. Often co-prescribed with lithium in bipolar disorder. Check valproic acid level. |

## Workup

**Labs:**
- **Serum lithium level** -- the essential test. Draw immediately. Repeat every 2-4 hours until clearly downtrending and below 1.5 mEq/L. In sustained-release ingestion, levels may continue to rise for 12+ hours.
- **BMP (Chem-8)** -- sodium, potassium, chloride, bicarbonate, BUN, creatinine, glucose, calcium. Renal function determines clearance capacity. Hypernatremia may indicate NDI. Hypercalcemia from lithium-induced hyperparathyroidism.
- **Magnesium** -- hypomagnesemia lowers seizure threshold and exacerbates cardiac conduction abnormalities.
- **TSH** -- chronic lithium causes hypothyroidism in 20-30% of patients, which can confound the clinical picture (lethargy, myxedema).
- **Serum osmolality and urine osmolality** -- if NDI suspected (urine osm <300 mOsm/kg with serum osm >290 mOsm/kg suggests NDI).
- **Urinalysis** -- isosthenuria (fixed urine specific gravity ~1.005-1.010) suggests NDI.
- **VBG with lactate** -- acidosis suggests severe tissue effects or concurrent sepsis.
- **CBC** -- leukocytosis is common with lithium (lithium stimulates granulopoiesis; WBC 10-14K is a known chronic effect, not necessarily infection).
- **Pregnancy test** -- all females of reproductive age. Lithium is Pregnancy Category D (Ebstein anomaly risk in first trimester).

**ECG:**
- All patients. Lithium blocks cardiac sodium and potassium channels. Look for: T-wave flattening or inversion (most common), QTc prolongation, ST depression, sinus bradycardia, sinoatrial block, junctional rhythms, U waves (similar to hypokalemia). Brugada-pattern ECG has been reported with lithium toxicity.

**Imaging:**
- **CT head (non-contrast)** -- if altered mental status, seizures, or focal neurologic deficits to exclude structural pathology. Lithium toxicity does not produce specific CT findings acutely.
- **MRI brain** -- if considering SIND (irreversible lithium neurotoxicity). May show cerebellar and basal ganglia abnormalities.

**Do NOT order:**
- Activated charcoal (lithium is not adsorbed by charcoal)
- Standard urine toxicology screen to diagnose lithium (lithium is not detected)

## Treatment

**Volume Resuscitation (first-line for all lithium toxicity):**
- Normal saline 0.9% -- 20 mL/kg IV bolus, then 200-300 mL/hr continuous infusion
- Goal: restore intravascular volume, optimize renal perfusion, maximize renal lithium excretion
- Volume repletion alone can increase lithium clearance substantially in dehydrated patients
- Avoid forced diuresis with loop diuretics -- furosemide does NOT enhance lithium excretion and may worsen volume depletion and electrolyte derangement
- Monitor urine output (target >1 mL/kg/hr)

**GI Decontamination:**
- **Activated charcoal: NOT effective.** Lithium is a small monovalent cation not adsorbed by charcoal.
- **Whole bowel irrigation (WBI):** Indicated for sustained-release lithium preparations or large acute ingestions. Polyethylene glycol electrolyte solution (GoLYTELY) 1-2 L/hr in adults (25 mL/kg/hr in children) via NGT until clear rectal effluent. Contraindicated in bowel obstruction, ileus, or hemodynamic instability.
- **Gastric lavage:** Consider only if massive acute ingestion presenting within 1 hour. Limited utility given lithium's rapid absorption.
- **Sodium polystyrene sulfonate (SPS/Kayexalate):** Some case reports suggest SPS binds lithium in the GI tract, but evidence is insufficient to recommend routine use. Not standard of care.

**Hemodialysis -- EXTRIP Workgroup Recommendations (Decker et al., CJASN 2015):**

Lithium is an ideal dialysis candidate: low molecular weight (6.94 Da), no protein binding, small volume of distribution, water-soluble.

**Indications for hemodialysis:**
- Lithium level >5.0 mEq/L (regardless of symptoms)
- Lithium level >4.0 mEq/L with impaired renal function (GFR <45 mL/min)
- Altered mental status, seizures, or life-threatening dysrhythmia regardless of lithium level
- Expected time to reduce lithium to <1.0 mEq/L exceeds 36 hours with supportive care alone
- Failure to improve clinically despite aggressive IV hydration

**Hemodialysis logistics:**
- Hemodialysis is the preferred extracorporeal modality (removes lithium faster than CRRT)
- Continuous renal replacement therapy (CRRT) is an acceptable alternative if intermittent HD is unavailable or the patient is hemodynamically unstable
- Continue HD until clinical improvement is apparent AND lithium level <1.0 mEq/L
- Minimum 6 hours of HD if lithium levels cannot be obtained during the procedure
- **Rebound phenomenon:** Lithium re-equilibrates from intracellular/tissue compartments after HD stops. Recheck lithium level 6-8 hours post-dialysis. Repeat HD if level rebounds >1.0 mEq/L with persistent symptoms. Multiple HD sessions may be required.

**Seizure Management:**
- Lorazepam 0.1 mg/kg IV (max 4 mg), repeat once at 5 minutes if seizure persists
- Second-line: levetiracetam 20-60 mg/kg IV (max 4500 mg) over 15 minutes
- Phenytoin is NOT effective for lithium-induced seizures (toxin-mediated mechanism, not epileptogenic focus)
- Refractory seizures: continuous infusion midazolam or propofol with intubation

**Cardiac Management:**
- Continuous telemetry monitoring
- Symptomatic bradycardia: atropine 0.5-1 mg IV; temporary transcutaneous pacing if refractory
- QTc prolongation: correct magnesium (magnesium sulfate 2g IV over 20 minutes if Mg <2.0 mg/dL), avoid QTc-prolonging medications
- Hemodynamically unstable arrhythmias: standard ACLS protocols

**Supportive Care:**
- Discontinue lithium immediately
- Discontinue all nephrotoxic medications and drugs that reduce lithium clearance (NSAIDs, thiazides, ACE inhibitors/ARBs)
- Correct electrolyte abnormalities (sodium, potassium, magnesium, calcium)
- Avoid haloperidol if possible (both lithium and haloperidol can cause NMS; combination increases risk)
- Temperature monitoring -- lithium toxicity can cause hyperthermia

## Disposition

**ICU Admission:**
- Lithium level >4.0 mEq/L (any pattern)
- Altered mental status, seizures, or coma
- Hemodynamically significant cardiac dysrhythmia
- Requiring hemodialysis
- Chronic toxicity with level >2.5 mEq/L and neurologic symptoms (high-risk pattern)
- Renal failure (unable to clear lithium endogenously)

**Admit to Monitored Bed (Observation/Telemetry):**
- Lithium level 2.0-4.0 mEq/L with mild symptoms (tremor, GI complaints) that are improving on IV hydration
- Acute ingestion of sustained-release preparation (levels may continue to rise -- requires serial monitoring for minimum 12-24 hours)
- Chronic toxicity with level 1.5-2.5 mEq/L and mild neurologic symptoms
- Psychiatric evaluation if intentional overdose (medical clearance first)

**Discharge Criteria (must meet ALL):**
- Lithium level <1.5 mEq/L and downtrending on at least two serial measurements 4-6 hours apart
- Asymptomatic -- no tremor, no GI symptoms, no neurologic findings
- Normal renal function (or stable baseline creatinine)
- Normal ECG
- Precipitant identified and addressed (medication reconciliation, hydration status, renal function)
- Lithium dose adjusted or discontinued with outpatient follow-up arranged
- Psychiatric evaluation completed if intentional overdose
- Clear return precautions: return for tremor, confusion, unsteady gait, persistent vomiting, decreased urine output

**Nephrology Follow-up:**
- Any patient who required hemodialysis
- Any patient with new or worsening renal impairment
- Suspected lithium-induced NDI for outpatient evaluation and possible amiloride therapy

## Pitfalls

1. **Assuming serum lithium level correlates with clinical severity in all patterns.** In acute ingestion, brain levels lag behind serum levels by hours. A patient with a lithium level of 5 mEq/L who is alert at 2 hours post-ingestion may seize at 8 hours as lithium distributes into the CNS. In chronic toxicity, the opposite applies: a level of 2.0 mEq/L can produce severe neurotoxicity because the brain has fully equilibrated. Always interpret the level in the context of the toxicity pattern.

2. **Drawing a single lithium level and basing disposition on it.** Sustained-release formulations produce delayed and prolonged absorption. Levels can continue to rise for 12+ hours after ingestion. Post-dialysis levels can rebound 6-8 hours later due to tissue re-equilibration. Serial levels every 2-4 hours until clearly downtrending are mandatory.

3. **Giving activated charcoal.** Lithium is a small monovalent cation (molecular weight 6.94 Da) that is not adsorbed by activated charcoal. Administering charcoal wastes time, adds aspiration risk, and may delay whole bowel irrigation. The only GI decontamination with evidence for lithium is WBI for sustained-release preparations.

4. **Not recognizing chronic toxicity as the most dangerous pattern.** Emergency physicians often associate "toxicity" with large acute ingestions. But chronic lithium toxicity from gradual accumulation carries the highest morbidity and mortality. A patient on maintenance lithium who presents with subtle confusion and tremor after starting an NSAID or thiazide may have life-threatening CNS lithium accumulation at a "mildly elevated" level of 2.0 mEq/L.

5. **Using loop diuretics to "force" lithium excretion.** Furosemide does not enhance lithium clearance. Lithium is reabsorbed primarily in the proximal tubule (same transporter as sodium), not the loop of Henle. Loop diuretics cause volume depletion and hyponatremia, which increase proximal sodium (and lithium) reabsorption, potentially worsening toxicity. Normal saline volume expansion is the correct approach.

6. **Failing to ask about drug interactions as precipitants.** The most common cause of chronic lithium toxicity is a new medication that reduces renal lithium clearance. NSAIDs, thiazide diuretics, ACE inhibitors, and ARBs are the major offenders. Any patient on lithium presenting with toxicity symptoms needs a thorough medication reconciliation including OTC medications (ibuprofen, naproxen).

7. **Delaying hemodialysis consultation.** Lithium is one of the most dialyzable toxins known (small molecule, no protein binding, water-soluble). Hemodialysis can clear lithium 4-5 times faster than renal excretion. Early nephrology consultation saves time -- arranging dialysis access and coordinating with the dialysis unit takes hours. Do not wait until the patient deteriorates to call nephrology.

8. **Stopping hemodialysis based on a mid-treatment lithium level.** The intravascular lithium level drops rapidly during HD, but tissue stores have not equilibrated. After HD ends, lithium redistributes from the intracellular compartment back into serum, causing the rebound phenomenon. Check lithium level 6-8 hours post-HD. Multiple HD sessions are often required for severe toxicity.

9. **Forgetting that lithium-treated patients may have nephrogenic diabetes insipidus.** Up to 50% of chronic lithium users develop NDI from aquaporin-2 downregulation. These patients are chronically volume-depleted at baseline and decompensate rapidly with any additional fluid loss (vomiting, diarrhea, reduced intake). NDI also means the kidney cannot concentrate urine to conserve water, creating a vicious cycle of dehydration and rising lithium levels. Hypernatremia and dilute urine in a lithium-toxic patient should raise this concern.

10. **Overlooking SIND (syndrome of irreversible lithium-effectuated neurotoxicity).** Persistent cerebellar dysfunction (ataxia, dysarthria, intention tremor), cognitive impairment, and extrapyramidal signs can be permanent after severe lithium toxicity. SIND is not a failure to treat -- it reflects irreversible neuronal damage. Recognizing it matters for prognosis, disposition (likely needs inpatient rehabilitation), and for communicating with the patient and family that these deficits may not resolve.
