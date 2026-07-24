# 0057_lung_blines-in-pulmonary-contusion

## Step 1 — Per-Position Classification

**p00 (Image 1 — ~5% from left):**
Top ~25% is nearly black (edge dropout), but the lower portion shows two bright columns with clearly **granular/speckled texture** and no regular horizontal lines below. → **Seashore** (low-confidence due to top darkness, but texture is distinctly sandy)

**p01 (Image 2):**
Two bright columns persist; top is still slightly dark but more signal present. Bright areas display **granular, sandy background texture**. No horizontal-line dominance in the subpleural zone. → **Seashore**

**p02 (Image 3):**
Tops of bright columns become **rounded/irregular**, consistent with pleural-line motion (waviness). Granular texture fills the subpleural zone. → **Seashore**

**p03 (Image 4):**
Similar rounded column-tops indicating pleural motion. One bright vertical line (reverberation artifact/A-line) visible over a clearly **granular background**. → **Seashore**

**p04 (Image 5):**
Horizontal bands (chest wall + A-lines) appear at the top; below them the background remains **distinctly granular** with no smooth parallel-line saturation. → **Seashore**

**p05 (Image 6):**
More horizontal banding at the top (A-lines), but the interstitial background between lines retains **granular/sandy character**. → **Seashore**

**p06 (Image 7):**
Upper region shows A-line-like horizontal stripes; lower zone remains **granular in texture between lines**. A-lines over sandy background = seashore, per the caveat. → **Seashore**

**p07 (Image 8):**
Complex bright areas with **irregular speckled/granular texture** throughout the subpleural zone; some horizontal elements present but background noise is non-linear. → **Seashore**

**p08 (Image 9):**
Upper-right corner is dark (right-edge dropout), but the central/left area shows sufficient signal with **granular texture**. → **Seashore** (borderline, but classifiable)

**p09 (Image 10 — ~95% from left):**
Strikingly different from all prior images. Shows **regular, thin, evenly-spaced bright horizontal lines spanning the full image width**, both in the near field and far field, with **no granular texture anywhere**. The pleural line region blends smoothly into the horizontal-line pattern. This is the classic **barcode/stratosphere pattern**. → **Stratosphere**

---

## Per-Position Summary Table

| Position | Classification |
|----------|---------------|
| p00 | Seashore |
| p01 | Seashore |
| p02 | Seashore |
| p03 | Seashore |
| p04 | Seashore |
| p05 | Seashore |
| p06 | Seashore |
| p07 | Seashore |
| p08 | Seashore |
| p09 | **Stratosphere** |

---

## Step 2 — Overall Decision

There is a **clear spatial transition**: positions p00–p08 uniformly show **seashore** (pleural sliding present), while position p09 shows **stratosphere** (pleural sliding absent). This coexistence of both patterns at different lateral positions, with sliding present on the left and absent on the right, defines a **lung point**.

### ✅ Overall Label: **BOTH** — Lung point detected
