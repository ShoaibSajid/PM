# Tasks Missing In Asana (Consolidated)

**Last Updated:** February 19, 2026 (Whiteboard sync added)  
**Purpose:** Single source of truth for tasks discussed in chat/member updates but not reliably tracked in Asana.  
**Dedup Policy:** Duplicate or near-duplicate tasks are merged into grouped task items below.

---

## Asana Raw Cross-Check

- Generated: 2026-02-19 07:37:27
- Source list file: `ASANA_TASKS_LIST.md`
- Source raw file: `ASANA_TASKS_RAW.json`
- List tasks evaluated: 118
- Raw tasks available: 139
- Missing in raw: 0
- Result: no tasks from `ASANA_TASKS_LIST.md` are missing in `ASANA_TASKS_RAW.json`

---

## Consolidated Missing Tasks (Deduplicated)

## 1) Screw Driver

- Stabilize screw feeder mirror setup and finalize special jig/mechanical design for reliable production.
  Owners: Vision + Mechanical (Odil, Haider, Shams)
- Resolve screw fastening quality issues in one grouped effort:
  angle issue (bit coming out of screw head), insufficient depth (Z-log analysis), top-right/bottom-right hole position inaccuracy, and improper screw grip detection from mirror images.
  Owners: Hieu, Ammad, Vision team
- Reduce cycle-time overhead from vision pipeline:
  hole detection latency (800-950ms), inference-time reduction, and frame-capture synchronization.
  Owners: Vision team
- Stabilize Model-1 reliability:
  return-data inconsistency (depth append), intermittent crashes, and validation of first-image-center depth method on real inference.
  Owners: Rizwan, Quy Ninh, Vision team
- Continue production-side optimization:
  cycle timeout handling and queued follow-up issue list closure for Screw/Rubber.
  Owners: Tugi, Hieu
- Complete grouped screw runtime stabilization from on-site whiteboard:
  production observation + rectify loop, first-screw angle/position stabilization, small-screw position reliability, screw-depth envelope validation by position/type (including +2mm trial), debug-mode re-screw behavior, and feeder-empty logic re-test.
  Owners: Hieu, Tugi, Robot team
- Complete grouped screw GUI/control integration:
  screw-type field in registration and Fairino position control from GUI.
  Owners: Jalol, Hieu

## 2) Rubber Foot

- Execute grouped calibration and positioning package:
  R-foot calibration across products/printer types, offset tuning, wrong-hole-center analysis, and rubber index/order anomaly root-cause.
  Owners: Tugi, Rizwan, Vision team
- Complete grouped rubber hardware package:
  sheet clamp design, roller assembly scale-up (3 units), aluminum bracket redesign, 3-column mounting plates, and plastic-to-metal finalization for scooper/finger-nail-related parts.
  Owners: Myeongun, Tugi, Muazzam, Mechanical team
- Resolve wrinkling and pickup stability issues, then validate in production-like long runs.
  Owners: Robot + Vision teams
- Implement and validate grouped dispenser/flow tasks:
  3-dispenser handling plus pickup/rescan edge-case reliability.
  Owners: Tugi, Muazzam
- Add grouped rubber robot sanity package from on-site whiteboard:
  logic integration hardening, three-tries-per-index safeguard, and pose-range validation for `x,y,z,rx,ry,rz`.
  Owners: Tugi, Hieu

## 3) PCB

- Install new vertical sensor and complete the required L-shape bracket workflow (measure -> design -> fabricate -> install).
  Owners: PCB hardware + Mechanical team
- Resolve PCB lighting/controller reliability and maintain at least one spare controller strategy.
  Owners: Ammad, Kwanghyeop, Saad

## 4) GUI / Software / Framework

- Complete grouped GUI robustness package:
  terminal kill isolation (terminal should not kill GUI/backend), robot-active status consistency, and submenu config settings implementation.
  Owners: Jalol, Framework/GUI team
- Implement grouped operations visibility package:
  success/failure counters for Screw/Rubber (same standard as PCB), GUI issue/status tracking, and final GUI testing/layout cleanup.
  Owners: Jalol, Tan
- Fix grouped messaging/control issues:
  MQTT queue guard logic for missed final popup, error-message display completion, and conveyor operation guide validation.
  Owners: Tugi, Hieu, Jalol, Ammad
- Complete grouped framework/robot control backlog:
  add_command blending and tolerance upgrades, extra linear blend-zero point, duration-based signal stop, pause functionality, feeder-empty handling, conveyor signal testing, and Fairino speed optimization.
  Owners: Ammad, Hieu, Muazzam

## 5) Vision / Detection

- Complete grouped detection-improvement package:
  product-size-aware bbox tightening, detection-size history averaging, ROI robustness under tighter mechanism, and Omron-based displacement/mis-attachment detection.
  Owners: Rizwan, Haider Shah, Odil, Shams
- Train and deploy lightweight Omron product-presence detector for safe gripping zone checks.
  Owners: Odil
- Organize image/data structure by product and ensure scooped-image capture quality for model improvement.
  Owners: Odil, Shoaib, Tugi, Hieu
- Verify and use tilt angle in motion pipeline where required.
  Owners: Hieu, Vision team
- Complete grouped rubber-foot position tracking updates:
  skipped-index handling, per-pad XY mapping (including 2nd row), and on-site training closure.
  Owners: Vision team, Tugi
- Complete grouped screw-hole robustness updates:
  shifted-hole collision-risk fix, false S-hole non-circle rejection reduction, and rescan-count optimization.
  Owners: Vision team, Hieu

## 6) Hardware / Ops / Vendor / Documentation

- Complete grouped Fairino hardware readiness package:
  redesigned fingers (including all products + spare), position adjust per printer, vertical plates for straight screw insertion, and remaining government-report hardware installations.
  Owners: Saad, Myeongun, Jalol, Muazzam, Ammad, Hieu
- Complete grouped factory-ops readiness package:
  clear conveyor process, camera/equipment installation closure, stable ethernet replacement, and manager-facing operational checks.
  Owners: Kwanghyeop, Muazzam, Ammad
- Complete grouped external/vendor dependencies:
  Fairino SDK training/vendor follow-up and mobile-printer flange-hole height measurements.
  Owners: Ammad, Kwanghyeop
- Complete grouped reporting/dataset package:
  Book.xlsx updates, PPT evidence set (48 images), dataset collection, and vision model validation summary.
  Owners: Hieu, Tugi, Rizwan, Tan, Vision team
- Complete grouped support material tasks:
  checkerboards/Aruco prep and site-provided M4 bolt-length / shallow-hole print support.
  Owners: Tan, Myeongun, Hieu
- Complete grouped whiteboard hardware closure:
  gripper wiring to tool flange, remaining metal component conversion, Fairino finger completion, and camera/finger-base mounting items.
  Owners: Muazzam, Ammad, Mechanical team
- Complete grouped safety/operations behavior updates:
  exit strategy behavior, emergency signal handling, and ignore-printers-with-level-greater-than-1 rule.
  Owners: Framework + Operations teams

---

## Merged Similar Items (Traceability)

- Buzzer-related tasks merged:
  `Install buzzers for error/warning display` + `Integrate buzzer alarm - Both systems`.
- GUI stability tasks merged:
  `GUI active/inactive mismatch`, `terminal kill cascade`, `submenu config missing`, and `GUI finalize/testing/layout`.
- Screw quality tasks merged:
  `angle`, `depth`, `position accuracy`, and `improper grip detection`.
- Vision performance tasks merged:
  `reduce inference time`, `hole detection latency`, and `camera frame sync`.
- Model-1 tasks merged:
  `data type inconsistency`, `crash`, and `first-image-center depth validation`.
- PCB hardware tasks merged:
  `new vertical sensor` + `L-shape bracket design`.

---

## Source Windows Used

- Chat updates (Feb 1-2, Feb 2-4, Feb 10-18, Feb 19 team member update)
- Member-list pending items (Rubber/Screw)
- Historical high-priority missing backlog from prior `MISSING_TASKS.md`
