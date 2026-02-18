# Everint Project – Status Report

**Client:** Everint (company name)  
**Project Owner:** Shoaib (recently joined to manage all teams)  
**Last Updated:** February 19, 2026  
**Project Phase:** Validation, Acceptance, and Handover

---

## Project Overview

The Everint project involves the deployment, validation, and handover of multiple **industrial robotic systems** used for automated assembly operations at Everint factory. Each robot system operates **independently** and is evaluated based on **cycle-time-driven acceptance criteria**.

**Robot Systems:**
- **PCB Screw Robot:** Scans product, identifies screw holes, performs automated screwing
- **Label Printer Screw Robot:** Identifies screw holes on product body and screws them
- **Rubber Foot Robot:** Attaches rubber pads to product body (placed after Label Printer Screw Robot)

A robot cycle is considered **PASS** if:
- All required actions are completed (all screws fastened / all rubber pads attached)
- The cycle completes within the predefined cycle time for the given product type

If a cycle cannot be completed for any reason, the system **raises a warning**.  
Sequential handover between robots is **not required**.

---

## Overall Status Summary

- **Implementation:** Complete
- **Validation:** In progress
- **Documentation:** In progress
- **Risk Level:** Low to Medium (primarily validation and handover completeness)

The project is transitioning from execution to formal acceptance and ownership transfer, with remaining work focused on evidence, documentation, and clarity rather than new development.

---

## Documentation Structure

This project documentation is organized into the following files:

### Active Tracking
- **[URGENT_ISSUES_CHECKLIST.md](./URGENT_ISSUES_CHECKLIST.md)** ⭐ **Main tracking file** - Tasks matching Asana screenshots
- **[ASANA_TASKS_LIST.md](./ASANA_TASKS_LIST.md)** - Complete list of all tasks from Asana (organized by owner, priority, category, due date)
- **[COMPLETED_TASKS.md](./COMPLETED_TASKS.md)** - Archive of all completed tasks
- **[TASKS_MISSING_IN_ASANA_RAW_REVIEW.md](./TASKS_MISSING_IN_ASANA_RAW_REVIEW.md)** - Consolidated missing tasks (deduplicated)

### Reference Files
- **[MISSING_ITEMS.md](./MISSING_ITEMS.md)** - Detailed missing items (reference)
- **[CHAT_ANALYSIS_FEB_10_18.md](./CHAT_ANALYSIS_FEB_10_18.md)** - Chat analysis Feb 10–18
- **[TODAY_SUMMARY_FEB_19.md](./TODAY_SUMMARY_FEB_19.md)** - Today action summary (Screw, Rubber, PCB)

---

## Quick Links

- [Complete Tracking Checklist](./URGENT_ISSUES_CHECKLIST.md) ⭐ **Main tracking file (matches Asana)**
- [Asana Tasks List](./ASANA_TASKS_LIST.md) - Complete Asana tasks reference (51 tasks: 7 completed, 44 pending)
- [Completed Tasks Archive](./COMPLETED_TASKS.md) - All completed tasks
- [Missing Tasks (Not in Asana)](./TASKS_MISSING_IN_ASANA_RAW_REVIEW.md) - Tasks needing review
- [Chat Analysis (Feb 10-18)](./CHAT_ANALYSIS_FEB_10_18.md) - Latest KakaoTalk extraction analysis
- [Today Summary (Feb 19)](./TODAY_SUMMARY_FEB_19.md) - Action focus for Screw/Rubber/PCB
- [Missing Items (Detailed)](./MISSING_ITEMS.md) - Reference document for information gaps

---

**Note:** URGENT_ISSUES_CHECKLIST.md now contains only tasks that match Asana screenshots. Completed tasks are archived in COMPLETED_TASKS.md. Tasks not in Asana are listed in TASKS_MISSING_IN_ASANA_RAW_REVIEW.md for review.
Historical snapshots and old one-off summaries are intentionally pruned from the working tree; recover any removed document from git history if needed.

---

## Asana Integration (Codex Tracking)

Use the sync script to pull live tasks from Asana and refresh `ASANA_TASKS_LIST.md`:

```bash
export ASANA_PAT="your_asana_personal_access_token"
export ASANA_PROJECT_GID="your_project_gid"
python3 scripts/sync_asana_tasks.py
```

For multiple projects, set comma-separated IDs:

```bash
export ASANA_PROJECT_GID="1211933636406772,1211933636406778,1212715232979031,1212715232979034,1212715232979040"
python3 scripts/sync_asana_tasks.py
```

This updates:
- `ASANA_TASKS_LIST.md` (human-readable tracking file for Codex)
- `ASANA_TASKS_RAW.json` (full raw task payload)

`ASANA_TASKS_LIST.md` is grouped into:
- `Screw Driver`
- `Rubber Foot`
- `PCB`
- `Mobile Printers`

Note: `ASANA_TASKS_LIST.md` includes pending tasks only. Completed tasks are excluded from section tables.
