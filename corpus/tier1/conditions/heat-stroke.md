---
id: heat-stroke
condition: Heat Stroke
aliases: [heatstroke, sun stroke, hyperthermia, exertional heat stroke, classic heat stroke, EHS]
icd10: [T67.01XA, T67.02XA, T67.09XA]
esi: 1
time_to_harm: "< 30 minutes"
mortality_if_delayed: "10-50% depending on duration of hyperthermia; >80% if cooling delayed >2 hours"
category: environmental
track: tier1
sources:
  - type: guideline
    ref: "Wilderness Medical Society Clinical Practice Guidelines for the Prevention and Treatment of Heat Illness: 2019 Update"
  - type: pubmed
    ref: "Bouchama A, Knochel JP. Heat Stroke. N Engl J Med 2002;346(25):1978-1988"
    pmid: "12075060"
  - type: pubmed
    ref: "Casa DJ et al. National Athletic Trainers' Association Position Statement: Exertional Heat Illnesses. J Athl Train 2015;50(9):986-1000"
    pmid: "26381473"
  - type: pubmed
    ref: "Hifumi T et al. Heat stroke. J Intensive Care 2018;6:30"
    pmid: "29850022"
  - type: cdc
    ref: "CDC Heat-Related Illness: Prevention, Symptoms, Treatment (2023)"
last_updated: "2026-02-18"
compiled_by: agent
reviewed_by: null
---

# Heat Stroke

## Recognition

**Definition:** Core body temperature >40°C (104°F) with central nervous system dysfunction (altered mental status, seizures, coma). Distinct from heat exhaustion, which preserves CNS function.

**Two Forms:**
- **Exertional heat stroke (EHS):** Young, healthy individuals during strenuous physical activity (military, athletes, laborers). Rapid onset. Often diaphoretic (sweating may still be present).
- **Classic (non-exertional) heat stroke:** Elderly, chronically ill, medications impairing thermoregulation (anticholinergics, diuretics, beta-blockers, antipsychotics). Develops over hours to days during heat waves. Skin typically hot and dry (anhidrotic).

**Clinical Features:**
- Core temperature >40°C (104°F) — rectal temperature is the standard. Oral, axillary, temporal, and tympanic readings underestimate core temperature and are unreliable.
- Altered mental status: confusion, agitation, delirium, ataxia, seizures, coma
- Hot skin (dry in classic; may be diaphoretic in exertional)
- Tachycardia, hypotension (distributive shock pattern)
- Tachypnea, respiratory alkalosis
- Nausea, vomiting, diarrhea

**Organ Damage (temperature-duration dependent):**
- CNS: cerebral edema, cerebellar dysfunction (ataxia persists in 30% of EHS survivors)
- Hepatic: transaminases rise over 24-72 hours, hepatic failure in severe cases (peak at 72-96h)
- Renal: acute kidney injury from rhabdomyolysis, direct thermal injury, hypovolemia
- Hematologic: DIC develops in severe cases (24-48h)
- Cardiac: myocardial injury, arrhythmias
- Rhabdomyolysis: CK >5000, myoglobinuria (more common in EHS)

**High-Risk Medications:**
- Anticholinergics (impair sweating)
- Diuretics (dehydration)
- Beta-blockers (impair cardiac output response)
- Phenothiazines, antipsychotics (impair thermoregulation)
- Sympathomimetics (MDMA, amphetamines — increase heat production)
- SSRIs (serotonin syndrome overlap)

## Critical Actions

1. **Measure RECTAL temperature** — the only reliable core temperature measurement. Do not rely on oral, axillary, temporal, or tympanic readings.
2. **Begin aggressive cooling IMMEDIATELY** — cold-water immersion (CWI) is the gold standard: immerse patient in ice water bath (1-3°C) targeting cooling rate of 0.15-0.35°C/min. If CWI unavailable: ice packs to axillae, groin, neck, and torso; evaporative cooling (spray lukewarm water + high-flow fans); cold IV NS bolus 4°C 500 mL-1L.
3. **Target core temperature 38.5-39°C, then STOP active cooling** to prevent overshoot hypothermia. Continuous rectal temperature monitoring during cooling.
4. **IV fluid resuscitation** — NS or LR 1-2L IV bolus (cold fluids preferred for dual cooling/resuscitation effect). Guide ongoing fluids by urine output, hemodynamics, and lactate clearance.
5. **Treat seizures** — midazolam 5-10 mg IV/IM or diazepam 10 mg IV. Seizures increase heat production and must be controlled urgently.
6. **Intubate if GCS <=8** — airway protection for comatose patients. Avoid succinylcholine if rhabdomyolysis suspected (hyperkalemia risk). Use rocuronium 1.2 mg/kg IV.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Neuroleptic malignant syndrome (NMS) | Antipsychotic exposure, "lead-pipe" rigidity, elevated CK, develops over days |
| Serotonin syndrome | Serotonergic drug exposure, clonus (especially lower extremity), hyperreflexia, mydriasis, diarrhea |
| Malignant hyperthermia | Occurs during/after anesthesia with volatile agents or succinylcholine, muscle rigidity, rapidly rising ETCO2 |
| Thyroid storm | Known hyperthyroidism, goiter, exophthalmos, atrial fibrillation, elevated free T4/T3, low TSH |
| Sympathomimetic toxicity | Cocaine/amphetamine use, agitation, mydriasis, diaphoresis, hypertension, tachycardia |
| Meningitis/encephalitis | Fever with neck stiffness, headache, photophobia, CSF pleocytosis |
| Status epilepticus | Witnessed seizures, EEG confirms — hyperthermia secondary to muscle activity |
| Anticholinergic toxicity | "Dry as a bone, blind as a bat, mad as a hatter" — dry skin, mydriasis, urinary retention, absent bowel sounds |

## Workup

**Labs:**
- CBC — hemoconcentration, leukocytosis, thrombocytopenia (DIC)
- BMP — hypernatremia, hypo/hyperkalemia, acute kidney injury (elevated creatinine), hypophosphatemia
- Hepatic panel — AST/ALT rise over 24-72 hours, peak at 72-96 hours. Markedly elevated transaminases (>1000) indicate severe hepatic injury.
- Coagulation panel: INR, PTT, fibrinogen, D-dimer — DIC screening
- CK — rhabdomyolysis (CK >5000). Repeat at 6, 12, 24 hours (CK peaks at 24-72h).
- Urinalysis — myoglobinuria (dipstick positive for blood without RBCs on microscopy)
- Lactate — tissue hypoperfusion
- ABG/VBG — respiratory alkalosis (early), metabolic acidosis (late/severe)
- Troponin — myocardial injury
- Ammonia — hepatic encephalopathy in severe hepatic failure
- Blood glucose — hypoglycemia from hepatic failure

**ECG:**
- Sinus tachycardia (most common)
- ST changes from myocardial injury
- QTc prolongation
- Arrhythmias (ventricular tachycardia, atrial fibrillation)
- Hyperkalemia pattern if rhabdomyolysis (peaked T waves, widened QRS)

**Imaging:**
- CT head — if altered mental status persists after cooling (rule out intracranial pathology)
- CXR — aspiration, pulmonary edema
- CT abdomen — if hepatic failure suspected or abdominal pain

## Treatment

**Cooling (THE priority — every minute of delay increases mortality and morbidity):**
- **Cold-water immersion (gold standard):** ice water bath (1-3°C), target cooling rate 0.15-0.35°C/min, most effective method. Continuously monitor rectal temperature. Requires team coordination for monitoring access.
- **If CWI not feasible:** ice packs to axillae, groin, neck, and torso; wet sheets with fan-assisted evaporative cooling; cold IV fluids (4°C NS 500 mL-1L bolus); ice-water gastric lavage (NG tube with cold saline); ice-water bladder irrigation; peritoneal lavage with cold saline (severe refractory cases).
- **Stop active cooling at core temp 38.5-39°C** — afterdrop from peripheral vasoconstriction will continue to lower temperature. Overcooling causes shivering (increases heat production) and hypothermia-related complications.
- **Dantrolene is NOT effective** for heat stroke (unlike malignant hyperthermia). Do not use.
- **Antipyretics (acetaminophen, NSAIDs) are INEFFECTIVE** — heat stroke is not mediated by hypothalamic pyrogen set-point elevation. Antipyretics are useless and acetaminophen may worsen hepatic injury.

**IV Fluid Resuscitation:**
- NS or LR 1-2L IV bolus, then titrate to urine output >0.5 mL/kg/hr (>200 mL/hr if rhabdomyolysis)
- Cold IV fluids serve dual purpose: volume resuscitation and core cooling
- Avoid dextrose-containing fluids initially (hyperglycemia worsens neurological outcomes)

**Rhabdomyolysis Management:**
- Aggressive IV hydration: NS 200-300 mL/hr targeting UOP 200-300 mL/hr
- Monitor CK every 6-12 hours
- Monitor potassium (hyperkalemia) — calcium gluconate 3g IV, insulin 10 units IV + dextrose 50g IV, kayexalate, or emergent dialysis if refractory
- Sodium bicarbonate drip (150 mEq/L in D5W) to alkalinize urine pH >6.5 (controversial but still practiced for myoglobin clearance)

**Seizure Control:**
- Midazolam 5-10 mg IV/IM or diazepam 10 mg IV — repeat as needed
- Seizures dramatically increase heat production and oxygen consumption
- Refractory: propofol infusion 20-75 mcg/kg/min

**DIC Management:**
- Supportive: FFP 15 mL/kg for INR >2.0 with bleeding, cryoprecipitate 10 units for fibrinogen <100 mg/dL, platelet transfusion for count <50,000 with bleeding
- Cooling resolves the underlying trigger

**Hepatic Failure:**
- Transaminases peak at 72-96 hours — monitor serially
- N-acetylcysteine 150 mg/kg IV protocol (same as acetaminophen hepatotoxicity protocol) — evidence supports use for heat stroke hepatic failure
- Transplant hepatology consultation if INR >3.0, encephalopathy, or progressive liver failure
- Hypoglycemia monitoring with dextrose supplementation

## Disposition

**ICU Admission (all heat stroke patients):**
- Ongoing cooling and continuous rectal temperature monitoring
- Serial labs every 6-12 hours for 72 hours (transaminases peak late)
- Hemodynamic monitoring
- Rhabdomyolysis management
- DIC surveillance
- Neurological monitoring

**Hepatology/Transplant Consultation:**
- AST or ALT >1000
- INR >3.0
- Encephalopathy
- Acute liver failure

**Nephrology Consultation:**
- Acute kidney injury with oliguria despite adequate resuscitation
- Refractory hyperkalemia
- Need for renal replacement therapy

**Extended Monitoring:**
- Hepatic transaminases must be trended for 72-96 hours (delayed peak)
- CK must be trended for 48-72 hours
- Cerebellar dysfunction may persist (ataxia in 30% of EHS survivors)

**Never discharge a heat stroke patient from the ED.** Even if temperature normalizes, organ injury evolves over 72-96 hours.

## Pitfalls

1. **Using oral, tympanic, or temporal artery temperature instead of rectal.** These methods underestimate core temperature by 1-3°C and miss the diagnosis. Rectal temperature is the only reliable core measurement in suspected heat stroke.

2. **Delaying cooling for any reason.** Duration of hyperthermia directly determines mortality and organ damage. Cooling rate and time to target temperature are the strongest predictors of survival. Start cooling in the field, continue in the ED. Do not delay for IV access, labs, or imaging.

3. **Administering antipyretics.** Acetaminophen and NSAIDs do not lower temperature in heat stroke — the hypothalamic set point is normal. Acetaminophen may compound hepatic injury. Antipyretics are harmful or useless.

4. **Failing to monitor for delayed hepatic failure.** Transaminases may be normal or mildly elevated on presentation and peak at 72-96 hours. A normal initial hepatic panel does NOT exclude life-threatening hepatic injury. Serial monitoring for 3-4 days is mandatory.

5. **Missing rhabdomyolysis.** EHS frequently causes rhabdomyolysis with CK >100,000. Acute kidney injury from myoglobin nephropathy is preventable with aggressive hydration. Check CK on all heat stroke patients and repeat serially.

6. **Overcooling below 38°C.** Active cooling should stop at core temp 38.5-39°C. Afterdrop continues to lower temperature after external cooling stops. Hypothermia triggers shivering (heat generation) and coagulopathy.

7. **Confusing heat stroke with serotonin syndrome or NMS.** All three cause hyperthermia with altered mental status. Drug history differentiates: antipsychotics (NMS), serotonergic drugs (serotonin syndrome), environmental exposure/exertion (heat stroke). Exam findings differ: lead-pipe rigidity (NMS), clonus and hyperreflexia (serotonin syndrome).

8. **Not considering occult heat stroke in elderly patients.** Classic heat stroke in the elderly develops insidiously during heat waves. Presentation mimics sepsis, stroke, or delirium. Rectal temperature is required. Mortality exceeds 50% in elderly patients during heat waves.

9. **Using dantrolene.** Dantrolene treats malignant hyperthermia, not heat stroke. These are different entities with different mechanisms. Dantrolene has no role in heat stroke management.
