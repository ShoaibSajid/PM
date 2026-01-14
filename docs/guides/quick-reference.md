# Three-Tool Workflow Quick Reference

## 🔄 The Workflow at a Glance

```
ChatGPT → Cursor → You (Manual Review) → Asana → Cursor → Asana
(Plan)    (Track)   (Review)            (Assign)  (Update) (Complete)
```

## 📱 Tool Overview

| Tool | Purpose | Used For |
|------|---------|----------|
| **ChatGPT** | Planning | Generate tasks, break down features, estimate effort |
| **Cursor** | Tracking | Create files, update status, commit changes |
| **Asana** | Assignment | Review, assign, set dates, track completion |

---

## 🚀 Quick Start

### 1️⃣ Planning with ChatGPT (5 min)
```
Prompt: "Break down [feature] into tasks with 
acceptance criteria and estimates"
→ Copy markdown output
```

### 2️⃣ Document with Cursor (2 min)
```bash
# Create file
docs/tasks/task-name.md
# Paste content
# Add metadata: status: draft
# Commit
git add . && git commit -m "Add task: [name]"
```

### 3️⃣ Review Yourself (5 min)
- Read task description
- Validate estimates
- Check acceptance criteria
- Update status to "ready" if approved

### 4️⃣ Assign in Asana (3 min)
- Create Asana task
- Assign to team member
- Set due date
- Copy Asana URL

### 5️⃣ Link in Cursor (1 min)
```markdown
**Asana Link:** [URL]
**Status:** assigned
```
Commit changes

### 6️⃣ Track Progress (Daily)
- Team updates Asana
- You/team updates repository via Cursor
- Commit progress notes

---

## 📋 Status Values

| Status | Meaning | Where |
|--------|---------|-------|
| `draft` | Just created, needs review | Repository only |
| `ready` | Reviewed, ready to assign | Repository only |
| `assigned` | Created in Asana, assigned | Both systems |
| `in-progress` | Being worked on | Both systems |
| `in-review` | Under review | Both systems |
| `done` | Completed | Both systems |

---

## 💡 Common Commands

### ChatGPT Prompts
```
# Generate tasks
"Create 5 tasks for [feature] with acceptance criteria"

# Break down feature
"Break down [feature] into phases and tasks"

# Estimate effort
"Estimate hours for each of these tasks: [list]"

# Refine task
"Add more detail and acceptance criteria to [task]"
```

### Cursor Commands
```bash
# Create task
cp docs/templates/task-template.md docs/tasks/new-task.md

# Update status
# Edit file, change **Status:** field

# Commit changes
git add . && git commit -m "Update: task progress"

# Daily sync
git pull && git add . && git commit -m "EOD updates" && git push
```

### Asana Actions
```
1. Create task from repository
2. Assign + set due date
3. Copy URL → update repository
4. Track completion
5. Mark done when complete
```

---

## 🎯 Daily Routine

### Morning (10 min)
- [ ] Pull latest from repository: `git pull`
- [ ] Review Asana: today's tasks
- [ ] Check for blockers

### During Day
- [ ] Update task status as you work (Cursor)
- [ ] Comment progress in Asana
- [ ] Commit changes: `git commit -am "Progress update"`

### Evening (10 min)
- [ ] Update completion % (Cursor)
- [ ] Add daily notes (Cursor)
- [ ] Commit: `git commit -am "EOD: [date]"`
- [ ] Push: `git push`
- [ ] Update Asana task status

---

## 📁 File Locations

```
docs/
├── tasks/           ← Individual tasks
├── features/        ← Feature breakdowns
├── bugs/           ← Bug tracking
├── templates/      ← Copy these to create new items
└── guides/         ← Help documentation
```

---

## ⚡ Quick Tips

### For Efficiency
1. **Batch Create**: Generate multiple tasks in one ChatGPT session
2. **Template Copy**: Use `cp` to quickly create from templates
3. **Bulk Update**: Use multi-cursor in Cursor for batch edits
4. **Daily Commits**: Commit at least once per day

### For Accuracy
1. **Review Everything**: Always review ChatGPT output
2. **Validate Estimates**: Adjust based on team capacity
3. **Keep Synced**: Update both Asana and repository
4. **Document Blockers**: Note issues immediately

### For Collaboration
1. **Link Everything**: Always link Asana ↔ Repository
2. **Clear Descriptions**: Write for your future self
3. **Update Progress**: Daily updates help everyone
4. **Communicate**: Use comments in both systems

---

## 🔗 Key Links

- **Repository**: `/home/runner/work/PM/PM` (or your path)
- **Templates**: `docs/templates/`
- **Guides**: `docs/guides/`
  - [ChatGPT Guide](docs/guides/chatgpt-guide.md)
  - [Cursor Guide](docs/guides/cursor-guide.md)
  - [Asana Guide](docs/guides/asana-guide.md)

---

## 🆘 Troubleshooting

### Task Not Clear?
→ Ask ChatGPT to expand/clarify

### Status Confused?
→ Check status meanings above

### Lost Changes?
→ Use `git log` to find commit

### Asana Link Missing?
→ Go to Asana, copy URL, update in Cursor

### Merge Conflict?
→ `git pull`, resolve in Cursor, commit

---

## 📊 Example: Complete Flow

```
1. ChatGPT: "Break down user authentication feature"
   → Get 8 tasks with details
   
2. Cursor: Create docs/features/user-auth.md
   → Paste content, add metadata
   → git commit -m "Add feature: user auth"
   
3. You: Review tasks 1-8
   → Validate estimates and requirements
   → Update status: draft → ready
   
4. Asana: Create project "User Authentication"
   → Create 8 tasks from feature file
   → Assign: Task 1-3 to John, 4-6 to Jane
   → Set due dates
   
5. Cursor: Update feature file
   → Add Asana project link
   → Add assignee names
   → Status: ready → assigned
   → Commit changes
   
6. Team: Works on tasks
   → Updates Asana daily
   → Updates repository via Cursor
   
7. You: Track progress
   → Review updates in both systems
   → Update repository with notes
   → Mark complete when done
```

---

## 🎓 Learning Path

### Day 1: Setup
- Read README
- Try creating first task with ChatGPT
- Practice Cursor file management

### Day 2-3: Practice
- Generate 3-5 tasks
- Create in repository
- Assign in Asana

### Week 1: Establish Routine
- Daily status updates
- Link tasks properly
- Keep systems synced

### Ongoing: Optimize
- Refine ChatGPT prompts
- Improve documentation
- Adjust workflow as needed

---

**🔥 Pro Tip**: Save this file as a bookmark or keep it open in a tab. Reference it until the workflow becomes second nature!
