# 0051_lung_jellyfish-sign

## Observations

**Frame-by-frame analysis:**

Across all 10 sequential frames, the following findings are consistently observed:

1. **Large anechoic space**: A prominent black, echo-free region is present throughout the sequence, occupying a significant portion of the image. This is bounded by:
   - The pleural line superiorly
   - A visible lung line/compressed lung inferiorly
   - Rib shadows laterally
   - This constitutes a clear **quad sign**

2. **Jellyfish sign**: In frames 1-5, there is a floating, undulating structure within the anechoic fluid collection — representing atelectatic/compressed lung moving with respiration within the surrounding effusion.

3. **Hepatized lung tissue**: In the deeper portions of the image (particularly frames 4-9), the visible lung parenchyma appears tissue-like and echogenic, resembling liver — consistent with **consolidation/compressive atelectasis**.

4. **Air bronchograms**: Punctate hyperechoic foci are visible within the consolidated lung tissue in several frames (particularly frames 7-9), representing air-filled bronchi within non-aerated lung.

## Conclusion

```json
{
  "plaps": true,
  "type": "both",
  "confidence": "high"
}
```

**Reasoning**: There is a large pleural effusion (quad sign, jellyfish sign) with associated compressive atelectasis/consolidation (hepatized lung tissue with air bronchograms) in the dependent posterior zone — a classic PLAPS pattern combining both effusion and consolidation.
