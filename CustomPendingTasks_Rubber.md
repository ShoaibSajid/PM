# Custom Pending Tasks — Rubber Foot Robot

**Last updated:** February 4, 2026 (from latest chat Feb 2–4)

---

## Completed (from latest chat)

- Vision PRs merged; no pending PRs (Tugi, Rizwan).
- Rescan code tested; robot places next rubber if vision says missing (Tugi).
- Top camera integrated on both screw and rubber foot robot; lens replaced, rubber camera rotated to match screw (Tugi).
- Code merged between both robots; robot PC, screw PC, vision branch aligned (Tugi).
- Recent images on GUI (1 per product, red box if fail) (Tan, Tugi).
- Rubber depth calculation does not affect cycle time; ThreadPoolExecutor + shared memory (Quy Ninh).

---

## Planned / In progress

1. **Reposition the platform / rubber pad holders**
   - Position so we can put 3 holders on the platform
   - Redesign if needed

2. **3D print the catching basket for sheets/rubbers**
   - Design and print it

3. **R-foot calibration** *(from chat – Professor request)*
   - Detailed photos: 4 products × 4 feet per printer type, 3 printer types
   - Compare positions for x,y offset estimation

4. **Make PPT** *(from chat – Shoaib Feb 4)*
   - Tune rubber pad positions first
   - 1 printer model × 4 products × 4 foot images = 16 images; × 3 printer types = 48 images total

---

## From members

*Issues pending as we discussed over the phone:*

- Rubber feet roller assembly needs to be **3**. Currently it is only one.

- Rubber feet roller assembly is not mounted properly: aluminum brackets need redesign and mounting plates should be made according to **3 column design** with proper holes to secure them.

- Rubber feet roller assembly has an issue when inserting rubber sheets: **wrinkling when we scoop** — not always but from time to time.

- Need to make **scooper blade**, scooper blade mounting bracket, and finger-nail-based gripper bracket in **metal** (currently using old long design with 2D camera).

- Need to **finalize all hardware equipment** to their final form in terms of material (**plastic → metal**).
