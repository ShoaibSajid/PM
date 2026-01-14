# Usage Guide - Industrial Project Coordination Assistant

## Overview

This system extracts actionable task candidates from messy inputs (chat transcripts, emails, meeting notes) and formats them for easy copy-paste into Asana.

## Quick Start

### 1. Installation

```bash
cd PM
pip install -r requirements.txt
```

### 2. Basic Usage

#### Extract from a file:
```bash
python scripts/extract_tasks.py --input your_chat_log.txt
```

#### Save to file:
```bash
python scripts/extract_tasks.py --input meeting_notes.txt --output tasks_output.md
```

#### Get summary statistics:
```bash
python scripts/extract_tasks.py --input notes.txt --summary
```

## Input Format

### Supported File Types
- `.txt` - Plain text files
- `.md` - Markdown files
- Any text-based format (chat logs, emails, notes)

### Example Input

```
[10:32] John: Hey team, we need to test the motor controller firmware v2.3 before deployment. This is urgent.

[10:35] Sarah: I can handle that. When do you need it by?

[10:36] John: Tomorrow would be ideal. The production line is waiting.

[10:40] Mike: Also, we need to calibrate the pressure sensors on unit #3.
```

## Output Format

### Standard Output (Markdown)

Tasks are grouped by category with all required fields:

```markdown
## Software Tasks

### Task: Test motor controller firmware v2.3
- **Owner**: Sarah
- **Status**: Not started
- **Urgency**: High
- **Next follow-up**: Confirm by 2026-01-15 (KST)
- **Risks**: Production line blocked if not completed

## Mechanical/Hardware Tasks

### Task: Calibrate pressure sensors on unit #3
- **Owner**: Mike (Assumed)
- **Status**: Not started
- **Urgency**: Medium
- **Next follow-up**: Check status by 2026-01-16 (KST)
- **Risks**: None identified
```

## Workflow

### 1. Collect Input
Gather your project communications:
- Copy chat transcripts
- Save email threads
- Export meeting notes
- Any unstructured text

### 2. Run Extraction
```bash
python scripts/extract_tasks.py --input input.txt --output tasks.md
```

### 3. Review Output
Open `tasks.md` and review extracted tasks:
- Check accuracy of task titles
- Verify owner assignments
- Validate urgency levels
- Review next follow-up actions
- Confirm risk assessments

### 4. Copy to Asana
For each task:
1. Open Asana
2. Create new task
3. Copy title from output
4. Paste description details
5. Set assignee (from Owner field)
6. Set priority (from Urgency field)
7. Set due date (from Next follow-up)
8. Add risks to notes/comments

## Advanced Usage

### Batch Processing

Process multiple files at once:

```bash
python scripts/extract_tasks.py \
  --input-dir ./meeting_notes/ \
  --output-dir ./extracted_tasks/
```

This will:
- Process all `.txt` and `.md` files in `meeting_notes/`
- Create corresponding `*_tasks.md` files in `extracted_tasks/`

### Output Formats

#### JSON (for integration):
```bash
python scripts/extract_tasks.py --input notes.txt --format json --output tasks.json
```

#### CSV (for spreadsheets):
```bash
python scripts/extract_tasks.py --input notes.txt --format csv --output tasks.csv
```

#### Plain Text:
```bash
python scripts/extract_tasks.py --input notes.txt --format plain --output tasks.txt
```

### Category Filtering

Extract only specific categories:

```bash
# Software tasks only
python scripts/extract_tasks.py --input notes.txt --category Software

# Logistics tasks only
python scripts/extract_tasks.py --input notes.txt --category Logistics
```

## Python API

### Basic Example

```python
from src.parser import TaskExtractor
from src.formatter import format_tasks_for_asana

# Initialize extractor
extractor = TaskExtractor()

# Parse text
text = """
John needs to test the firmware by tomorrow. This is urgent.
Sarah will update the documentation.
"""

tasks = extractor.parse(text)

# Format output
output = format_tasks_for_asana(tasks, format_type="markdown")
print(output)
```

### Advanced Example

```python
from src.parser import TaskExtractor
from src.formatter import generate_summary
from src.sensitivity import scrub_sensitive_info

# Scrub sensitive info first
text = "Password: secret123. Deploy the API to 192.168.1.100"
scrubbed_text, was_scrubbed = scrub_sensitive_info(text)

# Extract tasks
extractor = TaskExtractor()
tasks = extractor.parse(scrubbed_text, source="email_thread.txt")

# Generate summary
summary = generate_summary(tasks)
print(summary)

# Get tasks by category
software_tasks = [t for t in tasks if t.category == "Software"]
print(f"Found {len(software_tasks)} software tasks")
```

## Understanding Output Fields

### Title
- **Format**: Imperative verb + objective
- **Example**: "Test motor controller firmware v2.3"
- **Purpose**: Copy directly to Asana task title

### Owner
- **Explicit**: "John" - name mentioned in text
- **Assumed**: "John (Assumed)" - inferred from context
- **Default**: "Team Member (Assumed)" - no clear owner

### Status
- **Not started**: New task, not yet begun
- **In progress**: Actively being worked on
- **Blocked**: Cannot proceed due to blocker
- **Waiting on X**: Waiting for something/someone
- **Needs clarification**: Unclear requirements

### Urgency
- **High**: Urgent, critical, must do, ASAP, deadline
- **Medium**: Normal priority (default)
- **Low**: Nice to have, when possible, optional

### Next Follow-up
- **Format**: "Action by YYYY-MM-DD (KST)"
- **Assumed**: Marked if date is inferred
- **Purpose**: Set reminder/due date in Asana

### Risks
- Identifies potential issues
- Dependencies between tasks
- Safety concerns
- Schedule risks
- System stability issues

## Best Practices

### For Best Results

1. **Feed Quality Input**
   - Include names when possible
   - Mention deadlines explicitly
   - Note urgency levels
   - Describe dependencies

2. **Review All Output**
   - Verify extracted information
   - Adjust assumed fields
   - Correct misinterpreted tasks
   - Add missing context

3. **Consistent Workflow**
   - Process inputs daily
   - Review before creating Asana tasks
   - Keep naming conventions
   - Archive processed inputs

### Common Patterns

#### High-Quality Input
```
✅ "John needs to test firmware v2.3 by Thursday. This is urgent because
    the production line is waiting. He'll need the test environment ready first."
```

#### Low-Quality Input
```
❌ "Someone should do something about the thing soon."
```

#### Better Alternative
```
✅ "Sarah should update the API documentation by end of week. The mobile team
    needs it for their integration work."
```

## Troubleshooting

### No Tasks Extracted
- **Cause**: Input lacks action keywords
- **Solution**: Ensure input contains verbs like "need to", "must", "should", "implement", etc.

### Wrong Owner Assignment
- **Cause**: Ambiguous names or pronouns
- **Solution**: Use explicit names in input or manually correct in Asana

### Incorrect Categorization
- **Cause**: Task description lacks clear indicators
- **Solution**: Add keywords (e.g., "deploy code" → Software, "order parts" → Logistics)

### Sensitive Info Not Scrubbed
- **Cause**: Unusual format not detected
- **Solution**: Check config.yaml sensitivity_mode, manually review output

### Dates Not Parsed
- **Cause**: Unclear date references
- **Solution**: Use explicit dates ("2026-01-15") or clear relative dates ("tomorrow")

## Configuration

Edit `config.yaml` to customize behavior:

```yaml
# Timezone for all dates
timezone: "Asia/Seoul"

# Default values
default_urgency: "Medium"
default_status: "Not started"

# Output format
output_format: "markdown"

# Sensitivity scrubbing
sensitivity_mode: "strict"  # strict | moderate | lenient
```

## Tips & Tricks

### Tip 1: Use Templates
Create input templates for common scenarios:
- Daily standup notes
- Weekly status reports
- Client emails
- Meeting minutes

### Tip 2: Batch Process
Process multiple inputs at once:
```bash
# Put all files in inputs/
python scripts/extract_tasks.py --input-dir inputs/ --output-dir outputs/
```

### Tip 3: Add Context
Include project context in input:
```
Project: Motor Controller V2
Date: 2026-01-14
Team: John, Sarah, Mike

[Tasks here...]
```

### Tip 4: Use Summary
Get overview before reviewing details:
```bash
python scripts/extract_tasks.py --input notes.txt --summary
```

### Tip 5: Pipe to Clipboard
Copy output directly to clipboard (macOS):
```bash
python scripts/extract_tasks.py --input notes.txt | pbcopy
```

Or on Linux:
```bash
python scripts/extract_tasks.py --input notes.txt | xclip -selection clipboard
```

## Examples

See `docs/examples/` for:
- `chat_transcript_example.txt` - Sample chat input
- `expected_output_example.md` - Expected output format

## Next Steps

1. **Try the examples**
   ```bash
   python scripts/extract_tasks.py --input docs/examples/chat_transcript_example.txt
   ```

2. **Process your own data**
   - Collect some chat logs or notes
   - Run extraction
   - Review output
   - Copy to Asana

3. **Refine your workflow**
   - Adjust configuration
   - Create input templates
   - Automate batch processing
   - Integrate with your tools

## Support

For help:
- Check this guide
- Review `README.md`
- See examples in `docs/examples/`
- Open an issue on GitHub

---

**Remember**: This tool extracts task **candidates**. Always review and validate before creating tasks in Asana!
