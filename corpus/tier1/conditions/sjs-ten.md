---
id: sjs-ten
condition: Stevens-Johnson Syndrome and Toxic Epidermal Necrolysis
aliases: [SJS, TEN, Stevens-Johnson syndrome, toxic epidermal necrolysis, SJS-TEN overlap, Lyell syndrome, drug-induced epidermal necrolysis]
icd10: [L51.1, L51.2, L51.3]
esi: 2
time_to_harm: "< 24 hours"
mortality_if_delayed: "SJS 10%, SJS-TEN overlap 20%, TEN >30%"
category: dermatologic
track: tier1
sources:
  - type: guideline
    ref: "British Association of Dermatologists guidelines for the management of Stevens-Johnson syndrome/toxic epidermal necrolysis in adults (2016)"
    doi: "10.1111/bjd.14530"
  - type: pubmed
    ref: "Bastuji-Garin S, et al. SCORTEN: a severity-of-illness score for toxic epidermal necrolysis. J Invest Dermatol. 2000;115(2):149-153"
    pmid: "10951229"
  - type: pubmed
    ref: "Gonzalez-Herrada C, et al. Cyclosporine use in epidermal necrolysis is associated with an important mortality reduction. J Invest Dermatol. 2017;137(10):2092-2100"
    pmid: "28634032"
  - type: pubmed
    ref: "Seminario-Vidal L, et al. Society of Dermatology Hospitalists supportive care guidelines for the management of Stevens-Johnson syndrome/toxic epidermal necrolysis in adults. J Am Acad Dermatol. 2020;82(6):1553-1567"
    pmid: "32151629"
  - type: review
    ref: "Dodiuk-Gad RP, et al. Stevens-Johnson syndrome and toxic epidermal necrolysis: an update. Am J Clin Dermatol. 2015;16(6):475-493"
    pmid: "26481651"
last_updated: "2026-02-18"
compiled_by: agent
risk_tier: B
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
# Stevens-Johnson Syndrome and Toxic Epidermal Necrolysis

## Recognition

### Classification by BSA Detachment
| Entity | Epidermal Detachment |
|---|---|
| SJS | < 10% BSA |
| SJS-TEN overlap | 10-30% BSA |
| TEN | > 30% BSA |

### Clinical Features
- **Prodrome:** Fever, malaise, upper respiratory symptoms 1-3 days before skin findings
- **Mucocutaneous involvement:** Painful erythematous or violaceous macules with epidermal detachment; atypical targetoid lesions (flat, irregular borders) distinct from erythema multiforme
- **Mucous membrane involvement:** Oral erosions (90%), ocular involvement (50-80%), genital erosions (40-60%)
- **Nikolsky sign positive:** Lateral pressure on uninvolved skin causes epidermal separation
- **Asboe-Hansen sign positive:** Pressure on blister causes lateral extension

### SCORTEN Prognostic Score (assess within first 24 hours)
| Parameter | Points |
|---|---|
| Age > 40 years | 1 |
| Heart rate > 120/min | 1 |
| Cancer/hematologic malignancy | 1 |
| BSA detachment > 10% on day 1 | 1 |
| BUN > 28 mg/dL (urea > 10 mmol/L) | 1 |
| Serum bicarbonate < 20 mEq/L | 1 |
| Serum glucose > 252 mg/dL (14 mmol/L) | 1 |

| SCORTEN | Predicted Mortality |
|---|---|
| 0-1 | 3.2% |
| 2 | 12.1% |
| 3 | 35.3% |
| 4 | 58.3% |
| >= 5 | 90% |

### High-Risk Medications (onset typically 4-28 days after initiation)
- **Allopurinol** (most common single-drug cause)
- **Aromatic anticonvulsants:** carbamazepine, phenytoin, lamotrigine, phenobarbital
- **Sulfonamide antibiotics:** trimethoprim-sulfamethoxazole, sulfasalazine
- **NSAIDs:** piroxicam, meloxicam (oxicam class)
- **Antiretrovirals:** nevirapine
- **Antibiotics:** fluoroquinolones, aminopenicillins (rare)

### HLA Associations
- HLA-B*58:01 and allopurinol (Southeast Asian, African American populations)
- HLA-B*15:02 and carbamazepine (East Asian populations)
- HLA-A*31:01 and carbamazepine (European populations)

## Critical Actions

| Action | Target |
|---|---|
| STOP the offending drug | Immediately upon recognition |
| SCORTEN calculation | Within first 24 hours; repeat at 72 hours |
| Fluid resuscitation | Ringer's lactate 2 mL/kg/% BSA detachment/day |
| Ophthalmology consult | Within 24 hours (ocular involvement in 50-80%) |
| Transfer to burn center | If BSA > 10% or escalating, or if no local expertise |
| Pain control | IV opioids PRN (morphine 0.1 mg/kg IV q2-4h) |
| Initiate cyclosporine | 3 mg/kg/day PO/IV divided BID within first 72 hours |

1. Identify and STOP the causative drug immediately. Use ALDEN algorithm for causality assessment if multiple suspects. Earlier drug withdrawal improves survival.
2. Calculate SCORTEN within 24 hours for prognostication and disposition.
3. Start IV fluid resuscitation: Ringer's lactate at 2 mL/kg/% BSA/day (less aggressive than burn resuscitation of 4 mL/kg/%).
4. Obtain ophthalmology consult within 24 hours regardless of symptoms.
5. Arrange burn unit transfer for BSA > 10% or rapidly progressing disease.
6. Begin wound care with non-adherent dressings (petrolatum gauze, silver-impregnated dressings). Do NOT debride attached epidermis.
7. Initiate cyclosporine 3 mg/kg/day PO or IV divided BID.

## Differential Diagnosis

- **Erythema multiforme major:** Typical target lesions (3 zones), acral distribution, often HSV-triggered, limited mucosal involvement
- **Staphylococcal scalded skin syndrome (SSSS):** Superficial (intraepidermal) cleavage, no mucosal involvement, predominantly children < 5 years, cultures positive for S. aureus
- **Drug reaction with eosinophilia and systemic symptoms (DRESS):** Facial edema, eosinophilia, hepatitis, no epidermal detachment
- **Acute generalized exanthematous pustulosis (AGEP):** Hundreds of nonfollicular sterile pustules, rapid onset (< 48h), no epidermal sheets
- **Pemphigus vulgaris:** Chronic course, flaccid blisters, positive Nikolsky, no drug trigger, biopsy with acantholysis
- **Autoimmune bullous diseases:** Linear IgA, bullous pemphigoid; DIF/IIF differentiate
- **Toxic shock syndrome:** Diffuse erythroderma, hypotension, desquamation occurs late (1-2 weeks)
- **Graft-versus-host disease:** Stem cell transplant history

## Workup

- **Skin biopsy:** Full-thickness necrosis of the epidermis; distinguishes from SSSS (subcorneal split). Send for frozen section if SSSS in differential.
- **CBC with differential:** Neutropenia (poor prognostic sign), lymphopenia
- **CMP:** BUN, creatinine, glucose, bicarbonate (SCORTEN parameters); LFTs for hepatic involvement
- **Serum bicarbonate:** Component of SCORTEN
- **Blood cultures:** Rule out sepsis as a trigger or complication
- **Wound cultures:** Baseline and if clinical deterioration (secondary infection is leading cause of death)
- **Chest X-ray:** Respiratory involvement (tracheobronchial sloughing) occurs in 20-25%
- **Mycoplasma IgM and PCR:** Mycoplasma pneumoniae causes SJS-like mucositis (especially in children), often without skin involvement
- **Urinalysis:** Assess for renal involvement, genitourinary mucosal sloughing

## Treatment

### Drug Withdrawal
- Stop ALL suspect medications immediately. In the ALDEN algorithm, the drug started 4-28 days before onset is the most likely culprit.
- Earlier withdrawal (within 24 hours of onset) is associated with improved survival in TEN.

### Fluid Resuscitation
- Ringer's lactate at 2 mL/kg/% BSA detachment/day (approximately half the Parkland formula rate)
- Adjust based on urine output target of 0.5-1.0 mL/kg/hr
- Avoid over-resuscitation: these patients are at risk for pulmonary edema from capillary leak

### Wound Care
- Non-adherent dressings (petrolatum-impregnated gauze, Mepitel, Aquacel Ag)
- Do NOT debride attached or partially detached epidermis; it serves as a biological dressing
- Silver sulfadiazine is CONTRAINDICATED (sulfonamide)
- Gentle daily wound care in warm environment (30-32 degrees C ambient temperature)
- Reverse isolation precautions

### Immunomodulatory Therapy
- **Cyclosporine:** 3 mg/kg/day PO or IV divided BID for 10-14 days; strongest observational evidence for mortality reduction. Monitor renal function and drug levels.
- **IVIG:** Controversial. If used, dose at 1-2 g/kg total over 3-4 days. Evidence is conflicting; recent meta-analyses do not show mortality benefit.
- **Corticosteroids:** NOT recommended. Associated with increased infection risk and delayed wound healing. Controversial — some retrospective data support pulse-dose methylprednisolone, but no RCT evidence.
- **Etanercept:** Emerging data; 50 mg SC single dose in one RCT showed benefit. Not yet standard of care.

### Supportive Care
- **Pain:** Morphine 0.1 mg/kg IV q2-4h or fentanyl 1-2 mcg/kg IV q1-2h; avoid NSAIDs
- **Nutrition:** High-protein, high-calorie enteral nutrition (1.5 g protein/kg/day, 25-30 kcal/kg/day); nasogastric tube if oral intake limited by mucosal erosions
- **Thermoregulation:** Maintain ambient temperature 30-32 degrees C
- **VTE prophylaxis:** Enoxaparin 40 mg SC daily
- **Stress ulcer prophylaxis:** Pantoprazole 40 mg IV daily

### Mucosal Care
- **Eyes:** Preservative-free artificial tears q1-2h, erythromycin ophthalmic ointment, symblepharon lysis with glass rod daily by ophthalmology, amniotic membrane grafts for severe involvement
- **Oral:** Chlorhexidine 0.12% mouthwash, viscous lidocaine 2% swish/spit before meals
- **Genitourinary:** Foley catheter if urethral involvement; gynecology consult for vaginal synechiae prevention

## Disposition

- **BSA > 10% or rapidly progressing:** Transfer to burn center or ICU with burn expertise
- **SCORTEN >= 3:** ICU admission
- **BSA < 10%, SCORTEN 0-1, stable:** Monitored bed with dermatology co-management; burn unit transfer if progression
- **All SJS/TEN patients require admission.** No patient with active SJS/TEN is appropriate for discharge.
- Subspecialty involvement: dermatology, ophthalmology, burn surgery (if available); add gynecology/urology for genital involvement, pulmonology if respiratory mucosal involvement

## Pitfalls

1. **Failing to stop the causative drug.** Every hour of continued exposure worsens prognosis. Review the medication list aggressively and stop all suspects, especially drugs started 4-28 days ago.

2. **Confusing SJS/TEN with SSSS.** Staphylococcal scalded skin syndrome has superficial intraepidermal cleavage (no mucosal involvement, cultures positive), while SJS/TEN has full-thickness epidermal necrosis. Frozen section biopsy differentiates them in under 1 hour.

3. **Using the Parkland formula for fluid resuscitation.** SJS/TEN patients lose less fluid than thermal burn patients. Over-resuscitation causes pulmonary edema and worsens outcomes. Use 2 mL/kg/% BSA/day, not 4 mL/kg/% BSA.

4. **Applying silver sulfadiazine to wounds.** Silver sulfadiazine is a sulfonamide and may have triggered the reaction. Use non-sulfonamide wound care (petrolatum gauze, Aquacel Ag, Mepitel).

5. **Debriding attached epidermis.** Attached or partially detached epidermis acts as a biological dressing, reducing pain and fluid loss. Leave it in place. Only detached necrotic tissue should be gently removed.

6. **Delaying ophthalmology consultation.** Ocular involvement occurs in 50-80% and can cause blindness from corneal scarring, symblepharon, and keratinization. Consult within 24 hours even without eye complaints.

7. **Administering systemic corticosteroids.** No RCT evidence supports corticosteroids in SJS/TEN. Observational data suggest increased infection risk, delayed healing, and no mortality benefit. Cyclosporine has stronger evidence.

8. **Underestimating BSA involvement at initial presentation.** SJS/TEN is a dynamic process. BSA detachment at presentation frequently underestimates final extent. Reassess BSA at 24, 48, and 72 hours. Recalculate SCORTEN at 72 hours.

9. **Missing Mycoplasma-induced SJS in children.** Mycoplasma pneumoniae causes a mucocutaneous eruption mimicking SJS (Mycoplasma-induced rash and mucositis, MIRM), sometimes without skin detachment. Check Mycoplasma IgM/PCR. Treatment is macrolide antibiotics, not immunosuppression.

10. **Forgetting long-term sequelae counseling.** Survivors face chronic ocular surface disease, vaginal/urethral strictures, skin dyspigmentation, and psychological morbidity. Arrange outpatient dermatology, ophthalmology, and mental health follow-up before discharge.
