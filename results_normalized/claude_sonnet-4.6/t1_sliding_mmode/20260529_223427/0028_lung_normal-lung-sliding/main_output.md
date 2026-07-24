# 0028_lung_normal-lung-sliding

## Step 1 — Per-Position Classification

### p00 (Image 1)
**Observation:** Clear horizontal lines in the upper one-third; below the apparent pleural line, the image is overwhelmingly black with no detectable texture.
**Classification: UNCLASSIFIABLE** — edge artifact / insufficient signal below pleural line.

---

### p01 (Image 2)
**Observation:** Very similar to p00. Slight brightening in the mid-zone but the lower half remains predominantly black. No identifiable texture below.
**Classification: UNCLASSIFIABLE** — insufficient signal.

---

### p02 (Image 3)
**Observation:** Upper horizontal lines are slightly less bright than in later images. Below the pleural band there is faint structure but no reliably classifiable texture; still predominantly dark.
**Classification: UNCLASSIFIABLE** — borderline signal, cannot confidently distinguish pattern type.

---

### p03 (Image 4)
**Observation:** Upper portion shows distinct, well-separated parallel bright bands (chest-wall lines). A bright pleural band is visible roughly mid-image. Below this band, **irregular, somewhat granular/patchy texture** begins to appear — not organized horizontal lines. Pleural line shows slight waviness.
**Classification: SEASHORE** — granular texture below pleural line; pleural sliding PRESENT.

---

### p04 (Image 5)
**Observation:** Clear chest-wall lines above. Below the pleural line, **moderate granular/sandy texture** is present with brightness variation that lacks the regularity of a barcode. No crisp, uniform horizontal lines below the pleural band.
**Classification: SEASHORE** — sliding PRESENT.

---

### p05 (Image 6)
**Observation:** Same architecture. Below the pleural band, the texture is **granular and non-uniform** — the lower region does not mirror the organized lines of the upper region. Some faint sub-pleural A-line echoes riding over a sandy background.
**Classification: SEASHORE** — sliding PRESENT.

---

### p06 (Image 7)
**Observation:** Well-defined chest-wall lines. Below pleural band: **granular, somewhat mottled texture** — inconsistent horizontal elements mixed with random noise. Clearly different character from the orderly lines above.
**Classification: SEASHORE** — sliding PRESENT.

---

### p07 (Image 8)
**Observation:** Chest-wall lines still visible but slightly less crisp. Below the pleural line: **heterogeneous, granular-to-patchy texture** with no ordered barcode structure.
**Classification: SEASHORE** — sliding PRESENT.

---

### p08 (Image 9)
**Observation:** Chest-wall lines are fewer and fainter. Below the pleural region: **diffuse, cloud-like patchy texture** — irregular and non-linear. The pattern below is entirely inconsistent with uniform horizontal barcode lines.
**Classification: SEASHORE** — sliding PRESENT (diffuse granular/patchy texture below pleural line).

---

### p09 (Image 10)
**Observation:** Very few horizontal lines remain in the upper zone; lower half is largely black with only faint patchy signal. Structure is insufficient for confident classification — likely approaching the right edge of the active scan region.
**Classification: UNCLASSIFIABLE** — edge artifact / insufficient signal.

---

## Summary Table

| Position | Classification |
|----------|---------------|
| p00 | **Unclassifiable** |
| p01 | **Unclassifiable** |
| p02 | **Unclassifiable** |
| p03 | **Seashore** |
| p04 | **Seashore** |
| p05 | **Seashore** |
| p06 | **Seashore** |
| p07 | **Seashore** |
| p08 | **Seashore** |
| p09 | **Unclassifiable** |

---

## Step 2 — Overall Decision

- **Classifiable positions:** p03–p08 (6 positions)
- **Seashore:** 6/6 classifiable positions
- **Stratosphere:** 0
- **Alternating:** 0
- No spatial transition between seashore and stratosphere regions detected.

> ### ✅ Overall Label: **PRESENT**
> Pleural sliding is **present** across all classifiable lateral positions. The consistent granular/sandy texture below the pleural line at positions p03–p08, with no barcode pattern identified anywhere, indicates normal lung sliding throughout the active scan region.
