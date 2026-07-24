# 0021_lung_large-pleural-effusion — Reasoning

The user wants me to analyze a lung ultrasound (LUS) video clip.
The goal is to determine if a PLAPS (Posterolateral Alveolar and/or Pleural Syndrome) pattern is present.

1.  **Analyze the video frames:**
    *   The video shows a lung ultrasound at the PLAPS point (posterior/lateral zone).
    *   I see a large anechoic (black) space below the lung tissue. This represents fluid (effusion).
    *   The lung tissue itself looks solid and echogenic, like liver tissue. This is hepatization.
    *   There is a clear irregular border between the aerated part of the lung (above, with some artifacts) and the consolidated part (below, in the fluid).
    *   Looking closely at the consolidated lung within the fluid, I can see some small bright spots, which could be air bronchograms.
    *   The lung tissue is floating in the fluid. This is the "jellyfish sign".
    *   The fluid collection forms a quadrilateral shape bounded by the pleural line and ribs. This is the "quad sign".

2.  **Apply the criteria provided:**
    *   **Effusion signs:**
        *   **Quad sign**: Yes, there's a large anechoic space that looks like it could form a quadrilateral.
        *   **Jellyfish sign**: Yes, the hepatized lung tissue is floating within the anechoic fluid.
    *   **Consolidation signs:**
        *   **Tissue-like hepatization**: Yes, the lung looks like solid tissue (liver-like).
        *   **Shred sign**: Yes, the border between the aerated and consolidated lung is irregular/shredded.
        *   **Air bronchograms**: Yes, there are some bright punctate areas within the consolidation.

3.  **Classify the findings:**
    *   `plaps = true`: Because both effusion and consolidation signs are present.
    *   `type = "both"`: Because both effusion (quad, jellyfish signs) and consolidation (hepatization, shred, air bronchograms) are clearly visible.

4.  **Final output format:**
    *   Describe observations.
    *   State conclusion (`plaps = true`, `type = "both"`).
