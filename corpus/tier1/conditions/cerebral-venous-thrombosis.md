---
id: cerebral-venous-thrombosis
condition: Cerebral Venous Thrombosis
aliases: [CVT, cerebral venous sinus thrombosis, CVST, dural sinus thrombosis]
icd10: [I67.6, I63.6]
esi: 2
time_to_harm:
  irreversible_injury: "< 24 hours"
  death: "< 72 hours"
  optimal_intervention_window: "< 24 hours"
category: neurological
track: tier1
sources:
  - type: guideline
    ref: "Silvis SM et al. Diagnosis and Management of Cerebral Venous Thrombosis: A Scientific Statement From the American Heart Association. Stroke. 2024;55:e54-e76"
  - type: guideline
    ref: "Ferro JM et al. European Stroke Organization guideline for the diagnosis and treatment of cerebral venous thrombosis. Eur J Neurol. 2017;24(10):1203-1213"
  - type: guideline
    ref: "Saposnik G et al. Diagnosis and management of cerebral venous thrombosis: a statement for healthcare professionals from the AHA/ASA. Stroke. 2011;42(4):1158-1192"
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
# Cerebral Venous Thrombosis (CVT)

## Recognition

**Clinical presentation (highly variable — high index of suspicion required):**
- Headache (>90%): progressive, severe, often worst headache of life; may mimic SAH
- Seizures (40%): focal or generalized; can be presenting feature
- Focal neurologic deficits (40-60%): hemiparesis, aphasia, cranial nerve palsies
- Papilledema and visual changes from raised ICP
- Altered mental status or coma in severe cases
- Isolated intracranial hypertension (headache + papilledema without focal deficits)

**High-risk populations:**
- Women of reproductive age (oral contraceptives, pregnancy, puerperium)
- Prothrombotic states: Factor V Leiden, prothrombin gene mutation, antiphospholipid syndrome, protein C/S deficiency
- Infection: mastoiditis, sinusitis, meningitis (septic CVT)
- Malignancy, dehydration, recent surgery, head trauma

**Key diagnostic features:**
- CT may be normal in 30%; "dense triangle sign" (hyperdense sinus) or "empty delta sign" (on contrast CT) are classic but insensitive
- MRI/MRV or CT venography is required for diagnosis
- D-dimer: sensitive but not specific; negative D-dimer has good NPV in low-probability cases

## Critical Actions

1. **Emergent CT head** — identify hemorrhagic infarction (present in 30-40%) or mass effect
2. **CT venography (CTV) or MRI/MRV** — confirmatory imaging; CTV more accessible in ED
3. **Start anticoagulation with heparin** — UFH IV or LMWH SQ even in the presence of hemorrhagic infarction (this is counterintuitive but supported by evidence)
4. **Seizure management** — lorazepam 4 mg IV for active seizures; levetiracetam 1000-1500 mg IV loading for prophylaxis in patients with supratentorial lesions
5. **Manage raised ICP** — elevate HOB 30 degrees; acetazolamide 250-500 mg PO/IV BID; emergent neurosurgery for herniation
6. **Neurology and neurosurgery consultation**

## Differential Diagnosis

- Subarachnoid hemorrhage (thunderclap headache, positive LP or CTA)
- Acute ischemic stroke (arterial territory distribution; CTA shows arterial occlusion)
- Intracerebral hemorrhage (non-venous distribution)
- Idiopathic intracranial hypertension (similar presentation; no sinus thrombosis on imaging)
- Brain tumor (subacute, mass effect on imaging)
- Meningitis/encephalitis (fever, meningismus, CSF pleocytosis)
- Preeclampsia/eclampsia (pregnancy, hypertension, proteinuria)
- PRES (posterior predominant edema on MRI, hypertension)

## Workup

- **CT head without contrast** — initial; may show hemorrhagic infarction, dense sinus sign
- **CT venography** — first-line confirmatory test in ED (sensitivity >95%)
- **MRI brain + MR venography** — gold standard; better for parenchymal characterization
- **D-dimer** — negative D-dimer helps exclude CVT in low-probability cases; elevated in most CVT
- **CBC, BMP, PT/INR, PTT, fibrinogen**
- **Thrombophilia workup** (defer to inpatient, not in acute phase): Factor V Leiden, prothrombin 20210A, protein C/S, antithrombin III, antiphospholipid antibodies
- **LP** — only if meningitis suspected; opening pressure often elevated; defer if mass effect
- **Blood cultures** if septic CVT suspected
- **Pregnancy test** in women of reproductive age

## Treatment

### Anticoagulation (Mainstay)
- **UFH** IV: bolus 80 units/kg, then 18 units/kg/hr; target aPTT 1.5-2.5x control (preferred if surgery may be needed or large hemorrhage)
- **Enoxaparin** 1 mg/kg SQ q12h (preferred by European guidelines for non-surgical patients)
- Anticoagulate EVEN with hemorrhagic infarction — the hemorrhage is venous, not arterial; anticoagulation prevents propagation and improves outcomes
- Transition to warfarin (target INR 2-3) or DOAC for 3-12 months depending on etiology

### Oral Anticoagulation (Maintenance)
- Transient risk factor (OCP, pregnancy): 3-6 months
- Unprovoked or thrombophilia: 6-12 months or indefinite
- DOACs (dabigatran 150 mg PO BID or rivaroxaban 20 mg PO daily) — reasonable alternative to warfarin per 2024 AHA statement

### Seizure Management
- Active seizures: lorazepam 4 mg IV, may repeat x1
- Antiepileptic prophylaxis for supratentorial lesions: levetiracetam 500-1500 mg IV/PO BID
- Avoid phenytoin (enzyme inducer, reduces anticoagulant effectiveness)

### ICP Management
- Elevate HOB 30 degrees
- Acetazolamide 250-500 mg PO/IV BID (reduces CSF production)
- LP with CSF drainage for refractory elevated ICP (therapeutic)
- Decompressive craniectomy for malignant CVT with herniation — life-saving
- Endovascular thrombectomy for severe CVT failing medical therapy (emerging evidence)

## Disposition

- **All CVT patients:** inpatient admission, minimum neurology consultation
- **Hemorrhagic CVT, seizures, altered mental status:** ICU or neuro-ICU
- **Severe CVT with herniation risk:** neurosurgical ICU
- **Mild CVT (isolated headache, no hemorrhage, no seizures):** general neurology ward with telemetry

## Pitfalls

1. **Missing CVT because CT head is "normal."** Non-contrast CT is normal in 30% of CVT. Any unexplained progressive headache — especially in young women on OCPs — requires CTV or MRV.

2. **Withholding anticoagulation because of hemorrhagic infarction.** This is a critical error. Venous hemorrhagic infarction is caused by venous congestion; anticoagulation treats the underlying cause and is recommended even with hemorrhage.

3. **Attributing symptoms to migraine or tension headache.** Progressive headache with papilledema, seizures, or focal deficits should trigger CVT workup. "New worst headache" in a young woman on contraceptives is CVT until proven otherwise.

4. **Failing to check D-dimer in low-probability cases.** A normal D-dimer has good negative predictive value for CVT and can help exclude the diagnosis in low-risk patients. However, D-dimer can be falsely negative in isolated headache presentations.

5. **Using phenytoin for seizure prophylaxis.** Phenytoin is a cytochrome P450 inducer that reduces the effectiveness of warfarin and DOACs. Levetiracetam is preferred.
