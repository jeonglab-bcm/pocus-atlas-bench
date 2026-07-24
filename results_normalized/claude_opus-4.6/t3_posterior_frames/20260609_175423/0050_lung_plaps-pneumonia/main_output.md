# 0050_lung_plaps-pneumonia

## Observations

Analyzing these sequential frames from the PLAPS point:

### Frame-by-Frame Analysis:

1. **Large anechoic space**: Throughout all frames, there is a prominent **dark (anechoic) fluid collection** visible deep to the chest wall/pleural line. This space is clearly bounded, forming a **quad sign**.

2. **Moving lung structure within fluid**: Across the sequential frames, a bright curvilinear echogenic structure (the compressed/atelectatic lung) is seen moving and undulating within the surrounding fluid collection. This structure changes position and shape between frames — characteristic of the **jellyfish sign** — atelectatic lung floating freely within pleural fluid.

3. **Sinusoid sign (inferred)**: The respiratory variation in the position of the lung line relative to the pleural line across frames suggests cyclical movement consistent with the sinusoid sign.

4. **Rib shadows**: Lateral acoustic shadows from ribs are visible on the left side of several frames, helping define the quadrilateral boundaries.

5. **No significant hepatization or air bronchograms**: The floating lung tissue appears atelectatic rather than showing frank tissue-like consolidation with air bronchograms.

---

## Conclusion

```json
{
  "plaps": true,
  "type": "effusion",
  "signs_present": [
    "quad sign",
    "jellyfish sign",
    "sinusoid sign (dynamic, inferred from sequential frames)"
  ],
  "confidence": "high",
  "description": "Large pleural effusion at the PLAPS point with jellyfish sign — atelectatic lung floating and undulating within the surrounding anechoic fluid collection."
}
```
