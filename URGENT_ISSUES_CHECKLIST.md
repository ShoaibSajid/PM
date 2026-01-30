# Urgent Issues - Complete Tracking Checklist

**Last Updated:** January 30, 2026 (Matched with Asana tasks)  
**Timezone:** Asia/Seoul (KST)

**Note:** 
- PCB system is almost complete and running. Ammad (Robot/Framework) and Tan (Vision) are currently helping other robot systems (Hieu, Tugi) as additional resources.
- This file now contains only tasks that match Asana screenshots. Completed tasks moved to [COMPLETED_TASKS.md](./COMPLETED_TASKS.md). Tasks not in Asana moved to [MISSING_TASKS.md](./MISSING_TASKS.md).

---

## 🔴 Critical / Blocking Issues

```
📁 CRITICAL ISSUES
│
│ ┌─ REGISTRATION & SETUP (Highest Priority for Demo) ─┐
│ │
│ ├── 🔴 ⏳ Register All Products with update system / metal fingers
│ │   └── Owner: Hieu, Tugi, Quy Ninh | Status: Only 2 done (XD5-40D, XD3-40D), waiting for manual registration fix | CRITICAL for Monday demo
│ │
│ └──────────────────────────────────────────────────────┘
│
│ ┌─ HARDWARE & MECHANICAL (Blocks Production) ─┐
│ │
│ ├── 🔴 ⏳ Fix Printer Tilt (Depth based angle adjustment)
│ │   └── Owner: Ammad, Hieu | Status: Printer is tilted, causing bit offset after each screwing causing pick miss, also screw robot reset timeout (Jan 21) | CRITICAL - Urgent/Important
│ │
│ ├── 🔴 ⏳ Fix screw bit drift from pickup position after screwing
│ │   └── Owner: Ammad, Hieu | Status: Screw bit occasionally drifts away from pickup position, suspected caused by unsmooth screwing in top-right screw hole (Jan 21) | CRITICAL - Blocks production
│ │
│ └──────────────────────────────────────────────────────┘
│
│ ┌─ VISION & DETECTION (Blocks Production Quality) ─┐
│ │
│ ├── 🔴 ⏳ Finalize rescan logic (rubber foot)
│ │   └── Owner: Tugi | Status: Tested (Jan 19-20), rolled back due to issues, vision team working on fixes | Affects reliability
│ │
│ ├── 🔴 ⏳ Integrate rubber pad offset from vision model / Capture rubber pad after scooping
│ │   └── Owner: Tugi | Status: Pending integration | Affects pickup accuracy
│ │
│ ├── 🔴 ⏳ Integrate top camera / validate printer location
│ │   └── Owner: Ghulam Muhammd, Hieu | Status: PR #136, #141 merged with README (Jan 22), needs integration and testing | CRITICAL - Collision detection
│ │
│ └──────────────────────────────────────────────────────┘
│
│ ┌─ SOFTWARE & SYSTEM STABILITY ─┐
│ │
│ ├── 🔴 ⏳ Integrate Fairino / Add error handling / Collision handling
│ │   └── Owner: Ammad, Hieu | Status: Collision signal developed on Fairino side but not integrated (Jan 28) | CRITICAL - System safety
│ │
│ ├── 🔴 ⏳ Integrate update vision algorithm for depth estimation
│ │   └── Owner: Tan, Hieu | Status: Need to filter outlier depth points, compute mean only from inliers (Jan 28) | CRITICAL - Depth accuracy
│ │
│ └──────────────────────────────────────────────────────┘
│
│ ┌─ RUBBER FOOT ROBOT - CUSTOM PENDING TASKS ─┐
│ │
│ ├── 🔴 ⏳ Merge screw/rubber foot robot code
│ │   └── Owner: Hieu, Tugi | Status: From CustomPendingTasks_Rubber.md (Jan 28) | CRITICAL - Code consistency
│ │
│ ├── 🔴 ⏳ Install finger gripper
│ │   └── Owner: Tugi, Muazzam | Status: From CustomPendingTasks_Rubber.md (Jan 28) | CRITICAL - Hardware installation
│ │
│ ├── 🔴 ⏳ Integrate finger gripper sequence for rubber foot robot
│ │   └── Owner: Tugi | Status: From CustomPendingTasks_Rubber.md (Jan 28) - Modify code to integrate different gripper, modify logic to skip validation | CRITICAL - System integration
│ │
│ ├── 🔴 ⏳ Reposition platform for rubber foot robot
│ │   └── Owner: Tugi, Muazzam | Status: From CustomPendingTasks_Rubber.md (Jan 28) - Position to allow 3 holders on platform, redesign if needed | CRITICAL - Hardware optimization
│ │
│ └── 🔴 ⏳ 3D print catching basket
│     └── Owner: Myeongun | Status: From CustomPendingTasks_Rubber.md (Jan 28) - Design and print | CRITICAL - Hardware design
│ │
│ └──────────────────────────────────────────────────────┘
```

---

## 🟡 High Priority Issues

```
📁 HIGH PRIORITY ISSUES
│
├── 🟡 ⏳ Optimize motions / reduce cycle time (screw)
│   └── Owner: Hieu | Status: After 1st priority tasks | Blocks cycle time targets
│
├── 🟡 ⏳ Optimize motions / reduce cycle time (rubber foot)
│   └── Owner: Tugi, Shoaib | Status: After 1st priority tasks | Blocks cycle time targets
│
├── 🟡 ⏳ Test self-training code for rubber foot robot
│   └── Owner: Tugi | Status: After 1st priority tasks | In progress
│
├── 🟡 ⏳ [screw] Ordering spare screw driver bits
│   └── Owner: Kwanghyeop | Status: Requested by Ammad (Jan 19) | Need to order replacement bits
│
├── 🟡 ⏳ Pre-pickup rubber pad at end/start of cycle.
│   └── Owner: Tugi, Hieu | Status: From CustomPendingTasks | Optimization for cycle time
│
├── 🟡 ⏳ Ensure spares for 3D printed parts
│   └── Owner: Muazzam, Myeongun | Status: In progress | Critical for production continuity
│
├── 🟡 ⏳ List of deliverable items (pending delivery)
│   └── Owner: Kwanghyeop | Status: Uploaded to OneDrive (Jan 16), needs verification | Missing items may delay handover
│
├── 🟡 ⏳ Order/Prepare finger spares
│   └── Owner: Tugi, Myeongun | Status: Spare fingers prepared (Jan 16) | Ready for replacement
│
├── 🟡 ⏳ Test Screw/Rubber GUI and report issues
│   └── Owner: Jalol, Samrah | Status: From CustomPendingTasks_Screw.md (Jan 28) | CRITICAL - System quality
│
└──────────────────────────────────────────────────────┘
```

---

## 🟢 Important / Low Priority Issues

```
📁 IMPORTANT ISSUES
│
└── 🟢 ⏳ Prepare system documentation and handover package for Everint
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
├── 📋 ⏳ [screw] Robot finger with spring mechanism for PCB robot
│   └── Owner: Ammad | Status: In progress | Needs completion
│
└── 📋 ⏳ [screw] Adjustable Label printer aligner jig for worker placement
    └── Owner: Kwanghyeop | Status: In progress | Needs completion
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
- 🔍 = Missing Item / Information Gap (moved to [MISSING_TASKS.md](./MISSING_TASKS.md))
- ⚠️ = Risk / Dependency
- 📅 = Deadline

---

**Related Files:**
- [COMPLETED_TASKS.md](./COMPLETED_TASKS.md) - All completed tasks archive
- [MISSING_TASKS.md](./MISSING_TASKS.md) - Tasks not in Asana (need review)
- [BLINDSPOTS.md](./BLINDSPOTS.md) - PM perspective gaps and risks
- [ASANA_PENDING_TASKS.md](./ASANA_PENDING_TASKS.md) - Tasks ready for Asana

---

**Note:** This checklist now contains only tasks that match Asana screenshots. All tasks should be verified and tracked in Asana. Status and urgency may change based on project progress.
