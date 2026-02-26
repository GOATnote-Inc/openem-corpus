---
id: acetaminophen-overdose
condition: Acetaminophen Overdose
aliases: [APAP overdose, paracetamol overdose, Tylenol overdose, APAP toxicity, paracetamol poisoning]
icd10: [T39.1X1A, T39.1X2A, T39.1X4A, K71.10]
esi: 2
time_to_harm: "< 8 hours for NAC efficacy; hepatotoxicity at 24-72 hours"
mortality_if_delayed: "1-2% with early NAC; 5-10% with fulminant hepatic failure"
category: toxicologic
track: tier1
sources:
  - type: guideline
    ref: "American College of Medical Toxicology Position Statement: Updated Guidelines for the Management of Acetaminophen Overdose (2021)"
  - type: pubmed
    ref: "Rumack BH, Bateman DN. Acetaminophen and acetylcysteine dose and duration: past, present and future. Clin Toxicol (Phila) 2012;50(2):91-98"
    pmid: "22320209"
  - type: pubmed
    ref: "Heard KJ. Acetylcysteine for acetaminophen poisoning. N Engl J Med 2008;359(3):285-292"
    pmid: "18635433"
  - type: pubmed
    ref: "Prescott LF et al. Intravenous N-acetylcysteine: the treatment of choice for paracetamol poisoning. BMJ 1979;2(6198):1097-1100"
    pmid: "519312"
  - type: guideline
    ref: "Poison Control Center Clinical Guidance: Acetaminophen Toxicity. AAPCC/ACMT (2022)"
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
  provenance_links: []
---
# Acetaminophen Overdose

## Recognition

**Pathophysiology:** At therapeutic doses, acetaminophen (APAP) is metabolized via glucuronidation and sulfation. In overdose, these pathways saturate and CYP2E1 produces the toxic metabolite NAPQI. Glutathione conjugates NAPQI; when glutathione is depleted (typically at ingestions >150 mg/kg), NAPQI binds hepatocyte proteins causing centrilobular necrosis.

**Stages of Acute Toxicity:**
- **Stage I (0-24h):** Asymptomatic or nonspecific (nausea, vomiting, malaise, diaphoresis). Normal labs. This is the critical treatment window.
- **Stage II (24-72h):** RUQ pain, rising AST/ALT, rising INR, bilirubin. Nausea may resolve (false reassurance).
- **Stage III (72-96h):** Peak hepatotoxicity. AST/ALT may exceed 10,000. Coagulopathy, jaundice, renal failure, encephalopathy. Fulminant hepatic failure possible.
- **Stage IV (96h-2 weeks):** Recovery phase in survivors. Complete hepatic regeneration typical if patient survives.

**Toxic Doses:**
- Acute single ingestion: >150 mg/kg or >7.5g (whichever is less) in a healthy adult
- Repeated supratherapeutic ingestion (RSTI): >150 mg/kg/24h or >6g/24h for 48+ hours
- High-risk patients (chronic alcohol use, malnutrition, CYP2E1 inducers, glutathione depletion): lower thresholds

**Key Point:** Patients present ASYMPTOMATIC during the window when NAC is most effective. A normal-appearing patient with a significant APAP level needs treatment.

## Critical Actions

1. **Draw serum APAP level at 4 hours post-ingestion** (or immediately if presentation >4 hours). Plot on Rumack-Matthew nomogram for acute single ingestions.
2. **Start N-acetylcysteine (NAC) if indicated** — IV NAC: 150 mg/kg in 200 mL D5W over 60 minutes, then 50 mg/kg in 500 mL D5W over 4 hours, then 100 mg/kg in 1000 mL D5W over 16 hours (21-hour IV protocol). PO NAC: 140 mg/kg loading dose, then 70 mg/kg every 4 hours for 17 additional doses (72-hour oral protocol).
3. **Administer activated charcoal** 1g/kg PO (max 50g) if within 1-2 hours of ingestion and patient has a protected airway.
4. **Check hepatic panel, INR, BMP, lactate** — baseline and serial monitoring.
5. **Contact Poison Control** (1-800-222-1222) for co-ingestions, chronic ingestions, or complex scenarios.
6. **Assess for co-ingestants** — APAP overdose frequently accompanies intentional polypharmacy. Screen for salicylates, ethanol, and other coingestants.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Viral hepatitis | Prodromal illness, transaminases rarely >5000, positive viral serologies |
| Alcoholic hepatitis | AST:ALT ratio >2:1, AST rarely >500, chronic alcohol history |
| Other drug-induced hepatotoxicity | Temporal relationship with offending drug, different transaminase pattern |
| Ischemic hepatitis (shock liver) | Preceding hypotension/hypoxia, massive AST/ALT with rapid rise and rapid fall |
| Acute fatty liver of pregnancy | Third trimester, moderate transaminase elevation, hypoglycemia, DIC |
| Mushroom poisoning (Amanita) | Delayed GI symptoms 6-24h after ingestion, progressive hepatic failure |
| Wilson disease (acute) | Young patient, hemolytic anemia, low ceruloplasmin, Kayser-Fleischer rings |

## Workup

**Labs:**
- Serum APAP level — timed at 4 hours post-ingestion for nomogram use. If time of ingestion unknown, draw immediately and treat based on detectable level + clinical scenario.
- AST, ALT — most sensitive marker of hepatotoxicity. Peak typically 72-96h post-ingestion.
- INR/PT — first coagulation marker to rise, reflects synthetic function
- BMP — creatinine for renal injury (APAP causes direct renal tubular toxicity independent of hepatorenal syndrome)
- Venous blood gas with lactate — lactate >3.5 mmol/L after fluid resuscitation is a poor prognostic marker
- Serum phosphate — rising phosphate suggests poor hepatic regeneration (King's College criteria)
- Lipase — if abdominal pain
- Salicylate level, ethanol level — co-ingestion screen
- Urine drug screen — co-ingestion evaluation
- Pregnancy test — affects management
- Ammonia — if encephalopathy suspected (stage III)

**The Rumack-Matthew Nomogram:**
- Applies ONLY to acute single ingestions with a known time of ingestion
- Plot 4-hour APAP level: line starts at 150 mcg/mL at 4 hours, 37 mcg/mL at 12 hours
- Above the treatment line = start NAC
- Does NOT apply to: repeated ingestions, extended-release formulations, unknown ingestion time, chronic ingestions

**Imaging:**
- RUQ ultrasound if hepatomegaly or concern for alternative diagnosis
- CT head if altered mental status (rule out co-ingestion sequelae, cerebral edema)

## Treatment

**N-Acetylcysteine (NAC):**
- Start NAC if: APAP level above treatment line on nomogram, ingestion >150 mg/kg with level pending, any detectable APAP with transaminase elevation, RSTI with detectable APAP and any transaminase elevation, late presentation with evidence of hepatotoxicity
- IV protocol (preferred for vomiting, pregnancy, hepatic failure): 150 mg/kg IV over 60 min, then 50 mg/kg IV over 4h, then 100 mg/kg IV over 16h
- Oral protocol: 140 mg/kg PO loading, then 70 mg/kg PO q4h x 17 doses (total 72h)
- NAC is nearly 100% hepatoprotective when started within 8 hours of acute ingestion
- Continue NAC beyond standard protocol if: AST/ALT rising, INR >2.0, APAP still detectable, clinical hepatotoxicity ongoing

**Anaphylactoid Reaction to IV NAC:**
- Occurs in 10-20% of patients (dose-related, during first infusion)
- Flushing, urticaria, pruritus, bronchospasm, angioedema
- STOP infusion. Treat: diphenhydramine 50 mg IV, epinephrine 0.3 mg IM if bronchospasm/angioedema
- Restart NAC at slower rate (first bag over 60 min instead of 15-60 min) once symptoms controlled. NAC is NOT contraindicated — reaction is anaphylactoid, not true allergy.

**GI Decontamination:**
- Activated charcoal 1 g/kg PO (max 50g) within 1-2 hours of ingestion
- Effective at reducing absorption if given early; less useful after 2 hours
- Contraindicated if altered mental status without protected airway, caustic co-ingestion, or bowel obstruction

**Fulminant Hepatic Failure:**
- Criteria for transplant evaluation (King's College): pH < 7.3 after resuscitation, OR all three: INR >6.5, creatinine >3.4 mg/dL, grade III/IV encephalopathy
- Continue IV NAC (improves survival even in established hepatic failure)
- Dextrose infusion for hypoglycemia (hepatic glycogen depleted)
- FFP/vitamin K for active bleeding only — do not correct INR prophylactically (masks progression)
- Lactulose 30 mL PO q2h for encephalopathy (target 3-4 stools/day)
- Emergent hepatology and transplant surgery consultation

## Disposition

**Admit to ICU:**
- ALT >1000, INR >2.0
- Encephalopathy
- Metabolic acidosis, elevated lactate
- Fulminant hepatic failure
- Active NAC infusion with anaphylactoid reaction requiring monitoring

**Admit to Floor/Observation:**
- NAC treatment initiated — complete the 21-hour IV or 72-hour PO protocol
- Co-ingestion requiring monitoring
- Psychiatric evaluation for intentional overdose (medical clearance first)

**Discharge Criteria (must meet ALL):**
- APAP level below treatment line on nomogram at appropriate time point
- Normal AST, ALT, INR
- Asymptomatic
- Psychiatric safety assessment completed (if intentional)
- Reliable follow-up

## Pitfalls

1. **Discharging an asymptomatic patient without checking an APAP level.** Stage I toxicity is asymptomatic. An undisclosed or unrecognized APAP ingestion that presents late has high mortality. Check APAP levels on all intentional ingestions and unexplained transaminase elevations.

2. **Plotting a level on the nomogram for a repeated supratherapeutic ingestion.** The Rumack-Matthew nomogram applies ONLY to acute single ingestions with known timing. RSTI requires a different approach: any detectable APAP level with transaminase elevation warrants NAC.

3. **Waiting for the 4-hour level to decide on activated charcoal.** Charcoal must be given within 1-2 hours of ingestion to be effective. Give charcoal early if the ingestion history supports a toxic dose.

4. **Stopping NAC after the standard protocol despite worsening labs.** Continue NAC if AST/ALT are rising, INR >2.0, or APAP remains detectable. The 21-hour IV protocol is a minimum, not a fixed endpoint.

5. **Assuming the nomogram catches all at-risk patients.** Chronic alcohol users, malnourished patients, and those on CYP2E1 inducers (isoniazid, phenytoin, phenobarbital) have depleted glutathione and develop toxicity at lower doses. Use a lower threshold for NAC.

6. **Correcting INR prophylactically with FFP.** INR is the most sensitive prognostic marker in APAP hepatotoxicity and a key component of King's College criteria. Correcting it prophylactically masks progression toward transplant criteria. Reserve FFP for active bleeding.

7. **Failing to screen for co-ingestants.** APAP overdose in the intentional setting frequently involves multiple drugs. Check salicylate level, ethanol, and a urine drug screen. Unrecognized co-ingestions kill.

8. **Dismissing an anaphylactoid reaction to NAC as a reason to withhold treatment.** Anaphylactoid reactions to IV NAC are common (10-20%), dose-related, and manageable. Stop the infusion, treat symptoms, then restart at a slower rate. NAC remains indicated — the reaction is not a contraindication.

9. **Missing extended-release acetaminophen formulations.** Extended-release products have delayed and prolonged absorption. A single 4-hour level may be misleading. Obtain a second APAP level at 8-10 hours. If either level is above the treatment line, start NAC.
