# 0037_lung_pulmonary-contusion — Reasoning

The user wants me to analyze a series of lung ultrasound (LUS) frames from an anterior lung zone.

1.  **Analyze frames for B-lines:**
    *   I see hyperechoic vertical artifacts originating from the pleural line and extending to the bottom of the screen.
    *   These artifacts are present in all frames.
    *   They are quite confluent, especially in the center, creating a "white lung" or ground-glass appearance.
    *   In some areas, they look a bit more discrete, but overall they coalesce.
    *   Therefore, `lung_rockets = true`.
    *   Since they are confluent/coalescing, the subtype is `ground_glass`.

2.  **Analyze frames for consolidation:**
    *   I don't see any tissue-like hepatization of the lung.
    *   I don't see a shred sign (irregular border between air and tissue).
    *   I don't see air bronchograms (bright spots in a solid-looking lung).
    *   The hyperechoic areas are vertical artifacts (B-lines), not solid tissue.
    *   Therefore, `consolidation = false`.
    *   `consolidation_type = null`.

3.  **Final Synthesis:**
    *   B-lines are present and confluent.
    *   No evidence of consolidation.
