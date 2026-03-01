---
id: neonatal-resuscitation
condition: Neonatal Resuscitation
aliases: [NRP, newborn resuscitation, neonatal resuscitation program, delivery room resuscitation]
icd10: [P96.83, P84, P28.5, P21.0, P21.1]
esi: 1
time_to_harm:
  irreversible_injury: "< 5 minutes (hypoxic-ischemic encephalopathy)"
  death: "< 10 minutes without effective ventilation in apneic neonate"
  optimal_intervention_window: "< 60 seconds (the Golden Minute) — initial steps and PPV if needed"
mortality_if_delayed: "10% of newborns require some intervention; 1% require extensive resuscitation; delay in effective ventilation is the primary driver of neonatal mortality"
category: procedural
track: tier1
sources:
  - type: guideline
    ref: "Wyckoff MH, Wyllie J, Aziz K, et al. Part 5: Neonatal Resuscitation: 2020 AHA Guidelines for CPR and ECC. Circulation. 2020;142(16_suppl_2):S524-S550."
    pmid: "33081528"
  - type: guideline
    ref: "Wyckoff MH, Greif R, Morley PT, et al. 2022 International Consensus on Cardiopulmonary Resuscitation and Emergency Cardiovascular Care Science With Treatment Recommendations: Neonatal Life Support. Circulation. 2022;146(25):e283-e321."
  - type: guideline
    ref: "AHA/AAP Neonatal Resuscitation Program (NRP), 8th Edition. 2021."
  - type: guideline
    ref: "Part 5: Neonatal Resuscitation: 2025 AHA and AAP Guidelines for CPR and ECC. Circulation. 2025."
  - type: pubmed
    ref: "Perlman JM, Wyllie J, Kattwinkel J, et al. Neonatal resuscitation: 2015 International Consensus on CPR and ECC Science with Treatment Recommendations. Circulation. 2015;132(16 Suppl 1):S204-S241."
    pmid: "26472855"
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
# Neonatal Resuscitation

## Recognition

**Indications (All Newborns Require Initial Assessment):**

**Three rapid assessment questions (within 30 seconds of birth):**
1. Term gestation?
2. Good muscle tone?
3. Breathing or crying?

If YES to all three: routine care (dry, warm, skin-to-skin, delayed cord clamping)
If NO to any: proceed to initial steps of neonatal resuscitation

**Risk Factors for Needing Resuscitation:**
- Preterm (< 37 weeks, especially < 32 weeks)
- Meconium-stained amniotic fluid
- Fetal bradycardia (FHR < 110 bpm)
- Maternal general anesthesia, opioid administration
- Prolapsed or compressed cord
- Placental abruption
- Prolonged second stage of labor
- Multiple gestation
- Congenital anomalies (diaphragmatic hernia, airway malformation)

**NRP Algorithm Flow:**
- Initial steps (warm, dry, stimulate, clear airway) → 30-second assessment
- If HR < 100 or apneic: positive pressure ventilation (PPV)
- If HR < 60 after 30 seconds of effective PPV: chest compressions + PPV (3:1 ratio)
- If HR < 60 after 60 seconds of compressions + PPV: epinephrine via UVC or ET

## Critical Actions

| Action | Target |
|--------|--------|
| Initial steps (warm, dry, stimulate) | First 30 seconds of life |
| PPV initiated (if needed) | Within 60 seconds of birth (Golden Minute) |
| HR assessment | At 60 seconds; repeat q30 seconds |
| Chest compressions (if HR < 60) | After 30 seconds of effective PPV |
| Epinephrine (if HR < 60) | After 60 seconds of compressions + PPV |

1. **Warm** — radiant warmer on; dry with warm towels; remove wet linens; cover head
2. **Clear airway if needed** — suction mouth then nose (only if obstruction present; routine suctioning NOT recommended)
3. **Stimulate** — flick soles of feet, rub back gently
4. **Assess HR and breathing** at 30 seconds — use cardiac monitor for most accurate HR; pulse oximetry on right hand (preductal)
5. **PPV if apneic or HR < 100** — 21% O2 for term, 21-30% for preterm (> 32 weeks), 30% for < 32 weeks
6. **Chest compressions if HR < 60 after 30 sec effective PPV** — 3:1 ratio (3 compressions : 1 ventilation, 120 events/min)
7. **Epinephrine if HR < 60 after 60 sec of compressions + PPV**
8. **Reassess every 30 seconds**

## Differential Diagnosis

**Causes of Neonatal Depression at Birth:**

| Category | Examples |
|----------|---------|
| Respiratory | Meconium aspiration, pneumothorax, diaphragmatic hernia, choanal atresia, Robin sequence |
| Cardiovascular | Congenital heart disease, persistent pulmonary hypertension, hypovolemia |
| Neurologic | Birth asphyxia, maternal opioids/magnesium, congenital neuromuscular disease |
| Hematologic | Fetal-maternal hemorrhage, placental abruption, cord avulsion |
| Infectious | Chorioamnionitis, congenital sepsis |
| Metabolic | Hypoglycemia, inborn errors |

## Workup

**Pre-Delivery Preparation:**

| Equipment | Specification |
|-----------|---------------|
| Radiant warmer | Preheated; towels/blankets warmed |
| Bulb syringe | For suctioning |
| Suction catheter | 8-10 Fr with wall suction at 80-100 mmHg |
| PPV device | Self-inflating bag (240 mL neonatal) with 21-30% O2 blender; or T-piece resuscitator (preferred — more consistent pressure delivery) |
| Face masks | Sizes 0 (preterm) and 1 (term) |
| Pulse oximeter | Preductal (right hand/wrist) |
| Cardiac monitor | 3-lead ECG (most accurate HR assessment in DR) |
| Laryngoscope | Miller blade 0 (preterm) and 1 (term) |
| ETT | 2.5 (< 1000 g), 3.0 (1-2 kg), 3.5 (2-3 kg), 3.5-4.0 (> 3 kg); uncuffed |
| UVC supplies | 3.5-5 Fr umbilical catheter, 3-way stopcock, NS flush |
| Medications | Epinephrine 1:10,000 (0.1 mg/mL); NS for volume expansion |
| Timer | Visible clock or timer started at birth |

**Target SpO2 by Minute After Birth (Preductal — Right Hand):**

| Time | Target SpO2 |
|------|------------|
| 1 min | 60-65% |
| 2 min | 65-70% |
| 3 min | 70-75% |
| 4 min | 75-80% |
| 5 min | 80-85% |
| 10 min | 85-95% |

## Treatment

### Initial Steps (First 30 Seconds)

**Thermoregulation:**
- Place under radiant warmer
- Dry vigorously with warm towel (also provides stimulation)
- Remove wet linen, replace with dry
- Cover head with hat (40% of heat loss is through the head)
- For very preterm (< 32 weeks): place in polyethylene bag immediately (below the neck) without drying; radiant warmer over bag
- Target temperature: 36.5-37.5 degrees C (hypothermia and hyperthermia both worsen outcomes)

**Airway:**
- Position: neutral "sniffing" position (slight extension); shoulder roll if needed
- Suction ONLY if airway obstruction is evident (meconium, blood, excessive secretions)
- Routine suctioning is NOT recommended — it delays ventilation and can cause bradycardia
- If meconium present and baby is vigorous (crying, breathing): observe, do not suction
- If meconium present and baby is NOT vigorous: clear airway with suction, then PPV

**Stimulation:**
- Gentle rubbing of back
- Flicking soles of feet
- If no response after 10-15 seconds of stimulation: proceed to PPV

### Positive Pressure Ventilation (PPV)

**When:** apneic, gasping, or HR < 100 at 30-second assessment

**Technique:**
- Apply face mask (correct size — covers nose and mouth, not eyes)
- Use T-piece resuscitator (preferred) or self-inflating bag
- Initial PIP: 20-25 cmH2O (term); 20 cmH2O (preterm)
- PEEP: 5 cmH2O (T-piece delivers PEEP; self-inflating bag does NOT unless PEEP valve attached)
- Rate: 40-60 breaths/min
- FiO2: start at 21% for term (> 35 weeks); 21-30% for preterm (30-35 weeks); 30% for < 30 weeks; titrate to SpO2 targets
- Ventilation rate: "Breathe... two... three... breathe... two... three..." (40-60/min)

**Assessing Effective PPV (MR SOPA):**
- **M**ask adjustment — reposition for seal
- **R**eposition head — neutral/sniffing position
- **S**uction — clear mouth and nose
- **O**pen mouth — slight jaw thrust
- **P**ressure increase — increase PIP by 5 cmH2O increments (max 30-40 cmH2O)
- **A**lternative airway — ETT or laryngeal mask

**HR should increase within 15-30 seconds of effective PPV.** If HR remains < 100 after 30 seconds of effective PPV, continue PPV. If HR < 60 after 30 seconds of effective PPV, initiate chest compressions.

### Chest Compressions

**When:** HR < 60 bpm despite 30 seconds of effective PPV

**Technique:**
- Two-thumb encircling technique (preferred): thumbs on lower 1/3 of sternum, hands encircle the chest
- Compress 1/3 of anteroposterior chest diameter
- 3:1 ratio: 3 compressions then 1 ventilation (90 compressions + 30 ventilations = 120 events/min)
- "One-and-two-and-three-and-breathe-and..."
- Increase FiO2 to 100% when compressions are initiated
- Continue for 60 seconds, then reassess HR

### Epinephrine and Vascular Access

**When:** HR < 60 bpm despite 60 seconds of effective compressions + PPV

**Umbilical Venous Catheter (UVC) — Preferred Route:**
1. Cut umbilical cord 1-2 cm from the skin
2. Identify the umbilical vein (single, large, thin-walled vessel; versus two smaller, thick-walled arteries)
3. Insert 3.5-5 Fr umbilical catheter into the vein, advance 2-4 cm until free blood return (just past the abdominal wall; do not advance too far — risk of liver injury or portal vein placement)
4. Confirm blood return, flush with NS

**Epinephrine Dosing:**
- IV (UVC): 0.01-0.03 mg/kg of 1:10,000 concentration (0.1-0.3 mL/kg)
- ET (if no IV access): 0.05-0.1 mg/kg of 1:10,000 (0.5-1 mL/kg) — higher dose needed due to poor absorption; IV preferred
- Follow with 1 mL NS flush
- May repeat q3-5 min if HR remains < 60

**Volume Expansion:**
- If suspected hypovolemia (pallor, poor perfusion despite effective resuscitation; placental abruption, cord hemorrhage)
- NS 10 mL/kg IV over 5-10 minutes
- O-negative pRBC 10 mL/kg if blood loss confirmed

### Post-Resuscitation
- Continue monitoring: HR, SpO2, temperature, glucose
- Blood glucose within 1 hour (target > 45 mg/dL; treat hypoglycemia with D10W 2 mL/kg IV)
- Blood gas (cord or venous)
- If prolonged resuscitation: consider therapeutic hypothermia (33.5 degrees C x 72 hours for moderate-severe HIE; initiate within 6 hours of birth)
- NICU admission for any neonate requiring PPV > 2 minutes or chest compressions

## Disposition

- **Vigorous neonate, no resuscitation needed:** routine newborn care; skin-to-skin; nursery admission
- **Required brief PPV (< 2 minutes) with prompt response:** close monitoring; may remain with mother if otherwise well; pediatric assessment
- **Required prolonged PPV, compressions, or epinephrine:** NICU admission; continuous monitoring; consider cooling for HIE
- **No response after 20 minutes of appropriate resuscitation (no HR detected):** discussion of cessation of resuscitation (NRP 8th edition guideline); involve family in shared decision-making
- **Transfer:** if no NICU available, stabilize with ongoing PPV/monitoring and arrange transport to facility with NICU (neonatal transport team if available)

## Pitfalls

1. **Delaying positive pressure ventilation beyond the Golden Minute.** Ventilation is the single most important intervention in neonatal resuscitation. Most neonates who need help only need effective ventilation. Delay in initiating PPV while attempting to suction, stimulate, or assess further allows hypoxia to worsen. If the baby is not breathing by 60 seconds, begin PPV.

2. **Routine deep suctioning of vigorous meconium-stained neonates.** Current NRP guidelines (2020, 2025) do NOT recommend routine intubation and tracheal suctioning of vigorous meconium-stained neonates. This delays ventilation without improving outcomes. Suction only if the airway is obstructed.

3. **Using 100% oxygen from the start in a term neonate.** Hyperoxia causes oxidative stress and has been associated with increased mortality. Begin with 21% FiO2 (room air) for term neonates and titrate to SpO2 targets. Increase to 100% only when chest compressions are initiated.

4. **Relying on pulse oximetry alone for HR assessment in the delivery room.** Pulse oximetry can take 1-2 minutes to acquire a reliable signal and may underestimate HR. Cardiac monitor (3-lead ECG) provides the most rapid and accurate HR assessment. Attach cardiac monitor immediately for any neonate requiring resuscitation.

5. **Administering epinephrine via ETT when a UVC is achievable.** ET epinephrine has unpredictable absorption and lower efficacy than IV. The UVC can be placed in 30-60 seconds and provides reliable vascular access. Prioritize UVC placement for epinephrine delivery.

6. **Not checking temperature after resuscitation.** Both hypothermia and hyperthermia worsen neonatal outcomes. Target 36.5-37.5 degrees C. Preterm neonates are particularly vulnerable to heat loss. Check temperature within 10 minutes of birth and correct immediately.

7. **Performing chest compressions before ensuring effective ventilation.** The most common cause of persistent neonatal bradycardia is inadequate ventilation, not primary cardiac failure. Before starting compressions, ensure PPV is effective: adequate chest rise, correct mask seal, clear airway (MR SOPA). Compressions without effective ventilation are futile.
