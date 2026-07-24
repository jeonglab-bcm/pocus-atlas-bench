# 0009_lung_lung-point-pneumothorax

# Lung Ultrasound M-Mode Analysis

## Step 1 — Per-Position Classification

### p00
**Observation:** Upper ~45% is nearly black with minimal structure; lower half shows ~6 bright vertical columns separated by dark gaps. Very limited active signal.
**Classification: UNCLASSIFIABLE** — edge position, insufficient active signal.

---

### p01
**Observation:** Upper ~30% shows a few clean parallel horizontal lines (chest wall). Lower ~70% displays prominent bright vertical columns (A-lines) with an **irregular, somewhat granular background texture between them** — not organized continuous horizontal lines. The pleural line appears slightly non-uniform.
**Classification: SEASHORE** — horizontal lines above, granular/A-line texture below indicates sliding.

---

### p02
**Observation:** Upper ~40% shows cleaner parallel horizontal lines. Below, vertical bright columns (A-lines) persist over a **grainy, non-linear background**. Horizontal structure is present but interrupted by sandy/granular elements between the A-line columns.
**Classification: SEASHORE** — two-zone pattern with granular texture below.

---

### p03
**Observation:** Upper ~40% shows **dense, organized parallel horizontal lines** (chest wall). A distinct bright horizontal band marks the pleural line. Below: bright vertical A-line columns over a **textured, somewhat granular/irregular background** — not purely continuous parallel lines.
**Classification: SEASHORE** — clear two-zone structure; A-lines over granular background below pleural line.

---

### p04
**Observation:** Very similar to p03. Upper portion: very dense organized horizontal lines + a highly prominent bright pleural line. Lower portion: bright vertical A-line columns with **granular/irregular inter-column texture**. The pleural line area appears slightly wavy/irregular.
**Classification: SEASHORE** — granular background between A-lines confirms sliding.

---

### p05
**Observation:** Dense horizontal lines in upper portion with a very bright pleural band. Lower portion: vertical A-line columns still prominent, though inter-column texture shows **slightly more horizontal organization** compared to p03–p04. Granular elements still present.
**Classification: SEASHORE** — granularity still visible between A-lines, though approaching transition.

---

### p06
**Observation:** Vertical A-line columns are now less dominant; **horizontal striping is increasingly present in the lower zone as well**. Some granular texture persists but the pattern is becoming more organized. The overall image begins showing horizontal lines throughout.
**Classification: SEASHORE** (transitional) — granular elements still detectable, but border zone.

---

### p07
**Observation:** The image is now **dominated by dense, continuous, evenly spaced parallel horizontal lines from top to bottom**. Vertical columns are nearly absent. The few residual faint vertical structures (lower-left) do not disrupt the overwhelmingly horizontal barcode pattern. No discernible granular texture anywhere.
**Classification: STRATOSPHERE/BARCODE** — uniform horizontal lines throughout, no granularity.

---

### p08
**Observation:** **Very uniform dense horizontal parallel lines** throughout the upper ~65–70% of the image. The lower portion is darker but retains faint horizontal continuations. Classic barcode appearance; no sandy/granular texture visible anywhere.
**Classification: STRATOSPHERE/BARCODE** — clear barcode pattern.

---

### p09
**Observation:** Overall image is significantly dimmer than p08, with only faint horizontal lines and a largely dark lower half. Reduced brightness suggests exit from the active beam region.
**Classification: UNCLASSIFIABLE** — edge position, degraded signal.

---

## Summary Table

| Position | Classification | Notes |
|----------|---------------|-------|
| p00 | **UNCLASSIFIABLE** | Left edge, nearly black |
| p01 | **Seashore** | Granular texture below pleural line |
| p02 | **Seashore** | A-lines on granular background |
| p03 | **Seashore** | Clear two-zone pattern |
| p04 | **Seashore** | Clear two-zone pattern |
| p05 | **Seashore** | Granular still present |
| p06 | **Seashore** | Transitional but granular detectable |
| p07 | **Stratosphere** | All horizontal lines, no granularity |
| p08 | **Stratosphere** | Classic barcode |
| p09 | **UNCLASSIFIABLE** | Right edge, degraded signal |

---

## Step 2 — Overall Decision

**Classifiable positions:** p01–p08 (8 positions)
- Seashore: p01, p02, p03, p04, p05, p06 (6 positions, left-to-center)
- Stratosphere: p07, p08 (2 positions, right side)

There is a **clear spatial transition** across lateral positions: seashore pattern (pleural sliding PRESENT) on the left → stratosphere pattern (pleural sliding ABSENT) on the right. Both patterns coexist across different lateral positions within the same scan region.

> ## ✅ Overall Label: **"BOTH" — LUNG POINT IDENTIFIED**
> The spatial coexistence of seashore (p01–p06) and stratosphere (p07–p08) patterns at different lateral positions defines a **lung point**, marking the boundary between aerated and non-aerated lung.
