# Chat Analysis - January 19-20, 2026

**Date:** January 20, 2026  
**Chat File:** KakaoTalk_Chat_Everint_2026-01-20-11-16-13.csv

---

## Summary

This document summarizes key updates, completed tasks, new tasks, and pending items from the chat messages on January 19-20, 2026.

---

## ✅ Completed Tasks (Jan 19-20)

### Screw Robot (Hieu, Ammad, Muazzam)
1. **Screw pickup issue resolved** - Adjusted pickup speed, filed screw bit to make it fit perfectly with phillips head, lowered checking position (big help from Ammad and Muazzam)
2. **Holes detection fixed** - Fixed by changing reference image for XD5-40dc (with Shams)
3. **Model 2 screw validation code updated** - Updated and tested, model2's owner needs to distinguish some fail cases that have same detection as normal
4. **Removed moveXB** - Removed when moving to fastening position to avoid non-reaching issue
5. **Adjusted fastening angle** - Adjusted fastening angle of screw driver
6. **Robot speed issue** - Reset control box helped, need further observation (Ammad)

### Rubber Foot Robot (Tugi)
1. **Changed vacuum suction cup spring** - Replaced with thicker one
2. **Vacuum gripper operation restored** - Previously air was leaking inside, now fixed
3. **Vacuum box cleaned and sealed** - Cleaned debris inside vacuum box and sealed properly, suction improved
4. **Rescan logic tested** - Tested with latest code, rolled back due to issues, vision team working on fixes

### Vision Team (Rizwan, Shams, Haider Shah)
1. **Vision PRs merged** - PR #125, #126, #129 merged for rubber foot attachment and detection improvements
   - Added logic to handle 'extracted_bbox' drawing on annotated_image
   - Updated decision logic for handling 'H' and 'R' labels
   - Improved rescan_completed flag calculation
   - Added warning logging for misaligned rubber foot detection
   - Added confidence to improve rubber foot detection
   - Resolved indexing issue with rubber foot attachment

### Hardware (Myeongun)
1. **Fairino fingers Option B printed** - All Option B fingers printed

---

## 🔴 New Critical Issues Identified

1. **State machine execution issues** (Ammad, Jan 20)
   - Multiple command queue: Either multiple commands are being queued in one state or at stop signal commands are not cleared
   - Screwpick missing due to Xb_J: Solution - remove xb_j or setting distance blending to zero at last step
   - **Owner:** Ammad, Hieu

2. **Printer tilt forward/backward after release** (Screw Robot)
   - Printer tilts after release by screw robot, can cause issue for rubber foot robot
   - **Owner:** Ammad, Hieu

3. **Issues when start signal comes before completing cycle**
   - Identified by Hieu (Jan 19-20)
   - **Owner:** Hieu, Ammad

4. **Screw validation for model 2** - Distinguish fail cases with same detection as normal
   - Model 2 owner needs to distinguish some fail cases that have same detection as normal
   - **Owner:** Haider Shah, Hieu

5. **Left side blur and brightness issue in camera images**
   - Left side of image seems blur and has lesser brightness (Rizwan, Jan 19)
   - **Owner:** Rizwan, Hieu

6. **Add printer config files to different folder** - Prevent overwriting during PR merge
   - Requested by Rizwan (Jan 19)
   - **Owner:** Hieu

---

## 🟡 New High Priority Issues

1. **Install mirror for model 2 (screw robot)**
   - Shams started but couldn't finish (Jan 19)
   - Haider can do if robot team busy
   - **Owner:** Haider Shah, Shams

2. **Capture scooped rubber foot images after scooping**
   - Currently not capturing (Shoaib confirmed)
   - Haider says necessary because scooping may change position of rubber pads and cause problem while picking up
   - **Owner:** Tugi, Hieu (someone else to capture if Tugi stays in lab)

3. **Test rolling/gripper based rubber pickup mechanism**
   - Deadline: Thursday lunch time (Jan 23)
   - Need ready to install, 3D printed, working version
   - **Owner:** Ammad, Muazzam

4. **Prepare complete spare for vacuum box with motor**
   - Requested by Shoaib (Jan 20)
   - Need complete spare ready if using current mechanism for more than a week
   - **Owner:** Tugi, Ammad, Muazzam

5. **Order screw bits**
   - Requested by Ammad (Jan 19)
   - **Owner:** Kwanghyeop

---

## 📋 Tasks from CustomPendingTasks.md

1. **Install screw robot mirror** - Added to high priority
2. **Printer tilt forward/backward after release** - Added to critical issues
3. **Take rubber pad pictures every cycle and after scooping / integrate rubber pad offset** - Added to high priority
4. **Link screw/rubber robots, to pre pickup the rubber pad** - Added to high priority
5. **Work on the new rubber pad design** - Added to high priority (Tugi and Muazzam)
6. **Work on identifying the state machine race condition** - Added to high priority (Ammad and Hieu)

---

## ⏳ In Progress / Pending Tasks

### Vision Team Requests (Pending from Robot Team)
1. **List of pending tasks requested by vision team** - Shoaib requested (Jan 20)
   - Vision team needs to share list

### Robot Team Requests (Pending from Vision Team)
1. **List of current issues from vision models** - Shoaib requested (Jan 20)
   - Robot team needs to share list

### Rescan Logic
- Tested by Tugi (Jan 19-20)
- Rolled back due to issues
- PR #129 merged for improvements
- Needs re-integration and testing

### Rubber Foot ROI Detection
- Still having failures (Tugi reported Jan 19)
- Vision team working on it

### Screw Validation
- Model 2: 1-2 false negatives remain
- Sajad fixing (Hieu, Jan 19)

---

## 📊 Status Updates

### Cycle Time
- **Rubber Foot Robot:** 30s including rescan/validation (Tugi, Jan 19)
- **Screw Robot:** Pending confirmation

### Production Testing
- Screw Robot: Ran testing with all updates on production (5-6 printers) - worked fine (Hieu, Jan 19)
- Rubber Foot Robot: Processed last 10 products successfully without failure (without rescan/validation integration) (Tugi, Jan 19)

### Vision Model Status (Rizwan, Jan 19)
- Screw and rubber foot code for scanning from the same position verified and updated
- Issue with index at which rubber foot is attached - resolved in latest PR
- Shams and Haider analyzed with test sample - code working on test dataset
- Misaligned rubber foot detection method added - needs verification with real inference examples
- For mounted camera (Omron): Ghulam working to detect presence of printer and whether it's at center of robot fingers
- Self training code added and verified for one printer type by Hieu

---

## 🔍 Key Observations

1. **Robot Speed Issue:** Reset control box helped, but needs further observation (Ammad)
2. **State Machine Issues:** Multiple command queue and screwpick missing issues identified (Ammad, Jan 20)
3. **Vision Model Improvements:** Multiple PRs merged for rubber foot detection improvements
4. **Hardware:** Fairino fingers Option B printed, vacuum box cleaned and sealed
5. **Production Readiness:** Both robots tested with production samples, mostly working but some issues remain

---

## 📅 Next Steps

1. Fix state machine execution issues (critical)
2. Fix printer tilt after release (critical)
3. Complete rescan logic integration (after vision fixes)
4. Install mirror for model 2
5. Capture scooped rubber foot images
6. Test rolling/gripper mechanism (deadline: Thursday lunch)
7. Prepare vacuum box spare
8. Order screw bits

---

**Last Updated:** January 20, 2026

