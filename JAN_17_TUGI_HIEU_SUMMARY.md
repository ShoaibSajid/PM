# January 17, 2026 - Tugi and Hieu Work Summary

**Date:** January 17, 2026  
**Team Members:** Tugi (Rubber Foot Robot), Hieu (Screw Driver Robot)  
**Location:** Everint Factory

---

## 📋 Hieu's Work Summary (Screw Driver Robot)

### ✅ Completed Tasks

#### 1st Priority Tasks:
- ✅ **Provide dataset for 20+ runs to vision team**
  - Dataset captured for XD5-40dc product
  - Images uploaded and shared with vision team

#### 2nd Priority Tasks:
- ✅ **Fix tilted screw issue**
  - Adjusted screw pickup position
  - Added new magnet (silver magnet installed on screw bit, orange magnet inside screwdriver box)
  - Status: Seems better after adjustments

- ✅ **Install second magnet/spring on screw bit**
  - Successfully installed

- ✅ **Install screw feeder plate in plastic**
  - Installed but not working well
  - **Action taken:** Uninstalled it

#### 3rd Priority Tasks:
- ✅ **Integrate self-training mode**
  - Self training merged and tested
  - Tested for 1 printer registration
  - Note: File saving issue identified (saved to wrong folder, named with full path)

- ✅ **Fixed move up logic**
  - Fixed logic when abort signal comes or timeout while fastening screws

### ⏳ In Progress Tasks

#### 1st Priority Tasks:
- ⏳ **Fix the speed issue**
  - **Issue:** Robot gets slow randomly, only way to fix is restarting the control box
  - **Root cause:** Suspected issue in clean_up function when timeout (fastening) or abort signal occurs
  - **Action needed:** Ammad to help debug tomorrow
  - **Details requested by Ammad:**
    - Robot slows down randomly or on 3rd screw? → When timeout (fastening) or abort signal
    - Position reaching issue still persisting? → With tolerance 0.15, didn't happen again today
    - LAN issues details? → Connection sometimes missed between table and robot (as well as framework to robot)

- ⏳ **Display error messages**
  - In progress

- ⏳ **Screw validation tuning**
  - Merged PR from Haider Shah but didn't solve the issue
  - **Hieu's suggestion:** Add logic between range and tilt angle instead of strict "and" logic
  - **Multiple false positive/negative cases identified:**
    - False positives (should be normal): 17:34, 17:42:45, 17:42:41, 18:23:13, 18:23:18, 18:33:54, 18:33:38, 18:33:29, 18:52:22, 18:52:32, 18:52:35
    - False negative (should be tilt): 18:33:42, 18:52:45
  - **Action needed:** Vision team to tune on all images mentioned today and old dataset

### ❌ Not Completed / Skipped Tasks

#### 1st Priority Tasks:
- ❌ **Perform validation 2 times from different angles**
  - **Reason:** Camera view is fixed, so 2 times validation will not help unless rotating the bit
  - **Decision:** Skipped this task

#### 2nd Priority Tasks:
- ❌ **Install vertical plates to make screws straight**
  - Not completed

#### 3rd Priority Tasks:
- ❌ **Speed up robot movements to meet cycle time**
  - Not completed

### 🔧 Technical Issues Identified

1. **Self Training File Saving Issue**
   - File saved to wrong folder
   - Named with full path instead of proper structure
   - **Expected:** Should save in data folder: PrinterName/weights/PrinterName_roi.pt
   - **Solution needed:** Use os.path instead of hard coding, use / instead of \

2. **Auto Registration GUI Bug**
   - GUI bug prevents saving annotation results
   - Happens randomly, even with hand annotation
   - **Impact:** Only 2 printers registered (XD5-40D and XD3-40D) instead of all
   - **Action needed:** Saidjalol to check saving SVG issue

3. **Rubber Foot ROI Detection Issue**
   - User ROI from GUI is good
   - But tighter mechanism makes it wrong when passing through vision code
   - **Reference path:** data/inference/save_ref_data/XD5-40dc
   - **Action needed:** Rizwan to check and fix

4. **Product Registration Issue**
   - Due to GUI error, couldn't complete registration on XD5-40IIt
   - Same issue faced yesterday by Saidjalol

### 📊 Registration Status

- ✅ XD5-40D registered (product for Monday's demo)
- ✅ XD3-40D registered
- ❌ XD5-40IIt - Registration incomplete due to GUI bug
- ⏳ Other products - Pending due to GUI bug

### 📝 Additional Notes

- **Conveyor teaching:** Manager finished teaching, took longer than expected due to issues
- **Product samples:** Only received 1 XD5-40D from manager (others were XD5-43IIt and XD5-40IIt, not same)
- **Ethernet cables:** Requested new cables from lab (current one not stable, sometimes disconnects)
- **Quy Ninh:** Helped with auto registration process, dataset collection and organization

---

## 📋 Tugi's Work Summary (Rubber Foot Robot)

### ✅ Completed Tasks

1. ✅ **Run products and captured datasets with rubber foot partially attached**
   - Captured datasets following Rizwan's instructions
   - Quy sent path to vision team members
   - Dataset uploaded to NAS: /SmartFactory/[company]Everint/Label-Printer_images/Jan17_images

2. ✅ **Hand eye calibration**
   - Performed hand eye calibration
   - Ran the code while tuning the parameters
   - **Note:** Shoaib requested Tan/Muazzam to check if calibration needs further fine tuning (Jan 18)

3. ✅ **Implemented error/warning message display code**
   - Error/warning message display code implemented
   - **Action needed:** Reset of pop up message from GUI side requested by Shoaib to Saidjalol

### 📝 Additional Notes

- Worked on rubber foot robot operations
- Captured datasets for vision team analysis
- Focused on calibration and parameter tuning

---

## 🔍 Key Findings & Issues

### Critical Issues Identified:

1. **Robot Speed Issue (Hieu)**
   - Robot slows down when timeout or abort signal occurs
   - Suspected issue in clean_up function
   - Requires control box restart to fix
   - Needs Ammad's help for debugging

2. **GUI Registration Bug**
   - Prevents saving annotation results
   - Random occurrence
   - Blocks registration of all products
   - Only 2 products registered instead of all

3. **Screw Validation False Positives/Negatives**
   - Multiple cases identified
   - Current logic too strict
   - Needs range-based logic instead of strict "and" logic

4. **Self Training File Saving**
   - Path issues (Windows vs Linux)
   - Wrong folder structure
   - Needs os.path implementation

### Positive Progress:

- ✅ Self training integrated and tested
- ✅ Dataset captured for XD5-40D (Monday's demo product)
- ✅ Tilted screw issue improved with magnet adjustments
- ✅ Hand eye calibration completed
- ✅ Error message display code implemented
- ✅ Move up logic fixed for abort/timeout scenarios

---

## 📅 Next Steps (Jan 18)

### For Hieu:
- Debug robot speed issue with Ammad
- Complete error message display
- Fix auto registration GUI bug (coordinate with Saidjalol)
- Continue screw validation tuning

### For Tugi:
- Fine-tune hand eye calibration if needed
- Continue rubber foot placement accuracy improvements
- Test error message display with GUI reset functionality

### For Team:
- Fix GUI registration bug (Saidjalol)
- Complete product registration for all products
- Continue dataset collection
- Prepare for Monday demo (XD5-40D, 950EA)

---

**Last Updated:** January 18, 2026

