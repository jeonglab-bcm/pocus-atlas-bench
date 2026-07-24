# 0029_lung_parapneumonic-effusion — Reasoning

The user wants me to analyze a series of lung ultrasound (LUS) images.

1.  **Identify the type of image:** The prompt says "lung ultrasound (LUS) video clip", but the image clearly shows a "CARDIAC M" and "S4-2" probe, which is a phased array probe for echocardiography. The labels "RT" (right), "MI", "TIS" are standard for echocardiography. The image shows a heart chamber (likely a four-chamber view, though it's a bit rotated or unconventional). It's definitely NOT a lung ultrasound.
2.  **Evaluate the prompt's instructions:** The prompt asks me to look for "plaps" (pleural effusion/alveolar consolidation) signs in a "posterior lung zone".
3.  **Compare image content to prompt instructions:**
    *   The image is an echocardiogram, not a lung ultrasound.
    *   There are no lung zones, pleural lines, lung lines, quad signs, sinusoid signs, jellyfishes, hepatization, shred signs, or air bronchograms.
    *   Instead, I see heart chambers, valves, and a pericardial space.
4.  **Conclusion:** The image provided does not match the description in the prompt. It's not an LUS. Therefore, `plaps` is false and `type` is null.
5.  **Final check:**
    *   Image: Echocardiogram (Cardiac M, S4-2 probe).
    *   Prompt's request: Lung ultrasound analysis.
    *   Mismatch.
    *   `plaps = false`
    *   `type = null`
