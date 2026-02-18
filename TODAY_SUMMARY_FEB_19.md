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
