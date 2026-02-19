---
id: septic-arthritis
condition: Septic Arthritis
aliases: [septic joint, infectious arthritis, pyogenic arthritis, bacterial arthritis, gonococcal arthritis]
icd10: [M00.9]
esi: 2
time_to_harm: "< 24 hours"
mortality_if_delayed: "Irreversible joint destruction within 24-48 hours; 11% mortality in non-gonococcal septic arthritis"
category: musculoskeletal
track: tier1
sources:
  - type: review
    ref: "Long B, Koyfman A, Gottlieb M. Evaluation and Management of Septic Arthritis and its Mimics in the Emergency Department. West J Emerg Med. 2019;20(2):331-341"
    pmid: "30881554"
  - type: review
    ref: "Margaretten ME, Kohlwes J, Moore D, Bent S. Does This Adult Patient Have Septic Arthritis? JAMA. 2007;297(13):1478-1488"
    pmid: "17405973"
  - type: review
    ref: "Ross JJ. Septic Arthritis of Native Joints. Infect Dis Clin North Am. 2017;31(2):203-218"
    pmid: "28366221"
  - type: review
    ref: "Sharff KA, Richards EP, Townes JM. Clinical Management of Septic Arthritis. Curr Rheumatol Rep. 2013;15(6):332"
    pmid: "23591823"
  - type: pubmed
    ref: "Kocher MS, Zurakowski D, Kasser JR. Differentiating Between Septic Arthritis and Transient Synovitis of the Hip in Children: An Evidence-Based Clinical Prediction Algorithm. J Bone Joint Surg Am. 1999;81(12):1662-1670"
    pmid: "10608376"
last_updated: "2026-02-19"
compiled_by: agent
risk_tier: B
validation:
  schema_version: "2.0"
  automated_consistency_check: null
  dose_range_validator: null
  unit_normalization_check: null
  cross_file_consistency_check: null
  citation_presence_check: null
  duplicate_content_check: null
  outlier_detection_flag: clear
  guideline_version_reference: null
  provenance_links: []
---
# Septic Arthritis

## Recognition

**Definition:** Bacterial infection of a joint space causing acute inflammatory arthritis. Untreated, proteolytic enzymes and inflammatory mediators destroy articular cartilage within 24-48 hours, leading to permanent joint damage, osteomyelitis, or sepsis.

**Classic Presentation:**
- Acute monoarticular hot, swollen, erythematous joint with severe pain on passive range of motion
- Fever present in ~60% (absence does not exclude diagnosis)
- Knee is most commonly affected (~50%), followed by hip, shoulder, ankle, wrist
- Patient resists any active or passive movement of the joint

**Microbiology:**
- **Non-gonococcal:** Staphylococcus aureus is the most common organism (~75% of cases). MRSA prevalence increasing (up to 40% in some regions). Streptococcal species account for ~15%.
- **Gonococcal:** Most common cause in young sexually active adults (ages 15-40). Neisseria gonorrhoeae. Two presentations:
  - Bacteremic phase: migratory polyarthralgia, dermatitis (painless pustules on distal extremities), tenosynovitis (especially dorsal hand/wrist)
  - Localized phase: purulent monoarthritis (knee, wrist, ankle)
- **Gram-negative rods:** IV drug users, elderly, immunocompromised
- **Pediatric:** S. aureus (>2 years), Kingella kingae (<5 years), Group B Strep (neonates)

**Risk Factors:**
- Pre-existing joint disease (rheumatoid arthritis — strongest risk factor, OR 4.0)
- Prosthetic joint
- Recent joint injection or surgery
- IV drug use
- Immunosuppression (diabetes, HIV, chronic steroids, biologics)
- Skin infection/cellulitis overlying a joint
- Advanced age (>80 years)
- Bacteremia from any source

**Pediatric Considerations — Kocher Criteria (Hip):**
Used to differentiate septic arthritis from transient synovitis in children with hip pain:
1. Fever > 38.5 C
2. Non-weight-bearing on affected side
3. ESR > 40 mm/hr
4. Serum WBC > 12,000 cells/mm3

| Kocher Predictors Present | Predicted Probability of Septic Arthritis |
|--------------------------|------------------------------------------|
| 0 | < 0.2% |
| 1 | 3% |
| 2 | 40% |
| 3 | 93% |
| 4 | 99.6% |

Caird added CRP > 20 mg/L as a 5th criterion (98% probability with all 5 present).

## Critical Actions

1. **Aspirate the joint before antibiotics** -- arthrocentesis is the single most important diagnostic step. Send synovial fluid for cell count with differential, Gram stain, culture (aerobic and anaerobic), and crystal analysis.
2. **Start empiric IV antibiotics immediately after aspiration** -- do not delay for culture results. Joint destruction progresses hourly.
3. **Orthopedic consultation** -- for definitive irrigation and debridement (I&D). All septic joints ultimately require surgical washout; serial bedside aspiration is an alternative only when operative I&D is not immediately available or for gonococcal arthritis responding to antibiotics.
4. **Hip joint septic arthritis is a surgical emergency** -- hip cannot be adequately aspirated at bedside in most cases; fluoroscopic or ultrasound-guided aspiration or operative drainage required. Delayed drainage of hip septic arthritis leads to avascular necrosis of the femoral head.
5. **Immobilize the joint** -- splint in position of comfort to reduce pain.
6. **Blood cultures x2** -- positive in 25-50% of non-gonococcal septic arthritis.
7. **Assess for concurrent osteomyelitis** -- contiguous spread is common, especially in hip and shoulder infections.
8. **In children with hip pain and any Kocher criteria** -- ultrasound of the hip to look for effusion; if effusion present with >= 2 Kocher criteria, aspirate under image guidance.

## Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **Gout (monoarticular)** | Acute monoarthritis, often 1st MTP (podagra); negatively birefringent monosodium urate crystals on polarized microscopy; prior attacks common; tophi may be present. NOTE: gout and septic arthritis CAN coexist -- always send cultures even if crystals found |
| **Pseudogout (CPPD)** | Calcium pyrophosphate dihydrate crystals -- positively birefringent, rhomboid-shaped; knee and wrist most common; chondrocalcinosis on X-ray; older patients. Can coexist with infection |
| **Reactive arthritis** | Oligoarthritis 1-4 weeks after GI or GU infection; sterile joint fluid; may have conjunctivitis, urethritis, enthesitis; HLA-B27 association |
| **Lyme arthritis** | Monoarthritis (knee) in endemic area; history of tick bite or erythema migrans; positive Lyme serologies; synovial fluid WBC typically 25,000-50,000 (lower than septic arthritis); PCR for Borrelia in synovial fluid |
| **Traumatic hemarthrosis** | History of trauma; bloody synovial fluid; radiographs may show fracture. If lipohemarthrosis (fat droplets on aspirate), intra-articular fracture is present |
| **Rheumatoid arthritis flare** | Polyarticular, symmetric, chronic history; elevated RF/anti-CCP; sterile synovial fluid but can have elevated WBC; joint involvement pattern differs |
| **Osteoarthritis flare** | Chronic joint pain, mechanical symptoms, Heberden/Bouchard nodes; synovial fluid WBC usually < 2,000; radiographic joint space narrowing and osteophytes |
| **Transient synovitis (pediatric)** | Child 3-8 years, hip pain, low-grade/no fever, able to bear some weight; diagnosis of exclusion after septic arthritis ruled out via Kocher criteria and aspiration if indicated |

## Workup

**Arthrocentesis (mandatory):**
- Aspirate the joint BEFORE antibiotics whenever possible
- Send for: cell count with differential, Gram stain, culture (aerobic + anaerobic), crystal analysis
- Synovial fluid interpretation:

| Parameter | Normal | Non-inflammatory | Inflammatory | Septic |
|-----------|--------|-----------------|-------------|--------|
| WBC/mm3 | < 200 | 200-2,000 | 2,000-50,000 | > 50,000 (often > 100,000) |
| PMN % | < 25% | < 25% | > 50% | > 90% |
| Gram stain | Negative | Negative | Negative | Positive in 50-75% (non-gonococcal); < 25% (gonococcal) |
| Culture | Negative | Negative | Negative | Positive in 70-90% (non-gonococcal); < 50% (gonococcal) |

- **WBC > 50,000 with > 90% PMNs is highly suggestive but not diagnostic** -- crystal arthropathies can produce counts this high
- **WBC < 50,000 does not exclude septic arthritis** -- immunocompromised patients, early infection, or partially treated infection can have lower counts
- **Lactate > 10 mmol/L in synovial fluid** increases specificity for bacterial infection (LR+ 2.3)

**Labs:**
- CBC with differential -- leukocytosis (often > 10,000; may be normal)
- ESR (sensitivity ~90% but nonspecific) and CRP (sensitivity ~95%) -- most useful as negative predictors; normal ESR AND CRP make septic arthritis unlikely (NPV ~95%)
- Blood cultures x2 (positive in 25-50%)
- BMP -- baseline renal function before antibiotic dosing
- Lactate -- if systemic sepsis suspected
- Uric acid -- if gout in differential (but elevated uric acid does not exclude septic arthritis)
- Gonorrhea/chlamydia NAAT (urine, pharynx, rectum) -- if gonococcal arthritis suspected
- Procalcitonin -- serum > 0.5 ng/mL increases likelihood of septic arthritis (LR+ 3.3)

**Imaging:**
- **X-ray** of the affected joint -- soft tissue swelling, joint effusion, periarticular osteopenia. Normal X-ray does not exclude diagnosis. May show chondrocalcinosis (pseudogout) or erosions (chronic gout)
- **Ultrasound** -- detects joint effusion (sensitivity > 90% for hip and knee); guides aspiration; cannot differentiate septic from sterile effusion
- **MRI** -- most sensitive for early osteomyelitis, periarticular abscess, soft tissue extension. Not needed for ED diagnosis but valuable if contiguous osteomyelitis or abscess suspected
- **CT** -- useful for deep joints (sacroiliac, sternoclavicular) that are difficult to aspirate clinically

## Treatment

### Empiric Antibiotic Regimens (Start Immediately After Aspiration)

**Non-gonococcal (standard empiric):**
- **Vancomycin 15-20 mg/kg IV q8-12h** (target trough 15-20 mcg/mL) -- covers MRSA and MSSA
  - PLUS ceftriaxone 2 g IV q24h if gram-negative coverage needed (elderly, immunocompromised, IV drug use)
- Alternative if MRSA low prevalence and Gram stain shows gram-positive cocci in clusters: **cefazolin 2 g IV q8h**

**Gram stain directed (when available):**

| Gram Stain Finding | Recommended Antibiotic |
|--------------------|----------------------|
| Gram-positive cocci in clusters (Staph) | Vancomycin 15-20 mg/kg IV q8-12h |
| Gram-positive cocci in chains (Strep) | Ceftriaxone 2 g IV q24h |
| Gram-negative bacilli | Ceftriaxone 2 g IV q24h OR cefepime 2 g IV q8h |
| No organisms seen (non-gonococcal) | Vancomycin 15-20 mg/kg IV q8-12h + ceftriaxone 2 g IV q24h |

**Gonococcal arthritis:**
- **Ceftriaxone 1 g IV q24h** (transition to PO cefixime 400 mg BID after clinical improvement)
- PLUS azithromycin 1 g PO x1 (for presumptive chlamydia co-infection)
- Test and treat sexual partners

**Pediatric dosing:**
- Cefazolin 25 mg/kg IV q8h (max 2 g/dose) for empiric coverage in children > 3 months
- Add vancomycin 15 mg/kg IV q6h if MRSA risk factors or critically ill
- Neonates (< 3 months): vancomycin + cefotaxime (or gentamicin)

**Prosthetic joint infection:**
- Vancomycin 15-20 mg/kg IV q8-12h + ceftazidime 2 g IV q8h (covers Pseudomonas)
- Urgent orthopedic consultation -- likely requires operative debridement with component exchange

### Surgical Management
- **Operative irrigation and debridement** -- standard of care for all non-gonococcal septic arthritis
- **Serial arthrocentesis** -- acceptable alternative for accessible joints (knee) responding to antibiotics; requires daily aspiration until effusion resolves
- **Hip, shoulder, and pediatric septic joints** -- operative I&D is mandatory (closed spaces, risk of AVN)
- **Arthroscopic vs. open** -- orthopedic surgeon preference; arthroscopic washout adequate for most native joint infections

### Supportive Care
- Immobilize in position of comfort (splint)
- IV analgesia: morphine 0.1 mg/kg IV q4h PRN or ketorolac 15-30 mg IV q6h (max 5 days)
- IV fluid resuscitation if septic
- DVT prophylaxis if immobilized: enoxaparin 40 mg SC daily

## Disposition

### Admit (All Confirmed or Suspected Septic Arthritis)
- All patients with confirmed or high-suspicion septic arthritis require admission
- Orthopedic surgery consultation for operative I&D
- IV antibiotics (typical duration: 2-4 weeks total, with transition to PO after clinical improvement and culture-directed therapy)

### ICU Admission
- Septic arthritis with concurrent sepsis or septic shock
- Hemodynamic instability
- Multiorgan dysfunction

### Consider Discharge (Rare)
- **Gonococcal arthritis** with mild symptoms, no systemic toxicity, reliable follow-up: may complete initial IV dose in ED then discharge on PO antibiotics with 24-48 hour follow-up. This is the exception, not the rule.
- Monoarthritis with low pre-test probability (synovial fluid WBC < 25,000, no crystals, negative Gram stain, afebrile, non-toxic): close rheumatology follow-up in 24-48 hours with strict return precautions; must have culture follow-up plan.

## Pitfalls

1. **Assuming crystals in synovial fluid exclude infection.** Gout/pseudogout and septic arthritis coexist in 1-5% of cases. Crystal-positive fluid must still be sent for culture. A febrile patient with crystals and WBC > 50,000 should receive empiric antibiotics until cultures return negative.

2. **Using a WBC threshold of 50,000 as a hard cutoff.** Synovial WBC > 50,000 has a sensitivity of only ~60% for septic arthritis. Immunocompromised patients, early infection, and partially treated infections produce lower counts. Any acute inflammatory monoarthritis with WBC > 25,000 and clinical suspicion warrants empiric treatment pending cultures.

3. **Giving antibiotics before aspirating the joint.** Pre-aspiration antibiotics reduce culture yield by 20-30%. Aspirate first, then start antibiotics immediately. The only exception: hemodynamically unstable patients who need antibiotics before a safe aspiration can be arranged.

4. **Failing to consider gonococcal arthritis in young sexually active patients.** Disseminated gonococcal infection is the most common cause of acute infectious arthritis in adults aged 15-40. The classic triad of migratory polyarthralgia, dermatitis (painless pustules), and tenosynovitis is often missed. Culture yield from synovial fluid is < 50%; NAAT testing of urine, pharynx, and rectum increases diagnostic sensitivity.

5. **Relying on a negative Gram stain to exclude septic arthritis.** Gram stain sensitivity is only 50-75% for non-gonococcal and < 25% for gonococcal septic arthritis. A negative Gram stain does not rule out infection. Clinical decision-making must integrate cell count, clinical presentation, and risk factors.

6. **Delayed drainage of the hip.** The hip joint is intracapsular; elevated pressure from effusion can compress the retinacular blood supply to the femoral head. Delayed drainage leads to avascular necrosis, especially in children. Hip septic arthritis requires emergent operative washout, not serial bedside aspiration.

7. **Missing septic arthritis in a prosthetic joint.** Prosthetic joint infections can present with low-grade pain, minimal effusion, and near-normal labs. Synovial fluid WBC threshold for prosthetic joint infection is much lower (> 1,100 WBC with > 64% PMNs in knees). Synovial alpha-defensin and leukocyte esterase are adjunctive markers.

8. **Attributing polyarticular symptoms to a non-infectious etiology without considering disseminated gonococcal infection or endocarditis.** Polyarticular septic arthritis accounts for ~15% of cases and is associated with rheumatoid arthritis, immunosuppression, and S. aureus bacteremia. Blood cultures and echocardiography should be obtained.

9. **Discharging a patient with an unaspirated hot joint.** A swollen, erythematous, painful joint with restricted range of motion cannot be diagnosed or excluded without arthrocentesis. Clinical exam alone cannot reliably distinguish septic arthritis from crystal arthropathy. If you suspect it, tap it.

10. **Forgetting to reassess after initial negative workup.** Synovial fluid cultures take 24-72 hours. Patients discharged with presumed non-septic inflammatory arthritis must have a clear culture follow-up plan and return precautions for worsening symptoms, fever, or inability to bear weight.
