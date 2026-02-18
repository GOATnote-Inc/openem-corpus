---
id: traumatic-brain-injury
condition: Traumatic Brain Injury
aliases: [TBI, head injury, closed head injury, intracranial hemorrhage (traumatic), brain trauma]
icd10: [S06.9X0A, S06.0X0A, S06.4X0A, S06.5X0A, S06.6X0A, S06.309A]
esi: 1
time_to_harm: "< 60 minutes"
mortality_if_delayed: "30-50% for severe TBI; herniation is rapidly fatal"
category: traumatic
track: tier1
sources:
  - type: guideline
    ref: "Brain Trauma Foundation: Guidelines for the Management of Severe Traumatic Brain Injury, 4th Edition (2016)"
  - type: guideline
    ref: "ATLS Advanced Trauma Life Support, 10th Edition (2018)"
  - type: pubmed
    ref: "Carney N et al. Guidelines for the Management of Severe Traumatic Brain Injury, Fourth Edition. Neurosurgery 2017;80(1):6-15"
    pmid: "27654000"
  - type: pubmed
    ref: "Stocchetti N, Maas AI. Traumatic intracranial hypertension. N Engl J Med 2014;370(22):2121-2130"
    pmid: "24869722"
  - type: pubmed
    ref: "Stiell IG et al. The Canadian CT Head Rule for patients with minor head injury. Lancet 2001;357(9266):1391-1396"
    pmid: "11356436"
  - type: guideline
    ref: "Eastern Association for the Surgery of Trauma (EAST): Evaluation and Management of Blunt Traumatic Aortic Injury — includes TBI co-management (2015)"
last_updated: "2026-02-18"
compiled_by: agent
reviewed_by: null
verification:
  pmids_verified: "2026-02-18"
  audit_completed: "2026-02-18"
---

# Traumatic Brain Injury

## Recognition

**Classification by GCS:**
- Severe TBI: GCS 3-8 (requires intubation and ICP monitoring)
- Moderate TBI: GCS 9-12 (requires CT and observation, frequent neurological exams)
- Mild TBI: GCS 13-15 (use Canadian CT Head Rule or NEXUS II for imaging decision)

**Types of Intracranial Hemorrhage:**
- **Epidural hematoma (EDH):** lens-shaped, arterial (middle meningeal artery), lucid interval then rapid deterioration, ipsilateral pupil dilation
- **Subdural hematoma (SDH):** crescent-shaped, bridging vein disruption, elderly/anticoagulated/alcoholic patients, progressive decline
- **Subarachnoid hemorrhage (traumatic):** blood in sulci/cisterns, headache, photophobia
- **Intraparenchymal hemorrhage/contusion:** coup-contrecoup, frontal and temporal lobes most common
- **Diffuse axonal injury (DAI):** shearing of white matter, coma with minimal CT findings, MRI shows punctate hemorrhages

**Signs of Herniation (uncal):**
- Ipsilateral fixed, dilated pupil (CN III compression)
- Contralateral hemiparesis (progressing to bilateral posturing)
- Cushing triad: hypertension, bradycardia, irregular respirations (late, pre-terminal)
- Rapid decline in GCS

**Canadian CT Head Rule (minor head injury, GCS 13-15):**
High-risk (for neurosurgical intervention): GCS <15 at 2h post-injury, suspected open/depressed skull fracture, any sign of basal skull fracture (raccoon eyes, Battle sign, CSF otorrhea/rhinorrhea, hemotympanum), >=2 episodes of vomiting, age >=65.
Medium-risk (for brain injury on CT): amnesia before impact >30 min, dangerous mechanism (pedestrian struck, ejection from vehicle, fall >3 feet or >5 stairs).

## Critical Actions

1. **Secure airway with cervical spine precautions** — intubate all patients with GCS <=8. RSI with video laryngoscopy. Avoid hypoxia (SpO2 <90) and hypotension (SBP <100) — each independently doubles mortality.
2. **Maintain SBP >100 mmHg** (Brain Trauma Foundation target). Fluid resuscitate with NS or LR. Vasopressors (norepinephrine 0.1-0.5 mcg/kg/min) if fluid-unresponsive.
3. **Emergent CT head without contrast** — within 30 minutes of arrival for moderate/severe TBI.
4. **Reverse anticoagulation immediately** — warfarin: 4-factor PCC 25-50 units/kg IV + vitamin K 10 mg IV. DOACs: idarucizumab 5g IV for dabigatran; andexanet alfa or 4-factor PCC 50 units/kg for factor Xa inhibitors. Antiplatelet: platelet transfusion is NOT routinely recommended (PATCH trial).
5. **Treat elevated ICP** — head of bed 30 degrees, head midline, loosen c-collar if compressing neck veins. Osmotic therapy: mannitol 1 g/kg IV (20% solution) or hypertonic saline 23.4% 30 mL IV via central line (or 3% saline 250 mL IV peripheral OK). Hyperventilate briefly to PaCO2 30-35 mmHg ONLY as bridge to definitive intervention.
6. **Emergent neurosurgical consultation** — for all operative lesions (EDH, large SDH >10mm, depressed skull fracture, posterior fossa hemorrhage).

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Stroke (ischemic/hemorrhagic) | Focal deficits without trauma history, no scalp laceration/hematoma, CT/CTA distinguishes |
| Hypoglycemia | Fingerstick glucose <60, responds to dextrose, no focal CT findings |
| Post-ictal state | Witnessed seizure, tongue laceration, gradual improvement; trauma may be secondary to fall |
| Intoxication (alcohol/drugs) | Altered mental status attributed to intoxication — MUST image if mechanism or exam concerning; intoxication does not protect from TBI |
| Cervical spine injury | Quadriplegia/paraplegia without intracranial pathology on CT head; CT c-spine mandatory |
| Non-accidental trauma (children) | Retinal hemorrhages, inconsistent history, multiple injury ages, subdural hematomas in infants |
| CNS infection (meningitis, abscess) | Fever, meningismus, no trauma mechanism; LP after imaging |

## Workup

**Imaging:**
- CT head without contrast — gold standard for acute traumatic hemorrhage. Obtain within 30 minutes for GCS <=12 or high-risk minor TBI features.
- CT c-spine — all moderate/severe TBI patients (assume concurrent c-spine injury until cleared)
- CT angiography head/neck — if concern for vascular injury (skull base fracture, cervical spine fracture, expanding hematoma, neurological deficit unexplained by CT)
- Repeat CT head at 6-8 hours — if neurological worsening, anticoagulated patients, or initial CT concerning
- MRI brain — not emergent; useful for DAI, posterior fossa lesions, prognostication in subacute phase

**Labs:**
- POC glucose — exclude hypoglycemia
- CBC — baseline, platelet count
- BMP — electrolytes, glucose, renal function
- Coagulation panel: INR, PTT — guide reversal
- Type and screen — anticipate surgical intervention or transfusion
- Ethanol level — common confounder
- Lactate — systemic injury marker
- Troponin — neurogenic cardiac injury (sympathetic surge)
- Anti-Xa level — if on DOAC and timing of last dose unclear

**Monitoring:**
- ICP monitoring — all patients with severe TBI (GCS 3-8) and abnormal CT (Brain Trauma Foundation). Target ICP <22 mmHg and CPP 60-70 mmHg.
- Continuous EEG — if concern for nonconvulsive seizures (unexplained decline in GCS)

## Treatment

**Neuroprotective Targets (prevent secondary brain injury):**
- SpO2 >94%, PaO2 >60 mmHg — avoid hypoxia
- SBP >100 mmHg — avoid hypotension
- PaCO2 35-45 mmHg — normocapnia (hyperventilation only as acute bridge)
- Glucose 80-180 mg/dL — avoid hyper/hypoglycemia
- Temperature 36-37.5°C — fever worsens secondary injury
- Sodium 135-145 mEq/L (higher if using hypertonic saline for ICP)
- Hemoglobin >7 g/dL (transfuse if below)
- Seizure prophylaxis: levetiracetam 1000 mg IV q12h or phenytoin 20 mg/kg IV loading for 7 days (prevents early post-traumatic seizures; no benefit beyond 7 days)

**ICP Management (Stepwise):**
1. Head of bed 30 degrees, head midline, ensure no venous outflow obstruction
2. Sedation: propofol 20-75 mcg/kg/min or midazolam 0.05-0.2 mg/kg/hr + fentanyl 1-2 mcg/kg/hr
3. CSF drainage via EVD (if placed)
4. Osmotic therapy: mannitol 0.25-1 g/kg IV q6h (hold if serum osm >320) OR hypertonic saline 3% 250 mL IV bolus (can repeat) or 23.4% 30 mL via central line
5. Brief hyperventilation to PaCO2 30-35 mmHg (temporary bridge — causes cerebral vasoconstriction and potential ischemia if prolonged)
6. Decompressive craniectomy — neurosurgical decision for refractory ICP elevation

**Anticoagulant Reversal:**
- Warfarin: 4-factor PCC 25-50 units/kg IV (onset 10-15 min) + vitamin K 10 mg IV (onset 6-8 hours). Target INR <1.5 within 30 minutes.
- Dabigatran: idarucizumab (Praxbind) 5g IV
- Rivaroxaban/apixaban: andexanet alfa 400-800 mg IV bolus then infusion, or 4-factor PCC 50 units/kg IV if andexanet unavailable
- Heparin: protamine 1 mg per 100 units heparin given in last 2-3 hours (max 50 mg)
- Enoxaparin: protamine 1 mg per 1 mg enoxaparin given in last 8 hours (60-80% reversal)

**Surgical Indications:**
- Epidural hematoma: >30 mL, >15 mm thickness, or >5 mm midline shift
- Subdural hematoma: >10 mm thickness, >5 mm midline shift, GCS drop >=2 points
- Depressed skull fracture: depression greater than skull thickness, open fracture, neurological deficit
- Posterior fossa hemorrhage: any significant hemorrhage (limited space, rapid brainstem compression)

## Disposition

**Operating Room (emergent):**
- Epidural hematoma with neurological deterioration (minutes matter)
- Subdural hematoma meeting surgical criteria
- Depressed skull fracture with mass effect
- Posterior fossa hemorrhage

**Neurosurgical ICU:**
- All severe TBI (GCS 3-8)
- ICP monitoring required
- Post-craniotomy
- Anticoagulant-associated intracranial hemorrhage
- Progressive hemorrhage on repeat imaging

**Stepdown/Telemetry:**
- Moderate TBI (GCS 9-12) with stable CT
- Mild TBI on anticoagulation requiring serial neurological exams and repeat CT

**Discharge (mild TBI, GCS 15):**
- Normal or clinically insignificant CT
- Neurologically intact
- Reliable observer at home for 24 hours
- Return precautions: worsening headache, vomiting, confusion, focal weakness, seizure
- No anticoagulation, or anticoagulation with normal repeat CT at 24 hours

## Pitfalls

1. **Attributing altered mental status to intoxication.** Alcohol does not protect against TBI. Intoxicated patients with any mechanism of head injury require CT imaging. "Drunk" patients die from missed intracranial hemorrhage.

2. **Allowing hypotension in TBI.** A single episode of SBP <90 doubles mortality. In polytrauma, permissive hypotension (standard for hemorrhagic shock) does NOT apply to the TBI patient. Target SBP >100 mmHg.

3. **Prolonged hyperventilation for ICP control.** Hyperventilation causes cerebral vasoconstriction and ischemia. Use ONLY as a temporary bridge (minutes) to osmotic therapy or surgery. Target PaCO2 30-35 only acutely, then normalize to 35-45.

4. **Not reversing anticoagulation emergently.** Anticoagulated patients with intracranial hemorrhage expand their hemorrhage rapidly. PCC reverses warfarin within minutes. Do NOT wait for repeat INR before giving PCC. Reversal must happen in parallel with CT.

5. **Missing posterior fossa hemorrhage.** The posterior fossa is a small, non-compliant space. Even small hemorrhages cause rapid brainstem compression, obstructive hydrocephalus, and death. These patients need neurosurgical evaluation regardless of hemorrhage size.

6. **Failing to repeat CT for neurological change.** A stable initial CT does not guarantee stability. Any GCS decline, new focal deficit, or pupil asymmetry warrants immediate repeat CT. Contusions bloom; subdurals expand.

7. **Skipping seizure prophylaxis.** Early post-traumatic seizures (within 7 days) worsen secondary brain injury. Levetiracetam 1000 mg IV q12h for 7 days is standard for severe TBI. Phenytoin is an alternative but has more drug interactions and side effects.

8. **Treating fever passively.** Hyperthermia worsens secondary brain injury in TBI. Fever >38°C requires aggressive treatment: acetaminophen 1000 mg IV/PO, active cooling measures, and investigation for infectious source (ventilator-associated pneumonia, UTI, line infection).

9. **Not imaging the cervical spine.** Up to 10% of severe TBI patients have concurrent cervical spine fractures. CT c-spine is mandatory. MRI for ligamentous injury if CT is negative but exam is unreliable.

10. **Platelet transfusion for antiplatelet-associated ICH.** The PATCH trial (Lancet 2016) showed platelet transfusion WORSENED outcomes in antiplatelet-associated ICH. Do not reflexively transfuse platelets.
