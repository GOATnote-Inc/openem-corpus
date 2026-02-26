---
id: tricyclic-antidepressant-overdose
condition: Tricyclic Antidepressant Overdose
aliases: [TCA overdose, TCA poisoning, amitriptyline overdose, nortriptyline overdose, cyclic antidepressant overdose]
icd10: [T43.011A, T43.012A, T43.021A]
esi: 2
time_to_harm:
  irreversible_injury: "< 1 hour"
  death: "< 2 hours in massive ingestion"
category: toxicologic
track: tier1
sources:
  - type: pubmed
    ref: "Liebelt EL et al. Serial electrocardiographic changes in acute tricyclic antidepressant overdoses. Crit Care Med 1997;25(10):1721-1726"
    pmid: "9377878"
  - type: pubmed
    ref: "Boehnert MT, Lovejoy FH Jr. Value of the QRS duration versus the serum drug level in predicting seizures and ventricular arrhythmias after an acute overdose of tricyclic antidepressants. N Engl J Med 1985;313(8):474-479"
    pmid: "4022081"
  - type: pubmed
    ref: "Callaham M, Kassel D. Epidemiology of fatal tricyclic antidepressant ingestion: implications for management. Ann Emerg Med 1985;14(1):1-9"
    pmid: "3966492"
  - type: pubmed
    ref: "Pentel PR, Benowitz NL. Tricyclic antidepressant poisoning. Management of arrhythmias. Med Toxicol 1986;1(2):101-121"
    pmid: "3083165"
  - type: pubmed
    ref: "Kerr GW et al. Tricyclic antidepressant overdose: a review. Emerg Med J 2001;18(4):236-241"
    pmid: "11435353"
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
# Tricyclic Antidepressant Overdose

## Recognition

**Pathophysiology:** Tricyclic antidepressants (TCAs) are multi-receptor antagonists. Toxicity arises from three primary mechanisms:
1. **Sodium channel blockade (fast Na+ channel, type 1A):** Slows phase 0 depolarization → QRS widening → ventricular arrhythmias, conduction block
2. **Anticholinergic effects (muscarinic blockade):** Tachycardia, hyperthermia, agitation, urinary retention, decreased GI motility
3. **Alpha-1 adrenergic blockade:** Vasodilation → hypotension (often the most dangerous early hemodynamic feature)
Additional: antihistamine (sedation), GABA-A receptor blockade (seizures), inhibition of norepinephrine/serotonin reuptake (contributes to tachycardia and serotonergic features).

**Common TCAs:**
- Amitriptyline (Elavil) — among the most toxic; high sodium channel blocking activity
- Nortriptyline — slightly less cardiotoxic
- Imipramine (Tofranil)
- Desipramine (Norpramin) — highly cardiotoxic despite lower anticholinergic effects
- Clomipramine — also used for OCD; significant seizure risk
- Doxepin — also sedating at low doses

**Toxic Dose:** Ingestion >10-20 mg/kg is potentially life-threatening. TCA toxicity causes death at relatively low doses compared to many other antidepressants. Amitriptyline 1000 mg in an adult may cause cardiac arrest.

**Clinical Presentation:**
- Rapid onset: symptoms within 30-60 minutes of ingestion
- **Cardiovascular:** sinus tachycardia (most common early finding), hypotension (vasodilation + decreased contractility), QRS widening, ventricular arrhythmias (VT, VF), AV block
- **CNS:** agitation, delirium, seizures (generalized tonic-clonic), coma
- **Anticholinergic:** dry flushed skin, mydriasis, urinary retention, hyperthermia
- **Rapid deterioration:** a patient talking to you in triage can be in VF 30 minutes later

**ECG Landmarks (Boehnert 1985 NEJM study):**
- QRS >100 ms: risk of seizures; sensitivity ~40-50% for predicting seizures
- QRS >160 ms: risk of ventricular arrhythmias; high specificity
- R wave in aVR >3 mm (or R:S ratio in aVR >0.7): sensitive and specific marker of sodium channel blockade from TCA
- QTc prolongation (risk of torsades, though less common than VT from Na channel block)
- Terminal R wave in aVR and terminal S wave in I/aVL (rightward terminal QRS axis) — classic TCA pattern

**Speed of Deterioration:** TCAs cause some of the most rapid deteriorations in clinical toxicology. A patient who presents talking and appears mildly altered can develop refractory VT and death within 30-60 minutes. All TCA ingestions require immediate monitoring regardless of initial appearance.

## Critical Actions

1. **Sodium bicarbonate 1-2 mEq/kg IV bolus** for QRS >100 ms on ECG. Dual mechanism: (1) sodium load partially reverses sodium channel blockade; (2) alkalinization (pH 7.45-7.55) reduces TCA binding to sodium channels (ionized form has less affinity). Follow with continuous NaHCO3 infusion: 3 ampules (150 mEq) in 1L D5W at 200-250 mL/hr. Maintain serum pH 7.45-7.55 (do NOT exceed 7.55 — alkalemia decreases ionized calcium and increases seizure risk). Monitor ABG every 30-60 min.

2. **QRS monitoring is the key metric for treatment.** Target: QRS narrows to <100 ms with bicarbonate. If QRS does not narrow or widens further, escalate NaHCO3 or add hypertonic saline (3% NaCl 1-2 mL/kg IV bolus) for sodium channel effect.

3. **Benzodiazepines for seizures** — lorazepam 0.1 mg/kg IV or diazepam 0.1-0.2 mg/kg IV. Repeat every 5 minutes until seizures controlled. TCA seizures may be brief and self-terminating but increase acidosis → worsen sodium channel blockade → precipitate arrhythmias. Control seizures aggressively.

4. **Do NOT use phenytoin for TCA seizures.** Phenytoin (and fosphenytoin) are sodium channel blockers — they compound TCA sodium channel blockade and increase arrhythmia risk. This combination is potentially lethal. Benzodiazepines are the only appropriate first-line anticonvulsants.

5. **Norepinephrine for hypotension** — start at 0.1 mcg/kg/min IV, titrate to MAP >65 mmHg. TCA hypotension is primarily from alpha-1 blockade (vasodilation); norepinephrine provides alpha-1 agonism. Avoid dopamine as primary agent (less alpha activity relative to norepinephrine in TCA-induced shock).

6. **Do NOT give flumazenil** if benzodiazepine co-ingestion is present or suspected. Flumazenil in a TCA-poisoned patient precipitates refractory seizures, rapid QRS widening, and cardiovascular collapse. Flumazenil reverses benzodiazepine-mediated anticonvulsant GABA-A agonism and unmasks TCA's GABA-A receptor blockade.

7. **Intubation with RSI** if required — use rocuronium 1.2 mg/kg IV. Avoid succinylcholine if rhabdomyolysis or prolonged immobility suspected (hyperkalemic cardiac arrest risk). Post-intubation: target hyperventilation (PaCO2 30-35 mmHg) and bicarbonate infusion to maintain serum pH 7.45-7.55.

8. **Do not cardiovert stable wide-complex tachycardia** with pulse — give bicarbonate and antiarrhythmic agents first. DC cardioversion in TCA toxicity can precipitate refractory VF. If VT with hemodynamic collapse and not responsive to bicarbonate: lidocaine 1-1.5 mg/kg IV is the preferred antiarrhythmic (does not worsen sodium channel blockade compared to other class Ia/Ic agents).

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Diphenhydramine OD | Anticholinergic features without QRS widening at low doses; QRS widening possible at high doses; similar management |
| Cocaine/amphetamine toxicity | Diaphoresis (sympathomimetic), no TCA history, QRS less prominent unless massive dose |
| Antipsychotic OD | QTc prolongation predominant; less QRS widening; anticholinergic may overlap |
| Hyperkalemia | Wide QRS, peaked T waves; no TCA exposure history; serum K+ elevated |
| Brugada syndrome exacerbated by drugs | Sodium channel blockers may unmask Brugada pattern |
| Propranolol OD | QRS widening from sodium channel block; bradycardia (not tachycardia); different medication history |

## Workup

**Labs:**
- Serum TCA levels — tricyclic levels above 1000 ng/mL associated with severe toxicity, but level does not replace ECG for management decisions
- Acetaminophen and salicylate levels (co-ingestion screen)
- BMP — electrolytes, creatinine; hypokalemia and hypomagnesemia worsen arrhythmias
- ABG — pH monitoring critical during bicarbonate therapy
- CK — rhabdomyolysis from seizures
- Lactate — tissue perfusion
- Urine drug screen — qualitative TCA (immunoassay); note that many UDS cross-react with antihistamines and antipsychotics

**12-Lead ECG (mandatory on arrival, repeat serially):**
- QRS duration — measure every 15-30 minutes until stable
- Terminal R wave in aVR (>3 mm or R:S ratio >0.7) — highly specific TCA marker
- QTc — prolongation risk for torsades
- PR interval, AV block assessment
- Serial ECG during bicarbonate therapy to document QRS narrowing

**Do Not Wait for Labs:** The ECG is the most important monitor. QRS widening mandates immediate bicarbonate regardless of lab results.

## Treatment

**GI Decontamination:**
- Activated charcoal 1 g/kg PO (max 50g) within 1-2 hours if alert and airway intact
- Do not administer charcoal to an obtunded patient without a protected airway — TCA ingestions deteriorate rapidly; if any concern about mental status, intubate first
- Ipecac and gastric lavage: no role

**Sodium Bicarbonate Protocol:**
- Bolus: 1-2 mEq/kg IV for QRS >100 ms or ventricular arrhythmia
- Repeat bolus every 5-10 min if QRS still wide or arrhythmia not resolving
- Maintenance infusion: 150 mEq (3 ampules 8.4% NaHCO3) in 1L D5W at 200-250 mL/hr
- Target: serum pH 7.45-7.55, QRS <100 ms
- Monitor: ABG every 30-60 min, ionized calcium (alkalemia → hypocalcemia), sodium, potassium

**Hypertonic Saline:**
- 3% NaCl 1-2 mL/kg IV bolus for QRS widening unresponsive to bicarbonate
- Provides sodium load without additional alkalinization; useful when pH already adequate

**Antiarrhythmics:**
- Lidocaine 1-1.5 mg/kg IV for VT/VF unresponsive to bicarbonate (preferred — does not worsen Na channel block)
- Magnesium sulfate 2g IV for torsades (if QTc-driven arrhythmia)
- Avoid: Class Ia (quinidine, procainamide), Class Ic (flecainide), Class III (amiodarone — prolongs QT)

**Vasopressors:**
- Norepinephrine 0.1-2 mcg/kg/min IV (alpha-1 agonism for TCA vasodilation)
- Vasopressin 0.04 units/min for refractory hypotension

**IV Lipid Emulsion:**
- 20% ILE 1.5 mL/kg IV bolus for lipophilic TCA cardiac arrest (amitriptyline, doxepin)
- Reserve for refractory cardiac arrest unresponsive to bicarbonate and ACLS

## Disposition

**ICU for all symptomatic TCA overdoses:**
- QRS >100 ms (mandatory ICU)
- Seizures, altered mental status
- Hypotension requiring vasopressors
- Any ventricular arrhythmia
- Post-intubation patients

**Monitored Observation (minimum 6 hours, often 24 hours):**
- Asymptomatic with documented ingestion: observe minimum 6 hours with continuous telemetry
- Normal ECG (QRS <100 ms) maintained throughout observation: may step down from monitored setting
- Asymptomatic at 6 hours with normal ECG: medical clearance; psychiatric evaluation

**Discharge:**
- 6-hour observation, QRS <100 ms on serial ECGs, asymptomatic, hemodynamically stable
- Psychiatric safety assessment completed and documented

## Pitfalls

1. **Using phenytoin for TCA-induced seizures.** Phenytoin is a sodium channel blocker — it compounds TCA sodium channel toxicity and may precipitate ventricular arrhythmias. This is a fatal management error. Use benzodiazepines exclusively for TCA seizure management.

2. **Giving flumazenil to a TCA-poisoned patient.** When patients with multiple ingestions receive flumazenil to reverse benzodiazepine sedation, flumazenil unmasks TCA-mediated GABA blockade, precipitating explosive seizures and cardiovascular collapse. Never give flumazenil in undifferentiated polypharmacy overdose.

3. **Waiting for QRS >160 ms before starting bicarbonate.** The evidence-based threshold is QRS >100 ms. At 160 ms, you are behind the arrhythmia curve. Start bicarbonate at 100 ms — the goal is to prevent arrhythmias, not treat them after they develop.

4. **Discharging an asymptomatic TCA patient at 2-3 hours.** TCA overdose can evolve rapidly over the first 6 hours. Patients who appear well at 2-3 hours have subsequently developed VF at 4-5 hours. Minimum 6-hour observation with continuous cardiac monitoring is required for any confirmed or suspected TCA ingestion.

5. **Failing to recognize the R wave in aVR.** Many providers look at QRS duration and miss the terminal R in aVR — a highly sensitive and specific marker of TCA sodium channel blockade. Measure R wave height in aVR and look for rightward terminal QRS axis on every TCA overdose ECG.

6. **Targeting a normal pH instead of a mildly alkaline pH.** The target pH is 7.45-7.55. A normal pH (7.35-7.45) is subtherapeutic — the sodium channel affinity for TCA is pH-dependent, and you want to shift the equilibrium toward ionized (lower-affinity) TCA in the sodium channel. Monitor ABGs frequently to stay in the therapeutic alkalemia window without overshooting into pH >7.55 territory (which causes hypocalcemia and seizures).