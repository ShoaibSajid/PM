# Pending Tasks for Asana

**Last Updated:** January 30, 2026 (Updated based on Asana completion status)  
**Purpose:** Copy-paste into Asana. Each task has **Title**, **Description**, and **1 Owner**.

**Note:** Tasks marked with ~~strikethrough~~ and ✅ are completed and should not be added to Asana.

**Completed Tasks (Jan 30):**
- Install damper on conveyor (Ammad)
- Check/Save GUI parameters change for vision models (Jalol)
- Assembly Process Product Image 1 (Samrah)
- [screw] Robot Config (Product Specs YAML file) (Sawera)
- Integrate misalignment warning messages for rubber foot at cycle end (Tugi)
- Dump Timestamps for each cycle (Tugi)
- Control pallet conveyor from framework using PLC Signal (Tugi)

---

## ⚠️ Tasks Already in Asana (DO NOT ADD)

These tasks are already present in Asana and should NOT be added again:

| # | Title | Owner | Asana Status |
|---|--------|--------|--------------|
| 3 | Fix printer tilt – depth-based angle adjustment (Screw Robot) | Ammad | Pending |
| 4 | Fix screw bit drift from pickup position (Screw Robot) | Ammad | Pending |
| 16 | Integrate Omron camera / top camera (Screw Robot) | Hieu | Pending |
| 20 | Test GUI and find issues (Screw Robot) | Jalol | Pending |
| 22 | Integrate Fairino collision signal (Screw/Rubber) | Ammad | Pending |
| 23 | Add depth outlier filtering (Screw Robot) | Tan | Pending |
| 24 | Fairino error handling (Screw Robot) | Ammad | Pending |
| 25 | Merge screw/rubber code and test (Rubber Robot) | Hieu | Pending |
| 27 | Install finger gripper (Rubber Robot) | Tugi | Pending |
| 28 | Integrate finger gripper in code (Rubber Robot) | Tugi | Pending |
| 30 | Reposition platform and rubber pad holders (Rubber Robot) | Tugi | Pending |
| 36 | Speed up robot to meet cycle time (Screw Robot) | Hieu | Pending |
| 37 | Speed up robot to meet cycle time (Rubber Robot) | Tugi | Pending |
| 38 | Integrate self-training logic (Rubber Robot) | Tugi | Pending |
| 58 | Order screw bits (Screw Robot) | Kwanghyeop | Pending |
| 60 | Link screw/rubber robots to pre-pickup rubber pad (Both systems) | Tugi | Pending |
| 61 | Rubber pad pictures every cycle and offset (Rubber Robot) | Tugi | Pending |
| 66 | Ensure spares for each 3D printed part (Both systems) | Muazzam | Pending |
| 70 | Equipment list – installed and pending (Both systems) | Kwanghyeop | Pending |
| 71 | 3D parts list (Both systems) | Muazzam | Pending |
| 72 | Maintain 3D components tracking list (Both systems) | Myeongun | Pending |
| 73 | Finger replacement (Rubber Robot) | Tugi | Pending |
| 83 | Complete handover documentation package | Kwanghyeop | Pending |

---

## ✅ Tasks NOT in Asana (ADD THESE)

These tasks are NOT currently in Asana and should be added:

### Critical / Blocking

| # | Title | Description | Owner |
|---|--------|-------------|--------|
| 1 | Fix manual registration issue (Both systems) | GUI registration issue blocks product registration. Ensure manual registration works and product details/images persist. Critical for demo. | Jalol |
| 2 | Register all products with new code (Both systems) | Only 2 products done (XD5-40D, XD3-40D). Complete registration for all products once manual registration is fixed. | Hieu |
| 5 | Fix metal finger spacing (Both systems) | Finger spacing incorrect; add plastic sheet or thin flat washer as needed. | Myeongun |
| 6 | Provide finger spares (Both systems) | No spares for fingers available. Prepare spares for production continuity. | Myeongun |
| 7 | Install dedicated bracket for screw mirror (Screw Robot) | Replace magnetic base with fixed, repeatable bracket for mirror (vibration makes current setup unstable). | Muazzam |
| 8 | Complete 2D camera hardware installation (Both systems) | Finish 2D camera installation for full system functionality. | Muazzam |
| 9 | Request continuous roll rubber pad sheets 8xN (Rubber Robot) | Request 8xN continuous roll instead of 8x8 sheets to reduce jams in roller area. | Kwanghyeop |
| 10 | Conveyor position adjustment / fix (Both systems) | Adjust or fix conveyor position. Critical for demo. | Ammad |
| 11 | Fix out-of-place product on conveyor (Both systems) | Products misaligned cause collision. Use top camera to ensure product is in acceptable zone. | Ammad |
| 12 | Fix screw pickup validation – 2nd feeder FPs (Screw Robot) | Resolve remaining false positives/negatives for model 2 screw feeder validation. | Hieu |
| 13 | Fix rubber foot ROI detection (Rubber Robot) | Tighter mechanism makes ROI from GUI wrong. Fix for accurate detection. | Rizwan |
| 14 | Test rescan logic (Rubber Robot) | Test rescan logic after vision fixes. Rolled back previously due to issues. | Tugi |
| 15 | Integrate rubber pad pickup offset (Rubber Robot) | Integrate pickup offset for rubber pad in robot framework. | Tugi |
| 19 | Fix upper light holder (Screw Robot) | Replace temporary tape fix with proper upper light holder. | Ammad |
| 21 | Capture depth maps with different light settings (Screw Robot) | Capture depth maps under different lighting for vision analysis and tuning. | Tan |
| 29 | Grind / scrub sheet roller (Rubber Robot) | Maintain sheet roller for reliable feeding. | Tugi |
| 31 | 3D print dual fingers for scoop (Rubber Robot) | Design and print dual fingers for scoop; confirm tilt angle with Saad. | Myeongun |
| 32 | 3D print catching basket for sheets/rubbers (Rubber Robot) | Design and print basket for catching sheets/rubbers. | Myeongun |
| 33 | Sheet clamp design to curve/bend sheet (Rubber Robot) | Design and print clamp to curve/bend sheet. | Myeongun |

### High Priority

| # | Title | Description | Owner |
|---|--------|-------------|--------|
| 34 | Improve calibration accuracy (Rubber Robot) | Reduce position error for attachment accuracy. | Tugi |
| 35 | Method for irregular rubber foot shape (Rubber Robot) | Define method to handle irregular rubber foot shape for consistent attachment. | Tugi |
| 39 | Install buzzers for error/warning (Both systems) | Install buzzers for system halt and warning. | Muazzam |
| 40 | Redesign Fairino fingers for gripping (Both systems) | Improve finger design for better grip (e.g. metal/inward bent). | Myeongun |
| 41 | Install vertical plates for straight screws (Screw Robot) | Install vertical plates so screws are straight in feeder. | Ammad |
| 42 | Integrate buzzer alarm (Both systems) | Integrate buzzer in framework for start/finish/error. | Ammad |
| 43 | Install remaining hardware per government report | Complete installation per government report. | Muazzam |
| 44 | Install all cameras from hardware list (Both systems) | Install all cameras and equipment from purchase list. | Muazzam |
| 45 | Use product size to tighten YOLO bbox (Both systems) | Use product size in vision to tighten detection bbox and avoid false detections. | Rizwan |
| 46 | Maintain detection size history for tighter bboxes (Both systems) | Keep history of last n detections for tighter bboxes. | Rizwan |
| 47 | Analyze Omron images for printer displacement (Both systems) | Use Omron camera to detect wrong printer displacement after installation. | Shams |
| 48 | Finalize GUI for PCB/Screw/Rubber | Complete GUI for all three systems. | Jalol |
| 49 | Make error message display changes in GUI (Both systems) | Implement GUI side of error message display (framework side done by Hieu/Tugi). | Jalol |
| 50 | Fix conveyor operation guide (Both systems) | Update and validate conveyor operation guide. | Ammad |
| 51 | Use Omron to detect rubber foot mis-attachment (Rubber Robot) | Use Omron camera for mis-attachment detection. | Odil |
| 52 | Train lightweight product presence detector (Omron) (Both systems) | Train detector for product presence in safe gripping zone. | Odil |
| 53 | Organize images in product folder structure (Both systems) | Organize images (e.g. 5–6 per product) into product ID folders. | Odil |
| 54 | Install mirror for model 2 (Screw Robot) | Install mirror for model 2 screw validation. | Haider Shah |
| 55 | Capture scooped rubber foot images after scooping (Rubber Robot) | Capture and save images after scooping for vision tuning. | Tugi |
| 56 | Test rolling/gripper-based rubber pickup (Rubber Robot) | Test alternative pickup mechanism. | Ammad |
| 57 | Prepare spare for vacuum box with motor (Rubber Robot) | Prepare complete spare for production continuity. | Tugi |
| 59 | Work on new rubber pad design (Rubber Robot) | Explore new rubber pad design for pickup. | Tugi |
| 62 | Fix screw validation logic – range and tilt (Screw Robot) | Fix range and tilt angle logic to reduce false positives/negatives. | Hieu |
| 64 | Prepare checkerboards and Aruco codes (Both systems) | Print checkerboards and Aruco codes for calibration. | Tan |
| 65 | Bring new ethernet cables from lab (Both systems) | Replace unstable cables. | Ammad |
| 67 | Create Excel – GUI tasks and issues status (Both systems) | Maintain Excel with GUI tasks, issues, owner, target date. | Jalol |
| 68 | Collect dataset for vision model testing (Rubber Robot) | Collect dataset when operation is stable. | Rizwan |
| 69 | Complete vision model validation summary (Both systems) | Finalize vision validation summary for handover. | Rizwan |
| 74 | Fix temporary anti-shake solution for DX220 (Screw Robot) | Replace temporary solution with permanent fix. | Ammad |
| 75 | Document fasten torque for mobile printer screw (Screw Robot) | Document torque value (3.5–4 kgf.cm) for mobile printer screw. | Ammad |
| 76 | Evaluate reducing platform height for motion optimization (Rubber Robot) | Evaluate lower platform height for motion optimization (requested by Muazzam). | Tugi |
| 77 | Update screw hole positions for fastening (Rubber Robot) | Update screw hole positions after rolling pad dispenser position change. | Muazzam |
| 78 | Modify platform to place three dispensers (Rubber Robot) | Modify platform to accommodate three dispensers. | Muazzam |
| 79 | Finish PCB registration part (PCB) | Complete registration flow in PCB GUI/code. | Jalol |
| 80 | Add gripper size adjustment feature (PCB) | Add GUI/framework feature to adjust gripper size as discussed in meeting. | Tan |
| 81 | Provide raw depth data to vision team (~50) (Screw Robot) | Provide raw depth data for vision team analysis. | Tan |

### Follow-up / Lower Priority

| # | Title | Description | Owner |
|---|--------|-------------|--------|
| 82 | Fix auto registration GUI bug – saving SVG (Both systems) | Fix random bug that prevents saving annotation results. Do after manual registration fix. | Jalol |

---

**Note:** When multiple owners were listed in source docs, the first name was chosen as the single owner. Adjust in Asana as needed.

**Summary:**
- **Tasks already in Asana:** 22 tasks (do not add)
- **Tasks NOT in Asana:** 61 tasks (add these)
- **Completed tasks:** 7 tasks (do not add)
