# Custom Pending Tasks — Screw Driver Robot

**Last updated:** February 4, 2026 (from latest chat Feb 2–4)

---

## Completed (from latest chat)

- ~~**Depth Map Analysis**~~ ✅ — Raw depth data provided to vision team (~50).
- ~~**Integrate Top Camera**~~ ✅ — Done on screw robot (trigger mode); top camera merged on both robots (Tugi).
- ~~**Tilt Rx,Ry in framework**~~ ✅ — Integrated from Shams/Quy (Quy Ninh); angle **not yet used in robot motion**.
- Terminate signal → warning + image on GUI (Hieu).
- Screw driver timeout at last hole → warning, no drop in next cycle (Hieu).
- Model not initialized → warning (Hieu).
- No detections after 4 rescans → warning on GUI (Hieu).
- SLP-DX220 cycle time 25–27s stable (Quy Ninh).
- Brightness threshold Sajjad Model 2, feeder A/B 100→105 (Ghulam Muhammd).
- Raw depth / depth-normalized / RGB file handling (Tan); Farino bracket spacing for largest product (Tan).

---

## Planned / In progress

1. **Use tilt angle (Rx, Ry) in robot motion**
   - Tilt is integrated in framework; use returned angle when moving/screwing (Hieu).

2. **Install Mirror properly**
   - Fixed and repeatable position; need **special jig** (Odil: will talk to Haider) — mirror was removed, was unstable.

3. **Fairino Collision Integration**
   - Integrate Fairino collision flag (not yet integrated).
   - **Fairino SDK:** connection fixed then “SDK version wrong”; **contact vendor for guidance/training** (Ammad, Feb 4).

4. **Test GUI and find potential issues**
   - **GUI bug:** robot active but GUI showed not active until refresh (Hieu sent GUI-issue.mp4; Jalol to check).

5. **Reduce inference time** (tilt + detection)
   - Hieu: inference time quite long; vision team to optimize.

---

## From members

*Hardware / code list from team:*

1. **GPU** — New algorithm makes inference time x3 (or x4); need a more powerful GPU.

2. **Extension part for gripper fingers** should be in **metal**, otherwise it will break after some time.

3. **SLP-DX220** (2 holes in lower layer): modify the code to calculate depth — top surface subtract a fixed value.

4. **Jalol:** Professor required a feature to adjust position of Fairino robot; movement is complex. Muazzam is using moveJ with fixed movement for every printer. If we want it per printer, need Muazzam to help.
