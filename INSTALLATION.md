# Installation Guide

## Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git

## Quick Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ShoaibSajid/PM.git
cd PM
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or use the package installation:

```bash
pip install -e .
```

### 3. Verify Installation

Test the extraction pipeline:

```bash
python scripts/extract_tasks.py --input docs/examples/chat_transcript_example.txt
```

You should see extracted task candidates formatted as markdown.

## Installation Options

### Option 1: Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Option 2: System-Wide Installation

```bash
pip install -r requirements.txt
```

### Option 3: Development Installation

For development work with editable installation:

```bash
pip install -e .[dev]
```

This includes development dependencies (pytest, black, flake8, mypy).

## Verifying Installation

### Run Tests

```bash
# Run all tests
python -m pytest

# Or run individual test files
python tests/test_parser.py
python tests/test_sensitivity.py
python tests/test_date_utils.py
python tests/test_formatter.py
```

### Test Extraction

```bash
python scripts/extract_tasks.py --input docs/examples/chat_transcript_example.txt
```

Expected output: Extracted task candidates grouped by category.

## Configuration

### Edit Config File

Default configuration is in `config.yaml`:

```yaml
timezone: "Asia/Seoul"
default_urgency: "Medium"
output_format: "markdown"
sensitivity_mode: "strict"
```

Customize as needed for your workflow.

## Usage

### Command Line

```bash
# Extract from file
python scripts/extract_tasks.py --input your_file.txt

# Save to output file
python scripts/extract_tasks.py --input input.txt --output tasks.md

# With summary
python scripts/extract_tasks.py --input input.txt --summary

# Different format
python scripts/extract_tasks.py --input input.txt --format json
```

### Python API

```python
from src.parser import TaskExtractor
from src.formatter import format_tasks_for_asana

extractor = TaskExtractor()
tasks = extractor.parse("Your text here...")
output = format_tasks_for_asana(tasks)
print(output)
```

## Troubleshooting

### ModuleNotFoundError

If you get import errors:

```bash
# Make sure you're in the PM directory
cd PM

# Install dependencies
pip install -r requirements.txt

# Or add to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### Timezone Issues

If timezone errors occur:

```bash
# Install pytz explicitly
pip install pytz

# On Windows, also install tzdata
pip install tzdata
```

### Python Version

Verify Python version:

```bash
python3 --version
```

Should be 3.9 or higher.

## Next Steps

1. Read the [Usage Guide](docs/guides/usage-guide.md)
2. Try the examples in `docs/examples/`
3. Process your own data
4. Review [README.md](README.md) for full documentation

## Support

For issues:
1. Check [Usage Guide](docs/guides/usage-guide.md)
2. Review examples in `docs/examples/`
3. Open an issue on GitHub

---

**Version**: 1.0.0  
**Last Updated**: 2026-01-14
