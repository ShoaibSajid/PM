# Cursor Integration Guide

## Overview
This guide explains how to use Cursor effectively for updating, tracking, and managing tasks in the PM system.

## What is Cursor Used For?

In this workflow, Cursor is your primary tool for:
- ✅ Creating and editing task files
- ✅ Updating task status
- ✅ Tracking progress and time spent
- ✅ Managing documentation
- ✅ Committing changes to repository
- ✅ Keeping files synchronized

## Setting Up Your Workspace

### Repository Structure
Navigate to your PM repository:
```bash
cd /path/to/PM
```

Your working directories:
- `docs/tasks/` - Individual task files
- `docs/features/` - Feature documentation
- `docs/bugs/` - Bug tracking
- `docs/templates/` - Templates for new items

## Common Workflows with Cursor

### Workflow 1: Creating a New Task from ChatGPT Output

1. **Copy from ChatGPT**
   - Generate task in ChatGPT
   - Copy the markdown output

2. **Create File in Cursor**
   ```bash
   # Use a descriptive filename
   docs/tasks/implement-user-login.md
   ```

3. **Paste and Format**
   - Paste ChatGPT output
   - Add metadata at top:
     ```markdown
     **Created:** 2026-01-14
     **Status:** draft
     **Asana Link:** [pending]
     ```

4. **Review and Edit**
   - Verify all sections are complete
   - Adjust estimates if needed
   - Add any missing details

5. **Commit**
   ```bash
   git add docs/tasks/implement-user-login.md
   git commit -m "Add task: Implement user login"
   git push
   ```

### Workflow 2: Updating Task Status

1. **Open Task File**
   - Navigate to `docs/tasks/[task-name].md`

2. **Update Status Field**
   ```markdown
   **Status:** in-progress
   ```
   
   Status values:
   - `draft` - Just created, not reviewed
   - `ready` - Reviewed, ready for assignment
   - `assigned` - Assigned in Asana
   - `in-progress` - Being worked on
   - `in-review` - Under review
   - `done` - Completed

3. **Add Progress Notes**
   ```markdown
   ## Progress Notes
   
   ### 2026-01-14
   - Started implementation
   - Set up basic structure
   - Completed 30% of work
   ```

4. **Update Metadata**
   ```markdown
   **Last Updated:** 2026-01-14
   **Time Spent:** 3 hours
   **Completion:** 30%
   ```

5. **Commit Changes**
   ```bash
   git add docs/tasks/implement-user-login.md
   git commit -m "Update: User login task 30% complete"
   git push
   ```

### Workflow 3: Adding Asana Link After Assignment

1. **Get Asana Task URL**
   - Open task in Asana
   - Copy the task URL

2. **Update Task File**
   ```markdown
   **Asana Link:** https://app.asana.com/0/project/task-id
   **Assigned To:** John Doe
   **Status:** assigned
   ```

3. **Commit**
   ```bash
   git commit -am "Link task to Asana: implement-user-login"
   git push
   ```

### Workflow 4: Tracking Daily Progress

1. **Open Task Files** for tasks you're working on

2. **Add Daily Entry**
   ```markdown
   ### 2026-01-14
   **Time Spent:** 2.5 hours
   **Progress:**
   - Completed authentication logic
   - Added validation
   - Started writing tests
   
   **Blockers:**
   - Need design review for error messages
   
   **Next Steps:**
   - Finish unit tests
   - Integration testing
   ```

3. **Update Completion**
   ```markdown
   **Completion:** 60%
   ```

4. **Commit End of Day**
   ```bash
   git add .
   git commit -m "Daily update: progress on active tasks"
   git push
   ```

### Workflow 5: Completing a Task

1. **Final Update**
   ```markdown
   **Status:** done
   **Completion:** 100%
   **Completed:** 2026-01-15
   ```

2. **Add Summary**
   ```markdown
   ## Completion Summary
   - All acceptance criteria met
   - Tests passing
   - Code reviewed and merged
   - Documentation updated
   
   **Total Time:** 8 hours
   **Actual vs Estimated:** 8h / 6h (133%)
   ```

3. **Commit**
   ```bash
   git commit -am "Complete: implement-user-login"
   git push
   ```

## File Management

### Naming Conventions

#### Task Files
```
docs/tasks/[brief-description].md
```
Examples:
- `docs/tasks/add-user-authentication.md`
- `docs/tasks/fix-login-redirect.md`
- `docs/tasks/update-api-documentation.md`

#### Feature Files
```
docs/features/[feature-name].md
```
Examples:
- `docs/features/user-authentication.md`
- `docs/features/payment-integration.md`

#### Bug Files
```
docs/bugs/bug-[id]-[brief-description].md
```
Examples:
- `docs/bugs/bug-001-login-timeout.md`
- `docs/bugs/bug-002-payment-error.md`

### Organizing Files

#### Active Tasks
Keep in main directory while active:
```
docs/tasks/active-task-1.md
docs/tasks/active-task-2.md
```

#### Completed Tasks
Option 1: Move to archive
```bash
mkdir -p docs/tasks/archive/2026-01
mv docs/tasks/completed-task.md docs/tasks/archive/2026-01/
```

Option 2: Add date prefix and keep
```bash
mv docs/tasks/task-name.md docs/tasks/2026-01-15-task-name.md
```

## Using Cursor Features

### Quick Navigation
- `Cmd/Ctrl + P` - Quick file open
- `Cmd/Ctrl + Shift + F` - Search across files
- `Cmd/Ctrl + B` - Toggle sidebar

### AI Assistance
Use Cursor's AI features for:
- Writing task descriptions
- Formatting markdown
- Generating checklists
- Creating consistent structure

### Multi-file Editing
Select multiple task files to:
- Update status in batch
- Add common fields
- Standardize formatting

## Syncing with Git

### Daily Sync Routine
```bash
# Morning: Pull latest
git pull

# Throughout day: Commit frequently
git add docs/tasks/
git commit -m "Update: task progress"
git push

# End of day: Final push
git add .
git commit -m "EOD: task updates"
git push
```

### Best Practices
- Commit often (every meaningful change)
- Use descriptive commit messages
- Pull before starting work
- Push at end of day
- Review diff before committing

## Status Tracking Dashboard

### Create a Status Overview
Create `docs/status.md`:

```markdown
# Task Status Overview

**Last Updated:** 2026-01-14

## Active Tasks (In Progress)

| Task | Assignee | Progress | Due Date | Asana Link |
|------|----------|----------|----------|------------|
| User Login | John | 60% | 2026-01-20 | [Link](#) |
| API Docs | Jane | 30% | 2026-01-22 | [Link](#) |

## Ready for Assignment

| Task | Priority | Estimate | Status |
|------|----------|----------|--------|
| Add Logging | High | 4h | ready |
| Update Tests | Medium | 6h | ready |

## Completed This Week

- [x] Setup CI/CD
- [x] Database Migration
- [x] Error Handling
```

### Update Daily
Use Cursor to update this file daily with current status.

## Tips and Tricks

### Quick Status Update
Use search and replace:
- Find: `**Status:** in-progress`
- Replace: `**Status:** in-review`

### Batch Metadata Update
Use multi-cursor editing to update dates across multiple files.

### Template Insertion
Save common snippets:
- Progress note template
- Status update template
- Completion summary template

### File Templates
Keep templates handy:
```bash
cp docs/templates/task-template.md docs/tasks/new-task.md
```

## Integration with Asana

### Linking Tasks
Always add Asana link after assignment:
```markdown
**Asana Link:** https://app.asana.com/0/project/task-id
```

### Syncing Status
When you update status in repository:
1. Update the task file in Cursor
2. Also update status in Asana
3. Keep both in sync

### Referencing Tasks
In task files, reference related tasks:
```markdown
## Related Tasks
- [Setup Auth Service](docs/tasks/setup-auth-service.md)
- Asana: https://app.asana.com/0/related-task
```

## Common Issues

### Merge Conflicts
If you get merge conflicts:
```bash
git pull
# Resolve conflicts in Cursor
git add .
git commit
git push
```

### Lost Changes
Use git to recover:
```bash
git log
git checkout <commit-hash> -- path/to/file
```

### File Organization
If files get messy:
```bash
# Create monthly archives
mkdir -p docs/tasks/archive/2026-01
mv docs/tasks/completed-*.md docs/tasks/archive/2026-01/
```

## Checklist for Task Management

### When Creating Task
- [ ] Copy from ChatGPT or use template
- [ ] Add all metadata fields
- [ ] Set status to "draft"
- [ ] Use descriptive filename
- [ ] Commit to repository

### When Updating Task
- [ ] Update status field
- [ ] Add progress notes with date
- [ ] Update completion percentage
- [ ] Update time spent
- [ ] Commit changes

### When Assigning Task
- [ ] Add Asana link
- [ ] Add assignee name
- [ ] Change status to "assigned"
- [ ] Commit changes

### When Completing Task
- [ ] Set status to "done"
- [ ] Set completion to 100%
- [ ] Add completion date
- [ ] Write completion summary
- [ ] Commit final update

---

**Remember:** Cursor is your daily tool for keeping the PM system up to date. Commit frequently and keep information current!
