# 0025_lung_malignant-pleural-effusion

## Observations

Analyzing the sequential frames from the PLAPS point:

### Effusion Signs:
- **Quad sign**: A large **anechoic (black) space** is clearly visible throughout the sequence, bounded by anatomical landmarks, forming the classic quadrilateral configuration of pleural effusion.
- **Jellyfish sign**: Across the frames, a floating, undulating tissue structure is seen moving within the surrounding fluid collection. This atelectatic/consolidated lung segment oscillates with respiratory and cardiac motion, creating the characteristic "jellyfish in water" appearance.

### Consolidation Signs:
- **Tissue-like hepatization**: Within and adjacent to the effusion, there is echogenic tissue that closely resembles liver parenchyma in echotexture — consistent with consolidated/atelectatic lung.
- **Air bronchograms**: Punctate hyperechoic foci are visible within the hepatized lung tissue, representing air-filled bronchi surrounded by non-aerated consolidated parenchyma.

### Dynamic Assessment:
Across the frames, the consolidated lung segment is seen moving freely within the large effusion, confirming both a significant free-flowing fluid collection and compressive atelectasis/consolidation of the dependent lung.

---

## Conclusion

```json
{
  "plaps": true,
  "type": "both",
  "confidence": "high",
  "findings": [
    "Large pleural effusion (quad sign)",
    "Jellyfish sign - atelectatic lung floating in effusion",
    "Hepatized/consolidated lung tissue",
    "Air bronchograms within consolidation"
  ]
}
```

**PLAPS = true | Type = both (effusion + consolidation)**

This pattern is highly suggestive of a significant pleural effusion with associated compressive atelectasis/consolidation — commonly seen in pneumonia, empyema, or other causes of dependent pleural fluid accumulation with secondary lung collapse.
