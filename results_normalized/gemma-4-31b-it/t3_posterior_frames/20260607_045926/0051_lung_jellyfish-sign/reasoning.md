# 0051_lung_jellyfish-sign — Reasoning

The user wants me to analyze a sequence of ultrasound images from a posterior lung zone (PLAPS point).

1.  **Analyze the images:**
    *   The images show a large anechoic (black) area. This is characteristic of pleural effusion.
    *   Within this anechoic area, there is a piece of lung tissue that is floating and moving. This matches the "jellyfish sign" (floating, undulating atelectatic lung within a surrounding effusion).
    *   The lung tissue itself looks consolidated (hepatization), as it's solid and echogenic compared to the fluid around it.
    *   The overall picture is a combination of a large pleural effusion and a consolidated/atelectatic lung fragment.

2.  **Evaluate against the provided signs:**
    *   **Effusion signs:** The large black space is an effusion. The floating piece of lung is the "jellyfish sign".
    *   **Consolidation signs:** The floating lung piece exhibits "tissue-like hepatization".
    *   Therefore, both effusion and consolidation are present.

3.  **Determine the classification:**
    *   `plaps = true` (since effusion and consolidation are present).
    *   `type = "both"` (since both fluid and consolidated lung are visible).

4.  **Draft the description:**
    *   The ultrasound images demonstrate a large anechoic space, consistent with a pleural effusion.
    *   Within this fluid collection, there is a fragment of consolidated lung tissue that appears to be floating and moving, which is known as the "jellyfish sign".
    *   The lung fragment shows hepatization (tissue-like appearance).
    *   This combination of findings is typical for a PLAPS pattern involving both pleural effusion and consolidation/atelectasis.
