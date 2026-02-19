# Everint Today Summary (2026-02-19)

**Source baseline:** Latest Asana sync (`ASANA_TASKS_LIST.md` / `ASANA_TASKS_RAW.json`, synced 2026-02-19 14:45:08)

---

## Shared Context

- Latest chat anchor: **2026-02-18 15:07:48** (Shoaib: "I will send a list of tasks in a while.")
- Related files: [URGENT_ISSUES_CHECKLIST.md](./URGENT_ISSUES_CHECKLIST.md), [TASKS_MISSING_IN_ASANA_RAW_REVIEW.md](./TASKS_MISSING_IN_ASANA_RAW_REVIEW.md), [CHAT_ANALYSIS_FEB_10_18.md](./CHAT_ANALYSIS_FEB_10_18.md), [README.md](./README.md)

---

## Current Asana Snapshot

- Projects tracked: Everint, everint, PCB, Screw Driver, Rubber Foot, Unassigned Tasks, AI Robot 2026
- Deduplicated tasks in raw: 185
- Pending tasks: 115
- Completed tasks: 70
- Pending in Unassigned Tasks: 0
- Pending in AI Robot 2026: 33 (renamed/split review items)

---

## Today Focus by System (Everint)

### Screw Driver (Label Printer Screw Robot)

- Finalize product registration testing (manual + auto) for screw/rubber.
- Fix printer tilt (depth-based angle adjustment) and screw bit drift after screwing.
- Close first-screw angle + small-screw position reliability; retune screw-depth range (+2mm trial).
- Re-test feeder-empty handling and reduce rescan count overhead.
- Keep GUI registration field, counters, and error-message flow aligned with screw workflow.

### Rubber Foot Robot

- Finalize rescan logic and integrate rubber-pad offset after scooping.
- Complete 3-dispenser handling, skipped-index handling, and per-pad XY mapping.
- Add model-pose range guards to prevent invalid pad placements.
- Integrate finger-gripper sequence and reposition platform for 3 holders.
- 3D print and install the catching basket.

### PCB Screw Robot

- Finalize product registration testing (manual + auto) for PCB.
- Complete vertical sensor + L-shape bracket workflow.
- Resolve PCB light controller reliability and spare strategy.
- Test OBB DETR model for PCB detection.

---

## Priority Focus (From AI Robot 2026)

### Framework

- Complete 3-dispenser handling and pickup/rescan edge-case reliability.
- Close cycle-time/runtime controls: cycle interval feedback loop, timeout handling, pause, feeder-empty, conveyor signal tests, Fairino speed optimization.
- Keep rubber robot startup/sanity safeguards active and validated.

### GUI

- Finalize screw-type registration field with DB persistence.
- Ensure success/failure counters for Screw/Rubber are complete and accurate.
- Confirm terminal-kill isolation (terminal should not kill GUI/backend).

### Vision

- Complete screw-hole robustness fixes (non-circle false rejection, cycle-time overhead).
- Close rubber-foot indexing and wrong-hole-center reliability work.
- Finish on-site training integration and low-priority depth-assisted registration support.

### Hardware / Ops

- Complete vertical sensor + L-shape bracket workflow.
- Resolve PCB light controller reliability with spare strategy.
- Finish wrinkling/pickup stability, metal conversion items, and production-observation closures.

---

## Tracking Rule

`TASKS_MISSING_IN_ASANA_RAW_REVIEW.md` is now strict missing-only and currently empty.
Use `AI Robot 2026` to triage/reassign split review work.
