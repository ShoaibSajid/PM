# Everint Project – Status Report

**Client:** Everint (company name)  
**Project Owner:** Shoaib (recently joined to manage all teams)  
**Last Updated:** March 11, 2026  
**Project Phase:** Validation, Acceptance, and Handover

---

## Shared Context

- Latest Asana sync: **2026-03-11 23:18:39** (`ASANA_TASKS_LIST.md`, `ASANA_TASKS_RAW.json`)
- Latest Asana comments snapshot: **2026-03-11 23:20:02** (`ASANA_TASK_COMMENTS_LATEST.md`, `ASANA_TASK_COMMENTS_RAW.json`)
- Latest chat anchor: **2026-03-11 22:48:37** (Shoaib: "Today, they were producing a different printer ...")
- Latest today summary: [TODAY_SUMMARY_MAR_11.md](./TODAY_SUMMARY_MAR_11.md)

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
- **[CHAT_ANALYSIS_FEB_26_TO_MAR_11.md](./CHAT_ANALYSIS_FEB_26_TO_MAR_11.md)** - Chat analysis Feb 26 to Mar 11 (latest)
- **[CHAT_ANALYSIS_FEB_22_25.md](./CHAT_ANALYSIS_FEB_22_25.md)** - Chat analysis Feb 22–25
- **[CHAT_ANALYSIS_FEB_19_21.md](./CHAT_ANALYSIS_FEB_19_21.md)** - Chat analysis Feb 19–21
- **[CHAT_ANALYSIS_FEB_10_18.md](./CHAT_ANALYSIS_FEB_10_18.md)** - Chat analysis Feb 10–18 (historical)
- **[ASANA_TASK_COMMENTS_LATEST.md](./ASANA_TASK_COMMENTS_LATEST.md)** - Latest Asana comments summary
- **[TODAY_SUMMARY_MAR_11.md](./TODAY_SUMMARY_MAR_11.md)** - Today action summary (Kakao + debug-group updates: registration, calibration, reporting, hardware)
- **[TODAY_SUMMARY_FEB_26.md](./TODAY_SUMMARY_FEB_26.md)** - Today action summary (Kakao + direct updates: Screw, Rubber, Vision)
- **[TODAY_SUMMARY_FEB_24.md](./TODAY_SUMMARY_FEB_24.md)** - Today action summary (meeting notes/direct updates: Rubber Foot + Screw)

---

## Quick Links

- [Complete Tracking Checklist](./URGENT_ISSUES_CHECKLIST.md) ⭐ **Main tracking file (matches Asana)**
- [Asana Tasks List](./ASANA_TASKS_LIST.md) - Complete Asana tasks reference (latest sync: 89 pending, 105 completed excluded)
- [Asana Task Comments](./ASANA_TASK_COMMENTS_LATEST.md) - Latest task comments across pending tasks
- [Completed Tasks Archive](./COMPLETED_TASKS.md) - All completed tasks
- [Missing Tasks (Not in Asana)](./TASKS_MISSING_IN_ASANA_RAW_REVIEW.md) - Tasks needing review
- [Chat Analysis (Feb 26 to Mar 11)](./CHAT_ANALYSIS_FEB_26_TO_MAR_11.md) - Latest KakaoTalk extraction analysis
- [Today Summary (Mar 11)](./TODAY_SUMMARY_MAR_11.md) - Latest Kakao + debug-group action packaging
- [Missing Items (Detailed)](./MISSING_ITEMS.md) - Reference document for information gaps

---

## Project Memory

- Start with [memory.md](./memory.md) for the operational runbook (scripts, file ownership/roles, and update workflows).
- Standard cadence is: sync Asana, process Kakao updates, ask for meeting notes, reconcile tracker files, then create missing Asana review tasks.
- `ASANA_PAT` and `ASANA_PROJECT_GID` template variables are defined in `.env.example` (placeholder values only; do not commit real tokens).

---

**Note:** URGENT_ISSUES_CHECKLIST.md now contains only tasks that match Asana screenshots. Completed tasks are archived in COMPLETED_TASKS.md. `TASKS_MISSING_IN_ASANA_RAW_REVIEW.md` is strict missing-only and may be empty when all work is represented in Asana.
Historical snapshots and old one-off summaries are intentionally pruned from the working tree; recover any removed document from git history if needed.

---

## Asana Integration (Codex Tracking)

Use the sync script to pull live tasks from Asana and refresh `ASANA_TASKS_LIST.md`:

`ASANA_PAT` is expected from local environment setup using the `.env.example` template.

```bash
export ASANA_PAT="your_asana_personal_access_token"
export ASANA_PROJECT_GID="your_project_gid"
python3 scripts/sync_asana_tasks.py
```

For multiple projects, set comma-separated IDs:

```bash
export ASANA_PROJECT_GID="1211933636406772,1211933636406778,1212715232979031,1212715232979034,1212715232979040,1213338742027940,1213338784855695"
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

## Create Missing-Task Review Items In Asana

Use the importer to create missing-task review items from
`TASKS_MISSING_IN_ASANA_RAW_REVIEW.md` into project `1213338742027940`
(`Unassigned Tasks`), assigned to yourself first:

```bash
ASANA_PAT="your_asana_personal_access_token" \
python3 scripts/create_missing_asana_tasks.py --dry-run

ASANA_PAT="your_asana_personal_access_token" \
python3 scripts/create_missing_asana_tasks.py
```

Optional:

```bash
python3 scripts/create_missing_asana_tasks.py --limit 5
```
