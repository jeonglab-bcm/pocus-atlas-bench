# 0090_lung_skfn1nk408w1wvqph7pxsc5fr6pbs9 — Reasoning

The user wants me to analyze a series of ultrasound frames from a lung ultrasound (LUS) video.

1.  **Analyze the frames:**
    *   The frames show an anterior lung zone ultrasound.
    *   The pleural line is visible as a bright, horizontal line.
    *   Below the pleural line, there are bright, vertical artifacts that extend to the bottom of the screen.
    *   These vertical artifacts are numerous and appear to coalesce, creating a "white sheet" effect. This is characteristic of ground-glass B-lines.
    *   There is no evidence of solid, hepatized lung tissue or a shred sign. The entire visible lung field (below the pleura) is dominated by these confluent B-lines.
    *   Therefore, `lung_rockets` is `true`.
    *   Since the B-lines are confluent and create a bright sheet, the subtype is `ground_glass`.
    *   There's no sign of `consolidation`. So `consolidation` is `false` and `consolidation_type` is `null`.

2.  **Detailed breakdown per frame (though they all look identical/very similar):**
    *   All frames show the same pattern: a bright, horizontal pleural line and intense, confluent vertical hyperechoic artifacts extending to the bottom of the scan field. This represents a "ground-glass" pattern of B-lines. No consolidated, hepatized lung is seen.

3.  **Final conclusions:**
    *   `lung_rockets`: true
    *   `b_line_subtype`: "ground_glass"
    *   `consolidation`: false
    *   `consolidation_type`: null
