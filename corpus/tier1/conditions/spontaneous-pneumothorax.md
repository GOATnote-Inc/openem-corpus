---
id: spontaneous-pneumothorax
condition: Spontaneous Pneumothorax
aliases: [primary spontaneous pneumothorax, PSP, secondary spontaneous pneumothorax, SSP, collapsed lung]
icd10: [J93.11, J93.12, J93.0]
esi: 2
time_to_harm: "< 6 hours (SSP); variable (PSP)"
mortality_if_delayed: "1-2% PSP; 10-17% SSP with respiratory failure"
category: respiratory
track: tier1
sources:
  - type: guideline
    ref: "MacDuff A, Arnold A, Harvey J. Management of spontaneous pneumothorax: British Thoracic Society Pleural Disease Guideline 2010. Thorax. 2010;65(Suppl 2):ii18-ii31"
    pmid: "20696690"
  - type: guideline
    ref: "Roberts ME, Rahman NM, Maskell NA, et al. British Thoracic Society Guideline for pleural disease. Thorax. 2023;78(Suppl 3):s1-s42"
    pmid: "37553157"
  - type: guideline
    ref: "Hallifax RJ, Yousuf A, Jones HE, et al. Joint ERS/EACTS/ESTS clinical practice guidelines on adults with spontaneous pneumothorax. Eur Respir J. 2024;63(5):2300797"
    pmid: "38806203"
  - type: pubmed
    ref: "Brown SGA, Ball EL, Perrin K, et al. Conservative versus Interventional Treatment for Spontaneous Pneumothorax. N Engl J Med. 2020;382(5):405-415"
    pmid: "31995686"
  - type: pubmed
    ref: "Baumann MH, Strange C, Heffner JE, et al. Management of spontaneous pneumothorax: an American College of Chest Physicians Delphi consensus statement. Chest. 2001;119(2):590-602"
    pmid: "11171742"
last_updated: "2026-02-19"
compiled_by: agent
risk_tier: B
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
# Spontaneous Pneumothorax

## Recognition

**Definition:** Air in the pleural space without preceding trauma or iatrogenic cause. Classified as primary (PSP) or secondary (SSP) based on presence of underlying lung disease.

### Primary Spontaneous Pneumothorax (PSP)
- Typical patient: tall, thin male, age 15-35, often a smoker
- No clinically apparent underlying lung disease (apical subpleural blebs on CT in >80%)
- Incidence: 7.4-18/100,000 males; 1.2-6/100,000 females per year
- Recurrence: ~30% at 1 year; ~50% lifetime

### Secondary Spontaneous Pneumothorax (SSP)
- Occurs in patients with known lung disease
- Etiologies: COPD (most common), cystic fibrosis, Pneumocystis jirovecii pneumonia, tuberculosis, lung cancer, lymphangioleiomyomatosis (LAM), Marfan syndrome, catamenial (endometriosis-related, menstrual cycle timing)
- Higher morbidity and mortality than PSP due to limited pulmonary reserve
- All SSP require inpatient management regardless of size

### Presentation
- Acute ipsilateral pleuritic chest pain (90%)
- Dyspnea (80%; more severe in SSP due to baseline impairment)
- Tachycardia, tachypnea
- Decreased breath sounds on affected side
- Hyperresonance to percussion
- Decreased tactile fremitus
- Small PSP may present with minimal or no symptoms

### Size Classification (BTS 2010)
- **Small:** < 2 cm interpleural distance at the hilum level on upright PA CXR
- **Large:** >= 2 cm interpleural distance at the hilum level on upright PA CXR
- Note: The 2023 BTS and 2024 ERS/EACTS/ESTS guidelines emphasize symptom severity over size alone for PSP management decisions

### Red Flags for Tension Physiology
- Hemodynamic instability, progressive hypoxia, tracheal deviation, JVD
- See `tension-pneumothorax.md` for full tension pneumothorax management

## Critical Actions

1. **Assess hemodynamic stability immediately.** Unstable patient with pneumothorax = treat as tension until proven otherwise (see tension-pneumothorax.md).
2. **Classify PSP vs SSP.** History of COPD, CF, ILD, or other lung disease determines management pathway.
3. **Determine size on upright CXR.** Measure interpleural distance at hilum level on PA film.
4. **PSP, small (< 2 cm), minimal symptoms:** Needle aspiration first-line. If aspiration fails (re-accumulates to > 2 cm on repeat CXR), place chest tube.
5. **PSP, large (>= 2 cm) or symptomatic:** Needle aspiration or small-bore chest tube (12-16 Fr). 2024 ERS/EACTS/ESTS guideline: strong recommendation for aspiration over chest tube as initial treatment.
6. **SSP, any size:** Chest tube (12-16 Fr small-bore or 16-24 Fr). Aspiration alone has unacceptable failure rate in SSP (> 50%). Admit all SSP patients.
7. **Apply supplemental O2.** High-flow O2 (10-15 L/min via NRB) accelerates pleural air resorption by 4x baseline (nitrogen washout effect). Applicable to all pneumothoraces.
8. **Avoid positive-pressure ventilation unless absolutely necessary.** PPV worsens air leak and risks tension conversion.
9. **Obtain post-procedure CXR** at 2-4 hours to confirm lung re-expansion and tube position.

## Differential Diagnosis

| Condition | Key Differentiators |
|-----------|-------------------|
| Tension pneumothorax | Hypotension, JVD, tracheal deviation, obstructive shock; clinical diagnosis — decompress immediately |
| Pulmonary embolism | Dyspnea + pleuritic pain, but bilateral breath sounds; tachycardia, hypoxia, Wells score, D-dimer, CTPA |
| Acute coronary syndrome | Substernal or pressure-quality pain, ECG changes, troponin; breath sounds normal |
| Musculoskeletal chest pain | Reproducible with palpation, no dyspnea, normal CXR, normal vitals |
| Pericarditis | Positional pleuritic pain (better sitting forward), friction rub, diffuse ST elevation, bilateral breath sounds |
| Pneumomediastinum | Subcutaneous emphysema, Hamman crunch; often post-Valsalva; CXR shows mediastinal air not pleural air |
| Pleural effusion | Dullness to percussion (not hyperresonance), meniscus sign on CXR |
| Acute asthma/COPD exacerbation | Wheezing, bilateral decreased air entry; can coexist with SSP — always CXR |

## Workup

### Imaging
- **Upright PA CXR:** First-line. Visceral pleural line visible with absent lung markings peripherally. Deep sulcus sign on supine films. Measure interpleural distance at hilum.
- **Point-of-care ultrasound (POCUS):** Sensitivity 90-95%, specificity ~99%. Findings: absent lung sliding, absent B-lines, absent lung pulse, "barcode/stratosphere sign" on M-mode. "Lung point" (transition between sliding and non-sliding) is pathognomonic. Superior to supine CXR (sensitivity 40-50%).
- **CT chest:** Not required for straightforward cases. Obtain for: unclear CXR, suspected bullous disease, recurrent pneumothorax, surgical planning, suspected SSP etiology.
- **Expiratory films:** No longer recommended; do not increase diagnostic yield over standard PA.

### Laboratory
- **ABG/VBG:** For SSP or any patient with significant dyspnea/hypoxia. Expect respiratory alkalosis acutely; hypercapnia in SSP with baseline COPD.
- **CBC, BMP:** Baseline.
- **Coagulation studies:** If on anticoagulants or coagulopathy suspected.
- **No specific laboratory test diagnoses pneumothorax.**

### ECG
- Rule out ACS in patients with chest pain. Pneumothorax can cause: right axis deviation, precordial T-wave inversions, decreased R-wave amplitude (mimics anterior ischemia), QRS voltage changes.

## Treatment

### Observation (Conservative Management)
**Indications:** PSP, small (< 2 cm), minimal symptoms, hemodynamically stable, reliable patient.
- 2024 ERS/EACTS/ESTS: conditional recommendation for conservative management in minimally symptomatic PSP regardless of size (based on Brown et al. 2020 PSP trial — 84.6% resolved without intervention).
- Supplemental O2 10-15 L/min via NRB (accelerates resorption from 1.25%/day to ~5%/day of hemithorax volume).
- Repeat CXR at 4-6 hours. If stable or improved and patient reliable, discharge with 24-48 hour follow-up.

### Needle Aspiration
**Indications:** PSP first-line for large or symptomatic pneumothorax (BTS 2010/2023, ERS 2024). NOT recommended as sole therapy for SSP.
- **Technique:** 16-18g IV cannula or dedicated aspiration kit. Site: 2nd ICS MCL or 4th-5th ICS AAL (safe triangle). Prep with chlorhexidine. Local anesthesia: lidocaine 1% 5-10 mL infiltrated to pleura. Advance needle over superior rib border with aspiration. Aspirate with 50 mL syringe via 3-way stopcock. Stop when resistance felt or > 2.5 L aspirated.
- Success rate in PSP: 50-80%. If > 2.5 L aspirated without resolution, stop — likely persistent air leak, proceed to chest tube.
- Repeat CXR immediately post-aspiration.

### Chest Tube (Tube Thoracostomy)
**Indications:** Failed aspiration (PSP), all SSP, large PSP with respiratory compromise, bilateral pneumothorax.
- **Size:** Small-bore (12-16 Fr) pigtail catheter is non-inferior to large-bore for spontaneous pneumothorax. Large-bore (24-28 Fr) only needed if concomitant hemothorax or viscous pleural fluid.
- **Site:** Safe triangle — bounded by anterior border of latissimus dorsi, lateral border of pectoralis major, line superior to horizontal level of nipple, and apex below axilla. Typically 4th-5th ICS, anterior axillary line.
- **Technique (Seldinger for small-bore):** Chlorhexidine prep. Local anesthesia: lidocaine 1% 10-20 mL (max 4.5 mg/kg without epi, 7 mg/kg with epi) infiltrated from skin to pleura. Seldinger technique: needle entry, guidewire, dilator, catheter. Confirm with aspiration of air. Secure with suture and dressing.
- Connect to underwater seal drainage at -10 to -20 cmH2O. Do NOT clamp tube.
- Confirm placement with CXR.

### Heimlich Valve / Ambulatory Management
- One-way flutter valve attached to small-bore chest tube allows outpatient management of selected PSP.
- 2024 ERS/EACTS/ESTS: conditional recommendation for ambulatory management as initial PSP treatment.
- Patient selection: PSP only, reliable patient, no significant comorbidities, lives close to hospital, has responsible companion.
- Instruct to return for persistent air leak > 4 days, worsening dyspnea, fever, or drain dislodgement.

### Pain Management
- Acetaminophen 1000 mg PO/IV q6h (max 4 g/day; 2 g/day if hepatic impairment)
- Ibuprofen 400-600 mg PO q6h with food (avoid if renal impairment)
- Ketorolac 15-30 mg IV q6h (max 120 mg/day, max 5 days)
- Opioids if refractory: fentanyl 25-50 mcg IV q5-10min titrated to effect, or oxycodone 5-10 mg PO q4-6h PRN
- Intercostal nerve block for chest tube pain: bupivacaine 0.25% 5 mL per level, 1 level above and below the tube insertion site

### Recurrence Prevention
- Smoking cessation: reduces recurrence by ~40%. Mandatory counseling.
- Surgical pleurodesis (VATS preferred): for second ipsilateral PSP, first contralateral PSP, bilateral PSP, persistent air leak > 5-7 days, high-risk occupation (pilot, diver).
- Chemical pleurodesis (talc slurry, doxycycline): alternative when surgical risk prohibitive. Doxycycline 500 mg in 50 mL NS via chest tube, clamp 1-2 hours. Talc slurry 5 g in 50 mL NS. Pre-medicate with lidocaine 3 mg/kg (max 250 mg) intrapleural.

## Disposition

### Discharge from ED (PSP Only)
All of the following must be met:
- PSP confirmed (no underlying lung disease)
- Small pneumothorax (< 2 cm) or successful aspiration with post-procedure CXR showing resolution
- Stable or improved on repeat CXR at 4-6 hours
- SpO2 > 96% on room air
- Minimal symptoms, tolerating oral intake
- Reliable patient with transportation and access to follow-up
- Discharge instructions: return immediately for worsening dyspnea, chest pain, fever. No flying until full radiographic resolution + 1 week. No diving until bilateral CT-confirmed resolution + surgical pleurodesis.
- Follow-up: repeat CXR in 24-48 hours, respiratory clinic in 2-4 weeks.

### Admit to Ward
- PSP with failed aspiration requiring chest tube
- PSP with persistent air leak
- Any SSP regardless of size (all SSP patients admitted)
- Bilateral pneumothorax
- Significant comorbidities limiting outpatient safety

### ICU Admission
- Respiratory failure requiring mechanical ventilation
- SSP with hypoxemic or hypercapnic respiratory failure
- Hemodynamic instability
- Tension physiology (see tension-pneumothorax.md)

### Surgical/Thoracic Surgery Referral
- Persistent air leak > 5-7 days
- Recurrent ipsilateral pneumothorax (2nd episode)
- First contralateral pneumothorax
- Bilateral simultaneous pneumothorax
- High-risk occupation (pilot, diver, military)
- Hemothorax associated with spontaneous pneumothorax
- Known large bullae on CT

## Pitfalls

1. **Treating all spontaneous pneumothoraces the same.** SSP carries 10-17% mortality with respiratory failure vs 1-2% for PSP. Every SSP needs a chest tube and admission. Aspiration alone fails in > 50% of SSP.

2. **Relying on supine CXR to exclude pneumothorax.** Supine AP radiographs miss 30-50% of pneumothoraces. Use upright PA film when possible. Use POCUS (absent lung sliding, barcode sign) — sensitivity 90-95% vs 40-50% for supine CXR.

3. **Inserting a large-bore chest tube for uncomplicated spontaneous pneumothorax.** Small-bore (12-16 Fr) pigtail catheters are equally effective and cause less pain. Reserve large-bore (24-28 Fr) for hemopneumothorax or empyema.

4. **Forgetting supplemental high-flow O2.** 100% O2 via NRB increases pleural air resorption rate 4-fold via nitrogen washout gradient. Benefits all pneumothoraces, not just large ones.

5. **Discharging a patient with SSP.** Even small SSP in a COPD patient can decompensate rapidly. Admit all SSP. Limited respiratory reserve means a small pneumothorax produces disproportionate symptoms.

6. **Missing tension physiology in SSP.** COPD patients with hyperinflation and air trapping can develop tension physiology with relatively small pneumothoraces. Monitor closely for hemodynamic compromise.

7. **Clamping the chest tube.** Clamping a chest tube with an active air leak risks tension pneumothorax. The only indication for transient clamping is prior to removal to assess for recurrence, and only under direct monitoring.

8. **Failing to counsel on recurrence and activity restrictions.** PSP recurrence is ~30% at 1 year. Patients must avoid flying until full radiographic resolution plus 1 week (BTS). Scuba diving is permanently contraindicated unless bilateral pleurodesis with normal post-operative CT.

9. **Overlooking catamenial pneumothorax.** Recurrent right-sided pneumothorax in a woman of reproductive age within 72 hours of menses onset. Requires thoracic surgery referral and hormonal suppression, not just chest tube management.

10. **Attributing pneumothorax symptoms in SSP solely to the underlying disease.** COPD patients presenting with "exacerbation" may have an SSP as the precipitant. CXR is mandatory in any COPD patient with acute worsening, especially if unilateral findings on exam.
