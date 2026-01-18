# Urgent Issues - Complete Tracking Checklist

**Last Updated:** January 18, 2026 (Based on Jan 17-18 updates)  
**Timezone:** Asia/Seoul (KST)

**Note:** PCB system is almost complete and running. Ammad (Robot/Framework) and Tan (Vision) are currently helping other robot systems (Hieu, Tugi) as additional resources.

---

## 🔴 Critical / Blocking Issues

```
📁 CRITICAL ISSUES
│
├── 🔴 ⏳ Fix rubber foot attachment position error (Rubber Foot Robot)
│   └── Owner: Tugi | Status: Multiple contributing factors (vision variations, calibration, robot repeatability, suction cup, irregular rubber shape) | Blocks production quality
│
├── 🔴 ⏳ Fix fragile Fairino fingers bending when gripping (Both systems)
│   └── Owner: Ammad, Myeongun | Status: Fingers bend when gripping product | Solution: Use metal/inward bent fingers
│
├── 🔴 ⏳ Fix out of place product on conveyor causing collision
│   └── Owner: Ammad, Hieu | Status: Products misaligned causing collision/damage | Solution: Use top camera to detect product within acceptable zone
│
├── 🔴 ⏳ Debug screwdriver robot moving slow
│   └── Owner: Hieu, Ammad | Status: Robot speed needs investigation | Blocks cycle time
│
├── 🔴 ⏳ Investigate and fix screw pickup tilting
│   └── Owner: Hieu, Ammad | Status: Likely magnetism and long screw issue | Solution: Consider replacing feeder's rotating plate with plastic
│
├── 🔴 ⏳ Complete 2D camera hardware installation
│   └── Owner: Muazzam, Ammad | Status: Hardware installation incomplete | Blocks full system functionality
│
├── 🔴 ⏳ Fix screw speed issue - Label Printer Screw Robot (1st Priority)
│   └── Owner: Hieu, Ammad | Status: Robot slows when timeout/abort signal, suspected clean_up function issue, needs control box restart | CRITICAL - Blocks cycle time
│
├── 🔴 ⏳ Display error messages - Label Printer Screw Robot (1st Priority)
│   └── Owner: Hieu | Status: In progress (Jan 17) | CRITICAL for Monday demo
│
├── 🔴 ⏳ Fix GUI registration bug (saving SVG issue) - Both systems
│   └── Owner: Jalol | Status: Random bug prevents saving annotation results, blocks registration | CRITICAL - Only 2 products registered (XD5-40D, XD3-40D)
│
├── 🔴 ⏳ Register all products with new code - Both systems
│   └── Owner: Hieu, Tugi, Quy Ninh | Status: Only 2 done (XD5-40D, XD3-40D) due to GUI bug | CRITICAL for Monday demo
│
├── 🔴 ⏳ Fix self training file saving issue (path format)
│   └── Owner: Haider Shah | Status: File saved to wrong folder, named with full path, use os.path | Blocks proper saving
│
├── 🔴 ⏳ Fix robot speed in timeout/collision (clean_up function)
│   └── Owner: Ammad | Status: Dump robot's system variables at start and after slowdown for analysis | CRITICAL - Blocks cycle time
│
├── 🔴 ⏳ Calibrate placement position - Label Printer Rubber Foot Robot (1st Priority)
│   └── Owner: Tugi, Muazzam, Tan | Status: Hand eye calibration done (Jan 17), needs fine-tuning check (Jan 18) | CRITICAL for Monday demo
│
├── 🔴 ⏳ Get robot to place rubber foot in correct position - Label Printer Rubber Foot Robot (1st Priority)
│   └── Owner: Tugi | Status: Hand eye calibration done, tuning parameters in progress | CRITICAL for Monday demo
│
├── 🔴 ⏳ Fix rubber foot ROI detection (tighter mechanism issue)
│   └── Owner: Rizwan, Hieu | Status: User ROI from GUI good, but tighter mechanism makes it wrong | Blocks accurate detection
│
├── 🔴 ⏳ Integrate new vision code PR - Both systems
│   └── Owner: Hieu, Rizwan | Status: PR ready, needs integration to Hieu-second branch, solve conflicts | Blocks new features
│
├── 🔴 ⏳ Register XD5-40D with new code - Both systems
│   └── Owner: Hieu, Tugi | Status: References changed due to new gripper fingers | CRITICAL for Monday demo (950EA production)
│
├── 🔴 ⏳ Fix screw pickup validation - Label Printer Screw Robot (2nd screw feeder FPs)
│   └── Owner: Hieu, Haider Shah, Rizwan | Status: Multiple false positive/negative cases (Jan 17), PR merged but didn't solve, needs range-based logic instead of strict "and" | Blocks production
│
├── 🔴 ⏳ Fix tilted screw issue - Label Printer Screw Robot (2nd Priority)
│   └── Owner: Ammad | Status: Adjusted pickup position, added magnet (seems better), plastic plate installed but uninstalled (not working), vertical plates not done | In progress
│
├── 🔴 ⏳ Test rescan logic (Rubber Foot Robot) (2nd Priority)
│   └── Owner: Tugi | Status: Pending testing | Affects reliability
│
├── 🔴 ⏳ Integrate rescan logic - Label Printer Rubber Foot Robot (2nd Priority)
│   └── Owner: Tugi | Status: Pending integration | Affects reliability
│
├── 🔴 ⏳ Integrate rubber pad pickup offset - Label Printer Rubber Foot Robot (2nd Priority)
│   └── Owner: Tugi | Status: Pending integration | Affects pickup accuracy
│
├── 🔴 ⏳ Recapture reference images for all products (FR3 holding, not pressing arm)
│   └── Owner: Tugi, Hieu, Odil | Status: References changed due to new gripper fingers | Blocks accurate detection
│
├── 🔴 ⏳ Conveyor position adjustment / fix (1st Priority)
│   └── Owner: Ammad | Status: CRITICAL for Monday demo | Affects product positioning
│
├── 🔴 ⏳ Confirm cycle time - Label Printer Screw Robot
│   └── Owner: Hieu, Saad | Status: Pending | Cycle time validation pending
│
└── 🔴 ⏳ Confirm cycle time - Label Printer Rubber Foot Robot
    └── Owner: Tugi, Saad | Status: Pending | Cycle time validation pending
│
│
├── 🔴 ✅ Complete robot teaching - Label Printer Screw Robot (FR3)
│   └── Owner: Hieu | Status: Complete (Jan 15) | Robot teaching done
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
├── 🔴 ✅ Display error messages - Label Printer Rubber Foot Robot (1st Priority)
│   └── Owner: Tugi | Status: Complete (Jan 17) | Error/warning message display code implemented (GUI reset needed)
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
