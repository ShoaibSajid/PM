# Everint PM Project Memory (Concise)

## Core Rules
- Source of truth for task status: Asana.
- Source of truth for discussions: KakaoTalk + user meeting notes.
- `ASANA_PAT` and `ASANA_PROJECT_GID` template keys are defined in `.env.example` (placeholder-only in repo).
- Before finalizing updates, always ask:  
  `"Do you have any meeting notes or extra updates to include before I finalize the files?"`
- PM operations only. `StateMachines/` is out of scope.

## Scripts
- `scripts/sync_asana_tasks.py`  
  Pulls Asana tasks (single/multi project), deduplicates, excludes completed rows from section tables, updates:
  - `ASANA_TASKS_LIST.md`
  - `ASANA_TASKS_RAW.json`

- Asana comments snapshot (ad-hoc workflow, until a dedicated script exists)  
  For "check comments" requests, fetch task stories (`comment_added`) for pending tasks and update:
  - `ASANA_TASK_COMMENTS_LATEST.md`
  - `ASANA_TASK_COMMENTS_RAW.json`

- `scripts/create_missing_asana_tasks.py`  
  Parses `TASKS_MISSING_IN_ASANA_RAW_REVIEW.md`, dedupes by normalized title, creates/syncs missing review tasks in Asana (`--dry-run`, `--limit`, prefix options).

## Key Files and Roles
- `README.md`: top-level project status and links.
- `memory.md`: this operating playbook.
- `.env.example`: placeholders only (`ASANA_PAT`, `ASANA_PROJECT_GID`).
- `ASANA_TASKS_LIST.md`: latest pending tasks report.
- `ASANA_TASKS_RAW.json`: raw Asana snapshot.
- `ASANA_TASK_COMMENTS_LATEST.md`: latest comments summary.
- `ASANA_TASK_COMMENTS_RAW.json`: raw comments snapshot.
- `URGENT_ISSUES_CHECKLIST.md`: active Asana-aligned checklist.
- `TASKS_MISSING_IN_ASANA_RAW_REVIEW.md`: strict missing-in-Asana source.
- `COMPLETED_TASKS.md`: completed archive.
- `MISSING_ITEMS.md`: gap/reference list.
- `CHAT_ANALYSIS_*.md`, `TODAY_SUMMARY_*.md`: chat and day-level synthesis.

## Standard Workflow
1. Sync Asana:
```bash
export ASANA_PAT="<token>"
export ASANA_PROJECT_GID="<gid1>,<gid2>,..."
python3 scripts/sync_asana_tasks.py
```
2. If comments are requested, refresh Asana comments snapshot (`ASANA_TASK_COMMENTS_LATEST.md`, `ASANA_TASK_COMMENTS_RAW.json`).
3. Process latest Kakao updates and move the "next-run anchor" to the latest processed message timestamp.
4. Ask user for meeting notes/additions (unless user explicitly asks to proceed without waiting).
5. Reconcile docs (`URGENT_ISSUES_CHECKLIST.md`, `TASKS_MISSING_IN_ASANA_RAW_REVIEW.md`, `COMPLETED_TASKS.md`, `MISSING_ITEMS.md`, `README.md`, relevant chat/today summaries).
6. Create missing Asana tasks:
```bash
ASANA_PAT="<token>" python3 scripts/create_missing_asana_tasks.py --dry-run
ASANA_PAT="<token>" python3 scripts/create_missing_asana_tasks.py
```
7. Validate:
```bash
pytest -q
```

## Done Criteria
- Asana snapshots refreshed.
- Asana comments snapshot refreshed when requested.
- Chat and meeting-note updates reflected.
- Latest Kakao anchor advanced and documented.
- Missing/urgent/completed trackers reconciled.
- Missing review tasks created in Asana (or none needed).
- Tests pass and changed files are reported.

## Security Reminder
- `.env.example` must never contain a real `ASANA_PAT`; keep placeholder-only values in tracked files.
- `ASANA_PAT` is declared in `.env.example` as the template key to fill locally (do not commit real tokens).
