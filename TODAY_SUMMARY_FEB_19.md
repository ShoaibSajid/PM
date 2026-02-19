# Everint Today Summary (2026-02-19)

**Source baseline:** KakaoTalk updates through 2026-02-18 15:07:48 (KST)

---

## Screw Driver

- Finalize mirror stability and remove temporary mounting risk before longer runs.
- Continue investigation of first/last screw reliability and cycle-time timeout edge cases.
- Fix angle behavior where screwdriver bit can come out of screw head.
- Investigate depth insufficiency using Z-value logs.
- Reduce hole-detection latency (currently 800-950ms per detection).
- Fix top-right and bottom-right hole position inaccuracy.
- Resolve camera frame capture synchronization issues.
- Stabilize intermittent Model-1 crashes.
- Validate detection of improper screw grip from mirror images.
- Keep production runs collecting error-tagged evidence for unresolved screw failures.

## Rubber Foot

- Verify depth/tilt behavior under current rescan strategy and confirm no regression.
- Resolve rubber index/order and hole-center inconsistency with focused test cases.
- Complete and validate 3-dispenser pickup-point setup under production-like cycles.
- Track misplaced pad cases with image-linked logs for faster root-cause closure.
- Implement pending config settings from GUI submenu for rubber workflow.

## PCB

- Confirm PCB light controller issue root cause and stabilize hardware wiring behavior.
- Ensure spare light controller availability and assign storage/ownership.
- Verify system state transitions around lighting are reflected correctly in operations.
- Install new vertical sensor.
- Measure and design the required L-shape bracket for the vertical sensor.

## Everint-Wide

- Prevent terminal process kills from cascading into GUI/backend shutdown.
- Add success/failure counters to Screw/Rubber GUI to match PCB visibility.
- Fix MQTT queue guard logic so final queued popup is not dropped.
- Keep daily shift plan aligned with current staffing and production goals.

---

## Whiteboard Sync (2026-02-19, on-site)

### Rubber Foot

- Robot: complete 3-dispenser production logic integration and re-verify after logic-test fixes.
- Robot: finish vision integration for dispenser pad XY points and keep depth/tilt path disabled until re-validated.
- Robot: add sanity guardrails (3 tries per rubber index; reject model outputs when `x,y,z,rx,ry,rz` are out of range).
- Vision: complete depth/tilt estimation path for first scan plus rescan flow.
- Vision: finalize rubber-foot position handling (skipped-index behavior and on-site training closure).
- Vision: finalize dispenser-rubber-pad coordinates (XY for 2nd row and XY per pad slot).
- Hardware: close remaining metal conversion + camera/finger-base mounting items.

### Screw Driver

- Robot: continue production observation and rectify first-screw angle/position drift and small-screw position misses.
- Robot: re-tune screw depth envelope by screw type/position and validate additional depth margin (+2mm trial).
- Robot: re-test feeder-empty handling and debug-mode re-screw behavior.
- Robot: expose Fairino position controls in GUI and continue cycle-time reduction.
- Vision: reduce runtime overhead tied to `Rx/Ry/Rz` handling and repeated rescans.
- Vision: fix shifted screw-hole detection that can cause collision, and reduce false non-circle S-hole results.
- GUI: add screw type selection in registration and Fairino position control from GUI.
- Hardware: complete gripper wiring to tool flange and close remaining metal/Fairino finger parts.

### Cross-Cutting

- Add/verify exit strategy behavior and emergency signal handling.
- Implement rule to ignore printers with level greater than 1 during automated flow.
