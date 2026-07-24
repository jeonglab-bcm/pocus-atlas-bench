# 0015_lung_plaps-consolidation — Reasoning

The user wants me to analyze a series of ultrasound frames to identify a PLAPS pattern.

**1. Analyze the images:**
*   **Image 1:** Shows a large anechoic (black) area in the center/right. Superiorly, there's a pleural line. Laterally, there are rib shadows. The inferior border is somewhat obscured but looks like lung tissue below. This looks like a fluid collection. Wait, let's look closer. It's a large dark area.
*   **Image 2:** The view changes. Now I see lung tissue with some hyperechoic lines (ribs?) and some dark areas. There's a vertical dark shadow.
*   **Image 3:** Similar to Image 2.
*   **Image 4:** Similar to Image 3.
*   **Image 5:** The image shows a distinct interface. On the left is a more homogeneous, tissue-like area. On the right is darker. There is a vertical dark shadow, likely a rib shadow.
*   **Image 6:** Shows a similar pattern.
*   **Image 7:** Similar pattern.
*   **Image 8:** Similar pattern.

Let's re-evaluate the sequence as a whole. It looks like a video sequence of a lung ultrasound.
*   **Frame 1:** This frame is distinct. It shows a large anechoic space. This is classic for a pleural effusion. The space is bounded superiorly by the chest wall/pleura and laterally by ribs (shadows). The "Quad sign" is suggested. The lung is compressed below.
*   **Frames 2-8:** These frames show the lung parenchyma. It looks relatively solid or "hepatized" in some areas, but mostly it looks like normal lung with A-lines or just standard lung texture, but there are vertical artifacts. Wait, let's look at the "Quad sign" again in Frame 1.
    *   **Quad Sign:** In the first image, there is a large anechoic region. It is bounded by the chest wall (top), a rib shadow on the left, and likely another rib or the liver/spleen below? No, looking at the orientation, this is a posterior scan (PLAPS point). The probe is likely placed on the back.
    *   The first image clearly shows a large anechoic area. This is fluid. This is the "Quad sign" or part of it. The lung is compressed and appears as a solid mass below the fluid (atelectasis). This is the "Jellyfish sign" or just compressed lung.
    *   Let's look at the other frames. They show the lung tissue adjacent to this fluid or perhaps the fluid has moved out of view, or the probe moved.
    *   Actually, looking at the sequence, it seems the probe is scanning across the area.
    *   Frame 1: Large anechoic space. This is effusion.
    *   Frames 2-8: These frames show the lung tissue below/adjacent to the effusion. The tissue looks somewhat solid/hepatized, which is common with compressive atelectasis in the presence of effusion. However, looking closely at frames 2-8, I see vertical reverberation artifacts (A-lines) and B-lines? No, they look more like normal lung markings or perhaps some consolidation.
    *   Let's look for specific signs requested:
        *   **Quad sign:** Frame 1 shows a large anechoic space bounded by structures. It looks like the quad sign.
        *   **Jellyfish sign:** In Frame 1, the lung tissue at the bottom of the anechoic space looks like it's floating or compressed. This fits the description of atelectatic lung in effusion.
        *   **Consolidation:** In frames 5-8, the tissue looks somewhat echogenic, but it's hard to distinguish "hepatization" perfectly without seeing the liver. However, the presence of the effusion (Frame 1) strongly suggests a PLAPS pattern.
    *   The prompt asks to assess for *presence* of PLAPS.
    *   Frame 1 is the key. It shows a significant anechoic collection. This is pleural effusion.
    *   The other frames show the lung tissue. In a PLAPS point scan with effusion, the lung is often atelectatic (consolidated).
    *   Let's look at the "type". Since there is a clear fluid collection (anechoic area) in the first frame, it's definitely "effusion".
    *   Is there consolidation? The lung tissue below the fluid in Frame 1 and the tissue in subsequent frames looks relatively solid. In Frame 1, the tissue below the fluid is hypoechoic/homogenous. This suggests compressive atelectasis (consolidation). So "both" is a strong possibility. Or maybe just effusion with secondary atelectasis.
    *   Let's re-read the definitions.
        *   **Effusion signs:** Quad sign (yes, Frame 1), Jellyfish sign (yes, Frame 1 - the lung floating in fluid).
        *   **Consolidation signs:** Tissue-like hepatization (maybe, the lung looks solid), Shred sign (hard to see clearly), Air bronchograms (hard to see clearly).
    *   The first frame is the most diagnostic. It shows a large anechoic space. This is the Quad Sign.
    *   The lung tissue below it is compressed. This is the Jellyfish sign (if it moves) or just atelectasis.
    *   So, `plaps = true`.
    *   What is the type? The primary feature in the most distinct frame (Frame 1) is the fluid. So `type = "effusion"`. Wait, looking at the other frames, they seem to show the lung parenchyma *without* the large fluid pocket, or perhaps a different angle. But Frame 1 is definitive for effusion.
    *   Let's look at the other frames again. They show a vertical dark shadow (rib) and lung tissue to the right. The lung tissue has some hyperechoic lines. It looks like normal lung or perhaps mild consolidation. But Frame 1 is the "smoking gun" for PLAPS.
    *   Actually, looking closely at Frame 1, it's a large black area. This is fluid.
    *   Looking at Frames 2-8, they seem to show the lung tissue adjacent to the fluid or perhaps the fluid is in the far field? No, the probe is likely static or moving slowly.
    *   Let's assume the sequence captures the PLAPS point.
    *   Frame 1: Large anechoic area. This is a pleural effusion. The lung is compressed.
    *   Frames 2-8: These look like they might be showing the lung tissue *after* the fluid or just a different part of the scan. Wait, looking at the timestamps or sequence, it's a video.
    *   Actually, looking at all frames, they look very similar, just slight variations in angle/brightness.
    *   Let's look at Frame 5, 6, 7. There is a vertical interface. To the left is liver/spleen? To the right is lung? No, in a posterior scan, the liver is usually not seen unless there's massive effusion.
    *   Let's reconsider the "Quad sign". The quad sign is: Superior = Pleural line. Inferior = Lung line. Lateral = Rib shadows. The space between is anechoic (fluid).
    *   In Frame 1, we see a large black area. The top boundary is the chest wall. The side boundary is a rib shadow (hyperechoic line with shadow). The bottom boundary is the lung (which is compressed). This fits the Quad Sign perfectly.
    *   Therefore, there is an effusion.
    *   The lung tissue below the fluid is likely atelectatic (consolidated). This is a common pairing.
    *   So, `plaps = true`.
    *   Type: Since there is a clear fluid collection, `type = "effusion"`. The presence of atelectasis is a secondary sign often associated with effusion in this context, but the primary sign identified in the prompt for "effusion" type is the fluid itself. However, the prompt allows for `type = "both"`.
    *   Let's look for consolidation signs specifically.
        *   "Tissue-like hepatization": In Frame 1, the area below the fluid is dark but distinct from the fluid. It looks like compressed lung.
        *   "Air bronchograms": I don't clearly see punctate hyperechoic foci in the consolidated area.
    *   However, the effusion is the dominant feature in Frame 1.
    *   Let's look at the other frames (2-8). They seem to show the lung parenchyma *without* the large fluid pocket, or perhaps the fluid is not in that specific slice. Wait, looking at the sequence, Frame 1 is very different. Frames 2-8 look like standard lung ultrasound with A-lines or B-lines? No, they look like the lung tissue is solid.
    *   Actually, let's look at the transition. Frame 1 shows the fluid. Frames 2-8 show the lung tissue *below* the fluid? Or is Frame 1 an outlier?
    *   Let's assume the whole sequence represents the PLAPS point.
    *   In Frame 1, we see the effusion.
    *   In the subsequent frames, we see the lung tissue. It looks relatively echogenic, possibly "hepatized".
    *   Let's look at the "Shred sign". This is the irregular border between consolidated and aerated lung.
    *   In Frames 5-8, there is a vertical interface. To the left is a more uniform texture. To the right is... darker?
    *   Actually, let's look at the "Jellyfish sign". This is floating lung in fluid. In Frame 1, the lung tissue at the bottom of the black area looks like a flap. This fits the Jellyfish sign.
    *   So, definitely Effusion.
    *   Is there consolidation? The lung floating in the fluid is technically "consolidated" (atelectatic). But usually, "consolidation" type refers to pneumonia. "Effusion" type refers to free fluid. The prompt says "type = 'both': Both effusion and consolidation are visible."
    *   In the context of PLAPS, it's very common to have both.
    *   Let's look at Frame 1 again. The black area is huge. The tissue below it is the lung.
    *   In Frames 2-8, the probe seems to have moved or the fluid is gone? No, looking closely at Frame 2, there is a vertical dark shadow. This is likely a rib. The tissue to the right of it has some vertical lines. This looks like B-lines or just normal lung.
    *   Wait, let's look at the first frame again. It's extremely dark. Is it possible that Frame 1 is just a bad image or a different view? No, it looks like a classic effusion view.
    *   Let's look at the other frames. They show the "Quad sign" borders but the space is filled with tissue? No, in Frame 1 the space is black (fluid). In Frame 2, the space is... actually, it looks like the probe is scanning *through* the fluid or adjacent to it.
    *   Let's look at the "Quad sign" definition again: "Anechoic (black) space bounded by pleural line superiorly, lung line inferiorly, and rib shadows laterally".
    *   In Frame 1, I see a large black area. Superiorly is the skin/chest wall. Laterally is a rib shadow. Inferiorly is the lung. This is the Quad sign.
    *   So, Effusion is present.
    *   Now, is there consolidation? The lung tissue seen in Frame 1 (below the fluid) is likely atelectatic. Atelectasis is a form of consolidation.
    *   Also, in the later frames, the lung tissue visible (if it's the same area) looks somewhat solid.
    *   However, the most prominent feature is the fluid.
    *   Let's classify as `type = "effusion"`. Why? Because the fluid is the most distinct "PLAPS sign" here (Quad sign). The consolidation is likely secondary (compressive atelectasis). But the prompt allows for "both".
    *   Let's look for "Air bronchograms". In Frame 1, inside the hypoechoic tissue below the fluid, are there bright spots? It's hard to tell, but there are some echogenic foci.
    *   Let's look at the "Shred sign". The interface between the fluid and the lung is the "deep border". It looks somewhat irregular.
    *   Let's look at the provided solution in similar tasks. Usually, if there's a big effusion, it's "effusion". If there's a big consolidation, it's "consolidation". If both are prominent, "both".
    *   In Frame 1, the effusion is very large. The lung is compressed.
    *   In Frames 2-8, the view changes. It looks like we are looking at the lung parenchyma *outside* the main fluid pocket, or perhaps the fluid is posterior and the lung is anterior? No, PLAPS is posterior.
    *   Actually, looking at the sequence, it seems the probe is moving.
    *   Frame 1: Big fluid.
    *   Frame 2: Maybe the fluid is gone? Or maybe I'm misinterpreting Frame 1.
    *   Let's look at Frame 1 again. Is it possible that the black area is *not* fluid but a large consolidation with air bronchograms? No, it's too uniformly black (anechoic). That's fluid.
    *   Is it possible that Frame 1 is the "Quad sign"? Yes.
    *   So, Effusion is present.
    *   What about the other frames? They show lung tissue. Is it consolidated? It looks somewhat homogeneous.
    *   Let's assume the question implies the whole video shows the pathology.
    *   The pathology is a PLAPS.
    *   The signs are primarily effusion (Quad sign in Frame 1).
    *   Therefore, `plaps = true`.
    *   `type = "effusion"`.

    *   Wait, let's look closer at Frame 1. Is it possible that the black area is the lung and the tissue above is something else? No, standard ultrasound orientation: top is probe (superficial), bottom is deep.
    *   Top: Chest wall / Pleura.
    *   Middle: Anechoic space (Fluid).
    *   Bottom: Compressed lung (Atelectasis).
    *   This is classic.
    *   So, Effusion.
    *   Are there signs of consolidation *separate* from the atelectasis?
    *   In frames 2-8, we see tissue that looks like "hepatized" lung. It has a liver-like texture. This could be pneumonia consolidation.
    *   If both are present, the answer is "both".
    *   Let's look at Frame 5. There is a vertical line. To the left, tissue looks like liver. To the right, tissue looks like... lung?
    *   Actually, in PLAPS, the liver (or spleen) is often seen below the diaphragm if the effusion is large.
    *   In Frame 1, the bottom of the image shows a curved line. Below that is... dark?
    *   Let's reconsider the "Quad sign".
    *   Superior: Pleural line.
    *   Inferior: Lung line (or liver/spleen line if fluid is deep).
    *   Lateral: Ribs.
    *   In Frame 1, the black area is bounded by ribs laterally. The superior boundary is the chest wall. The inferior boundary is the compressed lung. This is the Quad Sign.
    *   So, Effusion is definitely present.
    *   Now, is there consolidation?
    *   The lung compressed by the effusion is atelectatic, which is technically a consolidation (solidification).
    *   However, usually "consolidation" in these reports refers to pneumonia.
    *   Let's look at the other frames. They show the lung tissue *adjacent* to the effusion? Or is the effusion small and the consolidation big?
    *   Actually, looking at the sequence, Frame 1 is the only one with the big black space. Frames 2-8 look like normal lung or maybe mild B-lines.
    *   Wait, let's look at Frame 2 again. There is a vertical dark shadow. To the right of it, there are some bright spots.
    *   Let's look at Frame 5. There is a distinct vertical interface. This looks like the diaphragm or a fissure? No, in PLAPS, we look for the fluid above the diaphragm.
    *   Let's assume the video shows the PLAPS point.
    *   The presence of the Quad sign in Frame 1 is sufficient for "plaps = true" and "type = effusion".
    *   Is there consolidation? The lung tissue *below* the fluid in Frame 1 is atelectatic. This is a form of consolidation.
    *   So "both" is a valid interpretation.
    *   However, usually, if the primary finding is fluid, it's classified as effusion. If the primary finding is solid lung, it's consolidation.
    *   In Frame 1, the fluid takes up a significant portion of the image.
    *   Let's look at the "Jellyfish sign". This is the lung floating in the fluid. In Frame 1, the tissue at the bottom of the fluid pocket looks like a flap. This is the Jellyfish sign. This confirms effusion.
    *   Does the video show pneumonia (consolidation with air bronchograms) *independent* of the effusion?
    *   In the later frames, the image quality is poorer, but I see some echogenic foci.
    *   Let's stick to the strongest evidence.
    *   Strongest evidence: Frame 1 shows a large anechoic space (Effusion).
    *   Secondary evidence: The lung tissue below it is compressed (Atelectasis/Consolidation).
    *   So, `plaps = true`.
    *   `type = "effusion"` or `type = "both"`.
    *   Let's look at the definitions again.
    *   `type = "effusion"`: Predominantly fluid collection signs.
    *   `type = "consolidation"`: Predominantly tissue-like/hepatized lung without significant free fluid.
    *   `type = "both"`: Both effusion and consolidation are visible.
    *   In Frame 1, we see *both*. We see the fluid (quad sign) and the compressed lung (which is a form of consolidation, and potentially the "jellyfish sign" implies the lung is distinct from the fluid).
    *   Also, in the later frames, if we see lung tissue that is not just compressed but consolidated (pneumonia), then it's "both".
    *   Actually, looking at Frame 5, 6, 7, the tissue looks quite homogeneous and echogenic, resembling liver. This is "hepatization". This suggests consolidation.
    *   And Frame 1 shows the effusion.
    *   So, "both" seems appropriate.
    *   However, often in PLAPS, the effusion is the key differentiator.
    *   Let's look at the visual evidence again.
    *   Frame 1: Large black area. This is fluid.
    *   Frames 2-8: These look like they are showing the lung *below* the fluid or adjacent to it. The texture is somewhat solid.
    *   Let's try to find "Air bronchograms". In Frame 1, inside the hypoechoic area (lung), there are some bright spots. These could be air bronchograms.
    *   So, we have Effusion (Fluid) and Consolidation (Hepatized lung with possible air bronchograms).
    *   Conclusion: `plaps = true`, `type = "both"`.

    *   Wait, let's look at the "Quad sign" again.
    *   The Quad sign is: Anechoic space.
    *   Superior: Pleural line.
    *   Inferior: Lung line.
    *   Lateral: Rib shadows.
    *   In Frame 1, I see the rib shadows. I see the anechoic space. I see the lung line at the bottom.
    *   This confirms Effusion.
    *   Is there consolidation?
    *   The lung tissue *in* the quad sign (the "lung line") is often consolidated/atelectatic.
    *   But is there *another* area of consolidation?
    *   In the later frames, the view is different. It looks like we are scanning the lung parenchyma. It looks somewhat solid.
    *   Let's assume the standard PLAPS presentation: Effusion + Atelectasis (which is a consolidation).
    *   So, "both" is the most accurate description if we count atelectasis as consolidation.
    *   However, if the prompt distinguishes between "effusion" (free fluid) and "consolidation" (pneumonia), and the tissue is just atelectatic, maybe it's just "effusion".
    *   Let's look at the "Jellyfish sign" description: "Floating, undulating atelectatic lung within a surrounding effusion". This combines both. The presence of the Jellyfish sign implies both effusion and the floating lung (which is consolidated/atelectatic).
    *   So if I see the Jellyfish sign, I see both.
    *   Do I see the Jellyfish sign?
    *   In Frame 1, the tissue at the bottom of the fluid looks like a distinct layer. It's not just a line. It has texture. This fits the description of "floating lung".
    *   So, Jellyfish sign is present.
    *   Therefore, both effusion and consolidation (atelectasis) are present.
    *   Type: "both".

    *   Let's double check.
    *   Is it possible that Frame 1 is just a big consolidation with artifact? No, it's too anechoic. It's fluid.
    *   Is it possible that the other frames are just normal lung?
    *   In Frame 5, the tissue on the left looks like liver. The tissue on the right looks like... lung?
    *   Actually, in PLAPS, you look for fluid above the diaphragm. The liver is below the diaphragm.
    *   In Frame 1, the bottom of the image shows a curved structure. This could be the diaphragm/liver interface.
    *   So, we have fluid (black) above the diaphragm.
    *   This confirms Effusion.
    *   The lung is floating in it.
    *   So, Effusion is the primary finding.
    *   Is there consolidation *of the lung* (pneumonia)?
    *   The floating lung is atelectatic. Is it also pneumonic? Hard to say definitively, but PLAPS is often associated with pneumonia.
    *   Let's look for "Shred sign".
    *   The border between the fluid and the floating lung is the deep border of the fluid.
    *   The border between the consolidated lung and aerated lung (if any) is the shred sign.
    *   In Frame 1, we don't see aerated lung. We see fluid and compressed lung.
    *   So, maybe it's just effusion with secondary atelectasis.
    *   In that case, `type = "effusion"`.
    *   But the prompt says "type = 'both': Both effusion and consolidation are visible."
    *   Atelectasis is a type of consolidation.
    *   So "both" is technically correct.
    *   However, usually "consolidation" in these reports implies the "tissue-like hepatization" of pneumonia.
    *   Let's look at the other frames again.
    *   Frames 2-8 show a vertical shadow. To the right, there is tissue.
    *   Is it possible that the video shows *both* areas?
    *   Area 1 (Frame 1): Effusion.
    *   Area 2 (Frames 2-8): Consolidation?
    *   In Frames 2-8, the tissue looks relatively homogeneous. It lacks the "A-line" pattern of normal aerated lung. It looks more like "B-lines" or solid tissue.
    *   If there is no fluid in Frames 2-8, but the tissue is solid, that's consolidation.
    *   So, the video shows an area with effusion (Frame 1) and an area with consolidation (Frames 2-8)?
    *   Or is Frame 1 showing the effusion *and* the consolidated lung below it? Yes.
    *   And Frames 2-8 are just different angles of the same pathology.
    *   In Frames 2-8, the fluid might be out of the main field of view, or it's the "Jellyfish" part moving.
    *   Actually, looking at Frame 2, the top part shows the chest wall. The middle shows... tissue. The bottom shows... tissue.
    *   It looks like the lung is "hepatized" (solid).
    *   So, we have solid lung (consolidation).
    *   And we have fluid (effusion) in Frame 1.
    *   So, "both" is the best answer.

    *   Let's refine the observation.
    *   Observation: The first frame clearly demonstrates the "Quad sign" — a large anechoic (black) space representing pleural effusion, bounded by the chest wall/pleura superiorly and rib shadows laterally. Below the fluid, there is hypoechoic tissue which represents atelectatic/consolidated lung. This appearance is consistent with the "Jellyfish sign" (floating lung in fluid).
    *   Subsequent frames show lung parenchyma that appears echogenic and solid (hepatization), consistent with consolidation.
    *   Conclusion: PLAPS is present. Both effusion and consolidation are visible.

    *   Wait, let's look at the "Quad sign" definition again.
    *   "Anechoic space bounded by pleural line superiorly, lung line inferiorly, and rib shadows laterally".
    *   In Frame 1, the "lung line" is the top of the compressed lung.
    *   So, Effusion is definitely there.
    *   Is the lung "consolidated"? Yes, compressed atelectatic lung is echogenic/hypoechoic and solid.
    *   So, `plaps = true`.
    *   `type = "both"`.

    *   Let's consider if it could just be "effusion".
    *   If the lung is just collapsed (atelectasis) due to the fluid, is that considered "consolidation" for the purpose of this classification?
    *   The prompt defines consolidation signs: "Tissue-like hepatization... with loss of normal aeration artifacts."
    *   Atelectatic lung fits this description (loss of aeration, tissue-like).
    *   So yes, it counts as consolidation signs.
    *   Therefore, since we see effusion (fluid) and consolidation (solid lung), the type is "both".

    *   Final check of the images.
    *   Image 1: Large black area (Effusion). Tissue below it (Consolidation/Atelectasis).
    *   Images 2-8: Show tissue that looks like the consolidated lung seen in Image 1, just from a slightly different angle or time. The vertical dark lines are likely rib shadows. The tissue is solid.
    *   So, both signs are present.

    *   One detail: "Quad sign" is specific for effusion.
    *   "Jellyfish sign" is specific for effusion + floating lung (consolidation).
    *   So seeing the Jellyfish sign confirms both.
    *   I see a large fluid collection and a distinct tissue mass within/adjacent to it.
    *   So, `type = "both"`.

    *   Wait, is it possible that the black area in Frame 1 is NOT fluid?
    *   Could it be a large pneumothorax? No, pneumothorax shows A-lines and sliding lung below the pleural line. This is anechoic. Fluid is anechoic.
    *   Could it be a large abscess? Unlikely in lung US unless specified.
    *   So, fluid is the best bet.

    *   Is it possible that the tissue in Frame 1 is NOT lung?
    *   In PLAPS, we are looking at the posterior lung.
    *   The structure below the fluid is the lung.
    *   So, yes, it's lung.

    *   Conclusion stands: PLAPS = true. Type = both.

    *   Let's write down the description.
    *   The first image shows a large anechoic region consistent with the Quad sign, indicating a pleural effusion.
    *   Within/below this fluid, there is hypoechoic tissue which appears to be atelectatic lung (Jellyfish sign).
    *   The subsequent images show lung parenchyma that appears solid and echogenic (hepatization), consistent with consolidation.
    *   Therefore, both effusion and consolidation are present.

    *   Wait, let me look really closely at Frame 1.
    *   The black area is very large.
    *   Is it possible that this is a "massive" effusion?
    *   Yes.
    *   And the lung is fully collapsed.
    *   So, Effusion is the dominant feature.
    *   But the collapsed lung is still visible.
    *   So "both" is correct.

    *   One alternative interpretation:
    *   Maybe the black area is just the "Quad sign" and the lung is not clearly "consolidated" in the sense of pneumonia, just collapsed.
    *   But the classification scheme separates "effusion" (fluid) and "consolidation" (tissue-like).
    *   Collapsed lung is tissue-like.
    *   So "both" remains the most accurate technical classification.

    *   Let's check if the prompt implies mutual exclusivity.
    *   "type = 'both': Both effusion and consolidation are visible."
    *   This implies they can coexist.
    *   In PLAPS, they often do.
    *   So I will go with "both".

    *   Let's re-read the "Consolidation signs".
    *   "Tissue-like hepatization": Lung parenchyma appears solid and echogenic.
    *   In Frame 1, the tissue below the fluid is not very echogenic. It's hypoechoic.
    *   Wait, fluid is anechoic (black). Consolidation is usually isoechoic or hyperechoic to liver (gray/white).
    *   In Frame 1, the tissue below the black fluid is... actually quite dark too.
    *   Maybe it's just very fluid-filled? No, that would be another effusion pocket.
    *   Maybe it's atelectasis which can be hypoechoic.
    *   In Frames 2-8, the tissue is more echogenic (gray/white).
    *   Frame 2: Gray tissue with white lines.
    *   Frame 5: Gray tissue.
    *   This looks like "hepatization".
    *   So, Frames 2-8 show consolidation.
    *   Frame 1 shows effusion.
    *   So the video shows both.
    *   Therefore, `type = "both"`.

    *   Final decision:
    *   plaps = true
    *   type = "both"

