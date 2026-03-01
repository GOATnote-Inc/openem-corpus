---
id: fat-embolism-syndrome
condition: Fat Embolism Syndrome
aliases: [FES, fat embolism, post-fracture fat embolism, marrow embolism]
icd10: [T79.1XXA]
esi: 1
time_to_harm:
  irreversible_injury: "< 24 hours"
  death: "< 48 hours without respiratory support"
  optimal_intervention_window: "< 6 hours from symptom onset"
mortality_if_delayed: "5-15% overall; up to 36% in fulminant form"
category: traumatic
track: tier1
sources:
  - type: pubmed
    ref: "Gurd AR, Wilson RI. The fat embolism syndrome. J Bone Joint Surg Br. 1974;56B(3):408-416."
    pmid: "4547466"
  - type: pubmed
    ref: "Mellor A, Soni N. Fat embolism. Anaesthesia. 2001;56(2):145-154."
    pmid: "11167474"
  - type: review
    ref: "Akhtar S. Fat embolism. Anesthesiol Clin. 2009;27(3):533-550."
    pmid: "19825491"
  - type: review
    ref: "Gupta A, Reilly CS. Fat embolism. Continuing Education in Anaesthesia Critical Care & Pain. 2007;7(5):148-151."
    doi: "10.1093/bjaceaccp/mkm027"
  - type: pubmed
    ref: "Kosova E, Bergmark B, Piazza G. Fat embolism syndrome. Circulation. 2015;131(3):317-320."
    pmid: "25601951"
confusion_pairs:
  - condition: pulmonary-embolism
    differentiators:
      - "FES: petechial rash (axillae, conjunctivae, chest) — pathognomonic; absent in PE"
      - "FES: onset 24-72 hours after long bone fracture or orthopedic surgery; PE can occur at any time"
      - "FES: neurological changes (confusion, agitation, coma) prominent early; PE typically presents with dyspnea and pleuritic chest pain without encephalopathy"
      - "FES: no DVT source on compression ultrasound; PE often has proximal DVT"
      - "CTA: FES shows diffuse ground-glass opacities without filling defects; PE shows intraluminal filling defect"
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
# Fat Embolism Syndrome

## Recognition

**Definition:** Systemic inflammatory response caused by fat globules entering the venous circulation and lodging in pulmonary and systemic capillary beds. Distinguished from fat embolism (radiographic finding in up to 90% of long bone fractures) by the presence of clinical syndrome.

**Classic triad (present in <33% of cases):**
1. **Hypoxemia/respiratory distress** — earliest and most common (95%); tachypnea, dyspnea, progressing to ARDS
2. **Neurological changes** — second most common (60-80%); confusion, agitation, drowsiness, seizures, coma; out of proportion to hypoxemia
3. **Petechial rash** — pathognomonic but late (20-50%); non-palpable, non-blanching; axillae, conjunctivae, anterior chest, neck; appears 24-36 hours after onset; transient (resolves within 7 days)

**Onset:** 24-72 hours after inciting event (rarely as early as 12 hours). The latent period distinguishes FES from acute PE.

**Risk factors:**
- Long bone fractures (femur > tibia; bilateral > unilateral)
- Pelvic fractures
- Orthopedic surgery (intramedullary nailing, joint arthroplasty)
- Multiple fractures (incidence 5-10% with single long bone fracture, up to 33% with multiple)
- Delayed fracture fixation (>24 hours increases risk)
- Closed fractures (higher intramedullary pressure than open)

**Non-traumatic causes (rare):**
- Liposuction
- Bone marrow transplant
- Pancreatitis
- Sickle cell crisis (bone marrow necrosis)
- Parenteral lipid infusion
- Decompression sickness

**Gurd criteria (clinical diagnosis — no single definitive test):**

*Major criteria (need 1 major + 4 minor):*
- Petechial rash
- Respiratory insufficiency (PaO2 <60 mmHg on room air)
- Cerebral involvement (unrelated to head injury or other cause)

*Minor criteria:*
- Tachycardia >120 bpm
- Fever >38.5C
- Retinal fat emboli (on fundoscopy — fat globules in retinal vessels)
- Renal insufficiency (oliguria, lipiduria, fat globules in urine)
- Acute thrombocytopenia (drop >50% from baseline)
- Acute anemia (hemoglobin drop >20% from baseline)
- Elevated ESR >71 mm/hr
- Fat macroglobulinemia

**Schonfeld criteria (point-based, score >=5 diagnostic):**

| Finding | Points |
|---------|--------|
| Petechiae | 5 |
| CXR diffuse infiltrates | 4 |
| Hypoxemia (PaO2 <70 mmHg) | 3 |
| Fever >38C | 1 |
| Tachycardia >120 bpm | 1 |
| Confusion | 1 |

## Critical Actions

1. **Maintain a high index of suspicion in all long bone fracture patients developing respiratory distress, altered mental status, or petechiae 12-72 hours post-injury.** Diagnosis is clinical — no confirmatory test exists.
2. **Secure the airway early.** Fulminant FES progresses to ARDS requiring mechanical ventilation in 10-44% of cases. Intubate for GCS <8, PaO2 <60 mmHg on high-flow O2, or respiratory fatigue.
3. **Lung-protective ventilation.** Tidal volume 6 mL/kg ideal body weight, plateau pressure <30 cmH2O, titrate PEEP to oxygenation (ARDSNet protocol).
4. **Aggressive supportive care.** There is no specific pharmacologic treatment for FES. Management is supportive with focus on oxygenation and hemodynamic stability.
5. **Early fracture fixation.** Orthopedic consultation for definitive fixation within 24 hours reduces FES incidence (damage control orthopedics). Intramedullary reaming should use vented nails or unreamed techniques to reduce intramedullary pressure.
6. **Volume resuscitation.** Crystalloid (lactated Ringer's preferred) to maintain euvolemia. Hypovolemia worsens end-organ fat deposition. Target MAP >65 mmHg; use vasopressors (norepinephrine 0.1-0.5 mcg/kg/min) if fluid-refractory.
7. **Exclude PE.** CTA pulmonary angiogram to rule out thromboembolic disease — FES and PE have overlapping presentations.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Pulmonary embolism | CTA shows filling defect; no petechial rash; DVT on compression ultrasound; onset at any time (not 24-72h window); no neurological changes unless massive PE with hemodynamic collapse |
| ARDS (non-FES) | Multiple etiologies (sepsis, aspiration, transfusion); no petechial rash; no temporal relationship to fracture; diagnosis of exclusion |
| Traumatic brain injury | Direct head trauma on CT/MRI; no respiratory component unless concurrent lung injury; no petechial rash; TBI is acute (not delayed 24-72h) |
| Sepsis | Infectious source identifiable; positive cultures; procalcitonin elevated; no petechial rash pattern (petechiae in DIC are diffuse, not axillary/conjunctival predominant) |
| Diffuse alveolar hemorrhage | Hemoptysis; dropping hemoglobin; BAL increasingly bloody with serial aliquots; associated with vasculitis or anticoagulation |
| Transfusion-related acute lung injury | Within 6 hours of transfusion; bilateral infiltrates; no cardiac cause; anti-HLA antibodies |
| Air embolism | History of central line placement, surgery, or diving; sudden onset (not delayed); mill-wheel murmur; air on echo |

## Workup

**Bedside:**
- Pulse oximetry — continuous; desaturation is the earliest finding
- ABG — PaO2/FiO2 ratio (ARDS criteria: <300 mild, <200 moderate, <100 severe)
- Fundoscopy — retinal fat emboli (cotton-wool spots, perivascular hemorrhages, intravascular fat globules); present in 50% of cases; pathognomonic when present
- Skin survey — inspect axillae, conjunctivae, anterior chest, neck for petechiae q4-6h for 72 hours

**Labs:**
- CBC — thrombocytopenia (drop >50%), anemia (hemoglobin drop >20%); often develops 24-48h after onset
- CMP — renal function (acute kidney injury from fat deposition)
- Coagulation studies — DIC screen (fibrinogen, D-dimer, PT/INR); DIC occurs in severe cases
- Lipase — elevated in pancreatitis-associated FES
- Lactate — tissue hypoperfusion marker
- Urinalysis — fat globules in urine (lipiduria); sensitivity ~50%
- ESR — elevated (>71 mm/hr supports Gurd criteria); nonspecific

**Imaging:**
- **CXR:** Bilateral diffuse infiltrates ("snowstorm" pattern); develops 24-48 hours after symptom onset; indistinguishable from ARDS
- **CTA chest:** Rule out PE (filling defect absent in FES); may show ground-glass opacities
- **MRI brain:** Multiple punctate hyperintensities on T2/FLAIR and diffusion-weighted imaging (DWI) in a "starfield" pattern — white matter predominant; most sensitive imaging test for cerebral FES; obtain when neurological changes are disproportionate to hypoxemia
- **Echocardiography:** Right ventricular dilation and dysfunction from acute pulmonary hypertension; mobile echogenic material in right heart (fat); patent foramen ovale allowing paradoxical embolism to brain/skin

## Treatment

**Respiratory support:**
- Supplemental O2 to target SpO2 >92%
- High-flow nasal cannula (40-60 L/min) for moderate hypoxemia
- Intubation and mechanical ventilation for PaO2/FiO2 <150 or clinical deterioration
- ARDSNet lung-protective ventilation: TV 6 mL/kg IBW, plateau pressure <30 cmH2O, PEEP per FiO2/PEEP table, target SpO2 88-95%
- Prone positioning for PaO2/FiO2 <150 despite optimal PEEP (16h/day cycles)

**Hemodynamic support:**
- Lactated Ringer's 30 mL/kg initial bolus, then titrate to MAP >65 mmHg and UOP >0.5 mL/kg/hr
- Norepinephrine 0.1-0.5 mcg/kg/min for vasodilatory shock (first-line vasopressor)
- Dobutamine 2.5-10 mcg/kg/min for RV failure with low cardiac output (echo-guided)
- Avoid aggressive fluid loading if RV failure is present (worsens RV dilation)

**Neurological support:**
- Seizure management: levetiracetam 1500 mg IV load then 1000 mg IV q12h (first-line; does not impair coagulation) OR lorazepam 0.1 mg/kg IV (max 4 mg) for active seizures
- Avoid sedation that obscures neurological assessment when possible
- Serial GCS monitoring q2h

**Corticosteroids (prophylaxis — evidence is limited and conflicting):**
- Methylprednisolone 1.5 mg/kg IV q8h for 48 hours — some evidence supports prophylactic use in high-risk patients (bilateral femur fractures, multiple long bone fractures) to reduce FES incidence. NOT proven for treatment of established FES.
- Routine use not recommended by current guidelines

**DVT prophylaxis:**
- Enoxaparin 40 mg SC daily (start when hemostasis assured, typically 24-48h post-fixation)
- Mechanical prophylaxis (pneumatic compression devices) from admission

**Fracture management (prevention is the best treatment):**
- Early definitive fixation (<24 hours) of long bone fractures reduces FES incidence from ~22% to ~5%
- Damage control orthopedics in hemodynamically unstable patients: temporary external fixation, convert to definitive fixation when stable
- Intramedullary nailing: vented nails, unreamed technique, and lavage of medullary canal before reaming reduce fat embolization

## Disposition

**ICU admission (all symptomatic FES):**
- Mechanical ventilation requirement
- Hemodynamic instability
- Neurological compromise (GCS <13)
- PaO2/FiO2 <200

**Step-down/monitored bed:**
- Mild FES (hypoxemia responsive to nasal cannula, no neurological changes)
- Post-fixation observation in high-risk patients (bilateral femur fractures)
- Minimum 72 hours of monitoring — FES onset peaks at 24-72 hours

**No outpatient disposition.** All patients with suspected or confirmed FES require inpatient monitoring.

## Pitfalls

1. **Attributing altered mental status to head injury or opioids in a fracture patient.** Encephalopathy appearing 24-72 hours after long bone fracture is FES until proven otherwise. Perform fundoscopy (retinal fat emboli), MRI brain (starfield pattern), and assess for concurrent petechiae and hypoxemia before attributing confusion to other causes.

2. **Waiting for the classic triad to make the diagnosis.** The complete triad (hypoxemia + neuro changes + petechial rash) is present in <33% of cases. Hypoxemia alone (PaO2 <60 mmHg) in a long bone fracture patient 24-72 hours post-injury warrants a presumptive diagnosis and supportive management.

3. **Ordering a D-dimer to "rule out" FES.** D-dimer is elevated in both FES and PE and does not differentiate them. CTA is required to exclude thromboembolic PE. There is no specific confirmatory test for FES — diagnosis is clinical using Gurd or Schonfeld criteria.

4. **Delaying fracture fixation beyond 24 hours.** Delayed fixation is an independent risk factor for FES. Early stabilization (within 24 hours) reduces incidence from ~22% to ~5% and is the single most effective preventive measure.

5. **Missing petechiae.** The rash is transient (resolves within 24-48 hours of appearance), non-palpable, and located in areas not routinely examined (axillae, conjunctivae, anterior chest). Deliberate skin survey q4-6h for 72 hours in high-risk patients is required. The rash is pathognomonic — its presence eliminates the differential.

6. **Aggressive fluid resuscitation without assessing RV function.** FES causes acute pulmonary hypertension and RV failure. Volume loading a failing RV worsens RV dilation and interventricular septal shift, decreasing LV filling and cardiac output. Bedside echocardiography guides volume management.

7. **Assuming FES only follows fractures.** Non-traumatic FES occurs with liposuction, bone marrow transplant, pancreatitis, sickle cell crisis, and parenteral lipid infusion. The same clinical syndrome (hypoxemia, neurological changes, petechiae) develops without antecedent trauma.
