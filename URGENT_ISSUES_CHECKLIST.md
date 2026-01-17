# Urgent Issues - Complete Tracking Checklist

**Last Updated:** January 17, 2026 (Based on Jan 16-17 chat updates)  
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
├── 🔴 ⏳ Fix screw pickup validation - Label Printer Screw Robot (2nd screw feeder FPs)
│   └── Owner: Hieu, Rizwan | Status: Tuning parameters in progress (Jan 16) | Blocks production
│
├── 🔴 ⏳ Test rescan logic (Rubber Foot Robot)
│   └── Owner: Tugi | Status: Pending testing | Affects reliability
│
├── 🔴 ⏳ Self Training update - Label Printer Screw Robot
│   └── Owner: Rizwan | Status: In progress (Jan 16) | Self training update needed
│
├── 🔴 ⏳ Recapture reference images for all products (FR3 holding, not pressing arm)
│   └── Owner: Tugi, Hieu, Odil | Status: Reference images need update due to FR3 holding method change | Blocks accurate detection
│
├── 🔴 ⏳ Display error/warning on failure (rubber foot attachment, missed rubber foot, failed to screw, etc.)
│   └── Owner: Hieu, Tugi, Jalol | Status: Required for production monitoring | Critical for quality control
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
├── 🟡 ⏳ Install buzzers for error/warning display
│   └── Owner: Ammad | Status: Need to install | Required for production monitoring
│
├── 🟡 ⏳ Bring one more 100% infill Fairino finger base from lab
│   └── Owner: Ammad, Muazzam, Myeongun | Status: Need spares | Critical for production continuity
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
│   └── Owner: Jalol | Status: In progress (Jan 16) | Deadline: Sunday morning shift
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
│
├── 🔍 ⏳ Support and escalation information
│   └── Owner: Shoaib, Kwanghyeop | Status: Needs definition | Contacts, escalation paths, ownership
│
├── 🔍 ⏳ Vision model validation reports
│   └── Owner: Vision team | Status: In progress | 10-20 product tests, accuracy, failure analysis
│
├── 🔍 ⏳ Cycle time validation reports
│   └── Owner: Robot team, Saad | Status: Pending | Documented times, comparison vs targets
│
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
├── 🔍 ⏳ Hardware delivery tracking
│   └── Owner: Kwanghyeop | Status: Needs tracking system | Safety covers, pending equipment
│
├── 🔍 ⏳ Daily/weekly status summary
│   └── Owner: Team leads | Status: May need regular cadence | Progress, blockers, next steps
│
├── 🔍 ⏳ Issue tracking system
│   └── Owner: Project coordination | Status: Excel requested, needs maintenance | Centralized log, resolution
│
├── 🔍 ⏳ Production metrics tracking
│   └── Owner: Robot team, Backend | Status: Some data available | Success rates, cycle times, failure analysis
│
├── 🔍 ⏳ Vision model performance metrics
│   └── Owner: Vision team | Status: Needs validation reports | Detection accuracy, false positive/negative rates
│
├── 🔍 ⏳ Clear acceptance criteria definition
│   └── Owner: Saad, Odil | Status: Requested Jan 14 | What is "done", measurable targets
│
└── 🔍 ⏳ Evidence collection
    └── Owner: All teams | Status: In progress | Test results, validation reports, performance metrics
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
│   └── Run 100 LB printers without stopping by Monday afternoon | Required for government report submission
│
├── 📅 Monday Morning Shift (Jan 20)
│   └── Run system continuously for 200+ products, prepare for demo, fix remaining tasks (no hardware/code changes)
│
├── 📅 Monday Evening Shift (Jan 20, 4PM-5PM)
│   └── Run 100+ products within target cycle time
│
├── 📅 Weekend Shifts (Jan 18-19)
│   ├── Saturday afternoon: Hieu (Screw robot), Shams/Quy Ninh (Vision), Tung (Equipment serial numbers)
│   ├── Sunday morning: Ammad (Fix robots, hardware check, install buzzers), Tan (Run system), Jalol (Finalize GUI)
│   └── Sunday evening: Shoaib, Tugi (Finalize rubber robot), Muazzam (Hardware, spares), Haider Shah (Rubber models)
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
