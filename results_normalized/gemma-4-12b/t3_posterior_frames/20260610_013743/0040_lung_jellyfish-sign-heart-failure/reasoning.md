# 0040_lung_jellyfish-sign-heart-failure — Reasoning

Thinking Process:

1.  **Analyze the Request:** The user wants to identify the presence of a PLAPS (Posterolateral Alveolar and/or Pleural Syndrome) pattern in a lung ultrasound (LUS) image of a posterior lung zone. They provided several signs for effusion (quad sign, sinusoid sign, jellyfish sign) and consolidation (tissue-like hepatization, shred sign, air bronchograms).

2.  **Analyze the Image:**
    *   **Overall view:** Posterior lung zone.
    *   **Central large dark area:** This is a large anechoic (black) space.
    *   **Superior boundary of the dark space:** There's a thin, somewhat irregular line.
    *   **Inferior/Lateral boundaries:** It's bounded by bright, linear reflective structures.
    *   **Specific Signs Search:**
        *   *Quad sign:* I see a large, well-defined anechoic space. It is bounded superiorly by the pleural line and inferiorly by a lung line. The lateral boundaries are the rib shadows. This forms a quadrilateral shape. It's very prominent.
        *   *Jellyfish sign:* Not clearly visible here; the "jellyfish" (atelectatic lung) isn't undulating in a large pool of fluid in a way that's classically obvious in this static frame, although some tissue is visible.
        *   *Tissue-like hepatization:* There's some tissue-like material adjacent to the fluid, but the main finding is the huge fluid collection.
        *   *Shred sign:* Not clearly visible as a primary finding.
        *   *Air bronchograms:* Not clearly visible.
    *   **Dominant Finding:** Large pleural effusion with a prominent quad sign.

3.  **Evaluate against Criteria:**
    *   *Effusion signs:* Quad sign is clearly present. The large anechoic space is characteristic of a large effusion in the dependent portion of the lung.
    *   *Consolidation signs:* Some tissue might be consolidated (hepatized) adjacent to it, but the effusion is the primary feature.
    *   *Classification:*
        *   `plaps = true` (due to quad sign/effusion).
        *   `type = "effusion"` (it's predominantly fluid-filled).

4.  **Formulate Description:**
    *   Observation: A large, well-circumscribed anechoic (black) area is visible in the posterior lung zone.
    *   Sign Identification: This area is bounded by the pleural line above, a lung line below, and rib shadows laterally, forming a distinct quadrilateral shape known as the **quad sign**.
    *   Conclusion: The image shows a large pleural effusion.

5.  **Final Output Structure:**
    *   Description of findings.
    *   Classification tags.
