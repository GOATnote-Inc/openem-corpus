---
id: electrical-injury
condition: Electrical Injury and Lightning Strike
aliases: [electrocution, electric shock, electrical burn, lightning injury, lightning strike, high-voltage injury, low-voltage electrical injury]
icd10: [T75.4XXA, T75.00XA, W86.0XXA, W86.1XXA, W85.XXXA]
esi: 2
time_to_harm: "< 10 minutes (cardiac arrest from VF/asystole; delayed compartment syndrome 6-12 hours)"
mortality_if_delayed: "3-15% overall; 30% for high-voltage; lightning cardiac arrest 10-30% if resuscitated promptly (reverse triage improves survival)"
category: environmental
track: tier1
sources:
  - type: review
    ref: "Gentges J, Schieche C. Electrical injuries in the emergency department: an evidence-based review. Emerg Med Pract 2018;20(11):1-20"
    pmid: "30358379"
  - type: review
    ref: "Ritenour AE et al. Lightning injury: a review. Burns 2008;34(5):585-594"
    pmid: "18395987"
  - type: pubmed
    ref: "Koumbourlis AC. Electrical injuries. Crit Care Med 2002;30(11 Suppl):S424-S430"
    pmid: "12528784"
  - type: pubmed
    ref: "Bailey B et al. Cardiac monitoring of high-risk patients after an electrical injury: a prospective multicentre study. Emerg Med J 2007;24(5):348-352"
    pmid: "17452703"
  - type: guideline
    ref: "2020 AHA Guidelines for CPR and ECC — Part 3: Adult Basic and Advanced Life Support (Lightning/Electrical Injury Considerations)"
last_updated: "2026-02-19"
compiled_by: agent
risk_tier: B
validation:
  automated_consistency_check: "2026-02-27"
  dose_range_validator: "2026-02-27"
  unit_normalization_check: "2026-02-27"
  cross_file_consistency_check: "2026-02-27"
  citation_presence_check: "2026-02-27"
  duplicate_content_check: "2026-02-27"
  outlier_detection_flag: clear
  schema_version: "2.0"
  provenance_links: []
---
# Electrical Injury and Lightning Strike

## Recognition

**Classification by Voltage:**
- **Low voltage (<1000V):** Household current (110-240V AC). Most common electrical injury. Alternating current (AC) causes tetanic muscle contraction that locks the victim's hand to the source, prolonging exposure. Cardiac arrest mechanism is ventricular fibrillation.
- **High voltage (>1000V):** Industrial/power line exposure. Massive tissue destruction along current path. Flash burns, arc burns, and flame burns from ignited clothing. Blast injuries from explosive arc. Cardiac arrest mechanism is asystole or VF. Limb amputation rate 30-40%.
- **Lightning (up to 300 million volts, 30,000 amps):** Extremely brief exposure (1-5 milliseconds). Direct current (DC). Cardiac arrest mechanism is asystole — the massive DC countershock depolarizes the entire myocardium simultaneously. Flashover effect: current travels over body surface rather than through it, accounting for relatively low internal burn severity compared to high-voltage industrial injury.

**Mechanisms of Lightning Injury:**
- Direct strike (most lethal, 3-5% of cases)
- Side splash (current jumps from nearby struck object — most common mechanism)
- Ground current (steps across voltage gradient on ground)
- Contact voltage (touching struck object)
- Upward streamer (partially completed leader from victim)
- Blunt trauma from shock wave (thunder produces overpressure up to 300 atm)

**Key Clinical Features:**
- **Cardiac:** VF (AC, low voltage), asystole (DC, lightning). Cardiac contusion, ST-segment changes, QT prolongation, transient hypertension. Cardiac arrest from lightning may be reversible because respiratory arrest outlasts cardiac automaticity recovery — if ventilation is provided, cardiac rhythm may return spontaneously.
- **Burns:** Entry and exit wounds. Surface burns may be deceptively small despite extensive deep tissue destruction along the current path (iceberg effect). Arc burns in flexion creases (antecubital, axillary, inguinal). Lightning: Lichtenberg figures (fern-like, pathognomonic, not true burns — resolve in 24-48 hours), linear burns in areas of moisture (sweat lines), punctate burns.
- **Musculoskeletal:** Tetanic contraction (AC) causes fractures (vertebral compression fractures, posterior shoulder dislocations bilateral), muscle necrosis along current path, compartment syndrome (delayed 6-24 hours), rhabdomyolysis.
- **Neurological:** Loss of consciousness, seizures, confusion, spinal cord injury (transverse myelitis, anterior spinal artery syndrome — may be delayed days to weeks), peripheral neuropathy. Lightning-specific: keraunoparalysis (transient paralysis and mottled cyanosis of extremities, resolves in hours — do not mistake for spinal cord injury or vascular injury).
- **ENT:** Tympanic membrane rupture (50% of lightning victims, up to 80% from direct strike), hearing loss, vertigo.
- **Ophthalmologic:** Cataracts (may develop days to months after injury), corneal burns, hyphema, vitreous hemorrhage, retinal detachment, optic nerve damage.
- **Vascular:** Thrombosis of vessels along current path, delayed hemorrhage from vessel wall necrosis.

## Critical Actions

1. **Scene safety first** — ensure power source is disconnected. Do not approach downed power lines (ground current lethal within 10 meters). Lightning: move casualties indoors or to a vehicle; lightning CAN strike the same area repeatedly.
2. **Reverse triage for lightning mass casualty** — treat apparently dead victims FIRST. Unlike other mass casualty events, lightning cardiac arrest victims who appear dead may have the best prognosis if given immediate CPR, because cardiac automaticity may recover before respiratory drive does. Those who are breathing and conscious will likely survive without immediate intervention.
3. **Immediate CPR and ACLS for cardiac arrest** — standard ACLS. Prolonged resuscitation is justified because the young age of typical victims and the mechanism (primary electrical cardiac arrest, not end-organ failure) favor neurologically intact survival. Epinephrine 1 mg IV/IO q3-5 min per standard protocol.
4. **12-lead ECG immediately** — assess for arrhythmia, ST changes, QT prolongation. Repeat if any abnormality.
5. **Assess the entire current pathway** — identify entry and exit wounds. Examine for occult deep tissue injury between entry and exit sites. Burns may appear minor externally.
6. **Assess compartments** — firm, tense compartments require emergent fasciotomy. Serial compartment checks every 2-4 hours for first 24 hours in high-voltage injury.
7. **Aggressive IV crystalloid resuscitation** — NS or LR. Fluid requirements exceed what burn size alone would predict (Parkland formula underestimates because deep tissue injury is occult). Target urine output 1-1.5 mL/kg/hr (75-100 mL/hr in adults). If myoglobinuria present, target 200 mL/hr to prevent renal tubular obstruction.
8. **Spinal immobilization** — electrical injury causes violent tetanic contraction and falls from height; assume c-spine injury until cleared.
9. **Tetanus prophylaxis** — update per burn protocol.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Thermal burn without electrical component | No entry/exit wounds, no current pathway injury, no cardiac effects, no rhabdomyolysis |
| Cardiac arrest from other cause at work site | No electrical source, no burns, no witnesses to electrical contact, toxicology/cardiac history |
| Stroke/seizure causing fall into electrical source | Pre-existing neurological symptoms, witnesses report collapse before contact |
| Lightning vs high-voltage industrial | Lightning: Lichtenberg figures, shorter exposure, flashover pattern, tympanic membrane rupture, keraunoparalysis. Industrial: prolonged contact, massive entry/exit wounds, deep tissue destruction |
| Compartment syndrome from crush injury | No electrical exposure history, no cardiac arrhythmia, mechanism is compression not current |
| Rhabdomyolysis from other cause | Exertional, drug-induced (statins, NMS), crush injury — no burns, no electrical exposure |
| Blast injury without electrical component | Explosion history without current path, no entry/exit burns, no arrhythmia |

## Workup

**ECG:**
- 12-lead on arrival for ALL electrical injury patients
- Sinus tachycardia (most common finding)
- ST-segment elevation or depression (myocardial injury)
- QT prolongation (arrhythmia risk)
- Nonspecific T-wave changes
- Atrial fibrillation, atrial flutter
- Ventricular tachycardia, ventricular fibrillation
- Heart block (first, second, or third degree)
- Bundle branch block pattern

**Labs:**
- CK (rhabdomyolysis screening — may be markedly elevated >10,000 with occult muscle destruction; repeat at 6, 12, 24 hours)
- Troponin (myocardial injury — serial)
- Urinalysis (myoglobinuria: dipstick positive for blood without RBCs on microscopy; tea/cola-colored urine)
- BMP (hyperkalemia from cell lysis and rhabdomyolysis, acute kidney injury from myoglobin nephropathy, metabolic acidosis)
- CBC (hemoconcentration, leukocytosis)
- Lactate (tissue hypoperfusion, compartment syndrome)
- Coagulation studies (DIC in severe injuries)
- ABG/VBG (metabolic acidosis)
- Hepatic panel (if abdominal current path suspected)
- Lipase (if abdominal current path)
- Type and screen (high-voltage injuries may require surgery)

**Imaging:**
- CT head (if altered mental status, fall, or lightning strike)
- CT cervical spine (tetanic contraction or fall mechanism)
- CXR (aspiration, pulmonary contusion from blast, pneumothorax)
- CT angiography of affected extremity if vascular compromise suspected
- Additional imaging guided by current pathway (CT abdomen if transabdominal path)

**Special Studies:**
- Compartment pressures (clinical exam or needle manometry if equivocal — threshold >30 mmHg or within 30 mmHg of diastolic pressure)
- Formal audiometry and otoscopic exam (lightning: tympanic membrane rupture assessment)
- Ophthalmologic exam (slit lamp if eye symptoms, lightning, or facial burns)

## Treatment

**Cardiac Arrest:**
- Standard ACLS protocol. VF/pVT: defibrillation 200J biphasic, epinephrine 1 mg IV/IO q3-5 min, amiodarone 300 mg IV first dose then 150 mg IV second dose
- Asystole/PEA: epinephrine 1 mg IV/IO q3-5 min, identify and treat reversible causes
- Prolonged resuscitation justified — electrical cardiac arrest in otherwise healthy patients has favorable neurologic outcomes with aggressive CPR
- Lightning arrest: begin ventilation immediately (respiratory arrest outlasts cardiac arrest; spontaneous cardiac rhythm may return if ventilation is supported)

**Arrhythmia Management:**
- Continuous cardiac monitoring for all symptomatic patients
- Sinus tachycardia: IV fluids, pain control — usually resolves
- Atrial fibrillation/flutter: rate control with diltiazem 0.25 mg/kg IV (max 20 mg) over 2 min or metoprolol 5 mg IV q5 min x3 — usually self-limited
- Ventricular tachycardia: amiodarone 150 mg IV over 10 min, then 1 mg/min infusion x6 hr
- Bradycardia/heart block: atropine 1 mg IV q3-5 min (max 3 mg); transcutaneous pacing if refractory

**Fluid Resuscitation:**
- NS or LR IV. High-voltage injury: initial bolus 20 mL/kg, then titrate to urine output
- Standard urine output target: 0.5-1 mL/kg/hr
- If rhabdomyolysis (CK >5000 or myoglobinuria): target UOP 200-300 mL/hr with NS, consider sodium bicarbonate 150 mEq in 1L D5W at 200 mL/hr to alkalinize urine (target urine pH >6.5)
- Parkland formula underestimates fluid needs — deep tissue injury is occult. Titrate to hemodynamics and urine output, not burn surface area alone

**Burn Care:**
- Sterile dressings to burn wounds
- Do NOT debride in ED — burns require assessment by burn surgery for deep tissue involvement
- Escharotomy for circumferential burns with vascular compromise

**Compartment Syndrome:**
- Emergent fasciotomy for clinical compartment syndrome or measured pressures >30 mmHg (or within 30 mmHg of diastolic)
- Consult orthopedic surgery or trauma surgery urgently
- Serial compartment checks q2-4h for first 24 hours in all high-voltage injuries

**Rhabdomyolysis Management:**
- Aggressive IV hydration targeting UOP 200-300 mL/hr
- Monitor CK q6-12h (peaks at 24-72 hours)
- Monitor potassium — treat hyperkalemia aggressively: calcium gluconate 10% 30 mL (3g) IV over 10 min (membrane stabilization), insulin 10 units regular IV + dextrose 50% 50 mL (25g) IV, kayexalate 15-30g PO
- Sodium bicarbonate infusion for urine alkalinization if myoglobinuria
- Nephrology consultation for oliguria despite adequate resuscitation or refractory hyperkalemia

**Pain Management:**
- Fentanyl 1-2 mcg/kg IV q30-60 min or morphine 0.1 mg/kg IV q2-4h
- Ketamine 0.1-0.3 mg/kg IV for adjunctive analgesia in severe burns
- Avoid NSAIDs (renal risk with rhabdomyolysis)

**Adjunctive:**
- Tetanus prophylaxis (Td or Tdap if indicated by immunization history)
- Seizure management: midazolam 5-10 mg IV/IM or diazepam 10 mg IV
- Lightning TM rupture: keep ear dry, ENT follow-up (most heal spontaneously)

## Disposition

**Cardiac Monitoring Duration:**
- **High-voltage (>1000V), lightning, or any arrhythmia/LOC/abnormal ECG:** admit for continuous cardiac monitoring minimum 24 hours
- **Low-voltage with normal ECG, no LOC, no arrhythmia, no symptoms:** observation 4-6 hours with repeat ECG. If repeat ECG normal and asymptomatic, discharge is reasonable
- **Low-voltage with ANY of the following:** abnormal ECG, loss of consciousness, transthoracic current path, tetany, chest pain — admit for 12-24 hour cardiac monitoring

**ICU Admission:**
- Cardiac arrest survivors
- High-voltage injury with significant burns or rhabdomyolysis
- Active arrhythmia requiring treatment
- Compartment syndrome requiring fasciotomy
- CK >10,000 or myoglobinuria requiring aggressive hydration
- Hemodynamic instability
- Altered mental status

**Burn Center Transfer:**
- High-voltage electrical burns (all)
- Burns involving hands, feet, face, genitalia, perineum, or major joints
- Burns with suspected deep tissue injury
- Any electrical burn requiring fasciotomy or surgical exploration
- Per ABA referral criteria: all electrical burns including lightning

**Surgical Consultation:**
- Orthopedics/trauma surgery: compartment syndrome, fractures from tetanic contraction or falls
- Vascular surgery: thrombosis or vascular compromise in extremity
- Burn surgery: all high-voltage burns, wounds requiring debridement or exploration

**Discharge Criteria (low-voltage only):**
- Normal ECG at presentation and repeat at 4-6 hours
- No loss of consciousness
- No arrhythmia on monitoring
- No significant burns
- Normal CK and urinalysis
- Asymptomatic
- Reliable follow-up for delayed cataracts, neurological symptoms

**Discharge Instructions:**
- Return immediately for palpitations, chest pain, shortness of breath, dark urine, extremity swelling or numbness, vision changes, hearing changes
- Ophthalmology follow-up within 1-2 weeks (delayed cataracts)
- Primary care follow-up within 48-72 hours

## Pitfalls

1. **Underestimating injury severity based on skin burns alone.** External burns in electrical injury are the tip of the iceberg. Current travels through deep tissues (muscle, nerve, vessel) along the path of least resistance. Small entry and exit wounds can overlie massive muscle necrosis, vascular thrombosis, and impending compartment syndrome. Every high-voltage injury requires investigation for deep tissue damage regardless of surface appearance.

2. **Using standard triage in lightning mass casualty events.** In conventional MCI triage, apparently dead victims are triaged last. Lightning is the exception: reverse triage dictates treating pulseless/apneic victims FIRST because lightning-induced cardiac arrest is often reversible with immediate CPR and ventilation. Victims who are conscious and breathing will likely survive without immediate intervention. Applying standard triage kills salvageable patients.

3. **Failing to monitor for delayed arrhythmia.** Patients with high-voltage injury, any arrhythmia, loss of consciousness, abnormal ECG, or transthoracic current path require 12-24 hours of continuous cardiac monitoring. Delayed lethal arrhythmias (VT, VF) have been reported hours after the initial injury. A single normal ECG does not exclude risk in high-risk patients.

4. **Missing rhabdomyolysis in the absence of visible burns.** Electrical current causes direct muscle necrosis along the current pathway. CK can be >50,000 with minimal external findings. Failure to check CK, urinalysis (myoglobinuria), and BMP (hyperkalemia, acute kidney injury) misses a treatable and potentially lethal complication. All electrical injury patients need CK and UA.

5. **Underresuscitating based on burn surface area.** The Parkland formula (4 mL/kg/% TBSA) grossly underestimates fluid requirements in electrical injury because it does not account for occult deep tissue destruction. Fluid resuscitation must be titrated to urine output (1-1.5 mL/kg/hr, or 200 mL/hr if myoglobinuria), not calculated from visible burn area.

6. **Not performing serial compartment checks.** Compartment syndrome from electrical injury is delayed (6-24 hours) as edema from muscle necrosis and aggressive resuscitation progresses. A normal compartment exam on arrival does not exclude compartment syndrome. Serial exams every 2-4 hours for the first 24 hours are mandatory for all high-voltage injuries.

7. **Mistaking keraunoparalysis for spinal cord injury or vascular occlusion.** Keraunoparalysis (lightning-specific transient paralysis with mottled, pulseless extremities) resolves spontaneously within hours. Initiating unnecessary vascular surgery or spinal cord injury workup delays appropriate management. Awareness of this lightning-specific phenomenon prevents harmful interventions, though concurrent spinal injury should still be excluded clinically.

8. **Forgetting tympanic membrane exam in lightning victims.** TM rupture occurs in approximately 50% of lightning strike victims (80% in direct strikes). Missed TM rupture causes unnecessary hearing loss if the ear is not kept dry and protected. Otoscopic exam is mandatory for all lightning injuries. ENT referral for confirmed rupture.

9. **Discharging without ophthalmology follow-up.** Cataracts from electrical injury (particularly lightning) may develop days to months after exposure. Patients discharged without explicit ophthalmology follow-up instructions miss the window for early detection. All electrical injury and lightning patients require ophthalmology referral within 1-2 weeks regardless of initial eye exam.

10. **Forgetting to evaluate for associated traumatic injuries.** Electrical injury causes violent tetanic muscle contraction (AC current) and blast/throw injuries (lightning, high-voltage arc). Posterior shoulder dislocations (bilateral), vertebral compression fractures, long bone fractures, and traumatic brain injury occur without any direct impact. Focused exam and imaging of the spine, shoulders, and any area of tenderness is required.
