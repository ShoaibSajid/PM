# Urgent Issues - Complete Tracking Checklist

**Last Updated:** January 15, 2026 (Updated from Asana tasks)  
**Timezone:** Asia/Seoul (KST)

**Note:** PCB system is almost complete and running. Ammad (Robot/Framework) and Tan (Vision) are currently helping other robot systems (Hieu, Tugi) as additional resources.

---

## 🔴 Critical / Blocking Issues

```
📁 CRITICAL ISSUES
│
├── 🔴 ✅ Complete robot teaching - Label Printer Screw Robot (FR3)
│   └── Owner: Hieu | Status: Completed (Asana) | Blocks cycle time & vision integration
│
├── 🔴 ⏳ Fix pad holding bracket - Label Printer Rubber Foot Robot
│   └── Owner: Tugi | Status: Broken bracket causing misalignment | Blocks vision testing
│
├── 🔴 ⏳ Integrate new vision model output format
│   └── Owner: Hieu, Rizwan | Status: Tugi merged (Jan 14), Hieu updated (Jan 15), Tugi needs to merge & test | Blocks full cycle
│
├── 🔴 ⏳ Test rescan logic (Rubber Foot Robot)
│   └── Owner: Tugi | Status: Operation working, rescan needs testing | Affects reliability
│
├── 🔴 ⏳ Complete vision integration status summary
│   └── Owner: Rizwan | Deadline: Jan 15, 2026 | Status: In progress
│
├── 🔴 ⏳ Confirm cycle time - Label Printer Screw Robot
│   └── Owner: Hieu, Saad | Status: Pending robot teaching | Critical acceptance criteria
│
└── 🔴 ✅ Confirm cycle time - Label Printer Rubber Foot Robot
    └── Owner: Tugi, Saad | Status: ~28 sec (needs optimization) | Critical acceptance criteria
```

---

## 🟡 High Priority Issues

```
📁 HIGH PRIORITY ISSUES
│
├── 🟡 ⏳ Fix GUI freezing/halt and slow issues (Label Printer)
│   └── Owner: Jalol | Status: Tuning codes, will push after testing (Jan 15) | Affects workflow
│
├── 🟡 ⏳ Create Excel file - GUI tasks and issues status
│   └── Owner: Jalol | Deadline: Jan 15, 2026 | Status: In progress, adding GUI & vision columns
│
├── 🟡 ⏳ Collect dataset for vision model testing
│   └── Owner: Rizwan, Shams, Tugi, Hieu | Status: Waiting for stable operation | Blocks validation
│
├── 🟡 ✅ Validate vision models for screw driver robot
│   └── Owner: Rizwan | Status: Completed (Asana) | Required for handover
│
├── 🟡 ✅ Validate vision models for rubber foot robot
│   └── Owner: Rizwan | Status: Completed (Asana) | Required for handover
│
├── 🟡 ✅ Equipment list (installed and pending delivery)
│   └── Owner: Kwanghyeop | Status: Completed (Asana) | List of items with serial numbers, locations, and pending deliveries
│
├── 🟡 ✅ 3D parts list
│   └── Owner: Muazzam | Status: Completed (Asana) | List of all 3D printed parts with installed locations
│
├── 🟡 ✅ Maintain 3D components tracking list (requested/printed/handed over)
│   └── Owner: Myeongun | Status: Completed (Asana) | Track all 3D component requests
│
├── 🟡 ✅ Order gripper base (with 2 or 3 springs) in metal
│   └── Owner: Myeongun | Status: Completed (Asana) | Ordered
│
├── 🟡 ✅ Order base part of gripper fingers in metal
│   └── Owner: Myeongun | Status: Completed (Asana) | Ordered
│
├── 🟡 ⏳ Complete Screw Driver Robot fingers (Fairino) - Design review
│   └── Owner: Ammad, Myeongun | Status: Design review in progress, needs changes (screw position, plate thickness, bendable sheet) | Blocks Fairino usage
│
├── 🟡 ✅ Prepare complete test bench with Hieu for label printer
│   └── Owner: Tan | Status: Completed (Asana) | Test bench ready
│
├── 🟡 ✅ Test OBB DETR model for PCB detection
│   └── Owner: Tan | Status: Completed (Asana) | PCB detection model tested
│
└── 🟡 ⏳ Define list of targets for Everint project acceptance
    └── Owner: Saad, Odil | Deadline: Friday | Status: Requested Jan 14
```

---

## 🟢 Important / Low Priority Issues

```
📁 IMPORTANT ISSUES
│
└── 🟢 ✅ Complete handover documentation package
    └── Owner: Kwanghyeop | Status: Completed (Asana) | All 6 sub-tasks completed:
    └──   ├── System Operation Documentation ✅
    └──   ├── Maintenance Documentation ✅
    └──   ├── Equipment & Hardware List ✅
    └──   ├── Vision System Documentation ✅
    └──   ├── Software & System Overview ✅
    └──   └── Handover & Ownership Information ✅
    └── Additional: Jalol creating registration guide, Sawera preparing manuals
```

---

## 📋 Follow-up Required

```
📁 FOLLOW-UP REQUIRED
│
├── 📋 ✅ Review and respond to assigned Asana tasks
│   └── Owner: All team members | Status: Multiple tasks completed (Asana)
│
├── 📋 ⏳ Capture production data for vision model validation
│   └── Owner: Vision team, Robot team | Status: Waiting for stable operation
│
├── 📋 ⏳ Request samples for Label Printer (XD3-40d, XD5-40d)
│   └── Owner: Kwanghyeop | Status: Need to request from manager | For production testing
│
├── 📋 ✅ Order LED/Buzzer for warning/error
│   └── Owner: Ammad | Status: Completed (Asana) | Ordered
│
├── 📋 ✅ Purchase Acrylic boundary for label printer table
│   └── Owner: Myeongun | Status: Completed (Asana) | Purchased
│
├── 📋 ✅ Purchase Acrylic boundary for PCB table
│   └── Owner: Myeongun | Status: Completed (Asana) | Purchased
│
├── 📋 ✅ Order one more metal mesh for the rubber foot
│   └── Owner: Myeongun | Status: Completed (Asana) | Ordered
│
├── 📋 ✅ Assembly Process Product Image
│   └── Owner: Samrah | Status: Completed (Asana) | Image processing completed
│
├── 📋 ✅ Test nail gripper and roller mechanism
│   └── Owner: Muazzam | Status: Completed (Asana) | Tested
│
├── 📋 ✅ [screw] Rubber Pad Pickup
│   └── Owner: Muazzam | Status: Completed (Asana) | Completed
│
├── 📋 ✅ [screw] Conveyor Shakes when robot moves
│   └── Owner: Ammad | Status: Completed (Asana) | Investigated and resolved
│
├── 📋 ✅ [screw] Investigate Collision when robot A move up
│   └── Owner: Ammad | Status: Completed (Asana) | Investigated and resolved
│
├── 📋 ✅ [screw] Wiring Feedback for screw driver
│   └── Owner: Ammad | Status: Completed (Asana) | Completed
│
├── 📋 ✅ [screw] Robot finger with spring mechanism for PCB robot
│   └── Owner: Ammad | Status: Completed (Asana) | Completed
│
├── 📋 ✅ Prepare cushion support using profiles, joints, and install on top
│   └── Owner: Ammad | Status: Completed (Asana) | Installed
│
├── 📋 ✅ [screw] Finalize the error list and events for LB-Screw
│   └── Owner: Hieu | Status: Completed (Asana) | Finalized
│
├── 📋 ✅ [screw] Collect data and provide to vision team for tilted printer
│   └── Owner: Hieu | Status: Completed (Asana) | Data collected and provided
│
└── 📋 ✅ [screw] Adjustable Label printer aligner jig for worker placement
    └── Owner: Kwanghyeop | Status: Completed (Asana) | Completed
│
└── 📋 ⏳ Vision status update
    └── Owner: Rizwan | Status: Follow-up requested Jan 15 | Vision integration status summary
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
├── 🔍 ✅ Complete equipment inventory with serial numbers
│   └── Owner: Kwanghyeop | Status: Completed (Asana) | Robots, controllers, cameras, grippers
│
├── 🔍 ✅ Pending delivery items tracking
│   └── Owner: Kwanghyeop | Status: Completed (Asana) | List of deliverable items (pending delivery)
│
├── 🔍 ✅ 3D printed parts inventory
│   └── Owner: Muazzam | Status: Completed (Asana) | List of all 3D printed parts with installed locations
│
├── 🔍 ✅ Operation manual completeness
│   └── Owner: Kwanghyeop | Status: Completed (Asana - System Operation Documentation) | Startup, operation, shutdown procedures
│
├── 🔍 ✅ Maintenance guide
│   └── Owner: Kwanghyeop | Status: Completed (Asana - Maintenance Documentation) | Preventive maintenance, troubleshooting
│
├── 🔍 ✅ Support and escalation information
│   └── Owner: Kwanghyeop | Status: Completed (Asana - Handover & Ownership Information) | Contacts, escalation paths, ownership
│
├── 🔍 ✅ Vision model validation reports
│   └── Owner: Rizwan | Status: Completed (Asana) | Validated for both screw driver and rubber foot robots
│
├── 🔍 ⏳ Cycle time validation reports
│   └── Owner: Robot team, Saad | Status: Pending | Documented times, comparison vs targets
│
├── 🔍 ⏳ End-to-end system testing
│   └── Owner: Team leads | Status: Needs scheduling | Full cycle testing, integration testing
│
├── 🔍 ⏳ Product registration procedures
│   └── Owner: Frontend, Backend | Status: May need update | Step-by-step guide, image capture, DB config
│
├── 🔍 ⏳ Error handling and recovery procedures
│   └── Owner: Team leads | Status: Needs documentation | Warning types, recovery steps, escalation
│
├── 🔍 ✅ Network infrastructure setup
│   └── Owner: Kwanghyeop | Status: Completed (Asana) | Detailed network diagram created
│
├── 🔍 ⏳ Network infrastructure implementation
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
└── ⚠️ GUI Issues → Product Registration
    └── Affects operational workflow | Mitigation: Prioritize critical GUI fixes
```

---

## 📅 Upcoming Deadlines

```
📁 UPCOMING DEADLINES
│
├── 📅 January 15, 2026
│   ├── Vision integration status summary (Rizwan)
│   └── GUI issues Excel file (Jalol) - adding GUI & vision columns
│
├── 📅 January 20, 2026
│   └── PCB production resumes (no production till 20th)
│
├── 📅 Friday (target)
│   └── Meet Everint project acceptance targets
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
