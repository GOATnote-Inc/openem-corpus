---
id: subdural-hematoma
condition: Subdural Hematoma
aliases: [SDH, subdural hemorrhage, acute subdural hematoma, chronic subdural hematoma, ASDH, CSDH]
icd10: [S06.5X0A, S06.5X1A, S06.5X2A, S06.5X3A, S06.5X4A, S06.5X5A, S06.5X9A]
esi: 1
time_to_harm: "< 2 hours for acute SDH with herniation; days to weeks for chronic SDH"
mortality_if_delayed: "50-90% for acute SDH requiring surgery; up to 100% with uncal herniation"
category: traumatic
track: tier1
sources:
  - type: guideline
    ref: "Bullock MR et al. Surgical Management of Acute Subdural Hematomas. Neurosurgery. 2006;58(3 Suppl):S16-S24"
    pmid: "16710968"
  - type: guideline
    ref: "Brain Trauma Foundation. Guidelines for the Management of Severe Traumatic Brain Injury, 4th Edition. Neurosurgery. 2017;80(1):6-15"
    pmid: "27654000"
  - type: review
    ref: "Shin DS, Hwang SC. Neurocritical Management of Traumatic Acute Subdural Hematomas. Korean J Neurotrauma. 2020;16(2):113-125"
    pmid: "33163419"
  - type: review
    ref: "Almenawer SA et al. Chronic Subdural Hematoma Management: A Systematic Review and Meta-Analysis of 34,829 Patients. Ann Surg. 2014;259(3):449-457"
    pmid: "24096761"
  - type: guideline
    ref: "Greenberg SM et al. 2022 Guideline for the Management of Patients With Spontaneous Intracerebral Hemorrhage: AHA/ASA Guideline. Stroke. 2022;53(7):e282-e361"
    pmid: "35579034"
last_updated: "2026-02-19"
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
  outlier_detection_flag: null
  guideline_version_reference: null
  provenance_links: []
---

## Recognition

**Definition:** Hemorrhage between the dura mater and arachnoid membrane, caused by tearing of bridging veins (or less commonly cortical arteries) that traverse the subdural space. The most common traumatic intracranial hemorrhage.

**Classification by Timing:**
- **Acute SDH:** < 3 days from injury. Hyperdense (bright white) on CT. Highest mortality.
- **Subacute SDH:** 3-21 days. Isodense to brain on CT (easily missed).
- **Chronic SDH:** > 21 days. Hypodense (dark) on CT. Encapsulated with neomembranes.
- **Mixed-density SDH:** Rebleed into chronic collection. Heterogeneous on CT.

**Epidemiology:**
- Most common traumatic intracranial hemorrhage (up to 25% of severe TBI)
- Acute SDH: peak incidence in young adults (trauma) and elderly (falls)
- Chronic SDH: incidence 1-5.3 per 100,000/year; increases to 58 per 100,000/year in patients > 70 years
- Male:female 3:1
- Mortality: acute SDH 40-60% overall, 90% in comatose patients with delayed surgery

**Pathophysiology:**
- **Bridging veins** span from cortical surface to dural venous sinuses; acceleration-deceleration forces shear them
- Blood accumulates in the subdural space, which is a potential space with no anatomic barriers — SDH spreads diffusely over the convexity, crossing suture lines (unlike EDH)
- Acute SDH is frequently associated with underlying parenchymal injury (contusion, diffuse axonal injury), which drives the high mortality independent of the hematoma itself
- Chronic SDH forms neomembranes with fragile capillaries prone to recurrent microhemorrhage, causing gradual expansion

**High-Risk Populations:**
- Elderly patients (brain atrophy stretches bridging veins, increasing vulnerability to trivial trauma)
- Patients on anticoagulants (warfarin, DOACs) or antiplatelet agents
- Chronic alcoholics (brain atrophy, coagulopathy, frequent falls)
- Patients with CSF shunts (low intracranial pressure pulls brain away from dura)
- Patients with coagulopathies (hepatic disease, thrombocytopenia)

**Presentation — Acute SDH:**
- History of significant head trauma (MVC, fall, assault)
- Rapid onset altered mental status, often no lucid interval (unlike EDH)
- Headache, vomiting, progressive obtundation
- Ipsilateral fixed dilated pupil (uncal herniation — CN III compression)
- Contralateral hemiparesis (or ipsilateral from Kernohan notch — false localizing sign)
- Cushing response (hypertension, bradycardia, irregular respirations) — late sign of herniation
- Seizures
- GCS decline on serial exams

**Presentation — Chronic SDH:**
- Often trivial or no recalled trauma (especially elderly)
- Insidious onset over weeks: headache, cognitive decline, personality change, gait instability
- Fluctuating level of consciousness ("waxing and waning")
- Focal weakness, speech difficulty — can mimic stroke or dementia
- Falls (both cause and consequence)
- Papilledema (if large chronic collection)

**Exam Findings:**
- Scalp hematoma, laceration (may be absent in chronic SDH)
- Anisocoria (ipsilateral mydriasis in acute SDH with herniation)
- Focal motor deficits (hemiparesis, pronator drift)
- Decreased GCS
- Gait ataxia, cognitive impairment (chronic SDH)

## Critical Actions

1. **Stabilize airway** — intubate for GCS <= 8 using rapid sequence intubation. Avoid hypoxia (SpO2 < 90%) and hypotension (SBP < 90 mmHg) — both independently double mortality in TBI.
2. **Non-contrast CT head immediately** — any head trauma patient with altered mental status, GCS < 15, focal deficits, anticoagulant use, or age > 65. CT shows crescent-shaped collection over convexity.
3. **Measure midline shift** — shift > 5 mm or clot thickness > 10 mm = surgical emergency regardless of GCS.
4. **Reverse anticoagulation immediately** — do not wait for lab confirmation of supratherapeutic INR:
   - **Warfarin:** 4-factor PCC (Kcentra) 25-50 IU/kg IV + vitamin K 10 mg IV over 10 minutes
   - **Dabigatran:** Idarucizumab (Praxbind) 5 g IV (given as two 2.5 g boluses)
   - **Rivaroxaban/apixaban:** Andexanet alfa per dosing protocol, OR 4-factor PCC 50 IU/kg IV if andexanet unavailable
   - **Antiplatelet agents:** Platelet transfusion 1 apheresis unit (evidence debated; give if surgical evacuation planned)
   - **Thrombocytopenia:** Platelet transfusion to target > 100,000/mcL for surgical candidates
5. **Emergent neurosurgical consultation** — call at time of CT diagnosis, not after results return. Time to surgery directly impacts survival.
6. **ICP management while awaiting OR:**
   - Elevate head of bed to 30 degrees, midline head position
   - Mannitol 1 g/kg IV bolus (20% solution) for signs of herniation
   - OR hypertonic saline 23.4% 30 mL IV over 10-20 minutes via central line
   - OR hypertonic saline 3% 250 mL IV bolus via peripheral line (repeat once if needed)
7. **Seizure prophylaxis:** Levetiracetam 1,000-1,500 mg IV loading dose or fosphenytoin 20 mg PE/kg IV. Early seizures occur in 10-25% of acute SDH.
8. **Avoid secondary brain injury:** Target SBP > 100 mmHg (age > 49) or > 110 mmHg (age 15-49) per BTF guidelines. Maintain SpO2 > 94%, normothermia, normoglycemia.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Epidural hematoma (EDH) | Biconvex (lens-shaped) hyperdensity, does NOT cross suture lines. Arterial source (middle meningeal artery). Lucid interval classic. Usually younger patients with temporal bone fracture. |
| Subarachnoid hemorrhage (traumatic) | Blood in sulci and cisterns, not forming a discrete extraaxial collection. Often accompanies SDH/contusions in trauma. |
| Intracerebral hemorrhage / contusion | Intraparenchymal hyperdensity, often frontal and temporal poles (coup-contrecoup). No extraaxial collection. |
| Subdural hygroma | Crescent-shaped fluid isodense to CSF (not blood). Post-traumatic, usually benign. Can coexist with or evolve into chronic SDH. |
| Stroke (ischemic or hemorrhagic) | No trauma history (unless fall from stroke). Vascular territory distribution. CT may show early ischemic changes or spontaneous parenchymal hemorrhage. |
| Dementia / normal pressure hydrocephalus | Chronic SDH mimics these. Triad of gait instability, cognitive decline, urinary incontinence in NPH. CT distinguishes: SDH shows extraaxial collection; NPH shows ventriculomegaly out of proportion to sulcal atrophy. |
| Brain metastases / mass lesion | Ring-enhancing lesions on contrast CT/MRI, no acute trauma. Subacute presentation with progressive deficits. |

## Workup

**Imaging:**
- **Non-contrast CT head** — diagnostic study of choice. Findings by phase:
  - **Acute (< 3 days):** Crescent-shaped hyperdensity (60-80 HU) over convexity, crossing suture lines. Conforms to brain surface. Most common location: frontotemporoparietal convexity.
  - **Subacute (3-21 days):** Isodense to brain parenchyma — EASILY MISSED. Look for effaced sulci, compressed ventricle, or subtle midline shift as indirect signs. MRI superior for isodense SDH.
  - **Chronic (> 21 days):** Hypodense (similar to CSF density), often with enhancing neomembranes on contrast.
  - **Mixed density:** Acute-on-chronic rebleed. Layering or heterogeneous density within the collection.
  - **Measure:** Maximal clot thickness (mm), midline shift at septum pellucidum (mm)
  - **Bilateral SDH** (15-25%): Midline shift may be absent despite large bilateral collections. Look for compressed ventricles and effaced sulci bilaterally.
- **CT angiography** — if concern for vascular injury, underlying aneurysm, or venous sinus thrombosis
- **MRI** — superior for subacute/isodense SDH, small convexity SDH, posterior fossa SDH, and assessing underlying parenchymal injury. Not required emergently for most cases.

**Labs:**
- CBC with platelet count
- PT/INR, PTT, fibrinogen
- BMP (sodium for osmotic therapy monitoring)
- Type and screen / crossmatch (anticipate OR need)
- Blood alcohol level, urine toxicology (confounders of neurological exam)
- Anti-Xa level if on DOAC (if available and will not delay treatment)
- Blood glucose (exclude hypoglycemia as cause of altered mental status)

## Treatment

### Acute SDH — Surgical Management

**Indications for surgical evacuation (Bullock et al. 2006):**
- Clot thickness > 10 mm
- Midline shift > 5 mm
- GCS decline of >= 2 points from time of injury to hospital
- ICP > 20 mmHg
- Any patient with GCS < 9 and clot thickness > 10 mm or midline shift > 5 mm — operate regardless

**Procedure:**
- Craniotomy with hematoma evacuation is the standard approach
- Decompressive craniectomy (bone flap removal) when significant brain swelling is anticipated or present
- Burr holes are NOT adequate for acute SDH (clot is organized/semisolid, not easily drained through a burr hole)

**Timing:** Operate within 4 hours of injury when possible. Each hour of delay increases mortality. Mortality is 40-60% even with surgery due to concomitant parenchymal injury.

**Non-operative management (selected cases):**
- Clot < 10 mm AND midline shift < 5 mm AND GCS stable
- Requires: ICU admission, serial neuro exams q1h, repeat CT at 6-8 hours and with any neurological change
- ICP monitoring if GCS < 9 (even if non-operative)

### Chronic SDH — Surgical Management

**Indications for surgery:**
- Symptomatic (headache, cognitive decline, focal deficit, gait instability)
- Clot thickness > 10 mm or midline shift > 5 mm
- Neurological deterioration

**Procedures:**
- **Burr hole drainage** with closed-system subdural drain — first-line for most chronic SDH. One or two burr holes with irrigation and drain placement for 24-48 hours. Recurrence rate 10-20%.
- **Twist-drill craniostomy** — bedside procedure for patients unable to tolerate general anesthesia. Smaller opening, drain left in place.
- **Craniotomy** — for organized/septated collections, recurrent SDH after burr holes, or membranes preventing adequate drainage.
- **Middle meningeal artery embolization** — emerging adjunct (randomized trial evidence supports reduction in recurrence and reoperation). May be used as standalone or combined with surgical drainage.

### Medical Management (ICP Reduction While Awaiting OR)

| Intervention | Dose / Details |
|-------------|---------------|
| **Head of bed elevation** | 30 degrees, midline head position, loosen cervical collar if safe |
| **Mannitol** | 1 g/kg IV bolus (20% solution). Can repeat 0.25-0.5 g/kg q4-6h. Hold if serum osmolality > 320 mOsm/L or SBP < 90 mmHg. |
| **Hypertonic saline 23.4%** | 30 mL IV over 10-20 min via central line. Preferred over mannitol if hypotensive. |
| **Hypertonic saline 3%** | 250 mL IV bolus via peripheral line. Can repeat once. |
| **Hyperventilation** | Target PaCO2 30-35 mmHg ONLY as temporizing bridge to OR (< 30 minutes). Sustained hyperventilation causes cerebral ischemia. |
| **Seizure prophylaxis** | Levetiracetam 1,000-1,500 mg IV or fosphenytoin 20 mg PE/kg IV |
| **Tranexamic acid** | 1 g IV over 10 min (consider within 3 hours of injury per CRASH-2/CRASH-3 data; evidence specific to SDH is limited) |

### Anticoagulant Reversal (Priority in All Anticoagulated Patients)

| Agent | Reversal |
|-------|---------|
| **Warfarin** | 4-factor PCC 25-50 IU/kg IV (reverses in minutes) + vitamin K 10 mg IV over 10 min (sustained reversal). Do NOT use FFP alone (too slow, volume overload). Target INR < 1.4. |
| **Dabigatran** | Idarucizumab (Praxbind) 5 g IV as two 2.5 g boluses. If unavailable: 4-factor PCC 50 IU/kg IV. |
| **Rivaroxaban / Apixaban** | Andexanet alfa (low-dose: 400 mg bolus then 4 mg/min x 120 min; high-dose: 800 mg bolus then 8 mg/min x 120 min based on agent/timing). If unavailable: 4-factor PCC 50 IU/kg IV. |
| **Heparin (unfractionated)** | Protamine 1 mg per 100 units heparin given in prior 2-3 hours. Max 50 mg. |
| **Enoxaparin** | Protamine 1 mg per 1 mg enoxaparin (if < 8 hours since dose). Partial reversal only (~60%). |
| **Antiplatelet agents** | Platelet transfusion 1 apheresis unit if surgery planned. Desmopressin (DDAVP) 0.3 mcg/kg IV — improves platelet function. |

## Disposition

**Operating Room (emergent):**
- All acute SDH meeting surgical criteria (thickness > 10 mm, midline shift > 5 mm, GCS decline)
- Acute SDH with signs of herniation (anisocoria, posturing, Cushing response)

**Neurosurgical ICU:**
- All postoperative SDH patients
- Non-operative acute SDH for serial monitoring (q1h neuro checks, repeat CT at 6-8 hours)
- All acute SDH patients with GCS < 9 (ICP monitoring)

**Neurosurgical floor / step-down:**
- Chronic SDH post-burr hole drainage (typically 24-48 hours with drain, then repeat CT after drain removal)
- Subacute SDH with stable exam, small collection

**Transfer:**
- If no neurosurgery available: stabilize, initiate ICP-lowering measures and anticoagulant reversal, arrange emergent transfer. Do NOT wait for deterioration — transfer at time of CT diagnosis. Mannitol, hypertonic saline, and seizure prophylaxis are bridging measures during transport.

**Discharge:**
- Acute SDH is NOT an ED discharge diagnosis. All patients with acute or subacute SDH on CT require admission and neurosurgical evaluation.
- Small chronic SDH in neurologically intact patients may be managed with close outpatient neurosurgery follow-up after initial evaluation, but this is a neurosurgical decision, not an ED disposition.

## Pitfalls

1. **Missing isodense subacute SDH on CT.** Between days 3 and 21, the hematoma becomes isodense to brain parenchyma and is nearly invisible on CT. Indirect signs include effaced sulci, compressed ipsilateral ventricle, and subtle midline shift. If clinical suspicion is high and CT appears "normal," obtain MRI. Bilateral isodense SDH can produce symmetric compression with no midline shift at all.

2. **Attributing chronic SDH symptoms to dementia or stroke.** Elderly patients with chronic SDH present with cognitive decline, gait instability, and fluctuating consciousness — identical to dementia or stroke. Every elderly patient with new or worsening cognitive decline, especially on anticoagulants, needs CT to exclude chronic SDH. This is a surgically curable cause of "dementia."

3. **Delayed anticoagulant reversal.** Every minute of continued coagulopathy allows hematoma expansion. Reverse at time of CT diagnosis, not after neurosurgical consultation. Use 4-factor PCC for warfarin (works in minutes, unlike FFP which takes hours). Know your DOAC reversal agents. Waiting for INR results to decide whether to reverse wastes critical time.

4. **Assuming bilateral SDH has no mass effect because there is no midline shift.** Bilateral SDH (15-25% of cases) produces symmetric compression. Midline shift is absent, but both hemispheres are compressed. Look for bilateral sulcal effacement, bilateral ventricular compression, and low-lying cerebellar tonsils. These patients can be severely impaired despite a "reassuring" midline.

5. **Using hyperventilation as sustained ICP management.** Hyperventilation (PaCO2 < 35 mmHg) reduces ICP via cerebral vasoconstriction but simultaneously reduces cerebral blood flow, risking ischemia in already-injured brain. Use only as a bridge to OR for active herniation, for no more than 15-30 minutes. Sustained hyperventilation worsens outcomes.

6. **Treating chronic SDH with observation when the patient is symptomatic.** Chronic SDH with focal deficits, cognitive decline, or gait instability warrants surgical drainage (burr hole). Observation alone allows continued neurological decline. Symptomatic chronic SDH is a surgical condition. Even "mild" symptoms in elderly patients (falls, confusion) warrant intervention when imaging shows significant collection.

7. **Failing to check anticoagulant/antiplatelet status in every head-injured elderly patient.** Elderly patients on anticoagulants can develop significant SDH from trivial trauma (or no recalled trauma). A normal initial CT does not exclude delayed hemorrhage. Anticoagulated head trauma patients with negative initial CT should have repeat CT at 6-24 hours or return precautions with low threshold for reimaging.

8. **Not recognizing acute-on-chronic SDH.** Mixed-density SDH (hyperdense layered within hypodense) indicates acute rebleed into a chronic collection. This changes management: the patient now has an acute surgical emergency, not a stable chronic SDH. Mixed density always warrants emergent neurosurgical evaluation and consideration of craniotomy rather than burr holes alone.

9. **Permissive hypotension protocols in polytrauma with concomitant SDH.** Permissive hypotension (targeting SBP 80-90 mmHg) is standard in hemorrhagic shock from torso trauma, but hypotension (SBP < 90 mmHg) doubles TBI mortality. When TBI coexists with hemorrhagic shock, target SBP > 100 mmHg. The brain cannot tolerate the same hypoperfusion that the body can. This requires explicit communication between trauma and neurosurgery teams.

10. **Discharging the anticoagulated patient with "negative CT" after minor head injury.** Delayed SDH can develop hours after initial negative imaging in anticoagulated patients. These patients require either observation with repeat CT at 6-24 hours or reliable return precautions with explicit instructions to return for headache, confusion, weakness, or drowsiness. Document the anticoagulant, dose, timing, and plan clearly.
