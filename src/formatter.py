"""Output formatter for task candidates."""

from typing import List, Dict
from collections import defaultdict
import json

from schemas.task_candidate import TaskCandidate


def format_tasks_for_asana(tasks: List[TaskCandidate], format_type: str = "markdown") -> str:
    """
    Format extracted tasks for Asana.
    
    Args:
        tasks: List of TaskCandidate objects
        format_type: Output format ("markdown", "json", "csv", "plain")
    
    Returns:
        Formatted string ready for copy-paste
    """
    if format_type == "markdown":
        return _format_markdown(tasks)
    elif format_type == "json":
        return _format_json(tasks)
    elif format_type == "csv":
        return _format_csv(tasks)
    elif format_type == "plain":
        return _format_plain(tasks)
    else:
        raise ValueError(f"Unknown format type: {format_type}")


def _format_markdown(tasks: List[TaskCandidate]) -> str:
    """Format tasks as Asana-ready markdown."""
    if not tasks:
        return "No tasks extracted."
    
    # Group by category
    categorized = _group_by_category(tasks)
    
    output_lines = ["# Extracted Task Candidates", ""]
    output_lines.append(f"**Total Tasks**: {len(tasks)}")
    output_lines.append(f"**Extracted**: {tasks[0].extracted_at.strftime('%Y-%m-%d %H:%M KST')}")
    output_lines.append("")
    output_lines.append("---")
    output_lines.append("")
    
    # Output tasks by category
    for category in ["Software", "Mechanical/Hardware", "Logistics", "Documentation", "Follow-ups"]:
        if category in categorized:
            output_lines.append(f"## {category} Tasks")
            output_lines.append("")
            
            for task in categorized[category]:
                output_lines.append(task.to_markdown())
                output_lines.append("")
            
            output_lines.append("---")
            output_lines.append("")
    
    return "\n".join(output_lines)


def _format_json(tasks: List[TaskCandidate]) -> str:
    """Format tasks as JSON."""
    task_dicts = [task.to_dict() for task in tasks]
    return json.dumps(task_dicts, indent=2)


def _format_csv(tasks: List[TaskCandidate]) -> str:
    """Format tasks as CSV."""
    if not tasks:
        return ""
    
    # Header
    headers = [
        "Category", "Title", "Owner", "Status", "Urgency",
        "Next Follow-up", "Risks", "Description", "Deadline"
    ]
    lines = [",".join(headers)]
    
    # Tasks
    for task in tasks:
        row = [
            task.category,
            _escape_csv(task.title),
            _escape_csv(task.owner),
            task.status,
            task.urgency,
            _escape_csv(task.next_follow_up),
            _escape_csv(task.risks),
            _escape_csv(task.description or ""),
            task.deadline or ""
        ]
        lines.append(",".join(row))
    
    return "\n".join(lines)


def _format_plain(tasks: List[TaskCandidate]) -> str:
    """Format tasks as plain text."""
    if not tasks:
        return "No tasks extracted."
    
    categorized = _group_by_category(tasks)
    
    lines = ["EXTRACTED TASK CANDIDATES", "=" * 50, ""]
    
    for category in ["Software", "Mechanical/Hardware", "Logistics", "Documentation", "Follow-ups"]:
        if category in categorized:
            lines.append(f"{category.upper()} TASKS")
            lines.append("-" * 50)
            
            for i, task in enumerate(categorized[category], 1):
                lines.append(f"\n{i}. {task.title}")
                lines.append(f"   Owner: {task.owner}")
                lines.append(f"   Status: {task.status}")
                lines.append(f"   Urgency: {task.urgency}")
                lines.append(f"   Next: {task.next_follow_up}")
                lines.append(f"   Risks: {task.risks}")
                if task.description:
                    lines.append(f"   Details: {task.description}")
            
            lines.append("")
    
    return "\n".join(lines)


def _group_by_category(tasks: List[TaskCandidate]) -> Dict[str, List[TaskCandidate]]:
    """Group tasks by category."""
    categorized = defaultdict(list)
    for task in tasks:
        categorized[task.category].append(task)
    return dict(categorized)


def _escape_csv(text: str) -> str:
    """Escape text for CSV format."""
    if not text:
        return ""
    # Quote if contains comma, newline, or quote
    if any(char in text for char in [',', '\n', '"']):
        text = text.replace('"', '""')
        return f'"{text}"'
    return text


def generate_summary(tasks: List[TaskCandidate]) -> str:
    """Generate a summary of extracted tasks."""
    if not tasks:
        return "No tasks extracted."
    
    categorized = _group_by_category(tasks)
    
    lines = ["## Task Extraction Summary", ""]
    lines.append(f"**Total Tasks**: {len(tasks)}")
    lines.append("")
    lines.append("### By Category:")
    for category in ["Software", "Mechanical/Hardware", "Logistics", "Documentation", "Follow-ups"]:
        count = len(categorized.get(category, []))
        if count > 0:
            lines.append(f"- {category}: {count} task(s)")
    
    lines.append("")
    lines.append("### By Urgency:")
    urgency_counts = defaultdict(int)
    for task in tasks:
        urgency_counts[task.urgency] += 1
    for urgency in ["High", "Medium", "Low"]:
        count = urgency_counts[urgency]
        if count > 0:
            lines.append(f"- {urgency}: {count} task(s)")
    
    lines.append("")
    lines.append("### By Status:")
    status_counts = defaultdict(int)
    for task in tasks:
        status_counts[task.status] += 1
    for status, count in status_counts.items():
        lines.append(f"- {status}: {count} task(s)")
    
    # Sensitive info warning
    sensitive_count = sum(1 for task in tasks if task.sensitive_info_scrubbed)
    if sensitive_count > 0:
        lines.append("")
        lines.append(f"⚠️ **{sensitive_count} task(s) had sensitive information scrubbed**")
    
    return "\n".join(lines)
