---
id: video-laryngoscopy
condition: Video Laryngoscopy
aliases: [VL, video-assisted intubation, indirect laryngoscopy, GlideScope, C-MAC, McGrath]
icd10: [T88.4XXA, Z53.09]
esi: 1
time_to_harm:
  irreversible_injury: "< 4 minutes (anoxic brain injury)"
  death: "< 8 minutes without oxygenation"
  optimal_intervention_window: "< 45 seconds from blade insertion to tube confirmation"
category: procedural
track: tier1
sources:
  - type: pubmed
    ref: "Hansel J, Rogers AM, Lewis SR, et al. Videolaryngoscopy versus direct laryngoscopy for adults undergoing tracheal intubation. Cochrane Database Syst Rev. 2022;4(4):CD011136."
    pmid: "35373840"
  - type: pubmed
    ref: "Driver BE, Prekker ME, Klein LR, et al. Effect of Use of a Bougie vs Endotracheal Tube and Stylet on First-Attempt Intubation Success Among Patients With Difficult Airways. JAMA. 2018;319(21):2179-2189."
    pmid: "29800096"
  - type: guideline
    ref: "Apfelbaum JL, Hagberg CA, Connis RT, et al. 2022 ASA Practice Guidelines for Management of the Difficult Airway. Anesthesiology. 2022;136(1):31-81."
    pmid: "34762729"
  - type: review
    ref: "Arulkumaran N, Lowe J, Ions R, et al. Videolaryngoscopy versus direct laryngoscopy for emergency orotracheal intubation outside the operating theatre: a systematic review and meta-analysis. Br J Anaesth. 2018;120(4):712-724."
    pmid: "29576112"
  - type: pubmed
    ref: "Prekker ME, Driver BE, Engstrom A, et al. Video versus Direct Laryngoscopy for Tracheal Intubation of Critically Ill Adults. N Engl J Med. 2023;389(5):418-429."
    pmid: "37326325"
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
# Video Laryngoscopy

## Recognition

**Indications:**
- Default first-line technique for emergency intubation (DEVICE trial, NEJM 2023: VL first-pass success 85.4% vs DL 75.0%, p<0.001)
- Predicted or known difficult airway (Mallampati III-IV, limited mouth opening, cervical spine immobilization, obesity, facial/neck trauma)
- Teaching and supervision of intubation (shared screen view)
- Blood or secretions obscuring direct view
- Anterior airway (Cormack-Lehane grade III-IV on prior DL)

**When Direct Laryngoscopy May Be Preferred:**
- Massive oropharyngeal hemorrhage obscuring the camera lens
- Equipment failure or unavailability of VL
- Provider highly experienced with DL and conditions are straightforward

**Device Categories:**

| Type | Examples | Blade Geometry | Key Feature |
|------|---------|---------------|-------------|
| Standard geometry | C-MAC standard, Storz DCI | Macintosh-shaped | Can be used as DL with or without screen; allows bougie passage |
| Hyperangulated | GlideScope, C-MAC D-blade, McGrath X-blade | 60-degree curve | Superior glottic view; requires stylet pre-curved to match blade angle |
| Channeled | Airtraq, King Vision channeled | Integrated tube channel | Guides tube to glottis; no stylet needed; limited to standard ETT sizes |

## Critical Actions

| Action | Target |
|--------|--------|
| Blade insertion to glottic view | < 15 seconds |
| Blade insertion to tube confirmation | < 45 seconds |
| Maximum laryngoscopy time per attempt | 30 seconds |
| ETCO2 confirmation | Immediately after tube placement |

1. **Select device and blade size** — standard geometry if DL backup desired; hyperangulated for difficult airway; adult sizes 3 or 4 blade
2. **Position patient** — sniffing position (ear-to-sternal-notch alignment); ramped for obese
3. **Preoxygenate** — NRB 15 L/min x 3 min + apneic oxygenation via 15 L/min nasal cannula
4. **Anti-fog the lens** — warm or apply anti-fog solution; wipe with gauze
5. **Insert blade midline** — advance along tongue to vallecula (standard) or epiglottis (hyperangulated)
6. **Optimize view** — lift vertically (not rotational lever as with DL); suction as needed
7. **Pass ETT/bougie** — watch on screen AND maintain view of oropharynx to avoid impingement
8. **Confirm with waveform capnography**

## Differential Diagnosis

**Alternative Intubation Techniques:**

| Technique | When to Use |
|-----------|------------|
| Direct laryngoscopy | Equipment failure; massive hemorrhage obscuring camera |
| Fiberoptic intubation | Awake intubation in anticipated difficult airway |
| Supraglottic airway (iGel, LMA) | Rescue after failed VL; bridge to definitive airway |
| Bougie-assisted intubation | Grade II-III view; blind passage through cords with tactile confirmation |
| Retrograde intubation | Cannot intubate from above, not yet CICO |
| Surgical cricothyrotomy | CICO — failed VL, failed SGA, failed BVM |

**Rescue Sequence After Failed VL Attempt:**
1. Return to BVM with two-person technique + oral airway
2. Reposition, suction, optimize
3. Switch blade geometry (standard → hyperangulated or vice versa)
4. Insert bougie if not used initially
5. Attempt with different VL device or direct laryngoscopy
6. Maximum 3 total laryngoscopy attempts → SGA rescue → surgical airway

## Workup

**Pre-Procedure Assessment:**
- LEMON airway assessment (< 30 seconds)
- Determine blade type: standard geometry for most; hyperangulated for predicted difficult airway
- Pre-shape stylet: 35-degree curve for standard geometry, 60-70-degree curve for hyperangulated (hockey-stick shape)
- OR use bougie (60 cm coude-tip) — higher first-pass success in difficult airways

**Equipment Checklist:**

| Item | Specification |
|------|---------------|
| Video laryngoscope | Charged, screen functional, anti-fogged |
| Blade | Size 3 or 4; standard + hyperangulated available |
| ETT | 7.0-8.0 (men), 6.5-7.5 (women) |
| Stylet | Pre-shaped to match blade geometry |
| Bougie | 60 cm coude-tip gum elastic bougie |
| Suction | Yankauer + large-bore (DuCanto) |
| ETCO2 | Waveform capnography |
| BVM | With PEEP valve, connected to O2 |
| Nasal cannula | 15 L/min for apneic oxygenation |
| Backup | Direct laryngoscope, SGA, surgical airway kit |

## Treatment

### Standard Geometry VL Technique (C-MAC, Storz)

**Step 1:** Insert blade midline along the tongue (unlike DL, which inserts from the right)
**Step 2:** Advance tip to the vallecula (same as Macintosh DL technique)
**Step 3:** Lift vertically to expose glottis — minimal rotational force needed; the camera provides the view
**Step 4:** Pass styletted ETT or bougie under direct visualization on screen
**Step 5:** Watch the tube approach the cords on screen but ALSO glance at the oropharynx to ensure the tube tip is not impinging on the right arytenoid or piriform sinus
**Step 6:** Advance tube through cords, inflate cuff, confirm with ETCO2

### Hyperangulated VL Technique (GlideScope, D-blade)

**Step 1:** Pre-curve the stylet to match the 60-degree blade angle (hockey-stick bend at distal 1/3)
**Step 2:** Insert blade midline; advance directly to the epiglottis — the hyperangulated blade lifts the epiglottis indirectly
**Step 3:** DO NOT advance the blade too deep — "best view" often requires pulling back slightly
**Step 4:** Guide the pre-curved ETT along the blade toward the glottic opening on screen
**Step 5:** Once the tube tip reaches the cords, STRAIGHTEN the stylet slightly by pulling it back 2-3 cm to allow the tube to advance anteriorly through the cords
**Step 6:** If tube hangs up on the anterior commissure: rotate tube 90 degrees counterclockwise, then advance
**Step 7:** Advance tube to standard depth, inflate cuff, confirm with ETCO2

### Troubleshooting

| Problem | Solution |
|---------|----------|
| Fogged lens | Warm blade, anti-fog solution, suction oral secretions |
| Excellent view but cannot pass tube | Blade too deep — withdraw 1-2 cm; straighten stylet; use bougie |
| Tube impinging on right arytenoid | Rotate tube 90 degrees counterclockwise; use smaller tube |
| Blood/secretions obscuring camera | Continuous suction; consider DL if camera useless |
| Cormack-Lehane I on screen but tube fails | Over-inserted blade; withdraw until grade II view, then pass tube |

### Post-Procedure
- Secure tube at measured depth (21-23 cm at teeth in adults)
- CXR confirmation: tip 2-4 cm above carina
- Initiate post-intubation sedation immediately
- Document device used, blade type/size, Cormack-Lehane grade, number of attempts

## Disposition

- **Successful intubation:** ICU admission for mechanical ventilation
- **Difficult VL requiring multiple attempts:** document in airway difficulty registry; anesthesia/ENT notification
- **Failed VL with SGA rescue:** if adequate ventilation, convert to definitive airway in controlled setting (OR with ENT/anesthesia); if inadequate, surgical airway
- **Transfer:** intubated patient transferred with portable ventilator and continuous capnography monitoring

## Pitfalls

1. **Advancing the hyperangulated blade too deep, losing the view.** The optimal position for a hyperangulated blade is often shallower than intuition suggests. If the glottic view disappears, withdraw the blade 1-2 cm rather than advancing further. The "pulling back" maneuver is the most common correction needed.

2. **Failing to match the stylet curve to the blade geometry.** A straight stylet with a hyperangulated blade will not navigate the 60-degree curvature — the tube tip catches on the anterior tracheal wall or right arytenoid. Pre-shape the stylet to a hockey-stick bend that parallels the blade angle.

3. **Watching only the screen and not the oropharynx during tube passage.** The camera shows the glottis but not the tube's path through the mouth. The tube tip can perforate the posterior pharyngeal wall, impale the palatoglossal arch, or lodge in the piriform sinus without appearing on screen. Alternate attention between screen and mouth.

4. **Over-reliance on the excellent glottic view without achieving tube delivery.** VL consistently provides a better view than DL, but Cormack-Lehane grade I on screen does not guarantee tube delivery success. The most common VL failure is "great view, can't pass the tube" — caused by blade too deep, stylet mismatch, or tube impingement. Recognize this pattern and troubleshoot systematically.

5. **Not having direct laryngoscopy as backup.** VL can fail due to fogging, blood, screen malfunction, or lens contamination. A direct laryngoscope must be immediately available. Providers must maintain DL skills even as VL becomes standard.

6. **Prolonged laryngoscopy attempts degrading oxygen reserves.** Each attempt should be limited to 30 seconds of laryngoscopy. The improved view with VL creates a false sense of security — operators persist with tube manipulation while the patient desaturates. Set an audible timer or have a team member announce elapsed time.
