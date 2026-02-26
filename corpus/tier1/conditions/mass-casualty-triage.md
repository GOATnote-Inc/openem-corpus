---
id: mass-casualty-triage
condition: Mass Casualty Incident Triage and Management
aliases: [MCI, mass casualty incident, multiple casualty incident, disaster triage]
icd10: [T07.XXXA, X37.0XXA, X37.1XXA, X38.XXXA, Y38.0X0A]
esi: 1
time_to_harm:
  irreversible_injury: "< 60 minutes for critically injured patients without triage"
  death: "< 2 hours without organized field triage and transport"
  optimal_intervention_window: "First 30 minutes — triage accuracy degrades with delay"
category: disaster-mci
track: tier1
sources:
  - type: consensus-statement
    ref: "Lerner EB et al. Mass casualty triage: an evaluation of the data and development of a proposed national guideline (SALT Triage). Disaster Med Public Health Prep. 2008;2(Suppl 1):S25-34."
    pmid: "18769263"
  - type: pubmed
    ref: "Benson M et al. The use of triage in disaster medicine. Ann Emerg Med. 1996;28(2):136-144."
    pmid: "8759575"
  - type: pubmed
    ref: "Romig LE. Pediatric triage: a system to JumpSTART your triage of young patients at MCIs. JEMS. 2002;27(7):52-63."
    pmid: "12141119"
  - type: guideline
    ref: "FEMA Emergency Support Function #8 — Public Health and Medical Services Annex, National Response Framework (2019)"
  - type: pubmed
    ref: "Jenkins JL et al. Mass-casualty triage: time for an evidence-based approach. Prehosp Disaster Med. 2008;23(1):3-8."
    pmid: "18491654"
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
# Mass Casualty Incident Triage and Management

## Recognition

**Definition:** A mass casualty incident (MCI) occurs when the number of patients exceeds available resources. The threshold is facility-dependent — a rural critical access hospital with 2 nurses and 1 physician reaches MCI at 5 critical patients; a Level I trauma center may absorb 20 before activating MCI protocols.

**Scene Assessment:**
- Identify mechanism: natural disaster, structural collapse, transportation incident, explosion, active violence, chemical/biological/radiological/nuclear (CBRN)
- Establish scene safety: secondary devices, structural instability, hazardous materials, active threat
- Estimate patient count and distribute across triage categories
- Identify access/egress routes and casualty collection points (CCPs)

**Incident Command Activation Triggers:**
- ≥5 patients requiring emergency transport simultaneously
- ≥3 critical patients presenting to a single ED within 30 minutes
- Any CBRN event regardless of patient count
- Any event requiring mutual aid from neighboring jurisdictions
- Hospital surge: ED census exceeds 120% of staffed bed capacity

**MCI Declaration Elements:**
1. Activate Hospital Incident Command System (HICS)
2. Designate Medical Branch Director, Triage Officer, Treatment Area Supervisor, Transport Officer
3. Establish triage, treatment, and transport areas in the field
4. Notify receiving hospitals via regional coordination center
5. Activate surge staffing (call-back lists, disaster credentialing)

## Critical Actions

1. **Activate Incident Command System (ICS) immediately.** Assign Incident Commander (IC), establish unified command if multi-agency. The IC does not provide patient care — the IC coordinates resources. Failure to establish command structure is the single most common cause of MCI response failure.

2. **Perform field triage using SALT (Sort-Assess-Lifesaving interventions-Treatment/Transport):**
   - **Sort:** Global sorting by voice command — "Walk to the sound of my voice" (walking wounded → Minor/Green). Remaining patients assessed by wave/purposeful movement (Delayed) vs. still/obvious life threat (Immediate).
   - **Assess:** Individually assess non-ambulatory patients: obeys commands? → has peripheral pulse? → not in respiratory distress? → major hemorrhage controlled?
   - **Lifesaving interventions only:** Open airway (jaw thrust/recovery position), apply tourniquet/direct pressure for massive hemorrhage, chest seal for open pneumothorax, auto-injector antidote for chemical exposure. Stop. No splinting, no IV access, no definitive care in the field during triage.
   - **Assign category:** Immediate (Red), Delayed (Yellow), Minor (Green), Expectant (Gray/Blue), Dead (Black).

3. **START Triage for adult patients (alternative to SALT):**
   - Respirations: absent after repositioning airway → Dead (Black). Present and >30/min → Immediate (Red).
   - Perfusion: radial pulse absent OR capillary refill >2 sec → Immediate (Red). Control hemorrhage with direct pressure.
   - Mental status: does not follow simple commands → Immediate (Red). Follows commands → Delayed (Yellow).
   - All ambulatory patients → Minor (Green).

4. **JumpSTART for pediatric patients (age 1–8):**
   - Non-ambulatory, apneic after airway positioning → give 5 rescue breaths. If respirations resume → Immediate (Red). If no response → Dead (Black).
   - Respirations 15–45/min: proceed to perfusion check. <15 or >45 → Immediate (Red).
   - Perfusion: peripheral pulse absent → Immediate (Red).
   - Mental status: AVPU scale — P or U → Immediate (Red); A or V → Delayed (Yellow).
   - Infants <1 year: triaged as Immediate (Red) by default if non-ambulatory.

5. **Establish casualty collection point (CCP) and treatment areas.** Separate treatment areas by triage category. Red (Immediate) area closest to transport corridor. Green (Minor) area farthest from transport to prevent convergence on ambulances.

6. **Allocate transport by triage priority.** Red patients to Level I/II trauma centers first. Do not send all patients to the nearest hospital — distribute across receiving facilities. Regional coordination center manages bed availability. Target: no single facility receives >30% of total MCI patients.

7. **Activate hospital surge capacity.** Cancel elective procedures. Convert PACU, OR holding, endoscopy suites to treatment areas. Discharge stable inpatients. Establish alternate care sites (conference rooms, lobbies). Deploy disaster supply caches.

8. **Implement crisis standards of care when resources are exhausted.** Shift from individual-patient optimization to population-level benefit maximization. Document triage decisions. Expectant category patients receive comfort care only.

## Differential Diagnosis

MCI triage itself is not a diagnostic entity — the differential applies to **MCI declaration vs. surge vs. routine operations:**

| Scenario | Distinguishing Features |
|----------|------------------------|
| **True MCI** | Patient volume exceeds institutional capacity; mutual aid required; crisis standards of care activated |
| **Multi-patient event (not MCI)** | 3–5 patients, manageable within existing staffing; no activation of ICS required |
| **Surge event** | Volume increase (e.g., influenza season) stresses capacity but does not require crisis standards; managed with overtime and diversion |
| **Disaster (prolonged MCI)** | Sustained MCI lasting >24 hours; infrastructure damage (power, water, communications); requires state/federal resources |

**Triage Category Differential — common mis-categorization errors:**

| Error | Consequence |
|-------|-------------|
| Over-triage (Yellow → Red) | Overwhelms Red treatment area; delays care for truly critical patients |
| Under-triage (Red → Yellow) | Preventable death from delayed intervention |
| Failing to assign Expectant | Resources consumed on non-survivable injuries at the expense of salvageable patients |
| Treating Green patients first | Most common error by untrained providers; lowest-acuity patients are loudest and most visible |

## Workup

**Field (Triage Phase):**
- No diagnostic workup during field triage — triage is a sorting tool, not a diagnostic process
- SALT/START assessment takes 30–60 seconds per patient; any longer delays downstream patients
- Document triage category on triage tag (paper or electronic) — tag stays with patient

**Hospital (Treatment Phase):**
- All Red/Immediate patients: FAST exam, CXR (portable), pelvis XR, CBC, T&S or crossmatch, lactate, POC glucose
- All Yellow/Delayed patients: focused exam, targeted imaging based on mechanism
- Green/Minor patients: standardized rapid assessment form, defer imaging unless clinical concern
- Re-triage at hospital arrival — field triage category is a starting point, not a disposition

**Documentation:**
- Triage tag number, category assignment, time
- Decontamination status (if CBRN)
- Lifesaving interventions performed in field
- Track patient flow on incident tracking board or MCI-specific EMR module

## Treatment

**Field Treatment by Triage Category:**

**Red (Immediate):**
- Airway: jaw thrust, NPA/OPA, recovery position. Endotracheal intubation only if trained provider available and will not delay triage of remaining patients.
- Breathing: needle decompression for tension pneumothorax (14-gauge, 2nd intercostal space midclavicular OR 5th intercostal anterior axillary). Chest seal for open pneumothorax (vented preferred).
- Circulation: tourniquet for extremity hemorrhage (CAT or SOFTT-W, applied 2–3 inches proximal to wound, tightened until bleeding stops, time documented on tourniquet). Hemostatic gauze (kaolin or chitosan-based) packed into junctional wounds with direct pressure. Pelvic binder for suspected pelvic fracture.
- No IV fluid resuscitation in field during MCI unless transport delayed >30 minutes.

**Yellow (Delayed):**
- Wound packing, pressure dressings, splinting
- Oral analgesics if alert: acetaminophen 1000 mg PO, ibuprofen 800 mg PO
- IV access established during treatment phase if resources available

**Green (Minor):**
- Self-aid and buddy-aid
- Wound cleansing, bandaging, tetanus prophylaxis
- Psychological first aid

**Expectant (Gray):**
- Comfort care: morphine 5–10 mg IV/IM q15min PRN, or ketamine 0.5 mg/kg IV for analgesia
- If resources become available and patient remains viable, upgrade to Red and treat

**Hospital Surge Treatment Adjustments:**
- Damage control resuscitation: 1:1:1 pRBC:FFP:platelets, permissive hypotension (SBP 80–90 mmHg) for penetrating trauma without TBI
- Damage control surgery: abbreviated procedures (pack and close), definitive repair deferred
- Ventilator allocation: crisis standards if ventilator demand exceeds supply — use SOFA-based or similar triage tool for allocation

## Disposition

**Field Disposition:**
- Red patients transported first to highest-capability facility (Level I/II trauma center)
- Yellow patients transported second, distributed across Level II/III facilities
- Green patients transported last or via bus/van to alternate care sites
- Expectant patients remain in field or transferred to comfort care area
- Dead patients: do not transport; document location, do not move until medicolegal authority (coroner/medical examiner) authorizes

**Hospital Disposition:**
- Red patients: OR, ICU, or resuscitation bay
- Yellow patients: ED treatment area, observation unit, or OR when available
- Green patients: fast-track area, lobby triage, or alternate care site
- Re-triage continuously — patients decompensate (Yellow → Red) or improve (Red → Yellow)

**Facility Load-Balancing:**
- Regional coordination center assigns patients to hospitals based on: remaining capacity, specialty capability (burn, pediatric, neurosurgery), distance
- No single facility receives all patients — distribute even if nearest hospital is not at capacity
- Activate mutual aid agreements for transport and staffing before capacity is reached
- Track patient distribution on regional dashboard (WebEOC, EMTrack, or equivalent)

**Demobilization:**
- MCI stands down when patient volume returns to manageable levels
- After-action review within 72 hours
- Critical incident stress debriefing for staff

## Pitfalls

1. **Failure to establish Incident Command.** Without a clear IC, resources converge chaotically. Ambulances arrive at the closest hospital and bypass higher-capability centers. Communication breaks down between field and hospital. Every MCI plan dies the moment nobody is in charge.

2. **Treating instead of triaging.** The natural instinct of every emergency provider is to stop and treat the first critically injured patient encountered. In MCI, this delays triage of dozens of remaining patients. The triage officer tags and moves — 30–60 seconds per patient maximum. Definitive care happens in the treatment area, not the triage area.

3. **Failure to assign Expectant category.** Declaring a patient Expectant is psychologically difficult. Providers default to categorizing non-survivable injuries as Red, consuming ventilators, blood products, and OR time that salvageable patients need. Expectant designation is a resource allocation decision, not an abandonment decision. It must be made early and by a designated senior clinician.

4. **Sending all patients to the nearest hospital.** The closest ED is overwhelmed within minutes. Hospitals 20 minutes farther away sit empty. Regional distribution through a coordination center is essential. If no coordination center exists, the field IC must direct ambulances to alternate facilities.

5. **Over-triaging pediatric patients.** Children with tachycardia and crying are not Immediate — they are responsive and perfusing. JumpSTART addresses pediatric-specific vital sign ranges. Applying adult START criteria to children results in massive over-triage and depletes Red resources.

6. **Ignoring the second wave.** Initial MCI response focuses on the first cohort of patients. The second wave arrives 1–4 hours later: walking wounded who self-transport, patients with delayed presentations (blast lung, crush syndrome), and patients transferred from overwhelmed facilities. Hospitals must reserve surge capacity for the second wave.

### System Overwhelm

MCI is the defining scenario for system overwhelm. The transition from conventional to crisis standards of care is the inflection point:

- **Staffing collapse:** Call-back lists yield 30–50% response rates. Remaining staff work 12–24 hour shifts with degrading performance. Assign 2:1 or 3:1 patient-to-nurse ratios in ICU. Use non-critical-care nurses for monitoring with physician oversight.
- **Supply exhaustion:** Blood bank depletes within 2–4 hours of massive MCI. Activate regional blood mutual aid. Ventilator shortages require allocation protocols (SOFA-based triage committees, not bedside physician discretion). Medication substitutions (ketamine for propofol, morphine for fentanyl) when preferred agents exhaust.
- **Communication failure:** Radio frequencies saturate, cell towers overload, EMR systems crash under volume. Designate runners, use whiteboards for patient tracking, revert to paper triage tags. Establish a single communication officer per facility to interface with regional coordination.
- **Morgue capacity:** Mass fatality events exceed hospital morgue capacity (typically 10–20 bodies). Activate refrigerated trailer mutual aid. Do not store remains in clinical areas — designate a separate, secure location.
- **Psychological toll:** Staff moral injury from Expectant triage decisions, pediatric casualties, and prolonged operations. Do not delay debriefing — embedded behavioral health support during the event reduces post-incident PTSD.
