---
id: serotonin-syndrome
condition: Serotonin Syndrome
aliases: [serotonin toxicity, serotonergic syndrome]
icd10: [G90.81]
esi: 2
time_to_harm: "< 12 hours"
mortality_if_delayed: "2-12% in severe cases"
category: toxicologic
track: tier1
sources:
  - type: review
    ref: "Boyer EW, Shannon M. The Serotonin Syndrome. N Engl J Med 2005;352:1112-20"
    pmid: "15784664"
    doi: "10.1056/NEJMra041867"
  - type: pubmed
    ref: "Dunkley EJC et al. The Hunter Serotonin Toxicity Criteria: simple and accurate diagnostic decision rules for serotonin toxicity. QJM 2003;96(9):635-42"
    pmid: "12925718"
  - type: pubmed
    ref: "Isbister GK, Buckley NA. The pathophysiology of serotonin toxicity in animals and humans: implications for diagnosis and treatment. Clin Neuropharmacol 2005;28(5):205-14"
    pmid: "16239759"
  - type: pubmed
    ref: "Graudins A et al. Treatment of the serotonin syndrome with cyproheptadine. J Emerg Med 1998;16(4):615-19"
    pmid: "9696181"
  - type: pubmed
    ref: "Mikkelsen N et al. Serotonin syndrome — A focused review. Basic Clin Pharmacol Toxicol 2023;133(2):124-29"
    pmid: "37309284"
last_updated: "2026-02-19"
compiled_by: agent
risk_tier: B
validation:
  schema_version: "2.0"
  automated_consistency_check: "2026-02-27"
  dose_range_validator: "2026-02-27"
  unit_normalization_check: "2026-02-27"
  cross_file_consistency_check: "2026-02-27"
  citation_presence_check: "2026-02-27"
  duplicate_content_check: "2026-02-27"
  outlier_detection_flag: clear
  provenance_links: []
---
# Serotonin Syndrome

## Recognition

**Hunter Serotonin Toxicity Criteria (sensitivity 84%, specificity 97%):**
Requires exposure to a serotonergic agent PLUS any ONE of the following:

1. Spontaneous clonus
2. Inducible clonus + agitation OR diaphoresis
3. Ocular clonus + agitation OR diaphoresis
4. Tremor + hyperreflexia
5. Hypertonia + temperature >38C + ocular clonus OR inducible clonus

**Clinical triad:**
- Neuromuscular excitation: clonus (spontaneous, inducible, ocular), hyperreflexia, tremor, rigidity (late/severe)
- Autonomic dysfunction: diaphoresis, tachycardia, hypertension, hyperthermia, mydriasis, flushing, diarrhea
- Altered mental status: agitation, confusion, restlessness, hypomania

**Onset:** Typically within 6-24 hours of drug initiation, dose change, or addition of second serotonergic agent. 60% present within 6 hours.

**Severity spectrum:**
- Mild: tremor, hyperreflexia, diaphoresis, mydriasis, diarrhea
- Moderate: agitation, clonus (inducible > spontaneous), ocular clonus, hyperthermia <40C, tachycardia
- Severe: hyperthermia >41.1C, sustained clonus, rigidity (replaces clonus as muscles stiffen), seizures, rhabdomyolysis, DIC, metabolic acidosis, multiorgan failure

**High-risk drug combinations:**

| Mechanism | Agents |
|---|---|
| MAO inhibition + SRI | MAOI (phenelzine, tranylcypromine, selegiline, linezolid, methylene blue) + SSRI/SNRI |
| Serotonin release + SRI | MDMA, amphetamines + SSRI/SNRI |
| Dual SRI | SSRI + tramadol, SSRI + meperidine |
| Precursor loading + MAO inhibition | L-tryptophan + MAOI |
| Single-agent overdose | SSRI overdose, venlafaxine overdose (uncommon but described) |

**Commonly missed serotonergic agents:** linezolid (reversible MAOI), methylene blue (potent MAOI), tramadol, meperidine, fentanyl (weak), dextromethorphan, ondansetron (case reports, disputed), St. John's wort, lithium

## Critical Actions

| Action | Target |
|---|---|
| Stop all serotonergic agents | Immediately |
| Benzodiazepines for agitation | < 15 minutes |
| Cyproheptadine if moderate-severe | < 30 minutes |
| Active cooling if temp >41C | Immediately |

1. **Discontinue all serotonergic agents.** This is the single most effective intervention. Most mild-moderate cases resolve within 24-72 hours after drug cessation alone.
2. **IV access, continuous monitoring** — cardiac monitor, pulse oximetry, core temperature (rectal/esophageal, not axillary/tympanic)
3. **Benzodiazepines for agitation and neuromuscular hyperactivity** — first-line pharmacotherapy
4. **Cyproheptadine** for moderate-severe cases (see Treatment)
5. **Active cooling** for temperature >41C: evaporative cooling, ice packs to groin/axillae/neck, cold IV saline. Do NOT use antipyretics (ineffective — hyperthermia is from muscular hyperactivity, not hypothalamic reset)
6. **Intubation and neuromuscular blockade** for severe/refractory cases: temperature >41.1C unresponsive to cooling, sustained rigidity, status epilepticus. Use non-depolarizing agent (rocuronium 1.2 mg/kg IV). Avoid succinylcholine (hyperkalemia risk from rhabdomyolysis)
7. **Contact Poison Control (1-800-222-1222)** for complex polypharmacy or refractory cases

## Differential Diagnosis

| Condition | Distinguishing Features |
|---|---|
| Neuroleptic malignant syndrome (NMS) | Slow onset (days-weeks), antipsychotic/dopamine antagonist exposure, lead-pipe rigidity, bradykinesia, akinesia, NO clonus/hyperreflexia. Temperature rise slower. CK markedly elevated. |
| Anticholinergic toxidrome | Dry skin (vs diaphoresis), urinary retention, absent bowel sounds, mydriasis, delirium. NO clonus, NO hyperreflexia. Skin hot and DRY. |
| Sympathomimetic toxidrome | Cocaine/amphetamine exposure, hypertension, tachycardia, mydriasis, diaphoresis. NO clonus. Hyperreflexia less prominent. |
| Malignant hyperthermia | Perioperative setting, volatile anesthetic/succinylcholine exposure, early ETCO2 rise, generalized rigidity ("board-like"). NO clonus. |
| Thyroid storm | Known thyroid disease, goiter, lid lag, atrial fibrillation, jaundice. Develops over days. |
| Meningitis/encephalitis | Fever, nuchal rigidity, focal neuro deficits, CSF pleocytosis. NO clonus pattern. |
| Drug withdrawal (alcohol, BZD) | Withdrawal history, seizures, autonomic instability. Tremor present but NO clonus. |

**Key discriminator:** Clonus (especially lower extremity inducible clonus and ocular clonus) strongly favors serotonin syndrome over all differentials. NMS produces rigidity with bradykinesia; serotonin syndrome produces clonus with hyperreflexia.

## Workup

**Labs:**
- BMP: creatinine (rhabdomyolysis/AKI), potassium (hyperkalemia), glucose
- CBC: leukocytosis (nonspecific), thrombocytopenia (DIC)
- CK: elevated in moderate-severe cases (rhabdomyolysis). Serial q6h if elevated
- Hepatic panel: transaminases elevated in severe cases
- Coagulation: PT/INR, PTT, fibrinogen, D-dimer (DIC screen for severe cases)
- Lactate: elevated with sustained muscular hyperactivity
- ABG/VBG: metabolic acidosis in severe cases
- Urinalysis: myoglobinuria (dipstick positive for blood, no RBCs)
- Serum drug levels as clinically indicated (acetaminophen, salicylate if co-ingestion suspected)

**Imaging:**
- CT head: if altered mental status with unclear etiology, to exclude structural cause
- CXR: if aspiration suspected or intubated

**No confirmatory test exists.** Diagnosis is clinical using Hunter criteria + serotonergic drug exposure history.

## Treatment

### Mild (tremor, hyperreflexia, diaphoresis, no hyperthermia)
- Discontinue serotonergic agent(s)
- Benzodiazepines PRN for agitation: **diazepam 5-10 mg IV q5-10 min** or **lorazepam 1-2 mg IV q5-10 min**
- Observation 6-8 hours
- Most resolve within 24 hours

### Moderate (clonus, agitation, hyperthermia <40C, tachycardia)
- Discontinue serotonergic agent(s)
- **Benzodiazepines:** diazepam 5-10 mg IV q5-10 min or lorazepam 2 mg IV q5-10 min titrated to effect
- **Cyproheptadine** (5-HT2A antagonist):
  - **Loading dose:** 12 mg PO/NG
  - **Maintenance:** 2 mg PO/NG q2h until clinical improvement
  - **Maximum:** 32 mg/24 hours
  - Available only in oral form — crush and administer via NG tube if patient cannot swallow
- IV crystalloid resuscitation
- External cooling PRN

### Severe (temp >41.1C, rigidity, seizures, rhabdomyolysis, DIC)
- Discontinue serotonergic agent(s)
- **Cyproheptadine 12 mg PO/NG** loading dose, then 2 mg q2h (max 32 mg/24h)
- **Aggressive benzodiazepine sedation:** diazepam 10 mg IV q5 min or midazolam 5 mg IV q5 min until agitation/rigidity controlled
- **Intubation** for airway protection, refractory agitation, or respiratory failure
- **Neuromuscular blockade for refractory hyperthermia:** rocuronium 1.2 mg/kg IV (eliminates muscular heat generation). Do NOT use succinylcholine (hyperkalemia from rhabdomyolysis). Note: paralysis masks clinical signs — monitor core temperature and labs for treatment response
- **Active cooling:** evaporative cooling (mist + fan), ice packs to groin/axillae/neck, cold IV NS (4C) 1-2 L, cooling blankets. Target core temp <38.5C, then stop active cooling
- **Rhabdomyolysis management:** IV NS targeting UOP >1-2 mL/kg/hr, monitor CK q6h, sodium bicarbonate 1-2 mEq/kg IV to alkalinize urine if CK >5000
- **Seizures:** benzodiazepines first-line. No phenytoin (ineffective for toxin-induced seizures)
- **Vasopressors** for refractory hypotension: norepinephrine preferred. Avoid serotonergic vasopressors
- **DIC:** supportive (FFP, cryoprecipitate, platelets as indicated)

### Medications to AVOID
- Antipyretics (acetaminophen, NSAIDs): ineffective — hyperthermia is muscular, not hypothalamic
- Succinylcholine: hyperkalemia risk from rhabdomyolysis
- Bromocriptine/dantrolene: these are for NMS, not serotonin syndrome
- Physical restraints without chemical sedation: isometric contraction against restraints worsens hyperthermia and rhabdomyolysis

## Disposition

**Admit to ICU:**
- Temperature >41C
- Hemodynamic instability
- Rhabdomyolysis (CK >5000 IU/L)
- Altered mental status/coma
- Seizures
- DIC
- Requiring intubation or neuromuscular blockade
- Requiring continuous benzodiazepine infusion

**Admit to monitored bed:**
- Moderate symptoms (persistent clonus, tachycardia, agitation) requiring IV benzodiazepines
- Temperature 38-40C
- Ongoing need for cyproheptadine dosing

**Observation (6-8 hours) with potential discharge:**
- Mild symptoms only (tremor, hyperreflexia, mild diaphoresis)
- No hyperthermia
- Symptoms resolving after drug discontinuation
- Reliable follow-up with prescribing physician within 24-48 hours
- Discharge instructions: do not resume serotonergic agent(s) without physician guidance; return for fever, confusion, muscle rigidity, or seizures

**Before discharge:** contact prescribing physician to coordinate medication changes. Document serotonergic drug interaction in the medical record.

## Pitfalls

1. **Confusing serotonin syndrome with NMS.** NMS has lead-pipe rigidity, bradykinesia, and slow onset over days. Serotonin syndrome has clonus, hyperreflexia, and rapid onset within hours. The presence of clonus — especially lower extremity inducible clonus — effectively rules out NMS. Treating serotonin syndrome with bromocriptine (a dopamine agonist for NMS) is ineffective and delays appropriate therapy.

2. **Missing linezolid and methylene blue as serotonergic agents.** Linezolid is a reversible MAOI. Methylene blue is a potent MAOI at doses used for methemoglobinemia (1-2 mg/kg IV). Both cause life-threatening serotonin syndrome when combined with SSRIs/SNRIs. Surgical and ICU teams frequently prescribe these without checking the patient's antidepressant list.

3. **Attributing symptoms to "anxiety" or the psychiatric condition being treated.** Agitation, diaphoresis, and tachycardia after starting or titrating a serotonergic drug are serotonin syndrome until proven otherwise. Checking reflexes and looking for clonus takes 30 seconds and distinguishes the two.

4. **Using antipyretics for serotonin syndrome hyperthermia.** Acetaminophen and NSAIDs target hypothalamic fever pathways. Serotonin syndrome hyperthermia results from sustained muscular hyperactivity. Antipyretics are ineffective and delay active cooling and sedation.

5. **Applying physical restraints without adequate chemical sedation.** Isometric muscular contraction against physical restraints generates heat and accelerates rhabdomyolysis, lactate production, and metabolic acidosis. Benzodiazepines must accompany or precede physical restraint.

6. **Waiting for a "classic" presentation before treating.** Not all Hunter criteria features are present simultaneously. Mild cases present with only tremor and hyperreflexia. Clonus in a patient on serotonergic medication warrants action — do not wait for autonomic instability or hyperthermia to develop.

7. **Failing to obtain a complete medication and supplement list.** Over-the-counter dextromethorphan, St. John's wort, and tramadol (often not volunteered by patients) are serotonergic. MDMA and other recreational drugs are additional sources. Targeted medication reconciliation identifies the causative interaction.

8. **Using succinylcholine for RSI in a patient with rhabdomyolysis.** Severe serotonin syndrome with prolonged rigidity causes rhabdomyolysis. Succinylcholine-induced potassium release on top of existing hyperkalemia from rhabdomyolysis causes cardiac arrest. Use rocuronium 1.2 mg/kg IV.

9. **Discharging moderate cases without adequate observation.** MAOIs have long half-lives (tranylcypromine t1/2 ~2.5h, but irreversible MAO inhibition persists 2-3 weeks). Patients on MAOIs who develop serotonin syndrome require extended observation because symptom recurrence is possible as the interacting drug re-equilibrates.

10. **Not recognizing single-agent overdose as a cause.** Serotonin syndrome is classically taught as a drug-drug interaction, but single-agent SSRI or SNRI overdose (especially venlafaxine, citalopram) produces serotonin syndrome. Overdose patients with clonus and agitation need Hunter criteria assessment.
