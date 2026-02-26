---
id: toxic-shock-syndrome
condition: Toxic Shock Syndrome
aliases: [TSS, staphylococcal toxic shock, streptococcal toxic shock, STSS, menstrual TSS, non-menstrual TSS]
icd10: [A48.3, A48.0]
esi: 1
time_to_harm:
  irreversible_injury: "< 6 hours (multi-organ failure from superantigen-driven cytokine storm)"
  death: "< 24 hours without aggressive resuscitation and source control"
  optimal_intervention_window: "< 2 hours — antibiotics and source control within first 2 hours of recognition"
category: infectious
track: tier1
sources:
  - type: cdc
    ref: "CDC. Toxic Shock Syndrome (TSS): Case Definition and Clinical Description. National Notifiable Diseases Surveillance System."
    url: "https://ndc.services.cdc.gov/case-definitions/toxic-shock-syndrome-2011/"
  - type: pubmed
    ref: "DeVries AS et al. Staphylococcal toxic shock syndrome 2000-2006: epidemiology, clinical features, and molecular characteristics. PLoS One. 2011;6(8):e22997."
    pmid: "21857978"
  - type: review
    ref: "Lappin E, Ferguson AJ. Gram-positive toxic shock syndromes. Lancet Infect Dis. 2009;9(5):281-290."
    pmid: "19393958"
  - type: pubmed
    ref: "Carapetis JR et al. The global burden of group A streptococcal diseases. Lancet Infect Dis. 2005;5(11):685-694."
    pmid: "16253886"
  - type: guideline
    ref: "Stevens DL et al. Practice guidelines for the diagnosis and management of skin and soft tissue infections: 2014 update by the IDSA. Clin Infect Dis. 2014;59(2):e10-52."
    pmid: "24973422"
last_updated: "2026-02-26"
compiled_by: agent
reviewed_by: "Brandon Dent, MD — Board Certified Emergency Medicine"
review_date: "2026-02-27"
risk_tier: A
confusion_pairs:
  - condition: sepsis
    differentiators:
      - "TSS: diffuse macular erythroderma (sunburn-like rash) is characteristic"
      - "TSS: desquamation of palms/soles occurs 1-2 weeks after onset"
      - "TSS: blood cultures often negative (toxin-mediated, not bacteremia-dependent)"
  - condition: meningococcemia
    differentiators:
      - "Meningococcemia: petechial/purpuric rash (not erythroderma)"
      - "Meningococcemia: blood cultures positive for N. meningitidis"
      - "TSS rash is diffuse, blanching erythroderma; meningococcal rash is non-blanching petechiae"
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
# Toxic Shock Syndrome

## Recognition

**Definition:** Toxic shock syndrome (TSS) is a superantigen-mediated toxemia caused by Staphylococcus aureus (TSST-1, staphylococcal enterotoxins) or Group A Streptococcus (streptococcal pyrogenic exotoxins). Superantigens bypass normal antigen processing and directly activate 5-30% of T cells, triggering massive cytokine release and multi-organ failure.

**Two Major Forms:**

| Feature | Staphylococcal TSS | Streptococcal TSS (STSS) |
|---------|--------------------|-----------------------|
| **Toxin** | TSST-1 (menstrual), enterotoxins B/C (non-menstrual) | Streptococcal pyrogenic exotoxins A, B, C |
| **Blood cultures** | Usually negative (toxin-mediated) | Positive in 60% (invasive infection) |
| **Soft tissue** | No necrotizing fasciitis | Necrotizing fasciitis in 50% |
| **Mortality** | 3-5% | 30-70% |
| **Rash** | Diffuse erythroderma, late desquamation | Erythroderma less common; may have local wound erythema |
| **Common source** | Tampon/menstrual, surgical wound, nasal packing | Skin/soft tissue infection, varicella, postpartum |

**CDC Case Definition (Staphylococcal TSS) — all 5 criteria required:**
1. Fever ≥ 38.9°C (102°F)
2. Hypotension: SBP ≤ 90 mmHg (adults) or < 5th percentile for age (children)
3. Diffuse macular erythroderma (sunburn-like rash)
4. Desquamation (1-2 weeks after onset, especially palms and soles)
5. Involvement of ≥ 3 organ systems: GI (vomiting/diarrhea), muscular (CPK elevation), mucous membrane hyperemia, renal (BUN/Cr elevation), hepatic (bilirubin/transaminase elevation), hematologic (platelets < 100,000), CNS (confusion without focal signs)

**Clinical Timeline:**
- Hours 0-6: Fever, myalgias, nausea/vomiting/diarrhea, sunburn-like rash
- Hours 6-24: Hypotension, oliguria, altered mental status, erythroderma spreads
- Hours 24-72: Multi-organ dysfunction, ARDS, DIC
- Days 7-14: Desquamation of palms, soles, fingers, toes (pathognomonic)

**Risk Factors:**
- Menstrual: tampon use (especially super-absorbent), menstrual cups
- Non-menstrual: surgical wound packing, nasal packing, burns, postpartum
- Streptococcal: recent varicella, skin break, NSAID use (controversial), postpartum, diabetes

## Critical Actions

1. **Aggressive fluid resuscitation.** NS 30 mL/kg IV bolus within the first hour, repeat as needed. TSS patients may require 10-20 L crystalloid in the first 24 hours due to massive capillary leak. Target MAP ≥ 65 mmHg, urine output > 0.5 mL/kg/hr.

2. **Remove the source immediately.** Remove tampon, nasal packing, wound packing, or any retained foreign body. Irrigate and debride any wound. For streptococcal TSS with suspected necrotizing fasciitis: emergent surgical exploration and debridement — do not delay for imaging.

3. **Antibiotics within 1 hour of recognition.** Vancomycin 25-30 mg/kg IV loading dose (covers MRSA) + clindamycin 900 mg IV q8h (suppresses toxin production — this is the key mechanistic rationale for clindamycin) + piperacillin-tazobactam 4.5 g IV q6h (broad coverage). Clindamycin is the critical drug — it inhibits ribosomal toxin synthesis at the translational level, independent of bacterial kill.

4. **Vasopressors for fluid-refractory shock.** Norepinephrine 0.1-0.5 mcg/kg/min IV as first-line. Add vasopressin 0.04 units/min IV for refractory vasodilatory shock. TSS shock is predominantly distributive — catecholamine requirements may be very high.

5. **IVIG 1 g/kg IV on day 1, may repeat 0.5 g/kg on day 2.** Binds and neutralizes circulating superantigen toxins. Most evidence in streptococcal TSS with refractory shock. Give early — efficacy decreases after toxin has bound T-cell receptors.

6. **Source control for streptococcal TSS.** If necrotizing fasciitis is suspected (disproportionate pain, woody induration, crepitus, bullae, rapid progression), emergent surgical debridement is the definitive intervention. Mortality increases by 10% per hour of delay in surgical debridement for necrotizing fasciitis.

7. **Blood cultures x2 before antibiotics** (but do not delay antibiotics for cultures). Send wound cultures if source identified.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **Meningococcemia** | Petechial/purpuric rash (non-blanching), not erythroderma; positive blood cultures for N. meningitidis; nuchal rigidity |
| **Staphylococcal scalded skin syndrome** | Nikolsky-positive bullae with exfoliation; typically affects young children; no multi-organ failure; toxin causes skin cleavage at granular layer |
| **Kawasaki disease** | Pediatric (< 5 years); ≥ 5 days fever; conjunctival injection, strawberry tongue, extremity changes; no hypotension initially |
| **Drug reaction (DRESS, SJS/TEN)** | Temporal relationship to new medication; SJS/TEN has mucosal erosion and skin detachment; DRESS has eosinophilia |
| **Septic shock (non-TSS)** | No characteristic erythroderma; positive blood cultures typical; no desquamation |
| **Scarlet fever** | Sandpaper rash with Pastia lines; pharyngitis; not systemically toxic; no multi-organ failure |
| **Necrotizing fasciitis without TSS** | Local soft tissue findings dominate; may not have systemic erythroderma; overlap with streptococcal TSS is common |
| **Adrenal crisis** | Hypotension, altered mental status; no rash; cortisol < 3 mcg/dL; responds to hydrocortisone |

## Workup

**Immediate:**
- CBC with differential (leukocytosis with left shift; thrombocytopenia < 100,000 in severe TSS)
- BMP (elevated creatinine, hyponatremia from fluid third-spacing)
- LFTs (elevated bilirubin, transaminases)
- CK (elevation in > 50% — rhabdomyolysis component)
- Coagulation studies: PT/INR, fibrinogen, D-dimer (DIC screening)
- Blood cultures x2
- Lactate (prognostic; > 4 mmol/L indicates severe tissue hypoperfusion)
- Blood gas

**Source Identification:**
- Vaginal exam: remove tampon; send vaginal swab for culture
- Wound inspection: send wound culture; probe for fascia integrity
- CT with IV contrast if necrotizing fasciitis suspected and patient stable (do NOT delay surgery for imaging if clinical diagnosis clear)

**Additional:**
- Urinalysis (pyuria without UTI = renal involvement)
- CXR (ARDS, pulmonary edema)
- ECG (myocarditis, arrhythmia)

## Treatment

**Hemodynamic Support:**
- NS 30 mL/kg IV bolus, repeat x2-3 as needed (expect massive fluid requirements)
- Norepinephrine 0.1-0.5 mcg/kg/min IV for MAP < 65 after fluid resuscitation
- Vasopressin 0.04 units/min IV as second vasopressor
- Stress-dose hydrocortisone 100 mg IV q8h for refractory shock (relative adrenal insufficiency common in TSS)

**Antimicrobial Therapy:**
- Vancomycin 25-30 mg/kg IV loading dose (target trough 15-20 mcg/mL) — covers MRSA
- Clindamycin 900 mg IV q8h — toxin production inhibition (continue regardless of susceptibility — mechanism is translational suppression, not bactericidal)
- Piperacillin-tazobactam 4.5 g IV q6h — broad gram-negative coverage for undifferentiated source
- Narrow antibiotics once cultures and sensitivities return

**IVIG:**
- IVIG 1 g/kg IV on day 1 for streptococcal TSS with refractory shock
- May repeat 0.5 g/kg on day 2 if no improvement
- Evidence strongest for streptococcal TSS; weaker for staphylococcal TSS but often given in severe cases

**Organ Support:**
- Mechanical ventilation for ARDS (low tidal volume 6 mL/kg IBW, PEEP per ARDSNet)
- CRRT for AKI with volume overload or refractory acidosis
- Platelet and FFP transfusion for DIC with active bleeding

**Source Control:**
- Tampon/foreign body removal
- Wound debridement (bedside or OR)
- Necrotizing fasciitis: emergent surgical debridement — multiple returns to OR at 24-48 hour intervals until viable tissue margins achieved

## Disposition

**All TSS patients require ICU admission.** Mortality in staphylococcal TSS is 3-5%; in streptococcal TSS 30-70%.

**Surgical consultation** is required for:
- Suspected necrotizing fasciitis
- Wound debridement
- Any soft tissue source requiring operative management

**Public health notification:** TSS is a notifiable condition in most jurisdictions. Report to local health department.

**Follow-up:**
- Anti-TSST-1 antibody levels do not develop in ~30% of staphylococcal TSS patients, creating risk of recurrence (up to 30% recurrence rate in menstrual TSS)
- Counsel menstrual TSS patients against future tampon use

## Pitfalls

1. **Dismissing the sunburn-like rash as drug reaction or viral exanthem.** The diffuse macular erythroderma of TSS is often described as "sunburn" and is easily misattributed to medication allergy, viral illness, or sunburn itself. In the context of fever + hypotension + erythroderma, TSS must be the working diagnosis. The rash may be subtle in early disease or in dark-skinned patients — examine conjunctival and mucosal hyperemia.

2. **Omitting clindamycin from the antibiotic regimen.** Clindamycin is the mechanistically critical antibiotic in TSS. It suppresses toxin production at the ribosomal level, which beta-lactams and vancomycin do not. Beta-lactams kill bacteria but do not stop toxin synthesis from organisms already expressing toxin genes. Clindamycin must be included regardless of susceptibility testing because the mechanism is translational, not dependent on bactericidal activity.

3. **Delaying surgical exploration for streptococcal TSS with soft tissue findings.** Necrotizing fasciitis complicates 50% of streptococcal TSS cases. CT imaging has ~80% sensitivity for necrotizing fasciitis — a normal CT does not exclude it. If clinical suspicion is high (pain out of proportion, woody induration, rapid progression, hemodynamic instability), proceed directly to surgical exploration. Mortality increases with each hour of delay.

4. **Underestimating fluid requirements.** TSS causes profound capillary leak similar to severe burns. Patients commonly require 10-20 L of crystalloid in the first 24 hours. Inadequate resuscitation leads to end-organ hypoperfusion and worsening lactic acidosis. Monitor urine output, lactate clearance, and hemodynamic response — not just central venous pressure.

5. **Failing to search for retained foreign body in non-menstrual TSS.** Non-menstrual TSS sources include surgical wound packing, nasal packing (rhinoplasty, epistaxis), retained vaginal foreign bodies (menstrual cup, contraceptive device), and burns. A thorough search for and removal of retained foreign material is essential — antibiotics alone cannot overcome continuous toxin generation from a colonized foreign body.
