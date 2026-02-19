---
id: thyroid-storm
condition: Thyroid Storm
aliases: [thyrotoxic crisis, thyrotoxic storm, decompensated thyrotoxicosis, accelerated hyperthyroidism]
icd10: [E05.01, E05.11, E05.21, E05.81, E05.91]
esi: 1
time_to_harm: "< 6 hours"
mortality_if_delayed: "10-30% mortality even with treatment; > 50% untreated"
category: endocrine-metabolic
track: tier1
sources:
  - type: guideline
    ref: "Ross DS et al. 2016 American Thyroid Association Guidelines for Diagnosis and Management of Hyperthyroidism. Thyroid 2016;26:1343-1421"
    pmid: "27521067"
  - type: pubmed
    ref: "Burch HB, Wartofsky L. Life-Threatening Thyrotoxicosis: Thyroid Storm. Endocrinol Metab Clin North Am 1993;22:263-277"
    pmid: "8325286"
  - type: pubmed
    ref: "Akamizu T et al. Diagnostic Criteria, Clinical Features, and Incidence of Thyroid Storm Based on Nationwide Surveys. Thyroid 2012;22:661-679"
    pmid: "22690898"
  - type: pubmed
    ref: "Chiha M et al. Thyroid Storm: An Updated Review. J Intensive Care Med 2015;30:131-140"
    pmid: "23920160"
last_updated: "2026-02-18"
compiled_by: agent
risk_tier: A
validation:
  automated_consistency_check: "2026-02-18"
  dose_range_validator: "2026-02-19"
  unit_normalization_check: "2026-02-19"
  cross_file_consistency_check: "2026-02-19"
  citation_presence_check: "2026-02-19"
  duplicate_content_check: "2026-02-19"
  outlier_detection_flag: clear
  schema_version: "2.0"
  guideline_version_reference: null
  provenance_links: []
---
# Thyroid Storm

## Recognition

**Definition:** Life-threatening decompensation of thyrotoxicosis with multiorgan dysfunction. A clinical diagnosis — thyroid hormone levels do not distinguish thyroid storm from uncomplicated thyrotoxicosis.

**Burch-Wartofsky Point Scale (BWPS):** Score >= 45 highly suggestive, 25-44 impending storm, < 25 unlikely.
- Temperature: 37.2-37.7 (5 pts), 37.8-38.2 (10), 38.3-38.8 (15), 38.9-39.3 (20), 39.4-39.9 (25), >= 40 (30)
- CNS effects: mild agitation (10), moderate (delirium, psychosis, extreme lethargy) (20), severe (seizure, coma) (30)
- GI-hepatic: moderate (diarrhea, nausea/vomiting, abdominal pain) (10), severe (unexplained jaundice) (20)
- Heart rate: 99-109 (5), 110-119 (10), 120-129 (15), 130-139 (20), >= 140 (25)
- Heart failure: mild (pedal edema) (5), moderate (bibasilar rales) (10), severe (pulmonary edema) (15)
- Atrial fibrillation: present (10)
- Precipitant: present (10)

**Clinical Features:**
- Fever > 40°C (104°F) — disproportionate to any identified infection
- Tachycardia out of proportion (HR 140-200+), atrial fibrillation (present in 10-35%)
- Severe agitation, psychosis, delirium, seizures, coma
- High-output heart failure, pulmonary edema
- Nausea, vomiting, diarrhea, jaundice (ominous)
- Diaphoresis, tremor, lid lag, exophthalmos (Graves' disease)

**Precipitants:**
- Infection (most common)
- Surgery (especially thyroid surgery in unprepared patient)
- Iodinated contrast dye
- Discontinuation of antithyroid drugs
- DKA, trauma, pregnancy/labor, pulmonary embolism
- Amiodarone initiation

## Critical Actions

1. **Propranolol 60-80 mg PO q4-6h** (or propranolol 0.5-1 mg IV over 10 min, repeat q15 min to max 10 mg) — controls adrenergic symptoms AND blocks peripheral T4-to-T3 conversion. Preferred over cardioselective beta-blockers. For severe heart failure or asthma: esmolol 250-500 mcg/kg IV bolus then 50-100 mcg/kg/min infusion.
2. **Propylthiouracil (PTU) 500-1000 mg PO/NG loading dose, then 250 mg PO q4h** — blocks new hormone synthesis AND peripheral T4-to-T3 conversion. Preferred over methimazole in thyroid storm for the latter property.
3. **Iodine (SSKI 5 drops PO q6h or Lugol's solution 8 drops PO q6h)** — blocks thyroid hormone release (Wolff-Chaikoff effect). MUST be given at least 1 hour AFTER first PTU dose to prevent iodine being used as substrate for new hormone synthesis.
4. **Hydrocortisone 100 mg IV q8h** — blocks T4-to-T3 conversion, treats possible coexistent adrenal insufficiency, prevents relative adrenal insufficiency from hypermetabolic state.
5. **Aggressive cooling** — acetaminophen 1000 mg IV/PO. External cooling (ice packs, cooling blankets). Do NOT use aspirin (displaces thyroid hormone from binding proteins, increasing free hormone).
6. **Treat precipitant** — infection workup, blood cultures, empiric antibiotics if sepsis suspected.
7. **Supportive care** — aggressive IV fluid resuscitation (high insensible losses from fever/tachycardia), correct electrolytes, dextrose-containing fluids for increased metabolic demand.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Sepsis/septic shock | Fever, tachycardia, hypotension overlap; obtain TSH/free T4 in septic patients not responding to standard therapy. Can be the precipitant of thyroid storm. |
| Sympathomimetic toxicity (cocaine, amphetamines) | Tachycardia, hyperthermia, agitation; UDS positive, no goiter, no eye findings |
| Neuroleptic malignant syndrome | Rigidity (lead-pipe), hyperthermia, recent antipsychotic use, elevated CK |
| Serotonin syndrome | Clonus, hyperreflexia, diarrhea; recent serotonergic medication change |
| Malignant hyperthermia | Perioperative, volatile anesthetic exposure, extreme rigidity, markedly elevated CK |
| Pheochromocytoma crisis | Paroxysmal hypertension (not typically present in thyroid storm), headache, diaphoresis, elevated catecholamines/metanephrines |
| Heat stroke | Environmental exposure, altered mental status, anhidrosis (classic heat stroke) |
| Delirium tremens | Alcohol withdrawal history, visual hallucinations, tremor, autonomic instability |

## Workup

**Labs:**
- TSH — suppressed (< 0.01 mIU/L); normal TSH effectively excludes thyroid storm
- Free T4, free T3, total T3 — elevated, but levels do not correlate with storm severity
- CBC — leukocytosis (stress response or infection)
- CMP — hyperglycemia (catecholamine-mediated), elevated AST/ALT and bilirubin (hepatic dysfunction — poor prognostic sign), hypercalcemia, elevated alkaline phosphatase
- Cortisol — rule out concurrent adrenal insufficiency
- Lactate — elevated in shock
- CK — mildly elevated from hypermetabolic state
- Coagulation studies — DIC screening
- Blood cultures — infection is most common precipitant
- UA, CXR — infection source

**ECG:**
- Sinus tachycardia, atrial fibrillation (10-35%), atrial flutter
- ST changes from demand ischemia
- Shortened QT interval

**Imaging:**
- CXR — pulmonary edema, infection
- CT head — if altered mental status, seizure (rule out structural cause)

## Treatment

**Treatment Order Matters — Sequential Blockade:**

**Step 1: Beta-Blockade**
- Propranolol 60-80 mg PO q4-6h (preferred — inhibits T4-to-T3 conversion)
- IV alternative: propranolol 0.5-1 mg IV over 10 min
- Esmolol infusion 50-100 mcg/kg/min if IV required or severe heart failure concern (short half-life, titratable)
- Diltiazem 120-360 mg/day PO or 0.25 mg/kg IV if beta-blockers contraindicated

**Step 2: Thionamide (block new hormone synthesis)**
- PTU 500-1000 mg PO/NG load, then 250 mg PO q4h
- Alternative: methimazole 20-25 mg PO q6h (lacks peripheral conversion blockade)
- PTU preferred in thyroid storm, pregnancy first trimester

**Step 3: Iodine (block hormone release) — MINIMUM 1 HOUR after thionamide**
- SSKI 5 drops (250 mg) PO q6h
- Lugol's solution 8 drops PO q6h
- Lithium carbonate 300 mg PO q8h if iodine allergy (blocks hormone release via different mechanism)

**Step 4: Glucocorticoid**
- Hydrocortisone 100 mg IV q8h (300 mg/day)
- Alternative: dexamethasone 2 mg IV q6h

**Step 5: Cooling**
- Acetaminophen 1000 mg PO/IV q6h
- External cooling measures
- Avoid aspirin

**Refractory Thyroid Storm:**
- Cholestyramine 4 g PO q6h — binds thyroid hormone in enterohepatic circulation
- Plasmapheresis/therapeutic plasma exchange — removes circulating thyroid hormones. Reserve for patients deteriorating despite maximal medical therapy.
- Emergent thyroidectomy — last resort

**Atrial Fibrillation:**
- Rate control with beta-blockers (as above)
- Anticoagulation — thyrotoxic AF has high embolic risk. Heparin infusion if no contraindications.
- Cardioversion often fails until euthyroid. Spontaneous conversion expected with treatment of thyrotoxicosis.

## Disposition

**ICU Admission — all patients with thyroid storm.** Continuous telemetry, arterial line if hemodynamically unstable.

**Monitoring:**
- Continuous cardiac monitoring
- Temperature q1-2h
- Glucose monitoring (hyperglycemia common)
- Hepatic function — worsening transaminases/bilirubin indicate poor prognosis
- I/O — high-output heart failure monitoring

**Consultation:**
- Endocrinology — emergent
- ICU/critical care
- Surgery — if refractory to medical therapy (emergent thyroidectomy)

**Transfer:** If facility lacks ICU or endocrinology, stabilize with beta-blocker + PTU + hydrocortisone, then transfer.

## Pitfalls

1. **Waiting for thyroid function tests before starting treatment.** Thyroid storm is a clinical diagnosis. TSH results take hours. Start empiric treatment based on clinical picture — a BWPS >= 45 with tachycardia, fever, and altered mental status warrants immediate therapy.

2. **Giving iodine before or simultaneously with thionamide.** Iodine given before PTU/methimazole provides substrate for additional thyroid hormone synthesis, paradoxically worsening the storm. Always give thionamide at least 1 hour before iodine.

3. **Using aspirin for fever.** Aspirin displaces T4 and T3 from thyroid-binding globulin, acutely increasing free hormone levels. Use acetaminophen and external cooling only.

4. **Relying on thyroid hormone levels to diagnose storm.** Patients with uncomplicated thyrotoxicosis have the same lab values as thyroid storm. The distinction is clinical — multiorgan dysfunction and decompensation define storm.

5. **Choosing methimazole over PTU in thyroid storm.** PTU has the unique advantage of blocking peripheral T4-to-T3 conversion in addition to blocking new synthesis. Methimazole only blocks synthesis. PTU is the preferred thionamide in acute storm.

6. **Neglecting stress-dose steroids.** Thyroid storm creates a relative adrenal insufficiency due to accelerated cortisol metabolism. Hydrocortisone 100 mg IV q8h also inhibits T4-to-T3 conversion.

7. **Cardioverting atrial fibrillation before controlling thyrotoxicosis.** Cardioversion in the thyrotoxic state almost always fails. Rate-control with beta-blockers is the priority. AF typically converts spontaneously once euthyroid.

8. **Missing the precipitant.** Thyroid storm rarely occurs spontaneously — it is triggered by a physiologic stressor. Failure to identify and treat the precipitant (infection, DKA, PE, surgery) leads to treatment failure.

9. **Using cardioselective beta-blockers (metoprolol, atenolol) instead of propranolol.** Propranolol has the unique advantage of blocking peripheral T4-to-T3 conversion. Cardioselective agents lack this effect. Propranolol is the beta-blocker of choice in thyroid storm.
