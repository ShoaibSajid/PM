# Quick Start Guide - PM Assistant

This guide will help you get started with the PM Assistant in 5 minutes.

## Installation

```bash
# Clone the repository
git clone https://github.com/ShoaibSajid/PM.git
cd PM

# Install dependencies
pip install -e .
```

## Basic Usage

### 1. Parse a Text File

Create a file called `tasks.txt`:
```
- Fix the API bug @john (urgent)
- Update documentation
- Order new sensors by Friday
```

Run the parser:
```bash
pm-parse tasks.txt
```

### 2. Parse from Clipboard

```bash
# macOS
pbpaste | pm-parse -

# Linux (with xclip)
xclip -o | pm-parse -

# Windows (with PowerShell)
Get-Clipboard | pm-parse -
```

### 3. Save Output to File

```bash
pm-parse tasks.txt --output asana_tasks.md
```

### 4. Compact Output for Quick Review

```bash
pm-parse tasks.txt --compact
```

## Python API

```python
from src.parser import TaskParser
from src.formatter import AsanaFormatter

# Parse text
parser = TaskParser(timezone="Asia/Seoul")
summary = parser.parse("- Fix critical bug @alice", source="Daily standup")

# Format for Asana
formatter = AsanaFormatter()
markdown = formatter.format_summary(summary)
print(markdown)
```

## Common Patterns

### Meeting Notes
```
Meeting Notes - 2026-01-14

Action Items:
- Fix authentication bug @john (urgent)
- Update API docs
- Deploy to staging by tomorrow

Blockers:
- Waiting for database migration
```

### Email or Chat
```
From: team@company.com

Hi team, we need to:
- Order 50 sensors from vendor X
- Replace broken motor on line 3 (safety risk!)
- Test new firmware version

Thanks!
```

### Task List
```
TODO:
- Implement user login
- Fix payment processing bug
- Update database schema

URGENT:
- Deploy hotfix to production ASAP
```

## Features in Action

### Automatic Owner Detection
```
Input:  "Fix bug @john"
Output: Owner: John

Input:  "Fix bug assigned to alice"
Output: Owner: Alice

Input:  "Fix bug"
Output: Owner: Unassigned (Assumed)
```

### Status Detection
```
Input:  "Fix bug - blocked by database"
Output: Status: Blocked

Input:  "Working on feature X"
Output: Status: In progress

Input:  "Waiting for approval from manager"
Output: Status: Waiting on - Waiting on Approval From Manager
```

### Urgency Detection
```
Input:  "Fix bug ASAP"
Output: Urgency: High

Input:  "Update docs (low priority)"
Output: Urgency: Low

Input:  "Order parts"
Output: Urgency: Medium (default)
```

### Deadline Extraction
```
Input:  "Deploy by tomorrow"
Output: Deadline: 2026-01-15 17:00

Input:  "Complete report due Jan 20"
Output: Deadline: 2026-01-20 17:00
```

### Category Classification
```
Input:  "Fix API bug in database"
Output: Category: Software

Input:  "Replace sensor on motor"
Output: Category: Mechanical/Hardware

Input:  "Order 10 parts from vendor"
Output: Category: Logistics

Input:  "Write installation guide"
Output: Category: Documentation

Input:  "Follow up with client"
Output: Category: Follow-ups
```

### Risk Detection
```
Input:  "Deploy update (safety risk with new code)"
Output: ⚠️ Risks:
         - Deploy update (safety risk with new code)
```

### Sensitive Data Scrubbing
```
Input:  "Server password: secret123 at IP 192.168.1.1"
Output: Server password: (omitted) at IP (IP omitted)
        ⚠️ Warnings:
        - Sensitive data detected and removed
```

## Tips for Better Results

1. **Use clear task markers**: Start lines with `-`, `*`, or `TODO:`
2. **Mention owners explicitly**: Use `@username` or `Owner: Name`
3. **Include urgency keywords**: "urgent", "ASAP", "low priority"
4. **Specify deadlines**: "by tomorrow", "due Jan 20"
5. **Flag blockers**: "blocked", "waiting for"
6. **Note risks**: "safety risk", "schedule risk"

## Troubleshooting

### No tasks extracted?
- Ensure lines start with `-`, `*`, `•`, or keywords like `TODO:`
- Check that text is not just a paragraph

### Wrong category?
- Add category keywords: "code", "software", "hardware", "sensor", "order", "document"

### Owner not detected?
- Use `@username` or `Owner: Name` format
- Put owner mentions early in the task description

## Next Steps

- Read the [full README](../README.md) for detailed information
- Check [examples.md](examples.md) for more usage patterns
- Run `scripts/example_api_usage.py` for Python API examples
- Write your own scripts using the PM Assistant API

## Support

For questions or issues, contact the project team or check the documentation.

---

**Happy task extracting! 🎯**
