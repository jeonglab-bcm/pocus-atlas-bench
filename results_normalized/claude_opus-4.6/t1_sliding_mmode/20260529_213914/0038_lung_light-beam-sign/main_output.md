# 0038_lung_light-beam-sign

# M-mode Image Analysis

## Per-Position Classification

**p00:** Nearly completely black with only a faint thin bright line near the top. Minimal signal structure visible. → **UNCLASSIFIABLE**

**p01:** Very dark image with faint, barely perceptible texture in the lower half. Insufficient detail for reliable classification. → **UNCLASSIFIABLE**

**p02:** Emerging structure visible — faint brighter horizontal bands in the upper portion with a granular/sandy texture developing below. The texture below the pleural line is irregular and speckled rather than smooth horizontal lines. → **SEASHORE**

**p03:** Clear horizontal parallel lines above the pleural line. Below the pleural line, the texture is distinctly granular/sandy with vertical dark bands (rib shadows). Bright horizontal A-lines visible but the background between them is grainy, not smooth. → **SEASHORE**

**p04:** Prominent horizontal lines above, distinct pleural line (slightly wavy/irregular), and below: granular sandy texture with dark vertical shadow bands. No continuous clean horizontal lines below. → **SEASHORE**

**p05:** Bright horizontal bands above pleural line. Below: textured, granular appearance. A-lines present but background between them is sandy, not composed of parallel lines. → **SEASHORE**

**p06:** Similar to p05. Horizontal lines confined to above the pleural line; below shows granular/chaotic texture with vertical shadowing. Pleural line has slight irregularity. → **SEASHORE**

**p07:** Horizontal lines above, granular texture below the pleural line. Less contrast but the sandy pattern persists below. → **SEASHORE**

**p08:** Very dark image with minimal visible structure. Insufficient detail for classification. → **UNCLASSIFIABLE**

**p09:** Dark upper portion with very bright white parallel lines at the bottom edge — appears to be an edge/frame artifact, not genuine lung pattern. → **UNCLASSIFIABLE**

## Summary Table

| Position | Classification |
|----------|---------------|
| p00 | UNCLASSIFIABLE |
| p01 | UNCLASSIFIABLE |
| p02 | Seashore |
| p03 | Seashore |
| p04 | Seashore |
| p05 | Seashore |
| p06 | Seashore |
| p07 | Seashore |
| p08 | UNCLASSIFIABLE |
| p09 | UNCLASSIFIABLE |

## Overall Decision

All 6 classifiable positions (p02–p07) consistently show **seashore pattern** — granular/sandy texture below the pleural line with slightly wavy/irregular pleural lines indicating motion.

**Overall Label: PRESENT** (pleural sliding is present)
