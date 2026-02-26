# Proposed Schedule (2026-02-23 to 2026-03-01)

## Non-blocking scheduling rules used
- Run hardware-dependent tasks in parallel with software-only tasks.
- Put unblockers first (startup reliability, calibration prerequisites).
- Reserve daily handoff windows to prevent cross-team idle time.

## Proposed plan
- Mon (Feb 23):
  - Track A (Rubber/Framework): finalize startup safety + preflight checklist.
  - Track B (GUI/Infra): verify counters/popups/paths in clean reboot scenario.
  - Track C (Ops): lock procurement/install slots for controller + calibration support.
- Tue (Feb 24):
  - Track A: rubber offset/depth tuning loop (controlled no-LED and exposure variants).
  - Track B: screw/PCB configuration cleanup and port consistency checks.
  - Handoff: end-of-day merged parameter set for Wed validation.
- Wed (Feb 25):
  - Joint validation day: 10-printer acceptance run using Tue merged settings.
  - Parallel fallback lane: while validation runs, GUI team closes non-blocking polish tickets.
- Thu (Feb 26):
  - Hardware install/calibration window (if parts/support available).
  - In parallel: regression checks for dispenser logic and emergency signal behavior.
- Fri (Feb 27):
  - Buffer + closure day: unresolved blockers only, then Asana cleanup and documentation sync.
- Sat-Sun (Feb 28-Mar 1):
  - Optional light monitoring + report prep; avoid new dependency-creating work.

## Why this avoids blocking
- No team waits for a single critical handoff before starting work.
- Validation is scheduled after prerequisites, with a parallel fallback lane.
- Hardware uncertainty is isolated to a bounded window, not the entire week.
