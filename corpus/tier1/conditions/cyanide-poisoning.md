---
id: cyanide-poisoning
condition: Cyanide Poisoning
aliases: [cyanide toxicity, hydrogen cyanide exposure, CN poisoning, smoke inhalation cyanide]
icd10: [T65.0X1A, T65.0X2A]
esi: 1
time_to_harm:
  irreversible_injury: "< 5 minutes"
  death: "< 15 minutes without treatment"
  optimal_intervention_window: "Hydroxocobalamin within minutes of exposure"
category: toxicologic
track: tier1
sources:
  - type: pubmed
    ref: "Borron SW et al. Prospective study of hydroxocobalamin for acute cyanide poisoning in smoke inhalation. Ann Emerg Med 2007;49(6):794-801, 801.e1-2"
    pmid: "17509730"
  - type: pubmed
    ref: "Anseeuw K et al. Cyanide poisoning by fire smoke inhalation: a European expert consensus. Eur J Emerg Med 2013;20(1):2-9"
    pmid: "22828651"
  - type: pubmed
    ref: "Hall AH et al. Sodium thiosulfate or hydroxocobalamin for the empiric treatment of cyanide poisoning? Ann Emerg Med 2007;49(6):806-813"
    pmid: "17509731"
  - type: pubmed
    ref: "Baud FJ et al. Elevated blood cyanide concentrations in victims of smoke inhalation. N Engl J Med 1991;325(25):1761-1766"
    pmid: "1944484"
  - type: guideline
    ref: "CDC Emergency Preparedness and Response: Cyanide. Centers for Disease Control and Prevention. 2024."
    url: "https://emergency.cdc.gov/agent/cyanide/index.asp"
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
# Cyanide Poisoning

## Recognition

**Pathophysiology:** Cyanide (CN-) binds ferric iron (Fe3+) in cytochrome c oxidase (complex IV of the mitochondrial electron transport chain), halting oxidative phosphorylation. Cells cannot use oxygen — histotoxic hypoxia. Despite normal or elevated arterial oxygen content, tissues cannot extract oxygen. The body shifts to anaerobic glycolysis, generating profound lactic acidosis. Death occurs from cellular energy failure in the most oxygen-dependent organs: brain and heart.

**Sources of Cyanide Exposure:**
- **Smoke inhalation (most common ED presentation):** HCN released from combustion of nitrogen-containing materials (wool, silk, polyurethane, nylon, rubber). House fire victim with depressed consciousness has cyanide poisoning until proven otherwise.
- Industrial: electroplating, metal processing, chemical synthesis, photography, mining
- Iatrogenic: sodium nitroprusside infusion (CN- released from nitroprusside metabolism; at doses >10 mcg/kg/min or prolonged infusion)
- Plant-derived: bitter almonds, apricot pits, cassava (release cyanogenic glycosides; rare but possible with large ingestions)
- Chemical warfare/terrorism: hydrogen cyanide (AC), cyanogen chloride (CK)
- Acetonitrile: present in artificial nail removers; hepatically metabolized to CN-; delayed-onset toxicity

**Clinical Presentation:**

*Mild:*
- Anxiety, headache, dizziness, nausea
- Tachycardia, mild hypertension

*Moderate:*
- Altered mental status, confusion, agitation
- Hypotension, tachycardia or bradycardia
- Tachypnea/dyspnea

*Severe:*
- Coma, seizures
- Apnea
- Cardiovascular collapse, bradycardia
- Lactic acidosis (lactate often >8-10 mmol/L)
- Cardiac arrest (PEA pattern; myocardium depleted of ATP)

**Classic Clue — Arterialization of venous blood:** Venous PO2 approaches arterial PO2 because tissues cannot extract oxygen from hemoglobin. Mixed venous saturation elevated (>70%) despite hemodynamic collapse.

**Smoke Inhalation Context:**
- Any fire victim with loss of consciousness, altered mental status, or cardiovascular compromise should receive empiric hydroxocobalamin — do NOT wait for a cyanide level
- Co-oximetry to detect concurrent carboxyhemoglobin (CO poisoning) — both may coexist
- Cyanide poisoning and CO poisoning have additive toxicity; both impair cellular respiration

**Bitter Almond Odor:** Often described but unreliable — genetic inability to detect the odor in 20-40% of the population. Do not exclude cyanide because you cannot smell it.

## Critical Actions

1. **Administer hydroxocobalamin (Cyanokit) 5g IV over 15 minutes** — first-line antidote, especially for smoke inhalation. Do NOT delay for lab confirmation. Hydroxocobalamin binds CN- to form cyanocobalamin (vitamin B12), which is renally excreted. Safe in concurrent CO poisoning. Does not cause methemoglobinemia (unlike nitrite regimen). Side effects: bright red discoloration of urine, skin, mucous membranes (expected, not harmful), and transient hypertension. May interfere with colorimetric lab assays (red discoloration of serum). If no response in 15-30 min, repeat 5g IV (max 15g total).

2. **Sodium thiosulfate 12.5g (50 mL of 25% solution) IV over 10-20 minutes** — given in addition to hydroxocobalamin or as sole antidote if hydroxocobalamin unavailable. Provides sulfur donor for rhodanese enzyme to convert CN- to thiocyanate (SCN-, excreted renally). Slower mechanism than hydroxocobalamin; complement, not substitute. Can be given safely with hydroxocobalamin.

3. **DO NOT delay antidote administration for laboratory confirmation.** Cyanide levels are not available in real time in most centers. The diagnosis is clinical. Death occurs in minutes. Lactate >8-10 mmol/L in the context of smoke inhalation, chemical exposure, or unexplained cardiovascular collapse = empiric hydroxocobalamin now.

4. **High-flow oxygen via non-rebreather mask (NRB) or intubation** — while awaiting antidote. 100% O2 competes with CN- at cytochrome oxidase (partial mechanism), and is mandatory for concurrent CO poisoning. Do not delay NRB mask for IV access.

5. **Treat seizures with benzodiazepines** — lorazepam 0.1 mg/kg IV or diazepam 0.1-0.2 mg/kg IV. Pyridoxine (vitamin B6) 5g IV for isoniazid-associated seizures that may coexist; not specific to cyanide.

6. **Standard resuscitation for cardiac arrest** — standard ACLS; higher doses of epinephrine may be needed given profound cellular energy failure. Give antidotes IV push in arrest.

7. **Nitrite regimen (alternative if Cyanokit unavailable):** Amyl nitrite (inhalation) while establishing IV access; sodium nitrite 300 mg (10 mL of 3% solution) IV over 5-7 minutes, then sodium thiosulfate 12.5g IV. Mechanism: nitrites cause methemoglobinemia; methemoglobin (Fe3+) attracts CN- from cytochrome oxidase. CONTRAINDICATED with concurrent CO poisoning (methemoglobin further reduces oxygen-carrying capacity in CO-poisoned patients). Use hydroxocobalamin in fire victims.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| CO poisoning | Cherry-red skin (unreliable), co-oximetry COHgb elevated; often coexists with CN in fires |
| Hydrogen sulfide (H2S) poisoning | Rotten-egg odor, similar mechanism; hydroxocobalamin less effective; nitrites used |
| Sodium nitroprusside toxicity | ICU setting, prolonged high-dose infusion, rising lactate |
| Organophosphate poisoning | SLUDGE/DUMBELS, miosis, bradycardia, bronchospasm; atropine/pralidoxime treatment |
| Septic shock | Hemodynamic collapse without specific CN exposure history; cultures positive |
| Status epilepticus with lactic acidosis | Seizure activity primary; no CN exposure |
| Methanol poisoning | Elevated osmol gap, visual symptoms, slow onset; specific toxic alcohol workup |

## Workup

**Immediate (do not delay antidote for results):**
- Point-of-care glucose — hypoglycemia
- Arterial blood gas — profound metabolic (lactic) acidosis, normal or elevated PaO2
- Lactate — elevated (often >8-10 mmol/L); lactate >10 mmol/L in fire victims: sensitivity ~90% for toxic cyanide levels
- Co-oximetry panel — COHgb (concurrent CO), MetHgb (if nitrite therapy given), pulse oximetry unreliable in both CO and CN poisoning
- Serum electrolytes, BMP — anion gap calculation

**Secondary (confirmatory, post-treatment):**
- Whole blood cyanide level — values >1 mg/L (38 mcmol/L) toxic; >3 mg/L potentially lethal. Not available stat at most centers; results after clinical decisions made.
- After hydroxocobalamin: expect serum discoloration (bright red); will interfere with colorimetric assays (CO-oximetry, bilirubin, creatinine). Collect pre-treatment samples where possible.

**ECG:**
- Sinus tachycardia (early), bradycardia (severe)
- ST-segment changes, conduction abnormalities in severe toxicity

## Treatment

**Antidote Priority (choose based on scenario):**

*Fire victim or CN exposure of any type — first choice:*
- Hydroxocobalamin (Cyanokit) 5g IV over 15 min
- Sodium thiosulfate 12.5g IV over 10-20 min (add on, or if Cyanokit unavailable)

*Non-fire CN exposure, NO concurrent CO poisoning suspected:*
- Hydroxocobalamin 5g IV, OR
- Nitrite regimen: sodium nitrite 300 mg IV over 5-7 min THEN sodium thiosulfate 12.5g IV
- (Nitrite regimen CONTRAINDICATED in concurrent CO poisoning)

**Supportive:**
- 100% O2 by NRB or ventilator (FiO2 = 1.0)
- Vasopressors for refractory hypotension: norepinephrine 0.1-2 mcg/kg/min IV
- Bicarbonate for severe lactic acidosis (pH <7.1): NaHCO3 1-2 mEq/kg IV — temporizing only; antidote corrects the underlying mechanism
- Seizures: benzodiazepines as above
- Hyperbaric oxygen: beneficial for concurrent severe CO poisoning; hydroxocobalamin takes priority and can be given in the ambulance before HBO

**Decontamination (industrial/dermal exposure):**
- Remove contaminated clothing (first responder risk with HCN off-gassing from skin)
- Copious water irrigation of skin and eyes (15-20 minutes)
- HCN gas: evacuate area; do not enter without full SCBA

## Disposition

**ICU for all symptomatic cyanide poisoning:**
- Altered mental status, seizures, cardiovascular compromise
- Lactate >5 mmol/L
- Post-antidote monitoring: serial lactate, neurological status, cardiovascular parameters
- Antidote re-dosing may be required

**Monitored Observation:**
- Asymptomatic exposure with documented potential significant exposure (industrial spill)
- Observe minimum 6 hours for delayed-onset presentations (acetonitrile)

**Decontamination and Release:**
- Dermal exposure, fully decontaminated, asymptomatic at 6 hours, normal lactate/ABG

**HAZMAT Notification:**
- Industrial exposure: notify hospital safety officer, local HAZMAT team
- Terrorism/mass casualty: activate incident command; isolate scene; law enforcement notification

## Pitfalls

1. **Waiting for cyanide levels before treating.** Cyanide levels are not available in real time. The diagnosis is clinical + contextual (fire, industrial exposure, unexplained lactic acidosis). Death occurs in minutes. Give hydroxocobalamin empirically to any fire victim with altered mental status, any patient with unexplained high-lactate cardiovascular collapse, or any scenario consistent with CN exposure.

2. **Using the nitrite regimen in concurrent CO poisoning (fire victims).** Sodium nitrite induces methemoglobinemia — a functional anemia that further reduces oxygen-carrying capacity in a patient already impaired by CO. This is potentially lethal. Use hydroxocobalamin in all fire victims. Reserve nitrites for non-fire CN exposure without suspected CO component.

3. **Relying on pulse oximetry to assess oxygenation.** SpO2 reads falsely normal in both CN poisoning (normal PaO2, cannot use O2) and CO poisoning (oximeter cannot distinguish COHgb from OxyHgb). Arterial blood gas with co-oximetry is required.

4. **Missing cyanide poisoning in nitroprusside infusion.** Prolonged sodium nitroprusside infusions at doses >10 mcg/kg/min generate free cyanide. An ICU patient on nitroprusside who develops an unexplained rising lactate or altered mental status has nitroprusside-induced cyanide toxicity until proven otherwise. Stop the nitroprusside and give sodium thiosulfate.

5. **Not recognizing the bright red discoloration post-hydroxocobalamin.** Hydroxocobalamin turns blood, urine, and mucous membranes bright red-orange. Lab technicians and nurses may report alarming findings (red serum, "hematuria") that are expected antidote effects. Warn the team before administering hydroxocobalamin.