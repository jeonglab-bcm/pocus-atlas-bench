# 0049_lung_pleural-shred-sign

Based on the sequential frames of the lung ultrasound (LUS) from the anterior lung zone:

**B-lines Assessment:**
- **Observation:** There is a prominent, broad, hyperechoic vertical artifact arising from the pleural line and extending to the bottom of the screen. These B-lines are coalescing and confluent, creating a "white sheet" appearance that obscures normal A-lines and lung parenchyma.
- **Conclusion:** B-lines are present (**lung_rockets = true**). The pattern is confluent and coalescing, which is characteristic of **ground_glass** B-lines.

**Consolidation Assessment:**
- **Observation:** The vertical hyperechoic regions are artifacts (B-lines), not solid tissue. There is no evidence of tissue-like hepatization, an irregular "shred sign" border, or internal air bronchograms.
- **Conclusion:** Consolidation is not present (**consolidation = false**), and the consolidation type is **null**.

**Final Conclusions:**
- **lung_rockets:** true
- **b_line_subtype:** ground_glass
- **consolidation:** false
- **consolidation_type:** null
