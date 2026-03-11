# Everint Today Summary (2026-03-11)

**Source baseline:** Kakao main-group updates plus last-2-weeks debug-group updates reviewed on 2026-03-11

---

## Today Updates

### Vision / Registration

1. Top-camera calibration scope was clarified:
   - capture a top-camera image with a measurement scale on the conveyor
   - derive pixel-to-mm ratio
   - return printer width/height together with scan results
2. Everint requested registration of 2 new PCB products on 2026-03-11.
3. March chat history still shows unresolved registration/config persistence risk:
   - registration was sometimes unreliable in testing
   - config generation was reported missing multiple times on 2026-03-03

### Screw / Rubber Reporting

1. Error-counting structure was discussed in detail for rubber-foot output.
2. Shoaib asked for grouped failure visibility plus per-index drill-down:
   - overall screw failures / pad failures
   - per-hole or per-pad failure counts for diagnosis

### Hardware / Ops

1. The printer guide / aligner remains installed only on one side and is still 3D printed.
2. Requested follow-up:
   - convert it to metal
   - install on both sides
3. Everint added a ball flange and reduced conveyor speed to help pallet damping; effect still needs observation.

### Deployment Preparation

1. Before future Everint deployment, one lab system should remain ready with:
   - GUI
   - Robot Framework
   - Vision
2. This was requested to reduce deployment risk and make full-stack verification possible before site rollout.

---

## Action Packaging For Tracking

- Keep registration-finalization tasks open and explicitly include the new PCB-product registration demand in follow-up planning.
- Treat the top-camera pixel-to-mm + width/height return requirement as a separate tracked item unless it is merged into an existing vision-registration task.
- Keep hardware follow-up on the printer guide / aligner visible until the metal two-sided installation is complete.
- Expand reporting expectations around grouped and per-index failure counts while keeping the line stable during production runs.

---

## Additional Planning Notes For Tomorrow

1. **Product shifting**
   - Vision team: update model to return offset in mm.
   - Robot team: implement Fairino left/right movement control using the returned offset.

2. **DB table update**
   - Jalol: test locally, then deploy on production machine.
   - After DB update, Tugi, Hieu, and Samrah should start framework/frontend integration so graphs show the new DB structure correctly.

3. **Finalize scanning strategy**
   - Decide between:
     - 2-shot strategy:
       - upper rubber pad shot
       - lower rubber pads shot
       - robot-side 2-shot support already implemented by Tugi
       - second-shot integration depends on updated vision model
     - 1-shot strategy with extra light:
       - vision team must finalize light type, placement, and control
   - Registration cost must be treated as a decision constraint because changing light or exposure forces product re-registration.

4. **Conveyor damping**
   - Kwanghyeop: finalize conveyor damper.
   - Replace sponge used to apply damping force to the conveyor.

5. **Remaining carry-over items**
   - Aligner jig
   - 3rd dispenser metal plate
   - Isolation of registration/configs of both robots
   - GUI graphs
   - Log-based analysis for attempts, success, failures
   - Conveyor stop / auto-manual signal
