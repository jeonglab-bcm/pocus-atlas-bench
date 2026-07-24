# 0003_lung_lung-point-finding

## Step 1 — Per-Position Classification

| Position | Observation | Classification |
|---|---|---|
| **p00** | Nearly entirely black; no discernible structure above noise threshold | **UNCLASSIFIABLE** |
| **p01** | Very dark; only faint trace at top margin; insufficient signal | **UNCLASSIFIABLE** |
| **p02** | Low-but-present signal; horizontal lines visible superiorly; below the pleural line the texture appears irregular/granular rather than composed of tight parallel lines; pleural line appears slightly wavy/non-straight | **SEASHORE** |
| **p03** | Clear image; multiple well-defined parallel horizontal bands throughout; the lower zone shows horizontal line continuation without sandy texture; pleural line straight | **STRATOSPHERE** |
| **p04** | Strong signal; classic dense barcode-like pattern; parallel lines fill both upper and lower zones with no granularity visible; perfectly straight pleural line | **STRATOSPHERE** |
| **p05** | Dense parallel horizontal lines top-to-bottom; no granular/sandy zone detected below the pleural line | **STRATOSPHERE** |
| **p06** | Continues barcode pattern; dense horizontal lines with no interruption by granularity | **STRATOSPHERE** |
| **p07** | Dense parallel horizontal lines throughout; slightly less bright than p05 but pattern identical; no granularity | **STRATOSPHERE** |
| **p08** | Horizontal banding with dense parallel lines; lower zone maintains line structure; no sandy texture apparent | **STRATOSPHERE** |
| **p09** | Noticeably darker than p08; signal diminishes toward right edge; structural detail insufficient for confident classification | **UNCLASSIFIABLE** |

---

## Step 2 — Overall Decision

**Classifiable positions: p02 through p08 (7 positions)**
- Seashore: **p02** (1 position — leftmost active zone)
- Stratosphere: **p03, p04, p05, p06, p07, p08** (6 positions)

A **clear spatial transition** is present: seashore at the left margin of the active region transitioning to stratosphere across the remainder of the scan. This coexistence of both patterns at different lateral positions is the defining feature of a **lung point**.

---

## ✅ Overall Label: **BOTH** — Lung Point Detected

> **Interpretation:** Pleural sliding is **present** at the far-left lateral position (p02, ~25%) and **absent** (stratosphere/barcode) across the rest of the probe footprint (p03–p08, ~35–85%). The transition between p02 and p03 represents the **lung point** — the lateral boundary where the partially collapsed lung reaches during respiration.
