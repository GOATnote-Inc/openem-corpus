---
id: difficult-airway-management
condition: Difficult Airway Management
aliases: [failed airway algorithm, CICO, can't intubate can't oxygenate, difficult intubation, failed intubation]
icd10: [T88.4XXA, J96.00]
esi: 1
time_to_harm:
  irreversible_injury: "< 4 minutes (anoxic brain injury)"
  death: "< 8-10 minutes without oxygenation"
  optimal_intervention_window: "< 3 minutes from failed first attempt"
category: procedural
track: tier1
confusion_pairs:
  - condition: surgical-cricothyrotomy
    differentiators:
      - "Difficult airway management: encompasses the entire decision algorithm from RSI through rescue devices to surgical airway; cricothyrotomy is the final step in the failed airway pathway"
      - "Surgical cricothyrotomy: a specific procedure within the difficult airway algorithm, performed when all non-surgical options have failed (CICO scenario)"
      - "Critical rule: declaring CICO and proceeding to cricothyrotomy should occur after a maximum of 3 failed oral attempts — the algorithm exists to prevent fixation on a failed technique"
sources:
  - type: guideline
    ref: "Apfelbaum JL, Hagberg CA, Connis RT, et al. 2022 American Society of Anesthesiologists Practice Guidelines for Management of the Difficult Airway. Anesthesiology. 2022;136(1):31-81."
    pmid: "34762729"
  - type: guideline
    ref: "Frerk C, Mitchell VS, McNarry AF, et al. Difficult Airway Society 2015 guidelines for management of unanticipated difficult intubation in adults. Br J Anaesth. 2015;115(6):827-848."
    pmid: "26556848"
  - type: pubmed
    ref: "Chrimes N. The Vortex: a universal 'high-acuity implementation tool' for emergency airway management. Br J Anaesth. 2016;117(Suppl 1):i20-i27."
    pmid: "27440673"
  - type: pubmed
    ref: "Brown CA 3rd, Bair AE, Pallin DJ, et al. Techniques, success, and adverse events of emergency department adult intubations. Ann Emerg Med. 2015;65(4):363-370.e1."
    pmid: "25533140"
  - type: review
    ref: "Cook TM, Woodall N, Frerk C; Fourth National Audit Project. Major complications of airway management in the UK: results of the Fourth National Audit Project of the Royal College of Anaesthetists and the Difficult Airway Society. Part 1: anaesthesia. Br J Anaesth. 2011;106(5):617-631."
    pmid: "21447488"
last_updated: "2026-02-26"
compiled_by: agent
risk_tier: A
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
# Difficult Airway Management

## Recognition

**Definition:** A clinical situation where a trained provider experiences difficulty with facemask ventilation, laryngoscopy, endotracheal intubation, or supraglottic airway placement. The "failed airway" is declared when a provider cannot intubate AND cannot oxygenate the patient (CICO — Can't Intubate, Can't Oxygenate).

**LEMON Assessment (pre-intubation evaluation):**
- **L**ook externally: facial trauma, large tongue, obesity, short neck, facial hair, blood/vomit in airway
- **E**valuate 3-3-2: 3 fingers mouth opening, 3 fingers hyomental distance, 2 fingers thyromental distance
- **M**allampati score: Class III-IV associated with difficult laryngoscopy
- **O**bstruction: epiglottitis, angioedema, peritonsillar abscess, neck hematoma, foreign body
- **N**eck mobility: c-spine immobilization, ankylosing spondylitis, rheumatoid arthritis, prior cervical fusion

**Predictors of Difficult Bag-Mask Ventilation (MOANS):**
- **M**ask seal (beard, facial trauma, edentulous)
- **O**besity/obstruction
- **A**ge >55
- **N**o teeth (edentulous — paradoxically difficult for mask seal)
- **S**tiff lungs/snoring (COPD, asthma, OSA)

**Predictors of Difficult Supraglottic Airway (RODS):**
- **R**estricted mouth opening (<2 cm)
- **O**bstruction at or below the glottis
- **D**isrupted airway anatomy (trauma, radiation, tumor)
- **S**tiff lungs/c-spine (high airway pressures, limited positioning)

**Decision Triggers for Difficult Airway Plan:**
- Any LEMON predictor present: prepare backup devices before first attempt
- Known difficult airway history (check for MedicAlert bracelet, anesthesia records)
- Active airway obstruction: angioedema, expanding neck hematoma, thermal inhalation injury
- Anticipated rapid desaturation: obesity, pregnancy, pediatric, shunt physiology

## Critical Actions

| Action | Target |
|--------|--------|
| Pre-oxygenation | 3 minutes or SpO2 >95% before first attempt |
| First intubation attempt | Optimized: positioning, device, operator |
| Maximum oral intubation attempts | 3 (each with a change in technique) |
| Declare CICO | After 3 failed intubation + failed SGA |
| Surgical airway | < 30 seconds from CICO declaration |

1. **Pre-oxygenate aggressively** — nasal cannula 15 L/min (apneic oxygenation) PLUS NRB or BVM at 100% FiO2 for >=3 minutes. Maintain nasal cannula flow during laryngoscopy attempts.
2. **First attempt = best attempt** — optimize all modifiable factors: sniffing position (ear-to-sternal notch alignment), video laryngoscopy as primary device, bougie loaded, most experienced operator
3. **3-attempt maximum for oral intubation** — each attempt must involve a technique change (different blade, different operator, bougie, head position); do not repeat the same failed technique
4. **After failed intubation: supraglottic airway** — insert second-generation SGA (i-gel size 4 for average adult, LMA Supreme); if ventilation achieved, decision: wake patient vs. intubate through SGA vs. proceed with SGA in situ
5. **CICO declared: immediate surgical cricothyrotomy** — do not attempt additional oral techniques; proceed to front-of-neck access within 30 seconds

## Differential Diagnosis

The failed airway is not a differential diagnosis — it is a procedural crisis. The "differential" is the set of alternative techniques and bail-out strategies:

| Technique Level | Options |
|----------------|---------|
| Optimized direct laryngoscopy | Bougie (first-pass adjunct), external laryngeal manipulation (BURP), different blade (Mac vs. Miller), head-elevated position |
| Video laryngoscopy | C-MAC, GlideScope, McGrath, King Vision — superior to direct laryngoscopy for difficult airways (Cormack-Lehane grade III-IV) |
| Supraglottic airway devices | i-gel, LMA Supreme, LMA ProSeal — second-generation devices allow higher seal pressure and gastric drainage |
| Intubation through SGA | Aintree catheter through SGA, or fiberoptic-guided intubation through SGA |
| Blind intubation devices | Intubating LMA (ILMA/Fastrach) — allows blind passage of ETT through the SGA |
| Front-of-neck access | Surgical cricothyrotomy (scalpel-bougie-tube), needle cricothyrotomy with jet ventilation (temporizing only in adults) |
| Awake techniques | Awake fiberoptic intubation — for anticipated difficult airway when spontaneous ventilation is preserved |

**The Vortex Approach (Chrimes 2016):**
Three non-surgical "lifelines" — facemask, SGA, ETT — each with a maximum of 3 optimized attempts. When all three lifelines are exhausted: the patient is in the "green zone" (CICO) and the single remaining option is surgical airway.

## Workup

**Equipment Check (before any intubation attempt):**

| Equipment | Specification |
|-----------|---------------|
| Suction | Yankauer and DuCanto (large-bore) suction, tested and functional |
| Oxygen | BVM connected to 15 L/min, nasal cannula at 15 L/min (apneic oxygenation) |
| Video laryngoscope | Charged, anti-fog, correct blade size (Mac 3-4 for adults) |
| Direct laryngoscope | Backup; Mac 3, Mac 4, Miller 2 blades available |
| Endotracheal tubes | Primary size (7.0 for females, 8.0 for males) plus one size smaller |
| Bougie | 60 cm coude-tip gum elastic bougie — loaded alongside first-attempt device |
| Supraglottic airway | Second-generation SGA (i-gel or LMA Supreme) — sized and at bedside |
| Surgical airway kit | 10-blade scalpel, bougie, 6.0 cuffed ETT or Shiley tracheostomy tube — at bedside, opened |
| Medications | RSI drugs drawn and labeled; paralytic choice based on patient factors |
| Monitoring | Continuous waveform capnography, pulse oximetry |

**Pre-Procedure Assessment:**
- LEMON assessment (described above)
- MOANS assessment for BMV difficulty
- RODS assessment for SGA difficulty
- Prior anesthesia records if available (check for "difficult airway" documentation)
- Neck anatomy: palpate cricothyroid membrane — mark with pen or finger if difficult anatomy anticipated

**Positioning:**
- Ramped position for obese patients: blankets or commercial ramp under shoulders and head to achieve ear-to-sternal notch alignment
- Sniffing position for non-obese: neck flexion with atlanto-occipital extension
- 25-degree head-up tilt improves pre-oxygenation reserve and laryngoscopic view

## Treatment

### Algorithm: Emergency Department Difficult Airway

**Step 1: Pre-Oxygenation (before paralysis)**
- Nasal cannula 15 L/min (maintained throughout all attempts — apneic oxygenation)
- BVM with 100% FiO2, tight mask seal, oral or nasal airway adjuncts
- Target SpO2 >95% for >=3 minutes before administering paralytic
- NODESAT: Nasal O2 During Efforts Securing A Tube

**Step 2: RSI (if not contraindicated)**
- Induction: ketamine 1.5 mg/kg IV (hemodynamically stable; preferred in hypotension, asthma, trauma) OR propofol 1.5 mg/kg IV (avoid in hypotension) OR etomidate 0.3 mg/kg IV
- Paralytic: rocuronium 1.2 mg/kg IV (full dose for RSI; sugammadex 16 mg/kg IV available for reversal) OR succinylcholine 1.5 mg/kg IV (avoid in hyperkalemia, burns >48h, crush injury, neuromuscular disease)
- Wait 45-60 seconds after paralytic before first attempt

**Step 3: First Attempt — Optimized**
- Video laryngoscopy with bougie loaded
- External laryngeal manipulation (bimanual or BURP)
- Confirm placement with continuous waveform capnography (ETCO2)
- Success: secure tube, confirm bilateral breath sounds, CXR

**Step 4: First Attempt Failed — Modify Technique**
- Return to BVM ventilation with oral airway and two-person technique
- Re-oxygenate to SpO2 >95% before second attempt
- Change one variable: different blade geometry, different operator, reposition patient, use bougie if not used
- Attempt 2 with the change

**Step 5: Second Attempt Failed**
- Return to BVM ventilation and re-oxygenate
- Third and FINAL oral attempt: change technique again
- If the operator cannot ventilate between attempts: go directly to SGA

**Step 6: Three Failed Intubation Attempts — Insert SGA**
- i-gel: size 4 for 50-90 kg adults, size 5 for >90 kg
- LMA Supreme: same sizing
- Confirm ventilation through SGA with ETCO2
- If SGA ventilation successful: decision tree
  - Oxygenating and ventilating: reassess — wake patient (if possible), call anesthesia, plan fiberoptic intubation through SGA, or proceed with SGA in situ for the case
  - Cannot oxygenate through SGA: CICO — proceed to surgical airway

**Step 7: CICO — Surgical Cricothyrotomy**
- Declare CICO verbally to the team
- Scalpel-bougie-tube technique (see surgical-cricothyrotomy condition file)
- 6.0 cuffed ETT or 6.0 Shiley tracheostomy tube through cricothyroid membrane
- Confirm ventilation with ETCO2
- Once oxygenating: secure the tube and plan definitive airway

### Pharmacologic Adjuncts
- Sugammadex 16 mg/kg IV: reversal of rocuronium for "can't intubate, CAN ventilate" situations where spontaneous ventilation is preferred
- Glycopyrrolate 0.2 mg IV: antisialagogue before awake fiberoptic intubation
- Topical lidocaine 4%: nebulized or atomized for awake airway techniques
- Dexmedetomidine 1 mcg/kg IV over 10 min: sedation for awake fiberoptic without respiratory depression (requires hemodynamic stability)

## Disposition

- **Successful intubation after difficult airway:** document the airway grade, number of attempts, devices used, and successful technique in the medical record; place a "Difficult Airway" alert in the chart
- **Surgical airway placed:** ICU admission; ENT or surgical consultation for conversion to formal tracheostomy within 24-72 hours
- **SGA in situ as bridge:** convert to definitive airway (ETT via fiberoptic through SGA or in OR with anesthesia) before leaving the ED
- **Awake intubation planned:** anesthesia consultation; may require OR with fiberoptic-guided intubation under sedation
- **Post-intubation care:** verify tube position with CXR; continuous waveform ETCO2; sedation and analgesia (propofol 5-50 mcg/kg/min + fentanyl 25-100 mcg/hr or ketamine 0.1-0.5 mg/kg/hr)

## Pitfalls

1. **Repeating the same failed technique without changing a variable.** If direct laryngoscopy with a Mac 3 fails, a second attempt with the same Mac 3 in the same position by the same operator will fail again. Each attempt must change something: blade geometry, bougie use, operator, patient positioning, or device type.

2. **Fixating on oral intubation beyond 3 attempts.** Each attempt causes edema, bleeding, and secretions that degrade subsequent attempts. After 3 failed oral attempts, the glottic view is worse than it was on attempt 1. Transition to SGA or surgical airway. Three is the maximum.

3. **Failing to maintain apneic oxygenation with nasal cannula.** High-flow nasal oxygen at 15 L/min during laryngoscopy extends the safe apnea time by 2-4 minutes. This is the simplest and most effective intervention for preventing desaturation during intubation attempts. It costs nothing and should run continuously.

4. **Not pre-oxygenating adequately before paralysis.** Three minutes of pre-oxygenation with 100% FiO2 provides 6-8 minutes of safe apnea time in a healthy adult. Obese patients, pregnant patients, and children desaturate in 2-3 minutes without pre-oxygenation. Rushing to paralysis without denitrogenation eliminates the safety margin.

5. **Delaying surgical airway in CICO.** NAP4 (2011) demonstrated that delayed front-of-neck access is the primary contributor to airway-related death. When CICO is recognized, the surgical airway must begin within 30 seconds. Every additional oral or SGA attempt in CICO wastes time and oxygen.

6. **Using needle cricothyrotomy as a definitive airway in adults.** Needle cricothyrotomy with jet ventilation is a temporizing measure in adults. It provides oxygenation but inadequate ventilation and does not protect against aspiration. Surgical cricothyrotomy is the definitive CICO intervention in adults.

7. **Placing an endotracheal tube and not confirming with waveform capnography.** Auscultation is unreliable (especially in noisy resuscitation environments, obese patients, and lung disease). Waveform ETCO2 is the gold standard for confirming tracheal placement. An esophageal intubation with delayed recognition is the most lethal airway complication.

8. **Not calling for help early.** The difficult airway is a team event. Call anesthesia, call a second emergency physician, call ENT — before the first attempt if the airway is anticipated to be difficult, or immediately after a failed first attempt. Do not attempt 3 solo attempts before calling for backup.

### Hesitation Bias
- The most dangerous moment in the difficult airway algorithm is the transition from non-surgical to surgical airway. Cognitive biases (anchoring on oral techniques, aversion to surgical procedures, optimism that "one more attempt" will succeed) cause fatal delays.
- Institutional drills, premarked cricothyroid membranes, and verbal declaration of CICO with a scripted checklist reduce hesitation bias.
- Assign a dedicated team member to monitor time and declare CICO if 3 oral attempts + SGA have failed.
