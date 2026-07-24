# 0050_lung_plaps-pneumonia — Reasoning

The user wants me to analyze a series of ultrasound frames from a posterior lung zone (PLAPS point).

1.  **Identify the anatomy**: The images show a posterior/lateral view of the lung.
2.  **Look for effusion signs**:
    *   **Quad sign**: I see a large, anechoic (black) space. It's bounded superiorly by the pleural line and inferiorly by a floating piece of lung. This looks like a pleural effusion.
    *   **Jellyfish sign**: The consolidated lung tissue is floating and moving within the anechoic fluid collection. This is a characteristic "jellyfish sign".
3.  **Look for consolidation signs**:
    *   **Tissue-like hepatization**: The lung tissue within the fluid (the "jellyfish") has a tissue-like, hepatized appearance, similar to the liver.
    *   **Air bronchograms**: There are some bright, hyperechoic foci within this hepatized lung, which likely represent air bronchograms.
4.  **Determine the pattern**:
    *   There is a clear anechoic fluid collection (effusion).
    *   There is consolidated, hepatized lung tissue floating in that fluid (consolidation).
    *   Since both are present, `plaps = true` and `type = "both"`.

*   Anechoic space: Present, large.
*   Floating lung tissue: Present, moving during respiration.
*   Lung tissue texture: Hepatized.
*   Air bronchograms: Present (bright dots in consolidated area).
*   Overall: This is a classic PLAPS pattern with both pleural effusion and associated lung consolidation/atelectasis.
