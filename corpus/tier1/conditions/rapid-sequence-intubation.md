---
id: rapid-sequence-intubation
condition: Rapid Sequence Intubation
aliases: [RSI, rapid sequence induction, crash airway induction]
icd10: [T88.4XXA, Z53.09, J96.00]
esi: 1
time_to_harm:
  irreversible_injury: "< 4 minutes (anoxic brain injury from hypoxia)"
  death: "< 8 minutes without oxygenation"
  optimal_intervention_window: "< 60 seconds from apnea to tube placement"
mortality_if_delayed: "Each failed attempt increases aspiration risk 4-fold; desaturation below 70% associated with cardiac arrest"
category: procedural
track: tier1
sources:
  - type: guideline
    ref: "Kornas RL, Owyang CG, Engel EA, et al. Society of Critical Care Medicine Clinical Practice Guidelines for Rapid Sequence Intubation in the Critically Ill Adult Patient. Crit Care Med. 2023;51(10):1411-1425."
    pmid: "37707379"
  - type: guideline
    ref: "Apfelbaum JL, Hagberg CA, Connis RT, et al. 2022 American Society of Anesthesiologists Practice Guidelines for Management of the Difficult Airway. Anesthesiology. 2022;136(1):31-81."
    pmid: "34762729"
  - type: review
    ref: "Brown CA III, Bair AE, Pallin DJ, et al. Techniques, success, and adverse events of emergency department adult intubations. Ann Emerg Med. 2015;65(4):363-370."
    pmid: "25533140"
  - type: pubmed
    ref: "Driver BE, Prekker ME, Klein LR, et al. Effect of Use of a Bougie vs Endotracheal Tube and Stylet on First-Attempt Intubation Success Among Patients With Difficult Airways Undergoing Emergency Intubation: A Randomized Clinical Trial. JAMA. 2018;319(21):2179-2189."
    pmid: "29800096"
  - type: guideline
    ref: "ATLS Advanced Trauma Life Support, 10th Edition. American College of Surgeons. 2018."
last_updated: "2026-03-01"
compiled_by: agent
risk_tier: A
validation:
  automated_consistency_check: null
  dose_range_validator: null
  unit_normalization_check: null
  cross_file_consistency_check: null
  citation_presence_check: null
  duplicate_content_check: null
  outlier_detection_flag: clear
  schema_version: "2.0"
  provenance_links: []
---
# Rapid Sequence Intubation

## Recognition

**Indications:**
- Airway protection in patients unable to maintain patency (GCS <= 8, loss of gag/cough)
- Respiratory failure refractory to noninvasive ventilation (PaO2 < 60 despite high-flow O2, PaCO2 > 60 with acidosis)
- Anticipated clinical deterioration (expanding neck hematoma, inhalation injury, angioedema)
- Need for controlled ventilation (severe TBI requiring PaCO2 management, status epilepticus)
- Facilitation of diagnostic/therapeutic procedures requiring deep sedation and airway protection

**Contraindications:**
- Known or suspected difficult airway where paralysis would eliminate all rescue options (relative — use awake intubation instead)
- Complete upper airway obstruction where bag-mask ventilation is impossible (proceed directly to surgical airway)
- Patient who can be managed with noninvasive strategies (high-flow nasal cannula, BiPAP)

**Airway Assessment (rapid, <30 seconds):**
- LEMON mnemonic: Look externally (facial trauma, obesity, short neck), Evaluate 3-3-2 rule (mouth opening 3 fingers, hyoid-to-chin 3 fingers, thyroid-to-mouth floor 2 fingers), Mallampati score, Obstruction (history of OSA, stridor, mass), Neck mobility
- Prior intubation history if available
- Identify need for awake technique vs RSI vs crash airway

## Critical Actions

| Action | Target |
|--------|--------|
| Preoxygenation | >= 3 minutes or SpO2 >= 95% |
| Apnea to tube confirmation | < 60 seconds |
| First-pass success | Goal > 85% |
| ETCO2 confirmation | Immediately post-intubation |

**The 7 Ps of RSI:**

**1. Preparation (t-10 min):**
- Equipment: ETT (7.0-8.0 men, 6.5-7.5 women), stylet or bougie, laryngoscope (video preferred), BVM, suction (Yankauer), ETCO2, backup airway (SGA, surgical kit)
- Two functioning IV lines
- Monitoring: continuous SpO2, ETCO2, cardiac monitor, BP
- Position: sniffing position (ear-to-sternal-notch alignment); ramped position for obese patients
- Assign roles: intubator, medication pusher, cricoid pressure, recorder

**2. Preoxygenation (t-5 to t-0):**
- Non-rebreather at 15 L/min flush rate x 3 minutes (goal: denitrogenation of FRC)
- Apneic oxygenation: nasal cannula at 15 L/min throughout procedure (continued during laryngoscopy)
- BVM preoxygenation if SpO2 < 93% despite NRB
- Target SpO2 >= 95% before induction; accept >= 90% in critically ill if plateau reached

**3. Pretreatment (t-3 min, situational):**
- Fentanyl 1-3 mcg/kg IV over 60 seconds — blunts sympathetic response to laryngoscopy (use in aortic dissection, intracranial hemorrhage, severe hypertension)
- Lidocaine 1.5 mg/kg IV — reactive airways disease (evidence weak; optional)
- Atropine 0.02 mg/kg IV (min 0.1 mg) — pediatric patients < 1 year receiving succinylcholine (prevents bradycardia)

**4. Paralysis with Induction (t-0):**

| Agent | Dose | Onset | Duration | Notes |
|-------|------|-------|----------|-------|
| **Induction** | | | | |
| Ketamine | 1.5-2 mg/kg IV | 45-60 sec | 10-20 min | Hemodynamically stable; bronchodilator; first-line in sepsis/hypotension |
| Etomidate | 0.3 mg/kg IV | 15-45 sec | 3-12 min | Hemodynamically neutral; avoid in septic shock (adrenal suppression) |
| Propofol | 1.5-2 mg/kg IV | 15-45 sec | 5-10 min | Reduces ICP; causes hypotension — avoid if SBP < 100 |
| Midazolam | 0.1-0.3 mg/kg IV | 60-90 sec | 15-30 min | Slowest onset; worst hemodynamic profile; last resort |
| **Paralytic** | | | | |
| Succinylcholine | 1.5 mg/kg IV | 45-60 sec | 6-10 min | Fastest onset; contraindicated in hyperkalemia risk (burns >48h, crush >48h, denervation, neuromuscular disease) |
| Rocuronium | 1.2 mg/kg IV | 60-90 sec | 40-60 min | Comparable onset to succinylcholine at RSI dose; reversible with sugammadex 16 mg/kg |

**5. Protection and Positioning (t+0):**
- Cricoid pressure (Sellick maneuver): 10 N before induction, 30 N after loss of consciousness — controversial; release if impairs glottic view
- Maintain apneic oxygenation via nasal cannula at 15 L/min

**6. Placement (t+30 sec):**
- Video laryngoscopy preferred (higher first-pass success in ED: 91% vs 84%)
- Insert blade, identify epiglottis, lift to expose vocal cords (Cormack-Lehane grade)
- Pass bougie or styletted ETT through cords under direct visualization
- Inflate cuff, remove stylet/bougie
- Confirm placement: waveform capnography (MANDATORY), bilateral breath sounds, chest rise, SpO2

**7. Post-Intubation Management (t+2 min):**
- Secure tube (tape or commercial holder); note depth at teeth (typically 21-23 cm in adults)
- CXR to confirm position (2-4 cm above carina)
- Initiate ventilator: AC mode, TV 6-8 mL/kg IBW, RR 14-16, PEEP 5, FiO2 100% then wean
- Post-intubation sedation: propofol 5-50 mcg/kg/min OR midazolam 1-5 mg/hr + fentanyl 25-100 mcg/hr OR ketamine 0.1-0.5 mg/kg/hr
- Post-intubation analgesia: fentanyl 25-100 mcg/hr
- Arterial blood gas within 30 minutes

## Differential Diagnosis

**Alternative Airway Strategies:**

| Approach | When to Use |
|----------|------------|
| Awake intubation (topical + sedation) | Predicted difficult airway, anticipated CICO |
| Delayed sequence intubation (DSI) | Combative/agitated patient unable to tolerate preoxygenation; ketamine 1 mg/kg IV for dissociation, then preoxygenate, then RSI |
| Supraglottic airway (iGel, LMA) | Rescue after failed intubation; bridge to surgical airway |
| Bag-valve-mask ventilation | Temporizing; two-person technique for optimal seal |
| High-flow nasal cannula / NIV | If intubation not yet indicated; trial of noninvasive support |
| Surgical cricothyrotomy | CICO — failed intubation AND failed SGA AND failed BVM |
| Fiberoptic intubation | Awake technique for anticipated difficult airway (rarely available emergently) |

## Workup

**Pre-Procedure Assessment:**
- SpO2, ETCO2 (if available pre-intubation), vital signs
- Focused airway exam: mouth opening, neck mobility, Mallampati (if cooperative), neck circumference
- Point-of-care ultrasound: submental view to identify epiglottis/airway anatomy (optional, time-permitting)
- Review for contraindications to succinylcholine: hyperkalemia, burns > 48 hours, neuromuscular disease, malignant hyperthermia history, denervation injury > 48 hours

**Equipment Checklist:**

| Item | Specification |
|------|---------------|
| ETT | 7.0-8.0 (men), 6.5-7.5 (women); one size smaller available |
| Laryngoscope | Video laryngoscope (preferred) + direct laryngoscope backup |
| Bougie | 60 cm coude-tip gum elastic bougie |
| Stylet | Malleable; hockey-stick configuration |
| BVM | Connected to O2 at 15 L/min with PEEP valve |
| Suction | Yankauer + large-bore suction (DuCanto or similar) |
| ETCO2 | Waveform capnography (colorimetric as backup only) |
| Nasal cannula | At 15 L/min for apneic oxygenation |
| Backup airway | iGel or LMA (size 4 women, size 5 men) |
| Surgical kit | 10-blade, bougie, 6.0 ETT (for surgical airway) |

## Treatment

### Induction Agent Selection by Clinical Scenario

| Scenario | First-Line | Rationale |
|----------|-----------|-----------|
| Hypotension / septic shock | Ketamine 1.5 mg/kg IV | Sympathomimetic; maintains BP |
| Elevated ICP / TBI | Ketamine 1.5 mg/kg IV or propofol 1.5 mg/kg IV | Ketamine does not raise ICP (prior dogma refuted); propofol lowers ICP but drops MAP |
| Status asthmaticus | Ketamine 1.5-2 mg/kg IV | Bronchodilator |
| Status epilepticus | Propofol 1.5-2 mg/kg IV or midazolam 0.2 mg/kg IV | Anticonvulsant properties |
| Cardiac disease / stable hemodynamics | Etomidate 0.3 mg/kg IV | Hemodynamically neutral |
| Anaphylaxis | Ketamine 1.5 mg/kg IV | Bronchodilation + hemodynamic support |

### Failed First Attempt Protocol
1. Return to BVM ventilation with two-person technique + oral airway
2. Reposition (ear-to-sternal-notch, external laryngeal manipulation)
3. Change blade type or size (hyperangulated if using standard geometry)
4. Use bougie if not used on first attempt
5. If second attempt fails: insert supraglottic airway (iGel/LMA)
6. If SGA fails: proceed to surgical cricothyrotomy
7. Maximum 3 laryngoscopy attempts before declaring failed airway

### Medication Doses for Special Populations

**Obesity:** dose induction agents on ideal body weight (IBW); dose succinylcholine on total body weight (TBW); dose rocuronium on IBW
**Pediatric:** ketamine 1-2 mg/kg IV; rocuronium 1.2 mg/kg IV; succinylcholine 2 mg/kg IV (< 10 kg) or 1.5 mg/kg IV (> 10 kg); atropine 0.02 mg/kg IV pretreatment if < 1 year
**Elderly:** reduce propofol dose by 30-50%; etomidate or ketamine at standard doses

## Disposition

- **Successful intubation:** ICU admission for mechanical ventilation; CXR confirmation; ABG within 30 minutes
- **Difficult intubation requiring multiple attempts:** document difficulty in chart; consider early tracheostomy consultation if prolonged ventilation anticipated
- **Failed intubation requiring surgical airway:** ICU admission; ENT/surgery consultation for airway conversion within 24-72 hours
- **Transfer:** if facility lacks ICU ventilator capability, intubate, stabilize, and arrange emergent transfer with ongoing ventilation and sedation

## Pitfalls

1. **Inadequate preoxygenation leading to desaturation during laryngoscopy.** The apneic window after RSI paralytic administration is only 3-5 minutes in a well-preoxygenated adult, but drops to < 60 seconds in obese, pregnant, or critically ill patients. Always achieve maximum preoxygenation before induction. Continue apneic oxygenation with 15 L/min nasal cannula during laryngoscopy.

2. **Using etomidate in septic shock.** Single-dose etomidate causes measurable adrenal suppression for 24-48 hours. While the mortality impact is debated, ketamine avoids this risk entirely and provides hemodynamic support through sympathomimetic effects. SCCM 2023 guidelines suggest avoiding etomidate in septic shock.

3. **Administering succinylcholine to patients with occult hyperkalemia risk.** Burns > 48 hours, crush injury > 48 hours, prolonged immobilization, neuromuscular disease, and spinal cord injury > 48 hours all cause upregulation of extrajunctional acetylcholine receptors. Succinylcholine in these patients triggers massive potassium efflux (K+ rise of 5-10 mEq/L), causing fatal cardiac arrest. Use rocuronium 1.2 mg/kg IV instead.

4. **Failure to have a backup plan before administering the paralytic.** Once succinylcholine or rocuronium is given, the patient cannot breathe independently. Before pushing the paralytic, verbalize the plan: "If I cannot intubate, I will place an iGel. If the iGel fails, I will perform a surgical airway." Having the surgical kit open at the bedside.

5. **Not using a bougie on the first attempt in difficult airways.** The BEAM trial (JAMA 2018) demonstrated significantly higher first-pass success with bougie compared to ETT + stylet in difficult airways (96% vs 82%). Bougie should be the default adjunct for emergency intubation.

6. **Forgetting post-intubation sedation after paralysis.** Rocuronium lasts 40-60 minutes. Without sedation, the patient is awake and paralyzed — a terrifying experience with hemodynamic consequences. Start continuous sedation (propofol or midazolam + fentanyl) immediately after confirming tube placement.

7. **Relying on auscultation alone for tube confirmation.** Esophageal intubation is lethal if unrecognized. Waveform capnography is the gold standard — flat ETCO2 tracing = esophageal placement until proven otherwise. Auscultation is unreliable in noisy resuscitation environments.
