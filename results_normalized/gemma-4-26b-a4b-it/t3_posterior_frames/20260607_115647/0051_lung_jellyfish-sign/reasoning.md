# 0051_lung_jellyfish-sign — Reasoning

The user wants me to analyze a lung ultrasound (LUS) video clip to identify the PLAPS (Posterolateral Alveolar and/or Pleural Syndrome) pattern.

1.  **Identify the region**: This is a posterior lung zone view (PLAPS point).
2.  **Scan for effusion signs**:
    *   **Quad sign**: I see a large anechoic (black) area. It's bounded by the pleural line at the top and the lung at the bottom. The ribs might provide lateral boundaries.
    *   **Sinusoid sign**: Not clearly assessable from a static clip, but looking at the animation, there's movement.
    *   **Jellyfish sign**: I see a piece of lung tissue floating within the large dark area. The lung tissue is clearly moving within the fluid. This is the classic "jellyfish sign".
3.  **Scan for consolidation signs**:
    *   **Tissue-like hepatization**: The floating piece of lung looks solid and echogenic.
    *   **Shred sign**: The border of the floating lung tissue is somewhat irregular.
    *   **Air bronchograms**: It's hard to be certain without zooming in, but there might be small bright spots.
4.  **Analyze the animation**:
    *   The large dark area is an anechoic space, representing fluid (effusion).
    *   Within this fluid, a chunk of lung tissue is visible.
    *   As the respiratory cycle occurs, this chunk of lung tissue moves/undulates within the dark fluid.
    *   This is a classic "jellyfish sign".
5.  **Determine classification**:
    *   `plaps = true` because the jellyfish sign is present (indicating both effusion and consolidated lung).
    *   `type = "both"` because there is clearly a large amount of fluid (effusion) and a piece of consolidated lung floating in it (consolidation).

Let's re-examine:
- The large black area is the effusion.
- The moving, solid-looking structure inside is the consolidated lung.
- The movement of the consolidated lung within the fluid is the **jellyfish sign**.
- The presence of both effusion and consolidation means `type = "both"`.

Conclusion:
- `plaps = true`
- `type = "both"`
