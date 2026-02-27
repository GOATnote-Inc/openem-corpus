---
id: blast-injury
condition: Blast Injury
aliases: [explosion injury, bomb injury, blast trauma, primary blast injury, secondary blast injury, blast lung]
icd10: [T70.8XXA, T14.8XXA, T07.XXXA, S27.329A, S09.8XXA, T79.A0XA]
esi: 1
time_to_harm:
  irreversible_injury: "< 60 minutes — blast lung and air embolism progress rapidly"
  death: "< 2 hours for unrecognized tension pneumothorax or blast lung"
  optimal_intervention_window: "Immediate — primary blast lung deteriorates over 24-48 hours even with early recognition"
mortality_if_delayed: "Primary blast lung mortality 45-90% in enclosed-space detonations; secondary fragment injuries mortality depends on hemorrhage control timing"
category: disaster-mci
track: tier1
sources:
  - type: review
    ref: "DePalma RG et al. Blast injuries. N Engl J Med. 2005;352(13):1335-1342."
    pmid: "15800229"
  - type: pubmed
    ref: "Wolf SJ et al. Blast injuries. Lancet. 2009;374(9687):405-415."
    pmid: "19631372"
  - type: pubmed
    ref: "Leibovici D et al. Blast injuries: bus versus open-air bombings — a comparative study of injuries in survivors of open-air versus confined-space explosions. J Trauma. 1996;41(6):1030-1035."
    pmid: "8970558"
  - type: consensus-statement
    ref: "Centers for Disease Control and Prevention (CDC). Explosions and Blast Injuries: A Primer for Clinicians. Atlanta, GA: CDC, 2003."
    url: "https://www.cdc.gov/niosh/docket/archive/pdfs/NIOSH-125/125-ExplosionsandBlastInjuries.pdf"
  - type: pubmed
    ref: "Sasser SM et al. Blast lung injury. Prehosp Emerg Care. 2006;10(2):165-172."
    pmid: "16531371"
last_updated: "2026-02-26"
compiled_by: agent
reviewed_by: "Brandon Dent, MD — Board Certified Emergency Medicine"
review_date: "2026-02-27"
risk_tier: A
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
# Blast Injury

## Recognition

**Definition:** Blast injury results from detonation of high-order (TNT, C-4, dynamite, ANFO) or low-order (pipe bombs, Molotov cocktails, gunpowder) explosives. High-order explosives generate a supersonic overpressure wave that causes unique primary blast injuries. Both high-order and low-order produce secondary, tertiary, and quaternary mechanisms.

**Four Blast Phases:**

| Phase | Mechanism | Target Organs | Typical Injuries |
|-------|-----------|---------------|------------------|
| **Primary** | Overpressure wave (blast wave) interacts with air-fluid interfaces | Lungs, ears, bowel, eyes | Blast lung, TM rupture, bowel perforation, globe rupture |
| **Secondary** | Projectile fragments (shrapnel, debris, bone) propelled by blast | Any body region | Penetrating wounds, lacerations, eye injuries, embedded foreign bodies |
| **Tertiary** | Body displacement / structural collapse / victim thrown | Head, spine, extremities, torso | Blunt trauma: TBI, fractures, crush injuries, traumatic amputation |
| **Quaternary** | Burns, inhalation, radiation, chemical, psychological | Skin, lungs, psyche | Flash burns, inhalation injury, radiation exposure, PTSD, exacerbation of chronic disease (MI, asthma) |

**Confined-Space vs. Open-Air Explosions:**
- Confined space (bus, building, subway): blast wave reflects off walls → amplified primary blast injury. Mortality 2–3x higher than open-air. Expect higher prevalence of blast lung and bowel injury.
- Open-air: blast wave dissipates with distance (inverse cube law). Primary blast injury less common. Secondary and tertiary mechanisms dominate.

**Primary Blast Injury — Organ-Specific Recognition:**

**Blast Lung (pulmonary blast injury):**
- Most common fatal primary blast injury among initial survivors
- Onset: immediate to 48 hours post-blast (delayed presentation is the rule)
- Signs: dyspnea, cough, hemoptysis, chest tightness, hypoxia
- CXR: bilateral "butterfly" or "bat-wing" infiltrates (NOT cardiogenic — no pulmonary venous congestion)
- Triad: apnea, bradycardia, hypotension at presentation suggests severe blast lung

**Tympanic Membrane Rupture:**
- Most sensitive indicator of primary blast exposure (threshold: ~5 psi overpressure)
- Present in 50% of blast survivors; absence does NOT rule out primary blast injury
- Otoscopic exam: perforation, hemorrhage, middle ear debris
- Hearing loss (conductive or sensorineural), tinnitus, vertigo

**Blast Bowel:**
- Delayed presentation 24–48 hours; can present up to 14 days post-blast
- Signs: abdominal pain, rebound, rigidity, absent bowel sounds, free air on imaging
- Colon and ileocecal junction are most vulnerable (gas-containing)
- Mesenteric ischemia and delayed perforation cause sepsis

**Blast Eye Injuries:**
- Globe rupture, hyphema, vitreous hemorrhage, retinal detachment
- Secondary fragment injuries to orbits and eyes
- All blast patients require formal ophthalmologic exam within 24 hours

## Critical Actions

1. **Scene safety and secondary device awareness.** All blast scenes carry risk of secondary explosions targeting first responders. Maintain safe perimeter. Medical providers enter only after EOD (Explosive Ordnance Disposal) or law enforcement clearance. Structural collapse risk persists.

2. **Triage using SALT or START.** Blast events are MCI events — apply mass casualty triage protocols. Expect bimodal distribution: immediate survivors with moderate injuries + delayed presenters with occult primary blast injury. Do not under-triage ambulatory patients — blast lung presents after a lucent interval.

3. **Assess all blast-exposed patients for primary blast injury regardless of visible wounds.** External injuries do not predict internal blast injury. An ambulatory patient with intact skin and no visible wounds can have lethal blast lung or bowel injury. Every patient within the blast radius requires formal evaluation.

4. **Bilateral otoscopic examination.** TM rupture is the most sensitive blast-exposure marker. Bilateral rupture suggests high overpressure exposure and increased risk of blast lung and bowel injury. Document hearing status.

5. **CXR on every blast-exposed patient.** Blast lung CXR may be initially normal — repeat at 4–6 hours and 24 hours post-exposure. CT chest is more sensitive but not feasible in MCI. Bilateral infiltrates without cardiomegaly or cephalization = blast lung until proven otherwise.

6. **Avoid positive-pressure ventilation until blast lung is assessed.** Overpressure disrupts alveolar-capillary interface. Positive pressure ventilation increases risk of air embolism and tension pneumothorax. If intubation required: low tidal volume (6 mL/kg IBW), low PEEP (start 5 cmH2O, titrate cautiously), permissive hypercapnia (accept PaCO2 50–60 mmHg if pH >7.20).

7. **Monitor for arterial air embolism.** Primary blast injury creates bronchovenous fistulae. Positive pressure ventilation forces air into pulmonary veins → systemic arterial air embolism → stroke, MI, mesenteric ischemia, sudden cardiac arrest. Signs: sudden neurological deficit, focal deficit inconsistent with head injury, livedo reticularis, coronary air on echo. Treatment: left lateral decubitus/Trendelenburg position, 100% O2, hyperbaric oxygen if available.

8. **Serial abdominal exams for all blast-exposed patients.** Blast bowel presents hours to days after exposure. Perform FAST, serial abdominal exams every 4–6 hours for 24 hours minimum. CT abdomen/pelvis with IV contrast if abdominal tenderness, free fluid on FAST, or hemodynamic instability.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **Blast lung vs. pulmonary contusion** | Both cause bilateral infiltrates; blast lung occurs without direct chest wall impact and is specific to overpressure exposure; pulmonary contusion requires direct blunt force |
| **Blast lung vs. ARDS** | Blast lung onset <48h post-exposure, bilateral infiltrates with no prior illness; ARDS develops from sepsis, aspiration, or transfusion over 48–72h; both treated similarly but blast lung carries air embolism risk |
| **Blast lung vs. cardiogenic pulmonary edema** | Blast lung: no cardiomegaly, no cephalization, no Kerley B lines, no JVD; cardiac echo normal LV function (unless concurrent cardiac contusion) |
| **Blast bowel vs. mesenteric ischemia** | Blast bowel follows blast exposure with lucent interval; mesenteric ischemia has vascular risk factors; CT findings similar (bowel wall edema, pneumatosis, free fluid) |
| **Blast TBI vs. blunt TBI** | Primary blast TBI: diffuse axonal injury pattern without impact; often no visible scalp wound; combined primary + tertiary mechanism common |
| **Arterial air embolism vs. stroke** | Acute focal neurological deficit post-blast with positive pressure ventilation → air embolism until proven otherwise; CT may show intravascular air; echocardiography may demonstrate air |

## Workup

**All Blast-Exposed Patients (regardless of symptoms):**
- Bilateral otoscopic examination with hearing assessment
- CXR PA/lateral (repeat at 4–6h and 24h if initially normal)
- SpO2 monitoring (continuous for minimum 6 hours)
- CBC, BMP, lactate, type and screen
- Urinalysis (myoglobinuria from crush/tertiary injury)

**Symptomatic or High-Exposure Patients:**
- CT chest without contrast for blast lung characterization
- CT abdomen/pelvis with IV contrast for abdominal complaints or hemodynamic instability
- FAST exam (free fluid → OR or CT based on hemodynamics)
- CT head without contrast for altered mental status, focal deficits, or mechanism suggesting TBI
- Troponin (cardiac contusion from blast wave or tertiary mechanism)
- ABG (quantify oxygenation impairment, assess for metabolic acidosis)
- Coagulation panel: PT, INR, PTT, fibrinogen (DIC screening — blast injury is a common trigger)

**Delayed Evaluation (24–48h):**
- Repeat CXR for all patients with primary blast exposure
- Formal ophthalmologic exam (slit lamp, dilated fundoscopy)
- Audiology referral for all TM ruptures and hearing complaints
- Repeat abdominal exam and FAST at 24h for blast bowel surveillance

## Treatment

**Blast Lung:**
- Oxygen: high-flow nasal cannula (40–60 L/min, FiO2 0.6–1.0) as first-line
- Avoid positive pressure ventilation unless SpO2 <88% despite HFNC
- If intubation required: ketamine 1–2 mg/kg IV for RSI induction (hemodynamically stable); low tidal volume 6 mL/kg IBW; PEEP 5 cmH2O initially, increase by 2 cmH2O increments only if hypoxia refractory (higher PEEP = higher air embolism risk); plateau pressure <30 cmH2O; permissive hypercapnia (PaCO2 50–60 acceptable if pH >7.20)
- Fluid management: restrictive strategy; avoid crystalloid boluses unless hemorrhagic shock coexists
- Chest tube (28–36 Fr) for pneumothorax or hemothorax
- Bilateral chest tubes prophylactically for severe blast lung requiring mechanical ventilation (high risk of bilateral tension pneumothorax)
- Prone positioning if severe ARDS physiology develops (P/F <150)

**Arterial Air Embolism:**
- Position: left lateral decubitus with head of bed down 15° (Durant maneuver — traps air in RV apex)
- 100% FiO2 (nitrogen washout accelerates air resorption)
- Hyperbaric oxygen therapy at 2.8 ATA if available (definitive treatment)
- Intubation and mechanical ventilation as needed — accept the paradox (positive pressure worsens fistula but may be required for oxygenation)
- Aspirin 325 mg PO/NG if stroke pattern (after ruling out hemorrhagic CVA)

**Hemorrhage from Secondary/Tertiary Blast Injury:**
- Tourniquet for extremity hemorrhage: CAT or SOFTT-W
- Hemostatic gauze packing for junctional wounds
- Damage control resuscitation: massive transfusion protocol 1:1:1 (pRBC:FFP:platelets)
- Tranexamic acid 1 g IV over 10 min within 3 hours of injury
- Calcium gluconate 1 g IV per 4 units blood products
- Permissive hypotension (SBP 80–90 mmHg) for penetrating mechanism without TBI
- Damage control surgery for truncal hemorrhage

**Blast Bowel:**
- NPO, nasogastric tube for decompression
- Broad-spectrum antibiotics: piperacillin-tazobactam 4.5 g IV q6h for peritonitis
- CT abdomen with IV contrast → surgical consultation for free air, mesenteric ischemia, or peritoneal signs
- Exploratory laparotomy for perforation, free air, or hemodynamic instability

**Burns (Quaternary):**
- Estimate BSA (Rule of Nines for adults, Lund-Browder for children)
- Parkland formula for burns >20% BSA: 4 mL/kg × %BSA LR over 24h (half in first 8h)
- Inhalation injury: early intubation for stridor, hoarse voice, singed nasal hairs, carbonaceous sputum
- Escharotomy for circumferential full-thickness burns with vascular compromise

**Analgesia:**
- Ketamine 0.3 mg/kg IV (sub-dissociative) for acute pain management
- Morphine 0.1 mg/kg IV q10min PRN for severe pain after hemodynamic stabilization
- Regional anesthesia (fascia iliaca block, femoral nerve block) for extremity fractures when available

## Disposition

**Admit (minimum 24h observation) all blast-exposed patients with:**
- Any CXR abnormality
- SpO2 <95% at any point
- TM rupture (especially bilateral — marker of high overpressure)
- Abdominal complaints or FAST-positive
- Any penetrating wound
- Burns >10% BSA or inhalation injury
- TBI (any severity)

**Extended observation (6–24h) for asymptomatic blast-exposed patients:**
- Normal CXR, normal SpO2, normal exam
- Repeat CXR at 4–6h
- Discharge only if 6h CXR normal, SpO2 stable, no abdominal complaints, reliable follow-up
- Return precautions: dyspnea, hemoptysis, abdominal pain, hearing changes, vision changes

**ICU Admission:**
- Blast lung requiring supplemental oxygen or mechanical ventilation
- Hemodynamic instability from any mechanism
- Massive transfusion
- DIC
- Post-operative damage control surgery
- Arterial air embolism

**Transfer:**
- Burn patients >20% BSA or inhalation injury → Burn Center
- Blast eye injuries requiring surgery → Ophthalmology with microsurgical capability
- Hyperbaric oxygen for air embolism → facility with HBO chamber

**MCI Distribution:**
- Confined-space blast events generate higher proportions of critical patients than open-air events — allocate more Red transport capacity
- Delayed presenters (blast lung, blast bowel) arrive 6–48h post-event — receiving facilities must maintain surge capacity for second wave

## Pitfalls

1. **Discharging blast-exposed patients based on normal initial CXR.** Blast lung may not manifest radiographically for 24–48 hours. A patient with bilateral TM rupture and normal initial CXR has sustained significant overpressure exposure and requires observation with repeat imaging. Discharge at presentation = missed blast lung → respiratory failure at home.

2. **Applying positive pressure ventilation without recognizing blast lung physiology.** Standard ARDS ventilation protocols apply, but the air embolism risk is unique to blast lung. The disrupted alveolar-capillary membrane creates bronchovenous fistulae. Every cmH2O of PEEP increases the fistula gradient. Use the minimum PEEP necessary, accept worse PaO2, and watch for sudden neurological change (coronary or cerebral air embolism).

3. **Using TM rupture as the sole indicator of primary blast exposure.** TM rupture sensitivity for primary blast injury is approximately 50%. The absence of TM rupture does not rule out blast lung or blast bowel. Assessment for primary blast injury must be based on proximity to detonation, confined vs. open-air environment, and clinical symptoms — not otoscopy alone.

4. **Missing blast bowel due to delayed presentation.** Blast bowel manifests 24–48 hours post-exposure (up to 14 days). Patients discharged before this window present to community EDs with abdominal pain and sepsis without context that they were blast-exposed. Discharge instructions must include specific return precautions for abdominal symptoms, and all blast patients require 24–48h abdominal follow-up.

5. **Failing to screen for embedded fragments.** Secondary blast injury embeds metal, glass, bone, and environmental debris throughout the body. Small fragments may not produce entry wounds visible on primary survey. CT imaging reveals embedded fragments in locations not suspected clinically. All blast patients with secondary fragment exposure require imaging of affected body regions.

6. **Ignoring the quaternary blast category.** Flash burns, inhalation injury, crush from structural collapse, exacerbation of chronic disease (acute MI, asthma attack, COPD exacerbation), and toxic exposure from burning materials all cause mortality in blast events. Treating only the "blast injury" while missing the MI triggered by the stress response is a lethal oversight.

### System Overwhelm

Blast events generate the most complex MCI patient mix — simultaneous primary, secondary, tertiary, and quaternary mechanisms across dozens to hundreds of patients:

- **Triage complexity:** Unlike single-mechanism events (shooting, vehicle crash), blast patients present with overlapping injury patterns. A single patient may have blast lung (primary), shrapnel to abdomen (secondary), TBI from being thrown (tertiary), and flash burns (quaternary). Standard START/SALT under-classifies these complex patients.
- **Imaging bottleneck:** CT is the critical resource for blast injury workup (chest, abdomen, head). A single CT scanner processes one study every 15–20 minutes. With 30+ patients requiring CT, the imaging queue extends 8–10 hours. Prioritize: hemodynamically unstable → neurologically altered → abdominal complaints → chest symptoms. Use CXR and FAST as surrogates.
- **Surgical demand:** Blast events produce more operative cases per capita than any other MCI type. Confined-space events: 30–40% of survivors require surgery. Activate all available ORs, recall all available surgeons (general surgery, orthopedics, neurosurgery, vascular), and implement damage control approach to maximize OR throughput.
- **Delayed surge:** The 24–48h delay in blast lung and blast bowel presentation means the second wave arrives a full day after the event when the hospital is demobilizing. Maintain observation capacity and staff awareness for 72 hours post-blast event.
- **Blood supply:** Multi-mechanism injuries increase blood product consumption per patient. Average: 6–10 units pRBC per surgical blast patient. A 20-patient blast MCI may require 100–200 units pRBC in the first 12 hours. Activate regional blood mutual aid at MCI declaration, do not wait for depletion.
