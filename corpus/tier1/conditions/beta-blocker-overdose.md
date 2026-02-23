---
id: beta-blocker-overdose
condition: Beta-Blocker Overdose
aliases: [BB overdose, beta blocker toxicity, propranolol overdose, metoprolol overdose]
icd10: [T44.7X1A, T44.7X2A]
esi: 2
time_to_harm:
  irreversible_injury: "< 2 hours"
  death: "< 6 hours"
category: toxicologic
track: tier1
sources:
  - type: pubmed
    ref: "Engebretsen KM et al. High-dose insulin therapy in beta-blocker and calcium channel-blocker poisoning. Clin Toxicol (Phila) 2011;49(4):277-283"
    pmid: "21563902"
  - type: pubmed
    ref: "Shepherd G. Treatment of poisoning caused by beta-adrenergic and calcium-channel blockers. Am J Health Syst Pharm 2006;63(19):1828-1835"
    pmid: "16990631"
  - type: pubmed
    ref: "Bailey B. Glucagon in beta-blocker and calcium channel blocker overdoses: a systematic review. J Toxicol Clin Toxicol 2003;41(5):595-602"
    pmid: "14514004"
  - type: pubmed
    ref: "Jang DH et al. Toxicokinetics and management of beta-blocker overdose. Clin Toxicol (Phila) 2014;52(7):717-729"
    pmid: "25059390"
  - type: pubmed
    ref: "Weinstein RS. Recognition and management of poisoning with beta-adrenergic blocking agents. Ann Emerg Med 1984;13(12):1123-1131"
    pmid: "6391500"
last_updated: "2026-02-23"
compiled_by: agent
risk_tier: B
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
# Beta-Blocker Overdose

## Recognition

**Pathophysiology:** Beta-blockers competitively antagonize catecholamines at beta-1 (cardiac) and beta-2 (peripheral vascular, bronchial) adrenergic receptors. In overdose: bradycardia (reduced SA node automaticity), decreased AV conduction (AV block), reduced myocardial contractility (cardiogenic shock), and bronchospasm. Membrane-stabilizing activity (MSA/sodium channel blockade) in lipophilic agents (propranolol, acebutolol) contributes to QRS widening and ventricular arrhythmia. Propranolol is uniquely dangerous: high lipophilicity → rapid CNS penetration → seizures and coma independent of hemodynamic status.

**Drug-Specific Features:**
- **Propranolol:** Highest CNS toxicity (seizures, coma), sodium channel blockade (wide QRS), highest lipophilicity. Most toxic beta-blocker in overdose. ILE may be beneficial.
- **Metoprolol, atenolol (cardioselective):** Primarily cardiac effects; less CNS toxicity; extended-release formulations cause delayed presentation.
- **Sotalol:** Unique risk of QTc prolongation and torsades de pointes via potassium channel blockade — treat with magnesium, overdrive pacing; does not respond to glucagon
- **Carvedilol:** Alpha and beta blockade; refractory vasodilation; CCB-like features

**Clinical Presentation:**
- Bradycardia (sinus or junctional), AV block (1st, 2nd, 3rd degree)
- Hypotension (cardiogenic, +/- distributive with beta-2 blockade)
- Bronchospasm (especially non-selective agents in asthma/COPD patients)
- Altered mental status (may be from reduced cardiac output; direct CNS with propranolol)
- Seizures (propranolol, acebutolol — can occur before hemodynamic compromise)
- Coma (propranolol)
- Wide QRS complex (propranolol, acebutolol — sodium channel effect)
- Hypoglycemia (impaired glycogenolysis, especially in pediatric patients and diabetics)

**Contrast with CCB Overdose:**
- Beta-blocker OD: hypoglycemia (blocked glycogenolysis)
- CCB OD: hyperglycemia (blocked beta-cell insulin release)
- Both: bradycardia + hypotension

**Timeline:**
- Immediate-release: onset 30-60 min, peak 1-2 hours
- Extended-release (metoprolol ER, atenolol): delayed onset 4-8h; may be stable for hours before rapid deterioration

## Critical Actions

1. **Glucagon 3-5 mg IV bolus** (first-line antidote for beta-blocker OD). Mechanism: bypasses the beta-receptor and activates adenylyl cyclase through glucagon receptors, increasing cAMP and improving heart rate and contractility. Followed immediately by infusion at 3-5 mg/hr (titrated to response). Reconstitute with NS, not the phenol-containing diluent supplied (phenol diluent causes nausea/vomiting and CNS depression in large doses). Antiemetic pretreatment (ondansetron 4-8 mg IV) reduces nausea.

2. **High-dose insulin euglycemia (HDI)** — start if glucagon insufficient or concurrently in severe toxicity. Regular insulin 1 unit/kg IV bolus, then 1 unit/kg/hr continuous infusion. Glucose 25g (D50W 50 mL) IV concurrently if glucose <250 mg/dL; maintain glucose 150-250 mg/dL with D10W or D25W infusion. Check glucose every 15-30 min. Mechanism: improves myocardial carbohydrate metabolism and inotropy.

3. **Atropine 0.5-1 mg IV** for bradycardia; repeat q3-5 min to max 3 mg. Often ineffective in beta-blocker OD (competitive antagonism of beta-receptor exceeds vagolytic benefit) but safe first attempt with simple bradycardia.

4. **Calcium chloride 10% 20-30 mL IV** — less effective than in CCB OD but reasonable adjunct. Reasonable to give simultaneously as part of empiric antidote cocktail.

5. **Sodium bicarbonate 1-2 mEq/kg IV** for QRS widening >100 ms (propranolol sodium channel blockade). Alkalinization and sodium load reduces sodium channel blockade. Target serum pH 7.45-7.55. Follow with continuous infusion in D5W if QRS improvement sustained.

6. **IV lipid emulsion (ILE)** for propranolol or other lipophilic BB with hemodynamic instability or CNS toxicity. 20% ILE 1.5 mL/kg IV bolus, then 0.25 mL/kg/min infusion for 30-60 min (max 10 mL/kg total). Use particularly for propranolol cardiac arrest.

7. **Vasopressors** — norepinephrine 0.1-2 mcg/kg/min IV for refractory hypotension. Epinephrine if combined alpha and beta support needed. Isoproterenol (pure beta agonist) may overcome beta blockade: 2-10 mcg/min IV titrated; high doses may be needed.

8. **Transcutaneous or transvenous pacing** for complete AV block unresponsive to pharmacologic therapy.

9. **Seizures (propranolol):** benzodiazepines first-line (lorazepam 0.1 mg/kg IV or diazepam 0.1-0.2 mg/kg IV). Propofol infusion for refractory seizures. Do not use phenytoin (no benefit in toxin-induced seizures, may worsen conduction).

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Calcium channel blocker overdose | Hyperglycemia; glucagon less effective; calcium + HDI primary |
| Digoxin toxicity | Bidirectional VT, specific ECG patterns, elevated digoxin level |
| Clonidine/imidazoline OD | Miosis, similar bradycardia; partial naloxone response; less cardiac depression |
| Sinus node dysfunction (intrinsic) | No ingestion history, may have structural disease |
| Inferior MI with vagal bradycardia | ST elevation in II/III/aVF; troponin elevation |
| Organophosphate poisoning | SLUDGE/DUMBELS toxidrome; bronchospasm; miosis; atropine first-line |

## Workup

**Labs:**
- BMP — glucose (hypoglycemia!), electrolytes, creatinine
- Glucose: check immediately and every 15-30 min during HDI
- Lactate — tissue perfusion marker; guides resuscitation
- Troponin — myocardial injury from prolonged shock
- CBC
- Acetaminophen and salicylate levels (co-ingestion screen in intentional)
- Quantitative beta-blocker levels: not clinically useful in real time; do not delay treatment

**ECG:**
- Sinus bradycardia, junctional rhythm, or AV block
- QRS >100 ms: sodium channel blockade (propranolol) → start NaHCO3
- QTc prolongation: sotalol — risk of torsades
- Assess continuously for progression

**Monitoring:**
- Continuous telemetry
- Glucose every 15-30 min during HDI
- Arterial line for beat-to-beat BP in hemodynamically unstable patients

## Treatment

**GI Decontamination:**
- Activated charcoal 1 g/kg PO (max 50g) within 1-2 hours
- Extended-release formulations: whole bowel irrigation with polyethylene glycol 1-2 L/hr until clear rectal effluent

**Pharmacologic Cascade (escalate rapidly in deteriorating patients — give multiple agents concurrently in severe toxicity):**

1. **Atropine** 0.5-1 mg IV (max 3 mg) — rapid first attempt
2. **Glucagon** 3-5 mg IV bolus + 3-5 mg/hr infusion — first-line antidote; onset 2-5 min
3. **HDI** 1 unit/kg bolus + 1 unit/kg/hr infusion with glucose supplementation
4. **Calcium chloride** 10% 20-30 mL IV — adjunct, especially if CCB co-ingestion possible
5. **NaHCO3** 1-2 mEq/kg IV if QRS >100 ms (propranolol)
6. **ILE** 20% 1.5 mL/kg bolus + 0.25 mL/kg/min (for lipophilic agents, cardiac arrest)
7. **Vasopressors**: norepinephrine, isoproterenol
8. **Pacing** (transcutaneous/transvenous)
9. **ECMO** for refractory cardiogenic shock or arrest

**Sotalol — Special Management:**
- Sotalol OD does not respond to glucagon
- Risk: torsades de pointes from QTc prolongation
- Magnesium sulfate 2g IV over 5-15 min for torsades or QTc >550 ms
- Overdrive pacing (100-120 bpm) to suppress torsades
- Isoproterenol 2-10 mcg/min IV (increases HR, reduces QTc)
- HD clears sotalol — call nephrology early

## Disposition

**ICU for all symptomatic patients and all extended-release ingestions.**

**ICU:**
- Any bradycardia, hypotension, AV block, QRS widening
- Seizures or altered mental status (propranolol)
- Active infusions (glucagon, HDI, vasopressors)
- Extended-release formulation — minimum 24h monitored observation

**Monitored Observation:**
- Asymptomatic immediate-release ingestion: minimum 6-8h
- Asymptomatic extended-release: minimum 24h
- Serial ECGs, glucose monitoring

**Discharge:**
- Normal vitals, ECG, and glucose throughout observation
- Confirmed declining or sub-toxic drug levels if available
- Psychiatric evaluation if intentional

## Pitfalls

1. **Reconstituting glucagon with the phenol-containing diluent in the kit at large doses.** The standard glucagon reconstitution kit contains a phenol-based diluent. At doses of 3-10 mg, the phenol volume becomes large enough to cause nausea, vomiting, and CNS depression. Reconstitute with 0.9% NS instead. Pretreat with antiemetics.

2. **Diagnosing propranolol seizures as primary neurological events.** Propranolol crosses the blood-brain barrier rapidly due to high lipophilicity. Seizures and coma can occur with normal blood pressure or before cardiovascular collapse. A seizing patient on propranolol who just overdosed needs the full antidote cascade — not just a seizure workup.

3. **Not starting HDI early enough.** HDI is frequently delayed as a "second-line" agent while glucagon is given multiple doses. In severe toxicity, start HDI concurrently with glucagon. The cardiac metabolic derangement causing cardiogenic shock requires insulin-mediated carbohydrate delivery to the myocardium — glucagon raises cAMP but does not address the energy substrate problem.

4. **Missing extended-release toxicity at initial presentation.** A patient who took metoprolol ER 1 hour ago and has a HR of 60 and BP of 110/70 may be normal. That same patient 8 hours later may have complete heart block. Extended-release beta-blockers require 24-hour observation. The initial presentation does not predict the nadir.

5. **Using phenytoin for seizures.** Phenytoin is ineffective for toxin-induced seizures and has sodium channel blocking activity that may worsen conduction in propranolol OD. Use benzodiazepines exclusively for seizure management in beta-blocker overdose.

6. **Forgetting hypoglycemia.** Beta-blockade impairs catecholamine-stimulated glycogenolysis and masks tachycardia as the first sign of hypoglycemia. A bradycardic beta-blocker OD patient may have a glucose of 30 mg/dL. Check glucose immediately and monitor every 15-30 min during HDI therapy.