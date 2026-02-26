---
id: contact-dermatitis
condition: Contact Dermatitis
aliases: [allergic contact dermatitis, irritant contact dermatitis, poison ivy dermatitis]
icd10: [L25.9, L23.9, L24.9]
esi: 4
time_to_harm: "N/A — benign inflammatory dermatosis; see escalation_triggers for emergency differential"
category: dermatologic
track: tier1
disposition_default: outpatient
escalation_triggers:
  - "Mucosal involvement (eyes, mouth, genitalia) — escalate for ophthalmology consult (ocular) or specialist management"
  - ">20% body surface area (BSA) involvement — requires dermatology input and possibly systemic steroids with closer follow-up"
  - "Skin sloughing or detachment — Stevens-Johnson Syndrome (SJS) or toxic epidermal necrolysis (TEN) until excluded"
  - "Target lesions with dusky centers or blistering at mucosal surfaces — SJS/TEN"
  - "Systemic symptoms with rash: fever, malaise, lymphadenopathy, mucositis — drug hypersensitivity reaction (DRESS, SJS/TEN)"
  - "Spreading erythema with warmth, tenderness, and systemic fever — superimposed cellulitis requiring antibiotics"
  - "Blistering on face, eyelids, or genitalia — admit for wound care and specialist involvement"
  - "Airway involvement (stridor, throat tightness, tongue swelling) — anaphylaxis, not contact dermatitis"
confusion_pairs:
  - condition: sjs-ten
    differentiators:
      - "Contact dermatitis: localized to exposure site; no mucosal involvement; no skin detachment; patient is systemically well"
      - "SJS/TEN: mucosal erosions (oral, ocular, genital); positive Nikolsky sign (skin separates with lateral pressure); >10% BSA epidermal detachment (TEN); targetoid lesions with dusky necrotic centers; systemic toxicity (fever, malaise); often drug-triggered (sulfonamides, anticonvulsants, allopurinol, oxicam NSAIDs)"
      - "Contact dermatitis: well-demarcated distribution matching allergen contact pattern; no fever; no mucositis"
      - "SJS/TEN: rapid progression over hours; involves multiple mucous membranes; biopsy shows full-thickness epidermal necrosis"
      - "Critical rule: any rash with mucosal erosions + systemic symptoms + recent drug initiation = SJS/TEN workup immediately"
  - condition: cellulitis-abscess
    differentiators:
      - "Contact dermatitis: pruritic; well-demarcated; distributed at contact site; bilateral patterns common; no fever; no lymphangitis"
      - "Cellulitis: painful (not pruritic); spreading, poorly demarcated erythema with warmth; systemic fever; unilateral; lymphangitis (red streak ascending limb); elevated WBC; no clear allergen exposure"
      - "Contact dermatitis: responds to topical steroids; cellulitis: requires antibiotics"
      - "Critical rule: cellulitis does not itch — pruritus strongly favors contact dermatitis over cellulitis"
sources:
  - type: guideline
    ref: "Fonacier L, Bernstein DI, Pacheco K, et al. Contact Dermatitis: A Practice Parameter — Update 2015. J Allergy Clin Immunol Pract. 2015;3(3 Suppl):S1-39."
    pmid: "25965350"
  - type: pubmed
    ref: "Kimber I, Basketter DA, Gerberick GF, Dearman RJ. Allergic contact dermatitis. Int Immunopharmacol. 2002;2(2-3):201-211."
    pmid: "11811924"
  - type: pubmed
    ref: "Warshaw EM, Maibach HI, Taylor JS, et al. North American contact dermatitis group patch test results: 2011-2012. Dermatitis. 2015;26(2):49-59."
    pmid: "25757279"
  - type: pubmed
    ref: "Perez-Ferriols A, Martinez-Tejerina A, Esteve-Martinez A, et al. Contact allergy to compositae in Spain. Contact Dermatitis. 2015;73(5):291-297."
    pmid: "26140404"
  - type: guideline
    ref: "Usatine RP, Riojas M. Diagnosis and management of contact dermatitis. Am Fam Physician. 2010;82(3):249-255."
    pmid: "20672788"
  - type: pubmed
    ref: "Herro EM, Jacob SE. Systemic contact dermatitis. J Clin Aesthet Dermatol. 2010;3(5):39-44."
    pmid: "20725546"
last_updated: "2026-02-23"
compiled_by: agent
risk_tier: C
validation:
  schema_version: "2.0"
  automated_consistency_check: "2026-02-27"
  dose_range_validator: "2026-02-27"
  unit_normalization_check: "2026-02-27"
  cross_file_consistency_check: "2026-02-27"
  citation_presence_check: "2026-02-27"
  duplicate_content_check: "2026-02-27"
  outlier_detection_flag: clear
  guideline_version_reference: "American Academy of Allergy Asthma & Immunology Practice Parameter 2015"
  provenance_links: []
---

## Recognition

Contact dermatitis is a localized inflammatory skin reaction caused by direct contact with an external substance. Two distinct mechanisms:

- **Irritant contact dermatitis (ICD)**: most common (80% of cases); non-immune-mediated; direct cytotoxic damage from chemicals, soaps, detergents, solvents, friction; onset hours to days after exposure; affects anyone with sufficient exposure
- **Allergic contact dermatitis (ACD)**: Type IV (delayed-type) cell-mediated hypersensitivity; prior sensitization required (days to weeks); re-exposure produces reaction within 12-72 hours; requires patch testing to identify allergen

The diagnosis is clinical. Distribution pattern matching the allergen exposure site is pathognomonic.

### Typical Clinical Presentation
- Pruritic erythematous papules, vesicles, or plaques
- Distribution conforms to contact pattern (linear streaks = poison ivy; band pattern = watchband; ear-shaped = nickel earrings; perimeter of glove = latex or rubber accelerators)
- Acute: erythema, vesicles, bullae, weeping
- Subacute: crusting, scaling
- Chronic: lichenification, fissuring, post-inflammatory hyperpigmentation
- Systemic features absent (no fever, no lymphadenopathy — their presence suggests alternative diagnosis)

### Common Allergens and Their Distribution Patterns
| Allergen | Distribution | Notes |
|----------|-------------|-------|
| Poison ivy/oak (urushiol) | Linear streaks; exposed skin | Most common plant ACD in the US; urushiol concentration in roots > stems > leaves |
| Nickel | Earlobes, wrists, umbilicus | Most common ACD allergen overall; costume jewelry, belt buckles, jeans rivets |
| Fragrances | Face, neck, axillae | Second most common; present in cosmetics and "unscented" products |
| Formaldehyde/releasers | Diffuse; any clothing contact | Permanent-press clothing, shampoos |
| Topical neomycin | Site of wound treatment | Common — patients mistake worsening wound for infection |
| Latex | Hands (glove pattern), anogenital (condom pattern) | Increasingly rare with nitrile shift in healthcare |
| Chromate | Hands, feet | Cement, leather (shoes) |
| Para-phenylenediamine (PPD) | Scalp, hairline, neck | Hair dye — severe reactions possible |

### Poison Ivy Dermatitis — Specific Features
- Urushiol binds to skin within 10-20 minutes; washing after this prevents new skin binding but does not affect already-bound antigen
- Linear vesicular streaks in exposed areas: face, arms, legs, often sparing covered skin
- Classic misconception: fluid in blisters does NOT spread the rash — the rash appears to "spread" due to delayed sensitization in lower-exposure areas
- Duration without treatment: 1-3 weeks; systemic steroids shorten course significantly

## Critical Actions

1. Assess body surface area (BSA) involvement using the Rule of Nines (palmar surface = approximately 1% BSA). Document involvement of palms, face, eyelids, genitalia as high-priority anatomic sites.
2. Examine mucous membranes — oral, ocular, genital. Any mucosal involvement removes this from the "simple contact dermatitis" category.
3. Apply Nikolsky sign if SJS/TEN is suspected: gentle lateral pressure on skin; positive = skin slides off with pressure = immediate escalation.
4. Review medication history for recent drug initiations — drugs causing SJS overlap with contact dermatitis presentation (sulfonamides, carbamazepine, phenytoin, allopurinol, oxicam NSAIDs, lamotrigine).
5. For poison ivy: instruct thorough skin washing with soap and water; wash clothing and equipment (urushiol on clothing remains active for months). Do not pop blisters (secondary infection risk).

## When NOT to Escalate

Contact dermatitis is appropriate for outpatient management when ALL of the following are met:
- No mucosal involvement (no oral erosions, no conjunctival injection with discharge, no genital involvement requiring specialist care)
- BSA <20%
- No systemic symptoms (afebrile, no malaise, no lymphadenopathy)
- No skin sloughing or positive Nikolsky sign
- No airway involvement (no stridor, no throat tightness, no tongue swelling)
- Rash distribution consistent with allergen exposure pattern
- Pruritic (not painful as primary complaint)
- No evidence of cellulitis (no expanding erythema beyond contact zone, no fever, not tender to palpation in a spreading pattern)

Systemic or topical steroids, allergen avoidance instruction, and outpatient follow-up are sufficient for the vast majority of contact dermatitis presentations.

## Differential Diagnosis

| Condition | Key Features | Distinguishing from Contact Dermatitis |
|-----------|-------------|----------------------------------------|
| **SJS/TEN** | Mucosal erosions (oral, ocular, genital); positive Nikolsky; dusky target lesions; >10% BSA detachment (TEN); drug history; fever; systemic toxicity | Contact dermatitis: no mucositis, no Nikolsky, no systemic toxicity, allergen exposure pattern |
| **Cellulitis** | Painful, not pruritic; spreading poorly-defined erythema; warmth; systemic fever; unilateral; lymphangitis | Contact dermatitis: pruritic; well-demarcated; bilateral patterns common; no fever; allergen exposure site |
| **DRESS (Drug Reaction with Eosinophilia and Systemic Symptoms)** | Diffuse morbilliform eruption; facial edema; lymphadenopathy; fever; eosinophilia; hepatitis; recent drug initiation (3-8 weeks prior) | Contact dermatitis: localized, allergen-pattern; no systemic organ involvement; no eosinophilia |
| **Impetigo** | Honey-colored crusted lesions; children; Staphylococcus or Streptococcus; responds to antibiotics | Contact dermatitis: vesicular, pruritic; no honey-crust; no bacterial culture positivity |
| **Herpes zoster (shingles)** | Dermatomal distribution; prodromal pain precedes rash; grouped vesicles on erythematous base; unilateral; does not cross midline | Contact dermatitis: allergen exposure pattern; bilateral possible; no prodromal pain |
| **Scabies** | Intensely pruritic; interdigital spaces, wrists, genitalia, axillae; worse at night; household contacts affected; burrows visible | Contact dermatitis: no burrows; does not affect interdigital spaces characteristically; no nocturnal predilection |
| **Psoriasis** | Silvery plaques on extensor surfaces; well-demarcated; chronic; Auspitz sign; nail pitting; family history | Contact dermatitis: acute onset; allergen exposure pattern; vesicular; responds to steroids rapidly |
| **Atopic dermatitis** | Flexural distribution (antecubital, popliteal fossae); personal/family history of atopy; chronic, relapsing; Dennie-Morgan folds | Contact dermatitis: acute, allergen-specific exposure pattern; no flexural predilection |

## Workup

### No Workup Required (Typical Contact Dermatitis)
- Clinical diagnosis based on distribution pattern, allergen exposure history, and morphology
- No labs or imaging required for localized, well-appearing contact dermatitis

### When to Order Labs
- **CBC with differential**: if DRESS suspected (eosinophilia >1,500 cells/mm³ is diagnostic criterion); if systemic infection cannot be excluded
- **Liver function tests**: DRESS work-up (hepatitis is the most common organ manifestation)
- **Herpes simplex PCR or Tzanck smear**: if grouped vesicles in perioral or genital distribution without clear allergen history
- **Bacterial culture of weeping lesions**: if superimposed infection suspected (purulent discharge, honey-crust, worsening despite steroids)

### Patch Testing (Outpatient — Not an ED Investigation)
- 72-96 hour epicutaneous patch test is the gold standard for identifying ACD allergen
- Refer to dermatology or allergist for patch testing after acute phase resolves
- Guides long-term allergen avoidance — the definitive treatment for recurrent ACD

## Treatment

### Allergen Removal
- Remove and wash any remaining allergen from skin, clothing, and equipment (soap and water within 10-20 minutes for urushiol significantly reduces reaction severity; washing after 60 minutes has limited effect on already-bound antigen)
- Identify and counsel on future allergen avoidance

### Topical Corticosteroids (First-Line for Localized Disease)
Potency selection based on body region:
- **High-potency (Class I-II)**: triamcinolone acetonide 0.1% cream/ointment twice daily, or clobetasol propionate 0.05% cream/ointment once daily — trunk and extremities (not face, skin folds, or genitalia); maximum 2 consecutive weeks to avoid skin atrophy
- **Low-potency (Class VI-VII)**: hydrocortisone 2.5% cream twice daily — face, groin, axillae; appropriate for thin-skin areas
- Ointment formulations preferred over creams for dry, fissured lesions; creams preferred for weeping, vesicular lesions

### Systemic Corticosteroids (Moderate-to-Severe or Widespread Disease)
- **Prednisone 0.5-1 mg/kg/day PO** (typical adult dose: 40-60 mg PO daily) tapered over 14-21 days. A 5-7 day taper is inadequate for poison ivy dermatitis — rebound dermatitis occurs. Minimum 14-day taper is standard for significant urushiol exposure.
- **Methylprednisolone dose pack (Medrol)**: commonly prescribed but provides only 6 days of tapering — insufficient for severe poison ivy; prescribe a prednisone taper instead for significant cases.
- Systemic steroids are the standard of care for moderate-to-severe poison ivy/oak dermatitis, >10% BSA involvement, or involvement of face/genitalia.
- **Triamcinolone acetonide 40 mg IM** (single dose): alternative for patients unable to take oral medications or with poor compliance; equivalent efficacy to oral prednisone.

### Antihistamines (Symptom Relief)
- **Diphenhydramine 25-50 mg PO every 4-6 hours PRN** (adults): sedating antihistamine; modest anti-pruritic effect; useful at bedtime
- **Hydroxyzine 25-50 mg PO every 6-8 hours PRN** (adults): preferred sedating antihistamine for contact dermatitis pruritus
- **Cetirizine 10 mg PO daily** or **loratadine 10 mg PO daily**: non-sedating; less effective for acute pruritus but useful for ongoing management
- Non-sedating antihistamines have limited evidence for pruritus from contact dermatitis — histamine is not the primary mediator (Type IV reaction is T-cell-mediated); antihistamines provide symptomatic relief, not immunologic treatment

### Wound Care for Bullae/Vesicles
- Leave intact bullae intact when possible — roof provides protection
- Ruptured bullae: gentle debridement of necrotic roof; non-adherent dressing (petrolatum gauze); keep moist to prevent secondary infection
- Do NOT apply topical antibiotics (neomycin/polymyxin) to contact dermatitis — neomycin is a common contact allergen that will worsen the reaction

## Disposition

### Discharge (Standard)
- Localized contact dermatitis without mucosal involvement, BSA <20%, no systemic symptoms: discharge with topical or systemic corticosteroids, allergen identification counseling, and return precautions
- Poison ivy: prescribe prednisone taper (minimum 14 days); provide wound care instructions; counsel on urushiol persistence on clothing/tools

### Urgent Dermatology Referral
- Ocular involvement: ophthalmology referral within 24-48 hours (steroid eye drops may be needed; ophthalmologist should supervise)
- Genital involvement: arrange urgent dermatology or urology/gynecology follow-up

### Admit / Escalate
- SJS/TEN: immediate dermatology or burn unit involvement; stop causative drug; do NOT use corticosteroids pending specialist review (controversial in SJS/TEN)
- Extensive bullous disease with wound care needs beyond outpatient capability
- Superimposed cellulitis requiring IV antibiotics

### Follow-up
- Primary care or dermatology in 1-2 weeks for treatment response assessment
- Patch testing at dermatology after acute phase resolves (minimum 2-4 weeks after complete resolution)

## Pitfalls

1. **Prescribing a 6-day methylprednisolone dose pack for significant poison ivy dermatitis.** The Medrol dose pack provides a rapid taper over 6 days — insufficient for the 14-21 day immune response of urushiol-triggered delayed hypersensitivity. The majority of patients prescribed Medrol for poison ivy return within 5-7 days with rebound dermatitis as the taper ends. Prednisone 40-60 mg PO daily with a 14-21 day taper is the appropriate prescription.

2. **Missing SJS/TEN in a patient with widespread "contact dermatitis" and fever.** SJS/TEN is a dermatologic emergency with 5-15% mortality (SJS) and 25-35% mortality (TEN). The critical differentiating sign is mucosal involvement — oral erosions, conjunctival injection with discharge, genital erosions. Nikolsky sign (skin sliding off with lateral pressure) is positive in SJS/TEN, negative in contact dermatitis. Any patient with a rash + fever + mucosal involvement + recent drug initiation requires immediate SJS/TEN evaluation.

3. **Applying topical neomycin to contact dermatitis wounds.** Neomycin is one of the most common contact allergens in the United States (top 10 on North American Contact Dermatitis Group screening series). Applying neomycin-containing triple antibiotic ointment to an already-inflamed contact dermatitis wound will sensitize or re-elicit an allergic response, worsening the rash. Use petrolatum alone as a wound barrier.

4. **Diagnosing bilateral lower extremity "contact dermatitis" without considering stasis dermatitis or venous insufficiency.** Bilateral lower extremity pruritic, scaly, erythematous eruption in an older patient with varicosities and edema is stasis dermatitis — not contact dermatitis. These patients are often allergic to their own compression stocking elastic or wound care products (secondary ACD on background of stasis), making the diagnosis compound. Treatment is compression plus topical steroids; leg elevation; addressing venous insufficiency.

5. **Confusing cellulitis with contact dermatitis and treating with steroids.** The most reliable clinical differentiator: contact dermatitis itches; cellulitis hurts. Pruritus favors contact dermatitis; pain, tenderness, and warmth favor cellulitis. Corticosteroids prescribed for "contact dermatitis" that is actually cellulitis will suppress the immune response and worsen a bacterial skin infection. When the diagnosis is uncertain, treat for cellulitis first.
