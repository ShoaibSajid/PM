# PM - Shoaib Project Management

**Industrial Project Coordination Assistant**

Transform messy project communications into structured, copy-ready task candidates for Asana.

---

## 🎯 Primary Objective

Turn messy inputs (chat transcripts, notes, emails, screenshots) into clear task candidates that you can review and copy into Asana. **This system does not create or update Asana items directly** - it prepares candidates for your manual review.

## 🔄 Workflow

```
Messy Input → Task Extraction → Structured Output → Your Review → Asana Entry
(Chat/Email)   (Automated)      (Copy-Ready)       (Manual)       (Manual)
```

## 📥 Supported Inputs

- Chat transcripts (Slack, Teams, WhatsApp, etc.)
- Email threads
- Meeting notes
- Voice-to-text transcripts
- Screenshots with OCR text
- Mixed/unstructured documentation

## 📤 Output Format

Tasks are automatically categorized and formatted with required fields for easy copy-paste into Asana.

### Task Categories
1. **Software** - Code, scripts, config, testing
2. **Mechanical/Hardware** - Physical components, assembly
3. **Logistics** - Procurement, shipping, scheduling
4. **Documentation** - Manuals, reports, specifications
5. **Follow-ups** - Status checks, clarifications

### Task Fields (Every Task)
- **Title**: Copy-paste ready, imperative verb, single objective
- **Owner**: Explicit if mentioned; "Assumed" if inferred
- **Status**: Not started / In progress / Blocked / Waiting on X / Needs clarification
- **Urgency**: High / Medium / Low
- **Next follow-up**: What to ask/check next with KST date
- **Risks**: Dependencies, safety, schedule concerns

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/ShoaibSajid/PM.git
cd PM

# Install dependencies
pip install -r requirements.txt
```

### Usage

#### Extract tasks from a file
```bash
python scripts/extract_tasks.py --input chat_transcript.txt
```

#### Save output to file
```bash
python scripts/extract_tasks.py --input email.txt --output tasks_2026-01-14.md
```

#### With summary statistics
```bash
python scripts/extract_tasks.py --input notes.txt --summary
```

#### Batch processing
```bash
python scripts/extract_tasks.py --input-dir ./inputs/ --output-dir ./outputs/
```

### Example

See `docs/examples/` for sample inputs and outputs:
- `chat_transcript_example.txt` - Example chat input
- `expected_output_example.md` - Example formatted output

## 🔒 Safety & Sensitivity

- **Never prints credentials, secrets, tokens, passwords, IP addresses**
- Sensitive information replaced with: `(sensitive details omitted)`
- Security items flagged for manual handling
- Safe for sharing outputs with stakeholders

## 🕐 Date/Time Rules

- **Always uses Asia/Seoul (KST) timezone**
- "Today" → explicit date (e.g., "2026-01-14")
- "Tomorrow" → explicit date (e.g., "2026-01-15")
- Relative dates converted to calendar dates
- Unclear deadlines marked as "Assumed"

## 📋 Task Handling Rules

1. **Never assumes tasks exist in Asana** - all outputs are candidates
2. **Never marks tasks as "Done"** unless explicitly confirmed in input
3. **Flags missing information** (owner, deadline, scope) as "Assumed"
4. **Extracts implicit status changes** (blocked, waiting, delayed)
5. **Identifies dependencies and risks** automatically

## 📁 Repository Structure

```
PM/
├── src/                          # Core task extraction pipeline
│   ├── models.py                 # Task data models
│   ├── parser.py                 # Text parsing logic
│   ├── formatter.py              # Output formatting
│   ├── sensitivity.py            # Credential scrubbing
│   └── date_utils.py             # KST date handling
├── schemas/                      # Task schemas
│   └── task_candidate.py         # TaskCandidate definition
├── scripts/                      # CLI utilities
│   └── extract_tasks.py          # Main extraction script
├── tests/                        # Unit tests
├── docs/                         # Documentation
│   ├── examples/                 # Example inputs/outputs
│   ├── guides/                   # Usage guides
│   └── templates/                # Task templates
├── requirements.txt              # Python dependencies
├── pyproject.toml                # Project metadata
├── config.yaml                   # Configuration
└── README.md                     # This file
```

## 🧪 Testing

```bash
# Run all tests
python -m pytest

# Run specific test file
python tests/test_parser.py

# Run with coverage
pytest --cov=src
```

## 📚 Documentation

- **Examples**: See `docs/examples/` for sample inputs and outputs
- **Guides**: See `docs/guides/` for detailed usage guides
- **Contributing**: See `CONTRIBUTING.md` for contribution guidelines
- **Roadmap**: See `ROADMAP.md` for project roadmap

## 🎯 Communication Style

- **Clear and concise** - no fluff
- **Bullet points preferred** over paragraphs
- **Compact tables** for structured data
- **Operational focus** - next steps, not judgement
- **Neutral tone** - factual reporting

## ⚙️ Features

### Automatic Detection
- ✅ Task extraction from unstructured text
- ✅ Status inference (blocked, waiting, in progress)
- ✅ Owner identification (explicit or inferred)
- ✅ Urgency assessment
- ✅ Risk and dependency flagging
- ✅ Sensitivity scrubbing

### Output Formats
- ✅ Markdown (Asana-ready)
- ✅ JSON (for integration)
- ✅ CSV (for spreadsheets)
- ✅ Plain text (minimal)

## 🤝 Contributing

See `CONTRIBUTING.md` for how to contribute to this project.

## 📄 License

This project is for internal use within Shoaib Project Management.

## 🆘 Support

For questions or issues:
1. Check `docs/examples/` and `docs/guides/`
2. Search [existing issues](../../issues)
3. Open a [new issue](../../issues/new)

---

**Version**: 1.0.0  
**Last Updated**: 2026-01-14  
**Timezone**: Asia/Seoul (KST)
