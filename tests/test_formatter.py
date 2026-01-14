"""Tests for output formatting."""

import sys
from pathlib import Path
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.formatter import format_tasks_for_asana, generate_summary, _group_by_category
from schemas.task_candidate import TaskCandidate
from src.date_utils import KST


def create_sample_task():
    """Create a sample task for testing."""
    return TaskCandidate(
        title="Test firmware v2.3",
        owner="John",
        status="Not started",
        urgency="High",
        next_follow_up="Check by 2026-01-15 (KST)",
        risks="System instability",
        category="Software",
        description="Test before deployment",
        extracted_at=datetime(2026, 1, 14, 12, 0, tzinfo=KST)
    )


def test_markdown_formatting():
    """Test markdown output formatting."""
    task = create_sample_task()
    output = format_tasks_for_asana([task], "markdown")
    
    assert "Software Tasks" in output
    assert "Test firmware v2.3" in output
    assert "John" in output
    assert "High" in output


def test_json_formatting():
    """Test JSON output formatting."""
    task = create_sample_task()
    output = format_tasks_for_asana([task], "json")
    
    assert '"title"' in output
    assert '"owner"' in output
    assert '"urgency"' in output


def test_csv_formatting():
    """Test CSV output formatting."""
    task = create_sample_task()
    output = format_tasks_for_asana([task], "csv")
    
    assert "Category" in output
    assert "Title" in output
    assert "Software" in output


def test_plain_formatting():
    """Test plain text formatting."""
    task = create_sample_task()
    output = format_tasks_for_asana([task], "plain")
    
    assert "SOFTWARE TASKS" in output
    assert "Test firmware v2.3" in output


def test_group_by_category():
    """Test grouping tasks by category."""
    task1 = create_sample_task()
    
    task2 = TaskCandidate(
        title="Order parts",
        owner="Lisa",
        status="Not started",
        urgency="Medium",
        next_follow_up="Check by 2026-01-15",
        risks="None",
        category="Logistics"
    )
    
    grouped = _group_by_category([task1, task2])
    
    assert "Software" in grouped
    assert "Logistics" in grouped
    assert len(grouped["Software"]) == 1
    assert len(grouped["Logistics"]) == 1


def test_summary_generation():
    """Test summary generation."""
    task = create_sample_task()
    summary = generate_summary([task])
    
    assert "Total Tasks" in summary
    assert "By Category" in summary
    assert "By Urgency" in summary


def test_empty_tasks():
    """Test formatting with no tasks."""
    output = format_tasks_for_asana([], "markdown")
    assert "No tasks extracted" in output


if __name__ == "__main__":
    test_markdown_formatting()
    test_json_formatting()
    test_csv_formatting()
    test_plain_formatting()
    test_group_by_category()
    test_summary_generation()
    test_empty_tasks()
    
    print("All formatter tests passed!")
