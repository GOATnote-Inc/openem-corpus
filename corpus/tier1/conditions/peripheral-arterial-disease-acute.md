---
id: peripheral-arterial-disease-acute
condition: Acute Peripheral Arterial Occlusion
aliases: [acute limb ischemia, ALI, acute arterial occlusion, acute peripheral arterial ischemia, thromboembolism of extremity]
icd10: [I74.3, I74.4, I74.5]
esi: 2
time_to_harm:
  irreversible_injury: "< 6 hours"
  death: "< 24 hours (from reperfusion injury/complications)"
  optimal_intervention_window: "< 6 hours"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "2016 AHA/ACC Guideline on the Management of Patients With Lower Extremity Peripheral Artery Disease. Circulation. 2017;135(12):e686-e725."
  - type: guideline
    ref: "2019 ESC/ESVS Guidelines on the Diagnosis and Treatment of Peripheral Arterial Diseases. Eur Heart J. 2020;41(2):111-112."
  - type: review
    ref: "Olinic DM, et al. Acute Limb Ischemia: An Update on Diagnosis and Management. J Clin Med. 2019;8(8):1215."
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
# Acute Peripheral Arterial Occlusion

## Recognition

**Six Ps of acute limb ischemia:**
- **Pain** — sudden onset, severe, distal to occlusion
- **Pallor** — white/mottled skin
- **Pulselessness** — absent distal pulses
- **Paresthesia** — numbness, tingling (early nerve ischemia)
- **Paralysis** — motor deficit (late, indicates threatened limb)
- **Poikilothermia** — cool extremity compared to contralateral

**Rutherford classification:**
- **Category I (Viable):** No sensory/motor deficit, audible Doppler signals. Not immediately threatened.
- **Category IIa (Marginally threatened):** Minimal sensory loss (toes), no motor deficit. Salvageable with prompt treatment.
- **Category IIb (Immediately threatened):** Sensory loss beyond toes, mild-moderate motor deficit, inaudible arterial Doppler. Requires immediate revascularization.
- **Category III (Irreversible):** Profound sensory/motor loss, muscle rigor, inaudible Doppler. Amputation necessary.

**Etiology:**
- Embolism (most common): atrial fibrillation, LV thrombus post-MI, prosthetic valve, paradoxical embolism
- Thrombosis in situ: atherosclerotic plaque rupture, aneurysm thrombosis, hypercoagulable state
- Trauma: arterial injury, compartment syndrome
- Aortic dissection with malperfusion

## Critical Actions

| Action | Target |
|---|---|
| Vascular assessment (pulses, Doppler) | < 10 minutes |
| Systemic anticoagulation | < 15 minutes |
| Vascular surgery consultation | < 30 minutes |
| Revascularization (Cat IIb) | < 6 hours |

1. **Immediate systemic anticoagulation** — heparin 80 units/kg IV bolus, then 18 units/kg/hr (prevents clot propagation)
2. **Vascular surgery consultation STAT** — required for all categories
3. **Keep limb in dependent position** (slightly below heart level) — maximizes perfusion pressure
4. **Avoid warming the limb externally** — increases metabolic demand beyond ischemic supply
5. **Pain management** — morphine 2-4 mg IV q5-15min or fentanyl 25-100 mcg IV
6. **IV fluid resuscitation** — prepare for reperfusion injury (hyperkalemia, myoglobinuria, acidosis)
7. **Type and crossmatch** — anticipate surgical blood loss
8. **Category IIb/III: emergent revascularization** — do not delay for additional imaging

## Differential Diagnosis

- **Deep vein thrombosis** — swelling, warmth, preserved pulses (venous vs arterial)
- **Acute compartment syndrome** — tense compartment, pain with passive stretch, may have intact pulses early
- **Aortic dissection with malperfusion** — bilateral lower extremity, back pain, BP differential
- **Phlegmasia cerulea dolens** — massive DVT causing arterial compromise; entire limb swollen and cyanotic
- **Cholesterol embolization (blue toe syndrome)** — localized digital ischemia with preserved pulses post-catheterization
- **Raynaud phenomenon/vasospasm** — episodic, bilateral, reversible

## Workup

- **Ankle-brachial index (ABI):** < 0.4 in affected limb confirms severe ischemia; absent in complete occlusion
- **Handheld Doppler:** Assess arterial and venous signals at ankle. Inaudible arterial signal = threatened limb.
- **CT angiography:** Preferred imaging for stable patients (Category I, IIa) — identifies occlusion site, etiology (embolus vs thrombosis), and guides intervention. Do NOT delay revascularization for imaging in Category IIb.
- **Labs:** CBC, BMP (K+ — anticipate reperfusion hyperkalemia), lactate, CK/myoglobin (rhabdomyolysis), coagulation studies, type and crossmatch
- **ECG:** Assess for atrial fibrillation (embolic source)
- **Echocardiography:** Identify cardiac source of embolism (LV thrombus, valvular pathology, PFO)
- **Hypercoagulability workup:** If no obvious embolic source, especially in young patients

## Treatment

### Category I (Viable) — Urgent Revascularization (6-24 hours)
- Systemic anticoagulation with heparin
- CTA to plan intervention
- Catheter-directed thrombolysis with tPA (0.5-1 mg/hr infusion via catheter) over 12-24 hours
- Serial angiographic assessment during lysis

### Category IIa (Marginally Threatened) — Emergent Revascularization
- Options: catheter-directed thrombolysis OR surgical embolectomy/thrombectomy
- Thrombolysis preferred for thrombosis in situ (native vessel or graft)
- Surgery preferred for large embolus with clear-cut embolic etiology

### Category IIb (Immediately Threatened) — Immediate Surgery
- **Surgical embolectomy** via Fogarty balloon catheter — first-line
- Femoral cutdown, arteriotomy, proximal/distal thrombectomy
- On-table angiography to confirm complete revascularization
- Consider fasciotomy prophylactically if ischemia > 4-6 hours
- Bypass grafting if underlying stenosis/thrombosis

### Category III (Irreversible) — Primary Amputation
- Revascularization is contraindicated (reperfusion of necrotic tissue → fatal hyperkalemia, myoglobin-induced renal failure, DIC)
- Urgent amputation to prevent systemic toxicity

### Reperfusion Injury Management
- Monitor for compartment syndrome post-revascularization — maintain low threshold for fasciotomy
- Aggressive IV fluids (NS 200-500 mL/hr) to prevent myoglobin-induced AKI
- Monitor K+ q2h for 12 hours post-revascularization — treat hyperkalemia aggressively
- Sodium bicarbonate 150 mEq/L in D5W at 150 mL/hr to alkalinize urine (prevents myoglobin precipitation)
- Monitor for metabolic acidosis, DIC

## Disposition

- **ICU admission:** Post-revascularization (all categories), compartment syndrome, reperfusion injury
- **Vascular surgery admission:** Category I on heparin awaiting intervention
- **Transfer:** Facilities without vascular surgery capability must transfer immediately (do not delay for imaging)
- **Post-discharge:** Anticoagulation, identify/treat embolic source, surveillance imaging

## Pitfalls

1. **Delaying anticoagulation while waiting for vascular surgery or imaging.** Heparin should be given immediately upon diagnosis of ALI, regardless of planned intervention. Clot propagation during delay converts viable tissue to nonviable tissue. There is no contraindication to heparin in ALI (it is standard of care even preoperatively).

2. **Attempting revascularization of Category III (irreversible) ischemia.** Muscle rigor, mottled fixed skin, and absent sensation/motor function indicate nonviable tissue. Revascularization releases lethal quantities of potassium, myoglobin, and lactate, causing cardiac arrest, renal failure, and DIC. Primary amputation is the correct treatment.

3. **Failing to perform compartment pressure checks or prophylactic fasciotomy after revascularization.** Reperfusion edema causes compartment syndrome in a significant proportion of patients, especially those with > 4-6 hours of ischemia. Delay in fasciotomy results in permanent nerve and muscle damage.

4. **Missing atrial fibrillation as the embolic source.** Approximately 80% of peripheral arterial emboli originate from the heart. An ECG should be obtained in every ALI patient. New or undiagnosed AF requires anticoagulation to prevent recurrent embolism.

5. **Confusing venous and arterial pathology.** A swollen, blue, painful leg is more likely phlegmasia cerulea dolens (venous) than ALI (arterial). Arterial ischemia causes a pale, cool, pulseless limb. Treatment is fundamentally different.
