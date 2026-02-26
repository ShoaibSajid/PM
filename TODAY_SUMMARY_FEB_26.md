# Everint Today Summary (2026-02-26)

**Source baseline:** Kakao updates plus direct individual updates received on 2026-02-26 (Screw Robot, Rubber Foot, Vision)

---

## Today Updates

### Screw Robot

#### Completed

1. Added dry mode using maintenance-mode button in GUI.
2. Corrected `move_l` to enforce linear move behavior.
3. Added `move_j` usage for motion-completion checks.
4. Added gripper JRT initialization and related failure handling.
5. Added gripper opening feedback check.
6. Added no-feedback closing check path for gripper close.
7. Added hole-surface position for `index[2]` in maintenance mode.
8. Added debug commands: `screwdriver_on` and `screwdriver_off`.
9. Added error message for JRT init failure.
10. Added error message for maintenance-mode proceeding path.
11. Added parser support for maintenance-mode button from GUI messages.
12. Corrected `_queue` empty check in `wait_and_pop_msg`.
13. Reduced command execution interval from ~10ms to ~2ms.

#### Remaining

1. Keep 24V to 27V screwdriver supply increase as backup-only optimization, not immediate action.
2. Add offsets to detection points.
3. Run/refresh vision calibration.

### Vision (Model 1)

1. Detection accuracy still needs verification against latest detection images.
2. Hole annotation style should follow dot/circular convention.

### Rubber Foot

1. Reviewed and verified Ghulam model-update PR against main framework.
2. Refined pad-refill and pad-pick detection logic.
3. Tested single-dispenser persistence until depletion, then shift to next dispenser.
4. Validated alarm-trigger scenarios and rescan flow.

### Response Notes Captured

1. Grip verification rule: check position changes every ~200ms; if position is stable, treat it as gripped.
2. Screwdriver voltage increase is deferred unless cycle-time pressure requires it.

---

## Action Packaging For Tracking

- Screw: preserve maintenance/debug improvements and close remaining detection-offset + calibration tasks.
- Rubber: keep depletion-first dispenser policy and validated alarm/rescan behavior in production test runs.
- Vision: prioritize model-1 detection review with annotation-format alignment and calibration closure.
