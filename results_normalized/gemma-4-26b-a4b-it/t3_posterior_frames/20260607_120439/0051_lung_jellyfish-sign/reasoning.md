# 0051_lung_jellyfish-sign — Reasoning

The user wants me to analyze a lung ultrasound video clip.

1.  **Identify the anatomy and view:** The video shows an ultrasound scan, likely a posterior lung view (PLAPS point area).
2.  **Observe findings frame by frame:**
    *   In the initial frames, there is a large, dark (anechoic) area. This represents fluid (effusion).
    *   Within this fluid, there's a more echogenic structure that is moving/undulating. It looks like lung tissue that is collapsed/atelectatic.
    *   This movement of the lung tissue within the fluid is a classic "jellyfish sign".
    *   The fluid collection forms a dark space. Looking at the shape, it's bounded by pleural lines and ribs.
    *   The lung tissue inside is echogenic and doesn't have typical aeration artifacts. It looks more like solid tissue (hepatization/consolidation) but it's clearly floating in fluid.
    *   Let's re-examine: The large black area is the effusion. The piece of lung tissue inside is moving rhythmically. This is the jellyfish sign.
    *   The lung tissue itself looks consolidated (hepatized).
    *   So, we see both an effusion and consolidation.
3.  **Apply classification criteria:**
    *   **Effusion signs:** Jellyfish sign is clearly present. The anechoic space is also present.
    *   **Consolidation signs:** The lung tissue looks hepatized.
    *   **Conclusion:**
        *   `plaps = true` (signs are present).
        *   `type = "both"` (both effusion and consolidation are visible). The jellyfish sign specifically combines these two: consolidated lung floating in an effusion.

Let's double-check the signs.
- **Jellyfish sign**: "Floating, undulating atelectatic lung within a surrounding effusion, resembling a jellyfish in water." Yes, that's what is happening. The lung tissue (atelectatic/consolidated) is moving within the dark fluid.
- **Hepatization**: The lung tissue has a solid appearance.
- **Effusion**: The dark area is clearly fluid.

Final determination:
- `plaps = true`
- `type = "both"` (due to the jellyfish sign which is a combination, and the clear presence of an anechoic fluid pocket and hepatized lung tissue).
