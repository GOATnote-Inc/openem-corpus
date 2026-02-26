---
id: air-embolism
condition: Venous Air Embolism
aliases: [VAE, air embolism, gas embolism, venous gas embolism, paradoxical air embolism]
icd10: [T79.0XXA]
esi: 1
time_to_harm:
  irreversible_injury: "< 10 minutes"
  death: "< 30 minutes with large volume (>5 mL/kg)"
  optimal_intervention_window: "< 5 minutes to Durant maneuver and aspiration"
mortality_if_delayed: "Lethal dose estimated at 3-5 mL/kg (200-300 mL in adults); smaller volumes (0.5-1 mL/kg) can cause hemodynamic collapse"
category: cardiovascular
track: tier1
sources:
  - type: pubmed
    ref: "Mirski MA, Lele AV, Fitzsimmons L, Toung TJ. Diagnosis and treatment of vascular air embolism. Anesthesiology. 2007;106(1):164-177."
    pmid: "17197859"
  - type: pubmed
    ref: "Muth CM, Shank ES. Gas embolism. N Engl J Med. 2000;342(7):476-482."
    pmid: "10675429"
  - type: review
    ref: "McCarthy CJ, Behravesh S, Naber SJ, et al. Air embolism: practical tips for prevention and treatment. J Clin Med. 2016;5(11):93."
    pmid: "27809224"
  - type: pubmed
    ref: "Gordy S, Rowell S. Vascular air embolism. Int J Crit Illn Inj Sci. 2013;3(1):73-76."
    pmid: "23724390"
  - type: pubmed
    ref: "Defined AJ, Muniappan A. Paradoxical air embolism complicating central venous catheter removal. J Emerg Med. 2012;43(5):e333-e336."
    pmid: "22541878"
confusion_pairs:
  - condition: pulmonary-embolism
    differentiators:
      - "Air embolism: history of air-entraining procedure (CVC insertion/removal, surgery in sitting position, laparoscopic surgery) or diving decompression"
      - "Air embolism: pathognomonic mill-wheel murmur (churning systolic-diastolic murmur) on auscultation"
      - "Air embolism: echocardiography shows intracardiac air (echogenic bubbles in right heart); PE shows RV dilation without air"
      - "Air embolism: sudden cardiovascular collapse temporally linked to a procedure; PE onset less predictable"
  - condition: tension-pneumothorax
    differentiators:
      - "Air embolism: mill-wheel murmur present; breath sounds bilateral; no tracheal deviation"
      - "Tension pneumothorax: absent breath sounds on affected side; tracheal deviation; hyperresonance to percussion; no mill-wheel murmur"
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
# Venous Air Embolism

## Recognition

**Definition:** Entry of air (or other gas) into the venous system with hemodynamic or neurological consequences. Air travels to the right heart and pulmonary vasculature, creating an air lock that obstructs right ventricular outflow, causing cardiovascular collapse.

**Lethal physiology:** Air in the right ventricle forms a compressible gas lock at the pulmonary outflow tract. The RV churns air and blood into foam that cannot be ejected effectively, causing acute right heart failure and obstructive shock. As little as 0.5 mL/kg (50 mL) can cause symptoms; 3-5 mL/kg (200-300 mL) is potentially fatal.

**Entrainment rate:** A 14G catheter with a 5 cmH2O pressure gradient entrains air at 100 mL/sec. A single deep inspiration through an open CVC can entrain a lethal volume in seconds.

**Iatrogenic causes (most common):**
- Central venous catheter insertion or removal (highest risk during catheter removal in upright/semi-upright position)
- Neurosurgery in sitting position (incidence 10-80%)
- Laparoscopic surgery (CO2 embolism)
- Orthopedic surgery (total hip arthroplasty, spinal surgery)
- Cesarean section
- Hemodialysis circuit disconnection
- Pressurized IV fluid administration
- Lung biopsy (CT-guided or transbronchial)
- Endoscopy (rare)

**Non-iatrogenic causes:**
- Diving (arterial gas embolism from barotrauma during ascent)
- Penetrating trauma to chest or neck (injury to internal jugular or subclavian vein with negative intrathoracic pressure)
- Orogenital sex during pregnancy (insufflation of vaginal veins)

**Paradoxical air embolism:** Venous air crosses to the arterial circulation through a patent foramen ovale (PFO, present in 25-30% of adults), atrial septal defect, or pulmonary AV malformation. Causes stroke, myocardial infarction, or limb ischemia. Can occur with small volumes of venous air.

**Clinical spectrum (dose-dependent):**

| Volume | Effect |
|--------|--------|
| 0.5-1 mL/kg | Tachycardia, hypotension, dyspnea |
| 1-3 mL/kg | Severe hypotension, arrhythmia, mill-wheel murmur |
| 3-5 mL/kg | Cardiovascular collapse, PEA/asystole |

**Signs and symptoms:**
- **Cardiovascular:** sudden hypotension, tachycardia, arrhythmia (SVT, VT, VF), elevated CVP, JVD, mill-wheel murmur (churning machinery-like murmur over precordium — pathognomonic but often absent), cardiac arrest (PEA or asystole)
- **Respiratory:** acute dyspnea, tachypnea, wheezing, hypoxemia, sudden drop in ETCO2 (followed by rise as cardiac output recovers or zero ETCO2 with cardiac arrest)
- **Neurological (paradoxical embolism):** sudden focal deficit, seizure, altered consciousness, stroke

## Critical Actions

1. **Immediately clamp or occlude the source of air entry.** Cover open CVC hub, clamp disconnected tubing, flood surgical field with saline and lower operative site below the heart.
2. **Place patient in left lateral decubitus position with head down (Durant maneuver).** Traps air in the apex of the right ventricle away from the RV outflow tract. This is the single most critical intervention after stopping air entry.
3. **100% FiO2 via non-rebreather mask or ventilator.** Nitrogen washout accelerates reabsorption of intravascular air by increasing the air-blood nitrogen gradient. Do NOT use nitrous oxide (expands intravascular gas volume).
4. **Aspirate air through existing central venous catheter.** If a multi-lumen CVC is in place, aspirate from the distal (most proximal to heart) port using a 50 mL syringe. Successful aspiration of frothy blood confirms the diagnosis and is therapeutic. Aspirate 30-50 mL repeatedly.
5. **If no CVC in place, emergent placement of a multi-orifice catheter** (e.g., Bunegin-Albin catheter) via right internal jugular or subclavian vein, advanced to the SVC-RA junction, for aspiration. Do NOT delay other interventions for CVC placement.
6. **Aggressive volume resuscitation** — NS or LR 1-2 L rapid bolus to increase venous pressure and reduce further air entrainment.
7. **Vasopressors for refractory hypotension.** Epinephrine 1-10 mcg/min IV infusion (alpha and beta effects support RV function and systemic perfusion) or norepinephrine 0.1-0.5 mcg/kg/min.
8. **ACLS for cardiac arrest.** Standard ACLS protocols with emphasis on epinephrine, chest compressions (may fragment large air lock), and continued aspiration attempts.
9. **Hyperbaric oxygen therapy (HBO)** for paradoxical arterial air embolism with neurological deficit or for refractory cases. Reduces bubble size per Boyle's law and accelerates nitrogen reabsorption.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Pulmonary embolism | No temporal relationship to air-entraining procedure; CTA shows filling defect (not air); no mill-wheel murmur; D-dimer elevated |
| Tension pneumothorax | Absent breath sounds unilaterally; tracheal deviation; hyperresonance; occurs after positive-pressure ventilation or trauma; CXR diagnostic |
| Anaphylaxis | Urticaria, angioedema, bronchospasm; temporal association with drug/allergen exposure; no mill-wheel murmur; responds to epinephrine IM |
| Acute MI | ECG changes (STEMI or dynamic ST/T changes); troponin elevation; no air on echo; no procedure-related trigger |
| Cardiac tamponade | Muffled heart sounds, JVD, hypotension (Beck's triad); echo shows pericardial effusion with diastolic collapse; no air |
| Vasovagal reaction | Bradycardia (not tachycardia); recovers with Trendelenburg and atropine; no sustained hemodynamic compromise |
| Local anesthetic systemic toxicity | Perioral numbness, tinnitus, seizures progressing to cardiac arrest; occurs during regional anesthesia; treat with intralipid |

## Workup

**Bedside (do NOT delay treatment for diagnostic workup):**
- **Precordial Doppler ultrasound:** Most sensitive non-invasive monitor (detects as little as 0.05 mL/kg air). Place over right heart (right sternal border, 4th intercostal space). Characteristic "washing machine" or "roaring" sound. Standard intraoperative monitor for sitting craniotomy.
- **Transesophageal echocardiography (TEE):** Most sensitive imaging modality. Detects intracardiac air bubbles in real time. Identifies PFO with paradoxical embolism. Available in OR/ICU settings.
- **Transthoracic echocardiography (TTE):** Rapidly available in ED. Shows air (echogenic material) in right atrium and ventricle, RV dilation, paradoxical septal motion. Can visualize air crossing PFO.
- **ETCO2 monitoring:** Sudden drop in ETCO2 (air in pulmonary vasculature reduces CO2 exchange). In intubated patients, this is often the first detected sign.

**Labs:**
- ABG — hypoxemia, hypercapnia, metabolic acidosis
- Troponin — paradoxical coronary air embolism causing MI
- Lactate — tissue hypoperfusion
- CBC, BMP, coagulation studies — baseline

**Imaging:**
- **CXR:** Air in the pulmonary artery or right heart (rarely captured); pulmonary edema in later stages
- **CT head (non-contrast):** Intravascular air in cerebral vessels (paradoxical embolism); ischemic changes if delayed
- **CT chest:** Air in pulmonary arteries, right heart chambers, or venous system; more sensitive than CXR
- **CTA:** If PE is in the differential, CTA distinguishes air from thrombus

## Treatment

**Immediate (within seconds — this is the critical window):**
1. Stop air entry — clamp all lines, cover all open venous access, flood surgical wound with saline
2. Durant maneuver — left lateral decubitus, Trendelenburg (head down 15-30 degrees)
3. 100% FiO2 — nitrogen washout to accelerate air reabsorption
4. Aspirate air via CVC — 50 mL syringe from distal port, repeated aspiration of frothy blood

**Hemodynamic support:**
- Crystalloid bolus: NS 1-2 L wide open (increases venous pressure, reduces entrainment gradient)
- Epinephrine infusion: 1-10 mcg/min IV (supports RV contractility, maintains coronary perfusion)
- Norepinephrine: 0.1-0.5 mcg/kg/min IV for systemic vascular resistance support
- Vasopressin: 0.04 units/min IV as adjunct if refractory to catecholamines

**Cardiac arrest management:**
- Standard ACLS: chest compressions, epinephrine 1 mg IV q3-5min, defibrillation for VF/VT
- Chest compressions may fragment a large air lock into smaller bubbles that pass through the pulmonary vasculature
- Continue aspiration via CVC during resuscitation
- Prolonged resuscitation justified — air reabsorbs over time and patients can have full recovery

**Hyperbaric oxygen therapy (HBO):**
- Indicated for paradoxical arterial air embolism with neurological deficit, refractory cardiovascular instability, or large volume air embolism
- Reduces bubble size (Boyle's law: 2.8 ATA reduces bubble volume by 64%)
- Enhances nitrogen gradient for reabsorption
- Provides tissue oxygenation independent of hemoglobin
- Administer within 6 hours of event for best outcomes; benefit may persist up to 24 hours
- Contact nearest HBO facility via Divers Alert Network (DAN) 24/7 hotline: +1-919-684-9111

**Prevention protocols during CVC removal:**
- Patient supine or Trendelenburg
- Apply occlusive dressing immediately upon catheter removal
- Instruct patient to perform Valsalva maneuver during removal (increases venous pressure)
- Hold site for minimum 5 minutes
- Occlusive dressing for 24 hours

## Disposition

**ICU admission (all symptomatic cases):**
- Any hemodynamic compromise
- Requirement for vasopressors
- Neurological deficit (paradoxical embolism)
- Post-cardiac arrest
- Ongoing mechanical ventilation

**HBO transfer:**
- Paradoxical air embolism with neurological deficit
- Refractory hypoxemia or hemodynamic instability despite standard treatment
- Coordinate with DAN for nearest chamber; air transport must be pressurized to ground level (helicopter restricted to <300 m altitude, fixed-wing at cabin pressure 1 ATA)

**Monitored bed:**
- Small volume air embolism with transient symptoms fully resolved
- Stable hemodynamics off vasopressors
- Minimum 24 hours observation — delayed neurological deterioration from paradoxical embolism can occur

**No outpatient disposition for any confirmed air embolism.**

## Pitfalls

1. **Failing to recognize CVC removal as a high-risk procedure.** Air embolism during CVC removal is more common than during insertion. Removing a CVC with the patient sitting upright without Valsalva or occlusive dressing creates a negative pressure gradient that entrains air through the tract. A mature catheter tract remains patent for 24-48 hours after removal.

2. **Placing the patient on the right side instead of the left.** The Durant maneuver requires LEFT lateral decubitus (left side down). This traps air in the apex of the right ventricle, away from the pulmonary outflow tract. Right lateral decubitus positions the air lock directly at the RV outflow tract, worsening obstruction.

3. **Delaying treatment for confirmatory imaging.** Air embolism is a clinical diagnosis. When a patient develops sudden cardiovascular collapse during or immediately after an air-entraining procedure, initiate treatment immediately (stop air entry, Durant maneuver, 100% O2, aspirate CVC). Echocardiography confirms but must not delay intervention.

4. **Forgetting paradoxical embolism through a PFO.** 25-30% of adults have a PFO. Venous air that crosses to the arterial circulation causes stroke, MI, or limb ischemia with volumes as small as 0.5 mL. Any neurological deficit after venous air embolism requires CT head and consideration of HBO, regardless of apparent hemodynamic stability.

5. **Using nitrous oxide in a patient with air embolism.** N2O diffuses into air bubbles 34 times faster than nitrogen diffuses out, expanding intravascular gas volume and worsening hemodynamic compromise. Discontinue N2O immediately if air embolism is suspected during anesthesia.

6. **Assuming small volumes of air are benign.** The lethal dose of 3-5 mL/kg applies to rapid bolus injection. Slower entrainment at lower volumes (0.5-1 mL/kg) still causes clinically significant hypotension, arrhythmia, and paradoxical embolism. There is no "safe" volume of intravascular air.

7. **Not contacting a hyperbaric facility early.** HBO is most effective within 6 hours and benefits diminish with delay. Contact DAN (+1-919-684-9111) at the time of diagnosis, even if the patient appears to be stabilizing. Arranging transport and chamber availability takes time.
