# Quick Start Guide

## Welcome to PM!

This guide will help you get started with the project management system quickly.

## Step 1: Understand the Structure

The PM repository uses:
- **GitHub Issues** for task tracking
- **Templates** for consistent planning
- **Documentation** for knowledge sharing
- **Roadmap** for long-term planning

## Step 2: Create Your First Task

1. Go to the [Issues tab](../../issues)
2. Click "New Issue"
3. Select "Task" template
4. Fill in:
   - Task title
   - Description
   - Priority level
   - Status (usually "To Do" for new tasks)
   - Acceptance criteria
5. Click "Submit new issue"

## Step 3: Organize Your Work

### Using Labels
Add labels to categorize issues:
- `task`, `bug`, `enhancement`
- `high-priority` for urgent items
- Custom labels as needed

### Using Milestones
Group related issues:
1. Go to Issues → Milestones
2. Create a new milestone (e.g., "Sprint 1", "Q1 2026")
3. Assign issues to the milestone
4. Track progress

### Using Project Boards
Visualize workflow:
1. Go to Projects tab
2. Create a new project board
3. Add columns: To Do, In Progress, In Review, Done
4. Add issues as cards
5. Drag cards across columns as work progresses

## Step 4: Plan a Project

1. Copy the project plan template:
   ```bash
   cp docs/templates/project-plan-template.md docs/my-project-plan.md
   ```

2. Fill in the template with:
   - Project objectives
   - Scope and deliverables
   - Timeline and milestones
   - Team and resources
   - Risks and dependencies

3. Commit the plan to the repository

## Step 5: Plan a Sprint

1. Copy the sprint plan template:
   ```bash
   cp docs/templates/sprint-plan-template.md docs/sprint-1-plan.md
   ```

2. Define:
   - Sprint goal
   - Sprint duration
   - Tasks from backlog
   - Team capacity
   - Definition of done

3. Create issues for sprint tasks

## Step 6: Document Meetings

1. Copy the meeting notes template:
   ```bash
   cp docs/templates/meeting-notes-template.md docs/meetings/2026-01-14-planning.md
   ```

2. Record:
   - Attendees
   - Discussion points
   - Decisions made
   - Action items

3. Commit to repository for team access

## Step 7: Track Progress

### Daily
- Update issue status
- Add comments on progress
- Report blockers

### Weekly
- Review sprint board
- Update documentation
- Close completed issues

### Monthly
- Review roadmap
- Update milestones
- Plan next phase

## Common Workflows

### Starting a New Task
1. Create issue from Task template
2. Assign to yourself
3. Add to project board (To Do column)
4. Create branch if needed
5. Move to In Progress when starting

### Completing a Task
1. Complete the work
2. Update issue with results
3. Move to In Review
4. Get review/approval
5. Move to Done
6. Close issue

### Reporting a Bug
1. Create issue from Bug Report template
2. Add severity label
3. Assign to developer
4. Link related issues if any
5. Verify fix when closed

### Requesting a Feature
1. Create issue from Feature Request template
2. Describe problem and solution
3. Add priority
4. Discuss in comments
5. Approve and add to backlog

## Tips for Success

### Be Specific
- Use clear, descriptive titles
- Provide detailed descriptions
- Include acceptance criteria
- Add relevant links or references

### Stay Organized
- Update issues regularly
- Use consistent labels
- Keep documentation current
- Archive completed work

### Communicate
- Comment on issues
- Tag team members with @mentions
- Document decisions
- Ask questions when unclear

### Review and Improve
- Reflect on what works
- Adjust processes as needed
- Share learnings
- Celebrate progress

## Getting Help

If you're stuck:
1. Check the [README](../README.md)
2. Review [CONTRIBUTING](../CONTRIBUTING.md)
3. Search existing issues
4. Ask in issue comments
5. Contact project maintainers

## Next Steps

- [ ] Create your first issue
- [ ] Set up a project board
- [ ] Review the roadmap
- [ ] Plan your first sprint
- [ ] Start tracking work

---

Happy planning! 🎉
