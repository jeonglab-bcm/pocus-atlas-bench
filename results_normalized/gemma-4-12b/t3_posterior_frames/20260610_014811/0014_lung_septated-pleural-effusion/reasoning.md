# 0014_lung_septated-pleural-effusion — Reasoning

The user wants me to analyze a lung ultrasound (LUS) video.
The task is to identify if a PLAPS pattern is present and classify it.

1.  **Analyze the video:**
    *   The video shows a posterior/lateral lung zone (PLAPS point).
    *   There's a large anechoic (black) area, which suggests pleural effusion.
    *   Within this anechoic area, there's a floating, irregular, hyperechoic structure that moves with respiration. This is characteristic of the "jellyfish sign" (undulating atelectatic lung within a fluid collection).
    *   The surrounding lung tissue looks solid and echogenic, similar to liver texture, which is "tissue-like hepatization".
    *   The irregular deep border of the consolidated lung is visible, which is the "shred sign".
    *   The anechoic space is bounded by the pleural line and the lung line, and there's a clear quadrilateral shape formed, suggesting a "quad sign".
    *   Since both effusion (jellyfish sign, quad sign) and consolidation (hepatization, shred sign) are visible, `plaps = true` and `type = "both"`.

2.  **Refine observations:**
    *   **Effusion signs:**
        *   **Jellyfish sign:** Clearly visible. There's an undulating, hyperechoic structure floating in a large black fluid collection. It moves with respiration.
        *   **Quad sign:** The pleural line is at the top of the fluid, and the lung line is at the bottom. The rib shadows are on the sides. This forms a quadrilateral space.
    *   **Consolidation signs:**
        *   **Tissue-like hepatization:** The lung tissue below the jellyfish is solid-looking and echogenic, like liver tissue.
        *   **Shred sign:** There's a jagged, irregular border between the consolidated area and the aerated lung (or the fluid).
    *   **Conclusion:** PLAPS is present. It shows both effusion and consolidation.

3.  **Final output structure:**
    *   Observation: Describe the jelly-fish sign, quad sign, hepatization, and shred sign.
    *   Classification: `plaps = true`, `type = "both"`.
