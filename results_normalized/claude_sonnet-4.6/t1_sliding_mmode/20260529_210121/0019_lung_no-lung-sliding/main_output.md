# 0019_lung_no-lung-sliding

# Lung Ultrasound M-Mode Analysis

## Step 1 — Per-Position Classification

### p00
**Observations:** Extremely bright white horizontal band near the top (pleural line). Below: large dark region with faint wavy undulating structures in the mid-section, very dark inferiorly. The wavy/irregular character of the bright band and undulating subpleural structures suggest motion.
**→ SEASHORE**

### p01
**Observations:** Bright pleural line visible; below it, multiple horizontal structures are present with visible granular/noisy texture interspersed. Some dark areas but overall granular character below the pleural line.
**→ SEASHORE**

### p02
**Observations:** Similar to p01 — bright pleural line with horizontal wave-like structures below; lower portion shows some dark granular texture. Pleural line appears slightly irregular/wavy.
**→ SEASHORE**

### p03
**Observations:** Horizontal lines more widely distributed throughout the image; however, there is still some irregular granularity and wave-like undulation between lines. Pleural line still shows slight waviness.
**→ SEASHORE** (transitional but retains granular quality)

### p04
**Observations:** Horizontal lines now distributed uniformly throughout both above and below the pleural line. No appreciable granular texture. Lines appear denser and more continuous. Pleural line appears straighter.
**→ STRATOSPHERE**

### p05
**Observations:** Dense, continuous parallel horizontal lines filling the image above and below the pleural line. No granular texture identifiable. Classic barcode appearance.
**→ STRATOSPHERE**

### p06
**Observations:** Dense horizontal parallel lines throughout the entire image. Smooth, straight pleural line. No sandy texture. Classic stratosphere/barcode pattern.
**→ STRATOSPHERE**

### p07
**Observations:** Bright horizontal lines concentrated in the middle section; lower portion transitions to darker, more granular region. The dark sandy appearance below the pleural line supports sliding.
**→ SEASHORE**

### p08
**Observations:** Bright horizontal band visible in the upper-middle region; lower portion is darker with some granular/noisy texture. Pattern similar to p01-p02.
**→ SEASHORE**

### p09
**Observations:** Nearly entirely black image. Minimal signal throughout — no discernible pleural line, no texture.
**→ UNCLASSIFIABLE**

---

## Summary Table

| Position | Classification |
|----------|---------------|
| p00 | Seashore ✓ |
| p01 | Seashore ✓ |
| p02 | Seashore ✓ |
| p03 | Seashore ✓ |
| p04 | Stratosphere ✗ |
| p05 | Stratosphere ✗ |
| p06 | Stratosphere ✗ |
| p07 | Seashore ✓ |
| p08 | Seashore ✓ |
| p09 | **UNCLASSIFIABLE** |

---

## Step 2 — Overall Decision

**Classifiable positions:** p00–p08 (9 positions)
- **Seashore:** p00, p01, p02, p03, p07, p08 → 6 positions
- **Stratosphere:** p04, p05, p06 → 3 positions

> There is a **clear spatial transition** from seashore (lateral positions) to stratosphere (central positions) and back to seashore — both patterns coexist across different probe positions.

## ✅ Overall Label: **BOTH** (Lung Point Present)

The spatial alternation from sliding (seashore) → no sliding (stratosphere) → sliding (seashore) across probe positions is characteristic of a **lung point**, indicating **focal pleural sliding absence** consistent with pneumothorax at this site.
