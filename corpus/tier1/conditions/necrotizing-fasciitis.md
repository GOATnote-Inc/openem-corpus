---
id: necrotizing-fasciitis
condition: Necrotizing Fasciitis
aliases: [nec fasc, flesh-eating disease, necrotizing soft tissue infection, NSTI, fournier gangrene]
icd10: [M72.6, N49.3, N76.89]
esi: 1
time_to_harm: "< 6 hours"
mortality_if_delayed: "Mortality increases 7.6% per hour of surgical delay"
category: infectious
track: tier1
sources:
  - type: guideline
    ref: "Stevens DL et al. IDSA Practice Guidelines for the Diagnosis and Management of Skin and Soft Tissue Infections: 2014 Update. Clin Infect Dis 2014;59:e10-52"
    pmid: "24973422"
  - type: pubmed
    ref: "Wong CH et al. The LRINEC Score: A Tool for Distinguishing Necrotizing Fasciitis from Other Soft Tissue Infections. Crit Care Med 2004;32:1535-1541"
    pmid: "15241098"
  - type: pubmed
    ref: "Nawijn F et al. Time Is of the Essence When Treating Necrotizing Soft Tissue Infections: A Systematic Review and Meta-analysis. World J Emerg Surg 2020;15:4"
    pmid: "31921330"
  - type: pubmed
    ref: "Lancerotto L et al. Necrotizing Fasciitis: Classification, Diagnosis, and Management. J Trauma Acute Care Surg 2012;72:560-566"
    pmid: "22491537"
last_updated: "2026-02-18"
compiled_by: agent
reviewed_by: "Brandon Dent, MD — Board Certified Emergency Medicine"
review_date: "2026-02-27"
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
  provenance_links: []
---
# Necrotizing Fasciitis

## Recognition

**Definition:** Rapidly progressive necrotic infection of fascial planes and subcutaneous tissue. Spreads along fascial planes at up to 1 inch/hour. Classified by microbiology:
- **Type I (polymicrobial):** Mixed aerobic/anaerobic. Older, diabetic, immunocompromised patients. Fournier gangrene (perineal), post-surgical.
- **Type II (monomicrobial):** Group A Streptococcus (most common), Staphylococcus aureus (including MRSA), Vibrio vulnificus (saltwater/raw shellfish exposure), Aeromonas (freshwater exposure).
- **Type III:** Gas gangrene (Clostridium perfringens).

**Clinical Features — Early (0-24h):**
- Pain out of proportion to exam findings — the hallmark. Severe pain with minimal skin changes.
- Erythema, swelling, warmth — indistinguishable from cellulitis at this stage
- Fever, tachycardia
- Edema extending beyond visible erythema

**Clinical Features — Late (24-72h):**
- Dusky or grayish skin, hemorrhagic bullae
- Crepitus (gas in tissues — present in only 13-31%)
- Skin anesthesia (cutaneous nerve destruction)
- Rapid progression of skin findings despite antibiotics
- Sepsis, shock, multiorgan failure
- "Dishwater" gray wound drainage

**Risk Factors:**
- Diabetes mellitus (most common comorbidity)
- Immunosuppression, HIV, malignancy
- IV drug use
- Obesity
- Peripheral vascular disease
- Recent surgery/trauma (including minor: insect bite, injection site)
- Chronic liver/kidney disease
- NSAIDs use (may mask symptoms and promote GAS progression)

**LRINEC Score (Laboratory Risk Indicator for Necrotizing Fasciitis):**
- CRP >= 150 mg/L (4 pts), WBC 15-25 (1 pt) or > 25 (2 pts), Hgb 11-13.5 (1 pt) or < 11 (2 pts), Na < 135 (2 pts), Creatinine > 1.6 (2 pts), Glucose > 180 (1 pt)
- Score >= 6: high suspicion (PPV 92%). Score >= 8: strongly predictive.
- LRINEC is a screening aid — a low score does NOT exclude NSTI. Sensitivity is only 68-80%.

## Critical Actions

1. **Emergent surgical consultation** — call surgery immediately when NSTI is suspected. Do NOT delay for imaging or lab results. Surgical debridement is the definitive treatment.
2. **Broad-spectrum IV antibiotics** — vancomycin 25-30 mg/kg IV loading dose then 15-20 mg/kg q8-12h + piperacillin-tazobactam 4.5 g IV q6h + clindamycin 900 mg IV q8h. Clindamycin is critical for toxin suppression (inhibits protein synthesis, reduces GAS superantigen/exotoxin production).
3. **Aggressive fluid resuscitation** — these patients develop septic shock rapidly. NS or LR boluses, titrate to MAP >= 65 mmHg. Vasopressors (norepinephrine) for refractory hypotension.
4. **Serial exams** — mark the borders of erythema with a skin marker and timestamp. Progression beyond marked borders despite antibiotics supports NSTI diagnosis.
5. **Obtain labs** — CBC, CMP, CRP, lactate, CK, blood cultures, coagulation studies. Calculate LRINEC score.
6. **Pain management** — these patients have severe pain. IV opioids titrated to effect. Pain out of proportion requiring escalating opioid doses further supports the diagnosis.
7. **Source control** — surgical debridement within 12 hours (ideally within 6 hours) of presentation. Mortality increases with every hour of delay.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Cellulitis | Pain proportional to exam findings, no systemic toxicity, responds to antibiotics, no pain out of proportion |
| Abscess | Fluctuant, localized, does not spread along fascial planes |
| Deep vein thrombosis | Unilateral leg swelling, positive Doppler, no crepitus or skin necrosis |
| Gas gangrene (clostridial myonecrosis) | Crepitus, bronze/brown skin, "sweet" odor, myonecrosis on exploration — clinically overlaps; treated similarly |
| Pyomyositis | Deep muscle infection, MRI shows intramuscular abscess, less fascial involvement |
| Calciphylaxis | Reticular purpura in ESRD patients, painful skin necrosis but chronic/subacute, no sepsis initially |
| Toxic epidermal necrolysis | Mucosal involvement, drug exposure history, epidermal sloughing, no fascial plane involvement |
| Warfarin-induced skin necrosis | 3-5 days after warfarin initiation, protein C-deficient areas (breasts, thighs, buttocks) |

## Workup

**Labs:**
- CBC — leukocytosis (WBC > 15,000) or leukopenia (poor prognostic sign)
- CMP — hyponatremia < 135, elevated creatinine, hyperglycemia
- CRP — markedly elevated (> 150 mg/L)
- Lactate — elevated in sepsis/tissue ischemia
- CK — elevated (muscle involvement)
- Blood cultures x 2 — positive in 40-60%
- Procalcitonin — elevated (aids differentiation from non-infectious inflammation)
- Coagulation studies, fibrinogen — DIC screening
- Blood gas — metabolic acidosis
- Calculate LRINEC score

**Imaging (do NOT delay surgery for imaging):**
- CT with IV contrast — fascial thickening/enhancement, fat stranding, gas tracking along fascial planes, fluid collections. Sensitivity 80-100% but cannot reliably exclude early NSTI.
- Plain radiograph — subcutaneous gas (specific but insensitive — present in only 13-31%)
- MRI — most sensitive imaging modality (fascial enhancement, T2 hyperintensity), but too time-consuming for unstable patients
- Ultrasound (point-of-care) — fascial thickening > 4mm, "cobblestoning" of subcutaneous tissue, subcutaneous air. Rapid bedside tool.

**Operative (gold standard):** Finger test — bedside incision under local anesthesia. Findings confirming NSTI: dishwater gray necrotic fascia, lack of bleeding, tissue planes separate with blunt finger dissection, "positive finger test" (finger passes easily along fascial plane with minimal resistance).

## Treatment

**Antibiotics (start immediately, do not wait for cultures):**
- Empiric broad-spectrum: vancomycin 25-30 mg/kg IV loading dose, then 15-20 mg/kg IV q8-12h (MRSA coverage; target AUC/MIC 400-600) + piperacillin-tazobactam 4.5 g IV q6h (gram-negative and anaerobic coverage) + clindamycin 900 mg IV q8h (toxin suppression)
- Alternative: vancomycin + meropenem 1 g IV q8h + clindamycin 900 mg IV q8h
- Penicillin allergy: vancomycin + aztreonam 2 g IV q8h + metronidazole 500 mg IV q8h + clindamycin 900 mg IV q8h
- Water exposure (Vibrio): add doxycycline 100 mg IV q12h
- Narrow antibiotics based on operative cultures and sensitivities

**Surgical Debridement:**
- Emergent wide excision of all necrotic tissue — aggressive debridement until healthy, bleeding tissue reached at all margins
- Planned re-exploration at 24-48 hours (second-look surgery mandatory)
- Repeat debridement as needed until wound bed is clean
- Wound VAC placement after final debridement

**Supportive Care:**
- ICU admission with invasive monitoring
- Fluid resuscitation — target MAP >= 65, UOP >= 0.5 mL/kg/hr
- Vasopressors — norepinephrine 0.05-0.5 mcg/kg/min IV first-line, add vasopressin 0.03 units/min if refractory
- Blood product resuscitation as needed (massive tissue loss, DIC)
- Nutritional support — high-protein, high-calorie diet (massive protein losses from open wounds)

**Adjuncts (limited evidence):**
- IVIG 1-2 g/kg — for streptococcal toxic shock syndrome (neutralizes superantigens). Observational benefit; no RCT confirmation.
- Hyperbaric oxygen — theoretical benefit for clostridial gas gangrene. Should not delay surgical debridement.

## Disposition

**All NSTI patients require ICU admission and emergent surgical intervention.**

**Mortality Predictors:**
- WBC > 30,000 or < 4,000
- Creatinine > 2 mg/dL
- Lactate > 4 mmol/L
- Age > 60
- Delay to surgery > 12 hours
- Trunk/perineal involvement
- Clostridial etiology

**Transfer:** If current facility lacks surgical capability for wide debridement and ICU care, stabilize with antibiotics and fluids, then emergent transfer. Do not delay transfer for imaging.

**Long-term:**
- Multiple staged debridements, wound care, skin grafting
- Physical therapy/rehabilitation
- Psychological support — significant body image impact

## Pitfalls

1. **Diagnosing cellulitis and discharging with oral antibiotics.** Pain out of proportion to visible findings, systemic toxicity, and rapidly progressing erythema are red flags for NSTI. Cellulitis that worsens despite appropriate antibiotics requires reassessment for NSTI.

2. **Waiting for imaging to confirm the diagnosis before consulting surgery.** CT and MRI can support the diagnosis but cannot reliably exclude early NSTI. Imaging should never delay surgical consultation. A normal CT does not rule out NSTI.

3. **Relying on crepitus as a diagnostic criterion.** Crepitus is present in only 13-31% of NSTI cases. Absence of crepitus does not exclude the diagnosis. Subcutaneous gas is a late finding.

4. **Using a low LRINEC score to exclude NSTI.** LRINEC sensitivity is 68-80%. A score < 6 does not rule out NSTI. Clinical suspicion overrides any scoring system.

5. **Treating with antibiotics alone without surgical debridement.** Antibiotics without source control are uniformly fatal. Devitalized tissue has no blood supply — antibiotics do not penetrate necrotic fascia. Surgery is mandatory.

6. **Omitting clindamycin from the antibiotic regimen.** Clindamycin inhibits bacterial protein synthesis, suppressing exotoxin and superantigen production in GAS. This reduces toxin-mediated organ damage independent of bacterial killing. Standard beta-lactams do not inhibit toxin production.

7. **Not re-exploring at 24-48 hours.** NSTI margins are difficult to define at initial debridement. Planned second-look surgery at 24-48 hours is standard of care. Patients deteriorating postoperatively may need earlier return to OR.

8. **Missing Fournier gangrene.** Perineal/genital necrotizing infection presents with scrotal/vulvar pain, swelling, and erythema. Patients are often embarrassed and may not volunteer genital complaints. Examine the perineum in any septic patient with pelvic, groin, or perianal pain.

9. **Attributing severe pain to anxiety or drug-seeking behavior.** Pain out of proportion is the earliest and most reliable clinical finding. Dismissing severe pain delays diagnosis and increases mortality.
