# 0098_lung_blunt-trauma-effusion — Reasoning

The user wants me to analyze a sequence of images from a lung ultrasound (LUS) video clip of a posterior lung zone (PLAPS point).

1.  **Analyze the images:**
    *   The images show a posterior lung zone.
    *   I see a large, hypoechoic area that looks like consolidated lung tissue.
    *   The texture of this area is solid and resembles liver tissue (tissue-like hepatization).
    *   There is a clear, irregular, "shredded" border between this consolidated tissue and the more aerated (or at least different) area above/beside it. This is a "shred sign".
    *   I don't see a clear pleural effusion (no quad sign, no jelly fish sign, no clear anechoic fluid collection).
    *   The hepatized area is prominent.
    *   I can't clearly see air bronchograms due to the image quality, but the hepatization and shred sign are quite distinct.
    *   The lung in this area doesn't look like normal aerated lung; it's solid.

2.  **Check the criteria:**
    *   **Effusion signs:** None clearly visible.
    *   **Consolidation signs:**
        *   **Tissue-like hepatization**: Yes, the central large area looks solid and echogenic, similar to liver tissue.
        *   **Shred sign**: Yes, the border between the hepatized area and the adjacent lung is irregular and "shredded".
        *   **Air bronchograms**: Not clearly visible but not strictly required if other signs are present.
    *   **Classification:**
        *   `plaps = true` because consolidation signs (hepatization, shred sign) are present.
        *   `type = "consolidation"` because there's no clear sign of effusion (no quad sign, etc.).

3.  **Structure the description:**
    *   Mention the solid, liver-like appearance of the lung parenchyma (tissue-like hepatization).
    *   Point out the irregular, shredded border (shred sign) between the consolidated lung and the surrounding lung.
    *   Note the absence of clear fluid signs like a quad sign or jellyfish sign.
    *   Conclude with the requested classification.
