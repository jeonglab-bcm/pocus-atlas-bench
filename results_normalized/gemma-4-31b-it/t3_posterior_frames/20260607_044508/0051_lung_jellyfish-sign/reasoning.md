# 0051_lung_jellyfish-sign — Reasoning

The user wants me to analyze a sequence of ultrasound frames from a PLAPS point.

1.  **Analyze the images:**
    *   The images show a large anechoic (black) area, which is characteristic of a pleural effusion.
    *   Inside this anechoic area, there is a floating, undulating tissue-like structure. This structure moves with the respiratory cycle. This is the "jellyfish sign", which represents atelectatic or consolidated lung floating in pleural fluid.
    *   The tissue-like structure itself shows hepatization (tissue-like appearance).
    *   The combination of a large pleural effusion and consolidated/atelectatic lung is a classic PLAPS pattern.

2.  **Match signs to categories:**
    *   **Effusion signs:** There is a large anechoic space. The floating lung is the "jellyfish sign".
    *   **Consolidation signs:** The floating lung has a tissue-like appearance (hepatization).
    *   Since both are present, `plaps = true` and `type = "both"`.

3.  **Draft the description:**
    *   Observe a large anechoic space consistent with a pleural effusion.
    *   Within this fluid, a piece of consolidated/atelectatic lung is seen floating and undulating during respiration, which is the characteristic "jellyfish sign".
    *   The floating lung shows tissue-like hepatization.
    *   Conclusion: PLAPS is present, and it's a combination of effusion and consolidation.
