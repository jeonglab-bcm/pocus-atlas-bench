# 0056_lung_lung-point

# Lung Ultrasound M-Mode Analysis

## Step 1 — Per-Position Classification

| Position | Observations | Classification |
|----------|-------------|----------------|
| **p00** | Thin bright horizontal lines confined to top ~15%; lower ~85% is nearly pure black with no discernible texture | **UNCLASSIFIABLE** |
| **p01** | Horizontal lines in upper ~30%; lower ~70% remains very dark/black with minimal structure | **UNCLASSIFIABLE** |
| **p02** | Horizontal lines above; below the pleural line, bumpy/rounded structures begin to emerge — early granular texture visible in mid-lower zone | **SEASHORE** |
| **p03** | Clear horizontal lines above pleural line; below shows multiple distinct rounded "cloud-blob" structures — classic sandy/granular seashore texture | **SEASHORE** |
| **p04** | Numerous horizontal lines above; rounded lobular structures clearly present below the pleural line; pleural line appears slightly irregular/wavy | **SEASHORE** |
| **p05** | Horizontal lines above; below the pleural line shows mixed granular texture with wavy/irregular pleural line contour — motion-consistent | **SEASHORE** |
| **p06** | Horizontal lines above; below shows diffuse granular/blurry sandy texture; pleural line has visible waviness | **SEASHORE** |
| **p07** | **Dense continuous parallel horizontal bands fill the entire image** — both above AND below the pleural line; pleural line is straight/smooth; no granularity anywhere | **STRATOSPHERE** |
| **p08** | Horizontal lines above; broad bright pleural band; below shows faint horizontal banding with no granular texture; pleural line straight | **STRATOSPHERE** |
| **p09** | A few upper horizontal lines, broad bright mid-band, lower ~50% nearly black; insufficient texture to classify reliably | **UNCLASSIFIABLE** |

---

## Step 2 — Overall Decision

**Classifiable positions:** p02–p08 (7 positions)

- **p02–p06** (5 positions): **SEASHORE** → pleural sliding **PRESENT**
- **p07–p08** (2 positions): **STRATOSPHERE** → pleural sliding **ABSENT**

There is a **clear spatial transition** — seashore pattern on the left (medial) side giving way to stratosphere/barcode pattern on the right (lateral) side across the lung field.

---

## 🫁 Overall Label: **"BOTH" — Lung Point Present**

> A lung point is identified at approximately the p06/p07 boundary. Pleural sliding is **present** medially and **absent** laterally, consistent with a pneumothorax with a detectable lung point at this intercostal level.
