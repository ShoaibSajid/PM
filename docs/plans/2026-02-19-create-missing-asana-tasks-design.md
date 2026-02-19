# Create Missing Asana Tasks Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a script that reads `TASKS_MISSING_IN_ASANA_RAW_REVIEW.md` and creates review tasks in Asana under project `1213338742027940`, assigned to `me` for triage.

**Architecture:** Add a standalone Python CLI script that parses the consolidated missing-task markdown sections and owners, computes deterministic task names, fetches existing tasks in the target project, and creates only non-duplicate tasks. Keep side-effect logic (Asana API calls) separate from pure parsing/name/selection helpers so behavior can be tested without network access.

**Tech Stack:** Python 3 standard library (`argparse`, `dataclasses`, `urllib`, `json`, `re`, `pathlib`), `unittest`.

---

### Task 1: Add parsing and planning tests

**Files:**
- Create: `tests/test_create_missing_asana_tasks.py`

**Step 1: Write the failing test**

```python
def test_parse_consolidated_missing_tasks_extracts_section_description_owners():
    ...
```

**Step 2: Run test to verify it fails**

Run: `pytest -q tests/test_create_missing_asana_tasks.py`
Expected: FAIL because module/functions do not exist.

**Step 3: Write additional failing tests**

```python
def test_build_task_name_includes_section_prefix():
    ...

def test_plan_creations_skips_existing_names_case_insensitive():
    ...
```

**Step 4: Run tests to verify failures**

Run: `pytest -q tests/test_create_missing_asana_tasks.py`
Expected: FAIL until implementation is added.

**Step 5: Commit**

```bash
git add tests/test_create_missing_asana_tasks.py
git commit -m "test: add coverage for missing-task importer"
```

### Task 2: Implement missing-task importer script

**Files:**
- Create: `scripts/create_missing_asana_tasks.py`
- Test: `tests/test_create_missing_asana_tasks.py`

**Step 1: Write minimal implementation**

```python
@dataclass
class MissingTask:
    section: str
    description: str
    owners: str
```

```python
def parse_missing_tasks_markdown(text: str) -> list[MissingTask]:
    ...
```

```python
def plan_creations(tasks, existing_names):
    ...
```

```python
class AsanaClient:
    def get(...): ...
    def post(...): ...
```

**Step 2: Run targeted tests**

Run: `pytest -q tests/test_create_missing_asana_tasks.py`
Expected: PASS.

**Step 3: Wire CLI behavior**

Run mode:
- default project gid: `1213338742027940`
- requires `ASANA_PAT`
- `--dry-run` prints what would be created
- creates tasks with assignee `me`

**Step 4: Re-run tests**

Run: `pytest -q`
Expected: PASS all tests.

**Step 5: Commit**

```bash
git add scripts/create_missing_asana_tasks.py tests/test_create_missing_asana_tasks.py
git commit -m "feat: add importer for missing Asana review tasks"
```

### Task 3: Add usage notes in README

**Files:**
- Modify: `README.md`

**Step 1: Add short usage snippet**

```bash
ASANA_PAT=... python3 scripts/create_missing_asana_tasks.py --dry-run
ASANA_PAT=... python3 scripts/create_missing_asana_tasks.py
```

**Step 2: Run tests for regression check**

Run: `pytest -q`
Expected: PASS.

**Step 3: Commit**

```bash
git add README.md
git commit -m "docs: add missing-task importer usage"
```
