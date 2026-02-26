# Project Memory and Operator Workflow Design

## Goal
Create a durable project memory at repo root that documents scripts, file roles, and the daily operating workflow for Asana and KakaoTalk-driven updates.

## Scope
- Add `memory.md` as canonical operations memory.
- Sanitize `.env.example` to safe placeholders.
- Add a brief `README.md` pointer so operators start from memory.

## Approach Options
1. Memory only.
2. Memory plus safety and README pointer. (Chosen)
3. Memory plus new orchestration automation script.

## Chosen Architecture
Use `memory.md` as the single operational playbook for:
- data sources (Asana + KakaoTalk),
- script usage, file ownership/roles,
- execution workflow for "fetch latest", meeting-note intake, tracker updates, and missing-task creation.

Keep runtime behavior in existing scripts unchanged; this is documentation + safety hardening only.

## Error Handling and Boundaries
- If `ASANA_PAT` or project IDs are missing, scripts fail fast.
- If Kakao export is stale, pause before downstream updates.
- If missing-task list is empty, skip creation step.

## Verification
- Ensure files exist and contain expected sections.
- Run unit tests to ensure documentation/safety edits did not break existing scripts.
