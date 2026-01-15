# Urgent Tasks

**Last Updated:** January 15, 2026 (Updated from Jan 15 chat)  
**Timezone:** Asia/Seoul (KST)

**Note:** PCB system is almost complete and running. Ammad (Robot/Framework) and Tan (Vision) are currently helping other robot systems (Hieu, Tugi) as additional resources.

---

## 🔴 Critical / Blocking (High Urgency)

### Robot Teaching & Integration
- **Task:** Complete robot teaching for Label Printer Screw Robot (FR3)
  - **Owner:** Hieu
  - **Status:** In progress (as of Jan 14)
  - **Next Follow-up:** Confirm completion and share video
  - **Risk:** Blocks cycle time testing and vision integration

- **Task:** Complete robot teaching for Label Printer Rubber Foot Robot (FR3)
  - **Owner:** Tugi
  - **Status:** Completed (as of Jan 15) - video sent, but broken pad holding bracket causing misalignment
  - **Next Follow-up:** Fix pad holding bracket, verify alignment
  - **Risk:** Blocks vision model testing

### Vision Integration
- **Task:** Integrate new vision model output format (Rizwan's final format) to both vision and robot framework
  - **Owner:** Hieu (integration), Rizwan (model)
  - **Status:** Tugi merged updates from Hieu (Jan 14), Hieu updated again (Jan 15 morning), Tugi needs to merge and test
  - **Next Follow-up:** Tugi to merge latest vision updates and test
  - **Risk:** Blocks full cycle testing

- **Task:** Test rescan logic (Rubber Foot Robot)
  - **Owner:** Tugi
  - **Status:** Overall operation working, rescan logic needs testing (as of Jan 15)
  - **Next Follow-up:** Test rescan functionality
  - **Risk:** Affects operation reliability

- **Task:** Complete vision integration status summary for all models
  - **Owner:** Rizwan
  - **Status:** In progress
  - **Deadline:** January 15, 2026
  - **Next Follow-up:** Share summary document

### Cycle Time Validation
- **Task:** Confirm cycle time for Label Printer Screw Robot
  - **Owner:** Hieu, Saad (review)
  - **Status:** Pending robot teaching completion
  - **Next Follow-up:** Measure and document cycle times
  - **Risk:** Critical acceptance criteria

- **Task:** Confirm cycle time for Label Printer Rubber Foot Robot
  - **Owner:** Tugi, Saad (review)
  - **Status:** Roughly 34 seconds (as of Jan 15), room for improvement
  - **Next Follow-up:** Optimize and finalize cycle time
  - **Risk:** Critical acceptance criteria

---

## 🟡 High Priority (Medium-High Urgency)

### GUI Issues
- **Task:** Fix product image display issue (images disappear when product details changed)
  - **Owner:** Tan, Samrah
  - **Status:** ✅ Fixed (Jan 7) - rename logic disabled and pushed to main
  - **Next Follow-up:** Monitor for any regressions
  - **Risk:** Affects product registration workflow

- **Task:** Fix GUI freezing issue (disabling function while waiting for robot acknowledgment)
  - **Owner:** Jalol
  - **Status:** Reported Jan 14, needs investigation
  - **Next Follow-up:** Debug and fix freezing issue
  - **Risk:** Affects operational workflow

- **Task:** Create Excel file with status of all pending GUI tasks and issues
  - **Owner:** Jalol
  - **Deadline:** January 15, 2026
  - **Status:** Requested Jan 14
  - **Next Follow-up:** Share file for review

### Vision Model Validation
- **Task:** Collect dataset for vision model testing (Rubber Foot Robot)
  - **Owner:** Rizwan, Shams, Tugi, Hieu
  - **Status:** Waiting for robot teaching completion
  - **Next Follow-up:** Capture dataset once robots running smoothly
  - **Risk:** Blocks vision validation (10-20 products required)

- **Task:** Complete vision model validation summary for all systems
  - **Owner:** Rizwan
  - **Status:** In progress
  - **Next Follow-up:** Complete summary document
  - **Risk:** Required for handover acceptance

### Documentation & Inventory
- **Task:** Complete handover documentation package
  - **Owner:** Kwanghyeop (lead), team support
  - **Status:** Tasks created in Asana, work in progress
  - **Includes:**
    - System operation procedures
    - Maintenance guidelines
    - Installed equipment lists (with serial numbers and locations)
    - Vision system details (cameras, mounting, lighting)
    - System overview
  - **Additional:** Jalol creating step-by-step product registration guide, Sawera preparing operation manuals
  - **Next Follow-up:** Review progress on assigned subtasks
  - **Risk:** Required for project handover

- **Task:** Equipment list (installed and pending delivery)
  - **Owner:** Kwanghyeop
  - **Status:** Requested Jan 14
  - **Next Follow-up:** Maintain shared file with delivery dates
  - **Risk:** Missing items may delay handover

- **Task:** 3D parts list
  - **Owner:** Muazzam, Ammad
  - **Status:** In progress (as of Jan 15)
  - **Next Follow-up:** Complete inventory list
  - **Note:** Critical for tracking components and spares

---

## 🟢 Important (Medium Urgency)

### Acceptance Criteria
- **Task:** Define list of targets required to pass Everint project
  - **Owner:** Saad, Odil
  - **Status:** Requested Jan 14
  - **Deadline:** Friday (target achievement)
  - **Next Follow-up:** Share target list for alignment

---

## 📋 Follow-up Required

### Pending Responses
- **Task:** Review and respond to assigned Asana tasks
  - **Owner:** All team members
  - **Status:** Requested Jan 14
  - **Next Follow-up:** Check assigned tasks and share updates

### Data Collection
- **Task:** Capture production data for vision model validation
  - **Owner:** Vision team, Robot team
  - **Status:** Waiting for stable robot operation
  - **Next Follow-up:** Begin systematic data collection

### Hardware Issues
- **Task:** Fix broken pad holding bracket (Rubber Foot Robot)
  - **Owner:** Tugi, Hardware team
  - **Status:** Broken bracket causing misalignment (reported Jan 15)
  - **Next Follow-up:** Replace bracket, verify alignment
  - **Risk:** Affects robot operation accuracy

- **Task:** Complete Screw Driver Robot fingers (Fairino robot)
  - **Owner:** Ammad, Myeongun
  - **Status:** Only base part ready, fingers pending (as of Jan 15)
  - **Next Follow-up:** Print and install fingers
  - **Risk:** Blocks Fairino robot usage on screw driver robot

---

## ⚠️ Risks & Dependencies

1. **Robot Teaching → Vision Integration → Cycle Time Testing**
   - Sequential dependency blocking multiple tasks
   - **Mitigation:** Prioritize robot teaching completion

2. **Dataset Collection → Vision Validation**
   - Requires stable robot operation
   - **Mitigation:** Schedule dedicated data collection sessions

3. **Documentation Completion → Handover**
   - Multiple documentation tasks in parallel
   - **Mitigation:** Assign clear owners, track progress

4. **GUI Issues → Product Registration**
   - Affects operational workflow
   - **Mitigation:** Prioritize critical GUI fixes

---

## 📅 Upcoming Deadlines

- **January 15, 2026:** Vision integration status summary (Rizwan)
- **January 15, 2026:** GUI issues Excel file (Jalol)
- **Friday (target):** Meet Everint project acceptance targets
- **Ongoing:** Handover documentation (Kwanghyeop)

---

**Note:** This list is extracted from chat transcripts and project documentation. All tasks should be verified and created in Asana by the project owner. Status and urgency may change based on project progress.

