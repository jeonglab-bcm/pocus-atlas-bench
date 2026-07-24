# 0043_lung_normal-lung

# M-Mode Image Analysis

## Per-Position Classification

**p00:** Nearly completely black with minimal signal visible only at the very bottom. This is at the edge of the active ultrasound region. → **Unclassifiable**

**p01:** Dark overall but granular/noisy texture is emerging in the lower half, with minimal horizontal line structure above. Subtle sandy texture visible below a faintly discernible pleural line. → **Seashore**

**p02:** Clear structure now visible. Horizontal lines in the upper (superficial) portion, a bright pleural line region, and below it a distinctly granular/sandy texture with some A-lines superimposed. The pleural line appears somewhat wavy/irregular. → **Seashore**

**p03:** Similar to p02. Parallel horizontal lines above the pleural line, with granular/sandy texture below. A-lines present but background texture between them is clearly granular. → **Seashore**

**p04:** Same pattern as p03. Sandy texture below pleural line, horizontal stratified lines above. Granularity clearly present between A-line artifacts. → **Seashore**

**p05:** Horizontal lines above, granular texture below with A-lines. Sandy background persists between the A-line reverberations. → **Seashore**

**p06:** Horizontal lines above with granular/speckled texture below. More A-lines visible but the inter-line texture remains granular, not purely linear. → **Seashore**

**p07:** Similar to p06. Granular texture between horizontal A-lines below the pleural line. The sandy pattern is still dominant. → **Seashore**

**p08:** Upper portion shows granular texture with a visible pleural line; bottom shows bright horizontal lines that appear to be display/edge artifacts. Main diagnostic area is granular. → **Seashore**

**p09:** Upper half mostly dark; bottom half shows very bright, smooth, dense parallel lines that are display frame elements, not tissue. Insufficient diagnostic tissue visible. → **Unclassifiable**

## Summary

| Position | Classification |
|----------|---------------|
| p00 | Unclassifiable |
| p01 | Seashore |
| p02 | Seashore |
| p03 | Seashore |
| p04 | Seashore |
| p05 | Seashore |
| p06 | Seashore |
| p07 | Seashore |
| p08 | Seashore |
| p09 | Unclassifiable |

## Overall Decision

8 out of 8 classifiable positions show **seashore** pattern (granular/sandy texture below the pleural line with some pleural line irregularity).

**Overall Label: PRESENT** (pleural sliding is present)
