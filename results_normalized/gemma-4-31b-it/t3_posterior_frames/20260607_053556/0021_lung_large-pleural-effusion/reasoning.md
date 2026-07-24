# 0021_lung_large-pleural-effusion — Reasoning

The user wants me to analyze a sequence of ultrasound frames from a posterior lung zone (PLAPS point).

1.  **Analyze the images:**
    *   The images show a posterior view of the lung.
    *   There is a large anechoic (black) area, which is characteristic of a pleural effusion.
    *   Within this fluid, there's a piece of lung that looks irregular and is moving/floating. This looks like the "jellyfish sign" or fragmented consolidated lung within an effusion.
    *   The consolidated lung has a tissue-like appearance (hepatization).
    *   The combination of a large fluid collection (anechoic space) and fragmented, consolidated lung indicates both pleural effusion and consolidation.

2.  **Check for specific signs:**
    *   **Effusion:** Large black space is visible. This matches the signs for pleural effusion.
    *   **Consolidation:** There's a consolidated piece of lung (hepatized appearance) floating in the fluid.
    *   **Combination:** Since both are present, `type = "both"`.

3.  **Formulate the description:**
    *   Start by noting the large anechoic space, which represents a pleural effusion.
    *   Mention the fragmented, echogenic lung tissue floating within the fluid, which is characteristic of the jellyfish sign and indicates consolidated lung (hepatization).
    *   Conclude that both effusion and consolidation are present.

4.  **Final classification:**
    *   `plaps = true`
    *   `type = "both"`
