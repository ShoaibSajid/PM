# Missing Tasks - Not in Asana

**Last Updated:** January 30, 2026  
**Purpose:** Tasks that are pending in URGENT_ISSUES_CHECKLIST.md but NOT currently tracked in Asana. These should be reviewed and added to Asana if still needed.

---

## 🔴 Critical / Blocking - Missing from Asana

### Registration & Setup
- **Fix manual registration issue - Both systems (1st Priority)**
  - Owner: Jalol
  - Status: GUI registration issue exists, Jalol fixing (Jan 22), Hieu did manual registration using existing name (SLP-DL413 instead of SLP-DX220)
  - Priority: CRITICAL for Monday demo

### Hardware & Mechanical
- **Fix metal finger spacing issue**
  - Owner: Myeongun, Muazzam
  - Status: Spacing not correct for fingers (Jan 22), need to add plastic sheet or thin flat washer
  - Priority: CRITICAL - Blocks production

- **No spares for finger present**
  - Owner: Myeongun, Muazzam
  - Status: Urgent/Important (Jan 21)
  - Priority: CRITICAL - Blocks production continuity

- **Install dedicated bracket for screw mirror (fixed and repeatable position)**
  - Owner: Muazzam, Ammad
  - Status: Magnetic base bracket unstable due to vibration, dedicated bracket required (Jan 21)
  - Priority: CRITICAL - Mirror critical for detecting tilts

- **Complete 2D camera hardware installation**
  - Owner: Muazzam, Ammad
  - Status: Hardware installation incomplete
  - Priority: Blocks full system functionality

- **Request continuous roll rubber pad sheets (8xN instead of 8x8)**
  - Owner: Kwanghyeop, Shoaib
  - Status: Current small sheets cause jam in roller area, need continuous roll for smooth operation (Jan 22)
  - Priority: CRITICAL - Improves reliability

- **Conveyor position adjustment / fix (1st Priority)**
  - Owner: Ammad
  - Status: CRITICAL for Monday demo
  - Priority: Affects product positioning

- **Fix out of place product on conveyor causing collision**
  - Owner: Ammad, Hieu
  - Status: Products misaligned causing collision/damage
  - Priority: Solution: Use top camera to detect product within acceptable zone

- **Fix upper light holder - Label Printer Screw Robot**
  - Owner: Ammad, Muazzam
  - Status: Upper light temporarily fixed with electrical tape (Jan 26), needs proper fixing in original holder
  - Priority: CRITICAL - System stability

### Vision & Detection
- **Fix screw pickup validation - Label Printer Screw Robot (2nd screw feeder FPs)**
  - Owner: Hieu, Haider Shah, Rizwan
  - Status: Model 2 screw validation updated (Jan 19-20), 1-2 false negatives remain, Sajad fixing
  - Priority: Blocks production

- **Fix rubber foot ROI detection (tighter mechanism issue)**
  - Owner: Rizwan, Hieu
  - Status: User ROI from GUI good, but tighter mechanism makes it wrong
  - Priority: Blocks accurate detection

- **Capture depth maps with different light settings**
  - Owner: Tan, Hieu
  - Status: Reflection analysis completed (Jan 28), JSON config tuned, needs testing (Jan 29)
  - Priority: CRITICAL - Vision model improvement

### Rubber Foot Robot - Custom Pending Tasks
- **Grind / Scrub Sheet Roller**
  - Owner: Tugi, Muazzam
  - Status: From CustomPendingTasks_Rubber.md (Jan 28)
  - Priority: CRITICAL - Hardware maintenance

- **3D print dual fingers for scoop**
  - Owner: Myeongun, Tugi
  - Status: From CustomPendingTasks_Rubber.md (Jan 28) - Determine tilt angle, share with Dr Saad
  - Priority: CRITICAL - Hardware design

- **Sheet Clamp Design to curve/bend the sheet**
  - Owner: Myeongun
  - Status: From CustomPendingTasks_Rubber.md (Jan 28) - Design and print
  - Priority: CRITICAL - Hardware design

---

## 🟡 High Priority - Missing from Asana

### Hardware & Mechanical
- **Improve calibration accuracy (Rubber Foot Robot)**
  - Owner: Tugi
  - Status: Needed to reduce position error
  - Priority: Critical for attachment accuracy

- **Method to overcome irregularities in rubber foot shape**
  - Owner: Tugi
  - Status: Need solution for irregular rubber foot shape
  - Priority: Affects attachment quality

- **Install buzzers for error/warning display (2nd Priority)**
  - Owner: Muazzam, Ammad
  - Status: Need to install
  - Priority: Required for production monitoring

- **Redesign fingers for Fairino to improve gripping (2nd Priority)**
  - Owner: Saad, Myeongun
  - Status: Need metal/inward bent fingers
  - Priority: Critical for production quality

- **Install vertical plates to make screws straight - Label Printer Screw Robot (2nd Priority)**
  - Owner: Ammad, Hieu
  - Status: Not done (Jan 17)
  - Priority: Blocks reliability

- **Integrate buzzer alarm - Both systems (3rd Priority)**
  - Owner: Ammad, Hieu, Tugi
  - Status: After 1st priority tasks
  - Priority: Required for production monitoring

- **Installation of remaining hardware according to government report (3rd Priority)**
  - Owner: Muazzam, Ammad
  - Status: After 1st priority tasks
  - Priority: Required for full functionality

- **Install all cameras and equipment from hardware purchase list**
  - Owner: Muazzam, Ammad
  - Status: 2D camera pending
  - Priority: Required for full functionality

### Vision & Detection
- **Use product size information while tightening YOLO bbox**
  - Owner: Rizwan, Haider Shah
  - Status: Need to use user-inserted product size
  - Priority: Prevents detecting black cushion with printer body

- **Maintain history of detection sizes for tighter bboxes**
  - Owner: Rizwan, Haider Shah
  - Status: Need to maintain average of last n detections
  - Priority: Improves detection accuracy

- **Analyze Omron camera images to detect wrong displacement of printers (after camera installation)**
  - Owner: Shams, Odil
  - Status: New task assigned (Jan 17)
  - Priority: Critical for product positioning

- **Fix rubber foot ROI detection (tighter mechanism issue)**
  - Owner: Rizwan, Hieu
  - Status: User ROI from GUI good, but tighter mechanism makes it wrong
  - Priority: Blocks accurate detection

- **Use Omron camera to detect mis-attachment of rubber foot**
  - Owner: Odil, Rizwan
  - Status: RealSense may not give clean view, Omron can provide better detection
  - Priority: After camera installation

- **Train lightweight detector for product presence (Omron camera)**
  - Owner: Odil
  - Status: Check if product is present and within safe gripping area
  - Priority: After camera installation

- **Organize images in cleaner format (product folder structure)**
  - Owner: Odil, Shoaib
  - Status: Currently 5-6 images per product, arrange in product ID folders
  - Priority: Improves organization

- **Install mirror for model 2 (screw robot)**
  - Owner: Haider Shah, Shams
  - Status: Shams started but couldn't finish (Jan 19), Haider can do if robot team busy
  - Priority: Required for model 2 detection

- **Capture scooped rubber foot images after scooping**
  - Owner: Tugi, Hieu
  - Status: Not capturing currently, Haider says necessary (scooping may change position)
  - Priority: Required for vision model improvement

### Software & GUI
- **Finalize GUI for PCB/Screw/Rubber**
  - Owner: Jalol
  - Status: Delay non-urgent tasks, finish urgent issues for Monday demo
  - Priority: Deadline: Sunday morning shift

- **Make changes to error message display (GUI side) - Both systems**
  - Owner: Jalol
  - Status: Hieu and Tugi completed framework side, Jalol needs to make GUI changes
  - Priority: CRITICAL for Monday demo

- **Fix conveyor operation guide**
  - Owner: Ammad, Tan
  - Status: Guide created (Jan 18), need to ensure proper operation
  - Priority: Affects system operation

- **Complete GUI testing (delayed due to depth tuning)**
  - Owner: Tan, Jalol
  - Status: Product testing could not be performed (Jan 28), needs completion
  - Priority: High priority - System quality

- **Refine GUI layout (cluttered, inconsistent button sizes)**
  - Owner: Jalol, Samrah
  - Status: Layout needs refinement, button sizes inconsistent between systems (Jan 28)
  - Priority: High priority - UX improvement

- **Fix screw validation logic (range and tilt angle)**
  - Owner: Hieu, Haider Shah
  - Status: Multiple false positive/negative cases, need range-based logic
  - Priority: Blocks production

### Framework & System Improvements
- **Bit alignment jig after screwing (improvisation oiling and spring insertion)**
  - Owner: Ammad, Muazzam
  - Status: Remaining task (Jan 21)
  - Priority: Improve bit alignment

- **Addition of add_command parameter XB motion different blending types and blending distance option**
  - Owner: Ammad
  - Status: Remaining task (Jan 21)
  - Priority: Framework improvement

- **Addition of one extra linear point to blend distance zero so it reaches actual position**
  - Owner: Ammad
  - Status: Remaining task (Jan 21)
  - Priority: Framework improvement

- **Addition of add_command function parameter for setting each motion tolerance**
  - Owner: Ammad
  - Status: Remaining task (Jan 21)
  - Priority: Framework improvement - set different tolerances for different motions

- **Increasing speed of Fairino robot up and down**
  - Owner: Ammad
  - Status: Remaining task (Jan 21)
  - Priority: Performance improvement

- **Screw feeder empty issue**
  - Owner: Ammad, Muazzam
  - Status: Remaining task (Jan 21)
  - Priority: Handle empty feeder condition

- **Duration based signal stop**
  - Owner: Ammad
  - Status: Remaining task (Jan 21)
  - Priority: Important - Signal handling improvement

- **Reduce cycle time, find area to improve**
  - Owner: Hieu, Ammad
  - Status: Remaining task (Jan 21)
  - Priority: Performance optimization

- **Pause functionality (debugging and saving product from damage)**
  - Owner: Ammad, Hieu
  - Status: Remaining task (Jan 21)
  - Priority: Important - Safety feature

- **Conveyor signal testing - magnetic switch on pneumatic**
  - Owner: Ammad, Hieu
  - Status: Magnetic switch on pneumatic used at set position but set to max reach point (Jan 21)
  - Priority: Signal handling

### Testing & Validation
- **Test rolling/gripper based rubber pickup mechanism**
  - Owner: Ammad, Muazzam
  - Status: Deadline: Thursday lunch time (Jan 23), need ready to install 3D printed working version
  - Priority: Alternative pickup mechanism

- **Test rubber foot attachment extensively with latest updated code**
  - Owner: Tugi, Tan, Rizwan
  - Status: Need extensive testing, need feedback from robot side (Jan 22)
  - Priority: High priority

- **Test metal fingers with new model**
  - Owner: Tugi, Muazzam
  - Status: Metal fingers prepared but not tested, need retraining after finger change (Jan 22)
  - Priority: High priority

- **Test RealSense JSON configuration**
  - Owner: Tan
  - Status: JSON config tuned (Jan 28), needs testing (Jan 29)
  - Priority: High priority - Vision improvement

### Documentation & Logistics
- **Prepare checkerboards and Aruco codes for calibration**
  - Owner: Tan
  - Status: Print two more checkerboards and two Aruco codes
  - Priority: For calibration support

- **Bring new ethernet cables from lab**
  - Owner: Ammad
  - Status: Current one not stable, sometimes disconnects
  - Priority: Blocks stable connection

- **Create Excel file - GUI tasks and issues status**
  - Owner: Jalol
  - Status: Deadline: Jan 15, 2026 | In progress, adding GUI & vision columns
  - Priority: Tracking

- **Collect dataset for vision model testing**
  - Owner: Rizwan, Shams, Tugi, Hieu
  - Status: Waiting for stable operation
  - Priority: Blocks validation

- **Complete vision model validation summary**
  - Owner: Rizwan
  - Status: In progress
  - Priority: Required for handover

- **3D parts list**
  - Owner: Muazzam, Ammad
  - Status: Shared Google Sheet (Jan 16)
  - Priority: Critical for tracking components

- **Maintain 3D components tracking list (requested/printed/handed over)**
  - Owner: Myeongun
  - Status: In progress
  - Priority: Track all 3D component requests

### Hardware Modifications
- **Work on new rubber pad design**
  - Owner: Tugi, Muazzam
  - Status: From CustomPendingTasks
  - Priority: Alternative design for rubber pad pickup

- **Prepare complete spare for vacuum box with motor**
  - Owner: Tugi, Ammad, Muazzam
  - Status: Requested (Jan 20), need complete spare ready if using current mechanism for more than a week
  - Priority: Critical for production continuity

- **Contact manufacturer to lengthen one side of rubber pad**
  - Owner: Kwanghyeop, Shoaib
  - Status: Need to contact manufacturer to lengthen one side for smooth scooping operation (Jan 22)
  - Priority: High priority

- **Contact Rainbow about control box bugs**
  - Owner: Kwanghyeop
  - Status: Need to contact Rainbow about PWM and gripper speed/force adjustment bugs (Jan 22)
  - Priority: High priority

- **Fix temporary anti-shake solution for DX220**
  - Owner: Ammad, Muazzam
  - Status: Temporary solution requested (Jan 23), needs review and permanent fix
  - Priority: High priority

- **Document fasten torque for mobile printer screw (3.5~4kgf.cm)**
  - Owner: Ammad, Hieu
  - Status: Torque value received (Jan 28)
  - Priority: High priority - Documentation

- **Suggest removing upper lights to manager**
  - Owner: Tan, Kwanghyeop
  - Status: Two upper lights too bright, significantly affect depth quality (Jan 28)
  - Priority: High priority - Hardware optimization

- **Install metal FR3 finger base parts**
  - Owner: Muazzam, Ammad
  - Status: Parts received (Jan 28), ready for installation
  - Priority: High priority - Hardware installation

- **Change plate attachment from nut to plate**
  - Owner: Muazzam
  - Status: Plate received from Cheongju manufacturer (Jan 28)
  - Priority: High priority - Hardware modification

- **Integrate finger position to Omron camera system**
  - Owner: Ghulam Muhammd, Hieu
  - Status: Need to send finger position from robot side to mounted camera system (Jan 22)
  - Priority: High priority - Future enhancement

- **Work on identifying the state machine race condition**
  - Owner: Ammad, Hieu
  - Status: From CustomPendingTasks (Jan 20), race condition fixed (Jan 21)
  - Priority: Debug state machine issues

---

## 📋 Follow-up Required - Missing from Asana

- **Fix auto registration GUI bug (saving SVG issue) - Both systems**
  - Owner: Jalol
  - Status: Random bug prevents saving annotation results, blocks registration
  - Priority: Do later (not today), after manual registration issue fixed

- **Capture production data for vision model validation**
  - Owner: Vision team, Robot team
  - Status: Waiting for stable operation

- **Request samples for Label Printer**
  - Owner: Kwanghyeop
  - Status: Need to request from manager
  - Priority: For production testing

- **Request black body products for testing**
  - Owner: Kwanghyeop
  - Status: Requested (Jan 16), pending manager approval
  - Priority: Needed for comprehensive testing

- **Request more XD5-40D samples for testing**
  - Owner: Kwanghyeop
  - Status: Only 1 XD5-40D received (others were different models)
  - Priority: Needed for Monday demo preparation

- **Order one more metal mesh for the rubber foot**
  - Owner: Myeongun
  - Status: In progress
  - Priority: Need to order

- **Test nail gripper and roller mechanism**
  - Owner: Muazzam
  - Status: Pending
  - Priority: Needs testing

- **[screw] Robot finger with spring mechanism for PCB robot**
  - Owner: Ammad
  - Status: In progress
  - Priority: Needs completion

- **Prepare cushion support using profiles, joints, and install on top**
  - Owner: Ammad
  - Status: In progress
  - Priority: Needs installation

- **[screw] Adjustable Label printer aligner jig for worker placement**
  - Owner: Kwanghyeop
  - Status: In progress
  - Priority: Needs completion

---

## 🔍 Missing Items & Information Gaps - Missing from Asana

- **Complete vision model inventory**
  - Owner: Rizwan, Vision team
  - Status: Requested
  - Priority: Model names, versions, integration status, validation results

- **Camera and lighting setup documentation**
  - Owner: Vision team, Kwanghyeop
  - Status: Part of handover
  - Priority: Locations, mounting, specs, calibration

- **Complete equipment inventory with serial numbers**
  - Owner: Kwanghyeop
  - Status: In progress
  - Priority: Robots, controllers, cameras, grippers

- **Pending delivery items tracking**
  - Owner: Kwanghyeop
  - Status: Needs shared file
  - Priority: Safety covers, equipment, delivery dates

- **3D printed parts inventory**
  - Owner: Muazzam, Myeongun
  - Status: In progress
  - Priority: Components list, materials, spare parts status, tracking requested/printed/handed over

- **Operation manual completeness**
  - Owner: Kwanghyeop, team
  - Status: Part of handover
  - Priority: Startup, operation, shutdown procedures

- **Maintenance guide**
  - Owner: Kwanghyeop, team
  - Status: Part of handover
  - Priority: Preventive maintenance, troubleshooting

- **End-to-end system testing**
  - Owner: Team leads
  - Status: Needs scheduling
  - Priority: Full cycle testing, integration testing

- **Code repository documentation**
  - Owner: Development team
  - Status: May be missing
  - Priority: Branch structure, deployment, config

- **Environment setup documentation**
  - Owner: Backend team, Kwanghyeop
  - Status: May need update
  - Priority: Software, versions, installation, network

- **Product registration procedures**
  - Owner: Frontend, Backend
  - Status: May need update
  - Priority: Step-by-step guide, image capture, DB config

- **Error handling and recovery procedures**
  - Owner: Team leads
  - Status: Needs documentation
  - Priority: Warning types, recovery steps, escalation

- **Network infrastructure setup**
  - Owner: Kwanghyeop, Everint IT
  - Status: Requested, pending response
  - Priority: LAN connection, wifi router

- **Clear acceptance criteria definition**
  - Owner: Saad, Odil
  - Status: Requested Jan 14
  - Priority: What is "done", measurable targets

---

**Note:** These tasks are currently tracked in URGENT_ISSUES_CHECKLIST.md but are NOT present in Asana. Review each task and add to Asana if still needed, or mark as obsolete if no longer relevant.
