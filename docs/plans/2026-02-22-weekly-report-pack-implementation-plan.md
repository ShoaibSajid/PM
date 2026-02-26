# Weekly Report Pack Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create concise weekly reporting artifacts for Feb 16-22, 2026 with evidence-backed history and a non-blocking next-week schedule.

**Architecture:** Extract last-week signals from Asana task raw JSON, Asana comments JSON, and existing chat summary markdown files; synthesize into three short markdown outputs under a date-based directory.

**Tech Stack:** Markdown, jq, shell utilities.

---

### Task 1: Collect evidence window
**Files:**
- Read: `ASANA_TASKS_RAW.json`
- Read: `ASANA_TASK_COMMENTS_RAW.json`
- Read: `CHAT_ANALYSIS_FEB_19_21.md`
- Read: `TODAY_SUMMARY_FEB_20.md`

### Task 2: Build concise summaries
**Files:**
- Create: `weekly_reports/2026-02-16_to_2026-02-22/01_weekly_report.md`
- Create: `weekly_reports/2026-02-16_to_2026-02-22/02_past_completion_schedule.md`
- Create: `weekly_reports/2026-02-16_to_2026-02-22/03_next_week_proposed_schedule.md`

### Task 3: Verify and report
**Files:**
- Verify created files and headings are concise.
