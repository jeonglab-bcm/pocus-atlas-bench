# 0050_lung_plaps-pneumonia

## Observation

Analyzing the sequential frames from this PLAPS point ultrasound:

### Structural Anatomy:
- **Upper portion**: Homogeneous gray parenchyma consistent with the liver, serving as an acoustic window
- **Diaphragm**: A bright, curved hyperechoic line visible traversing the image
- **Large anechoic space**: A prominent black/anechoic collection is clearly visible below the diaphragm, extending through all frames

### Key Findings:

1. **Quad sign** ✓: A large anechoic (black) space is bounded superiorly by the parietal pleural/diaphragmatic line, inferiorly by a lung line, and laterally by rib shadows — forming a quadrilateral shape consistent with pleural effusion.

2. **Jellyfish sign** ✓: Across the sequential frames, a tongue-like structure of echogenic tissue (atelectatic lung) is seen floating and undulating within the surrounding anechoic fluid collection. Its movement across frames mimics a jellyfish in water.

3. **Sinusoid sign** (inferred): The dynamic movement of the lung line toward the parietal pleura across respiratory cycles is suggested by the changing positions of the floating lung tissue between frames.

4. **No air bronchograms** or frank hepatization with shred sign are identified as dominant features.

## Conclusion

```json
{
  "plaps": true,
  "type": "effusion",
  "confidence": "high",
  "findings": [
    "Quad sign - large anechoic pleural fluid collection",
    "Jellyfish sign - atelectatic lung floating within effusion",
    "Sinusoid sign (dynamic, inferred from sequential frames)"
  ]
}
```

This represents a **large pleural effusion** with associated passive/compressive atelectasis of the underlying lung, a classic PLAPS-positive pattern seen in the dependent posterior zones.
