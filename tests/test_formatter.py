"""
Tests for the Asana formatter.
"""
import pytest
from datetime import datetime
import pytz

from schemas.task_model import (
    TaskSummary,
    TaskCandidate,
    TaskCategory,
    TaskStatus,
    TaskUrgency,
)
from src.formatter import AsanaFormatter


class TestAsanaFormatter:
    """Test cases for AsanaFormatter."""
    
    def test_format_single_task(self):
        """Test formatting a single task."""
        formatter = AsanaFormatter()
        
        task = TaskCandidate(
            title="Fix API bug",
            category=TaskCategory.SOFTWARE,
            owner="John",
            status=TaskStatus.IN_PROGRESS,
            urgency=TaskUrgency.HIGH,
            next_followup="Check progress with John",
        )
        
        summary = TaskSummary(tasks=[task])
        output = formatter.format_summary(summary)
        
        assert "Fix API bug" in output
        assert "John" in output
        assert "Software" in output
        assert "High" in output
    
    def test_format_multiple_categories(self):
        """Test formatting tasks in multiple categories."""
        formatter = AsanaFormatter()
        
        tasks = [
            TaskCandidate(
                title="Fix bug",
                category=TaskCategory.SOFTWARE,
                owner="Alice",
                status=TaskStatus.NOT_STARTED,
                urgency=TaskUrgency.MEDIUM,
                next_followup="Assign and start",
            ),
            TaskCandidate(
                title="Order parts",
                category=TaskCategory.LOGISTICS,
                owner="Bob",
                status=TaskStatus.IN_PROGRESS,
                urgency=TaskUrgency.LOW,
                next_followup="Track shipment",
            ),
        ]
        
        summary = TaskSummary(tasks=tasks)
        output = formatter.format_summary(summary)
        
        assert "Software" in output
        assert "Logistics" in output
        assert "Fix bug" in output
        assert "Order parts" in output
    
    def test_format_with_warnings(self):
        """Test formatting with warnings."""
        formatter = AsanaFormatter()
        
        summary = TaskSummary(
            tasks=[],
            warnings=["Sensitive data detected and removed"]
        )
        
        output = formatter.format_summary(summary)
        
        assert "Warnings" in output or "warning" in output.lower()
        assert "Sensitive" in output
    
    def test_format_high_urgency_callout(self):
        """Test that high urgency tasks are called out."""
        formatter = AsanaFormatter()
        
        task = TaskCandidate(
            title="Critical fix",
            category=TaskCategory.SOFTWARE,
            owner="Alice",
            status=TaskStatus.BLOCKED,
            urgency=TaskUrgency.HIGH,
            next_followup="Unblock immediately",
        )
        
        summary = TaskSummary(tasks=[task])
        output = formatter.format_summary(summary)
        
        # Should have a high urgency section
        assert "High Urgency" in output or "🔥" in output
    
    def test_format_compact_summary(self):
        """Test compact format."""
        formatter = AsanaFormatter()
        
        tasks = [
            TaskCandidate(
                title="Task 1",
                category=TaskCategory.SOFTWARE,
                owner="Alice",
                status=TaskStatus.NOT_STARTED,
                urgency=TaskUrgency.HIGH,
                next_followup="Start",
            ),
            TaskCandidate(
                title="Task 2",
                category=TaskCategory.SOFTWARE,
                owner="Bob",
                status=TaskStatus.IN_PROGRESS,
                urgency=TaskUrgency.MEDIUM,
                next_followup="Continue",
            ),
        ]
        
        summary = TaskSummary(tasks=tasks)
        output = formatter.format_compact_summary(summary)
        
        assert "2 tasks" in output.lower()
        assert "Software" in output
    
    def test_format_task_with_risks(self):
        """Test formatting task with risks."""
        formatter = AsanaFormatter()
        
        task = TaskCandidate(
            title="Deploy update",
            category=TaskCategory.SOFTWARE,
            owner="Alice",
            status=TaskStatus.NOT_STARTED,
            urgency=TaskUrgency.HIGH,
            next_followup="Review risks",
            risks=["Potential system instability", "Database migration required"],
        )
        
        summary = TaskSummary(tasks=[task])
        output = formatter.format_summary(summary)
        
        assert "Risks" in output or "⚠️" in output
        assert "system instability" in output
    
    def test_format_assumed_owner(self):
        """Test formatting task with assumed owner."""
        formatter = AsanaFormatter()
        
        task = TaskCandidate(
            title="Update docs",
            category=TaskCategory.DOCUMENTATION,
            owner="TBD",
            owner_assumed=True,
            status=TaskStatus.NOT_STARTED,
            urgency=TaskUrgency.LOW,
            next_followup="Assign owner",
        )
        
        summary = TaskSummary(tasks=[task])
        output = formatter.format_summary(summary)
        
        assert "Assumed" in output
    
    def test_format_with_deadline(self):
        """Test formatting task with deadline."""
        formatter = AsanaFormatter()
        
        deadline = datetime(2026, 1, 20, 17, 0, tzinfo=pytz.timezone('Asia/Seoul'))
        
        task = TaskCandidate(
            title="Complete report",
            category=TaskCategory.DOCUMENTATION,
            owner="Alice",
            status=TaskStatus.IN_PROGRESS,
            urgency=TaskUrgency.MEDIUM,
            next_followup="Review draft",
            deadline=deadline,
        )
        
        summary = TaskSummary(tasks=[task])
        output = formatter.format_summary(summary)
        
        assert "Deadline" in output
        assert "2026-01-20" in output
