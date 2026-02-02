# Chat Analysis – February 1–2, 2026

**Source:** KakaoTalk_Chat_Everint_2026-02-02-10-56-07.csv  
**Timezone:** Asia/Seoul (KST)

---

## Executive Summary

- **Feb 2 plan:** Morning: TX400 and DL410 run at factory (no robot on those). Update vision models in morning. Focus: prepare system and run **XD3-40t 200 products** through screw driver robot. Extension bracket not ready; big printer (TX400) not run; Hieu reverted to metal fingers/bracket.
- **Vision integration (Feb 1):** Agreed: framework sends rgb + depth together; vision returns **X, Y, Rx, Ry** in one response. Tilt detection to be integrated inside Rizwan’s model. Hieu to pass depth image and use returned values after PR merge.
- **Feb 2 morning:** Shallow-hole issue on screw robot – Hieu reported 2 holes too shallow to tighten. Myeongun (이명근) will 3D print through-hole part (optional heating nut). Hieu asked Ammad/Tan which changes to commit.
- **Finger design:** TX400 too big for current gripper fingers. Shoaib asked Muazzam to own Fairino finger design for all products + spare. Extension bracket deferred.

---

## Completed / Progress (Feb 1–2)

| Item | Owner | Status |
|------|--------|--------|
| Vision approach (X,Y + Rx,Ry in one model) | Odil, Shoaib | Agreed: one model returns X, Y, Rx, Ry; tilt inside Rizwan’s model |
| Depth format / pipeline | Shoaib, Odil | Framework sends rgb + depth together; vision runs tilt after detection |
| Feb 2 production focus | Shoaib, Hieu | Only XD3-40t (200 products); no TX400/DL410 robot run |
| Metal fingers (revert) | Hieu | Reverted to metal (extension bracket not ready) |
| 3D print for shallow holes | Myeongun | Will print through-hole part so screws latch; optional heating nut |

---

## New / Updated Tasks from Chat

| Task | Owner | Notes |
|------|--------|------|
| Update **Book.xlsx** with status of each printer | Hieu, Tugi | Shoaib shared link; write status so team can focus printer by printer |
| 3D print part for shallow-hole fix (through-hole + optional heating nut) | Myeongun (이명근) | Hieu: 2 holes can’t be tightened; Myeongun to print so bolts latch properly |
| Provide **M4 bolt length** used on site | Hieu / team | Myeongun asked for 3D print design; need to reply |
| Clarify **which changes Hieu should commit** | Ammad, Tan | Hieu asked (Feb 2); follow up so he can commit today’s work |
| Merge vision **3 PRs** (top camera, tilt in model, improved ROI) | Hieu | Shoaib: vision to provide Feb 2; Hieu to merge; separate screw-driver-only ROI PR if possible |
| Fairino finger design for **all products + spare** | Muazzam | Shoaib (Feb 1): manage so we can hold all products and keep spare; others to help |

---

## Product / Production Context (Feb 1–2)

- **Label printer (2/2):** TX400 436EA, DL410 166EA, XD3-40t 200EA, XD5-40d 116EA (Kwanghyeop).
- **PCB (2/2):** 350III 110EA, 380 480EA, 330III 804EA.
- **TX400:** Largest printer; current gripper fingers too short (Ammad); not running robot until extension bracket ready.
- **DL410 / DL413:** 4 screw holes, tilt 0, 2 holes deeper and non-circular; Hieu sent 3 photos.
- **XD3-40t:** No issue; target for Feb 2 – 200 products through screw driver.

---

## Risks / Follow-ups

- **Rizwan:** Screw driver PC code old; suggested consistent code on both robot PCs. Odil: avoid big change; system to be submitted this week.
- **RealSense:** Ammad shared post-processing filters (min/max range, hole filler, spatial, temporal, etc.); possible future improvement for depth.
- **Depth storage format:** .raw, .npy, 16-bit PNG, .ply discussed; inference uses raw values; Odil to confirm format for saved data.

---

## Links Referenced

- **Book.xlsx (printer status):**  
  https://msislabai-my.sharepoint.com/:x:/r/personal/saad_msislab_com/Documents/AI_Robot_Shared/Everint_ScrewDriver_Project/MSIS%20Documentation/Book.xlsx?d=wda4e9e34312243d584078823b242e1d3&csf=1&web=1&e=fRpIug
- **Bixolon label printers:** https://kr.bixolon.com/product.php?key=label
- **RealSense post-processing filters:** https://github.com/realsenseai/librealsense/blob/master/doc/post-processing-filters.md
