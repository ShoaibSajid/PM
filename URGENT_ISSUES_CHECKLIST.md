# Urgent Issues - Complete Tracking Checklist

**Last Updated:** January 30, 2026 (Matched with Asana tasks)  
**Timezone:** Asia/Seoul (KST)

**Note:** 
- PCB system is almost complete and running. Ammad (Robot/Framework) and Tan (Vision) are currently helping other robot systems (Hieu, Tugi) as additional resources.
- This file now contains only tasks that match Asana screenshots. Completed tasks moved to [COMPLETED_TASKS.md](./COMPLETED_TASKS.md). Tasks not in Asana moved to [TASKS_MISSING_IN_ASANA_RAW_REVIEW.md](./TASKS_MISSING_IN_ASANA_RAW_REVIEW.md).

---

## 🔴 Critical / Blocking Issues

```
📁 CRITICAL ISSUES
│
│ ┌─ REGISTRATION & SETUP (Highest Priority for Demo) ─┐
│ │
│ ├── 🔴 ⏳ Register All Products with update system / metal fingers
│ │   └── Owner: LT Le Thai Tan | Status: Only 2 done (XD5-40D, XD3-40D), waiting for manual registration fix | CRITICAL for Monday demo
│ │
│ └──────────────────────────────────────────────────────┘
│
│ ┌─ HARDWARE & MECHANICAL (Blocks Production) ─┐
│ │
│ ├── 🔴 ⏳ Fix Printer Tilt (Depth based angle adjustment)
│ │   └── Owner: hi hieu | Status: Printer is tilted, causing bit offset after each screwing causing pick miss, also screw robot reset timeout (Jan 21) | CRITICAL - Urgent/Important
│ │
│ ├── 🔴 ⏳ Fix screw bit drift from pickup position after screwing
│ │   └── Owner: hi hieu | Status: Screw bit occasionally drifts away from pickup position, suspected caused by unsmooth screwing in top-right screw hole (Jan 21) | CRITICAL - Blocks production
│ │
│ └──────────────────────────────────────────────────────┘
│
│ ┌─ VISION & DETECTION (Blocks Production Quality) ─┐
│ │
│ ├── 🔴 ⏳ Finalize rescan logic (rubber foot)
│ │   └── Owner: TJ Tuguldur Jigj | Status: Tested (Jan 19-20), rolled back due to issues, vision team working on fixes | Affects reliability
│ │
│ ├── 🔴 ⏳ Integrate rubber pad offset from vision model / Capture rubber pad after scooping
│ │   └── Owner: TJ Tuguldur Jigj | Status: Pending integration | Affects pickup accuracy
│ │
│ ├── 🔴 ⏳ Integrate top camera / validate printer location
│ │   └── Owner: hi hieu | Status: PR #136, #141 merged with README (Jan 22), needs integration and testing | CRITICAL - Collision detection
│ │
│ └──────────────────────────────────────────────────────┘
│
│ ┌─ SOFTWARE & SYSTEM STABILITY ─┐
│ │
│ ├── 🔴 ⏳ Use Start/Abort signal from conveyor (screw/rubber)
│ │   └── Owner: AW Ammad | Status: Conveyor signal integration needed | CRITICAL - System control
│ │
│ ├── 🔴 ⏳ Integrate Fairino / Add error handling / Collision handling
│ │   └── Owner: AW Ammad | Status: Collision signal developed on Fairino side but not integrated (Jan 28) | CRITICAL - System safety
│ │
│ ├── 🔴 ⏳ Integrate update vision algorithm for depth estimation
│ │   └── Owner: hi hieu | Status: Need to filter outlier depth points, compute mean only from inliers (Jan 28) | CRITICAL - Depth accuracy
│ │
│ ├── 🔴 ⏳ Test and finalize product registration (Manual and Auto) (PCB)
│ │   └── Owner: sa saidjalol | Status: Registration testing and finalization needed | CRITICAL - System functionality
│ │
│ ├── 🔴 ⏳ Test and finalize product registration (Manual and Auto) (Screw/Rubber)
│ │   └── Owner: sa saidjalol | Status: Registration testing and finalization needed | CRITICAL - System functionality
│ │
│ └──────────────────────────────────────────────────────┘
│
│ ┌─ RUBBER FOOT ROBOT - CUSTOM PENDING TASKS ─┐
│ │
│ ├── 🔴 ⏳ Merge screw/rubber foot robot code
│ │   └── Owner: hi hieu | Status: From CustomPendingTasks_Rubber.md (Jan 28) | CRITICAL - Code consistency
│ │
│ ├── 🔴 ⏳ Integrate finger gripper sequence for rubber foot robot
│ │   └── Owner: TJ Tuguldur Jigj | Status: From CustomPendingTasks_Rubber.md (Jan 28) - Modify code to integrate different gripper, modify logic to skip validation | CRITICAL - System integration
│ │
│ ├── 🔴 ⏳ Reposition platform for rubber foot robot
│ │   └── Owner: MA Muazzam | Status: From CustomPendingTasks_Rubber.md (Jan 28) - Position to allow 3 holders on platform, redesign if needed | CRITICAL - Hardware optimization
│ │
│ └── 🔴 ⏳ 3D print catching basket
│     └── Owner: SA Saad Arslan | Status: From CustomPendingTasks_Rubber.md (Jan 28) - Design and print | CRITICAL - Hardware design
│ │
│ └──────────────────────────────────────────────────────┘
```

---

## 🟡 High Priority Issues

```
📁 HIGH PRIORITY ISSUES
│
├── 🟡 ⏳ Optimize motions / reduce cycle time (screw)
│   └── Owner: hi hieu | Status: After 1st priority tasks | Blocks cycle time targets
│
├── 🟡 ⏳ Optimize motions / reduce cycle time (rubber foot)
│   └── Owner: TJ Tuguldur Jigj | Status: After 1st priority tasks | Blocks cycle time targets
│
├── 🟡 ⏳ Test self-training code for screw driver robot
│   └── Owner: hi hieu | Status: Testing needed | High priority
│
├── 🟡 ⏳ Test self-training code for rubber foot robot
│   └── Owner: TJ Tuguldur Jigj | Status: After 1st priority tasks | In progress
│
├── 🟡 ⏳ Order 1 5070 GPU for Screw Driver Robot (and 1 spare if possible)
│   └── Owner: KK Kwanghyeop | Status: Hardware procurement needed | High priority
│
├── 🟡 ⏳ [screw] Ordering spare screw driver bits
│   └── Owner: KK Kwanghyeop | Status: Requested by Ammad (Jan 19) | Need to order replacement bits
│
├── 🟡 ⏳ Prepare and install new metal fingers
│   └── Owner: MA Muazzam | Status: Hardware installation needed | High priority
│
├── 🟡 ⏳ Install 3 rubber pad holders
│   └── Owner: MA Muazzam | Status: Hardware installation needed | High priority
│
├── 🟡 ⏳ Finalize design for rubber pad holder
│   └── Owner: SA Saad Arslan | Status: Design finalization needed | High priority
│
├── 🟡 ⏳ Pre-pickup rubber pad at end/start of cycle.
│   └── Owner: TJ Tuguldur Jigj | Status: From CustomPendingTasks | Optimization for cycle time
│
├── 🟡 ⏳ Ensure spares for 3D printed parts
│   └── Owner: MA Muazzam | Status: In progress | Critical for production continuity
│
├── 🟡 ⏳ List of deliverable items (pending delivery)
│   └── Owner: KK Kwanghyeop | Status: Uploaded to OneDrive (Jan 16), needs verification | Missing items may delay handover
│
├── 🟡 ⏳ Prepare list of all the items installed with serial number, location and age
│   └── Owner: KK Kwanghyeop | Status: Documentation needed | High priority
│
├── 🟡 ⏳ Prepare list of all the 3D printed parts along with installed location, quantity and specifications
│   └── Owner: MA Muazzam | Status: Documentation needed | High priority
│
├── 🟡 ⏳ Order/Prepare finger spares
│   └── Owner: MA Muazzam | Status: Spare fingers prepared (Jan 16) | Ready for replacement
│
├── 🟡 ⏳ Test Screw/Rubber GUI and report issues
│   └── Owner: LT Le Thai Tan | Status: From CustomPendingTasks_Screw.md (Jan 28) | CRITICAL - System quality
│
├── 🟡 ⏳ Save images in PNG in case of failure (screw/rubber) in dedicated dir (/DATA/Failure
│   └── Owner: LT Le Thai Tan | Status: Error handling improvement needed | High priority
│
├── 🟡 ⏳ Integrate irregular rubber foot outer body for accurate attachment
│   └── Owner: TJ Tuguldur Jigj | Status: Vision/attachment improvement needed | High priority
│
└──────────────────────────────────────────────────────┘
```

---

## 🟢 Important / Low Priority Issues

```
📁 IMPORTANT ISSUES
│
└── 🟢 ⏳ Prepare system documentation and handover package for Everint
    └── Owner: KK Kwanghyeop | Status: Not started yet | Tasks created in Asana but work not begun
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
├── 📋 ⏳ [screw] Robot finger with spring mechanism for PCB robot
│   └── Owner: AW Ammad | Status: In progress | Needs completion
│
├── 📋 ⏳ [screw] Adjustable Label printer aligner jig for worker placement
│   └── Owner: KK Kwanghyeop | Status: In progress | Needs completion
│
├── 📋 ⏳ Visualize cycle execution times
│   └── Owner: TJ Tuguldur Jigj | Status: Analysis/visualization needed | Medium priority
│
├── 📋 ⏳ [screw] Investigate Collision when robot A move up from pcb holding position
│   └── Owner: AW Ammad | Status: Has comments (2) | Medium priority
│
├── 📋 ⏳ add new mqtt_subcall:mqqt_receive_msg_callback for command/data with sepe
│   └── Owner: AW Ammad | Status: Has comments (1) | Medium priority
│
├── 📋 ⏳ [screw] Wiring Feedback for screw driver
│   └── Owner: AW Ammad | Status: Has attachment, expandable task | Medium priority
│
├── 📋 ⏳ [screw] Finalize the error list and events for LB-Screw
│   └── Owner: hi hieu | Status: Has comments (1) | Medium priority
│
├── 📋 ⏳ [screw] Vision Test Bench
│   └── Owner: hi hieu | Status: Testing setup needed | Medium priority
│
├── 📋 ⏳ Make a detailed network diagram
│   └── Owner: KK Kwanghyeop | Status: Documentation needed | Medium priority
│
├── 📋 ⏳ Prepare complete test bench with Hieu for label printer
│   └── Owner: LT Le Thai Tan | Status: Testing setup needed | Medium priority
│
├── 📋 ⏳ [screw] Test OBB DETR model for PCB detection
│   └── Owner: LT Le Thai Tan | Status: Vision testing needed | Medium priority
│
├── 📋 ⏳ [screw] Robot scan area tuning
│   └── Owner: sa samrahsajid1 | Status: GUI/configuration needed | Medium priority
│
├── 📋 ⏳ [label] Terminal -> Logs
│   └── Owner: Sa Sawera | Status: GUI feature needed | Medium priority
│
├── 📋 ⏳ [screw] Realtime Logs (Front, Back, vision, robot)
│   └── Owner: Sa Sawera | Status: GUI feature needed | Medium priority
│
├── 📋 ⏳ [screw] Test Bench for registration
│   └── Owner: Sa Sawera | Status: Testing needed | Medium priority
│
├── 📋 ⏳ Finalize error message mechanism for Screw/Rubber GUI (auto timeout etc)
│   └── Owner: TJ Tuguldur Jigj | Status: GUI feature needed | Medium priority
│
└── 📋 ⏳ [screw] User Guide
    └── Owner: Sa Sawera | Status: Documentation needed | Low priority
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
- ✅ = Completed (moved to [COMPLETED_TASKS.md](./COMPLETED_TASKS.md))
- ⏳ = In Progress / Pending
- 🔴 = Critical / Blocking (High Urgency)
- 🟡 = High Priority (Medium-High Urgency) / Medium Priority
- 🟢 = Low Priority
- 📋 = Follow-up Required
- 🔍 = Missing Item / Information Gap (moved to [TASKS_MISSING_IN_ASANA_RAW_REVIEW.md](./TASKS_MISSING_IN_ASANA_RAW_REVIEW.md))
- ⚠️ = Risk / Dependency
- 📅 = Deadline

---

**Related Files:**
- [COMPLETED_TASKS.md](./COMPLETED_TASKS.md) - All completed tasks archive
- [TASKS_MISSING_IN_ASANA_RAW_REVIEW.md](./TASKS_MISSING_IN_ASANA_RAW_REVIEW.md) - Tasks not in Asana (need review)
- [BLINDSPOTS.md](./BLINDSPOTS.md) - PM perspective gaps and risks
- [ASANA_TASKS_LIST.md](./ASANA_TASKS_LIST.md) - Complete list of all Asana tasks

---

**Note:** This checklist now contains only tasks that match Asana screenshots. All tasks should be verified and tracked in Asana. Status and urgency may change based on project progress.
