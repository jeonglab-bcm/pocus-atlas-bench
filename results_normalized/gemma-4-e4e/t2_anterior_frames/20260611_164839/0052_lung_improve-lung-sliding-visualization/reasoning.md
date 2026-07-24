# 0052_lung_improve-lung-sliding-visualization — Reasoning

The user wants me to analyze a sequence of 15 lung ultrasound frames (LUS) from an anterior lung zone.
I need to perform two main analyses for each frame:
1.  **B-lines Assessment**: Identify if B-lines are present and, if so, classify the pattern (septal, ground_glass, or mixed).
2.  **Consolidation Assessment**: Identify if there are signs of consolidation (hepatization, shred sign, air bronchogram). If present, classify the type.

I will analyze the frames sequentially and then provide a summary of the findings for each frame.

**Frame-by-frame Analysis Plan:**
For each frame (1-15):
- Look at the area below the pleura (A-lines/B-lines).
- Check for vertical, hyperechoic artifacts (B-lines).
- Check if they are discrete (septal) or merged/diffuse (ground_glass).
- Look for signs of consolidation (liver-like echogenicity, shredding, air bronchograms) in the lung fields.

**Execution.**

(Starting with Frame 1)
