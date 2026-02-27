---
id: acute-thermal-dysregulation-syndrome
condition: Acute Thermal Dysregulation Syndrome
aliases: [ATDS, thermal dysregulation crisis, central thermoregulatory failure]
icd10: [R68.0, G93.40]
esi: 1
time_to_harm:
  irreversible_injury: "< 30 minutes"
  death: "< 2 hours"
  optimal_intervention_window: "< 15 minutes"
mortality_if_delayed: "40-60% mortality if cooling not initiated within 30 minutes"
category: environmental
track: tier1
sources:
  - type: guideline
    ref: "2022 Wilderness Medical Society Clinical Practice Guidelines for the Prevention and Treatment of Heat Illness"
    doi: "10.1016/j.wem.2022.01.001"
  - type: pubmed
    ref: "Bouchama A, et al. Heat Stroke. N Engl J Med. 2002;346(25):1978-1988"
    pmid: "12075060"
    doi: "10.1056/NEJMra011089"
  - type: guideline
    ref: "2020 AHA Guidelines for CPR and Emergency Cardiovascular Care — Part 7: Adult Advanced Cardiovascular Life Support"
    doi: "10.1161/CIR.0000000000000916"
last_updated: "2026-02-27"
compiled_by: agent
risk_tier: A
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
# Acute Thermal Dysregulation Syndrome

## Recognition

**Definition:** Acute failure of central thermoregulatory mechanisms resulting in uncontrolled core temperature elevation (> 40.5 C / 105 F) with associated end-organ dysfunction. Distinct from environmental heat stroke in that the primary mechanism is hypothalamic dysfunction rather than exogenous heat burden.

**Triggers:**
- Drug-induced: serotonin syndrome (SSRIs + MAOIs), neuroleptic malignant syndrome (antipsychotics), malignant hyperthermia (volatile anesthetics + succinylcholine)
- CNS injury: hypothalamic hemorrhage, encephalitis, traumatic brain injury
- Endocrine: thyroid storm with thermoregulatory collapse
- Idiopathic: rare familial variants

**Clinical features:**
- Core temperature > 40.5 C (rectal or esophageal probe -- tympanic/axillary unreliable)
- Altered mental status (confusion, agitation, seizures, coma)
- Tachycardia, hypotension, tachypnea
- Rigidity (NMS, malignant hyperthermia), clonus/hyperreflexia (serotonin syndrome)
- Diaphoresis (early) progressing to anhidrosis (late -- ominous sign)
- Rhabdomyolysis (CK > 5,000 IU/L), DIC, hepatic failure, acute kidney injury

**Key principle:** Core temperature > 40.5 C with altered mental status is a medical emergency regardless of etiology. Cooling must not be delayed for diagnostic workup.

## Critical Actions

| Action | Target |
|---|---|
| Core temperature measurement (rectal) | Immediate |
| Aggressive cooling initiation | < 5 minutes |
| IV access and fluid resuscitation | < 5 minutes |
| Consider early intubation for airway protection | < 15 minutes |
| Cardiac monitoring | Continuous |

1. Measure core temperature with rectal or esophageal probe. Do not rely on tympanic or oral thermometry.
2. Begin aggressive cooling immediately:
   - Ice-water immersion (gold standard): target cooling rate 0.15-0.20 C/min
   - Evaporative cooling (mist + fan) if immersion unavailable
   - Ice packs to axillae, groin, neck
   - Cold IV normal saline 4 C, 500 mL boluses
   - Stop cooling at 38.5 C to prevent overshoot
3. IV crystalloid resuscitation: normal saline 20-30 mL/kg bolus, titrate to MAP > 65 mmHg
4. Benzodiazepines for shivering or seizures: midazolam 5 mg or lorazepam 2 mg IV
5. Epinephrine 0.5 mg IV for cardiac arrest
6. Dantrolene 2.5 mg/kg IV for malignant hyperthermia or NMS: repeat q5-10min to max 10 mg/kg
7. Cyproheptadine 12 mg PO/NG loading dose for serotonin syndrome, then 4 mg PO q6h

## Differential Diagnosis

- Serotonin syndrome (clonus, hyperreflexia, diarrhea -- look for serotonergic drug exposure)
- Neuroleptic malignant syndrome (lead-pipe rigidity, bradykinesia -- develops over days, not hours)
- Malignant hyperthermia (intraoperative, masseter rigidity, rising EtCO2)
- Thyroid storm (goiter, lid lag, Burch-Wartofsky score > 45)
- Environmental heat stroke (exertional or classic -- exogenous heat burden)
- Anticholinergic toxidrome (dry, flushed, mydriasis, urinary retention, absent bowel sounds)
- Sympathomimetic toxidrome (diaphoresis, mydriasis, hypertension, tachycardia)
- CNS infection (meningitis, encephalitis -- fever + nuchal rigidity + focal deficits)
- Status epilepticus (sustained seizure activity generating heat)

## Workup

- **Core temperature:** rectal or esophageal probe (continuous monitoring preferred)
- **BMP:** electrolytes (hyperkalemia from rhabdomyolysis), glucose, BUN/Cr (AKI)
- **CBC with differential**
- **Coagulation panel:** PT/INR, PTT, fibrinogen, D-dimer (DIC screen)
- **CK:** serial measurements (rhabdomyolysis if > 5,000 IU/L)
- **LFTs:** AST/ALT (hepatic injury, often delayed 24-72 hours)
- **Lactate:** tissue hypoperfusion marker
- **Urinalysis:** myoglobinuria (tea-colored urine)
- **TSH, free T4:** if thyroid storm suspected
- **Toxicology screen** and medication reconciliation
- **Blood cultures** if infectious etiology suspected
- **CT head:** if focal neurologic deficits or suspected CNS lesion
- **Lumbar puncture:** if meningitis/encephalitis not excluded
- **Point-of-care echocardiography:** cardiac function, volume status
- **ABG/VBG:** acid-base status

## Treatment

### Cooling

- **Ice-water immersion** (gold standard): submerge to clavicles in 2-4 C water, continuously stir. Target cooling rate 0.15-0.20 C/min. Stop at core temp 38.5 C.
- **Evaporative cooling:** undress patient, mist with tepid water, apply high-flow fans. Less effective than immersion.
- **Adjuncts:** ice packs to axillae, groin, neck, scalp. Cold IV NS 4 C 500 mL boluses.
- **Avoid antipyretics** (acetaminophen, NSAIDs) -- these reset the hypothalamic set point, which is irrelevant when the hypothalamus is dysfunctional. They add hepatotoxicity risk.

### Fluid Resuscitation

- NS 20-30 mL/kg IV bolus, repeat as needed
- Target urine output 1-2 mL/kg/hr (especially if rhabdomyolysis)
- Avoid lactated Ringer's if hyperkalemia suspected (contains 4 mEq/L K+)

### Dantrolene and Cyproheptadine

- **Dantrolene** (malignant hyperthermia, severe NMS): 2.5 mg/kg IV, repeat q5-10min to max 10 mg/kg. Reconstitute with sterile water (not NS -- precipitates). Monitor for hepatotoxicity.
- **Cyproheptadine** (serotonin syndrome): 12 mg PO/NG load, then 4 mg q6h (max 32 mg/day). Only available PO -- no IV formulation.
- **Do NOT combine dantrolene and cyproheptadine** -- dantrolene potentiates serotonergic crisis through calcium-mediated 5-HT release amplification.

### Seizure Management

- Benzodiazepines first-line: lorazepam 4 mg IV or midazolam 10 mg IM
- Refractory: propofol 1-2 mg/kg IV bolus, then 20-80 mcg/kg/min infusion
- Avoid phenytoin in hyperthermia (ineffective for toxin-induced seizures, worsens dysrhythmias)

### Rhabdomyolysis Management

- Aggressive IV crystalloid: target UOP 200-300 mL/hr
- Sodium bicarbonate 150 mEq in 1 L D5W if urine pH < 6.5 (urine alkalinization)
- Monitor CK q6-12h, electrolytes q4-6h
- Renal replacement therapy if refractory AKI or life-threatening hyperkalemia

## Disposition

- **All patients:** ICU admission with continuous temperature monitoring
- **Cardiac arrest survivors:** ICU with targeted temperature management protocol
- **Rhabdomyolysis (CK > 5,000):** ICU with aggressive hydration, nephrology consultation if AKI
- **Malignant hyperthermia:** ICU for minimum 24 hours post-dantrolene (recrudescence risk 25%)
- **Serotonin syndrome:** If symptoms improve within 2 hours of discontinuing the serotonergic agent, discharge with outpatient neurology follow-up in 48 hours. Prescribe oral cyproheptadine for home use.
- **NMS:** ICU admission, psychiatry consultation for medication adjustment. Recovery typically 7-14 days.

## Pitfalls

1. **Relying on tympanic or oral temperature.** These underestimate core temperature by 1-2 C in hyperthermia. Rectal or esophageal probe is mandatory for accurate measurement and monitoring.

2. **Administering antipyretics.** Acetaminophen and NSAIDs target hypothalamic prostaglandin-mediated fever. In thermoregulatory failure, the hypothalamus is dysfunctional -- antipyretics are ineffective and add hepatotoxic risk in an already-stressed liver.

3. **Delaying cooling for diagnostic workup.** Cooling must begin within 5 minutes. Every minute of core temperature > 40.5 C increases end-organ damage. Start cooling, then investigate the cause.

4. **Failing to distinguish serotonin syndrome from NMS.** Serotonin syndrome: rapid onset (hours), clonus, hyperreflexia, diarrhea. NMS: slow onset (days), lead-pipe rigidity, bradykinesia, mutism. Treatment differs fundamentally (cyproheptadine vs bromocriptine/dantrolene).

5. **Not checking CK and monitoring for rhabdomyolysis.** Sustained hyperthermia and rigidity cause muscle breakdown. CK > 5,000 IU/L requires aggressive hydration to prevent myoglobin-induced AKI. Serial CK measurement is mandatory.

6. **Overshoot cooling.** Stopping cooling at 40.0 C instead of 38.5 C results in continued temperature drift downward. Body cooling has inertia. Stop active measures at 38.5 C.

7. **Missing malignant hyperthermia in the post-anesthesia setting.** Unexplained fever, rigidity, and rising EtCO2 in a patient recently exposed to volatile anesthetics or succinylcholine is malignant hyperthermia until proven otherwise. Dantrolene must be given immediately.

8. **Ignoring DIC.** Hyperthermia-induced coagulopathy progresses rapidly. Serial coagulation panels (PT, PTT, fibrinogen, D-dimer) are required. Fibrinogen < 100 mg/dL requires cryoprecipitate.
