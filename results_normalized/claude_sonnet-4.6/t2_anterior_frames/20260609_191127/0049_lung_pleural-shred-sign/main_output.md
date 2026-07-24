# 0049_lung_pleural-shred-sign

# Lung Ultrasound Sequential Frame Analysis

## Frame-by-Frame Observations

| Frame | Pleural Line | Vertical Artifacts | Deep Field | Notable Changes |
|-------|-------------|-------------------|------------|-----------------|
| 1 | Clear, bright, regular | Discrete vertical hyperechoic lines ≥2 visible | Attenuating but present | Baseline — well-separated B-lines |
| 2 | Clear | Discrete, spaced vertical artifacts | Similar | B-lines stable, separated by dark lung |
| 3 | Clear | Discrete B-lines, dark interspaces between | Mild attenuation | Consistent septal pattern |
| 4 | Clear | 2–3 discrete B-lines; slight crowding | Mild posterior shadowing | Slight increase in density |
| 5 | Clear | B-lines begin approximating each other | Moderate brightness below line | Transition beginning |
| 6 | Clear | B-lines more numerous, partial coalescence | Screen brighter inferiorly | Mixed pattern emerging |
| 7 | Slightly irregular | Near-confluent vertical artifacts | Diffuse white sheet partially developing | Ground-glass features emerging |
| 8 | Slightly irregular | Confluent artifacts, A-lines now obscured | Diffuse hyperechogenicity | Ground-glass dominant |
| 9 | Somewhat thickened appearance | Dense coalescing artifacts | Heavy posterior glow | Predominantly ground-glass |
| 10 | Slightly thickened | Dense, merged B-lines, no inter-B-line dark areas | Deep field uniformly bright | Ground-glass pattern established |

---

## B-Lines Assessment

### Presence
> **lung_rockets = `true`**

**Evidence:** Hyperechoic vertical artifacts arise unequivocally from the pleural line in all 10 frames, extend to the bottom of the screen without fading, and are consistent with classic B-line morphology.

### Subtype Classification
> **subtype = `mixed`**

**Reasoning:**
- **Frames 1–4 (Septal pattern):** B-lines are discrete, well-separated by clearly visible dark lung parenchyma between them. ≤3 B-lines per intercostal space, each individually distinguishable — consistent with *thickened interlobular septa*
- **Frames 5–7 (Transition zone):** B-lines progressively approximate and partially coalesce; inter-B-line dark spaces narrow
- **Frames 8–10 (Ground-glass pattern):** B-lines merge into a confluent white "waterfall," A-lines are completely obscured, and the sub-pleural field becomes a diffuse bright sheet — consistent with *alveolar flooding or diffuse interstitial disease*

---

## Consolidation Assessment

> **consolidation = `false`**
> **consolidation_type = `null`**

**Reasoning:**
| Sign | Observed? | Comment |
|------|-----------|---------|
| Hepatization (liver-like texture) | ❌ No | Sub-pleural field is bright due to B-line artifact, not tissue-like echogenicity |
| Shred sign | ❌ No | Deep border of lung is not visualized as irregular/shredded |
| Air bronchograms | ❌ No | No punctate or linear hyperechoic foci within a hepatized zone |

The bright appearance in later frames represents *confluent B-lines (ground-glass pattern)*, not true parenchymal consolidation. The pleural line, while slightly irregular in later frames, does not transition into a hepatized sub-pleural tissue block.

---

## Summary Conclusion

```
lung_rockets       = true
b_line_subtype     = "mixed"
                     (septal → ground_glass progression across clip)
consolidation      = false
consolidation_type = null
```

**Clinical Interpretation:** This sequential clip demonstrates a *dynamic interstitial syndrome* pattern, with discrete septal B-lines in early frames evolving into confluent ground-glass B-lines in later frames. This is consistent with **pulmonary edema (cardiogenic or non-cardiogenic)** or **diffuse interstitial lung disease**, without evidence of lobar/segmental consolidation in the anterior zone.
