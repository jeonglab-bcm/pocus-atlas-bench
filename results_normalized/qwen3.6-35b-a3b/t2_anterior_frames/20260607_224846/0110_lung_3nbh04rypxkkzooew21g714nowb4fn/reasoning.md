# 0110_lung_3nbh04rypxkkzooew21g714nowb4fn — Reasoning

The user wants me to analyze a sequence of lung ultrasound images.

**1. Analyze the images frame by frame:**
- **Images:** There are 8 pairs of images (left and right panels in each frame). Wait, looking closely at the input, it's actually just a sequence of 8 single images, but each image contains two side-by-side panels. Let's look at the first image provided. It shows two side-by-side ultrasound wedges. The prompt says "sequential frames from a lung ultrasound (LUS) video clip". The provided input is a sequence of 8 images. Each image seems to be a single frame containing two views, or perhaps just two views side-by-side. Let's assume each of the 8 rows is a distinct "frame" or timepoint. Actually, looking at the URLs, there are 8 distinct image files. Let's look at them one by one.
    - **Image 1:** Two side-by-side panels. Both show a pleural line at the top. Below it, there are vertical hyperechoic artifacts. In the left panel, there are distinct vertical lines. In the right panel, there is a large area of hyperechogenicity with vertical streaks. It looks like a lot of B-lines.
    - **Image 2:** Similar view. The left panel shows some vertical artifacts but less dense than image 1. The right panel shows a dense, white area, suggesting confluent B-lines.
    - **Image 3:** Left panel: Dense white area. Right panel: Dense white area. Looks like "ground glass" or very dense B-lines.
    - **Image 4:** Left panel: Dense white area. Right panel: Dense white area.
    - **Image 5:** Left panel: Dense white area. Right panel: Dense white area.
    - **Image 6:** Left panel: Dense white area. Right panel: Darker area with some vertical artifacts.
    - **Image 7:** Left panel: Dense white area. Right panel: Darker area.
    - **Image 8:** Left panel: Dense white area. Right panel: Distinct vertical lines, less dense than the left panel.

Wait, let me re-evaluate the structure. The prompt provides 8 image links. Each link contains two side-by-side panels. Let's assume the left panel is one probe position or time, and the right is another, or perhaps just different regions. The prompt asks to analyze "sequential frames". It's likely that the images provided are just different frames of the video. Let's look at the sequence as a whole.

Actually, looking at the provided images again, it seems like each "image" in the list is a single screenshot containing two side-by-side views. Let's look at the first image. It has a left panel and a right panel.
- Left panel: Pleural line at top. Below it, there are vertical artifacts. They look like B-lines. They are somewhat discrete but start to merge.
- Right panel: Pleural line. Below it, a very dense, white area. This looks like confluent B-lines (ground glass appearance) or possibly consolidation. But the vertical streaks suggest B-lines. The "shred sign" is not clearly visible as a border. It looks more like a large field of B-lines.

Let's look at the sequence of images provided.
- Image 1: Left panel shows distinct vertical lines (B-lines). Right panel shows a large area of hyperechogenicity, likely confluent B-lines.
- Image 2: Left panel shows fewer B-lines. Right panel shows a dense white area.
- Image 3: Left panel: Dense white. Right panel: Dense white.
- Image 4: Left panel: Dense white. Right panel: Dense white.
- Image 5: Left panel: Dense white. Right panel: Dense white.
- Image 6: Left panel: Dense white. Right panel: Darker, maybe normal lung with some B-lines? Or maybe just less dense.
- Image 7: Left panel: Dense white. Right panel: Darker.
- Image 8: Left panel: Dense white. Right panel: Distinct vertical lines (B-lines).

Wait, the prompt says "Analyze frame by frame first". This implies I should treat the sequence of images as a video.
Let's look at the "B-lines Assessment" criteria.
- **B-lines present**: Hyperechoic vertical artifacts arising from the pleural line, extending to the bottom, moving with lung sliding.
- **Absent**: No vertical artifacts.

Let's look at the images again.
In almost all frames, especially the left panels and the right panel of the first frame, there are prominent vertical hyperechoic artifacts.
- Frame 1 (Image 1): Left panel shows distinct B-lines. Right panel shows a very bright, white area which looks like "ground glass" B-lines (coalesced).
- Frame 2 (Image 2): Left panel shows some B-lines. Right panel shows a large area of hyperechogenicity.
- Frame 3 (Image 3): Both panels show diffuse hyperechogenicity, suggesting dense B-lines.
- Frame 4 (Image 4): Similar to 3.
- Frame 5 (Image 5): Similar to 3.
- Frame 6 (Image 6): Left panel dense. Right panel darker, maybe just A-lines and some artifacts? No, still looks like some vertical streaks.
- Frame 7 (Image 7): Left panel dense. Right panel darker.
- Frame 8 (Image 8): Left panel dense. Right panel shows distinct vertical lines.

The overall impression is a "white lung" or "lung point" pattern but with dense B-lines.
Let's look for consolidation.
- **Tissue-like hepatization**: Does the lung look like a solid organ? In some frames (e.g., Image 3 left), it looks very solid white. But is it hepatization or just dense B-lines? Dense B-lines (ground glass) can look like a white sheet. Hepatization usually has a more tissue-like texture, maybe with air bronchograms.
- **Air bronchograms**: I need to look for bright spots/lines inside the solid area.
    - In Image 6 (right panel), there's a darker area, maybe aerated lung next to consolidation? No, it looks like just different B-line density.
    - In Image 8 (right panel), there are distinct vertical lines.
    - In Image 6 (left panel), it's very white.
    - In Image 3 (left panel), it's very white.

Let's reconsider the "ground_glass" classification for B-lines.
- "ground_glass": Confluent or coalescing B-lines that merge into a diffuse white sheet obscuring A-lines.
- This matches what I see in many frames, especially the left panels and right panel of frame 1. The lung field is basically a vertical white sheet.

Let's reconsider "septal".
- "septal": Discrete, well-spaced B-lines.
- I see this in Image 1 left, Image 8 right. But the dominant feature seems to be the dense, white areas.

Let's look for "mixed".
- "mixed": Both septal and ground_glass patterns are visible.
- In the sequence, I see frames with distinct B-lines (septal-like) and frames with dense white sheets (ground_glass-like). For example, Image 1 Left has distinct lines. Image 1 Right has a white sheet. Image 8 Right has distinct lines. Image 8 Left has a white sheet. This suggests a "mixed" pattern or a transition. The prompt asks for a single assessment. Usually, if I see both, I classify as mixed.

Now for consolidation.
- Is there hepatization? The "white lung" of dense B-lines can mimic hepatization. However, hepatization is a solid tissue texture. B-lines are vertical artifacts.
- In Image 6 (right) and Image 7 (right), there is a darker area. Is that consolidation? No, darker usually means aerated lung (A-lines) or just less artifact. Wait, in lung ultrasound, dark usually means aerated lung (black with horizontal A-lines). White usually means fluid/B-lines.
- Let's look at Image 6 Right. It's darker than the left. It looks like it has horizontal lines (A-lines). This suggests that part of the scan is showing aerated lung.
- Let's look at Image 8 Right. It shows vertical lines.
- Let's look at Image 1 Left. Vertical lines.
- Let's look at Image 1 Right. A large white area. This looks like "white lung" caused by massive B-lines (alveolar-interstitial syndrome).
- Is there a solid area? In Image 3 Left, the entire field is white. Is this hepatization? Or just super-dense B-lines?
- Usually, "white lung" = severe B-lines. Hepatization = solid tissue.
- Let's look for air bronchograms. I don't see clear punctate hyperechoic foci inside a solid mass.
- Let's look for "shred sign". An irregular border between solid and aerated.
- In Image 6, the right panel looks aerated (darker, maybe horizontal lines) and the left panel looks white (dense B-lines or consolidation). The border between them isn't super sharp in the side-by-side, but within the panels...
- Actually, looking closely at Image 6 Right, it looks like it has some vertical artifacts but is darker.
- Looking at Image 8 Right, distinct B-lines.

Let's re-read the definitions.
- **B-lines**: Vertical artifacts.
- **Ground glass**: Coalescing B-lines.
- **Consolidation**: Tissue-like hepatization.

Let's look at the "ground_glass" vs "hepatization".
- Ground glass B-lines: "merge into a diffuse white sheet obscuring A-lines". This fits the images perfectly. The lung field is a white vertical sheet.
- Hepatization: "lung parenchyma appears solid and echogenic, resembling liver texture". Liver texture is a specific speckled grey. The images show a very bright, streaky white. This is characteristic of dense B-lines (white lung).
- However, sometimes severe B-lines are hard to distinguish from hepatization. But the definition of ground glass fits the "white sheet" description well.
- Wait, is it possible that the white areas *are* consolidation?
- Let's look for air bronchograms. In Image 6 Right, is that a solid area? No, it looks like it has horizontal striations (A-lines).
- In Image 3 Left, it's very white. Could be consolidation.
- But let's look at the overall pattern. The vertical streaks are prominent.
- Let's assume the primary finding is B-lines.
- Are they septal or ground glass?
    - Frame 1 Left: Discrete lines. (Septal)
    - Frame 1 Right: White sheet. (Ground glass)
    - Frame 3 Left: White sheet. (Ground glass)
    - Frame 8 Right: Discrete lines. (Septal)
- This variation suggests a **mixed** pattern. I see both distinct lines and confluent white areas.

Now, consolidation.
- If the white sheet is just dense B-lines, then consolidation is false.
- If the white sheet is hepatization, then consolidation is true.
- How to distinguish?
    - B-lines move with lung sliding. The prompt implies this is a video clip ("sequential frames"). I can't see movement, but I can infer.
    - Hepatization does not move with sliding (or moves differently).
    - Air bronchograms are key.
    - In the images, I don't see clear air bronchograms (punctate hyperechoic spots).
    - The texture is very "streaky" vertically. This is characteristic of B-lines.
    - However, look at Image 3, 4, 5. The left panels are very uniform white. This could be "white lung" (severe edema).
    - Look at Image 6 Right. It looks like normal lung with A-lines (horizontal lines).
    - Look at Image 8 Right. Distinct B-lines.
    - So we have areas of normal lung (A-lines) and areas of pathology.
    - The pathology is characterized by vertical artifacts. This points strongly to B-lines.
    - The "white sheet" appearance is classic for severe B-lines (interstitial syndrome).
    - Therefore, consolidation is likely **false**. The "solid" look is due to the density of the artifacts, not solid tissue.
    - Wait, let's look at Image 6 Right again. It looks darker. Is it possible that's the aerated lung? Yes.
    - Is there a shred sign? Between the dark (aerated) and white (B-lines) areas?
    - In Image 6, the right panel is darker. The left is white. But they are side by side. They might be different intercostal spaces.
    - In Image 8 Right, there is a clear separation? No, it's just a field of B-lines.

Let's refine the B-line classification.
- I see distinct vertical lines in several frames (e.g., Image 1 Left, Image 8 Right).
- I see confluent white areas in others (e.g., Image 1 Right, Image 3 Left).
- This fits **mixed**.

Let's refine the Consolidation classification.
- The prompt asks to assess for consolidation signs: hepatization, shred sign, air bronchograms.
- The white areas look like "white lung" (ground glass B-lines).
- Is there hepatization?
    - In Image 3 Left, the texture is very uniform white. Could be hepatization.
    - But in Image 1 Right, there are vertical streaks. This is B-line territory.
    - In Image 6 Right, it looks like it might be aerated lung (darker).
    - If I assume the white areas are B-lines, then consolidation is false.
    - If I assume the white areas are hepatization, then consolidation is true.
    - Let's look for air bronchograms again. I don't see them.
    - Let's look for "shred sign". An irregular border.
    - In Image 6 Right, there is a vertical dark band in the middle-right. Is that a border? It looks like a shadow or just less signal.
    - In Image 8 Right, there are two distinct bright vertical lines (ribs?) and artifacts between them.
    - Let's look at the pleural line. It's visible at the top.
    - The vertical artifacts arise from the pleural line. This is the definition of B-lines.
    - Therefore, the findings are B-lines.
    - The "white sheet" is ground glass B-lines.
    - So, **B-lines = true**.
    - Subtype: I see both distinct lines and coalesced lines. So **mixed**. Or maybe predominantly **ground_glass** because the white areas are quite dominant in the middle frames.
    - Let's look at the sequence again.
        - Frame 1: Left (septal-ish), Right (ground glass).
        - Frame 2: Left (sparse), Right (ground glass).
        - Frame 3: Left (ground glass), Right (ground glass).
        - Frame 4: Left (ground glass), Right (ground glass).
        - Frame 5: Left (ground glass), Right (ground glass).
        - Frame 6: Left (ground glass), Right (sparse/normal?).
        - Frame 7: Left (ground glass), Right (sparse/normal?).
        - Frame 8: Left (ground glass), Right (septal).
    - The dominant feature across the majority of frames (especially 3, 4, 5) is the dense white sheet. This is **ground_glass**.
    - However, the prompt allows for "mixed". If distinct B-lines are visible in *any* frame, and ground glass in others, it's mixed.
    - Frame 1 Left has distinct lines. Frame 8 Right has distinct lines.
    - So **mixed** is a good candidate.
    - But let's look closer at Frame 1 Left. Are they distinct? Yes, there is dark space between them.
    - Let's look at Frame 8 Right. Yes, distinct lines.
    - Let's look at Frame 3 Left. It's a solid white. Ground glass.
    - So **mixed** seems appropriate.

- Now, consolidation.
- If the white areas are ground glass B-lines, then consolidation is false.
- Is it possible that the white areas are hepatization?
    - Hepatization looks like liver. Liver is homogeneous grey.
    - Ground glass B-lines are a white sheet with vertical striations.
    - In the images, I can see vertical striations even in the "white" areas (e.g., Frame 3 Left). This suggests B-lines.
    - So consolidation is likely **false**.

- Wait, let's look at Image 6 Right. It looks like it has a "shred sign". The top part is white, the bottom part is darker with horizontal lines. The border is irregular.
    - Let's re-examine Image 6 Right.
    - Top: Pleural line.
    - Middle: Some vertical artifacts.
    - Bottom: Horizontal lines (A-lines).
    - The transition is somewhat irregular. This could be a shred sign.
    - If there is a shred sign, then **consolidation = true**.
    - What type? "shred_sign".
    - But looking at the rest of the frames, the "white" area dominates.
    - Let's look at Image 6 Right again. Is that a shred sign or just the edge of the ultrasound beam/artifact?
    - Actually, looking at Image 6 Right, the right half is dark with horizontal striations. The left half has some vertical streaks. The border is vertical. This might just be different lung zones (aerated vs B-lines).
    - Let's look at Image 8 Right. It shows distinct B-lines.
    - Let's look at Image 1 Right. It shows a huge white area.
    - Let's look at Image 3 Left. Huge white area.

    Let's reconsider the "ground_glass" vs "hepatization" distinction.
    - In severe pulmonary edema, you get "white lung". This is confluent B-lines.
    - In pneumonia/consolidation, you get hepatization.
    - The prompt mentions "anterior lung zone".
    - The images show artifacts arising from the pleural line.
    - If I see distinct B-lines in some frames (Frame 1 Left, Frame 8 Right), that confirms B-lines are present.
    - If I see a white sheet in others (Frame 3 Left), that is likely ground glass B-lines.
    - So B-lines = true, subtype = mixed (or ground_glass if the white areas are just extreme density of the same B-lines). The definition of mixed says "Both septal... and ground_glass... are visible in different regions or at different time points". Since I see distinct lines in Frame 1 Left and Frame 8 Right, and white sheets in Frame 3, "mixed" is technically correct.
    - However, often "ground glass" is used for the severe end of the spectrum.
    - Let's look at the "consolidation" part again.
    - Is there a shred sign? In Image 6 Right, there is a dark area with horizontal lines (aerated lung) next to an area with vertical lines. The border is somewhat irregular. But is it a *consolidation* border?
    - A shred sign is the border between consolidated (hepatized) lung and aerated lung.
    - If the "white" area is just B-lines, then the "aerated" area next to it is normal lung. The border is a "lung point" or just a transition zone.
    - If the "white" area is hepatization, then it's consolidation.
    - How to tell?
    - Look for air bronchograms. I don't see them.
    - Look at the texture. It looks very "streaky" vertical. This is B-line texture. Hepatization is more "tissue-like" (speckled grey).
    - The images are very bright white in the middle frames. This is classic for "white lung" in B-mode ultrasound, caused by massive B-lines.
    - So I lean towards **B-lines = true**, **ground_glass** (or mixed).
    - And **consolidation = false**.

    Let's check the "mixed" definition again. "Both septal (discrete, spaced) and ground_glass (confluent, coalescing) patterns are visible in different regions or at different time points in the clip."
    - I see discrete lines in Frame 1 Left.
    - I see confluent white in Frame 3 Left.
    - So **mixed** is the most accurate classification for B-lines.

    Now, is there any consolidation?
    - Look at Image 6 Right again. The right side is dark. The left side has vertical lines.
    - Look at Image 8 Right. It has vertical lines.
    - Look at Image 1 Left. Vertical lines.
    - I don't see a solid, liver-like texture. I see vertical streaks.
    - So **consolidation = false**.

    Wait, let's look at the provided solution options or standard interpretations.
    - "Ground glass" B-lines are often described as a "white lung".
    - "Hepatization" is consolidation.
    - The images show "white lung".
    - Therefore, B-lines = true, subtype = ground_glass (or mixed).
    - Consolidation = false.

    Let's look really closely at Image 6 Right.
    - It shows a vertical dark band on the right side. Inside the dark area, there are horizontal lines (A-lines). This is normal lung.
    - To the left of the dark band, there are vertical artifacts.
    - The border between the dark area and the vertical artifacts area is somewhat irregular.
    - Is it possible that the vertical artifacts area is *not* B-lines but consolidation with air bronchograms?
    - Air bronchograms appear as hyperechoic (white) dots/lines *within* the hypoechoic (grey) hepatized tissue.
    - Here, the tissue is white (hyperechoic). The artifacts are white. This is B-line territory.
    - In hepatization, the tissue is grey (tissue echogenicity), and air bronchograms are bright white spots.
    - In these images, the "tissue" is very bright white, which is more consistent with artifact (B-lines) than tissue.
    - Also, the vertical orientation is key. B-lines are vertical.
    - So, I am confident these are B-lines.

    Final check on B-line subtype.
    - Frame 1 Left: Discrete lines. (Septal)
    - Frame 3 Left: Confluent white. (Ground glass)
    - So **mixed**.

    Final check on Consolidation.
    - No hepatization, no shred sign (the irregular border is likely between aerated lung and B-line lung, not consolidated lung), no air bronchograms.
    - So **consolidation = false**.

    Wait, let me look at Image 6 Right again. Is it possible that the dark area is the consolidation? No, consolidation is echogenic (bright). Aerated lung is dark.
    - So the dark area is aerated lung.
    - The bright area next to it is pathology.
    - If the pathology is B-lines (which I think it is), then it's not consolidation.

    Let's look at Image 8 Right.
    - Pleural line.
    - Two bright vertical lines (ribs?).
    - Between them, vertical artifacts.
    - This is definitely B-lines.

    Let's look at Image 1 Right.
    - Pleural line.
    - Huge area of white.
    - Vertical streaks visible if you look closely.
    - This is severe B-lines (white lung).

    So, conclusion:
    - B-lines: True.
    - Subtype: Mixed (seeing both distinct and coalesced). Or maybe predominantly Ground Glass because the "white lung" is very prominent. But "mixed" fits the definition of seeing both in the clip.
    - Consolidation: False.

    Let's re-read the prompt's specific definitions.
    - **mixed**: "Both septal ... and ground_glass ... are visible in different regions or at different time points in the clip."
    - I see distinct lines in Frame 1 Left and Frame 8 Right.
    - I see confluent white in Frame 3 Left.
    - So "mixed" is correct.

    - **consolidation_type**: If consolidation is false, it's null.

    One distinct possibility: Could the "white lung" be hepatization?
    - If it were hepatization, I would expect a tissue-like texture (grey, speckled).
    - These images are very bright white.
    - Also, hepatization usually obscures the pleural line or shows it irregularly. Here, the pleural line is visible at the top, and artifacts arise *from* it.
    - B-lines arise from the pleural line.
    - Hepatization is *below* the pleural line.
    - In the images, the brightness seems to originate from the pleural line and go down. This confirms B-lines.

    So, B-lines = True.
    Subtype = Mixed (or Ground Glass). Given the definition "mixed" explicitly covers seeing both in different time points, and I see distinct lines in some frames, "mixed" is the most precise. However, often "ground glass" is used for the severe end. Let's look at the frames again.
    - Frame 1 Left: Distinct lines.
    - Frame 2 Left: Distinct lines.
    - Frame 8 Right: Distinct lines.
    - Frame 1 Right: Confluent.
    - Frame 3 Left: Confluent.
    - So yes, Mixed.

    Wait, is it possible that the "distinct lines" are just early ground glass?
    - "septal": "Discrete, well-spaced B-lines... Typically ≤3 B-lines per intercostal space".
    - In Frame 1 Left, there are maybe 2-3 distinct lines. This fits "septal".
    - In Frame 3 Left, it's a white sheet. This fits "ground_glass".
    - So "mixed" is definitely the right choice.

    Now, about consolidation.
    - Is there any chance the "white sheet" is actually consolidation with air bronchograms that are just very dense?
    - Air bronchograms are *inside* the consolidation.
    - If the whole field is white, maybe it's dense consolidation?
    - But the artifacts are vertical. Consolidation doesn't create vertical artifacts unless there are air bronchograms, but those are punctate/linear, not long vertical streaks to the bottom.
    - Long vertical streaks to the bottom are B-lines.
    - So it's B-lines.

    Final Conclusion:
    - B-lines: Present.
    - Subtype: Mixed (septal and ground_glass).
    - Consolidation: Absent.

    Let me double check the "ground_glass" definition for B-lines.
    - "Confluent or coalescing B-lines that merge into a diffuse white sheet obscuring A-lines."
    - This matches the images perfectly.
    - "indicating alveolar edema or diffuse interstitial disease."

    Let me double check the "mixed" definition.
    - "Both septal ... and ground_glass ... are visible in different regions or at different time points in the clip."
    - Yes, Frame 1 Left (septal) vs Frame 3 Left (ground_glass).

    So, B-lines = true, subtype = mixed.
    Consolidation = false.

    Wait, looking at the images again, specifically Image 6 Right and Image 7 Right.
    - In Image 6 Right, the right side is dark.
    - In Image 7 Right, the right side is dark.
    - In Image 8 Right, the right side has distinct lines.
    - In Image 6 Left, it's white.
    - This confirms the mix of patterns.

    One final check: Could the dark area in Image 6 Right be a "shred sign"?
    - If the white area (left of dark) was consolidation, and the dark area was aerated lung, the border would be the shred sign.
    - But the white area looks like B-lines (vertical artifacts).
    - So the border is between B-line lung and aerated lung. This is not a shred sign of consolidation. It's a transition from interstitial syndrome to normal lung.
    - So consolidation remains false.

    The prompt asks to "Describe what you observe for both B-lines and consolidation, then state your conclusions."

    Observation:
    - The images show an anterior lung zone.
    - The pleural line is visible at the top.
    - There are vertical hyperechoic artifacts arising from the pleural line extending to the bottom of the screen. This indicates B-lines.
    - In some frames (e.g., left panel of frame 1, right panel of frame 8), the B-lines are discrete and well-spaced (septal).
    - In other frames (e.g., right panel of frame 1, left panel of frame 3), the B-lines are confluent, forming a dense white sheet (ground glass).
    - The presence of both patterns suggests a mixed picture.
    - The "white lung" appearance is due to the density of the B-lines.
    - There is no evidence of tissue-like hepatization (solid grey texture).
    - There is no evidence of air bronchograms (punctate hyperechoic foci).
    - There is no clear shred sign (irregular border between solid and aerated lung). The transition seen in some frames (e.g., frame 6 right) is likely between areas of different B-line density or aerated lung, but the "white" part is clearly B-lines, not solid consolidation.

    Conclusion:
    - B-lines: true
    - Subtype: mixed (or ground_glass? No, mixed is more accurate given the frames). Let's look at the dominant pattern. The "white lung" is very prominent. But the definition of mixed fits perfectly. I will go with mixed.
    - Consolidation: false
    - Consolidation type: null

    Wait, let me look at the "ground_glass" B-line definition again.
    - "Confluent or coalescing B-lines that merge into a diffuse white sheet obscuring A-lines."
    - This describes the "white lung".
    - If the clip shows *only* ground glass, then subtype is ground_glass.
    - If it shows *both*, it's mixed.
    - Frame 1 Left: I see distinct lines. Are they B-lines? Yes, vertical, from pleural line. Are they distinct? Yes, there is dark space.
    - So yes, mixed.

    One detail: In Frame 6 Right, the area is darker. Does it have A-lines?
    - It looks like it has horizontal reverberation artifacts. Yes, A-lines.
    - This confirms that part of the lung is aerated.
    - The part with B-lines is pathological.
    - The transition is from B-lines to aerated lung.

    So, final plan:
    - B-lines: True.
    - Subtype: Mixed.
    - Consolidation: False.

