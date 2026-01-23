# Urgent Issues - Complete Tracking Checklist

**Last Updated:** January 23, 2026 (Based on Jan 22-23 updates)  
**Timezone:** Asia/Seoul (KST)

**Note:** PCB system is almost complete and running. Ammad (Robot/Framework) and Tan (Vision) are currently helping other robot systems (Hieu, Tugi) as additional resources.

---

## 🔴 Critical / Blocking Issues

```
📁 CRITICAL ISSUES
│
│ ┌─ REGISTRATION & SETUP (Highest Priority for Demo) ─┐
│ │
│ ├── 🔴 ⏳ Fix manual registration issue - Both systems (1st Priority)
│ │   └── Owner: Jalol | Status: GUI registration issue exists, Jalol fixing (Jan 22), Hieu did manual registration using existing name (SLP-DL413 instead of SLP-DX220) | CRITICAL for Monday demo
│ │
│ ├── 🔴 ⏳ Register all products with new code - Both systems
│ │   └── Owner: Hieu, Tugi, Quy Ninh | Status: Only 2 done (XD5-40D, XD3-40D), waiting for manual registration fix | CRITICAL for Monday demo
│ │
│ └──────────────────────────────────────────────────────┘
│
│ ┌─ HARDWARE & MECHANICAL (Blocks Production) ─┐
│ │
│ ├── 🔴 ⏳ Fix printer tilt - depth based angle adjustment while screwing (Screw Robot)
│ │   └── Owner: Ammad, Hieu | Status: Printer is tilted, causing bit offset after each screwing causing pick miss, also screw robot reset timeout (Jan 21) | CRITICAL - Urgent/Important
│ │
│ ├── 🔴 ⏳ Fix screw bit drift away from pickup position
│ │   └── Owner: Ammad, Hieu | Status: Screw bit occasionally drifts away from pickup position, suspected caused by unsmooth screwing in top-right screw hole (Jan 21) | CRITICAL - Blocks production
│ │
│ ├── 🔴 ⏳ Fix metal finger spacing issue
│ │   └── Owner: Myeongun, Muazzam | Status: Spacing not correct for fingers (Jan 22), need to add plastic sheet or thin flat washer | CRITICAL - Blocks production
│ │
│ ├── 🔴 ⏳ No spares for finger present
│ │   └── Owner: Myeongun, Muazzam | Status: Urgent/Important (Jan 21) | CRITICAL - Blocks production continuity
│ │
│ ├── 🔴 ⏳ Install dedicated bracket for screw mirror (fixed and repeatable position)
│ │   └── Owner: Muazzam, Ammad | Status: Magnetic base bracket unstable due to vibration, dedicated bracket required (Jan 21) | CRITICAL - Mirror critical for detecting tilts
│ │
│ ├── 🔴 ⏳ Complete 2D camera hardware installation
│ │   └── Owner: Muazzam, Ammad | Status: Hardware installation incomplete | Blocks full system functionality
│ │
│ ├── 🔴 ⏳ Request continuous roll rubber pad sheets (8xN instead of 8x8)
│ │   └── Owner: Kwanghyeop, Shoaib | Status: Current small sheets cause jam in roller area, need continuous roll for smooth operation (Jan 22) | CRITICAL - Improves reliability
│ │
│ ├── 🔴 ⏳ Conveyor position adjustment / fix (1st Priority)
│ │   └── Owner: Ammad | Status: CRITICAL for Monday demo | Affects product positioning
│ │
│ ├── 🔴 ⏳ Fix out of place product on conveyor causing collision
│ │   └── Owner: Ammad, Hieu | Status: Products misaligned causing collision/damage | Solution: Use top camera to detect product within acceptable zone
│ │
│ └──────────────────────────────────────────────────────┘
│
│ ┌─ VISION & DETECTION (Blocks Production Quality) ─┐
│ │
│ ├── 🔴 ⏳ Fix screw pickup validation - Label Printer Screw Robot (2nd screw feeder FPs)
│ │   └── Owner: Hieu, Haider Shah, Rizwan | Status: Model 2 screw validation updated (Jan 19-20), 1-2 false negatives remain, Sajad fixing | Blocks production
│ │
│ ├── 🔴 ⏳ Fix rubber foot ROI detection (tighter mechanism issue)
│ │   └── Owner: Rizwan, Hieu | Status: User ROI from GUI good, but tighter mechanism makes it wrong | Blocks accurate detection
│ │
│ ├── 🔴 ⏳ Test rescan logic (Rubber Foot Robot) (2nd Priority)
│ │   └── Owner: Tugi | Status: Tested (Jan 19-20), rolled back due to issues, vision team working on fixes | Affects reliability
│ │
│ ├── 🔴 ⏳ Integrate rubber pad pickup offset - Label Printer Rubber Foot Robot (2nd Priority)
│ │   └── Owner: Tugi | Status: Pending integration | Affects pickup accuracy
│ │
│ ├── 🔴 ⏳ Integrate Omron camera vision system (top camera) - Screw Robot
│ │   └── Owner: Ghulam Muhammd, Hieu | Status: PR #136, #141 merged with README (Jan 22), needs integration and testing | CRITICAL - Collision detection
│ │
│ ├── 🔴 ⏳ Integrate misalignment warning for rubber foot attachment
│ │   └── Owner: Rizwan, Tugi | Status: Misalignment argument already shared, initial version added and returned during inference but not currently used by robot side (Jan 22) | CRITICAL - Quality control
│ │
│ └──────────────────────────────────────────────────────┘
│
│ ┌─ SOFTWARE & SYSTEM STABILITY ─┐
│ │
│ ├── 🔴 ⏳ Ensure GUI parameter stability (values remain unchanged)
│ │   └── Owner: Jalol, Sawera | Status: Need to ensure GUI parameters remain unchanged during operation and across execution cycles (Jan 22) | CRITICAL - System stability
│ │
│ └──────────────────────────────────────────────────────┘
```
│
├── 🔴 ✅ Vision integration - Label Printer Screw Robot
│   └── Owner: Hieu, Rizwan | Status: Complete (Jan 15) | Vision integration done
│
├── 🔴 ✅ Fix pad holding bracket - Label Printer Rubber Foot Robot
│   └── Owner: Tugi | Status: Complete | Bracket installed
│
├── 🔴 ✅ Self Training update - Label Printer Rubber Foot Robot
│   └── Owner: Rizwan | Status: Complete | Self training update done
│
├── 🔴 ✅ Provide dataset for 20+ runs to vision team - Label Printer Screw Robot (1st Priority)
│   └── Owner: Hieu | Status: Complete (Jan 17) | XD5-40dc images captured and shared
│
├── 🔴 ✅ Perform hand eye calibration - Label Printer Rubber Foot Robot (1st Priority)
│   └── Owner: Tugi | Status: Complete (Jan 17) | Calibration done, parameters tuned
│
├── 🔴 ✅ Send last 2 days dataset to vision team - Label Printer Rubber Foot Robot (1st Priority)
│   └── Owner: Tugi, Quy Ninh | Status: Complete (Jan 17) | Dataset with rubber foot partially attached uploaded to NAS
│
├── 🔴 ✅ Display error messages - Label Printer Screw Robot (1st Priority)
│   └── Owner: Hieu, Tugi | Status: Complete (Jan 17) | Error/warning message display code implemented, Jalol needs to make changes
│
├── 🔴 ✅ Display error messages - Label Printer Rubber Foot Robot (1st Priority)
│   └── Owner: Tugi | Status: Complete (Jan 17) | Error/warning message display code implemented, Jalol needs to make changes (GUI reset needed)
│
├── 🔴 ✅ Self training merged and tested - Label Printer Screw Robot
│   └── Owner: Hieu, Rizwan | Status: Complete (Jan 17) | Tested for 1 printer registration (file saving issue identified)
│
├── 🔴 ✅ Auto registration process working - Label Printer Screw Robot
│   └── Owner: Quy Ninh | Status: Complete (Jan 17) | Working on screwdriver robot
│
├── 🔴 ✅ Conveyor teaching completed
│   └── Owner: Hieu | Status: Complete (Jan 17) | Manager finished teaching (took longer due to issues)
│
├── 🔴 ✅ Screw driver replacement
│   └── Owner: Hieu | Status: Complete (Jan 17) | Replaced wobbling screw driver with new one
│
├── 🔴 ✅ Install second magnet/spring on screw bit - Label Printer Screw Robot (2nd Priority)
│   └── Owner: Ammad, Hieu | Status: Complete (Jan 17) | Silver magnet on screw bit, orange magnet in box
│
├── 🔴 ✅ Fixed move up logic when abort/timeout - Label Printer Screw Robot
│   └── Owner: Hieu | Status: Complete (Jan 17) | Fixed logic when abort signal or timeout while fastening screws
│
├── 🔴 ✅ 3D printed spares ordered (2 sets FR3 fingers, RubberPad Base Plate, Scooping Fingers)
│   └── Owner: Myeongun | Status: Complete (Jan 17) | 2 sets (4ea) with 100% infill base
│
└── 🔴 ✅ JRT gripper prepared as backup
    └── Owner: Muazzam | Status: Complete (Jan 17) | Backup gripper ready
│
├── 🔴 ✅ Screw pickup issue resolved - Label Printer Screw Robot
│   └── Owner: Hieu, Ammad, Muazzam | Status: Complete (Jan 19-20) | Adjusted pickup speed, filed screw bit for better fit, lowered checking position
│
├── 🔴 ✅ Holes detection fixed - Label Printer Screw Robot
│   └── Owner: Hieu, Shams | Status: Complete (Jan 19-20) | Fixed by changing reference image for XD5-40dc
│
├── 🔴 ✅ Model 2 screw validation code updated - Label Printer Screw Robot
│   └── Owner: Hieu | Status: Complete (Jan 19-20) | Updated and tested, some fail cases need tuning
│
├── 🔴 ✅ Removed moveXB when moving to fastening position - Label Printer Screw Robot
│   └── Owner: Hieu | Status: Complete (Jan 19-20) | Removed to avoid non-reaching issue
│
├── 🔴 ✅ Adjusted fastening angle of screw driver - Label Printer Screw Robot
│   └── Owner: Hieu | Status: Complete (Jan 19-20) | Angle adjusted for better fastening
│
├── 🔴 ✅ Changed vacuum suction cup spring (thicker one) - Label Printer Rubber Foot Robot
│   └── Owner: Tugi | Status: Complete (Jan 19-20) | Spring replaced with thicker one
│
├── 🔴 ✅ Vacuum gripper operation restored - Label Printer Rubber Foot Robot
│   └── Owner: Tugi | Status: Complete (Jan 19-20) | Previously air was leaking inside, now fixed
│
├── 🔴 ✅ Vacuum box cleaned and sealed - Label Printer Rubber Foot Robot
│   └── Owner: Tugi | Status: Complete (Jan 19-20) | Cleaned debris inside vacuum box and sealed properly, suction improved
│
├── 🔴 ✅ Rescan logic tested - Label Printer Rubber Foot Robot
│   └── Owner: Tugi, Rizwan | Status: Complete (Jan 19-20) | Tested with latest code, rolled back due to issues, PR #129 merged for improvements
│
├── 🔴 ✅ Fairino fingers Option B printed
│   └── Owner: Myeongun | Status: Complete (Jan 19) | All Option B fingers printed
│
└── 🔴 ✅ Vision PRs merged for rubber foot detection improvements
    └── Owner: Rizwan, Tugi | Status: Complete (Jan 19) | PR #125, #126, #129 merged for rubber foot attachment and detection improvements
│
├── 🔴 ✅ State machine race condition fixed - Label Printer Screw Robot
│   └── Owner: Hieu | Status: Complete (Jan 21) | Race condition issue pointed out and fixed
│
├── 🔴 ✅ State machine issue resolved - Label Printer Screw Robot
│   └── Owner: Ammad | Status: Complete (Jan 21) | State machine issue resolved
│
├── 🔴 ✅ Screw pick improvement & troubleshooting - Label Printer Screw Robot
│   └── Owner: Ammad | Status: Complete (Jan 21) | Troubleshooting why in test bench work but assembly misses screw
│
├── 🔴 ✅ Speeding of xb to feeder and from feeder - Label Printer Screw Robot
│   └── Owner: Ammad | Status: Complete (Jan 21) | Movement speed optimized
│
├── 🔴 ✅ Addition of image capture before gripper using camera - Label Printer Screw Robot
│   └── Owner: Ammad, Hieu | Status: Complete (Jan 21) | Sending MQTT msg to capture image from Omron camera
│
├── 🔴 ✅ Addition of buzzer to inform system start and finished - Label Printer Screw Robot
│   └── Owner: Ammad | Status: Complete (Jan 21) | Buzzer added to inform system status
│
├── 🔴 ✅ Addition of screw tilt mirror - Label Printer Screw Robot
│   └── Owner: Ammad | Status: Complete (Jan 21) | Mirror added (temporary magnetic base, needs dedicated bracket)
│
├── 🔴 ✅ Improved logic when picking screw for next cycle - Label Printer Screw Robot
│   └── Owner: Hieu | Status: Complete (Jan 21) | Logic improved
│
├── 🔴 ✅ Optimized movements - Label Printer Screw Robot
│   └── Owner: Hieu | Status: Complete (Jan 21) | Still using move XB but always use moveL to target points
│
├── 🔴 ✅ Scoop image feature after scooping rubber foot - Label Printer Rubber Foot Robot
│   └── Owner: Tan | Status: Complete (Jan 20) | Move home => save image again, path: Data/scoop_images/Datetime
│
├── 🔴 ✅ Recent Images manager feature - Label Printer Rubber Foot Robot
│   └── Owner: Tan | Status: Almost complete (Jan 20) | Save recent image and svg in recent folder, need to filter type of image
│
├── 🔴 ✅ Omron camera vision system implemented - Collision detection
│   └── Owner: Ghulam Muhammd | Status: Complete (Jan 21) | Robot-triggered top-camera vision system to detect collisions, cycle time ~50ms
│
└── 🔴 ✅ Production run - 60+ products assembled
    └── Owner: Hieu, Ammad | Status: Complete (Jan 21) | Product ran in continuous sessions, total more than 60 (4 carts)
│
├── 🔴 ✅ Installed scooping pad on acrylic table - Label Printer Rubber Foot Robot
│   └── Owner: Tugi | Status: Complete (Jan 22) | Scooping pad installed
│
├── 🔴 ✅ Added vibration functionality to assist pickup rubber - Label Printer Rubber Foot Robot
│   └── Owner: Tugi | Status: Complete (Jan 22) | Vibration assists aligning rubber feet with suction cup
│
├── 🔴 ✅ Claw based scooping operation implemented - Label Printer Rubber Foot Robot
│   └── Owner: Tugi | Status: Complete (Jan 22) | Implemented in main robot framework with flag to switch between 2 methods
│
├── 🔴 ✅ Collected dataset for rubber pickup from scooping pad - Label Printer Rubber Foot Robot
│   └── Owner: Tugi | Status: Complete (Jan 22) | Dataset collected, path: /home/gpuadmin/DATA/New_Pad_scoop_images, need new algorithm for single row detection
│
├── 🔴 ✅ Metal gripper finger prepared - Label Printer Rubber Foot Robot
│   └── Owner: Tugi, Muazzam | Status: Complete (Jan 22) | Prepared by adding foam and green tape, not tested yet
│
├── 🔴 ✅ Fixed MQTT port issue (disabled linux ufw) - Both systems
│   └── Owner: Ammad | Status: Complete (Jan 22) | All ports MQTT 1883 and 8883 are now open
│
├── 🔴 ✅ Installed mirror for screw validation - Label Printer Screw Robot
│   └── Owner: Hieu, Ammad, Odil | Status: Complete (Jan 22) | Temporarily installed, ran XLP-TX420 and SLP-TX400 printers with mirror reflection
│
├── 🔴 ✅ Manual registration done for SLP-DX220 - Label Printer Screw Robot
│   └── Owner: Hieu | Status: Complete (Jan 22) | Used existing name SLP-DL413 instead of real name SLP-DX220 due to GUI issue
│
├── 🔴 ✅ Top camera vision system PR merged with README - Screw Robot
│   └── Owner: Ghulam Muhammd | Status: Complete (Jan 22) | PR #136, #141 merged, README added, needs integration
│
└── 🔴 ✅ Attached scooping claw on suction gripper and tested - Label Printer Rubber Foot Robot
    └── Owner: Tugi | Status: Complete (Jan 22) | Tested scoop and rubber pickup
│
├── 🔴 ✅ Fix rubber foot attachment position error (Rubber Foot Robot)
│   └── Owner: Tugi, Rizwan | Status: Complete (Jan 23) | Fixed
│
├── 🔴 ✅ Fix fragile Fairino fingers bending when gripping (Both systems)
│   └── Owner: Ammad, Myeongun | Status: Complete (Jan 23) | Fixed with metal/inward bent fingers
│
├── 🔴 ✅ Debug screwdriver robot moving slow
│   └── Owner: Hieu, Ammad | Status: Complete (Jan 23) | Fixed
│
├── 🔴 ✅ Investigate and fix screw pickup tilting
│   └── Owner: Hieu, Ammad | Status: Complete (Jan 23) | Fixed
│
├── 🔴 ✅ Fix screw speed issue - Label Printer Screw Robot (1st Priority)
│   └── Owner: Hieu, Ammad | Status: Complete (Jan 23) | Fixed
│
├── 🔴 ✅ Fix self training file saving issue (path format)
│   └── Owner: Haider Shah | Status: Complete (Jan 23) | Fixed using os.path
│
├── 🔴 ✅ Fix robot speed in timeout/collision (clean_up function)
│   └── Owner: Ammad | Status: Complete (Jan 23) | Fixed
│
├── 🔴 ✅ Calibrate placement position - Label Printer Rubber Foot Robot (1st Priority)
│   └── Owner: Tugi, Muazzam, Tan | Status: Complete (Jan 23) | Calibration done and fine-tuned
│
├── 🔴 ✅ Get robot to place rubber foot in correct position - Label Printer Rubber Foot Robot (1st Priority)
│   └── Owner: Tugi | Status: Complete (Jan 23) | Placement working correctly
│
├── 🔴 ✅ Integrate new vision code PR - Both systems
│   └── Owner: Hieu, Rizwan | Status: Complete (Jan 23) | Integrated
│
├── 🔴 ✅ Register XD5-40D with new code - Both systems
│   └── Owner: Hieu, Tugi | Status: Complete (Jan 23) | Registered
│
├── 🔴 ✅ Fix tilted screw issue - Label Printer Screw Robot (2nd Priority)
│   └── Owner: Ammad, Hieu | Status: Complete (Jan 23) | Fixed - adjusted pickup speed, filed screw bit, lowered checking position
│
├── 🔴 ✅ Integrate rescan logic - Label Printer Rubber Foot Robot (2nd Priority)
│   └── Owner: Tugi, Rizwan | Status: Complete (Jan 23) | Integrated with PR #129 improvements
│
├── 🔴 ✅ Recapture reference images for all products (FR3 holding, not pressing arm)
│   └── Owner: Tugi, Hieu, Odil | Status: Complete (Jan 23) | Reference images recaptured
│
├── 🔴 ✅ Confirm cycle time - Label Printer Screw Robot
│   └── Owner: Hieu, Saad | Status: Complete (Jan 23) | Cycle time confirmed
│
├── 🔴 ✅ Confirm cycle time - Label Printer Rubber Foot Robot
│   └── Owner: Tugi, Saad | Status: Complete (Jan 23) | 30s including rescan/validation confirmed
│
├── 🔴 ✅ Fix state machine execution issues (Multiple command queue, screwpick missing)
│   └── Owner: Ammad, Hieu | Status: Complete (Jan 23) | Race condition fixed, state machine issue resolved
│
├── 🔴 ✅ Fix issues when start signal comes before completing cycle
│   └── Owner: Hieu, Ammad | Status: Complete (Jan 23) | Fixed
│
├── 🔴 ✅ Fix screw validation for model 2 (distinguish fail cases with same detection as normal)
│   └── Owner: Haider Shah, Hieu | Status: Complete (Jan 23) | Fixed
│
├── 🔴 ✅ Fix false negative in screw tilt detection
│   └── Owner: Haider Shah, Hieu | Status: Complete (Jan 23) | Fixed
│
├── 🔴 ✅ Fix screw bit mis-grip issue (strikes screw head with force, remains stuck on edge)
│   └── Owner: Ammad, Hieu | Status: Complete (Jan 23) | Fixed
│
├── 🔴 ✅ Fix rubber foot attachment incorrect 
│   └── Owner: Tugi, Rizwan | Status: Complete (Jan 23) | Fixed
│
├── 🔴 ✅ New metal finger are not assembled & tested
│   └── Owner: Muazzam, Ammad | Status: Complete (Jan 23) | Metal gripper finger prepared and tested
│
├── 🔴 ✅ Find a way to drop screw near pick position (electromagnet)
│   └── Owner: Ammad, Muazzam | Status: Complete (Jan 23) | Solution implemented
│
├── 🔴 ✅ Fix left side blur and brightness issue in camera images
│   └── Owner: Rizwan, Hieu | Status: Complete (Jan 23) | Fixed
│
├── 🔴 ✅ Add printer config files to different folder to prevent overwriting during PR merge
│   └── Owner: Hieu | Status: Complete (Jan 23) | Implemented
│
├── 🔴 ✅ Fix pad pickup failure - Label Printer Rubber Foot Robot
│   └── Owner: Tugi, Muazzam | Status: Complete (Jan 23) | Fixed
│
├── 🔴 ✅ Fix claw scooping issue - first row plastic sheet not going under nail
│   └── Owner: Tugi, Muazzam | Status: Complete (Jan 23) | Fixed
│
├── 🔴 ✅ Fix Rainbow control box bugs (PWM and gripper speed/force adjustment)
│   └── Owner: Kwanghyeop, Ammad | Status: Complete (Jan 23) | Fixed
│
└── 🔴 ✅ Retrain model after metal finger change
    └── Owner: Hieu, Vision team | Status: Complete (Jan 23) | Model retrained
```

---

## 🟡 High Priority Issues

```
📁 HIGH PRIORITY ISSUES
│
├── 🟡 ⏳ Improve calibration accuracy (Rubber Foot Robot)
│   └── Owner: Tugi | Status: Needed to reduce position error | Critical for attachment accuracy
│
├── 🟡 ⏳ Method to overcome irregularities in rubber foot shape
│   └── Owner: Tugi | Status: Need solution for irregular rubber foot shape | Affects attachment quality
│
├── 🟡 ⏳ Speed up robot movements to meet cycle time - Label Printer Screw Robot (3rd Priority)
│   └── Owner: Hieu | Status: After 1st priority tasks | Blocks cycle time targets
│
├── 🟡 ✅ Integrate self-training model - Label Printer Screw Robot (3rd Priority)
│   └── Owner: Hieu | Status: Complete (Jan 17) | Self training integrated and tested
│
├── 🟡 ⏳ Speed up movements to meet cycle time - Label Printer Rubber Foot Robot (3rd Priority)
│   └── Owner: Tugi, Shoaib | Status: After 1st priority tasks | Blocks cycle time targets
│
├── 🟡 ⏳ Integrate self training logic - Label Printer Rubber Foot Robot (3rd Priority)
│   └── Owner: Tugi | Status: After 1st priority tasks | In progress
│
├── 🟡 ⏳ Install buzzers for error/warning display (2nd Priority)
│   └── Owner: Muazzam, Ammad | Status: Need to install | Required for production monitoring
│
├── 🟡 ⏳ Redesign fingers for Fairino to improve gripping (2nd Priority)
│   └── Owner: Saad, Myeongun | Status: Need metal/inward bent fingers | Critical for production quality
│
├── 🟡 ⏳ Install vertical plates to make screws straight - Label Printer Screw Robot (2nd Priority)
│   └── Owner: Ammad, Hieu | Status: Not done (Jan 17) | Blocks reliability
│
├── 🟡 ⏳ Integrate buzzer alarm - Both systems (3rd Priority)
│   └── Owner: Ammad, Hieu, Tugi | Status: After 1st priority tasks | Required for production monitoring
│
├── 🟡 ⏳ Installation of remaining hardware according to government report (3rd Priority)
│   └── Owner: Muazzam, Ammad | Status: After 1st priority tasks | Required for full functionality
│
├── 🟡 ⏳ Install all cameras and equipment from hardware purchase list
│   └── Owner: Muazzam, Ammad | Status: 2D camera pending | Required for full functionality
│
├── 🟡 ⏳ Use product size information while tightening YOLO bbox
│   └── Owner: Rizwan, Haider Shah | Status: Need to use user-inserted product size | Prevents detecting black cushion with printer body
│
├── 🟡 ⏳ Maintain history of detection sizes for tighter bboxes
│   └── Owner: Rizwan, Haider Shah | Status: Need to maintain average of last n detections | Improves detection accuracy
│
├── 🟡 ⏳ Analyze Omron camera images to detect wrong displacement of printers (after camera installation)
│   └── Owner: Shams, Odil | Status: New task assigned (Jan 17) | Critical for product positioning
│
├── 🟡 ⏳ Finalize GUI for PCB/Screw/Rubber
│   └── Owner: Jalol | Status: Delay non-urgent tasks, finish urgent issues for Monday demo | Deadline: Sunday morning shift
│
├── 🟡 ⏳ Make changes to error message display (GUI side) - Both systems
│   └── Owner: Jalol | Status: Hieu and Tugi completed framework side, Jalol needs to make GUI changes | CRITICAL for Monday demo
│
├── 🟡 ⏳ Fix rubber foot ROI detection (tighter mechanism issue)
│   └── Owner: Rizwan, Hieu | Status: User ROI from GUI good, but tighter mechanism makes it wrong | Blocks accurate detection
│
├── 🟡 ⏳ Fix conveyor operation guide
│   └── Owner: Ammad, Tan | Status: Guide created (Jan 18), need to ensure proper operation | Affects system operation
│
├── 🟡 ⏳ Use Omron camera to detect mis-attachment of rubber foot
│   └── Owner: Odil, Rizwan | Status: RealSense may not give clean view, Omron can provide better detection | After camera installation
│
├── 🟡 ⏳ Train lightweight detector for product presence (Omron camera)
│   └── Owner: Odil | Status: Check if product is present and within safe gripping area | After camera installation
│
├── 🟡 ⏳ Organize images in cleaner format (product folder structure)
│   └── Owner: Odil, Shoaib | Status: Currently 5-6 images per product, arrange in product ID folders | Improves organization
│
├── 🟡 ⏳ Install mirror for model 2 (screw robot)
│   └── Owner: Haider Shah, Shams | Status: Shams started but couldn't finish (Jan 19), Haider can do if robot team busy | Required for model 2 detection
│
├── 🟡 ⏳ Capture scooped rubber foot images after scooping
│   └── Owner: Tugi, Hieu | Status: Not capturing currently, Haider says necessary (scooping may change position) | Required for vision model improvement
│
├── 🟡 ⏳ Test rolling/gripper based rubber pickup mechanism
│   └── Owner: Ammad, Muazzam | Status: Deadline: Thursday lunch time (Jan 23), need ready to install 3D printed working version | Alternative pickup mechanism
│
├── 🟡 ⏳ Prepare complete spare for vacuum box with motor
│   └── Owner: Tugi, Ammad, Muazzam | Status: Requested (Jan 20), need complete spare ready if using current mechanism for more than a week | Critical for production continuity
│
├── 🟡 ⏳ Order screw bits
│   └── Owner: Kwanghyeop | Status: Requested by Ammad (Jan 19) | Need to order replacement bits
│
├── 🟡 ⏳ Work on new rubber pad design
│   └── Owner: Tugi, Muazzam | Status: From CustomPendingTasks | Alternative design for rubber pad pickup
│
├── 🟡 ⏳ Link screw/rubber robots to pre-pickup the rubber pad
│   └── Owner: Tugi, Hieu | Status: From CustomPendingTasks | Optimization for cycle time
│
├── 🟡 ⏳ Take rubber pad pictures every cycle and after scooping / integrate rubber pad offset
│   └── Owner: Tugi, Rizwan | Status: From CustomPendingTasks | Required for vision model improvement
│
├── 🟡 ⏳ Bit alignment jig after screwing (improvisation oiling and spring insertion)
│   └── Owner: Ammad, Muazzam | Status: Remaining task (Jan 21) | Improve bit alignment
│
├── 🟡 ⏳ Addition of add_command parameter XB motion different blending types and blending distance option
│   └── Owner: Ammad | Status: Remaining task (Jan 21) | Framework improvement
│
├── 🟡 ⏳ Addition of one extra linear point to blend distance zero so it reaches actual position
│   └── Owner: Ammad | Status: Remaining task (Jan 21) | Framework improvement
│
├── 🟡 ⏳ Addition of add_command function parameter for setting each motion tolerance
│   └── Owner: Ammad | Status: Remaining task (Jan 21) | Framework improvement - set different tolerances for different motions
│
├── 🟡 ⏳ Increasing speed of Fairino robot up and down
│   └── Owner: Ammad | Status: Remaining task (Jan 21) | Performance improvement
│
├── 🟡 ⏳ Screw feeder empty issue
│   └── Owner: Ammad, Muazzam | Status: Remaining task (Jan 21) | Handle empty feeder condition
│
├── 🟡 ⏳ Duration based signal stop
│   └── Owner: Ammad | Status: Remaining task (Jan 21) | Important - Signal handling improvement
│
├── 🟡 ⏳ Reduce cycle time, find area to improve
│   └── Owner: Hieu, Ammad | Status: Remaining task (Jan 21) | Performance optimization
│
├── 🟡 ⏳ Pause functionality (debugging and saving product from damage)
│   └── Owner: Ammad, Hieu | Status: Remaining task (Jan 21) | Important - Safety feature
│
├── 🟡 ⏳ Conveyor signal testing - magnetic switch on pneumatic
│   └── Owner: Ammad, Hieu | Status: Magnetic switch on pneumatic used at set position but set to max reach point (Jan 21) | Signal handling
│
├── 🟡 ⏳ Test rubber foot attachment extensively with latest updated code
│   └── Owner: Tugi, Tan, Rizwan | Status: Need extensive testing, need feedback from robot side (Jan 22) | High priority
│
├── 🟡 ⏳ Contact manufacturer to lengthen one side of rubber pad
│   └── Owner: Kwanghyeop, Shoaib | Status: Need to contact manufacturer to lengthen one side for smooth scooping operation (Jan 22) | High priority
│
├── 🟡 ⏳ Contact Rainbow about control box bugs
│   └── Owner: Kwanghyeop | Status: Need to contact Rainbow about PWM and gripper speed/force adjustment bugs (Jan 22) | High priority
│
├── 🟡 ⏳ Test metal fingers with new model
│   └── Owner: Tugi, Muazzam | Status: Metal fingers prepared but not tested, need retraining after finger change (Jan 22) | High priority
│
├── 🟡 ⏳ Integrate finger position to Omron camera system
│   └── Owner: Ghulam Muhammd, Hieu | Status: Need to send finger position from robot side to mounted camera system (Jan 22) | High priority - Future enhancement
│
├── 🟡 ⏳ Work on identifying the state machine race condition
│   └── Owner: Ammad, Hieu | Status: From CustomPendingTasks (Jan 20), race condition fixed (Jan 21) | Debug state machine issues
│
├── 🟡 ⏳ Fix screw validation logic (range and tilt angle)
│   └── Owner: Hieu, Haider Shah | Status: Multiple false positive/negative cases, need range-based logic | Blocks production
│
├── 🟡 ⏳ Use start/abort signal from conveyor PLC
│   └── Owner: Saad | Status: Combine with vision to determine if no printer | After camera installation
│
├── 🟡 ⏳ Prepare checkerboards and Aruco codes for calibration
│   └── Owner: Tan | Status: Print two more checkerboards and two Aruco codes | For calibration support
│
├── 🟡 ⏳ Bring new ethernet cables from lab
│   └── Owner: Ammad | Status: Current one not stable, sometimes disconnects | Blocks stable connection
│
├── 🟡 ⏳ Ensure spares for each 3D printed part
│   └── Owner: Muazzam, Myeongun | Status: In progress | Critical for production continuity
│
├── 🟡 ⏳ Create Excel file - GUI tasks and issues status
│   └── Owner: Jalol | Deadline: Jan 15, 2026 | Status: In progress, adding GUI & vision columns
│
├── 🟡 ⏳ Collect dataset for vision model testing
│   └── Owner: Rizwan, Shams, Tugi, Hieu | Status: Waiting for stable operation | Blocks validation
│
├── 🟡 ⏳ Complete vision model validation summary
│   └── Owner: Rizwan | Status: In progress | Required for handover
│
├── 🟡 ⏳ Equipment list (installed and pending delivery)
│   └── Owner: Kwanghyeop | Status: Uploaded to OneDrive (Jan 16), needs verification | Missing items may delay handover
│
├── 🟡 ⏳ 3D parts list
│   └── Owner: Muazzam, Ammad | Status: Shared Google Sheet (Jan 16) | Critical for tracking components
│
├── 🟡 ⏳ Maintain 3D components tracking list (requested/printed/handed over)
│   └── Owner: Myeongun | Status: In progress | Track all 3D component requests
│
├── 🟡 ⏳ Finger replacement - Label Printer Rubber Foot Robot
│   └── Owner: Tugi, Myeongun | Status: Spare fingers prepared (Jan 16) | Ready for replacement
│
│
├── 🟡 ✅ Fix GUI freezing/halt and slow issues (Label Printer)
│   └── Owner: Jalol | Status: Complete (Jan 16) | GUI problems solved
│
├── 🟡 ✅ Label Printer registration automation (GUI side)
│   └── Owner: Jalol | Status: Complete (Jan 16) | Registration automation completed
│
├── 🟡 ✅ Green sheet installation (Rubber Foot Robot)
│   └── Owner: Tugi, Ammad | Status: Complete (Jan 16) | Installation completed and working
│
├── 🟡 ✅ Spare fingers preparation (2 pairs FR3)
│   └── Owner: Muazzam, Ammad | Status: Complete (Jan 16) | Spare fingers ready
│
├── 🟡 ✅ Rubber pad platform installation
│   └── Owner: Muazzam | Status: Complete (Jan 16) | Platform installed
│
├── 🟡 ✅ FR3 teaching on screwdriver table
│   └── Owner: Muazzam | Status: Complete (Jan 16) | Installation and teaching done
│
├── 🟡 ✅ Rubber pad scooping position adjustment
│   └── Owner: Muazzam, Tugi | Status: Complete (Jan 16) | Position adjusted
│
├── 🟡 ✅ MoveXB integration
│   └── Owner: Hieu | Status: Complete (Jan 16) | Integrated and smoothly running
│
├── 🟡 ✅ Production run (~30 products)
│   └── Owner: Hieu, Tugi | Status: Complete (Jan 16) | Production tested
│
├── 🟡 ✅ Model integration tested successfully
│   └── Owner: Hieu, Rizwan | Status: Complete (Jan 16) | Holes and rubber detecting/verifying merged and tested
│
├── 🟡 ✅ Hand-eye calibration parameters tuned
│   └── Owner: Tugi, Hieu | Status: Complete (Jan 16) | Parameters tuned for accurate pad placing
│
├── 🟡 ✅ Rubber pad detection models integrated and tested
│   └── Owner: Tugi, Rizwan | Status: Complete (Jan 16) | Models integrated and tested
│
├── 🟡 ✅ Self training framework tested
│   └── Owner: Tugi | Status: Complete (Jan 16) | Tested after registration
│
├── 🟡 ✅ Complete Screw Driver Robot fingers installation - Label Printer Screw Robot
│   └── Owner: Ammad, Myeongun | Status: Complete (Jan 15) | Fingers installation done
│
├── 🟡 ✅ Hardware installation - Label Printer Screw Robot
│   └── Owner: Muazzam, Hieu | Status: Complete (Jan 15) | Hardware installation done
│
├── 🟡 ✅ Hardware installation - Label Printer Rubber Foot Robot
│   └── Owner: Muazzam, Tugi | Status: Complete (Jan 15) | Hardware installation done
│
├── 🟡 ✅ Rubber pad pickup - Label Printer Rubber Foot Robot
│   └── Owner: Tugi | Status: Complete (Jan 15) | Rubber pad pickup successful
│
├── 🟡 ✅ Rubber pad validation model update - Label Printer Rubber Foot Robot
│   └── Owner: Rizwan | Status: Complete (Jan 15) | Model updated
│
├── 🟡 ✅ Prepare complete test bench with Hieu for label printer
│   └── Owner: Tan | Status: Completed (Asana) | Test bench ready
│
├── 🟡 ✅ Test OBB DETR model for PCB detection
│   └── Owner: Tan | Status: Completed (Asana) | PCB detection model tested
│
└── 🟡 ✅ Define list of targets for Everint project acceptance
    └── Owner: Saad, Odil | Status: Complete | Targets defined
```

---

## 🟢 Important / Low Priority Issues

```
📁 IMPORTANT ISSUES
│
└── 🟢 ⏳ Complete handover documentation package
    └── Owner: Kwanghyeop | Status: Not started yet | Tasks created in Asana but work not begun
    └──   ├── System Operation Documentation ⏳
    └──   ├── Maintenance Documentation ⏳
    └──   ├── Equipment & Hardware List ⏳
    └──   ├── Vision System Documentation ⏳
    └──   ├── Software & System Overview ⏳
    └──   └── Handover & Ownership Information ⏳
    └── Additional: Jalol creating registration guide, Sawera preparing manuals
```

---

## 📋 Follow-up Required

```
📁 FOLLOW-UP REQUIRED
│
├── 📋 ⏳ Fix auto registration GUI bug (saving SVG issue) - Both systems
│   └── Owner: Jalol | Status: Random bug prevents saving annotation results, blocks registration | Do later (not today), after manual registration issue fixed
│
├── 📋 ⏳ Capture production data for vision model validation
│   └── Owner: Vision team, Robot team | Status: Waiting for stable operation
│
├── 📋 ⏳ Request samples for Label Printer 
│   └── Owner: Kwanghyeop | Status: Need to request from manager | For production testing
│
├── 📋 ⏳ Request black body products for testing
│   └── Owner: Kwanghyeop | Status: Requested (Jan 16), pending manager approval | Needed for comprehensive testing
│
├── 📋 ⏳ Request more XD5-40D samples for testing
│   └── Owner: Kwanghyeop | Status: Only 1 XD5-40D received (others were different models) | Needed for Monday demo preparation
│
├── 📋 ⏳ Order one more metal mesh for the rubber foot
│   └── Owner: Myeongun | Status: In progress | Need to order
│
├── 📋 ⏳ Test nail gripper and roller mechanism
│   └── Owner: Muazzam | Status: Pending | Needs testing
│
├── 📋 ⏳ [screw] Robot finger with spring mechanism for PCB robot
│   └── Owner: Ammad | Status: In progress | Needs completion
│
├── 📋 ⏳ Prepare cushion support using profiles, joints, and install on top
│   └── Owner: Ammad | Status: In progress | Needs installation
│
├── 📋 ⏳ [screw] Adjustable Label printer aligner jig for worker placement
│   └── Owner: Kwanghyeop | Status: In progress | Needs completion

```

---

## 🔍 Missing Items & Information Gaps

```
📁 MISSING ITEMS & GAPS
│
├── 🔍 ⏳ Complete vision model inventory
│   └── Owner: Rizwan, Vision team | Status: Requested | Model names, versions, integration status, validation results
│
├── 🔍 ⏳ Camera and lighting setup documentation
│   └── Owner: Vision team, Kwanghyeop | Status: Part of handover | Locations, mounting, specs, calibration
│
├── 🔍 ⏳ Complete equipment inventory with serial numbers
│   └── Owner: Kwanghyeop | Status: In progress | Robots, controllers, cameras, grippers
│
├── 🔍 ⏳ Pending delivery items tracking
│   └── Owner: Kwanghyeop | Status: Needs shared file | Safety covers, equipment, delivery dates
│
├── 🔍 ⏳ 3D printed parts inventory
│   └── Owner: Muazzam, Myeongun | Status: In progress | Components list, materials, spare parts status, tracking requested/printed/handed over
│
├── 🔍 ⏳ Operation manual completeness
│   └── Owner: Kwanghyeop, team | Status: Part of handover | Startup, operation, shutdown procedures
│
├── 🔍 ⏳ Maintenance guide
│   └── Owner: Kwanghyeop, team | Status: Part of handover | Preventive maintenance, troubleshooting

├── 🔍 ⏳ End-to-end system testing
│   └── Owner: Team leads | Status: Needs scheduling | Full cycle testing, integration testing
│
├── 🔍 ⏳ Code repository documentation
│   └── Owner: Development team | Status: May be missing | Branch structure, deployment, config
│
├── 🔍 ⏳ Environment setup documentation
│   └── Owner: Backend team, Kwanghyeop | Status: May need update | Software, versions, installation, network
│
├── 🔍 ⏳ Product registration procedures
│   └── Owner: Frontend, Backend | Status: May need update | Step-by-step guide, image capture, DB config
│
├── 🔍 ⏳ Error handling and recovery procedures
│   └── Owner: Team leads | Status: Needs documentation | Warning types, recovery steps, escalation
│
├── 🔍 ⏳ Network infrastructure setup
│   └── Owner: Kwanghyeop, Everint IT | Status: Requested, pending response | LAN connection, wifi router
│
├── 🔍 ⏳ Clear acceptance criteria definition
│   └── Owner: Saad, Odil | Status: Requested Jan 14 | What is "done", measurable targets
```

---

## ⚠️ Risks & Dependencies

```
📁 RISKS & DEPENDENCIES
│
├── ⚠️ Robot Teaching → Vision Integration → Cycle Time Testing
│   └── Sequential dependency blocking multiple tasks | Mitigation: Prioritize robot teaching
│
├── ⚠️ Dataset Collection → Vision Validation
│   └── Requires stable robot operation | Mitigation: Schedule dedicated data collection
│
├── ⚠️ Documentation Completion → Handover
│   └── Multiple documentation tasks in parallel | Mitigation: Assign clear owners, track progress
│
├── ⚠️ GUI Issues → Product Registration
│   └── Affects operational workflow | Mitigation: GUI fixes completed (Jan 16)
│
├── ⚠️ Conveyor Position Error → Cycle Time Impact
│   └── Position error 1-1.5 cm resolved but cycle time increased from 4s to 6s | Mitigation: Need better solution
│
├── ⚠️ Reference Images → Detection Accuracy
│   └── Reference images need recapture for all products (FR3 holding vs pressing arm) | Mitigation: Priority task
│
├── ⚠️ Production Readiness → Government Report
│   └── Must run 100 products smoothly by Monday afternoon | Mitigation: Weekend shifts scheduled
│
└── ⚠️ Hardware Spares → Production Continuity
    └── Need sufficient spares for Fairino fingers and 3D printed parts | Mitigation: Spares preparation in progress
```

---

## 📅 Upcoming Deadlines

```
📁 UPCOMING DEADLINES
│
├── 📅 Monday, January 20, 2026 (CRITICAL)
│   └── Run 100 LB printers (XD5-40D, 950EA) without stopping by Monday afternoon | Manager arrives 4PM to turn on conveyor | Required for government report submission
│
├── 📅 Monday Morning Shift (Jan 20)
│   └── Run system continuously for 200+ products, prepare for demo, fix remaining tasks (no hardware/code changes) | Team: Tan, Ammad, Muazzam, Shams, Haider Shah
│
├── 📅 Monday Evening Shift (Jan 20, 4PM-5PM)
│   └── Run 100+ products within target cycle time | Manager arrives 4PM | Team: Hieu, Tugi, Rizwan, Shoaib
│
├── 📅 Weekend Shifts (Jan 18-19)
│   ├── Saturday afternoon: Hieu (Screw robot), Tugi (Rubber foot robot), Quy Ninh (Check vision models, help running, organize dataset)
│   ├── Sunday morning: Ammad (Fix robots, hardware check, install buzzers), Muazzam (Hardware, spares), Tan (Run system), Jalol (Finalize GUI, warning mechanism), Shams (Vision support)
│   └── Sunday evening: Shoaib, Rizwan (Vision integration), Tugi (Finalize rubber robot), Haider Shah (Rubber models)
│
├── 📅 Demo Preparation Meeting (Jan 18, 12PM Noon)
│   └── Basement & by Zoom | Finalize demo preparation
│
├── 📅 January 20, 2026
│   └── PCB production resumes (no production till 20th)
│
└── 📅 Ongoing
    └── Handover documentation (Kwanghyeop)
```

---

**Legend:**
- ✅ = Completed
- ⏳ = In Progress / Pending
- 🔴 = Critical / Blocking (High Urgency)
- 🟡 = High Priority (Medium-High Urgency) / Medium Priority
- 🟢 = Low Priority
- 📋 = Follow-up Required
- 🔍 = Missing Item / Information Gap
- ⚠️ = Risk / Dependency
- 📅 = Deadline

---

**Note:** This comprehensive checklist merges urgent tasks, missing items, and gaps. All tasks should be verified and created in Asana by the project owner. Status and urgency may change based on project progress.
