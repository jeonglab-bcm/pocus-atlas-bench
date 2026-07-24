# 0078_lung_jellyfish — Reasoning

The user wants me to analyze a sequence of ultrasound frames to identify a PLAPS pattern (Posterolateral Alveolar and/or Pleural Syndrome).

1.  **Analyze the images:**
    *   The images are sequential frames from a lung ultrasound (LUS) video.
    *   The label "RT POSTERIOR" indicates it's the right posterior lung zone.
    *   The images show a large, dark (anechoic) area at the top/superior part of the scan, which is likely a pleural effusion.
    *   Within/below this fluid collection, there is lung tissue that looks solid and echogenic, similar to liver texture. This is "hepatization".
    *   Looking closely at the sequence (especially towards the end), I can see the lung tissue (consolidated part) moving within the fluid collection. It looks like a "jellyfish" (undulating, floating mass of tissue in fluid).
    *   There is an irregular border between the consolidative lung and the aerated lung/fluid, which might be a "shred sign".
    *   I don't clearly see punctate/linear air bronchograms in these specific frames, but the tissue-like appearance is very strong.
    *   The "quad sign" is also visible: the anechoic space is bounded by the pleural line (superiorly), the lung line (inferiorly), and the rib shadows (laterally).

2.  **Apply the criteria:**
    *   **Effusion signs:**
        *   **Quad sign:** Yes, a quadrilateral anechoic space is visible.
        *   **Jellyfish sign:** Yes, the consolidated lung tissue is floating and moving within the anechoic fluid collection as the probe or patient moves (or during respiration). It looks like a mass of tissue in fluid.
    *   **Consolidation signs:**
        *   **Tissue-like hepatization:** Yes, the lung appears solid and echogenic, resembling liver tissue.
        *   **Shred sign:** Yes, the border between the consolidated and aerated lung is irregular.
    *   **Classification:**
        *   Since both effusion (quad sign, jellyfish sign) and consolidation (hepatization, shred sign) are present, `plaps = true` and `type = "both"`.

3.  **Construct the final response:**
    *   **Observation:**
        *   The ultrasound images show a large anechoic (black) space in the right posterior lung zone, which is characteristic of a **pleural effusion** (demonstrated by the **quad sign**).
        *   Within this fluid, there is a mass of solid-looking, echogenic lung tissue that appears to be floating and moving, which is the **jellyfish sign**.
        *   The lung tissue itself exhibits **tissue-like hepatization**, appearing solid and similar to liver parenchyma.
        *   There is also an irregular, "shredded" border between the consolidated lung and the aerated lung/fluid (**shred sign**).
    *   **Conclusion:**
        *   `plaps = true`
        *   `type = "both"`
