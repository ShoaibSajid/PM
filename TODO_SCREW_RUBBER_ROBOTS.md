# TODO List - Screw Robot & Rubber Foot Robot

**Last Updated:** January 21, 2026  
**Status:** Active tracking for both robot systems

---

## 🔴 Screw Robot - Critical / Blocking Issues

### Hardware & Mechanical
- [ ] **Fix printer tilt - depth based angle adjustment while screwing**
  - Owner: Ammad, Hieu
  - Status: Printer is tilted, causing bit offset after each screwing causing pick miss, also screw robot reset timeout
  - Priority: Urgent/Important
  - Impact: CRITICAL - Blocks production

- [ ] **Fix screw bit mis-grip issue (strikes screw head with force, remains stuck on edge)**
  - Owner: Ammad, Hieu
  - Status: Screw bit frequently mis-grips screw, bit strikes screw head with force, strong magnetic attraction keeps screw stuck on edge
  - Priority: CRITICAL
  - Impact: Blocks production

- [ ] **Fix screw bit drift away from pickup position**
  - Owner: Ammad, Hieu
  - Status: Screw bit occasionally drifts away from pickup position, suspected caused by unsmooth screwing in top-right screw hole
  - Priority: CRITICAL
  - Impact: Blocks production

- [ ] **Install dedicated bracket for screw mirror (fixed and repeatable position)**
  - Owner: Muazzam, Ammad
  - Status: Magnetic base bracket unstable due to vibration, dedicated bracket required
  - Priority: CRITICAL
  - Impact: Mirror critical for detecting tilts

- [ ] **Find a way to drop screw near pick position (electromagnet)**
  - Owner: Ammad, Muazzam
  - Status: Urgent/Important
  - Priority: CRITICAL
  - Impact: Improves reliability

- [ ] **No spares for finger present**
  - Owner: Myeongun, Muazzam
  - Status: Urgent/Important
  - Priority: CRITICAL
  - Impact: Blocks production continuity

- [ ] **New metal finger are not assembled & tested**
  - Owner: Muazzam, Ammad
  - Status: Urgent/Important
  - Priority: CRITICAL
  - Impact: Blocks production

- [ ] **Fix fragile Fairino fingers bending when gripping**
  - Owner: Ammad, Myeongun
  - Status: Fingers bend when gripping product
  - Solution: Use metal/inward bent fingers
  - Priority: CRITICAL

### Vision & Detection
- [ ] **Fix false negative in screw tilt detection**
  - Owner: Haider Shah, Hieu
  - Status: FN in screw tilt detection causing screw bit to screw with tilted screw
  - Priority: CRITICAL
  - Impact: Causes quality issues

- [ ] **Fix screw pickup validation - Label Printer Screw Robot (2nd screw feeder FPs)**
  - Owner: Hieu, Haider Shah, Rizwan
  - Status: Model 2 screw validation updated (Jan 19-20), 1-2 false negatives remain, Sajad fixing
  - Priority: CRITICAL
  - Impact: Blocks production

- [ ] **Fix screw validation for model 2 (distinguish fail cases with same detection as normal)**
  - Owner: Haider Shah, Hieu
  - Status: Model 2 owner needs to distinguish some fail cases that have same detection as normal
  - Priority: CRITICAL
  - Impact: Blocks production

- [ ] **Fix left side blur and brightness issue in camera images**
  - Owner: Rizwan, Hieu
  - Status: Left side of image seems blur and has lesser brightness
  - Priority: CRITICAL
  - Impact: Blocks accurate detection

- [ ] **Fix tilted screw issue - Label Printer Screw Robot (2nd Priority)**
  - Owner: Ammad, Hieu
  - Status: Screw pickup improved (Jan 19-20) - adjusted pickup speed, filed screw bit for better fit, lowered checking position
  - Priority: High
  - Impact: In progress

- [ ] **Investigate and fix screw pickup tilting**
  - Owner: Hieu, Ammad
  - Status: Likely magnetism and long screw issue
  - Solution: Consider replacing feeder's rotating plate with plastic
  - Priority: CRITICAL

### Software & Framework
- [ ] **Fix state machine execution issues (Multiple command queue, screwpick missing)**
  - Owner: Ammad, Hieu
  - Status: Race condition issue pointed out and fixed (Jan 21), state machine issue resolved
  - Priority: CRITICAL
  - Impact: Blocks production

- [ ] **Fix issues when start signal comes before completing cycle**
  - Owner: Hieu, Ammad
  - Status: Identified (Jan 19-20)
  - Priority: CRITICAL
  - Impact: Can cause state machine issues

- [ ] **Fix screw speed issue - Label Printer Screw Robot (1st Priority)**
  - Owner: Hieu, Ammad
  - Status: Reset control box helped (Jan 19), need further observation
  - Priority: CRITICAL
  - Impact: Blocks cycle time

- [ ] **Fix robot speed in timeout/collision (clean_up function)**
  - Owner: Ammad
  - Status: Dump robot's system variables at start and after slowdown for analysis
  - Priority: CRITICAL
  - Impact: Blocks cycle time

- [ ] **Debug screwdriver robot moving slow**
  - Owner: Hieu, Ammad
  - Status: Robot speed needs investigation
  - Priority: CRITICAL
  - Impact: Blocks cycle time

- [ ] **Add printer config files to different folder to prevent overwriting during PR merge**
  - Owner: Hieu
  - Status: Requested by Rizwan (Jan 19)
  - Priority: High
  - Impact: Prevents config loss during merges

### Registration & Setup
- [ ] **Fix manual registration issue - Both systems (1st Priority)**
  - Owner: Jalol
  - Status: Work on this first, before auto registration bug
  - Priority: CRITICAL
  - Impact: CRITICAL for Monday demo

- [ ] **Register all products with new code - Both systems**
  - Owner: Hieu, Tugi, Quy Ninh
  - Status: Only 2 done (XD5-40D, XD3-40D), waiting for manual registration fix
  - Priority: CRITICAL
  - Impact: CRITICAL for Monday demo

- [ ] **Register XD5-40D with new code - Both systems**
  - Owner: Hieu, Tugi
  - Status: References changed due to new gripper fingers
  - Priority: CRITICAL
  - Impact: CRITICAL for Monday demo (950EA production)

- [ ] **Recapture reference images for all products (FR3 holding, not pressing arm)**
  - Owner: Tugi, Hieu, Odil
  - Status: Holes detection fixed for XD5-40dc (Jan 19-20), reference updated by Shams
  - Priority: CRITICAL
  - Impact: Blocks accurate detection

- [ ] **Integrate new vision code PR - Both systems**
  - Owner: Hieu, Rizwan
  - Status: PR ready, needs integration to Hieu-second branch, solve conflicts
  - Priority: CRITICAL
  - Impact: Blocks new features

- [ ] **Fix self training file saving issue (path format)**
  - Owner: Haider Shah
  - Status: File saved to wrong folder, named with full path, use os.path
  - Priority: CRITICAL
  - Impact: Blocks proper saving

### Conveyor & Positioning
- [ ] **Conveyor position adjustment / fix (1st Priority)**
  - Owner: Ammad
  - Status: CRITICAL for Monday demo
  - Priority: CRITICAL
  - Impact: Affects product positioning

- [ ] **Fix out of place product on conveyor causing collision**
  - Owner: Ammad, Hieu
  - Status: Products misaligned causing collision/damage
  - Solution: Use top camera to detect product within acceptable zone
  - Priority: CRITICAL

### Performance & Validation
- [ ] **Confirm cycle time - Label Printer Screw Robot**
  - Owner: Hieu, Saad
  - Status: Pending
  - Priority: CRITICAL
  - Impact: Cycle time validation pending

- [ ] **Complete 2D camera hardware installation**
  - Owner: Muazzam, Ammad
  - Status: Hardware installation incomplete
  - Priority: CRITICAL
  - Impact: Blocks full system functionality

---

## 🟡 Screw Robot - High Priority Tasks

### Framework Improvements
- [ ] **Bit alignment jig after screwing (improvisation oiling and spring insertion)**
  - Owner: Ammad, Muazzam
  - Status: Remaining task (Jan 21)
  - Priority: High
  - Impact: Improve bit alignment

- [ ] **Addition of add_command parameter XB motion different blending types and blending distance option**
  - Owner: Ammad
  - Status: Remaining task (Jan 21)
  - Priority: High
  - Impact: Framework improvement

- [ ] **Addition of one extra linear point to blend distance zero so it reaches actual position**
  - Owner: Ammad
  - Status: Remaining task (Jan 21)
  - Priority: High
  - Impact: Framework improvement

- [ ] **Addition of add_command function parameter for setting each motion tolerance**
  - Owner: Ammad
  - Status: Remaining task (Jan 21)
  - Priority: High
  - Impact: Framework improvement - set different tolerances for different motions

- [ ] **Increasing speed of Fairino robot up and down**
  - Owner: Ammad
  - Status: Remaining task (Jan 21)
  - Priority: High
  - Impact: Performance improvement

- [ ] **Screw feeder empty issue**
  - Owner: Ammad, Muazzam
  - Status: Remaining task (Jan 21)
  - Priority: High
  - Impact: Handle empty feeder condition

- [ ] **Duration based signal stop**
  - Owner: Ammad
  - Status: Remaining task (Jan 21)
  - Priority: High (Important)
  - Impact: Signal handling improvement

- [ ] **Reduce cycle time, find area to improve**
  - Owner: Hieu, Ammad
  - Status: Remaining task (Jan 21)
  - Priority: High
  - Impact: Performance optimization

- [ ] **Pause functionality (debugging and saving product from damage)**
  - Owner: Ammad, Hieu
  - Status: Remaining task (Jan 21)
  - Priority: High (Important)
  - Impact: Safety feature

- [ ] **Conveyor signal testing - magnetic switch on pneumatic**
  - Owner: Ammad, Hieu
  - Status: Magnetic switch on pneumatic used at set position but set to max reach point (Jan 21)
  - Priority: High
  - Impact: Signal handling

---

## 🔴 Rubber Foot Robot - Critical / Blocking Issues

### Attachment & Positioning
- [ ] **Fix rubber foot attachment incorrect**
  - Owner: Tugi, Rizwan
  - Status: Rubber foot attachment incorrect, stopped operating rubber foot robot (Jan 21)
  - Priority: CRITICAL
  - Impact: Blocks production

- [ ] **Fix rubber foot attachment position error (Rubber Foot Robot)**
  - Owner: Tugi, Rizwan
  - Status: Attachment incorrect in most trials, stopped operating rubber foot robot (Jan 21), constant offset applied but still unsatisfactory
  - Priority: CRITICAL
  - Impact: Blocks production quality

- [ ] **Get robot to place rubber foot in correct position - Label Printer Rubber Foot Robot (1st Priority)**
  - Owner: Tugi
  - Status: Hand eye calibration done, tuning parameters in progress
  - Priority: CRITICAL
  - Impact: CRITICAL for Monday demo

- [ ] **Calibrate placement position - Label Printer Rubber Foot Robot (1st Priority)**
  - Owner: Tugi, Muazzam, Tan
  - Status: Hand eye calibration done (Jan 17), needs fine-tuning check (Jan 18)
  - Priority: CRITICAL
  - Impact: CRITICAL for Monday demo

### Vision & Detection
- [ ] **Fix rubber foot ROI detection (tighter mechanism issue)**
  - Owner: Rizwan, Hieu
  - Status: User ROI from GUI good, but tighter mechanism makes it wrong
  - Priority: CRITICAL
  - Impact: Blocks accurate detection

- [ ] **Test rescan logic (Rubber Foot Robot) (2nd Priority)**
  - Owner: Tugi
  - Status: Tested (Jan 19-20), rolled back due to issues, vision team working on fixes
  - Priority: High
  - Impact: Affects reliability

- [ ] **Integrate rescan logic - Label Printer Rubber Foot Robot (2nd Priority)**
  - Owner: Tugi, Rizwan
  - Status: Tested (Jan 19-20), rolled back, PR #129 merged for improvements, needs re-integration
  - Priority: High
  - Impact: Affects reliability

- [ ] **Integrate rubber pad pickup offset - Label Printer Rubber Foot Robot (2nd Priority)**
  - Owner: Tugi
  - Status: Pending integration
  - Priority: High
  - Impact: Affects pickup accuracy

### Hardware
- [ ] **Fix fragile Fairino fingers bending when gripping (Both systems)**
  - Owner: Ammad, Myeongun
  - Status: Fingers bend when gripping product
  - Solution: Use metal/inward bent fingers
  - Priority: CRITICAL

### Registration & Setup
- [ ] **Fix manual registration issue - Both systems (1st Priority)**
  - Owner: Jalol
  - Status: Work on this first, before auto registration bug
  - Priority: CRITICAL
  - Impact: CRITICAL for Monday demo

- [ ] **Register all products with new code - Both systems**
  - Owner: Hieu, Tugi, Quy Ninh
  - Status: Only 2 done (XD5-40D, XD3-40D), waiting for manual registration fix
  - Priority: CRITICAL
  - Impact: CRITICAL for Monday demo

- [ ] **Register XD5-40D with new code - Both systems**
  - Owner: Hieu, Tugi
  - Status: References changed due to new gripper fingers
  - Priority: CRITICAL
  - Impact: CRITICAL for Monday demo (950EA production)

- [ ] **Recapture reference images for all products (FR3 holding, not pressing arm)**
  - Owner: Tugi, Hieu, Odil
  - Status: Holes detection fixed for XD5-40dc (Jan 19-20), reference updated by Shams
  - Priority: CRITICAL
  - Impact: Blocks accurate detection

- [ ] **Integrate new vision code PR - Both systems**
  - Owner: Hieu, Rizwan
  - Status: PR ready, needs integration to Hieu-second branch, solve conflicts
  - Priority: CRITICAL
  - Impact: Blocks new features

### Performance & Validation
- [ ] **Confirm cycle time - Label Printer Rubber Foot Robot**
  - Owner: Tugi, Saad
  - Status: 30s including rescan/validation (Jan 19)
  - Priority: CRITICAL
  - Impact: Cycle time validation pending

---

## 🟡 Rubber Foot Robot - High Priority Tasks

### Feature Completion
- [ ] **Complete Recent Images manager feature**
  - Owner: Tan
  - Status: Almost complete (Jan 20), need to filter type of image (depth/png/another)
  - Priority: High
  - Impact: Feature completion

### Integration & Testing
- [ ] **Test rolling/gripper based rubber pickup mechanism**
  - Owner: Ammad, Muazzam
  - Status: Deadline: Thursday lunch time (Jan 23), need ready to install 3D printed working version
  - Priority: High
  - Impact: Alternative pickup mechanism

- [ ] **Prepare complete spare for vacuum box with motor**
  - Owner: Tugi, Ammad, Muazzam
  - Status: Requested (Jan 20), need complete spare ready if using current mechanism for more than a week
  - Priority: High
  - Impact: Critical for production continuity

- [ ] **Work on new rubber pad design**
  - Owner: Tugi, Muazzam
  - Status: From CustomPendingTasks
  - Priority: High
  - Impact: Alternative design for rubber pad pickup

- [ ] **Link screw/rubber robots to pre-pickup the rubber pad**
  - Owner: Tugi, Hieu
  - Status: From CustomPendingTasks
  - Priority: High
  - Impact: Optimization for cycle time

- [ ] **Take rubber pad pictures every cycle and after scooping / integrate rubber pad offset**
  - Owner: Tugi, Rizwan
  - Status: From CustomPendingTasks
  - Priority: High
  - Impact: Required for vision model improvement

---

## 📋 Both Systems - Common Tasks

### Registration
- [ ] **Fix manual registration issue - Both systems (1st Priority)**
  - Owner: Jalol
  - Status: Work on this first, before auto registration bug
  - Priority: CRITICAL
  - Impact: CRITICAL for Monday demo

- [ ] **Register all products with new code - Both systems**
  - Owner: Hieu, Tugi, Quy Ninh
  - Status: Only 2 done (XD5-40D, XD3-40D), waiting for manual registration fix
  - Priority: CRITICAL
  - Impact: CRITICAL for Monday demo

- [ ] **Register XD5-40D with new code - Both systems**
  - Owner: Hieu, Tugi
  - Status: References changed due to new gripper fingers
  - Priority: CRITICAL
  - Impact: CRITICAL for Monday demo (950EA production)

- [ ] **Recapture reference images for all products (FR3 holding, not pressing arm)**
  - Owner: Tugi, Hieu, Odil
  - Status: Holes detection fixed for XD5-40dc (Jan 19-20), reference updated by Shams
  - Priority: CRITICAL
  - Impact: Blocks accurate detection

- [ ] **Integrate new vision code PR - Both systems**
  - Owner: Hieu, Rizwan
  - Status: PR ready, needs integration to Hieu-second branch, solve conflicts
  - Priority: CRITICAL
  - Impact: Blocks new features

### Hardware
- [ ] **Fix fragile Fairino fingers bending when gripping (Both systems)**
  - Owner: Ammad, Myeongun
  - Status: Fingers bend when gripping product
  - Solution: Use metal/inward bent fingers
  - Priority: CRITICAL

- [ ] **Fix out of place product on conveyor causing collision**
  - Owner: Ammad, Hieu
  - Status: Products misaligned causing collision/damage
  - Solution: Use top camera to detect product within acceptable zone
  - Priority: CRITICAL

---

## 📊 Progress Summary

### Screw Robot
- **Critical Issues:** 20 tasks
- **High Priority:** 10 tasks
- **Total:** 30 tasks

### Rubber Foot Robot
- **Critical Issues:** 12 tasks
- **High Priority:** 6 tasks
- **Total:** 18 tasks

### Both Systems
- **Common Tasks:** 6 tasks

### Grand Total
- **Total Tasks:** 54 tasks
- **Critical:** 32 tasks
- **High Priority:** 16 tasks
- **Common:** 6 tasks

---

## 🎯 Priority Focus Areas

### Immediate (This Week)
1. Fix printer tilt - depth based angle adjustment (Screw Robot)
2. Fix rubber foot attachment incorrect (Rubber Foot Robot)
3. Prepare finger spares (Both systems)
4. Assemble and test new metal fingers (Both systems)
5. Install dedicated bracket for screw mirror (Screw Robot)

### High Priority (Next Week)
1. Fix screw bit mis-grip issue (Screw Robot)
2. Fix screw bit drift (Screw Robot)
3. Fix false negative in screw tilt detection (Screw Robot)
4. Integrate rescan logic (Rubber Foot Robot)
5. Implement pause functionality (Screw Robot)

---

**Last Updated:** January 21, 2026

