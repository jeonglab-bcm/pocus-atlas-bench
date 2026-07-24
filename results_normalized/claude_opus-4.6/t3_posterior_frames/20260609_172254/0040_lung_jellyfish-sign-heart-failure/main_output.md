# 0040_lung_jellyfish-sign-heart-failure

## Observations

Analyzing these sequential PLAPS-point frames, I observe the following:

**Structural landmarks:**
- The chest wall and pleural line are visible at the top of the images
- Rib shadows are seen laterally, creating acoustic boundaries
- A large **anechoic (black) space** is present between the pleural line and a deeper echogenic structure

**Effusion signs:**
- **Quad sign**: A clearly defined anechoic quadrilateral space is visible, bounded by the pleural line superiorly, a lung line inferiorly, and rib shadows laterally
- **Jellyfish sign**: Across the sequential frames (particularly frames 3–7), a triangular/wedge-shaped echogenic structure is seen floating and undulating within the anechoic fluid collection — this represents atelectatic lung moving within the effusion

**Consolidation signs:**
- **Tissue-like hepatization**: The visible lung tissue within/adjacent to the effusion appears solid and echogenic (liver-like), indicating loss of normal aeration
- The compressed lung has a tissue density pattern consistent with compressive atelectasis/consolidation

## Conclusion

```json
{
  "plaps": true,
  "type": "both",
  "confidence": "high"
}
```

**Rationale:** There is a large **pleural effusion** (quad sign, jellyfish sign with floating atelectatic lung) combined with **consolidation/hepatization** of the compressed lung parenchyma. The dynamic movement of the atelectatic lung within the effusion across frames confirms the jellyfish sign, characteristic of significant effusion with associated passive atelectasis.
