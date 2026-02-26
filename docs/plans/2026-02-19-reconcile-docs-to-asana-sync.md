# Reconcile Docs To Asana Sync Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Update project markdown docs so they reflect the latest Asana state and keep `TASKS_MISSING_IN_ASANA_RAW_REVIEW.md` as strict missing-only.

**Architecture:** Use the latest generated `ASANA_TASKS_LIST.md` and `ASANA_TASKS_RAW.json` as ground truth, then rewrite summary docs to remove stale counts and obsolete “missing” entries now tracked in Asana.

**Tech Stack:** Markdown docs + shell inspection.

---

### Task 1: Reconcile missing-task tracker

**Files:**
- Modify: `TASKS_MISSING_IN_ASANA_RAW_REVIEW.md`

**Steps:**
1. Confirm latest Asana sync counts from `ASANA_TASKS_RAW.json`.
2. Replace consolidated missing-task list with only items still absent from Asana.
3. If none are missing, explicitly state none and document review timestamp/projects used.

### Task 2: Reconcile today summary with latest Asana-tracked review work

**Files:**
- Modify: `TODAY_SUMMARY_FEB_19.md`

**Steps:**
1. Rewrite sections around active review task buckets now tracked in Asana.
2. Keep concise action-oriented bullets; remove stale chat-only assumptions.

### Task 3: Reconcile README metadata/usage

**Files:**
- Modify: `README.md`

**Steps:**
1. Update stale Asana count text in quick links.
2. Update multi-project sync example to include `Unassigned Tasks` project.
3. Add note that missing-task file is strict missing-only and may be empty.
