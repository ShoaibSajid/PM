# PM Assistant - Industrial Project Coordination Assistant

Turn messy inputs (chat transcripts, notes, emails, screenshots) into clear task candidates that the project owner can copy into Asana.

## 🎯 Primary Objective

Extract actionable tasks from unstructured communications and format them into copy-paste ready task lists for Asana. The assistant does not create or update Asana items directly.

## 🚀 Features

- **Task Extraction**: Parses chat transcripts, emails, notes, and other messy inputs
- **Automatic Categorization**: Groups tasks by Software, Mechanical/Hardware, Logistics, Documentation, Follow-ups
- **Status Detection**: Identifies task status (Not started, In progress, Blocked, etc.)
- **Urgency Assessment**: Determines task urgency (High, Medium, Low)
- **Risk Identification**: Flags dependencies, safety concerns, schedule risks
- **Sensitivity Scrubbing**: Automatically removes credentials, secrets, tokens, IPs
- **Timezone Support**: Handles dates/times with Asia/Seoul (KST) as default

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/ShoaibSajid/PM.git
cd PM

# Install dependencies
pip install -e .

# For development
pip install -e ".[dev]"
```

## 💻 Usage

### Command Line Interface

```bash
# Parse a text file
pm-parse meeting_notes.txt

# Parse from stdin
cat transcript.txt | pm-parse -

# Specify source and output file
pm-parse notes.txt --source "Team meeting 2026-01-14" --output tasks.md

# Compact output for quick review
pm-parse notes.txt --compact

# Specify timezone
pm-parse notes.txt --timezone "America/New_York"
```

### Python API

```python
from src.parser import TaskParser
from src.formatter import AsanaFormatter

# Parse tasks from text
parser = TaskParser(timezone="Asia/Seoul")
summary = parser.parse(text_input, source="Email from client")

# Format for Asana
formatter = AsanaFormatter()
markdown_output = formatter.format_summary(summary)
print(markdown_output)

# Compact format
compact = formatter.format_compact_summary(summary)
print(compact)
```

## 📝 Input Format

The parser accepts various input formats:

```text
- Fix the API bug @john (urgent)
- Update documentation by tomorrow
TODO: Order replacement sensors
Action: Follow up with vendor about delivery
```

### Recognized Patterns

- **Task markers**: `- `, `* `, `• `, `TODO:`, `Action:`
- **Owner mentions**: `@username`, `Owner: John`, `assigned to Alice`
- **Status keywords**: `blocked`, `in progress`, `waiting for`
- **Urgency keywords**: `urgent`, `asap`, `critical`, `low priority`
- **Deadlines**: `by tomorrow`, `due Jan 20`, `deadline: 2026-01-15`
- **Risks**: `risk`, `safety`, `delay`, `unstable`

## 📤 Output Format

Each task includes:

- **Title**: Copy-paste ready, imperative verb, single objective
- **Owner**: Explicit if mentioned; otherwise inferred and marked as "Assumed"
- **Status**: Not started / In progress / Blocked / Waiting on X / Needs clarification
- **Urgency**: High / Medium / Low
- **Next Follow-up**: What to ask/check next
- **Risks**: Dependencies, safety concerns, schedule risks, system instability

### Example Output

```markdown
# Actionable Tasks Summary

**Extracted:** 2026-01-14 12:00 KST
**Timezone:** Asia/Seoul

## 🔥 High Urgency Tasks

- **Fix API authentication bug** (Software) - Owner: John

## Tasks by Category

### Software

**🔄 Fix API authentication bug** 🔴
  - **Owner:** John
  - **Status:** In progress
  - **Urgency:** High
  - **Next Follow-up:** Check progress with John
  - **⚠️ Risks:**
    - May affect production users

### Logistics

**⭕ Order replacement sensors** 🟡
  - **Owner:** Unassigned (Assumed)
  - **Status:** Not started
  - **Urgency:** Medium
  - **Deadline:** 2026-01-20 17:00
  - **Next Follow-up:** Assign owner and confirm scope
```

## 🔒 Safety & Sensitivity

The assistant automatically scrubs sensitive information:

- Credentials (passwords, usernames)
- API keys and tokens
- IP addresses
- Private keys
- GitHub tokens
- AWS keys

Sensitive data is replaced with `(sensitive details omitted)` and warnings are added to the output.

## 🕐 Date/Time Handling

- **Default timezone**: Asia/Seoul (KST)
- **Relative dates**: "today", "tomorrow", "next week" are converted to explicit dates
- **Assumed deadlines**: Marked clearly when inferred from context

## 🏗️ Project Structure

```
PM/
├── src/                    # Core logic
│   ├── __init__.py
│   ├── parser.py          # Task extraction from text
│   ├── formatter.py       # Asana markdown formatting
│   ├── sensitivity.py     # Credential scrubbing
│   └── cli.py            # Command-line interface
├── schemas/               # Data models
│   ├── __init__.py
│   └── task_model.py     # TaskCandidate schema
├── tests/                 # Unit tests
│   ├── test_parser.py
│   ├── test_formatter.py
│   └── test_sensitivity.py
├── docs/                  # Documentation
│   └── examples.md       # Usage examples
├── pyproject.toml        # Project configuration
└── README.md             # This file
```

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov=schemas

# Run specific test file
pytest tests/test_parser.py
```

## 🛠️ Development

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code (if using black)
black src/ schemas/ tests/

# Type checking (if using mypy)
mypy src/ schemas/
```

## 📋 Task Handling Rules

1. **Never assume tasks exist in Asana** - Treat everything as candidate tasks
2. **Never mark tasks as Done** - Unless explicitly confirmed
3. **Make reasonable assumptions** - But label them clearly as "Assumed"
4. **Ask clarifying questions** - Only if task extraction is completely blocked
5. **Flag missing info** - Owner, deadline, scope uncertainties

## 🎨 Communication Style

- Clear, concise, and neutral
- Bullet points and compact tables
- No long paragraphs
- Focus on operational next steps
- No judgement or decision-making

## 🤝 Contributing

This is an internal project coordination tool. For improvements:

1. Keep the codebase clean and well-documented
2. Add tests for new features
3. Update documentation
4. Follow existing code style

## 📄 License

Internal use for "Shoaib - Project Management" projects.

## 🔧 Troubleshooting

### Import Errors

If you encounter import errors, ensure you're in the project root and have installed the package:

```bash
cd /path/to/PM
pip install -e .
```

### Timezone Issues

If dates are not being parsed correctly, verify your timezone setting:

```bash
pm-parse notes.txt --timezone "Asia/Seoul"
```

### No Tasks Extracted

If no tasks are found, ensure your input follows recognizable patterns:
- Start tasks with `-`, `*`, or `•`
- Use keywords like `TODO:` or `Action:`
- Make sure text is not empty

## 📞 Support

For issues or questions about this assistant, contact the project team.

---

**Version**: 0.1.0  
**Last Updated**: 2026-01-14