# Chat Analysis - January 21, 2026

**Date:** January 21, 2026  
**Chat File:** KakaoTalk_Chat_Everint_2026-01-21-14-13-56.csv

---

## Summary

This document summarizes key updates, completed tasks, new tasks, and critical observations from the chat messages on January 21, 2026. Major production run of 60+ products was completed, but several critical issues were identified.

---

## ✅ Completed Tasks (Jan 21)

### Screw Robot (Hieu, Ammad)
1. **State machine race condition fixed** - Race condition issue pointed out and fixed (Owner: Hieu)
2. **State machine issue resolved** - State machine issue resolved (Owner: Ammad)
3. **Screw pick improvement & troubleshooting** - Troubleshooting why in test bench work but assembly misses screw (Owner: Ammad)
4. **Speeding of xb to feeder and from feeder** - Movement speed optimized (Owner: Ammad)
5. **Addition of image capture before gripper using camera** - Sending MQTT msg to capture image from Omron camera (Owner: Ammad, Hieu)
6. **Addition of buzzer to inform system start and finished** - Buzzer added to inform system status (Owner: Ammad)
7. **Addition of screw tilt mirror** - Mirror added (temporary magnetic base, needs dedicated bracket) (Owner: Ammad)
8. **Improved logic when picking screw for next cycle** - Logic improved (Owner: Hieu)
9. **Optimized movements** - Still using move XB but always use moveL to target points (Owner: Hieu)
10. **Production run - 60+ products assembled** - Product ran in continuous sessions, total more than 60 (4 carts) (Owner: Hieu, Ammad)

### Rubber Foot Robot (Tan)
1. **Scoop image feature after scooping rubber foot** - Move home => save image again, path: Data/scoop_images/Datetime (Owner: Tan, Jan 20)
2. **Recent Images manager feature** - Save recent image and svg in recent folder, almost complete, need to filter type of image (Owner: Tan, Jan 20)

### Vision Team (Ghulam Muhammd)
1. **Omron camera vision system implemented** - Robot-triggered top-camera vision system to detect collisions between robot gripper hands and printer on conveyor belt, cycle time ~50ms (Owner: Ghulam Muhammd)

---

## 🔴 New Critical Issues Identified

### Screw Robot Issues
1. **Printer is tilted - depth based angle adjustment while screwing**
   - Printer is tilted, causing bit offset after each screwing causing pick miss
   - Also causing screw robot reset timeout
   - **Owner:** Ammad, Hieu
   - **Priority:** Urgent/Important

2. **False negative in screw tilt detection**
   - FN in screw tilt detection causing screw bit to screw with tilted screw
   - **Owner:** Haider Shah, Hieu

3. **Screw bit mis-grip issue (strikes screw head with force, remains stuck on edge)**
   - Screw bit frequently mis-grips screw
   - Bit strikes screw head with force, strong magnetic attraction keeps screw stuck on edge
   - **Owner:** Ammad, Hieu

4. **Screw bit drift away from pickup position**
   - Screw bit occasionally drifts away from pickup position
   - Suspected caused by unsmooth screwing in top-right screw hole
   - **Owner:** Ammad, Hieu

5. **Install dedicated bracket for screw mirror**
   - Magnetic base bracket unstable due to vibration
   - Dedicated bracket required for fixed and repeatable position
   - Mirror critical for detecting tilts
   - **Owner:** Muazzam, Ammad

6. **Find a way to drop screw near pick position (electromagnet)**
   - **Owner:** Ammad, Muazzam
   - **Priority:** Urgent/Important

### Rubber Foot Robot Issues
1. **Rubber foot attachment incorrect in most trials**
   - Attachment incorrect in most trials
   - Stopped operating rubber foot robot due to repeated misattachments
   - Constant offset applied but still unsatisfactory
   - **Owner:** Tugi, Rizwan

### Hardware Issues
1. **No spares for finger present**
   - **Owner:** Myeongun, Muazzam
   - **Priority:** Urgent/Important

2. **New metal finger are not assembled & tested**
   - **Owner:** Muazzam, Ammad
   - **Priority:** Urgent/Important

### System Issues
1. **PCB robot PC turned off during process**
   - PC turned off during process, robot stopped
   - **Owner:** Ammad, Kwanghyeop

---

## 🟡 New High Priority Tasks

### Framework Improvements (Ammad)
1. **Bit alignment jig after screwing** - Improvisation oiling and spring insertion
2. **Addition of add_command parameter XB motion** - Different blending types and blending distance option
3. **Addition of one extra linear point** - To blend distance zero so it reaches actual position
4. **Addition of add_command function parameter** - For setting each motion tolerance (set different tolerances for different motions)
5. **Increasing speed of Fairino robot** - Up and down movements
6. **Screw feeder empty issue** - Handle empty feeder condition
7. **Duration based signal stop** - Important - Signal handling improvement
8. **Reduce cycle time** - Find area to improve
9. **Pause functionality** - Debugging and saving product from damage (Important - Safety feature)
10. **Conveyor signal testing** - Magnetic switch on pneumatic used at set position but set to max reach point

---

## 📊 Key Observations (Odil, Jan 21)

Approximately 60 LPs were screwed during the trial.

1. **Screw pickup mis-grip** - While picking up screws from the feeder, the screw bit frequently mis-grips the screw. The bit often strikes the screw head with force, and due to the strong magnetic attraction, the screw remains stuck on the edge of the bit.

2. **Screw bit drift** - During the screwing operation, the screw bit occasionally drifts away from the pickup position. This is suspected to be caused by unsmooth screwing in one of the LP screw holes, most frequently the top-right screw hole.

3. **Rubber foot attachment failure** - Rubber foot attachment was incorrect in most trials. Due to repeated misattachments, we eventually stopped operating the rubber foot robot.

4. **Constant offset insufficient** - Tan applied a constant offset to all screw attachment points; however, the results were still unsatisfactory.

5. **Mirror attachment instability** - Temporarily attaching the mirror using a magnetic base bracket is challenging because the robot table experiences continuous vibration during screwing. Additionally, the table surface interferes with the magnetic holding force.

6. **Dedicated bracket needed** - A dedicated bracket is required to hold the screw mirror in a fixed and repeatable position. Given the instability in screw feeding, the mirrored view is critical for detecting potential tilts, which are currently missed at times due to limited viewing angles.

---

## 📈 Production Statistics

- **Products assembled:** 60+ products (4 carts)
- **Production mode:** Continuous sessions
- **Status:** Completed successfully but with identified issues

---

## 🔍 Critical Findings

1. **Printer Tilt Issue** - This is causing cascading problems:
   - Bit offset after each screwing
   - Pick miss due to tilt
   - Screw robot reset timeout

2. **Rubber Foot Robot Stopped** - Due to repeated misattachments, the rubber foot robot was stopped during production run.

3. **Screw Pickup Issues** - Multiple issues with screw pickup:
   - Mis-grip (bit strikes screw head)
   - Screw stuck on edge due to strong magnetism
   - Bit drift away from pickup position

4. **Hardware Spares Critical** - No spares for fingers present, new metal fingers not assembled/tested.

---

## 🎯 Immediate Action Items

### Critical (Must Fix Before Next Production Run)
1. Fix printer tilt - depth based angle adjustment
2. Fix rubber foot attachment (resume operation)
3. Prepare finger spares
4. Assemble and test new metal fingers
5. Install dedicated bracket for screw mirror

### High Priority (Improve Reliability)
1. Fix screw bit mis-grip issue
2. Fix screw bit drift
3. Fix false negative in screw tilt detection
4. Implement electromagnet for dropping screw near pick position
5. Fix PCB robot PC stability issue

### Framework Improvements
1. Implement pause functionality
2. Add duration based signal stop
3. Improve cycle time
4. Add bit alignment jig improvements
5. Add motion tolerance parameters

---

## 📝 Notes

- **Team Collaboration:** Shoaib emphasized that team members must help each other regardless of assigned tasks. Uncooperative behavior will not be tolerated.

- **Production Stability:** Despite running 60+ products, several critical issues were identified that need immediate attention before next production run.

- **Vision System:** Omron camera collision detection system successfully implemented with 50ms cycle time.

- **Recent Images Feature:** Tan's recent images manager feature almost complete, needs image type filtering.

---

**Last Updated:** January 21, 2026

