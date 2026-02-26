# Codex Rules for PM Repository

## Mandatory First Step
- Before implementing any task, read `/Users/shoaibsajid/Desktop/Repositories/PM/memory.md`.
- Start execution only after aligning the task with the workflow in `memory.md`.

## Operating Sources
- Task status source of truth: Asana.
- Discussion/update source of truth: KakaoTalk exports and user-provided meeting notes.

## Required Update Cycle
1. Sync latest Asana data.
2. Sync latest Asana task comments when comments are requested:
   - update `ASANA_TASK_COMMENTS_LATEST.md`
   - update `ASANA_TASK_COMMENTS_RAW.json`
3. Process latest Kakao updates and roll the chat anchor forward.
4. Ask user for meeting notes or extra updates (unless user explicitly asks to proceed directly).
5. Update tracking files.
6. Create missing Asana review tasks if needed (`--dry-run` first, then real run).
7. Validate and report changed files.

## Scope
- This repo is PM operations/tracking only.
- `StateMachines/` is out of scope.

## Safety
- Never commit real secrets/tokens.
- Keep `.env.example` placeholders only.
- The `ASANA_PAT` variable is defined in `.env.example` as a template location (placeholder value only).
- If a real token is discovered in tracked files, treat it as a leak risk and replace it with placeholders in repo files.
