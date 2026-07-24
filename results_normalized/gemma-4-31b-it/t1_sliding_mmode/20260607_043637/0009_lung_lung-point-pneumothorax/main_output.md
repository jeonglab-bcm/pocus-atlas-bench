# 0009_lung_lung-point-pneumothorax

Based on the analysis of the 10 M-mode ultrasound strips, here is the per-position classification:

**Step 1: Per-position classification**
*   **p00**: The image is nearly black with very minimal signal, providing insufficient detail for classification. **Unclassifiable**.
*   **p01**: Shows a clear granular, "sandy" texture below the pleural line, indicating pleural sliding. **Seashore**.
*   **p02**: Shows a clear granular texture below the pleural line. **Seashore**.
*   **p03**: Shows a clear granular texture below the pleural line. **Seashore**.
*   **p04**: Shows a clear granular texture below the pleural line. **Seashore**.
*   **p05**: Maintains a grainy background texture, despite the presence of horizontal A-lines. **Seashore**.
*   **p06**: Transitioning, but still exhibits a grainy/sandy texture below the pleural line. **Seashore**.
*   **p07**: The grainy texture has disappeared and is replaced by continuous, dense parallel horizontal lines. **Stratosphere**.
*   **p08**: Shows dense, continuous parallel horizontal lines throughout, with no granularity. **Stratosphere**.
*   **p09**: Shows dense, continuous parallel horizontal lines throughout, with no granularity. **Stratosphere**.

**Step 2: Overall decision**
There is a clear spatial transition across the active ultrasound region. The left-to-middle positions (p01–p06) exhibit the **Seashore** pattern (sliding present), while the rightmost positions (p07–p09) exhibit the **Stratosphere/Barcode** pattern (sliding absent). The coexistence of these two patterns across different lateral positions is diagnostic of a lung point.

Overall label: **both**
