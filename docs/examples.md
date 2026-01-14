# PM Assistant - Usage Examples

This document provides practical examples of using the PM Assistant to extract tasks from various types of inputs.

## Example 1: Email Thread

### Input

```text
From: client@company.com
Subject: Project Update Needed

Hi team,

We need to address a few items urgently:

- The API is returning 500 errors for the authentication endpoint @john
- Documentation needs to be updated with the new OAuth flow
- We're still waiting for the hardware sensors to arrive - can someone follow up with the vendor?
- Deploy the hotfix by tomorrow EOD

The API issue is blocking our testing. Please treat as high priority.

Thanks,
Client
```

### Command

```bash
pm-parse email.txt --source "Email from client" --output tasks.md
```

### Output

```markdown
# Actionable Tasks Summary

**Extracted:** 2026-01-14 14:30 KST
**Timezone:** Asia/Seoul

## 🔥 High Urgency Tasks

- **API is returning 500 errors for the authentication endpoint** (Software) - Owner: John

## Tasks by Category

### Software

**🚫 API is returning 500 errors for the authentication endpoint** 🔴
  - **Owner:** John
  - **Status:** Blocked
  - **Urgency:** High
  - **Next Follow-up:** Check with dependencies or John on blockers
  - **Source:** Email from client

**⭕ Deploy the hotfix** 🔴
  - **Owner:** Unassigned (Assumed)
  - **Status:** Not started
  - **Urgency:** High
  - **Deadline:** 2026-01-15 17:00
  - **Next Follow-up:** Assign owner and confirm scope
  - **Source:** Email from client

### Documentation

**⭕ Documentation needs to be updated with the new OAuth flow** 🟡
  - **Owner:** Unassigned (Assumed)
  - **Status:** Not started
  - **Urgency:** Medium
  - **Next Follow-up:** Assign owner and confirm scope
  - **Source:** Email from client

### Follow-ups

**⭕ Follow up with the vendor** 🟡
  - **Owner:** Unassigned (Assumed)
  - **Status:** Not started
  - **Urgency:** Medium
  - **Next Follow-up:** Assign owner and confirm scope
  - **Source:** Email from client
```

## Example 2: Chat Transcript

### Input

```text
[10:30] Alice: We found a critical bug in the payment processing
[10:31] Bob: Is it affecting production?
[10:31] Alice: Yes, urgent fix needed ASAP
[10:32] Alice: @john can you look at this?
[10:33] John: On it. Will need database access though
[10:34] Bob: I'll grant the permissions
[10:35] Alice: Also, we should document this issue for the postmortem
```

### Command

```bash
pm-parse chat.txt --source "Slack #incidents" --compact
```

### Output

```markdown
📋 **4 tasks extracted** (2026-01-14 14:35)

🔥 1 high urgency task(s)

- Software: 1
- Documentation: 1
- Follow-ups: 2
```

## Example 3: Meeting Notes

### Input

```text
Weekly Team Meeting - 2026-01-14

Action Items:
- Fix the motor controller sensor issue (hardware team)
- Order replacement parts from vendor X by Friday
- Update the technical specifications document
- Schedule follow-up meeting with client next week
- Code review for PR #123 - waiting on Sarah's approval

Blockers:
- Cannot proceed with integration testing until the staging environment is fixed (safety risk if we test in production)
```

### Command

```bash
pm-parse meeting_notes.txt --source "Weekly team meeting"
```

## Example 4: Sensitive Data Handling

### Input

```text
TODO: Update server config
- Server IP: 192.168.1.100
- Password: admin123
- API Key: ghp_1234567890abcdefghijklmnopqrstuv

@mike please handle this ASAP
```

### Output

```markdown
# Actionable Tasks Summary

**Extracted:** 2026-01-14 14:40 KST
**Timezone:** Asia/Seoul

## ⚠️ Warnings

- Sensitive data detected and removed: (IP omitted)
- Sensitive data detected and removed: password: (omitted)
- Sensitive data detected and removed: (GitHub token omitted)

## 🔥 High Urgency Tasks

- **Update server config** (Software) - Owner: Mike

## Tasks by Category

### Software

**⭕ Update server config** 🔴
  - **Owner:** Mike
  - **Status:** Not started
  - **Urgency:** High
  - **Next Follow-up:** Check progress with Mike
  - **Source:** (credentials requested)
```

## Example 5: Complex Multi-Category Input

### Input

```text
Project Status Update:

Software:
- [ ] Implement user authentication API
- [x] Fix database connection pooling issue
- [ ] Deploy staging environment by tomorrow

Hardware:
- Replace broken sensor on assembly line 3 (urgent - safety risk)
- Order 50 units of motor controllers from Vendor Y
- Test new circuit board design

Documentation:
- Write installation guide for new hardware
- Update API documentation with authentication endpoints

All software tasks are waiting on DevOps to provision the servers.
```

### Python API Usage

```python
from src.parser import TaskParser
from src.formatter import AsanaFormatter

# Read input
with open('project_status.txt', 'r') as f:
    text = f.read()

# Parse
parser = TaskParser(timezone="Asia/Seoul")
summary = parser.parse(text, source="Project status update")

# Format
formatter = AsanaFormatter()
markdown = formatter.format_summary(summary)

# Save to file
with open('tasks_for_asana.md', 'w') as f:
    f.write(markdown)

# Print stats
print(f"Extracted {len(summary.tasks)} tasks")
print(f"High urgency: {sum(1 for t in summary.tasks if t.urgency == 'High')}")
print(f"Warnings: {len(summary.warnings)}")
```

## Example 6: Stdin Pipeline

```bash
# From clipboard (macOS)
pbpaste | pm-parse - --source "Clipboard"

# From another command
curl https://example.com/meeting-notes.txt | pm-parse - --output tasks.md

# With preprocessing
cat notes.txt | grep "TODO" | pm-parse - --compact
```

## Example 7: Automated Processing Script

```bash
#!/bin/bash
# process_daily_tasks.sh

DATE=$(date +%Y-%m-%d)
SOURCE_DIR="$HOME/notes"
OUTPUT_DIR="$HOME/tasks"

# Process all text files from today
for file in "$SOURCE_DIR"/*"$DATE"*.txt; do
    if [ -f "$file" ]; then
        basename=$(basename "$file" .txt)
        pm-parse "$file" \
            --source "Daily notes: $basename" \
            --output "$OUTPUT_DIR/$basename-tasks.md"
    fi
done

echo "✓ Processed all notes for $DATE"
```

## Example 8: Integration with Git Hooks

```bash
#!/bin/bash
# .git/hooks/commit-msg

# Extract tasks from commit messages
COMMIT_MSG_FILE=$1
COMMIT_MSG=$(cat "$COMMIT_MSG_FILE")

# Check for TODO or FIXME in commit
if echo "$COMMIT_MSG" | grep -qE "TODO|FIXME"; then
    echo "Found tasks in commit message:"
    echo "$COMMIT_MSG" | pm-parse - --compact
fi
```

## Example 9: Custom Category Detection

When the parser encounters domain-specific terms:

```text
Input:
- Fix the PLC programming bug in station 4
- Update the ladder logic for conveyor belt
- Order pneumatic cylinders
- Replace worn bearings on motor 3

Expected categories:
- PLC/ladder logic → Software (industrial control software)
- Pneumatic/bearings → Mechanical/Hardware
- Order → Logistics
```

## Tips for Better Task Extraction

1. **Use clear task markers**: Start lines with `-`, `*`, `TODO:`, or `Action:`
2. **Mention owners explicitly**: Use `@username` or `Owner: Name`
3. **Include urgency keywords**: "urgent", "ASAP", "low priority"
4. **Specify deadlines**: "by tomorrow", "due Jan 20", "deadline Friday"
5. **Flag blockers**: "blocked by", "waiting for", "cannot proceed"
6. **Note risks**: "safety risk", "schedule risk", "unstable"
7. **Group by category**: Use headers like "Software:", "Hardware:"

## Advanced Python Usage

### Custom Timezone

```python
parser = TaskParser(timezone="America/New_York")
summary = parser.parse(text)
```

### Filter High Urgency Tasks

```python
summary = parser.parse(text)
high_urgency = [t for t in summary.tasks if t.urgency == "High"]
for task in high_urgency:
    print(f"🔥 {task.title} - Owner: {task.owner}")
```

### Get Tasks by Category

```python
from schemas.task_model import TaskCategory

summary = parser.parse(text)
software_tasks = summary.get_tasks_by_category(TaskCategory.SOFTWARE)
print(f"Software tasks: {len(software_tasks)}")
```

### Check for Sensitive Data

```python
from src.sensitivity import SensitivityScrubber

scrubber = SensitivityScrubber()
if scrubber.has_sensitive_data(text):
    print("⚠️ Warning: Input contains sensitive data")
    scrubbed, warnings = scrubber.scrub(text)
    # Use scrubbed text
```

## Troubleshooting Common Issues

### No Tasks Extracted

**Problem**: Parser returns empty task list

**Solutions**:
1. Add task markers (`-`, `*`, `TODO:`)
2. Ensure text is not just a paragraph (break into lines)
3. Check that lines are long enough (>5 characters)

### Wrong Category Detected

**Problem**: Task categorized incorrectly

**Solutions**:
1. Add category keywords to task description
2. Use category headers in input
3. Explicitly mention domain-specific terms

### Owner Not Detected

**Problem**: All tasks show "Unassigned (Assumed)"

**Solutions**:
1. Use `@username` format
2. Add "Owner: Name" or "assigned to Name"
3. Put owner mentions early in task description

### Deadline Not Parsed

**Problem**: Deadlines not showing up

**Solutions**:
1. Use clear date formats: "by Jan 20", "deadline: 2026-01-15"
2. Use relative dates: "by tomorrow", "due today"
3. Use keywords: "by", "due", "deadline", "before"

---

For more information, see the [README](../README.md) or contact the project team.
