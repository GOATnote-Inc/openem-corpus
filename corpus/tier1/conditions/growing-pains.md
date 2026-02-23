---
id: growing-pains
condition: Growing Pains
aliases: [benign limb pain of childhood, recurrent limb pain]
icd10: [M79.3]
esi: 5
time_to_harm: "N/A — benign functional pain syndrome of childhood; see escalation_triggers for emergency differential"
category: pediatric
track: tier1
disposition_default: outpatient
escalation_triggers:
  - "Limp or refusal to bear weight — septic arthritis, osteomyelitis, Legg-Calvé-Perthes disease, or slipped capital femoral epiphysis (SCFE) until excluded"
  - "Joint swelling, warmth, or erythema — septic arthritis (monoarticular joint effusion = emergent aspiration and orthopedic consultation)"
  - "Systemic symptoms: fever, weight loss, or night sweats — septic arthritis, osteomyelitis, or malignancy"
  - "Persistent bone tenderness on direct palpation (point tenderness over bone, not muscle) — stress fracture, osteomyelitis, or bone malignancy"
  - "Lymphadenopathy or hepatosplenomegaly — leukemia, lymphoma"
  - "Abnormal CBC: anemia, thrombocytopenia, leukocytosis or leukopenia — leukemia evaluation mandatory"
  - "Pain localized to a single joint with systemic illness — septic arthritis (emergency — delay to aspiration and antibiotics results in permanent joint destruction)"
  - "Pain that is unilateral and persistent (not bilateral, recurrent, and resolving) — organic cause requires workup"
confusion_pairs:
  - condition: septic-arthritis
    differentiators:
      - "Growing pains: bilateral, symmetric, muscle-distribution (thighs, calves, behind knees); no joint swelling; no warmth or erythema; child bears weight normally; afebrile; normalizes by morning"
      - "Septic arthritis: monoarticular (single joint); fever; refusal to bear weight or move joint; joint effusion (swelling, warmth, erythema); WBC elevated; ESR and CRP markedly elevated; Kocher criteria (fever, non-weight-bearing, ESR >40, WBC >12,000) — ≥3 criteria = >93% probability of septic arthritis requiring operative washout"
      - "Growing pains: relieved by massage and parental reassurance; no objective joint findings; symmetric bilateral distribution"
      - "Septic arthritis: any range of motion of affected joint is painful and resisted; ultrasound shows joint effusion; synovial fluid >50,000 WBC/mm³ with PMN predominance"
      - "Critical rule: a child with fever + monoarticular joint symptoms has septic arthritis until proven otherwise — growing pains never cause fever or joint findings"
  - condition: leukemia
    differentiators:
      - "Growing pains: bilateral symmetrical muscular distribution; episodic; child is well-appearing between episodes; no lymphadenopathy; normal CBC"
      - "Leukemia (ALL — most common pediatric malignancy): persistent bone pain (often nocturnal); migratory; associated pallor, easy bruising, petechiae, lymphadenopathy, hepatosplenomegaly; abnormal CBC (anemia, thrombocytopenia, elevated or depressed WBC, circulating blasts on smear)"
      - "Growing pains: no hematologic abnormalities; no constitutional symptoms; pain bilateral and episodic with complete resolution between episodes"
      - "Leukemia: pain may be periosteal (bony tenderness on palpation) vs. growing pains which are muscular in distribution; radiology may show metaphyseal lucent bands ('leukemic lines') on plain film"
      - "Critical rule: order CBC before discharging any child with recurrent limb pain — leukemia can masquerade as growing pains; an abnormal CBC mandates urgent hematology consultation"
sources:
  - type: pubmed
    ref: "Uziel Y, Hashkes PJ. Growing pains in children. Pediatr Rheumatol Online J. 2007;5:5."
    pmid: "17550631"
  - type: pubmed
    ref: "Evans AM, Scutter SD. Prevalence of 'growing pains' in young children. J Pediatr. 2004;145(2):255-258."
    pmid: "15289779"
  - type: pubmed
    ref: "Hashkes PJ, Friedland O, Mathew D, et al. Decreased pain threshold in children with growing pains. J Rheumatol. 2004;31(3):610-613."
    pmid: "14994407"
  - type: pubmed
    ref: "Kocher MS, Zurakowski D, Kasser JR. Differentiating between septic arthritis and transient synovitis of the hip in children: an evidence-based clinical prediction algorithm. J Bone Joint Surg Am. 1999;81(12):1662-1670."
    pmid: "10608376"
  - type: pubmed
    ref: "Lowe RM, Hashkes PJ. Growing pains: a noninflammatory pain syndrome of early childhood. Nat Clin Pract Rheumatol. 2008;4(10):542-549."
    pmid: "18762798"
  - type: guideline
    ref: "American Academy of Pediatrics. Pediatric musculoskeletal evaluation: clinical resources and guidelines for limb pain in children. AAP; 2020."
last_updated: "2026-02-23"
compiled_by: agent
risk_tier: C
validation:
  schema_version: "2.0"
  automated_consistency_check: null
  dose_range_validator: null
  unit_normalization_check: null
  cross_file_consistency_check: null
  citation_presence_check: null
  duplicate_content_check: null
  outlier_detection_flag: clear
  guideline_version_reference: "AAP pediatric musculoskeletal resources 2020; Kocher criteria 1999 (validated)"
  provenance_links: []
---

## Recognition

Growing pains is a benign, functional pain syndrome of childhood characterized by recurrent, bilateral lower extremity muscle pain occurring in the late afternoon or evening, resolving by morning. It affects 10-37% of children aged 3-12 years. The cause is incompletely understood; current evidence supports a lower pain threshold (central sensitization) and possibly fatigue-related muscle pain after active days, rather than bone growth itself.

Growing pains is a diagnosis of exclusion — the primary emergency medicine task is to exclude septic arthritis, osteomyelitis, malignancy, and other organic causes before attributing recurrent limb pain to this benign condition.

### Diagnostic Criteria (Peterson Criteria)
All four criteria must be met:
1. **Bilateral pain**: always involves both legs (unilateral pain is a red flag)
2. **Muscle distribution**: thighs, calves, or behind the knees — NOT joint-localized
3. **Evening/night onset**: occurs in the late afternoon or evening; child may wake from sleep with pain
4. **Complete resolution by morning**: child wakes well; no morning stiffness, no limp
5. **Normal physical examination**: no joint swelling, tenderness is muscular not bony, no lymphadenopathy

### Typical Clinical Features
- Age: most common 3-5 years and 8-12 years; uncommon before age 2 or after puberty
- Pain: aching, cramping quality in thigh muscles, calf muscles, or posterior knee (popliteal fossa)
- Timing: characteristically late afternoon, evening, or nocturnal; not present in the morning
- Bilateral symmetry: both legs involved, though one may be worse than the other on a given night
- Intermittent: multiple symptom-free days between episodes (not daily continuous pain)
- Response to massage: dramatic improvement with parental massage is characteristic
- Normal daytime function: child runs, jumps, and plays normally during the day; no daytime limp
- No fever, no systemic symptoms

### Red Flags That Exclude the Diagnosis
- Fever (any temperature elevation)
- Limping or refusal to bear weight
- Joint swelling, warmth, or erythema
- Bone tenderness on direct palpation (point tenderness on bone — not muscular)
- Unilateral pain (growing pains is always bilateral)
- Lymphadenopathy or organomegaly
- Abnormal CBC
- Persistent daily pain without symptom-free intervals
- Pain present in the morning with stiffness

## Critical Actions

1. Obtain vital signs including temperature — fever excludes growing pains and mandates septic arthritis workup.
2. Perform a full musculoskeletal examination: range of motion of hip, knee, and ankle joints; palpate along bone cortex for point tenderness; assess for joint effusion; observe gait if the child can ambulate.
3. Assess weight-bearing and gait: any limp or refusal to bear weight requires imaging and orthopedic evaluation.
4. Examine for lymphadenopathy (anterior cervical, axillary, inguinal) and hepatosplenomegaly — their presence mandates urgent CBC.
5. Apply Kocher criteria if hip involvement is possible: fever (temperature >38.5°C), non-weight-bearing, ESR >40 mm/hr, WBC >12,000/mm³ — ≥3 criteria = high probability of septic arthritis requiring operative washout.
6. Order CBC with differential before discharge if there is any uncertainty — leukemia is more common than growing pains after age 12 and can present identically.

## When NOT to Escalate

Growing pains is appropriate for outpatient management when ALL of the following are met:
- Afebrile (temperature <38.0°C at triage and on re-check)
- Child bears weight normally and ambulates without limp
- No joint swelling, warmth, or erythema
- No bone point tenderness on palpation (muscular tenderness only, bilateral)
- No lymphadenopathy, no hepatosplenomegaly
- CBC is normal (if obtained) — no anemia, no thrombocytopenia, no circulating blasts
- Pain is bilateral, muscular distribution (thighs/calves/posterior knee), evening/night onset
- Complete resolution by morning with no residual symptoms on the day of presentation
- Prior identical episodes with same bilateral evening pattern

Reassurance, massage, and analgesics are the entire treatment. ED imaging and labs are not required in classic presentations meeting all of the above criteria.

## Differential Diagnosis

| Condition | Key Features | Distinguishing from Growing Pains |
|-----------|-------------|----------------------------------|
| **Septic arthritis** | Monoarticular; fever; non-weight-bearing; joint effusion (swelling, warmth, erythema); elevated WBC, ESR, CRP | Growing pains: bilateral muscular; afebrile; weight-bearing normal; no joint findings; normal inflammatory markers |
| **Leukemia (ALL)** | Persistent bone pain (often nocturnal); pallor, bruising, lymphadenopathy, hepatosplenomegaly; abnormal CBC | Growing pains: episodic with symptom-free intervals; no hematologic abnormalities; no constitutional symptoms |
| **Osteomyelitis** | Localized bone pain and tenderness; fever; elevated WBC, ESR, CRP; positive blood culture in 40-60%; MRI confirms | Growing pains: no bony point tenderness; afebrile; bilateral; normal labs |
| **Transient synovitis (irritable hip)** | Most common cause of hip pain in children 3-10 years; unilateral hip pain and limp; mild or no fever; hip effusion on ultrasound; WBC/ESR low-moderate | Growing pains: bilateral; no joint findings; not localized to hip; Kocher score distinguishes from septic arthritis |
| **Legg-Calvé-Perthes (LCP)** | Avascular necrosis of femoral head; unilateral hip or knee pain; limp; limited internal rotation of hip; plain film shows femoral head flattening | Growing pains: bilateral; no hip-specific findings; normal plain film |
| **SCFE (Slipped Capital Femoral Epiphysis)** | Adolescent, often obese; unilateral hip/knee pain; limp; obligate external rotation; Klein's line abnormal on AP hip film | Growing pains: younger age group (3-12); bilateral; no mechanical hip findings |
| **Juvenile idiopathic arthritis (JIA)** | Morning stiffness >6 weeks; joint swelling; may be oligoarticular; elevated ANA; chronic course | Growing pains: morning improvement (not stiffness); no synovitis; episodic; normal labs |
| **Hypermobility syndrome (benign joint hypermobility)** | Joint pain after activity; Beighton hypermobility score ≥4; no synovitis; may overlap with growing pains | Growing pains: assess Beighton score; hypermobility warrants physiotherapy for joint stabilization |
| **Stress fracture** | Repetitive loading (sports); point bony tenderness; positive tuning fork test; plain film often normal early; MRI confirms | Growing pains: no bony tenderness; bilateral; no activity-loading correlation |

## Workup

### No Workup Required (Classic Growing Pains)
- Afebrile, weight-bearing, bilateral muscular pain, evening/night onset, complete morning resolution, no joint findings, no lymphadenopathy, no constitutional symptoms, prior identical episodes
- No lab work or imaging required in this presentation

### When to Order Labs
- **CBC with differential**: any uncertainty about diagnosis; any lymphadenopathy or organomegaly; any pallor or easy bruising; first presentation in child >10 years (leukemia is more prevalent beyond the peak growing pains age range)
- **ESR and CRP**: fever or any inflammatory signs to calculate Kocher score and gauge probability of septic arthritis
- **WBC**: Kocher criteria (WBC >12,000 = 1 point toward septic arthritis diagnosis)

### Imaging
- **Plain radiograph of affected joints (AP + lateral)**: any limp, joint swelling, bony tenderness, or unilateral presentation — screens for SCFE, LCP, fracture, malignant bone lesion
- **Hip ultrasound**: if hip pain or antalgic gait — detects joint effusion (differentiates transient synovitis from septic arthritis in combination with Kocher criteria)
- **MRI (outpatient or urgent)**: osteomyelitis (not visible on plain film for 7-10 days); bone tumor; LCP (early avascular necrosis)
- **Bone scan**: widespread bone pain with suspected osteomyelitis or malignancy when MRI not immediately available

## Treatment

### Reassurance (Most Important Intervention)
- Explain that growing pains are real (not imagined), benign, and self-limited
- Pain episodes typically resolve spontaneously by adolescence
- Parental anxiety about "something serious" often drives ED presentation — address explicitly

### Massage
- Firm massage to the affected muscles during episodes dramatically reduces pain in most children
- Parents should be instructed in technique: sustained deep pressure along thigh and calf muscles for 5-10 minutes
- This is the most consistently effective acute intervention

### Analgesics
- **Ibuprofen 10 mg/kg PO** (children; max 400 mg per dose; max 40 mg/kg/day or 2400 mg/day): first-line analgesic for acute episodes; anti-inflammatory effect may benefit fatigue-related muscle inflammation; give with food
- **Acetaminophen 15 mg/kg PO** (children; max 1000 mg per dose; max 75 mg/kg/day or 4000 mg/day): alternative or adjunct; appropriate when NSAIDs are contraindicated
- Analgesics are for acute episode management — do not encourage daily prophylactic use
- Prophylactic ibuprofen at bedtime during active periods has been described but has limited evidence and is not standard practice

### Stretching
- Daily stretching of quadriceps, hamstrings, and calf muscles reduces episode frequency in some children
- Refer to pediatrician for ongoing stretching program guidance

## Disposition

### Discharge (Standard)
- Classic growing pains meeting all criteria: discharge with reassurance, massage instruction, ibuprofen prescription, return precautions, and primary care follow-up
- Provide written return precautions

### Return Precautions
- Limping or refusal to bear weight
- Joint swelling, warmth, or redness
- Fever at any point
- Pain present in the morning (not resolved by morning)
- Easy bruising or bleeding gums
- Swollen lymph nodes in neck, armpits, or groin
- Pain that is consistently localized to one leg only
- Child appears pale, fatigued, or unwell between pain episodes

### Follow-up
- Pediatrician within 1-2 weeks: confirm diagnosis in follow-up setting, track symptom pattern, review CBC results if ordered, provide parent education on home management
- Pediatric orthopedics or rheumatology: if diagnosis is uncertain after workup or symptoms are atypical

## Pitfalls

1. **Discharging a child with leukemia diagnosed as "growing pains" because the CBC was not checked.** Acute lymphoblastic leukemia (ALL), the most common pediatric malignancy, can present with bilateral lower extremity pain, nocturnal pain, and a well-appearing child between episodes — identical to growing pains. The CBC is the critical discriminating test. Abnormal findings (anemia, thrombocytopenia, elevated WBC, blasts on smear) require immediate hematology consultation. A normal CBC provides meaningful reassurance. For any first presentation of recurrent bilateral limb pain, or any child >8 years, the threshold for CBC should be very low.

2. **Missing septic arthritis because the child has "bilateral pains."** Growing pains is bilateral; septic arthritis is monoarticular. But parents often present a child saying "both legs hurt" when one joint is acutely infected and the other has incidental baseline growing pains. The critical examination is joint-specific: assess each knee, hip, and ankle individually for swelling, warmth, erythema, and range-of-motion-induced pain. Any monoarticular joint finding — even in the context of bilateral pain history — mandates septic arthritis workup.

3. **Attributing nocturnal pain that wakes a child from sleep entirely to growing pains.** Growing pains classically occur in the evening/night, and children may be roused from sleep. However, bone pain from malignancy also wakes children from sleep — this feature is often highlighted in oncology literature as a red flag. The distinction lies in the other features: growing pains is bilateral, muscular, and associated with a normal examination and normal labs. Pain waking from sleep is not pathognomonic of growing pains and should not be used as reassurance in isolation.

4. **Not informing parents of return precautions.** Growing pains is managed entirely in the outpatient setting, but the diagnosis can be mimicked by several serious conditions that evolve over days. Parents must know to return immediately for limping, joint swelling, fever, or pallor/bruising — the development of any of these features after a "growing pains" diagnosis is a red flag requiring urgent re-evaluation.

5. **Prescribing muscle relaxants for growing pains.** Cyclobenzaprine and other skeletal muscle relaxants are not appropriate for growing pains in children. They are not approved in children <15 years for this indication, have significant sedation risk, and do not address the pathophysiology. Ibuprofen and massage are the appropriate acute treatments.
