---
id: spontaneous-coronary-artery-dissection
condition: Spontaneous Coronary Artery Dissection
aliases: [SCAD, coronary artery dissection, spontaneous coronary dissection]
icd10: [I25.42]
esi: 1
time_to_harm:
  irreversible_injury: "< 2 hours (myocardial necrosis)"
  death: "< 6 hours without recognition"
  optimal_intervention_window: "< 90 minutes (STEMI protocol)"
mortality_if_delayed: "In-hospital mortality 1-5%; sudden cardiac death in 2-4% as presenting event"
category: cardiovascular
track: tier1
sources:
  - type: guideline
    ref: "Hayes SN, Kim ESH, Saw J, et al. Spontaneous Coronary Artery Dissection: Current State of the Science: A Scientific Statement From the American Heart Association. Circulation. 2018;137(19):e523-e557."
    pmid: "29472380"
  - type: pubmed
    ref: "Saw J, Humphries K, Aymong E, et al. Spontaneous Coronary Artery Dissection: Clinical Outcomes and Risk of Recurrence. J Am Coll Cardiol. 2017;70(9):1148-1158."
    pmid: "28838364"
  - type: pubmed
    ref: "Tweet MS, Hayes SN, Pitta SR, et al. Clinical features, management, and prognosis of spontaneous coronary artery dissection. Circulation. 2012;126(5):579-588."
    pmid: "22800851"
  - type: pubmed
    ref: "Saw J, Mancini GBJ, Humphries KH. Contemporary review on spontaneous coronary artery dissection. J Am Coll Cardiol. 2016;68(3):297-312."
    pmid: "27417009"
  - type: pubmed
    ref: "Adlam D, Alfonso F, Maas A, Vrints C; Writing Committee. European Society of Cardiology, acute cardiovascular care association, SCAD study group: a position paper on spontaneous coronary artery dissection. Eur Heart J. 2018;39(36):3353-3368."
    pmid: "29481627"
confusion_pairs:
  - condition: stemi
    differentiators:
      - "SCAD: young female (median age 44-53), often without traditional cardiovascular risk factors (no diabetes, no dyslipidemia, no smoking)"
      - "SCAD: peripartum or postpartum timing (pregnancy-associated SCAD in 5-10%); physical or emotional stress precipitant"
      - "SCAD: history of fibromuscular dysplasia (FMD, present in 25-86%), connective tissue disorders, or systemic arteriopathy"
      - "Atherosclerotic ACS: older patients with traditional risk factors; coronary angiography shows plaque rupture with thrombus; SCAD shows intramural hematoma or intimal flap without atherosclerotic plaque"
  - condition: takotsubo-cardiomyopathy
    differentiators:
      - "SCAD: troponin elevation follows coronary distribution; angiography shows dissection flap or intramural hematoma"
      - "Takotsubo: apical ballooning on echo/ventriculography not following single coronary territory; coronary angiography is normal; emotional trigger common"
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
# Spontaneous Coronary Artery Dissection

## Recognition

**Definition:** Non-atherosclerotic, non-traumatic, non-iatrogenic separation of the coronary artery wall by intramural hemorrhage or intimal tear, causing luminal compromise and myocardial ischemia. Distinct from atherosclerotic plaque rupture and iatrogenic dissection during PCI.

**Epidemiology:**
- Accounts for 1-4% of all ACS presentations
- Most common cause of MI in women <50 years old (up to 35% of MI in this population)
- Female predominance: 90-95% female
- Median age: 44-53 years
- Peripartum SCAD: 5-10% of all SCAD cases (highest risk in third trimester and first weeks postpartum)

**Associated conditions:**
- **Fibromuscular dysplasia (FMD):** Present in 25-86% of SCAD patients when systematically screened. Most commonly renal and iliac arteries.
- **Connective tissue disorders:** Marfan syndrome, Ehlers-Danlos type IV, Loeys-Dietz syndrome
- **Pregnancy/postpartum:** Hormonal and hemodynamic changes weaken arterial wall
- **Systemic inflammatory conditions:** SLE, polyarteritis nodosa, sarcoidosis, IBD
- **Hormonal therapy:** Oral contraceptives, fertility treatments, hormone replacement

**Precipitants:**
- Intense physical exertion (isometric exercise, Valsalva, heavy lifting)
- Intense emotional stress
- Labor and delivery
- Recreational drug use (cocaine, amphetamines)
- Retching/vomiting
- Coughing paroxysms

**Presentation:** Indistinguishable from atherosclerotic ACS at the bedside.
- Acute chest pain (96%) — typical or atypical
- STEMI pattern on ECG (26-87%)
- NSTEMI pattern (13-74%)
- Cardiogenic shock (2-5%)
- Ventricular arrhythmia/sudden cardiac death (2-4%)

**Coronary angiography classification (Saw classification):**

| Type | Description | Frequency |
|------|-------------|-----------|
| Type 1 | Multiple radiolucent lumen with contrast staining of arterial wall (pathognomonic) | 29-48% |
| Type 2a | Diffuse narrowing (>20 mm) with abrupt caliber change returning to normal | Most common |
| Type 2b | Diffuse narrowing extending to distal tip of artery | Common |
| Type 3 | Focal or tubular stenosis mimicking atherosclerosis (requires intravascular imaging — IVUS or OCT) | 3.9% |

**Affected vessels:**
- LAD: 32-46% (most common)
- LCx: 18-25%
- RCA: 12-23%
- Left main: 1-4% (high mortality)
- Multivessel: 9-23%

## Critical Actions

1. **Treat as ACS until angiography differentiates.** Standard ACS protocol applies: ECG within 10 minutes, troponin, aspirin, anticoagulation, cardiology consultation, cath lab activation for STEMI.
2. **Activate the cath lab for STEMI presentation.** Door-to-balloon target <90 minutes applies regardless of suspected etiology. SCAD diagnosis is made during coronary angiography, not before.
3. **Aspirin 325 mg PO (chewed) immediately** — standard for all ACS presentations.
4. **Heparin 60 units/kg IV bolus (max 4000 units) then 12 units/kg/hr (max 1000 units/hr)** — standard ACS anticoagulation.
5. **Hold P2Y12 inhibitor (clopidogrel, ticagrelor, prasugrel) until angiographic diagnosis is confirmed.** If SCAD is identified, P2Y12 inhibitors are NOT standard therapy (no atherosclerotic plaque to stabilize; antiplatelet agents may extend intramural hematoma).
6. **If SCAD confirmed on angiography: conservative management is first-line** for stable patients with TIMI 2-3 flow. Avoid PCI unless ongoing ischemia, hemodynamic instability, or left main involvement.
7. **Consult interventional cardiology urgently** — SCAD-specific management decisions (conservative vs. PCI vs. CABG) require subspecialist expertise.
8. **Screen for FMD.** CT angiography or MR angiography from head to pelvis within index hospitalization.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Atherosclerotic ACS (STEMI/NSTEMI) | Older patients; traditional risk factors (HTN, DM, hyperlipidemia, smoking, family history); angiography shows plaque rupture/erosion with thrombus; calcified vessels |
| Takotsubo cardiomyopathy | Apical ballooning on echo not following single coronary territory; normal coronary angiography; emotional precipitant; transient ST elevation; troponin elevation modest relative to wall motion abnormality |
| Myocarditis | Viral prodrome; diffuse ST changes (not single territory); troponin elevation; cardiac MRI shows subepicardial/mid-wall late gadolinium enhancement; normal coronary angiography |
| Coronary vasospasm (Prinzmetal) | Transient ST elevation resolving with nitroglycerin; normal angiography (or provoked spasm with acetylcholine/ergonovine); no intramural hematoma |
| Aortic dissection with coronary extension | Tearing chest/back pain; pulse deficits; widened mediastinum on CXR; CT shows aortic dissection flap extending into coronary ostium (usually RCA) |
| Pulmonary embolism | Dyspnea predominant; S1Q3T3 or right heart strain on ECG; CTA shows filling defect; troponin elevation from RV strain |
| Coronary artery embolism | Atrial fibrillation, prosthetic valve, or endocarditis; abrupt vessel cutoff on angiography without dissection plane; no intramural hematoma |

## Workup

**Emergent (standard ACS workup — SCAD diagnosis comes from cath lab):**
- ECG within 10 minutes — STEMI or NSTEMI pattern
- Troponin — elevated (serial measurement q3-6h)
- BMP — baseline renal function before contrast
- CBC, coagulation studies — baseline
- BNP/NT-proBNP — assess LV function
- Urine pregnancy test — all women of reproductive age (pregnancy-associated SCAD)

**Coronary angiography (diagnostic gold standard):**
- Identifies dissection plane, intramural hematoma, or false lumen
- Saw Type 1 is pathognomonic; Types 2-3 may require intravascular imaging (OCT or IVUS) for definitive diagnosis
- AVOID aggressive catheter manipulation — iatrogenic extension of dissection
- Avoid nitroglycerin challenge (does not resolve SCAD narrowing; helps differentiate from vasospasm)

**Intravascular imaging (when available):**
- **OCT (optical coherence tomography):** Superior resolution for intimal flap, intramural hematoma, false lumen. Preferred over IVUS.
- **IVUS (intravascular ultrasound):** Alternative when OCT unavailable. Identifies intramural hematoma.
- Risk: catheter advancement may propagate dissection. Use selectively when angiographic diagnosis is uncertain.

**Echocardiography:**
- Bedside TTE — assess LV function, regional wall motion abnormalities, rule out mechanical complications (MR, VSD)
- Reduced LVEF in 22-58% at presentation

**Vascular screening for FMD (during index hospitalization or shortly after):**
- CTA or MRA from head to pelvis (carotid, renal, iliac arteries)
- FMD identified in 25-86% — changes long-term surveillance and management

## Treatment

**Conservative management (first-line for majority of SCAD):**
- Indicated when: TIMI 2-3 flow in affected vessel, hemodynamically stable, no ongoing ischemia, single-vessel non-left-main disease
- Coronary artery heals spontaneously in >95% of conservatively managed cases on follow-up angiography
- Angiographic healing typically occurs within 30 days

**Medical therapy:**
- **Aspirin 81 mg PO daily** — long-term (expert consensus; no RCT data)
- **Beta-blocker:** Metoprolol succinate 25-50 mg PO daily, titrate to HR 55-65 bpm. Reduces arterial wall stress. Recommended by AHA scientific statement as standard therapy.
- **ACE inhibitor or ARB:** Lisinopril 2.5-5 mg PO daily (titrate to 10-20 mg daily) for LVEF <40%. Standard HF therapy if indicated.
- **Statin:** NOT routinely indicated (no atherosclerotic disease to treat). Use only if concurrent dyslipidemia exists.
- **P2Y12 inhibitor:** NOT standard therapy. Expert consensus varies — some prescribe for 1-12 months post-SCAD; others avoid entirely. Potential risk of extending intramural hematoma.
- **Anticoagulation:** Discontinue heparin once SCAD diagnosis confirmed and conservative management selected. No role for long-term anticoagulation unless other indication (e.g., LV thrombus, DVT).

**PCI (reserved for specific indications):**
- Ongoing ischemia despite medical therapy
- Hemodynamic instability
- Left main dissection
- TIMI 0-1 flow in a large territory
- Technical challenges: high failure rate (35-53%) due to propagation of dissection by wire/balloon. Drug-eluting stent preferred; cover the entire dissection length.

**CABG (last resort):**
- Multivessel SCAD with ongoing ischemia
- Failed PCI
- Left main SCAD with hemodynamic compromise
- Technically challenging: target vessels may be diffusely diseased; graft failure higher than in atherosclerotic disease

**Cardiac rehabilitation:**
- SCAD-specific program recommended (standard cardiac rehab protocols may be too aggressive)
- Avoid isometric exercise, Valsalva, and extreme physical exertion long-term
- Graduated return to activity over 3-6 months

## Disposition

**CCU/cardiac ICU:**
- STEMI presentation
- Hemodynamic instability or cardiogenic shock
- LVEF <35%
- Left main or multivessel SCAD
- Ventricular arrhythmia
- Post-PCI or post-CABG

**Telemetry/step-down:**
- Stable NSTEMI with TIMI 2-3 flow on conservative management
- Normal or mildly reduced LVEF
- No ongoing chest pain

**Minimum hospitalization: 3-5 days.** SCAD extension/recurrence risk is highest in the first 72 hours. Serial troponins, telemetry monitoring, and repeat echocardiography before discharge.

**Discharge planning:**
- Cardiology follow-up within 1-2 weeks
- Repeat coronary angiography at 3-6 months (assess healing)
- Vascular screening for FMD if not completed inpatient
- Genetic counseling if connective tissue disorder suspected
- Avoid pregnancy counseling (recurrence risk 10-20% in subsequent pregnancies)
- Psychological support — SCAD patients have high rates of anxiety and PTSD

**Recurrence:** 10-30% lifetime recurrence rate. Median time to recurrence: 2.3 years. Hypertension is the only modifiable risk factor associated with recurrence.

## Pitfalls

1. **Dismissing ACS in a young woman without traditional risk factors.** SCAD is the leading cause of MI in women <50. A 35-year-old postpartum woman with chest pain and ST elevation has a STEMI until coronary angiography proves otherwise. Age and risk factor profile do not exclude ACS.

2. **Aggressive PCI when conservative management is indicated.** PCI has a 35-53% technical failure rate in SCAD due to wire-induced dissection propagation and difficulty identifying the true lumen. Stable patients with TIMI 2-3 flow should be managed conservatively. Premature intervention worsens outcomes.

3. **Administering P2Y12 inhibitors reflexively before cath.** Standard ACS protocols call for dual antiplatelet therapy. In SCAD, P2Y12 inhibitors may extend the intramural hematoma. Hold P2Y12 inhibitor until angiographic diagnosis confirms or excludes SCAD.

4. **Not screening for fibromuscular dysplasia.** FMD is present in 25-86% of SCAD patients and involves other vascular beds (renal, carotid, iliac). Undiagnosed renal FMD causes secondary hypertension (the only modifiable recurrence risk factor). Head-to-pelvis vascular imaging is indicated during or shortly after the index hospitalization.

5. **Prescribing statins reflexively.** SCAD is not an atherosclerotic disease. Statins have no role unless the patient has an independent indication for lipid-lowering therapy. Prescribing statins implies atherosclerotic etiology and may delay recognition of the underlying arteriopathy.

6. **Discharging before 72 hours.** The highest risk period for SCAD extension and recurrence is the first 72 hours. Early discharge misses evolving dissection, troponin re-elevation, and mechanical complications. Minimum 3-5 day hospitalization with serial troponins and repeat echo before discharge.

7. **Failing to address pregnancy counseling.** Recurrence risk is 10-20% in subsequent pregnancies. Patients must be informed of this risk during the index hospitalization, with referral to maternal-fetal medicine and cardiology for shared decision-making before any future pregnancy.
