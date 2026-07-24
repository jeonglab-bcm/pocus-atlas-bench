# 0053_lung_aie26re0isbsydfwrnbcqi0ys4jbmx

# Lung Ultrasound M-Mode Analysis

## Step 1 — Per-Position Classification

| Position | Observations | Classification |
|----------|-------------|----------------|
| **p00** | Upper ~40%: Multiple clear bright/dark horizontal bands (chest wall). Lower ~60%: Very dark with faint granular noise. Pleural line forms a distinct demarcation. Right edge distortion. | **Seashore** |
| **p01** | Similar to p00. Clear chest wall lines above; lower half dark with slightly more faint granular texture than p00. Pleural line demarcation visible. | **Seashore** |
| **p02** | Cleaner, sharper horizontal lines above. Lower portion dark with subtle granular texture. Pleural line distinct. Right edge artifact. | **Seashore** |
| **p03** | Lines extend slightly further down than p00–p02. Lower portion shows increased granularity/noise texture. Pleural line identifiable. | **Seashore** |
| **p04** | Chest wall lines clearly visible. Below the pleural line: granular sandy texture with a focal bright region consistent with an A-line *over* a granular background. | **Seashore** |
| **p05** | Lines begin to show subtle undulation/waviness. Below: textured, somewhat granular. Pleural line slightly irregular (supports motion). | **Seashore** |
| **p06** | Lines show distinct undulation/waves — hallmark of pleural motion. Granular texture below. Pleural line clearly non-straight. | **Seashore** |
| **p07** | Lines exhibit clear undulating morphology. Multiple wavy bright lines. Granular texture in lower region. Strong seashore morphology. | **Seashore** |
| **p08** | Undulating lines with some broadening of the layered structure. Complex granular/sandy texture below pleural line. Wavy pleural line. | **Seashore** |
| **p09** | Only 3–4 lines visible at the very top; remainder predominantly black. Minimal signal throughout most of the strip. Likely at right edge of active field. | **Unclassifiable** |

---

## Step 2 — Overall Decision

- **Classifiable positions:** p00–p08 (n = 9)
- **Seashore:** 9/9 classifiable positions
- **Stratosphere:** 0
- **Alternating (lung point):** 0
- **Unclassifiable:** p09 (excluded)

> No position shows a true barcode/stratosphere pattern (horizontal lines filling the entire frame top-to-bottom with no granularity). All classifiable positions display the characteristic seashore morphology, with increasing pleural line waviness from p05 onward indicating active pleural sliding.

## ✅ Overall Label: **PRESENT**
**Pleural sliding is present** across all classifiable lateral positions.
