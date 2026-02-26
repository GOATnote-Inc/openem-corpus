---
id: acute-appendicitis
condition: Acute Appendicitis
aliases: [appendicitis, appy, acute appy, perforated appendicitis, appendiceal inflammation]
icd10: [K35.80, K35.89, K35.20, K35.21, K35.30, K35.31]
esi: 3
time_to_harm: "< 24 hours"
mortality_if_delayed: "Perforation rate increases 5% per 12-hour delay beyond 36 hours from symptom onset"
category: gastrointestinal
track: tier1
sources:
  - type: guideline
    ref: "2024 WSES Jerusalem Guidelines for Diagnosis and Treatment of Acute Appendicitis. World J Emerg Surg. 2024;19:2"
  - type: pubmed
    ref: "CODA Collaborative. A Randomized Trial Comparing Antibiotics with Appendectomy for Appendicitis. N Engl J Med. 2020;383(20):1907-1919"
    pmid: "33017106"
  - type: guideline
    ref: "ACR Appropriateness Criteria: Right Lower Quadrant Pain — Suspected Appendicitis. 2022"
  - type: pubmed
    ref: "Bhangu A, Søreide K, Di Saverio S, et al. Acute appendicitis: modern understanding of pathogenesis, diagnosis, and management. Lancet. 2015;386(10000):1278-1287"
    pmid: "26460662"
last_updated: "2026-02-18"
compiled_by: agent
risk_tier: C
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
# Acute Appendicitis

## Recognition

### Classic Presentation
- Periumbilical pain migrating to the right lower quadrant (RLQ) over 12-24 hours
- Anorexia, nausea, vomiting (typically after pain onset)
- Low-grade fever (37.5-38.5°C); high fever suggests perforation or abscess
- Localized RLQ tenderness at McBurney point (1/3 distance from ASIS to umbilicus)

### Examination Findings
- **McBurney point tenderness:** Most sensitive exam finding
- **Rovsing sign:** RLQ pain with LLQ palpation (referred peritoneal irritation)
- **Psoas sign:** RLQ pain with right hip extension (retrocecal appendix)
- **Obturator sign:** RLQ pain with internal rotation of flexed right hip (pelvic appendix)
- **Guarding/rigidity:** Localized (early) or diffuse (perforation with peritonitis)
- **Dunphy sign:** Increased pain with coughing

### Atypical Presentations
- **Retrocecal appendix (65%):** Back or flank pain, minimal anterior tenderness, psoas sign positive
- **Pelvic appendix:** Suprapubic pain, urinary frequency, diarrhea, rectal tenderness
- **Pregnant patients:** Pain migrates superiorly with gestational age; RUQ pain in third trimester
- **Elderly:** Blunted inflammatory response, minimal fever, delayed presentation, higher perforation rate (50-70%)
- **Immunosuppressed:** Attenuated signs, delayed diagnosis
- **Children < 5 years:** Irritability, vomiting, diarrhea; perforation rate >80% due to delayed diagnosis

### Scoring Systems
**Alvarado Score (MANTRELS):** Migration (1), Anorexia (1), Nausea/vomiting (1), Tenderness RLQ (2), Rebound (1), Elevation of temperature (1), Leukocytosis (2), Shift to left (1). Score >= 7 = high probability; 5-6 = intermediate; < 5 = low probability.

## Critical Actions

| Action | Target |
|---|---|
| IV access and fluid resuscitation | On arrival |
| Pain management | Within 30 minutes — does NOT mask exam findings |
| CT abdomen/pelvis with IV contrast | For intermediate-probability adults |
| Surgical consultation | Once diagnosis confirmed or high suspicion |
| NPO status | Immediately |
| Antibiotics | Pre-operatively or if perforation suspected |

1. Establish IV access and administer crystalloid for dehydration
2. Provide analgesia: ketorolac 15-30 mg IV or morphine 0.1 mg/kg IV
3. Obtain laboratory studies (CBC, BMP, lipase, urinalysis, pregnancy test)
4. Image based on clinical probability (CT for adults, ultrasound for children and pregnant patients)
5. Consult surgery for confirmed or high-probability appendicitis
6. Administer pre-operative antibiotics for complicated appendicitis

## Differential Diagnosis

- Mesenteric lymphadenitis (children, viral prodrome, clustered lymph nodes on CT)
- Ovarian pathology — torsion, ruptured cyst, ectopic pregnancy (pregnancy test mandatory)
- Meckel diverticulitis (younger patients, difficult to distinguish pre-operatively)
- Crohn disease (chronic symptoms, terminal ileitis on imaging)
- Cecal diverticulitis (older patients, CT distinguishes from appendicitis)
- Ureterolithiasis (colicky flank pain radiating to groin, hematuria)
- Urinary tract infection (dysuria, pyuria; can coexist with appendicitis)
- Right-sided inguinal hernia (incarcerated hernia with bowel obstruction)
- Cholecystitis (RUQ pain, Murphy sign, distinct location)
- Psoas abscess (fever, hip flexion contracture, CT diagnosis)
- Epiploic appendagitis (focal fat stranding on CT, self-limited)

## Workup

- **CBC:** Leukocytosis (WBC > 10,000) in 80-85%; left shift increases specificity. Normal WBC does NOT exclude appendicitis.
- **CRP:** Elevated in >90% after 12 hours of symptoms; normal CRP + normal WBC has high negative predictive value
- **BMP:** Assess dehydration, electrolytes, renal function
- **Urinalysis:** Pyuria/hematuria from adjacent inflammation (does not exclude appendicitis); rule out UTI
- **Pregnancy test:** Mandatory in all women of childbearing age (ectopic pregnancy, imaging decisions)
- **Lipase:** Exclude pancreatitis
- **CT abdomen/pelvis with IV contrast:** Sensitivity 94%, specificity 95%. Findings: dilated appendix >6 mm, wall enhancement, periappendiceal fat stranding, appendicolith, periappendiceal fluid/abscess. Gold standard for adults.
- **Ultrasound:** First-line in children, pregnant patients, and young women. Sensitivity 71-94%. Non-compressible blind-ending tubular structure >6 mm. Operator-dependent.
- **MRI abdomen without contrast:** Second-line for pregnant patients when ultrasound non-diagnostic. Sensitivity 96-97%.
- **Point-of-care ultrasound:** Graded compression technique; useful for rapid bedside assessment but does not replace formal imaging

## Treatment

### Analgesia
- **Ketorolac 15-30 mg IV** (15 mg if age > 65, renal impairment, or <50 kg)
- **Morphine 0.1 mg/kg IV every 4 hours PRN** or **fentanyl 1 mcg/kg IV every 1-2 hours PRN**
- Analgesia does NOT increase perforation risk or obscure physical examination findings — withholding pain medication is not justified

### Antibiotics
**Uncomplicated appendicitis (pre-operative):**
- Cefazolin 2 g IV (3 g if >120 kg) + metronidazole 500 mg IV — single pre-operative dose

**Complicated appendicitis (perforation, abscess, peritonitis):**
- Piperacillin-tazobactam 4.5 g IV every 6 hours
- OR ceftriaxone 2 g IV every 24 hours + metronidazole 500 mg IV every 8 hours
- Continue until afebrile with normal WBC and tolerating PO, then transition to oral amoxicillin-clavulanate 875/125 mg PO BID to complete 4-day total course post-operatively

### Surgical Management
- **Laparoscopic appendectomy:** Standard of care for uncomplicated appendicitis; within 24 hours of diagnosis
- **Nonoperative management with antibiotics alone:** Viable for uncomplicated appendicitis without appendicolith (CODA trial); 29% appendectomy rate at 90 days. Requires shared decision-making and reliable follow-up.
- **Interval appendectomy:** Phlegmon or large abscess (>4-5 cm) — percutaneous drainage + IV antibiotics, followed by interval appendectomy 6-8 weeks later

### Antiemetics
- **Ondansetron 4 mg IV** every 6 hours PRN

## Disposition

- **Operating room:** Confirmed uncomplicated appendicitis — appendectomy within 24 hours
- **ICU:** Septic from perforated appendicitis with peritonitis, hemodynamic instability
- **Surgical admission:** Complicated appendicitis (perforation, abscess) for IV antibiotics ± percutaneous drainage
- **Observation:** Intermediate clinical probability with equivocal imaging; serial abdominal exams every 4-8 hours, repeat imaging if worsening
- **Discharge:** Low probability (Alvarado < 5), negative CT, normal labs, able to tolerate PO, reliable follow-up within 24-48 hours with return precautions

## Pitfalls

1. **Excluding appendicitis based on atypical pain location.** Retrocecal and pelvic appendices cause flank, back, suprapubic, or even left-sided pain. A 65% retrocecal rate means "classic" RLQ presentation is not the majority.

2. **Withholding analgesia to "preserve the exam."** Multiple RCTs demonstrate opioid analgesia does not reduce diagnostic accuracy. Withholding pain medication is unethical and does not improve surgical decision-making.

3. **Relying on WBC alone to exclude appendicitis.** WBC is normal in 15-20% of confirmed appendicitis. CRP adds sensitivity, particularly after 12 hours of symptoms. Normal WBC with normal CRP has a negative predictive value >95%.

4. **Using CT with oral contrast and delaying diagnosis by hours.** IV-contrast-only CT has equivalent sensitivity and specificity to oral + IV contrast for appendicitis. Oral contrast delays diagnosis by 2-4 hours without improving accuracy.

5. **Missing appendicitis in elderly patients.** Elderly patients present with vague pain, minimal fever, and subtle lab findings. Perforation rate is 50-70% in patients >60. Maintain a low threshold for CT imaging.

6. **Failing to obtain a pregnancy test before imaging.** CT radiation and ectopic pregnancy are both concerns. Ultrasound is first-line in pregnant patients; MRI is second-line.

7. **Assuming urinalysis findings exclude appendicitis.** An inflamed retrocecal or pelvic appendix adjacent to the ureter or bladder causes pyuria and hematuria in up to 40% of cases. These findings may coexist with appendicitis.

8. **Dismissing nonoperative management without discussion.** The CODA trial demonstrated antibiotics-first is a viable option for uncomplicated appendicitis without appendicolith. Informed shared decision-making is the standard.

9. **Delaying surgical consultation while awaiting imaging in high-probability cases.** Alvarado >= 7 with classic presentation warrants early surgical consultation concurrent with imaging, not sequential.
