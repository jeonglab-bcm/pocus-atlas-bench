# 0018_lung_pericardial-pleural-effusions

## Observations

**Sequential Frame Analysis:**

Across all 10 frames, I observe the following consistent findings at the PLAPS point:

1. **Anechoic (black) space**: A well-defined dark fluid collection is visible in multiple frames, bounded superiorly by the parietal pleural line and inferiorly by a lung line — forming a **quad sign** configuration. This is most clearly visible in frames 1, 4, 6, and 7.

2. **Tissue-like echogenicity (hepatization)**: Adjacent to and beneath the fluid collection, there is echogenic tissue that resembles liver parenchyma in texture. This represents non-aerated, consolidated or atelectatic lung. This is particularly visible in frames 2, 3, 5, 8, and 9.

3. **Jellyfish-like motion**: Across the sequential frames, the atelectatic lung tissue appears to undulate and float within the surrounding effusion, suggesting a **jellyfish sign**.

4. **Possible air bronchograms**: Punctate hyperechoic foci are visible within the hepatized lung tissue in some frames (frames 2-3, 8-9), consistent with residual air in bronchi within consolidated parenchyma.

5. **No normal A-line pattern**: The typical A-line pattern of a normally aerated lung is completely absent.

## Conclusion

```json
{
  "plaps": true,
  "type": "both",
  "confidence": "high",
  "findings": [
    "Quad sign (pleural effusion)",
    "Jellyfish sign (atelectatic lung floating in effusion)",
    "Hepatization (tissue-like consolidated lung)",
    "Air bronchograms within consolidated tissue"
  ]
}
```

**PLAPS = true | Type = both** — There is a significant pleural effusion with adjacent consolidated/atelectatic lung, a classic dependent-zone PLAPS pattern seen in pneumonia, post-operative atelectasis, or decompensated heart failure.
