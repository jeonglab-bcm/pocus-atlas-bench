# 0119_lung_jr_normal-lung-slide

# M-Mode Analysis: Per-Position Classification

## Position-by-Position Assessment

**p00 (leftmost):** Horizontal lines visible above the pleural line. Below the pleural line, there is a granular/sandy texture with A-lines (bright periodic horizontal lines) superimposed. The pleural line shows slight irregularity. Background between A-lines is textured, not composed of continuous lines.
→ **Seashore**

**p01:** Similar to p00 — organized horizontal lines above, with a visible pleural line. Below, A-lines are present over a background that retains some granular quality. Not purely continuous lines below.
→ **Seashore**

**p02:** Dense, continuous parallel horizontal lines extending throughout the entire image, both above and below the pleural line. No granular texture discernible between lines. The sub-pleural area is filled with organized, uninterrupted horizontal striations.
→ **Stratosphere**

**p03:** Very similar to p02 — dense continuous horizontal lines throughout, with no appreciable granularity in the sub-pleural region. Classic barcode appearance.
→ **Stratosphere**

**p04:** Same pattern as p02-p03 — continuous horizontal lines pervade both regions. No sandy texture visible.
→ **Stratosphere**

**p05:** Horizontal lines continue throughout, slightly less dense than p02-p04, but still organized as continuous parallel lines without granularity below the pleural line.
→ **Stratosphere**

**p06:** Bright pleural line visible. Below the pleural line, the area is relatively dark with a faint A-line — crucially, there are NO dense continuous horizontal lines like in p02-p05. The absence of organized stratosphere lines with visible structure suggests sliding is present.
→ **Seashore**

**p07:** Pleural line and A-line visible. Sub-pleural region lacks the dense continuous line pattern; texture between A-lines is dark/slightly granular rather than organized horizontal lines.
→ **Seashore**

**p08:** Very dark image with minimal discernible structure. Insufficient detail to determine pattern reliably.
→ **Unclassifiable**

**p09:** Nearly black strip with no meaningful signal.
→ **Unclassifiable**

## Summary Table

| Position | Classification |
|----------|---------------|
| p00 | Seashore |
| p01 | Seashore |
| p02 | Stratosphere |
| p03 | Stratosphere |
| p04 | Stratosphere |
| p05 | Stratosphere |
| p06 | Seashore |
| p07 | Seashore |
| p08 | Unclassifiable |
| p09 | Unclassifiable |

## Overall Decision

Among the 8 classifiable positions, there is a clear spatial transition:
- **Seashore** at positions p00–p01 and p06–p07 (sliding present)
- **Stratosphere** at positions p02–p05 (sliding absent)

The coexistence of both patterns across different spatial positions indicates a **lung point** — the boundary between sliding and non-sliding lung.

## **Overall Label: BOTH (Lung Point)**
