# Red Team Review Checklist

Category-specific reference for automated and physician review of OpenEM conditions.

## Universal Checks (All Categories)

### Dosing Completeness
- [ ] Every drug dose includes route (IV/IM/PO/IO/SQ/SL/IN/PR)
- [ ] Every drug dose includes frequency or timing (q5min, once, infusion rate)
- [ ] Weight-based dosing has max dose cap where applicable
- [ ] Concentrations explicit (epinephrine 1:1,000 IM vs 1:10,000 IV or mg/mL)

### Critical Actions Quality
- [ ] No hedging language ("consider", "may want to", "if available", "if possible")
- [ ] Time targets stated (e.g., "within 10 minutes", "< 90 minutes")
- [ ] Actions are imperative and specific

### time_to_harm
- [ ] Tier A: structured object with `irreversible_injury`, `death`, `optimal_intervention_window`
- [ ] Values are specific (not "variable", "depends", "varies")
- [ ] Clinically accurate time windows

### Mortality
- [ ] `mortality_if_delayed` field present with numeric value
- [ ] Percentage or rate cited (not vague qualifiers)

### Pitfalls
- [ ] At least 7 pitfalls listed for tier A conditions
- [ ] Pitfalls are clinically actionable (not generic advice)
- [ ] Common cognitive errors and diagnostic traps included

### Source Currency
- [ ] At least one source from the last 5 years (>= 2021)
- [ ] Guidelines are current edition (not superseded)

### Dangerous Combinations
- [ ] Succinylcholine: warned against in hyperkalemia, organophosphate, malignant hyperthermia, crush injury
- [ ] Calcium chloride: "central line only" or peripheral administration warning
- [ ] Beta-blockers: warned against in cocaine toxicity
- [ ] Epinephrine: concentration specified (1:1,000 IM vs 1:10,000 IV)
- [ ] Flumazenil: warned against in mixed overdose or chronic benzodiazepine use

---

## Category-Specific Checks

### Cardiovascular
- [ ] Reperfusion/intervention time target stated (e.g., door-to-balloon < 90 min)
- [ ] Anticoagulation dosing is weight-based where applicable (units/kg)
- [ ] Antiplatelet therapy matches current ACC/AHA or ESC guidelines
- [ ] Hemodynamic targets stated (MAP, SBP goals)
- [ ] STEMI equivalents mentioned where relevant (posterior MI, Wellens, de Winter)

### Toxicologic
- [ ] Antidote dose + route correct and stated
- [ ] Max dose stated or "no maximum" explicitly documented
- [ ] Decontamination timing window stated (e.g., charcoal within 1-2 hours)
- [ ] Toxidrome recognition pattern included
- [ ] Dialysis/elimination enhancement indications listed where applicable
- [ ] Observation/monitoring duration stated

### Obstetric-Gynecologic
- [ ] Magnesium sulfate toxicity thresholds stated (reflexes, respiratory depression, serum levels)
- [ ] Fetal considerations addressed (monitoring, delivery indications)
- [ ] Gestational age cutoffs stated (viability threshold, term vs preterm management)
- [ ] Rh status consideration mentioned where applicable
- [ ] Uterotonic agents with dosing and contraindications

### Neurological
- [ ] Seizure medication dosing uses mg/kg for second-line agents
- [ ] Herniation signs listed (blown pupil, posturing, Cushing response)
- [ ] Thrombolytic eligibility criteria and time windows stated
- [ ] Blood pressure targets specific to condition
- [ ] Neurosurgical consultation indications listed

### Infectious
- [ ] Empiric antibiotic timing stated ("within 1 hour" or specific target)
- [ ] Blood cultures before antibiotics explicitly mentioned
- [ ] Source control timing addressed
- [ ] Immunocompromised host considerations
- [ ] Antibiotic doses weight-based or renal-adjusted where applicable

### Pediatric
- [ ] All doses weight-based (mg/kg or mcg/kg)
- [ ] Max adult dose cap stated for each medication
- [ ] Age-appropriate normal values referenced
- [ ] Equipment sizing guidance (Broselow, length-based)
- [ ] Weight estimation method mentioned if applicable

### Disaster-MCI
- [ ] Triage algorithm named (SALT, START, JumpSTART)
- [ ] Resource allocation criteria stated (immediate/delayed/minor/expectant)
- [ ] Command structure referenced (ICS)
- [ ] Surge capacity considerations
- [ ] Decontamination protocols if chemical/radiation

### Procedural
- [ ] Equipment list or setup checklist present
- [ ] Contraindications listed (absolute and relative)
- [ ] Complication rates cited with percentages
- [ ] Step-by-step procedural technique described
- [ ] Alternative approaches if primary fails

### Environmental
- [ ] Temperature management targets stated (cooling/rewarming rates)
- [ ] Monitoring parameters during treatment
- [ ] Specific rewarming/cooling methods with rates
- [ ] Complication monitoring (dysrhythmia, coagulopathy)

### Traumatic
- [ ] Hemorrhage control priorities (tourniquet, packing, intervention)
- [ ] Transfusion thresholds and ratios (1:1:1 or equivalent)
- [ ] Imaging decision points (CT timing, FAST exam)
- [ ] Surgical consultation indications
- [ ] Damage control resuscitation principles if applicable

### Respiratory
- [ ] Airway management decision points (when to intubate)
- [ ] Ventilator settings if mentioned (tidal volume, PEEP, FiO2)
- [ ] Non-invasive ventilation indications and contraindications
- [ ] Adjunct therapies with dosing (nebulizers, steroids)

### Hematologic
- [ ] Transfusion targets and ratios stated
- [ ] Component therapy indications (FFP, platelets, cryo)
- [ ] Reversal agents for anticoagulants with dosing
- [ ] Massive transfusion protocol activation criteria

### Endocrine-Metabolic
- [ ] Electrolyte correction rates stated (avoid overcorrection)
- [ ] Monitoring intervals specified
- [ ] Insulin dosing protocols if applicable
- [ ] Stress-dose steroid indications and dosing

---

## Running the Red Team Review

```bash
# Phase A only (deterministic checks)
python scripts/red_team_review.py

# Phase A + B (with LLM-augmented review of flagged conditions)
python scripts/red_team_review.py --llm

# JSON output in addition to YAML/MD
python scripts/red_team_review.py --json
```

### Output Files
| File | Purpose |
|------|---------|
| `review/tier_a_review_cards.yaml` | Machine-readable review results |
| `review/tier_a_review_cards.md` | Physician-friendly markdown with checkboxes |
| `review/RED_TEAM_CHECKLIST.md` | This file — category-specific reference |

### Severity Levels
| Level | Meaning | Action |
|-------|---------|--------|
| **critical** | Patient safety risk — immediate correction required | Block review sign-off |
| **major** | Clinical accuracy concern — physician review required | Must address before sign-off |
| **minor** | Quality improvement — should fix but not blocking | Document and schedule fix |
| **info** | Informational — no action required | Note for future updates |
