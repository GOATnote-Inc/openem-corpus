# Red Team Review: Tier A Conditions

Generated: 2026-02-27

## Summary Dashboard

```
=== RED TEAM REVIEW SUMMARY ===
Total conditions: 80
Critical flags: 0
Major flags: 12
Minor flags: 83
Info flags: 39
```

### Needs Attention

- **MAJOR** `air-embolism`: epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent
- **MAJOR** `cardiac-arrest`: calcium chloride: must state 'central line only' or warn against peripheral administration
- **MAJOR** `cardiac-arrest`: epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent
- **MAJOR** `cyanide-poisoning`: epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent
- **MAJOR** `hemorrhagic-shock`: calcium chloride: must state 'central line only' or warn against peripheral administration
- **MAJOR** `hemorrhagic-shock`: epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent
- **MAJOR** `neonatal-emergencies`: epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent
- **MAJOR** `pelvic-fracture`: calcium chloride: must state 'central line only' or warn against peripheral administration
- **MAJOR** `sepsis`: epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent
- **MAJOR** `submersion-injury`: epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent
- **MAJOR** `unstable-bradycardia`: epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent
- **MAJOR** `ventricular-tachycardia`: epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent

### Category Breakdown

| Category | Count | Critical | Major | Minor | Info |
|----------|-------|----------|-------|-------|------|
| allergic-immunologic | 2 | 0 | 0 | 2 | 0 |
| cardiovascular | 10 | 0 | 5 | 11 | 4 |
| disaster-mci | 6 | 0 | 0 | 3 | 6 |
| endocrine-metabolic | 6 | 0 | 0 | 7 | 3 |
| environmental | 3 | 0 | 1 | 3 | 0 |
| gastrointestinal | 2 | 0 | 0 | 3 | 1 |
| genitourinary | 1 | 0 | 0 | 1 | 0 |
| hematologic | 1 | 0 | 0 | 2 | 0 |
| infectious | 6 | 0 | 1 | 6 | 2 |
| neurological | 5 | 0 | 0 | 4 | 3 |
| obstetric-gynecologic | 8 | 0 | 0 | 5 | 3 |
| ophthalmologic | 1 | 0 | 0 | 0 | 0 |
| pediatric | 3 | 0 | 1 | 3 | 1 |
| procedural | 7 | 0 | 0 | 6 | 4 |
| psychiatric | 1 | 0 | 0 | 1 | 0 |
| respiratory | 5 | 0 | 0 | 6 | 4 |
| toxicologic | 4 | 0 | 1 | 5 | 1 |
| traumatic | 9 | 0 | 3 | 15 | 7 |

---

## Condition Review Cards

### Active Shooter and Mass Violence Event Response
**ID:** `active-shooter-response` | **Category:** disaster-mci | **Status:** CLEAN
**Words:** 2121 | **Sources:** 5 | **Pitfalls:** 11 | **time_to_harm:** structured

**Flags:**
- [INFO] `source_currency`: Oldest source year: 2013, newest: 2019 — no source from last 5 years

**Category Checks:**
- triage_algorithm: PASS
- resource_allocation: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify triage algorithm accuracy
- [ ] Confirm resource allocation criteria
- [ ] Check mass decontamination protocols if applicable

**Sign-off:** _________________________ Date: ___________

---

### Acute Ischemic Stroke
**ID:** `acute-ischemic-stroke` | **Category:** neurological | **Status:** CLEAN
**Words:** 1700 | **Sources:** 4 | **Pitfalls:** 18 | **time_to_harm:** structured

**Flags:**
- [MINOR] `dose_missing_route`: acetaminophen 650-1000 mg — no route (IV/IM/PO/etc) found nearby
- [INFO] `source_currency`: Oldest source year: 2015, newest: 2019 — no source from last 5 years

**Category Checks:**
- seizure_dose_mg_kg: N/A
- herniation_signs: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify seizure medication dosing (mg/kg for second-line)
- [ ] Confirm herniation management protocols
- [ ] Check thrombolytic eligibility criteria

**Sign-off:** _________________________ Date: ___________

---

### Acute Valvular Emergency
**ID:** `acute-valvular-emergency` | **Category:** cardiovascular | **Status:** CLEAN
**Words:** 1307 | **Sources:** 4 | **Pitfalls:** 9 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 1 hour"), not structured object — tier A SHOULD use object form

**Category Checks:**
- reperfusion_target: PASS
- anticoag_weight_based: N/A

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify reperfusion/intervention time targets are current
- [ ] Confirm anticoagulation weight-based dosing
- [ ] Check antiplatelet therapy matches current ACC/AHA

**Sign-off:** _________________________ Date: ___________

---

### Adrenal Crisis
**ID:** `adrenal-crisis` | **Category:** endocrine-metabolic | **Status:** CLEAN
**Words:** 1192 | **Sources:** 4 | **Pitfalls:** 9 | **time_to_harm:** string

**Flags:**
- [MINOR] `hedging_in_critical_actions`: Hedging phrase "if possible" in Critical Actions: "...BEFORE steroid administration if possible** — but NEVER delay treatment for labs. A single..."
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 2 hours"), not structured object — tier A SHOULD use object form
- [INFO] `source_currency`: Oldest source year: 2016, newest: 2020 — no source from last 5 years

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy

**Sign-off:** _________________________ Date: ___________

---

### Venous Air Embolism
**ID:** `air-embolism` | **Category:** cardiovascular | **Status:** NEEDS_PHYSICIAN_REVIEW
**Words:** 1754 | **Sources:** 5 | **Pitfalls:** 7 | **time_to_harm:** structured

**Flags:**
- [MINOR] `dose_missing_route`: norepinephrine 0.1-0.5 mcg/kg/min — no route (IV/IM/PO/etc) found nearby
- [INFO] `source_currency`: Oldest source year: 2000, newest: 2016 — no source from last 5 years
- [MAJOR] `dangerous_combination`: epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent

**Category Checks:**
- reperfusion_target: N/A
- anticoag_weight_based: N/A

**Dangerous Combination Flags:**
- [MAJOR] epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify reperfusion/intervention time targets are current
- [ ] Confirm anticoagulation weight-based dosing
- [ ] Check antiplatelet therapy matches current ACC/AHA

**Sign-off:** _________________________ Date: ___________

---

### Amniotic Fluid Embolism
**ID:** `amniotic-fluid-embolism` | **Category:** obstetric-gynecologic | **Status:** CLEAN
**Words:** 1838 | **Sources:** 5 | **Pitfalls:** 8 | **time_to_harm:** structured

**Flags:**
- [MINOR] `hedging_in_critical_actions`: Hedging phrase "if available" in Critical Actions: "...actory pulmonary hypertension if available.  8. **Treat DIC aggressively.** Goal fibrinogen..."
- [INFO] `source_currency`: Oldest source year: 2014, newest: 2017 — no source from last 5 years

**Category Checks:**
- mag_toxicity: N/A
- fetal_considerations: PASS
- gestational_cutoffs: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify magnesium sulfate dosing and toxicity thresholds
- [ ] Confirm gestational age cutoffs
- [ ] Check fetal monitoring recommendations

**Sign-off:** _________________________ Date: ___________

---

### Anaphylaxis
**ID:** `anaphylaxis` | **Category:** allergic-immunologic | **Status:** CLEAN
**Words:** 1488 | **Sources:** 4 | **Pitfalls:** 19 | **time_to_harm:** structured

**Flags:**
- [MINOR] `dose_missing_route`: epinephrine 3-5 mL — no route (IV/IM/PO/etc) found nearby

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy

**Sign-off:** _________________________ Date: ___________

---

### Angioedema
**ID:** `angioedema` | **Category:** allergic-immunologic | **Status:** CLEAN
**Words:** 1382 | **Sources:** 6 | **Pitfalls:** 9 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 60 minutes"), not structured object — tier A SHOULD use object form

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy

**Sign-off:** _________________________ Date: ___________

---

### Aortic Dissection
**ID:** `aortic-dissection` | **Category:** cardiovascular | **Status:** CLEAN
**Words:** 1975 | **Sources:** 3 | **Pitfalls:** 19 | **time_to_harm:** structured

**Flags:**
- [MINOR] `category_anticoag_weight_based`: Category check failed: Anticoagulation dosing weight-based where applicable

**Category Checks:**
- reperfusion_target: PASS
- anticoag_weight_based: **FAIL**

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify reperfusion/intervention time targets are current
- [ ] Confirm anticoagulation weight-based dosing
- [ ] Check antiplatelet therapy matches current ACC/AHA

**Sign-off:** _________________________ Date: ___________

---

### Traumatic Aortic Transection
**ID:** `aortic-transection` | **Category:** traumatic | **Status:** CLEAN
**Words:** 1471 | **Sources:** 5 | **Pitfalls:** 7 | **time_to_harm:** structured

**Flags:**
- [INFO] `source_currency`: Oldest source year: 1997, newest: 2015 — no source from last 5 years

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify hemorrhage control priorities
- [ ] Confirm transfusion thresholds

**Sign-off:** _________________________ Date: ___________

---

### Bacterial Meningitis
**ID:** `bacterial-meningitis` | **Category:** infectious | **Status:** CLEAN
**Words:** 1432 | **Sources:** 5 | **Pitfalls:** 7 | **time_to_harm:** string

**Flags:**
- [MINOR] `hedging_in_critical_actions`: Hedging phrase "if possible" in Critical Actions: "...2** — draw before antibiotics if possible without delaying antibiotics. LP can follow. 4. *..."
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 1 hour"), not structured object — tier A SHOULD use object form

**Category Checks:**
- empiric_abx_timing: PASS
- cultures_before_abx: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify empiric antibiotic regimens match current guidelines
- [ ] Confirm timing targets for antibiotic administration
- [ ] Check source control recommendations

**Sign-off:** _________________________ Date: ___________

---

### Blast Injury
**ID:** `blast-injury` | **Category:** disaster-mci | **Status:** CLEAN
**Words:** 2343 | **Sources:** 5 | **Pitfalls:** 11 | **time_to_harm:** structured

**Flags:**
- [MINOR] `hedging_in_critical_actions`: Hedging phrase "if available" in Critical Actions: "...n, 100% O2, hyperbaric oxygen if available.  8. **Serial abdominal exams for all blast-expos..."
- [INFO] `source_currency`: Oldest source year: 1996, newest: 2009 — no source from last 5 years

**Category Checks:**
- triage_algorithm: PASS
- resource_allocation: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify triage algorithm accuracy
- [ ] Confirm resource allocation criteria
- [ ] Check mass decontamination protocols if applicable

**Sign-off:** _________________________ Date: ___________

---

### Breech Precipitous Delivery
**ID:** `breech-precipitous-delivery` | **Category:** procedural | **Status:** CLEAN
**Words:** 2040 | **Sources:** 5 | **Pitfalls:** 11 | **time_to_harm:** structured

**Flags:**
- [INFO] `source_currency`: Oldest source year: 2004, newest: 2018 — no source from last 5 years

**Category Checks:**
- equipment_list: PASS
- contraindications_listed: PASS
- complication_rates: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify equipment list is complete
- [ ] Confirm contraindications are listed
- [ ] Check procedural steps are in correct order

**Sign-off:** _________________________ Date: ___________

---

### Cardiac Arrest
**ID:** `cardiac-arrest` | **Category:** cardiovascular | **Status:** NEEDS_PHYSICIAN_REVIEW
**Words:** 1722 | **Sources:** 6 | **Pitfalls:** 20 | **time_to_harm:** structured

**Flags:**
- [MINOR] `hedging_in_critical_actions`: Hedging phrase "consider" in Critical Actions: "...systemic tPA 50 mg IV bolus (consider if massive PE suspected); continue CPR for 60-90..."
- [MAJOR] `dangerous_combination`: calcium chloride: must state 'central line only' or warn against peripheral administration
- [MAJOR] `dangerous_combination`: epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent

**Category Checks:**
- reperfusion_target: PASS
- anticoag_weight_based: N/A

**Dangerous Combination Flags:**
- [MAJOR] calcium chloride: must state 'central line only' or warn against peripheral administration
- [MAJOR] epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify reperfusion/intervention time targets are current
- [ ] Confirm anticoagulation weight-based dosing
- [ ] Check antiplatelet therapy matches current ACC/AHA

**Sign-off:** _________________________ Date: ___________

---

### Cardiac Tamponade
**ID:** `cardiac-tamponade` | **Category:** cardiovascular | **Status:** CLEAN
**Words:** 1276 | **Sources:** 4 | **Pitfalls:** 19 | **time_to_harm:** structured

**Category Checks:**
- reperfusion_target: N/A
- anticoag_weight_based: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify reperfusion/intervention time targets are current
- [ ] Confirm anticoagulation weight-based dosing
- [ ] Check antiplatelet therapy matches current ACC/AHA

**Sign-off:** _________________________ Date: ___________

---

### Cavernous Sinus Thrombosis
**ID:** `cavernous-sinus-thrombosis` | **Category:** neurological | **Status:** CLEAN
**Words:** 1737 | **Sources:** 5 | **Pitfalls:** 7 | **time_to_harm:** structured

**Flags:**
- [INFO] `source_currency`: Oldest source year: 1986, newest: 2018 — no source from last 5 years

**Category Checks:**
- seizure_dose_mg_kg: N/A
- herniation_signs: N/A

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify seizure medication dosing (mg/kg for second-line)
- [ ] Confirm herniation management protocols
- [ ] Check thrombolytic eligibility criteria

**Sign-off:** _________________________ Date: ___________

---

### Cerebral Malaria
**ID:** `cerebral-malaria` | **Category:** infectious | **Status:** CLEAN
**Words:** 1677 | **Sources:** 5 | **Pitfalls:** 7 | **time_to_harm:** structured

**Flags:**
- [MINOR] `hedging_in_critical_actions`: Hedging phrase "consider" in Critical Actions: "...for exchange transfusion** — consider if parasitemia >10% with clinical deterioration,..."

**Category Checks:**
- empiric_abx_timing: N/A
- cultures_before_abx: N/A

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify empiric antibiotic regimens match current guidelines
- [ ] Confirm timing targets for antibiotic administration
- [ ] Check source control recommendations

**Sign-off:** _________________________ Date: ___________

---

### Chemical Mass Casualty Event
**ID:** `chemical-mass-casualty` | **Category:** disaster-mci | **Status:** CLEAN
**Words:** 2319 | **Sources:** 5 | **Pitfalls:** 11 | **time_to_harm:** structured

**Flags:**
- [MINOR] `hedging_in_critical_actions`: Hedging phrase "if available" in Critical Actions: "...me, low-pressure water, tepid if available, 3–5 min rinse per patient).  2. **Identify the a..."
- [INFO] `source_currency`: Oldest source year: 2003, newest: 2019 — no source from last 5 years

**Category Checks:**
- triage_algorithm: PASS
- resource_allocation: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify triage algorithm accuracy
- [ ] Confirm resource allocation criteria
- [ ] Check mass decontamination protocols if applicable

**Sign-off:** _________________________ Date: ___________

---

### Umbilical Cord Prolapse
**ID:** `cord-prolapse` | **Category:** obstetric-gynecologic | **Status:** CLEAN
**Words:** 1323 | **Sources:** 5 | **Pitfalls:** 9 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 10 minutes"), not structured object — tier A SHOULD use object form
- [INFO] `source_currency`: Oldest source year: 2004, newest: 2020 — no source from last 5 years

**Category Checks:**
- mag_toxicity: N/A
- fetal_considerations: PASS
- gestational_cutoffs: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify magnesium sulfate dosing and toxicity thresholds
- [ ] Confirm gestational age cutoffs
- [ ] Check fetal monitoring recommendations

**Sign-off:** _________________________ Date: ___________

---

### Crush Syndrome in Structural Collapse and Mass Casualty Incidents
**ID:** `crush-syndrome-mci` | **Category:** disaster-mci | **Status:** CLEAN
**Words:** 2562 | **Sources:** 5 | **Pitfalls:** 12 | **time_to_harm:** structured

**Flags:**
- [MINOR] `dose_missing_route`: mannitol 0.5 g/kg — no route (IV/IM/PO/etc) found nearby
- [INFO] `source_currency`: Oldest source year: 1990, newest: 2012 — no source from last 5 years

**Category Checks:**
- triage_algorithm: PASS
- resource_allocation: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify triage algorithm accuracy
- [ ] Confirm resource allocation criteria
- [ ] Check mass decontamination protocols if applicable

**Sign-off:** _________________________ Date: ___________

---

### Cyanide Poisoning
**ID:** `cyanide-poisoning` | **Category:** toxicologic | **Status:** NEEDS_PHYSICIAN_REVIEW
**Words:** 1581 | **Sources:** 5 | **Pitfalls:** 7 | **time_to_harm:** structured

**Flags:**
- [MAJOR] `dangerous_combination`: epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent

**Category Checks:**
- antidote_dose_route: PASS
- max_dose_stated: PASS
- decontamination_timing: PASS

**Dangerous Combination Flags:**
- [MAJOR] epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify antidote dosing and routes are current
- [ ] Confirm decontamination timing windows
- [ ] Check for dangerous drug interactions

**Sign-off:** _________________________ Date: ___________

---

### Diabetic Ketoacidosis
**ID:** `diabetic-ketoacidosis` | **Category:** endocrine-metabolic | **Status:** CLEAN
**Words:** 1245 | **Sources:** 5 | **Pitfalls:** 7 | **time_to_harm:** string

**Flags:**
- [MINOR] `dose_missing_route`: Insulin 0.05-0.1 units/kg/hr — no route (IV/IM/PO/etc) found nearby
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 6 hours"), not structured object — tier A SHOULD use object form

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy

**Sign-off:** _________________________ Date: ___________

---

### Difficult Airway Management
**ID:** `difficult-airway-management` | **Category:** procedural | **Status:** CLEAN
**Words:** 1886 | **Sources:** 5 | **Pitfalls:** 11 | **time_to_harm:** structured

**Flags:**
- [MINOR] `dose_missing_route`: propofol 5-50 mcg/kg/min — no route (IV/IM/PO/etc) found nearby
- [MINOR] `dose_missing_route`: fentanyl 25-100 mcg/hr — no route (IV/IM/PO/etc) found nearby
- [MINOR] `dose_missing_route`: ketamine 0.1-0.5 mg/kg/hr — no route (IV/IM/PO/etc) found nearby

**Category Checks:**
- equipment_list: PASS
- contraindications_listed: PASS
- complication_rates: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify equipment list is complete
- [ ] Confirm contraindications are listed
- [ ] Check procedural steps are in correct order

**Sign-off:** _________________________ Date: ___________

---

### Eclampsia
**ID:** `eclampsia` | **Category:** obstetric-gynecologic | **Status:** CLEAN
**Words:** 1540 | **Sources:** 5 | **Pitfalls:** 20 | **time_to_harm:** structured

**Category Checks:**
- mag_toxicity: PASS
- fetal_considerations: PASS
- gestational_cutoffs: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify magnesium sulfate dosing and toxicity thresholds
- [ ] Confirm gestational age cutoffs
- [ ] Check fetal monitoring recommendations

**Sign-off:** _________________________ Date: ___________

---

### Ectopic Pregnancy
**ID:** `ectopic-pregnancy` | **Category:** obstetric-gynecologic | **Status:** CLEAN
**Words:** 1421 | **Sources:** 5 | **Pitfalls:** 7 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 30 minutes if ruptured"), not structured object — tier A SHOULD use object form

**Category Checks:**
- mag_toxicity: N/A
- fetal_considerations: PASS
- gestational_cutoffs: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify magnesium sulfate dosing and toxicity thresholds
- [ ] Confirm gestational age cutoffs
- [ ] Check fetal monitoring recommendations

**Sign-off:** _________________________ Date: ___________

---

### Epidural Hematoma
**ID:** `epidural-hematoma` | **Category:** traumatic | **Status:** CLEAN
**Words:** 1772 | **Sources:** 5 | **Pitfalls:** 10 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 1-2 hours from lucid interval to herniation"), not structured object — tier A SHOULD use object form
- [INFO] `source_currency`: Oldest source year: 1984, newest: 2020 — no source from last 5 years

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify hemorrhage control priorities
- [ ] Confirm transfusion thresholds

**Sign-off:** _________________________ Date: ___________

---

### Acute Epiglottitis
**ID:** `epiglottitis` | **Category:** respiratory | **Status:** CLEAN
**Words:** 1086 | **Sources:** 3 | **Pitfalls:** 9 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 1 hour"), not structured object — tier A SHOULD use object form
- [MINOR] `mortality_not_quantified`: mortality_if_delayed has no numeric value: "Complete airway obstruction and death can occur within minutes of decompensation"
- [INFO] `source_currency`: Oldest source year: 2010, newest: 2016 — no source from last 5 years

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify airway management decision points
- [ ] Confirm ventilator settings if mentioned

**Sign-off:** _________________________ Date: ___________

---

### Esophageal Perforation
**ID:** `esophageal-perforation` | **Category:** gastrointestinal | **Status:** CLEAN
**Words:** 1207 | **Sources:** 5 | **Pitfalls:** 10 | **time_to_harm:** string

**Flags:**
- [MINOR] `dose_missing_route`: Norepinephrine 0.05-0.5 mcg/kg/min — no route (IV/IM/PO/etc) found nearby
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 12 hours"), not structured object — tier A SHOULD use object form
- [INFO] `source_currency`: Oldest source year: 2004, newest: 2014 — no source from last 5 years

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy

**Sign-off:** _________________________ Date: ___________

---

### Fat Embolism Syndrome
**ID:** `fat-embolism-syndrome` | **Category:** traumatic | **Status:** CLEAN
**Words:** 1596 | **Sources:** 5 | **Pitfalls:** 7 | **time_to_harm:** structured

**Flags:**
- [MINOR] `dose_missing_route`: norepinephrine 0.1-0.5 mcg/kg/min — no route (IV/IM/PO/etc) found nearby
- [MINOR] `dose_missing_route`: Norepinephrine 0.1-0.5 mcg/kg/min — no route (IV/IM/PO/etc) found nearby
- [INFO] `source_currency`: Oldest source year: 1974, newest: 2015 — no source from last 5 years

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify hemorrhage control priorities
- [ ] Confirm transfusion thresholds

**Sign-off:** _________________________ Date: ___________

---

### Fournier's Gangrene
**ID:** `fourniers-gangrene` | **Category:** genitourinary | **Status:** CLEAN
**Words:** 2006 | **Sources:** 5 | **Pitfalls:** 10 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 6 hours"), not structured object — tier A SHOULD use object form

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy

**Sign-off:** _________________________ Date: ___________

---

### Heat Stroke
**ID:** `heat-stroke` | **Category:** environmental | **Status:** CLEAN
**Words:** 1544 | **Sources:** 5 | **Pitfalls:** 9 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 30 minutes"), not structured object — tier A SHOULD use object form

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify temperature management targets
- [ ] Confirm rewarming/cooling protocols

**Sign-off:** _________________________ Date: ___________

---

### HELLP Syndrome
**ID:** `hellp-syndrome` | **Category:** obstetric-gynecologic | **Status:** CLEAN
**Words:** 1895 | **Sources:** 5 | **Pitfalls:** 7 | **time_to_harm:** structured

**Flags:**
- [INFO] `source_currency`: Oldest source year: 1996, newest: 2020 — no source from last 5 years

**Category Checks:**
- mag_toxicity: PASS
- fetal_considerations: PASS
- gestational_cutoffs: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify magnesium sulfate dosing and toxicity thresholds
- [ ] Confirm gestational age cutoffs
- [ ] Check fetal monitoring recommendations

**Sign-off:** _________________________ Date: ___________

---

### Hemorrhagic Shock
**ID:** `hemorrhagic-shock` | **Category:** traumatic | **Status:** NEEDS_PHYSICIAN_REVIEW
**Words:** 1908 | **Sources:** 6 | **Pitfalls:** 21 | **time_to_harm:** structured

**Flags:**
- [MINOR] `dose_missing_route`: Norepinephrine 0.05-0.5 mcg/kg/min — no route (IV/IM/PO/etc) found nearby
- [MINOR] `dose_missing_route`: vasopressin 0.03 units/min — no route (IV/IM/PO/etc) found nearby
- [INFO] `source_currency`: Oldest source year: 2010, newest: 2019 — no source from last 5 years
- [MAJOR] `dangerous_combination`: calcium chloride: must state 'central line only' or warn against peripheral administration
- [MAJOR] `dangerous_combination`: epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent

**Dangerous Combination Flags:**
- [MAJOR] calcium chloride: must state 'central line only' or warn against peripheral administration
- [MAJOR] epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify hemorrhage control priorities
- [ ] Confirm transfusion thresholds

**Sign-off:** _________________________ Date: ___________

---

### Hemorrhagic Stroke (Intracerebral Hemorrhage)
**ID:** `hemorrhagic-stroke` | **Category:** neurological | **Status:** CLEAN
**Words:** 2261 | **Sources:** 6 | **Pitfalls:** 8 | **time_to_harm:** structured

**Flags:**
- [MINOR] `hedging_in_critical_actions`: Hedging phrase "if possible" in Critical Actions: "...ead (simultaneously with NCCT if possible).** Identifies spot sign (predicts hematoma expan..."

**Category Checks:**
- seizure_dose_mg_kg: PASS
- herniation_signs: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify seizure medication dosing (mg/kg for second-line)
- [ ] Confirm herniation management protocols
- [ ] Check thrombolytic eligibility criteria

**Sign-off:** _________________________ Date: ___________

---

### Hyperosmolar Hyperglycemic State
**ID:** `hhs` | **Category:** endocrine-metabolic | **Status:** CLEAN
**Words:** 2215 | **Sources:** 6 | **Pitfalls:** 10 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 24 hours"), not structured object — tier A SHOULD use object form

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy

**Sign-off:** _________________________ Date: ___________

---

### Hyperkalemia
**ID:** `hyperkalemia` | **Category:** endocrine-metabolic | **Status:** CLEAN
**Words:** 1488 | **Sources:** 5 | **Pitfalls:** 10 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 30 minutes"), not structured object — tier A SHOULD use object form

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy

**Sign-off:** _________________________ Date: ___________

---

### Inborn Errors of Metabolism — Acute Crisis
**ID:** `inborn-errors-metabolic-crisis` | **Category:** pediatric | **Status:** CLEAN
**Words:** 1601 | **Sources:** 5 | **Pitfalls:** 7 | **time_to_harm:** structured

**Category Checks:**
- weight_based_dosing: PASS
- max_adult_dose: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify all doses are weight-based with adult max caps
- [ ] Confirm age-appropriate normal values referenced

**Sign-off:** _________________________ Date: ___________

---

### Lateral Canthotomy and Cantholysis
**ID:** `lateral-canthotomy` | **Category:** procedural | **Status:** CLEAN
**Words:** 1852 | **Sources:** 5 | **Pitfalls:** 11 | **time_to_harm:** structured

**Category Checks:**
- equipment_list: PASS
- contraindications_listed: PASS
- complication_rates: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify equipment list is complete
- [ ] Confirm contraindications are listed
- [ ] Check procedural steps are in correct order

**Sign-off:** _________________________ Date: ___________

---

### Ludwig's Angina
**ID:** `ludwigs-angina` | **Category:** infectious | **Status:** CLEAN
**Words:** 1266 | **Sources:** 4 | **Pitfalls:** 9 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 2 hours"), not structured object — tier A SHOULD use object form

**Category Checks:**
- empiric_abx_timing: PASS
- cultures_before_abx: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify empiric antibiotic regimens match current guidelines
- [ ] Confirm timing targets for antibiotic administration
- [ ] Check source control recommendations

**Sign-off:** _________________________ Date: ___________

---

### Malignant Hyperthermia
**ID:** `malignant-hyperthermia` | **Category:** environmental | **Status:** CLEAN
**Words:** 1336 | **Sources:** 4 | **Pitfalls:** 9 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 30 minutes"), not structured object — tier A SHOULD use object form

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify temperature management targets
- [ ] Confirm rewarming/cooling protocols

**Sign-off:** _________________________ Date: ___________

---

### Mass Casualty Incident Triage and Management
**ID:** `mass-casualty-triage` | **Category:** disaster-mci | **Status:** CLEAN
**Words:** 1892 | **Sources:** 5 | **Pitfalls:** 11 | **time_to_harm:** structured

**Flags:**
- [INFO] `source_currency`: Oldest source year: 1996, newest: 2019 — no source from last 5 years

**Category Checks:**
- triage_algorithm: PASS
- resource_allocation: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify triage algorithm accuracy
- [ ] Confirm resource allocation criteria
- [ ] Check mass decontamination protocols if applicable

**Sign-off:** _________________________ Date: ___________

---

### Massive Hemoptysis
**ID:** `massive-hemoptysis` | **Category:** respiratory | **Status:** CLEAN
**Words:** 1545 | **Sources:** 5 | **Pitfalls:** 7 | **time_to_harm:** structured

**Flags:**
- [INFO] `source_currency`: Oldest source year: 2000, newest: 2020 — no source from last 5 years

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify airway management decision points
- [ ] Confirm ventilator settings if mentioned

**Sign-off:** _________________________ Date: ___________

---

### Massive Transfusion
**ID:** `massive-transfusion` | **Category:** hematologic | **Status:** CLEAN
**Words:** 1156 | **Sources:** 5 | **Pitfalls:** 10 | **time_to_harm:** string

**Flags:**
- [MINOR] `hedging_in_critical_actions`: Hedging phrase "if available" in Critical Actions: "...ial POC testing** — TEG/ROTEM if available to guide component therapy. Check ionized calcium..."
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 30 minutes"), not structured object — tier A SHOULD use object form

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy

**Sign-off:** _________________________ Date: ___________

---

### Acute Mesenteric Ischemia
**ID:** `mesenteric-ischemia` | **Category:** gastrointestinal | **Status:** CLEAN
**Words:** 1379 | **Sources:** 5 | **Pitfalls:** 10 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 2 hours"), not structured object — tier A SHOULD use object form

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy

**Sign-off:** _________________________ Date: ___________

---

### Necrotizing Enterocolitis
**ID:** `necrotizing-enterocolitis` | **Category:** pediatric | **Status:** CLEAN
**Words:** 1390 | **Sources:** 5 | **Pitfalls:** 7 | **time_to_harm:** structured

**Flags:**
- [MINOR] `dose_missing_route`: epinephrine 0.05-0.3 mcg/kg/min — no route (IV/IM/PO/etc) found nearby
- [INFO] `source_currency`: Oldest source year: 1978, newest: 2011 — no source from last 5 years

**Category Checks:**
- weight_based_dosing: PASS
- max_adult_dose: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify all doses are weight-based with adult max caps
- [ ] Confirm age-appropriate normal values referenced

**Sign-off:** _________________________ Date: ___________

---

### Necrotizing Fasciitis
**ID:** `necrotizing-fasciitis` | **Category:** infectious | **Status:** CLEAN
**Words:** 1446 | **Sources:** 4 | **Pitfalls:** 9 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 6 hours"), not structured object — tier A SHOULD use object form
- [INFO] `source_currency`: Oldest source year: 2004, newest: 2020 — no source from last 5 years

**Category Checks:**
- empiric_abx_timing: PASS
- cultures_before_abx: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify empiric antibiotic regimens match current guidelines
- [ ] Confirm timing targets for antibiotic administration
- [ ] Check source control recommendations

**Sign-off:** _________________________ Date: ___________

---

### Neonatal Emergencies
**ID:** `neonatal-emergencies` | **Category:** pediatric | **Status:** NEEDS_PHYSICIAN_REVIEW
**Words:** 2156 | **Sources:** 6 | **Pitfalls:** 10 | **time_to_harm:** string

**Flags:**
- [MINOR] `hedging_in_critical_actions`: Hedging phrase "if available" in Critical Actions: "...IV (or cefotaxime 50 mg/kg IV if available, in place of gentamicin). 7. Add acyclovir 20 mg/..."
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 1 hour"), not structured object — tier A SHOULD use object form
- [MAJOR] `dangerous_combination`: epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent

**Category Checks:**
- weight_based_dosing: PASS
- max_adult_dose: PASS

**Dangerous Combination Flags:**
- [MAJOR] epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify all doses are weight-based with adult max caps
- [ ] Confirm age-appropriate normal values referenced

**Sign-off:** _________________________ Date: ___________

---

### Neuroleptic Malignant Syndrome
**ID:** `neuroleptic-malignant-syndrome` | **Category:** psychiatric | **Status:** CLEAN
**Words:** 1863 | **Sources:** 5 | **Pitfalls:** 10 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 24 hours"), not structured object — tier A SHOULD use object form

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy

**Sign-off:** _________________________ Date: ___________

---

### Opioid Overdose
**ID:** `opioid-overdose` | **Category:** toxicologic | **Status:** CLEAN
**Words:** 1321 | **Sources:** 4 | **Pitfalls:** 9 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 5 minutes"), not structured object — tier A SHOULD use object form
- [MINOR] `mortality_not_quantified`: mortality_if_delayed has no numeric value: "Respiratory arrest within minutes if untreated"

**Category Checks:**
- antidote_dose_route: PASS
- max_dose_stated: PASS
- decontamination_timing: N/A

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify antidote dosing and routes are current
- [ ] Confirm decontamination timing windows
- [ ] Check for dangerous drug interactions

**Sign-off:** _________________________ Date: ___________

---

### Organophosphate Poisoning
**ID:** `organophosphate-poisoning` | **Category:** toxicologic | **Status:** CLEAN
**Words:** 1355 | **Sources:** 5 | **Pitfalls:** 9 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 30 minutes"), not structured object — tier A SHOULD use object form

**Category Checks:**
- antidote_dose_route: PASS
- max_dose_stated: PASS
- decontamination_timing: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify antidote dosing and routes are current
- [ ] Confirm decontamination timing windows
- [ ] Check for dangerous drug interactions

**Sign-off:** _________________________ Date: ___________

---

### Pelvic Fracture
**ID:** `pelvic-fracture` | **Category:** traumatic | **Status:** NEEDS_PHYSICIAN_REVIEW
**Words:** 2257 | **Sources:** 5 | **Pitfalls:** 10 | **time_to_harm:** string

**Flags:**
- [MINOR] `hedging_in_critical_actions`: Hedging phrase "if available" in Critical Actions: "...tive FAST: angioembolization (if available within 30-60 min) OR preperitoneal pelvic packing..."
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 30 minutes"), not structured object — tier A SHOULD use object form
- [INFO] `source_currency`: Oldest source year: 2006, newest: 2018 — no source from last 5 years
- [MAJOR] `dangerous_combination`: calcium chloride: must state 'central line only' or warn against peripheral administration

**Dangerous Combination Flags:**
- [MAJOR] calcium chloride: must state 'central line only' or warn against peripheral administration

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify hemorrhage control priorities
- [ ] Confirm transfusion thresholds

**Sign-off:** _________________________ Date: ___________

---

### Penetrating Chest Trauma
**ID:** `penetrating-chest-trauma` | **Category:** traumatic | **Status:** CLEAN
**Words:** 1809 | **Sources:** 5 | **Pitfalls:** 9 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 10 minutes"), not structured object — tier A SHOULD use object form
- [INFO] `source_currency`: Oldest source year: 2011, newest: 2018 — no source from last 5 years

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify hemorrhage control priorities
- [ ] Confirm transfusion thresholds

**Sign-off:** _________________________ Date: ___________

---

### Perimortem Cesarean Delivery
**ID:** `perimortem-cesarean-delivery` | **Category:** procedural | **Status:** CLEAN
**Words:** 1819 | **Sources:** 5 | **Pitfalls:** 12 | **time_to_harm:** structured

**Flags:**
- [INFO] `source_currency`: Oldest source year: 1986, newest: 2020 — no source from last 5 years

**Category Checks:**
- equipment_list: PASS
- contraindications_listed: PASS
- complication_rates: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify equipment list is complete
- [ ] Confirm contraindications are listed
- [ ] Check procedural steps are in correct order

**Sign-off:** _________________________ Date: ___________

---

### Pheochromocytoma / Catecholamine Crisis
**ID:** `pheochromocytoma-crisis` | **Category:** endocrine-metabolic | **Status:** CLEAN
**Words:** 1440 | **Sources:** 5 | **Pitfalls:** 7 | **time_to_harm:** structured

**Flags:**
- [INFO] `source_currency`: Oldest source year: 2007, newest: 2019 — no source from last 5 years

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy

**Sign-off:** _________________________ Date: ___________

---

### Placental Abruption
**ID:** `placental-abruption` | **Category:** obstetric-gynecologic | **Status:** CLEAN
**Words:** 1347 | **Sources:** 5 | **Pitfalls:** 9 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 30 minutes"), not structured object — tier A SHOULD use object form

**Category Checks:**
- mag_toxicity: N/A
- fetal_considerations: PASS
- gestational_cutoffs: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify magnesium sulfate dosing and toxicity thresholds
- [ ] Confirm gestational age cutoffs
- [ ] Check fetal monitoring recommendations

**Sign-off:** _________________________ Date: ___________

---

### Postpartum Hemorrhage
**ID:** `postpartum-hemorrhage` | **Category:** obstetric-gynecologic | **Status:** CLEAN
**Words:** 1606 | **Sources:** 6 | **Pitfalls:** 10 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 30 minutes"), not structured object — tier A SHOULD use object form

**Category Checks:**
- mag_toxicity: N/A
- fetal_considerations: PASS
- gestational_cutoffs: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify magnesium sulfate dosing and toxicity thresholds
- [ ] Confirm gestational age cutoffs
- [ ] Check fetal monitoring recommendations

**Sign-off:** _________________________ Date: ___________

---

### Pulmonary Embolism
**ID:** `pulmonary-embolism` | **Category:** respiratory | **Status:** CLEAN
**Words:** 1552 | **Sources:** 4 | **Pitfalls:** 7 | **time_to_harm:** string

**Flags:**
- [MINOR] `hedging_in_critical_actions`: Hedging phrase "if available" in Critical Actions: "...bolism Response Team (PERT)** if available..."
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 1 hour for massive PE"), not structured object — tier A SHOULD use object form
- [INFO] `source_currency`: Oldest source year: 2011, newest: 2019 — no source from last 5 years

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify airway management decision points
- [ ] Confirm ventilator settings if mentioned

**Sign-off:** _________________________ Date: ___________

---

### Radiation Mass Casualty Event
**ID:** `radiation-mass-casualty` | **Category:** disaster-mci | **Status:** CLEAN
**Words:** 2564 | **Sources:** 5 | **Pitfalls:** 12 | **time_to_harm:** structured

**Flags:**
- [INFO] `source_currency`: Oldest source year: 2001, newest: 2011 — no source from last 5 years

**Category Checks:**
- triage_algorithm: PASS
- resource_allocation: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify triage algorithm accuracy
- [ ] Confirm resource allocation criteria
- [ ] Check mass decontamination protocols if applicable

**Sign-off:** _________________________ Date: ___________

---

### Resuscitative Endovascular Balloon Occlusion of the Aorta
**ID:** `reboa` | **Category:** procedural | **Status:** CLEAN
**Words:** 2018 | **Sources:** 5 | **Pitfalls:** 11 | **time_to_harm:** structured

**Flags:**
- [INFO] `source_currency`: Oldest source year: 2011, newest: 2018 — no source from last 5 years
- [MINOR] `category_complication_rates`: Category check failed: Complication rates cited

**Category Checks:**
- equipment_list: PASS
- contraindications_listed: PASS
- complication_rates: **FAIL**

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify equipment list is complete
- [ ] Confirm contraindications are listed
- [ ] Check procedural steps are in correct order

**Sign-off:** _________________________ Date: ___________

---

### Resuscitative Thoracotomy
**ID:** `resuscitative-thoracotomy` | **Category:** procedural | **Status:** CLEAN
**Words:** 1719 | **Sources:** 5 | **Pitfalls:** 12 | **time_to_harm:** structured

**Flags:**
- [INFO] `source_currency`: Oldest source year: 2000, newest: 2018 — no source from last 5 years

**Category Checks:**
- equipment_list: PASS
- contraindications_listed: PASS
- complication_rates: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify equipment list is complete
- [ ] Confirm contraindications are listed
- [ ] Check procedural steps are in correct order

**Sign-off:** _________________________ Date: ___________

---

### Retrobulbar Hemorrhage (Orbital Compartment Syndrome)
**ID:** `retrobulbar-hemorrhage` | **Category:** ophthalmologic | **Status:** CLEAN
**Words:** 1610 | **Sources:** 5 | **Pitfalls:** 7 | **time_to_harm:** structured

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy

**Sign-off:** _________________________ Date: ___________

---

### Ruptured Abdominal Aortic Aneurysm
**ID:** `ruptured-aaa` | **Category:** cardiovascular | **Status:** CLEAN
**Words:** 1486 | **Sources:** 6 | **Pitfalls:** 10 | **time_to_harm:** string

**Flags:**
- [MINOR] `hedging_in_critical_actions`: Hedging phrase "Consider" in Critical Actions: "...introducer sheaths (cordis). Consider bilateral antecubital or femoral access. 3. **Typ..."
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 30 minutes"), not structured object — tier A SHOULD use object form

**Category Checks:**
- reperfusion_target: PASS
- anticoag_weight_based: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify reperfusion/intervention time targets are current
- [ ] Confirm anticoagulation weight-based dosing
- [ ] Check antiplatelet therapy matches current ACC/AHA

**Sign-off:** _________________________ Date: ___________

---

### Sepsis and Septic Shock
**ID:** `sepsis` | **Category:** infectious | **Status:** NEEDS_PHYSICIAN_REVIEW
**Words:** 1332 | **Sources:** 3 | **Pitfalls:** 7 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 1 hour"), not structured object — tier A SHOULD use object form
- [MAJOR] `dangerous_combination`: epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent

**Category Checks:**
- empiric_abx_timing: PASS
- cultures_before_abx: PASS

**Dangerous Combination Flags:**
- [MAJOR] epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify empiric antibiotic regimens match current guidelines
- [ ] Confirm timing targets for antibiotic administration
- [ ] Check source control recommendations

**Sign-off:** _________________________ Date: ___________

---

### Traumatic Spinal Cord Injury
**ID:** `spinal-cord-injury` | **Category:** traumatic | **Status:** CLEAN
**Words:** 2474 | **Sources:** 5 | **Pitfalls:** 10 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 60 minutes"), not structured object — tier A SHOULD use object form

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify hemorrhage control priorities
- [ ] Confirm transfusion thresholds

**Sign-off:** _________________________ Date: ___________

---

### Spontaneous Coronary Artery Dissection
**ID:** `spontaneous-coronary-artery-dissection` | **Category:** cardiovascular | **Status:** CLEAN
**Words:** 1642 | **Sources:** 5 | **Pitfalls:** 7 | **time_to_harm:** structured

**Flags:**
- [INFO] `source_currency`: Oldest source year: 2012, newest: 2018 — no source from last 5 years

**Category Checks:**
- reperfusion_target: PASS
- anticoag_weight_based: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify reperfusion/intervention time targets are current
- [ ] Confirm anticoagulation weight-based dosing
- [ ] Check antiplatelet therapy matches current ACC/AHA

**Sign-off:** _________________________ Date: ___________

---

### Status Epilepticus
**ID:** `status-epilepticus` | **Category:** neurological | **Status:** CLEAN
**Words:** 1627 | **Sources:** 5 | **Pitfalls:** 20 | **time_to_harm:** structured

**Flags:**
- [INFO] `source_currency`: Oldest source year: 2012, newest: 2020 — no source from last 5 years

**Category Checks:**
- seizure_dose_mg_kg: PASS
- herniation_signs: N/A

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify seizure medication dosing (mg/kg for second-line)
- [ ] Confirm herniation management protocols
- [ ] Check thrombolytic eligibility criteria

**Sign-off:** _________________________ Date: ___________

---

### ST-Elevation Myocardial Infarction
**ID:** `stemi` | **Category:** cardiovascular | **Status:** CLEAN
**Words:** 1335 | **Sources:** 3 | **Pitfalls:** 18 | **time_to_harm:** structured

**Flags:**
- [MINOR] `dose_missing_route`: aspirin 81 mg — no route (IV/IM/PO/etc) found nearby

**Category Checks:**
- reperfusion_target: PASS
- anticoag_weight_based: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify reperfusion/intervention time targets are current
- [ ] Confirm anticoagulation weight-based dosing
- [ ] Check antiplatelet therapy matches current ACC/AHA

**Sign-off:** _________________________ Date: ___________

---

### Subarachnoid Hemorrhage
**ID:** `subarachnoid-hemorrhage` | **Category:** neurological | **Status:** CLEAN
**Words:** 1409 | **Sources:** 4 | **Pitfalls:** 9 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 60 minutes"), not structured object — tier A SHOULD use object form
- [MINOR] `category_seizure_dose_mg_kg`: Category check failed: Seizure med dosing uses mg/kg for second-line

**Category Checks:**
- seizure_dose_mg_kg: **FAIL**
- herniation_signs: N/A

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify seizure medication dosing (mg/kg for second-line)
- [ ] Confirm herniation management protocols
- [ ] Check thrombolytic eligibility criteria

**Sign-off:** _________________________ Date: ___________

---

### Subdural Hematoma
**ID:** `subdural-hematoma` | **Category:** traumatic | **Status:** CLEAN
**Words:** 2545 | **Sources:** 5 | **Pitfalls:** 10 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 2 hours for acute SDH with herniation; days to weeks for chronic SDH"), not structured object — tier A SHOULD use object form

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify hemorrhage control priorities
- [ ] Confirm transfusion thresholds

**Sign-off:** _________________________ Date: ___________

---

### Submersion Injury
**ID:** `submersion-injury` | **Category:** environmental | **Status:** NEEDS_PHYSICIAN_REVIEW
**Words:** 1401 | **Sources:** 5 | **Pitfalls:** 9 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 5 minutes (irreversible anoxic brain injury)"), not structured object — tier A SHOULD use object form
- [MAJOR] `dangerous_combination`: epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent

**Dangerous Combination Flags:**
- [MAJOR] epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify temperature management targets
- [ ] Confirm rewarming/cooling protocols

**Sign-off:** _________________________ Date: ___________

---

### Surgical Cricothyrotomy
**ID:** `surgical-cricothyrotomy` | **Category:** procedural | **Status:** CLEAN
**Words:** 2015 | **Sources:** 5 | **Pitfalls:** 11 | **time_to_harm:** structured

**Flags:**
- [MINOR] `dose_missing_route`: propofol 5-50 mcg/kg/min — no route (IV/IM/PO/etc) found nearby
- [MINOR] `dose_missing_route`: fentanyl 25-100 mcg/hr — no route (IV/IM/PO/etc) found nearby

**Category Checks:**
- equipment_list: PASS
- contraindications_listed: PASS
- complication_rates: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify equipment list is complete
- [ ] Confirm contraindications are listed
- [ ] Check procedural steps are in correct order

**Sign-off:** _________________________ Date: ___________

---

### Tension Pneumothorax
**ID:** `tension-pneumothorax` | **Category:** respiratory | **Status:** CLEAN
**Words:** 1241 | **Sources:** 4 | **Pitfalls:** 17 | **time_to_harm:** structured

**Flags:**
- [MINOR] `hedging_in_critical_actions`: Hedging phrase "consider" in Critical Actions: "...rovement after decompression, consider wrong diagnosis, wrong side, catheter kink/obstru..."

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify airway management decision points
- [ ] Confirm ventilator settings if mentioned

**Sign-off:** _________________________ Date: ___________

---

### Thyroid Storm
**ID:** `thyroid-storm` | **Category:** endocrine-metabolic | **Status:** CLEAN
**Words:** 1312 | **Sources:** 4 | **Pitfalls:** 9 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 6 hours"), not structured object — tier A SHOULD use object form
- [INFO] `source_currency`: Oldest source year: 1993, newest: 2016 — no source from last 5 years

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy

**Sign-off:** _________________________ Date: ___________

---

### Toxic Alcohol Ingestion
**ID:** `toxic-alcohol-ingestion` | **Category:** toxicologic | **Status:** CLEAN
**Words:** 1947 | **Sources:** 5 | **Pitfalls:** 9 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 6-12 hours"), not structured object — tier A SHOULD use object form
- [INFO] `source_currency`: Oldest source year: 1999, newest: 2008 — no source from last 5 years
- [MINOR] `category_max_dose_stated`: Category check failed: Max dose stated or 'no maximum' explicitly

**Category Checks:**
- antidote_dose_route: PASS
- max_dose_stated: **FAIL**
- decontamination_timing: N/A

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify antidote dosing and routes are current
- [ ] Confirm decontamination timing windows
- [ ] Check for dangerous drug interactions

**Sign-off:** _________________________ Date: ___________

---

### Toxic Shock Syndrome
**ID:** `toxic-shock-syndrome` | **Category:** infectious | **Status:** CLEAN
**Words:** 1636 | **Sources:** 5 | **Pitfalls:** 7 | **time_to_harm:** structured

**Flags:**
- [INFO] `source_currency`: Oldest source year: 2000, newest: 2014 — no source from last 5 years

**Category Checks:**
- empiric_abx_timing: PASS
- cultures_before_abx: PASS

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify empiric antibiotic regimens match current guidelines
- [ ] Confirm timing targets for antibiotic administration
- [ ] Check source control recommendations

**Sign-off:** _________________________ Date: ___________

---

### Tracheobronchial Disruption
**ID:** `tracheal-disruption` | **Category:** respiratory | **Status:** CLEAN
**Words:** 1566 | **Sources:** 5 | **Pitfalls:** 7 | **time_to_harm:** structured

**Flags:**
- [MINOR] `hedging_in_critical_actions`: Hedging phrase "if possible" in Critical Actions: "...positive pressure ventilation if possible.** PPV forces air through the disruption, worseni..."
- [INFO] `source_currency`: Oldest source year: 1992, newest: 2014 — no source from last 5 years

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify airway management decision points
- [ ] Confirm ventilator settings if mentioned

**Sign-off:** _________________________ Date: ___________

---

### Traumatic Brain Injury
**ID:** `traumatic-brain-injury` | **Category:** traumatic | **Status:** CLEAN
**Words:** 1514 | **Sources:** 6 | **Pitfalls:** 10 | **time_to_harm:** string

**Flags:**
- [MINOR] `dose_missing_route`: norepinephrine 0.05-0.5 mcg/kg/min — no route (IV/IM/PO/etc) found nearby
- [MINOR] `dose_missing_route`: propofol 20-75 mcg/kg/min — no route (IV/IM/PO/etc) found nearby
- [MINOR] `dose_missing_route`: midazolam 0.05-0.2 mg/kg/hr — no route (IV/IM/PO/etc) found nearby
- [MINOR] `dose_missing_route`: fentanyl 1-2 mcg/kg/hr — no route (IV/IM/PO/etc) found nearby
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 60 minutes"), not structured object — tier A SHOULD use object form
- [INFO] `source_currency`: Oldest source year: 2001, newest: 2018 — no source from last 5 years

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify hemorrhage control priorities
- [ ] Confirm transfusion thresholds

**Sign-off:** _________________________ Date: ___________

---

### Unstable Bradycardia
**ID:** `unstable-bradycardia` | **Category:** cardiovascular | **Status:** NEEDS_PHYSICIAN_REVIEW
**Words:** 1658 | **Sources:** 5 | **Pitfalls:** 10 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 10 minutes"), not structured object — tier A SHOULD use object form
- [MINOR] `mortality_not_quantified`: mortality_if_delayed has no numeric value: "Cardiac arrest imminent if perfusing rhythm not restored"
- [INFO] `source_currency`: Oldest source year: 2015, newest: 2020 — no source from last 5 years
- [MAJOR] `dangerous_combination`: epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent

**Category Checks:**
- reperfusion_target: PASS
- anticoag_weight_based: N/A

**Dangerous Combination Flags:**
- [MAJOR] epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify reperfusion/intervention time targets are current
- [ ] Confirm anticoagulation weight-based dosing
- [ ] Check antiplatelet therapy matches current ACC/AHA

**Sign-off:** _________________________ Date: ___________

---

### Uterine Rupture
**ID:** `uterine-rupture` | **Category:** obstetric-gynecologic | **Status:** CLEAN
**Words:** 1604 | **Sources:** 6 | **Pitfalls:** 7 | **time_to_harm:** structured

**Category Checks:**
- mag_toxicity: N/A
- fetal_considerations: PASS
- gestational_cutoffs: N/A

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify magnesium sulfate dosing and toxicity thresholds
- [ ] Confirm gestational age cutoffs
- [ ] Check fetal monitoring recommendations

**Sign-off:** _________________________ Date: ___________

---

### Ventricular Tachycardia
**ID:** `ventricular-tachycardia` | **Category:** cardiovascular | **Status:** NEEDS_PHYSICIAN_REVIEW
**Words:** 1573 | **Sources:** 6 | **Pitfalls:** 10 | **time_to_harm:** string

**Flags:**
- [MINOR] `time_to_harm_not_structured`: time_to_harm is a string ("< 5 minutes"), not structured object — tier A SHOULD use object form
- [MINOR] `mortality_not_quantified`: mortality_if_delayed has no numeric value: "Pulseless VT degenerates to VF and death within minutes without defibrillation"
- [INFO] `source_currency`: Oldest source year: 1991, newest: 2020 — no source from last 5 years
- [MAJOR] `dangerous_combination`: epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent

**Category Checks:**
- reperfusion_target: PASS
- anticoag_weight_based: PASS

**Dangerous Combination Flags:**
- [MAJOR] epinephrine concentration: epinephrine concentration must specify 1:1,000 (IM) vs 1:10,000 (IV) or mg/mL equivalent

**Physician Checklist:**
- [ ] Verify all drug doses match current guidelines
- [ ] Confirm Critical Actions are complete and time-targeted
- [ ] Check pitfalls for clinical accuracy
- [ ] Verify reperfusion/intervention time targets are current
- [ ] Confirm anticoagulation weight-based dosing
- [ ] Check antiplatelet therapy matches current ACC/AHA

**Sign-off:** _________________________ Date: ___________

---
