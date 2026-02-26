# Project Memory Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add and wire a root-level project memory that defines script/file responsibilities and update workflows.

**Architecture:** Documentation-first update. Add one canonical memory file, sanitize env template, and link memory from README.

**Tech Stack:** Markdown, Python scripts already in repo, pytest.

---

### Task 1: Create memory document

**Files:**
- Create: `memory.md`

**Step 1: Draft memory sections**
- Project operating rules
- Script inventory
- File-role catalog
- Standard operating workflows
- Prompt templates and update checklist

**Step 2: Write memory file**
- Ensure explicit commands and decision points exist.

**Step 3: Verify sections present**
Run: `rg '^#|^##' memory.md`
Expected: key sections visible.

### Task 2: Sanitize environment template

**Files:**
- Modify: `.env.example`

**Step 1: Replace sensitive value with placeholder**
- Keep variable names; remove real token values.

**Step 2: Verify no token-like content remains**
Run: `cat .env.example`
Expected: placeholders only.

### Task 3: Add README pointer

**Files:**
- Modify: `README.md`

**Step 1: Add short "Project Memory" section**
- Link `memory.md`.
- Tell operators to start there for workflow.

**Step 2: Verify location and formatting**
Run: `rg 'Project Memory|memory\.md' README.md`
Expected: section and link present.

### Task 4: Validate repository state

**Files:**
- Test: `tests/test_sync_asana_tasks.py`
- Test: `tests/test_create_missing_asana_tasks.py`

**Step 1: Run tests**
Run: `pytest -q`
Expected: pass.

**Step 2: Review diff**
Run: `git diff -- memory.md .env.example README.md`
Expected: only requested scope changes.
