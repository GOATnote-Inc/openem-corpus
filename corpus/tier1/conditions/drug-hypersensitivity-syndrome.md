---
id: drug-hypersensitivity-syndrome
condition: Drug Reaction with Eosinophilia and Systemic Symptoms (DRESS Syndrome)
aliases: [DRESS syndrome, drug hypersensitivity syndrome, drug-induced hypersensitivity syndrome, DIHS]
icd10: [T88.7XXA, L27.0]
esi: 2
time_to_harm:
  irreversible_injury: "< 48 hours (fulminant hepatitis)"
  death: "< 1 week (hepatic failure, myocarditis)"
  optimal_intervention_window: "< 24 hours for drug withdrawal and organ assessment"
mortality_if_delayed: "2-10% overall mortality; liver involvement increases risk"
category: allergic-immunologic
track: tier1
sources:
  - type: review
    ref: "Kardaun SH, et al. Drug reaction with eosinophilia and systemic symptoms (DRESS): an original multisystem adverse drug reaction. Results from the prospective RegiSCAR study. Br J Dermatol 2013;169(5):1071-1080"
  - type: review
    ref: "Husain Z, et al. DRESS syndrome: Part I. Clinical perspectives. J Am Acad Dermatol 2013;68(5):693.e1-14"
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
# Drug Reaction with Eosinophilia and Systemic Symptoms (DRESS Syndrome)

## Recognition

**Classic presentation (onset 2-8 weeks after drug initiation):**
- Fever (often > 38.5C, first symptom)
- Diffuse morbilliform rash (> 50% BSA), often becoming confluent
- Facial edema (characteristic — especially periorbital)
- Lymphadenopathy (widespread)
- Eosinophilia (> 1500/mcL) and/or atypical lymphocytes
- Visceral organ involvement (liver most common)

**RegiSCAR diagnostic criteria (score >= 5 = definite DRESS):**
- Fever >= 38.5C (+0)
- Lymphadenopathy at >= 2 sites (+1)
- Eosinophilia >= 700/mcL (+1) or >= 1500/mcL (+2)
- Atypical lymphocytes (+1)
- Rash > 50% BSA (+1), with >= 2 features (edema, infiltration, purpura, scaling) (+1)
- Organ involvement: 1 organ (+1), >= 2 organs (+2)

**Most common causative drugs (onset 2-8 weeks):**
- Anticonvulsants: carbamazepine, phenytoin, lamotrigine, phenobarbital
- Allopurinol
- Sulfonamides (dapsone, TMP-SMX)
- Minocycline
- Vancomycin
- Abacavir

**Organ involvement:**
- **Liver (80%):** hepatitis (elevated ALT/AST), may progress to fulminant hepatic failure
- **Kidney (40%):** interstitial nephritis, elevated creatinine
- **Lung (25%):** eosinophilic pneumonitis, interstitial pneumonia
- **Heart (10%):** myocarditis, pericarditis (most common cause of death)
- **Thyroid (5%):** thyroiditis (may present weeks-months after resolution)
- **Pancreas, CNS:** rare but reported

## Critical Actions

| Action | Target |
|---|---|
| Discontinue offending drug | IMMEDIATELY |
| Liver function tests | At presentation |
| Cardiac monitoring | If troponin or ECG abnormalities |
| Dermatology consultation | Same day |
| Corticosteroids if organ involvement | Within 6 hours |

1. **Identify and STOP the offending drug immediately** — review medication list for drugs started 2-8 weeks prior
2. **Comprehensive organ assessment:** LFTs, creatinine, urinalysis, CBC with eosinophil count, troponin, ECG, chest X-ray
3. **Dermatology consultation** — for biopsy and management guidance
4. **Corticosteroids** if liver involvement (ALT > 3x ULN) or other significant organ dysfunction
5. **Monitor for HHV-6 reactivation** — occurs in ~60% of DRESS and may drive organ damage

## Differential Diagnosis

- Stevens-Johnson syndrome / toxic epidermal necrolysis (mucosal involvement, epidermal detachment, Nikolsky sign positive)
- Serum sickness (earlier onset if drug-related; low complement; no eosinophilia)
- Viral exanthem (EBV, CMV — viral titers help differentiate)
- Kawasaki disease (children — fever > 5 days, conjunctivitis, strawberry tongue)
- Acute generalized exanthematous pustulosis (AGEP) — neutrophilic pustules, rapid onset (< 48 hours), short course
- Systemic lupus erythematosus (ANA, anti-dsDNA, chronic course)
- Hypereosinophilic syndrome (sustained eosinophilia without drug trigger)
- Adult-onset Still disease (quotidian fever, evanescent salmon-colored rash, ferritin markedly elevated)
- Hemophagocytic lymphohistiocytosis (HLH) — fever, cytopenias, hepatosplenomegaly, hyperferritinemia

## Workup

- **CBC with differential:** eosinophilia (> 1500/mcL in 90%), atypical lymphocytes (40%), leukocytosis
- **Liver function tests:** ALT, AST, ALP, total bilirubin, albumin — liver is the most commonly affected organ
- **BMP:** creatinine, electrolytes (renal involvement)
- **Urinalysis:** eosinophiluria, proteinuria (interstitial nephritis)
- **Troponin and ECG:** myocarditis screening — DRESS myocarditis can be fatal
- **Echocardiogram:** if troponin elevated or ECG abnormalities
- **Chest X-ray:** pulmonary infiltrates (eosinophilic pneumonitis)
- **TSH:** baseline (thyroiditis may develop weeks later)
- **HHV-6 PCR:** reactivation common; may guide treatment escalation
- **Skin biopsy:** interface dermatitis, eosinophilic infiltrate (dermatology performs)
- **Peripheral smear:** atypical lymphocytes, rule out hematologic malignancy

## Treatment

### Immediate
- **Discontinue ALL suspect drugs** — if multiple drugs started within the window, stop all and rechallenge cautiously later under allergy guidance
- **Supportive care:** IV hydration, skin care (emollients, cool compresses)

### Mild (Rash Only, No Organ Involvement, Eosinophilia < 5000)
- **Topical triamcinolone 0.1% cream** BID to affected areas
- **Antihistamines:** cetirizine 10 mg PO daily or hydroxyzine 25 mg PO q6h for pruritus
- **Monitor LFTs and CBC** every 2-3 days

### Moderate-Severe (Organ Involvement)
- **Prednisone 1-1.5 mg/kg/day PO (max 60 mg)** — taper SLOWLY over 8-12 weeks minimum
- Rapid taper (< 6 weeks) associated with relapse
- **Monitor LFTs, creatinine, CBC weekly** during taper

### Severe (Fulminant Hepatitis, Myocarditis, Multi-Organ)
- **Methylprednisolone 1000 mg IV daily x 3 days** (pulse dose) then oral prednisone 1 mg/kg/day with slow taper
- **Cyclosporine 3-5 mg/kg/day PO divided BID** — for steroid-refractory cases; monitor drug levels and renal function
- **IVIG 2 g/kg IV** divided over 2-5 days — for steroid-refractory or HHV-6-driven cases (evidence limited)
- **Hepatology consultation** if ALT > 10x ULN or rising bilirubin (liver transplant evaluation if progressing)
- **Cardiology consultation** for myocarditis

### Long-Term Monitoring
- **Thyroid function (TSH)** at 3, 6, and 12 months post-DRESS (autoimmune thyroiditis can develop late)
- **Renal function** monitoring if nephritis was present
- **Allergy referral** for culprit drug identification and cross-reactivity counseling

## Disposition

- **Mild (rash, eosinophilia, no organ involvement):** Discharge with drug discontinuation, topical steroids, outpatient dermatology follow-up in 3-5 days; repeat labs in 2-3 days
- **Moderate (liver involvement, renal involvement):** Admission for IV monitoring, systemic steroids, serial labs
- **Severe (fulminant hepatitis, myocarditis, multi-organ):** ICU admission; pulse-dose steroids; hepatology/cardiology consultation
- **All patients:** document drug allergy (including cross-reactive drugs); allergy referral; long-term thyroid monitoring

## Pitfalls

1. **Missing DRESS because the onset is weeks after drug initiation.** Unlike most drug rashes (days), DRESS onset is 2-8 weeks after starting the culprit drug. Physicians often do not connect a rash to a medication started months ago.

2. **Tapering steroids too quickly.** DRESS flares with rapid steroid tapers. The minimum taper duration should be 8-12 weeks. A 2-week prednisone taper will almost certainly cause relapse.

3. **Not checking troponin.** DRESS myocarditis is the most common cause of death. A baseline troponin and ECG should be obtained in every patient with suspected DRESS, even without cardiac symptoms.

4. **Confusing DRESS with SJS/TEN.** SJS/TEN features mucosal erosions, epidermal detachment, and a positive Nikolsky sign. DRESS features facial edema, eosinophilia, and organ involvement without significant epidermal detachment. The treatments differ significantly (corticosteroids are the mainstay for DRESS but controversial in SJS/TEN).

5. **Not monitoring thyroid function long-term.** Autoimmune thyroiditis can develop 3-12 months after DRESS resolution. All patients need TSH monitoring at 3, 6, and 12 months post-episode.
