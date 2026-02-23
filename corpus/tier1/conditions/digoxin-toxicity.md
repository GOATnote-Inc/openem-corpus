---
id: digoxin-toxicity
condition: Digoxin Toxicity
aliases: [digitalis toxicity, digoxin overdose, digitalis poisoning]
icd10: [T46.0X1A, T46.0X2A]
esi: 2
time_to_harm: "< 2 hours for acute massive ingestion; chronic toxicity onset over days"
category: toxicologic
track: tier1
sources:
  - type: pubmed
    ref: "Chan BS, Buckley NA. Digoxin-specific antibody fragments in the treatment of digoxin toxicity. Clin Toxicol (Phila) 2014;52(8):824-836"
    pmid: "25089790"
  - type: pubmed
    ref: "Antman EM et al. Treatment of 150 cases of life-threatening digitalis intoxication with digoxin-specific Fab antibody fragments. Final report of a multicenter study. Circulation 1990;81(6):1744-1752"
    pmid: "2188752"
  - type: pubmed
    ref: "Lapostolle F et al. Digoxin-specific Fab fragment-induced hypokalaemia in digoxin-intoxicated patients. Eur Heart J 2008;29(19):2376-2381"
    pmid: "18682436"
  - type: pubmed
    ref: "Ma G et al. Electrocardiographic manifestations: digitalis toxicity. J Emerg Med 2001;20(2):145-152"
    pmid: "11207397"
  - type: guideline
    ref: "American Heart Association. Management of Cardiac Glycoside Toxicity. AHA Scientific Statement 2020"
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
# Digoxin Toxicity

## Recognition

**Pathophysiology:** Digoxin inhibits the Na+/K+-ATPase pump, increasing intracellular Na+ and secondarily increasing intracellular Ca2+ (via Na+/Ca2+ exchanger). In therapeutic use: increases myocardial contractility and slows AV nodal conduction. In toxicity: intracellular calcium overload → ventricular automaticity (triggered activity), combined with vagally mediated bradycardia and AV block. Bidirectional ventricular tachycardia results from alternating ventricular foci driven by calcium overload.

**Two Distinct Toxicity Patterns:**

*Acute Overdose (single massive ingestion):*
- Typically intentional; younger patients; initially well
- Severe nausea/vomiting within 2-4 hours
- Profound bradycardia, AV block, ventricular arrhythmias
- **Hyperkalemia** (Na+/K+-ATPase inhibition → K+ leaves cells → serum K+ rises)
- Serum digoxin levels >2 ng/mL, often 5-20+ ng/mL
- Digoxin levels do NOT reflect tissue distribution for 6+ hours post-ingestion — acute level may be high but tissue distribution incomplete

*Chronic Toxicity (accumulation in therapeutic use):*
- Elderly patients on long-term digoxin; dose unchanged but renal function declined
- Insidious onset over days
- GI: nausea, vomiting, anorexia, weight loss
- CNS: visual disturbances (yellow-green halos, altered color perception), confusion, fatigue, weakness
- Cardiac: bradycardia, AV block, PACs, PVCs, atrial tachycardia with AV block (highly specific)
- **Hypokalemia** common (often from concurrent diuretic use — hypokalemia sensitizes the myocardium to digoxin toxicity)
- Serum level: may be only 2-4 ng/mL; toxicity occurs at lower levels than acute OD because of chronic tissue saturation

**ECG Findings:**
- Scooped ("Salvador Dali mustache") ST-segment changes — a marker of digoxin effect, not toxicity per se
- PACs, PVCs, bidirectional VT (pathognomonic for digoxin toxicity)
- Atrial tachycardia with AV block (PAT with block) — highly specific
- Junctional tachycardia, accelerated junctional rhythm
- Sinus bradycardia, SA block, AV block of any degree
- Regularized atrial fibrillation (loss of variable AV conduction) may indicate dig toxicity

**Bidirectional VT:** Beat-to-beat alternation of QRS axis/morphology. Pathognomonic for digoxin toxicity (also seen with catecholaminergic polymorphic VT and aconite poisoning). Highly unstable — treat immediately with Digifab.

**Other Cardiac Glycoside Sources:**
- Oleander (Nerium oleander), foxglove (Digitalis purpurea) — botanical cardiac glycoside exposure; cross-reacts with digoxin assay
- Bufo toad skin secretions (toad licking, aphrodisiacs)
- Chan Su (Chinese herbal preparation)

## Critical Actions

1. **Digoxin-specific antibody fragments (DigiFab) — antidote.** Give for: life-threatening arrhythmias, bidirectional VT, hemodynamic instability, severe bradycardia/AV block, serum K+ >5.5 mEq/L (acute OD), altered mental status.

   *Dose calculation:*
   - **Known acute ingestion:** Vials = (mg ingested × 0.8) / 0.5. One vial (40 mg of Fab) binds ~0.5 mg of digoxin.
   - **Known serum level:** Vials = (serum level ng/mL × weight kg) / 100. Or for chronic: (serum level × weight × 0.56) / 1000 × 2.
   - **Empiric dosing:** Acute life-threatening: 10-20 vials IV. Chronic life-threatening: 5-10 vials IV. Infuse over 30 minutes (bolus IV push for cardiac arrest).
   - After DigiFab: total serum digoxin level will RISE dramatically (Fab-bound digoxin measured but inactive). Do NOT recheck digoxin levels for 7 days — free digoxin level only meaningful; total level is misleading.

2. **Do NOT cardiovert or defibrillate digoxin-toxic VT if hemodynamically tolerated.** Digoxin toxicity markedly increases myocardial irritability. DC cardioversion precipitates refractory VF in digoxin-toxic patients. Use DigiFab for arrhythmia control. If cardioversion is absolutely necessary (PEA arrest), use lowest energy possible and have DigiFab immediately available.

3. **Atropine 0.5-1 mg IV** for symptomatic bradycardia while preparing DigiFab. Temporary measure only.

4. **Correct hypokalemia in chronic toxicity** — hypokalemia potentiates digoxin binding to Na+/K+-ATPase and worsens toxicity. KCl 10-20 mEq/hr IV via central line for K+ <3.5 mEq/L with ECG changes.

5. **Do NOT aggressively correct hyperkalemia in acute overdose.** In acute digoxin OD, hyperkalemia is the result of Na+/K+-ATPase inhibition — it is the toxic mechanism, not an independent problem. Treating hyperkalemia with calcium (calcium gluconate) carries theoretical risk of "stone heart" (hypercalcemia + digoxin-induced calcium overload → irreversible tetanic cardiac contraction). DigiFab will correct the hyperkalemia by restoring Na+/K+-ATPase function. If K+ >6.5 mEq/L with ECG changes and DigiFab is unavailable or delayed: sodium bicarbonate, insulin/dextrose, kayexalate — avoid calcium if possible.

6. **Activated charcoal 1 g/kg PO** if acute ingestion within 1-2 hours and airway protected.

7. **Hemodialysis does NOT clear digoxin** — large volume of distribution (7-8 L/kg). HD is not useful and does not replace DigiFab.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Sick sinus syndrome | No digoxin level elevation, no vomiting or GI symptoms, no ECG bidirectional VT |
| Acute inferior MI | ST elevation in II/III/aVF, troponin elevation, different bradyarrhythmia pattern |
| Hyperkalemia (non-digoxin) | Peaked T waves, wide QRS; serum K+ elevated without digoxin level elevation |
| CCB/BB overdose | No bidirectional VT, different medication history, different antidote |
| Aconite poisoning | Bidirectional VT also seen; aconite herbal exposure history, no digoxin level |
| Catecholaminergic polymorphic VT | Bidirectional VT; exercise-triggered; no medication/ingestion history; young patient |

## Workup

**Labs:**
- Serum digoxin level — therapeutic: 0.5-2.0 ng/mL; toxic: >2 ng/mL (but level interpretation requires clinical context)
  - In acute ingestion, draw level ≥6 hours post-ingestion (tissue distribution not complete earlier)
  - In chronic toxicity, draw trough level (any time)
- Electrolytes — potassium is critical: hypokalemia (chronic) or hyperkalemia (acute)
- Creatinine/BMP — renal failure is the most common cause of chronic dig toxicity (reduced clearance)
- Magnesium — hypomagnesemia potentiates toxicity; replace to Mg2+ >2 mg/dL
- Digoxin level in oleander/foxglove exposure: cross-reacts with immunoassay, may give falsely low or inaccurate level; treat clinically

**12-Lead ECG:**
- Scooped ST segments ("dig effect") — assess at baseline
- PVCs, PACs, PAT with block, bidirectional VT, AV block (any degree)
- Regularized A-fib — loss of variable AV conduction suggests digoxin toxicity
- Serial ECGs every 30-60 minutes if symptomatic

**Imaging:**
- Chest X-ray — cardiomegaly (underlying HF), pulmonary edema

## Treatment

**DigiFab (see Critical Actions for dosing):**
- Infuse over 30 minutes; IV push in cardiac arrest
- Half-life: 15-20 hours; digoxin rebound can occur at 6-12 hours as Fab is renally cleared — monitor for 24+ hours after DigiFab in renal failure patients
- Response: HR and BP improvement within 30-60 minutes

**Magnesium Sulfate:**
- MgSO4 2g IV over 15 minutes for ventricular arrhythmias (PVCs, VT) not meeting DigiFab criteria
- Correct Mg2+ to >2 mg/dL

**Potassium Replacement (chronic toxicity):**
- KCl 10-20 mEq/hr IV via central line for K+ <3.5 mEq/L
- Hypokalemia correction alone may terminate arrhythmias in mild chronic toxicity

**Pacing:**
- Transvenous pacing for complete AV block with hemodynamic compromise if DigiFab unavailable or insufficient
- Avoid aggressive pacing attempts that could induce VF in digoxin-toxic myocardium
- Isoproterenol 2-10 mcg/min IV as bridge to transvenous pacing

**Lidocaine:**
- Historical use for digoxin-toxic VT (2 mg/kg IV); less used now; second-line after DigiFab
- May suppress ventricular arrhythmias by reducing automaticity

## Disposition

**ICU for all patients with:**
- Hemodynamic instability
- Life-threatening arrhythmia (bidirectional VT, VF, complete AV block)
- Acute massive ingestion
- Post-DigiFab monitoring (minimum 24 hours; 48-72 hours for renal failure)

**Monitored Floor:**
- Symptomatic chronic toxicity with controlled arrhythmia after DigiFab
- GI symptoms with elevated level, hemodynamically stable
- Requires telemetry and serial potassium monitoring

**Discharge:**
- Accidental acute ingestion of small dose, no symptoms, sub-toxic level (drawn ≥6h post-ingestion), normal ECG
- Adjust chronic digoxin dose, correct precipitating factor (renal function, drug interaction), recheck level in 1 week

**Common precipitants of chronic toxicity to address at discharge:**
- Renal function decline (acute illness, NSAID use, contrast exposure, new ACE inhibitor)
- Drug interactions: amiodarone (increases digoxin level ×2), clarithromycin, verapamil, spironolactone
- Hypokalemia from diuretics
- Hypomagnesemia

## Pitfalls

1. **Giving calcium for hyperkalemia in acute digoxin overdose.** Calcium administration is standard management for hyperkalemia-induced cardiac toxicity — but in acute dig OD, the hyperkalemia is a result of Na+/K+-ATPase inhibition, and the myocardium is already calcium-overloaded. Adding exogenous calcium may precipitate "stone heart" — tetanic cardiac contraction. Give DigiFab. Avoid calcium in acute digoxin OD unless DigiFab is unavailable and the patient is in extremis.

2. **Cardioverting digoxin-toxic VT with DC shock.** DC cardioversion in the digoxin-toxic heart precipitates refractory VF. If you must cardiovert for hemodynamic collapse, use the lowest effective energy and have DigiFab immediately available and infusing.

3. **Rechecking digoxin level after DigiFab and acting on the result.** Total serum digoxin level after DigiFab reflects Fab-bound digoxin, which is pharmacologically inactive but measured by the immunoassay. Levels of 10-50 ng/mL post-DigiFab are expected and not an indication for more treatment. Free digoxin level (if your lab can run it) is the only meaningful post-Fab level.

4. **Under-dosing DigiFab for chronic toxicity.** Empiric 5-10 vials is appropriate for chronic life-threatening toxicity — a calculated dose based on serum level is often lower than the empiric dose because the tissue-loaded patient has more total body digoxin than the level reflects. When in doubt, give 10 vials for life-threatening chronic toxicity.

5. **Missing chronic digoxin toxicity in an elderly patient with "just confusion."** Visual changes (yellow/green halos, altered color vision, blurry vision), nausea, and fatigue in an elderly patient on digoxin are cardinal symptoms of chronic toxicity. Check a digoxin level and creatinine in any elderly dig patient with new confusion, arrhythmia, or GI symptoms.

6. **Failing to correct hypomagnesemia.** Hypomagnesemia potentiates digoxin binding and promotes ventricular arrhythmias. Correct Mg2+ to >2 mg/dL in all symptomatic dig-toxic patients, in addition to potassium replacement.