---
id: active-shooter-response
condition: Active Shooter and Mass Violence Event Response
aliases: [active shooter, mass shooting, mass violence event, active assailant, active threat event]
icd10: [Y38.0X0A, Y38.4X0A, Y38.890A, T07.XXXA, T14.90XA]
esi: 1
time_to_harm:
  irreversible_injury: "< 10 minutes for hemorrhagic shock from penetrating wounds"
  death: "< 30 minutes — majority of preventable deaths from compressible hemorrhage"
  optimal_intervention_window: "Tourniquet within 5 minutes of extremity hemorrhage"
category: disaster-mci
track: tier1
sources:
  - type: consensus-statement
    ref: "Jacobs LM et al. The Hartford Consensus: THREAT, a medical disaster preparedness concept. J Am Coll Surg. 2013;217(5):947-953."
    pmid: "24074826"
  - type: consensus-statement
    ref: "Jacobs LM et al. The Hartford Consensus III: Implementation of Bleeding Control. Bull Am Coll Surg. 2015;100(Suppl 1):S1-S20."
    pmid: "26477262"
  - type: pubmed
    ref: "Butler FK et al. Tactical Combat Casualty Care and Wilderness Medicine: Advancing trauma care in austere environments. Emerg Med Clin North Am. 2017;35(2):391-407."
    pmid: "28411933"
  - type: guideline
    ref: "Committee for Tactical Emergency Casualty Care (C-TECC): Guidelines for First Responders with a Duty to Act, 2nd Edition (2019)"
  - type: pubmed
    ref: "Eastman AL et al. Lessons learned from the Fort Hood shootings: an analysis of the EMS response. J Trauma Acute Care Surg. 2013;75(2 Suppl 2):S198-204."
    pmid: "23883905"
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
# Active Shooter and Mass Violence Event Response

## Recognition

**Definition:** An active shooter/mass violence event involves one or more individuals actively engaged in killing or attempting to kill people in a populated area. The event is dynamic, unpredictable, and evolves rapidly. Medical response operates in parallel with law enforcement threat neutralization — not sequentially.

**Scene Assessment:**
- Active vs. contained vs. neutralized threat status determines medical response posture
- Identify weapon type: firearms (handgun, rifle, shotgun), edged weapons, vehicle ramming, improvised explosive device (IED), combination
- Assess for secondary devices or additional attackers — assume multiple threats until confirmed otherwise
- Identify zones: Hot Zone (active threat — law enforcement only), Warm Zone (indirect threat — Rescue Task Force operates), Cool Zone (no immediate threat — treatment/transport area)

**Wound Pattern Recognition by Weapon:**

| Weapon | Injury Pattern | Expected Hemorrhage |
|--------|---------------|---------------------|
| **Handgun** | Low-velocity penetrating, through-and-through common | Moderate; survivable if hemorrhage controlled |
| **Rifle (5.56mm/.223)** | High-velocity cavitation, tumbling projectile, devastating tissue destruction | Massive; higher mortality per wound |
| **Shotgun** | Multiple projectiles, close range devastating, distance attenuates | Variable; close-range lethal, distance survivable |
| **Blast/IED** | Combined blast injury + penetrating fragments + burns | Multi-mechanism; see blast-injury |
| **Vehicle ramming** | Blunt multi-system trauma, pelvic/lower extremity predominance | Internal hemorrhage; delayed presentation |

**Hartford Consensus THREAT Mnemonic:**
- **T**hreat suppression (law enforcement)
- **H**emorrhage control
- **R**apid **E**xtrication to safety
- **A**ssessment by medical providers
- **T**ransport to definitive care

## Critical Actions

1. **Establish Unified Command with law enforcement immediately.** Medical branch operates under IC structure integrated with law enforcement operations. Medical providers do not enter the Hot Zone. Warm Zone operations require Rescue Task Force (RTF) — armed law enforcement escort with medical personnel.

2. **Deploy Rescue Task Forces into Warm Zone.** RTF composition: 2–4 law enforcement officers + 2 medical providers (EMT/paramedic). RTF mission: hemorrhage control, rapid triage (SALT), extraction to Casualty Collection Point. RTF carries: tourniquets (minimum 4 per provider), hemostatic gauze, chest seals, NPA. RTF does NOT carry stretchers, IV supplies, or advanced airway equipment — speed and simplicity.

3. **Hemorrhage control is the single highest-priority medical intervention.** 90% of preventable deaths in mass violence events result from compressible hemorrhage. Apply tourniquets to all extremity hemorrhage — do not waste time with direct pressure first in the Warm Zone. Tourniquet application:
   - Commercial tourniquet (CAT Gen 7, SOFTT-W): apply 2–3 inches proximal to wound, over clothing if needed, tighten windlass until bleeding stops, lock windlass, document time.
   - Junctional hemorrhage (axilla, groin, neck): wound packing with hemostatic gauze (kaolin-impregnated, e.g., QuikClot Combat Gauze), direct pressure for 3 minutes minimum.
   - Truncal hemorrhage: not compressible in the field — rapid extraction and transport.

4. **STOP THE BLEED principles for bystanders and first responders:**
   - Direct pressure for non-extremity wounds
   - Tourniquet for extremity hemorrhage with life-threatening bleeding
   - Wound packing for junctional wounds
   - Do not remove tourniquets in the field — reassess at hospital

5. **Airway management in Warm Zone: NPA only.** Nasopharyngeal airway (28–30 Fr for adults) if unconscious with intact respirations. Do not attempt endotracheal intubation in the Warm Zone. Recovery position for unconscious breathing patients. Tension pneumothorax: needle decompression (14-gauge, 5th intercostal anterior axillary line) if trained provider available.

6. **Rapid triage at Casualty Collection Point.** SALT triage with modification: patients with non-survivable injuries (GSW to head with fixed/dilated pupils and apnea, massive cranial destruction) are triaged Expectant immediately — do not initiate CPR in MCI setting for traumatic arrest with non-survivable mechanism.

7. **Transport to trauma centers — distribute patients.** Closest hospital is not always correct destination. Level I trauma centers receive Red patients. Penetrating torso trauma requires surgical capability. Distribute across 3+ facilities when >10 critical patients. Self-transport patients (walking wounded) will converge on nearest ED regardless of coordination — prepare for unannounced arrivals.

8. **Activate hospital MCI protocols.** Lockdown perimeter (patient may arrive who is the shooter or secondary attacker). Screen all arriving patients for weapons. Establish a single entry point. Prepare for blood product surge — activate massive transfusion protocol capability for multiple simultaneous patients.

## Differential Diagnosis

**Mechanism Differential — initial reports are unreliable:**

| Reported Event | Actual Event Possibilities |
|---------------|---------------------------|
| **"Active shooter"** | Single vs. multiple shooters; shooter with IED (combined attack); domestic violence event misidentified as active shooter |
| **"Explosion"** | IED (intentional), gas leak (accidental), secondary device targeting first responders |
| **"Mass stabbing"** | Edged weapon attack; chemical agent with secondary stabbing |
| **"Vehicle attack"** | Intentional ramming; driver medical event (syncope, seizure, MI); combined vehicle + edged weapon |

**Injury Pattern Differential:**

| Presentation | Likely Mechanism |
|-------------|-----------------|
| Multiple penetrating wounds, low velocity | Handgun |
| Cavitating wounds with massive tissue destruction | High-velocity rifle |
| Blast + fragment wounds | IED/explosive device |
| Crush injuries, pelvic fractures, lower extremity injuries | Vehicle ramming |
| Burns + penetrating | Incendiary device or secondary fire |

## Workup

**Field (Warm Zone/CCP) — minimal:**
- Hemorrhage assessment: tourniquet check, wound inspection
- Triage category assignment (SALT)
- No laboratory studies, no imaging, no monitoring in field

**Hospital (Receiving Facility):**
- FAST exam on all penetrating torso trauma
- CXR (portable AP) for thoracic wounds
- Pelvic XR for blunt (vehicle ramming) victims
- CT with IV contrast for hemodynamically stable penetrating torso trauma — trajectory assessment
- Labs: CBC, T&S (crossmatch 4–6 units), coagulation panel, lactate, ABG, POC hemoglobin
- All gunshot wound patients: 2-view imaging (entry/exit) or CT to identify retained fragments and trajectory

**Forensic Considerations:**
- Preserve clothing in paper bags (not plastic) for law enforcement
- Document wound locations precisely — use body diagrams
- Photograph wounds before surgical intervention when feasible
- Chain of custody for recovered projectiles/fragments

## Treatment

**Pre-Hospital (C-TECC Guidelines):**

**Warm Zone (Indirect Threat Care):**
- Tourniquet for extremity hemorrhage — immediate, no delay
- Hemostatic gauze (QuikClot Combat Gauze or equivalent) packed into junctional wounds, hold pressure 3 min
- Chest seal (vented: HyFin Vent, HALO) for open chest wounds
- Needle decompression for tension pneumothorax: 14-gauge angiocatheter, 3.25-inch minimum length, 5th intercostal space anterior axillary line
- NPA for airway — do not attempt advanced airway
- Rapid extraction to CCP

**Cool Zone (Evacuation Care):**
- Reassess tourniquets — conversion to pressure dressing if transport >2 hours and wound is amenable
- IV/IO access: 18-gauge IV or tibial IO
- Tranexamic acid 1 g IV over 10 min (give within 3 hours of injury)
- Fluid resuscitation: permissive hypotension target SBP 80–90 mmHg (no TBI) or SBP >100 mmHg (with TBI). Crystalloid 500 mL bolus, reassess. Whole blood or pRBC if available in prehospital setting.
- Analgesia: ketamine 0.3 mg/kg IV (sub-dissociative) or 1 mg/kg IM for field analgesia

**Hospital Treatment — Damage Control Resuscitation:**
- Massive transfusion protocol: 1:1:1 pRBC:FFP:platelets. Whole blood (low-titer O, warm fresh) if available.
- Tranexamic acid 1 g IV over 10 min if not already given (within 3 hours of injury)
- Calcium gluconate 1 g IV per 4 units blood products transfused
- Target: temperature >36°C, pH >7.2, ionized calcium >1.0 mmol/L, fibrinogen >150 mg/dL
- Permissive hypotension until surgical hemorrhage control achieved

**Hospital Treatment — Damage Control Surgery:**
- Penetrating torso with hemodynamic instability: emergent laparotomy/thoracotomy
- Abbreviated surgery: pack, ligate, shunt, staple — definitive repair in 24–48 hours after resuscitation
- Temporary abdominal closure for damage control laparotomy
- Extremity vascular injury: temporary shunt, fasciotomy as indicated

**Specific Wound Management:**
- GSW to extremity with vascular injury: tourniquet → OR for vascular repair or shunt; fasciotomy if >6 hours of ischemia
- GSW to chest: chest tube (36–40 Fr) for hemothorax. Autotransfusion if available. Thoracotomy if initial output >1500 mL or ongoing >200 mL/hr.
- GSW to abdomen: exploratory laparotomy for hemodynamic instability, peritonitis, evisceration, or impaled object
- GSW to head: GCS ≤5 with fixed/dilated pupils in MCI — Expectant. GCS 6+ or reactive pupils — neurosurgical consultation, ICP management

## Disposition

**Field Disposition:**
- Red/Immediate: helicopter or ground ambulance to Level I trauma center. Do not delay transport for additional interventions.
- Yellow/Delayed: ground transport to Level I or Level II trauma center
- Green/Minor: bus transport to non-trauma ED or alternate care site
- Expectant: field comfort care or designated comfort area at hospital
- Dead: remain in place for medicolegal investigation; do not transport

**Hospital Disposition:**
- Penetrating trauma requiring surgery: OR → SICU
- Hemodynamically stable penetrating wounds without surgical indication: ED observation 6–24 hours with serial exams
- Minor wounds (superficial GSW, graze injuries): ED treatment and discharge with 48-hour wound check
- All patients: behavioral health screening before discharge (acute stress reaction universal in mass violence survivors)

**Facility Distribution:**
- Pre-established distribution plans activate with MCI. First 5 critical patients to closest Level I. Subsequent patients distributed to Level I/II centers within 30-minute transport radius.
- Self-transport surge: up to 70% of mass violence victims arrive by private vehicle, not ambulance. Nearest hospitals absorb this uncontrolled influx regardless of coordination efforts. Staff accordingly.
- Pediatric patients: route to pediatric trauma center when available; adult trauma centers must be prepared to manage pediatric patients

**Law Enforcement Integration:**
- Maintain single-entry security screening at receiving hospital
- Designate law enforcement liaison officer at each receiving facility
- Prepare for media surge, family reunification center, VIP/elected official arrivals

## Pitfalls

1. **Waiting for scene clearance before medical entry.** Traditional EMS staging until "scene safe" results in preventable deaths. The Warm Zone / Rescue Task Force model enables medical intervention while threat is contained but not fully neutralized. Every minute of delay in hemorrhage control increases mortality. Providers must train for RTF operations before the event — not during.

2. **Failure to apply tourniquets early and aggressively.** Direct pressure wastes time in mass violence events. Tourniquets are first-line for all extremity hemorrhage. The tourniquet conversion debate is a hospital problem, not a field problem. Apply the tourniquet, document the time, move to the next patient. Tourniquet application by bystanders (STOP THE BLEED-trained) before EMS arrival saves lives — the median EMS response time of 7–9 minutes exceeds the hemorrhagic death window.

3. **Initiating CPR for traumatic arrest in MCI.** Traumatic arrest with penetrating mechanism has <2% survival even with immediate thoracotomy. In MCI with limited resources, performing CPR on traumatic arrest patients diverts 2–3 providers from salvageable patients. Triage as Expectant or Dead based on mechanism and presentation.

4. **Transporting all patients to the nearest hospital.** In the 2017 Las Vegas shooting (471 injured), the closest trauma center received 215 patients in 40 minutes. Distribution protocols exist for this reason. Field IC and regional coordination must direct ambulance traffic. However, self-transport patients (~70% of total) will bypass this system — hospitals must plan for uncoordinated arrival surges.

5. **Neglecting hospital lockdown and weapon screening.** Active violence victims may include the perpetrator(s). Secondary attacks targeting hospitals have occurred internationally. Screen all arriving patients for weapons at a single controlled entry point. Security must be in place before the first patient arrives.

6. **Ignoring psychological casualties.** For every physical casualty, expect 4–10 psychological casualties presenting with acute stress reactions, conversion symptoms, or exacerbation of pre-existing psychiatric conditions. These patients consume triage and treatment resources. Route to separate psychological first aid area staffed by behavioral health providers.

### System Overwhelm

Active violence events generate surge patterns distinct from other MCIs — the patient volume arrives in a compressed 15–45 minute window rather than over hours:

- **Blood product depletion:** Mass violence events with 20+ critical patients exhaust a typical hospital blood bank (100–150 units pRBC) within 2–3 hours. Activate regional blood center emergency release immediately at MCI declaration. Low-titer O-whole blood programs (walking blood banks) provide bridge supply. Do not wait for type-specific blood — uncrossmatched O-negative (or O-positive for males) for all critical patients.
- **OR saturation:** 4–6 simultaneous surgical cases exceed most hospital OR capacity. Damage control surgery (pack and close in <60 minutes) maximizes OR throughput. Convert PACU, endoscopy suites, or cardiac cath labs to temporary ORs for simple procedures (wound debridement, fasciotomy).
- **Ventilator demand:** Mass violence with combined blast mechanism or chest wounds generates ventilator demand exceeding supply. Allocation protocols must be pre-established — individual physicians should not make allocation decisions at the bedside.
- **Staff exposure:** Providers treating mass violence victims experience acute vicarious trauma. Rotate staff every 4–6 hours when possible. Embedded behavioral health support during the event, mandatory debriefing within 72 hours.
- **Forensic burden:** Every wound is evidence. Every patient interaction has medicolegal implications. Assign a dedicated forensic documentation team (typically ED nurses with forensic training) to avoid slowing clinical care with evidence preservation tasks.
