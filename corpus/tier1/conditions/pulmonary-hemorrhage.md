---
id: pulmonary-hemorrhage
condition: Pulmonary Hemorrhage / Diffuse Alveolar Hemorrhage
aliases: [DAH, diffuse alveolar hemorrhage, pulmonary hemorrhage, hemoptysis massive, alveolar hemorrhage]
icd10: [R04.89, J95.01]
esi: 1
time_to_harm:
  irreversible_injury: "< 2 hours"
  death: "< 6 hours"
  optimal_intervention_window: "< 1 hour"
category: respiratory
track: tier1
sources:
  - type: review
    ref: "Lara AR, Schwarz MI. Diffuse Alveolar Hemorrhage. Chest. 2010;137(5):1164-1171."
  - type: review
    ref: "de Prost N, et al. Diffuse Alveolar Hemorrhage in Immunocompetent Patients: Etiologies and Prognosis Revisited. Respir Med. 2012;106(7):1021-1032."
  - type: review
    ref: "Ioachimescu OC, Stoller JK. Diffuse Alveolar Hemorrhage: Diagnosing It and Finding the Cause. Cleve Clin J Med. 2008;75(4):258-280."
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
# Pulmonary Hemorrhage / Diffuse Alveolar Hemorrhage

## Recognition

**Classic triad of DAH:**
1. Hemoptysis (present in only ~60% — absence does NOT exclude DAH)
2. Bilateral alveolar infiltrates on CXR
3. Dropping hemoglobin/hematocrit

**Presentation:**
- Dyspnea (most consistent symptom), cough, hemoptysis
- Hypoxemia, tachypnea
- Fever (may suggest infection or vasculitis)
- Progressive bilateral infiltrates on CXR/CT over hours to days
- Rising DLCO (hemorrhage increases CO absorption — pathognomonic but rarely measured acutely)

**Etiologies:**
- **Pulmonary capillaritis (most common):** ANCA-associated vasculitis (GPA, MPA), anti-GBM disease (Goodpasture), SLE, antiphospholipid syndrome
- **Bland hemorrhage (no capillaritis):** Anticoagulation, mitral stenosis, pulmonary veno-occlusive disease, idiopathic pulmonary hemosiderosis
- **Diffuse alveolar damage with hemorrhage:** ARDS, bone marrow transplant, drug toxicity (amiodarone, crack cocaine)
- **Infection:** Leptospirosis, hantavirus, invasive aspergillosis

**BAL diagnostic confirmation:**
- Progressively hemorrhagic aliquots on serial BAL (sequential aliquots become MORE bloody, not less)
- Hemosiderin-laden macrophages (> 20% = DAH)

## Critical Actions

| Action | Target |
|---|---|
| Airway protection | Immediate |
| Type and crossmatch | < 15 minutes |
| Reverse anticoagulation | < 30 minutes |
| High-dose steroids (if vasculitis) | < 1 hour |

1. **Airway management** — intubation for respiratory failure or massive hemoptysis. Use LARGE ETT (>= 8.0) to facilitate bronchoscopy and suctioning.
2. **Positioning:** Bleeding side DOWN (if lateralized) — protects uninvolved lung
3. **Transfusion:** Crossmatch 4 units pRBC; transfuse for Hgb < 7 (or < 9 if hemodynamically unstable)
4. **Reverse anticoagulation** if on warfarin (4-factor PCC 25-50 units/kg IV + vitamin K 10 mg IV), heparin (protamine), or DOAC (andexanet alfa for Xa inhibitors, idarucizumab for dabigatran)
5. **High-dose methylprednisolone 1 g IV daily x 3 days** — if vasculitis/autoimmune DAH suspected (do NOT wait for confirmatory labs)
6. **Bronchoscopy** — both diagnostic (serial BAL confirming DAH) and therapeutic (iced saline lavage, topical epinephrine 1:20,000 for focal bleeding)
7. **Correct coagulopathy** — FFP, platelets, cryoprecipitate as indicated
8. **Rheumatology and pulmonology consultation** STAT

## Differential Diagnosis

- **Bilateral pneumonia** — fever, productive cough, no hemoglobin drop; cultures positive
- **ARDS** — bilateral infiltrates but no hemoptysis or hemoglobin drop (though DAH can cause ARDS)
- **Cardiogenic pulmonary edema** — elevated BNP, S3, responds to diuretics
- **Alveolar hemorrhage from focal source** — massive hemoptysis from bronchiectasis, tumor, or AVM; usually unilateral
- **Pulmonary renal syndrome** — DAH + glomerulonephritis: anti-GBM, ANCA vasculitis, SLE

## Workup

- **Bronchoscopy with BAL:** Definitive diagnosis — progressively hemorrhagic aliquots; hemosiderin-laden macrophages
- **CT chest:** Bilateral ground-glass opacities, crazy-paving pattern; may show focal or diffuse distribution
- **Labs:** CBC (serial Hgb q4-6h — dropping confirms ongoing hemorrhage), BMP (creatinine — pulmonary-renal syndrome), coagulation studies (PT/INR, aPTT, fibrinogen), type and crossmatch
- **Autoimmune panel:** ANCA (c-ANCA/PR3 for GPA, p-ANCA/MPO for MPA), anti-GBM antibodies, ANA, anti-dsDNA, complement (C3/C4), antiphospholipid antibodies
- **Urinalysis:** RBC casts, proteinuria (concurrent glomerulonephritis = pulmonary-renal syndrome)
- **Renal function:** Creatinine — may be rising rapidly if concurrent GN
- **Sputum/BAL cultures:** Rule out infectious cause (Legionella, leptospirosis, hantavirus)
- **CXR:** Bilateral alveolar infiltrates (may be patchy or diffuse)

## Treatment

### Autoimmune/Vasculitis DAH
- Pulse methylprednisolone 1 g IV daily x 3 days, then prednisone 1 mg/kg/day PO taper
- Cyclophosphamide 500 mg/m2 IV (for ANCA vasculitis or SLE) or rituximab 375 mg/m2 IV (for GPA/MPA — RAVE trial equivalent to cyclophosphamide)
- Plasmapheresis for anti-GBM disease (Goodpasture) — daily x 14 days or until anti-GBM levels undetectable. Also consider for severe ANCA vasculitis with DAH (PEXIVAS trial: conditional benefit in severe renal disease)

### Anticoagulation-Related DAH
- Reverse anticoagulation immediately (see Critical Actions)
- Transfuse as needed
- Identify if underlying vasculitis or other cause exists (anticoagulation may be unmasking subclinical DAH)

### Massive Hemoptysis Management
- Intubation with large ETT (>= 8.0)
- Positioning: bleeding side down
- Bronchoscopic interventions: iced saline lavage, topical epinephrine (1:20,000), balloon tamponade (Fogarty catheter)
- Interventional radiology: bronchial artery embolization (BAE) for focal arterial bleeding
- Surgical resection: last resort for localized hemorrhage refractory to all other measures

### Refractory DAH
- rFVIIa (recombinant factor VIIa) 50-90 mcg/kg IV — case reports/series show efficacy for refractory DAH (off-label)
- Intrapulmonary rFVIIa via bronchoscopy — local hemostasis
- VV-ECMO for refractory hypoxemia

## Disposition

- **ICU admission:** All DAH patients — high mortality (> 50% in some series), need for close monitoring, potential for rapid deterioration
- **Rheumatology/nephrology consultation:** Urgent — guide immunosuppressive therapy, monitor for pulmonary-renal syndrome
- **Transfer:** Facilities without bronchoscopy, interventional radiology (BAE), or ECMO capability
- **Serial Hgb monitoring:** Q4-6 hours until stable; persistent Hgb drop = ongoing hemorrhage

## Pitfalls

1. **Excluding DAH because hemoptysis is absent.** Up to 40% of DAH patients never have frank hemoptysis. Blood fills the alveolar spaces but may not be expectorated. Any patient with bilateral infiltrates, dropping hemoglobin, and hypoxemia should be evaluated for DAH even without hemoptysis.

2. **Waiting for autoimmune labs before starting steroids.** ANCA, anti-GBM, and complement levels take days to result. If clinical presentation strongly suggests vasculitis-related DAH (bilateral infiltrates, hemoptysis, renal dysfunction, rising creatinine), pulse steroids should be started immediately. Delay increases mortality.

3. **Attributing bilateral infiltrates to pneumonia without checking hemoglobin trend.** DAH and bilateral pneumonia look identical on CXR. A dropping hemoglobin trend with bilateral infiltrates should prompt bronchoscopy with sequential BAL to confirm DAH.

4. **Failing to evaluate for concurrent glomerulonephritis.** Pulmonary-renal syndrome (DAH + GN) occurs in anti-GBM disease, ANCA vasculitis, and SLE. Always check creatinine and urinalysis for RBC casts. Delayed recognition of renal involvement worsens renal outcomes.

5. **Not performing bronchoscopy.** DAH is a bronchoscopic diagnosis — progressively hemorrhagic BAL aliquots are pathognomonic. BAL also rules out infection and can provide therapeutic hemostasis. Empiric treatment without bronchoscopic confirmation may miss the true diagnosis.
