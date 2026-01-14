# ChatGPT Integration Guide

## Overview
This guide explains how to use ChatGPT effectively for planning and generating tasks in the PM system.

## Getting Started with ChatGPT

### Setting Up Context
When starting a new planning session, provide ChatGPT with context:

```
I'm using a project management system with the following workflow:
1. ChatGPT generates tasks
2. Cursor tracks and updates tasks
3. Asana handles assignment and completion

Please help me plan [describe your project/feature].
```

## Prompts for Task Generation

### For Project Planning
```
Generate a complete project plan for [project name] including:
- Project objectives and scope
- Milestone breakdown
- Task list with estimates
- Dependencies and risks
- Success criteria

Format the output in markdown.
```

### For Feature Tasks
```
Break down the [feature name] into detailed tasks including:
- Clear task descriptions
- Acceptance criteria for each task
- Estimated hours/effort
- Dependencies between tasks
- Priority levels

Use the format:
- Task title
- Description
- Acceptance criteria (checklist)
- Estimated hours
- Dependencies
```

### For Sprint Planning
```
Create a sprint plan for [sprint number/name] with:
- Sprint goal
- Task list from backlog
- Task priorities
- Estimated capacity vs work
- Definition of done

Include tasks in priority order with estimates.
```

### For Bug Analysis
```
Analyze this bug and create a structured bug report:
[Describe the bug]

Include:
- Problem description
- Steps to reproduce
- Expected vs actual behavior
- Potential root causes
- Suggested fix approach
- Estimated effort to fix
```

## Output Formats

### Ask ChatGPT for Specific Formats

#### For Tasks
```
Please format each task as:

# Task: [Title]
**Priority:** [Level]
**Estimated Hours:** [X]

## Description
[Details]

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2

## Dependencies
- Dependency 1
```

#### For Features
```
Please format the feature breakdown as:

# Feature: [Name]
**Priority:** [Level]
**Target:** [Date]

## Overview
[Description]

## Task Breakdown
1. **Task Name** (Est: Xh)
   - Details
   - [ ] Acceptance criterion 1
   - [ ] Acceptance criterion 2
```

## Best Practices

### Be Specific
❌ "Help me plan a website"
✅ "Help me plan an e-commerce website with user authentication, product catalog, shopping cart, and payment integration"

### Iterate and Refine
1. Start with high-level breakdown
2. Ask for more detail on specific areas
3. Request alternative approaches
4. Refine estimates and priorities

### Use Follow-up Prompts
- "Can you break down task #3 into smaller subtasks?"
- "What are the technical challenges for this feature?"
- "Estimate effort for each task in hours"
- "What dependencies exist between these tasks?"
- "What risks should I consider?"

### Request Structured Output
- "Format as markdown for easy copy-paste"
- "Use checklist format for acceptance criteria"
- "Include all metadata fields"
- "Follow the task template structure"

## Example Workflows

### Workflow 1: New Feature Planning
1. **Prompt:** "I need to add a user authentication system. Generate a complete task breakdown."
2. **Refine:** "Add detailed acceptance criteria for the login task"
3. **Expand:** "What security considerations should I include?"
4. **Estimate:** "Provide effort estimates for each task"
5. **Copy:** Copy the output to a new file in `docs/features/`
6. **Track:** Use Cursor to manage the file

### Workflow 2: Sprint Planning
1. **Prompt:** "Plan a 2-week sprint for implementing [features X, Y, Z]"
2. **Prioritize:** "Which tasks are critical path?"
3. **Capacity:** "We have 80 hours total. Prioritize tasks to fit."
4. **Detail:** "Add acceptance criteria for top 5 tasks"
5. **Save:** Save to `docs/sprint-[number]-plan.md`

### Workflow 3: Bug Triage
1. **Prompt:** "Analyze this bug: [description]"
2. **Root cause:** "What are likely root causes?"
3. **Fix:** "What's the best approach to fix it?"
4. **Test:** "What test cases should verify the fix?"
5. **Document:** Save to `docs/bugs/bug-[id].md`

## Integration Tips

### Copying to Repository
1. Generate content in ChatGPT
2. Copy the markdown output
3. Open Cursor
4. Create new file in appropriate directory
5. Paste and adjust formatting
6. Add metadata (dates, status)
7. Commit to repository

### Maintaining Consistency
- Use the same terminology across sessions
- Reference previous tasks/plans in prompts
- Keep project context in mind
- Update ChatGPT if priorities change

### Version Control
- Save ChatGPT session summaries
- Reference ChatGPT in task metadata
- Note when plans are AI-generated
- Review and validate all outputs

## Common Prompts Library

### Quick Task Generation
```
Generate 5 tasks for [objective] with:
- Clear titles
- 1-2 sentence descriptions
- 3 acceptance criteria each
- Effort estimates
```

### Detailed Feature Breakdown
```
Create a comprehensive feature document for [feature] including:
- Problem statement
- User stories
- Technical requirements
- Task breakdown (at least 10 tasks)
- Dependencies and risks
```

### Estimate Refinement
```
Review these task estimates and provide:
- Adjusted estimates based on complexity
- Breakdown of large tasks (>8 hours)
- Risk factors that might increase time
```

### Priority Assessment
```
Given these tasks and project goals, help me prioritize by:
- Critical path items
- Dependencies
- Business value
- Technical risk
```

## Troubleshooting

### Output Too Generic?
- Provide more specific context
- Share technical stack details
- Describe constraints and requirements
- Give examples of similar work

### Estimates Seem Off?
- Share your team's velocity
- Provide historical data
- Adjust based on team expertise
- Account for unknowns

### Missing Details?
- Ask follow-up questions
- Request specific sections
- Expand on particular tasks
- Ask for examples

## Next Steps

After generating tasks with ChatGPT:
1. ✅ Copy output to repository (using Cursor)
2. ✅ Review and validate all details
3. ✅ Add metadata (dates, status: draft)
4. ✅ Commit to repository
5. ✅ Review manually
6. ✅ Create in Asana and assign
7. ✅ Update status in repository (using Cursor)

---

**Remember:** ChatGPT is a planning tool. Always review, validate, and adjust generated content based on your specific needs and context.
