"""
Tests for the task parser.
"""
import pytest
from src.parser import TaskParser
from schemas.task_model import TaskCategory, TaskStatus, TaskUrgency


class TestTaskParser:
    """Test cases for TaskParser."""
    
    def test_parse_simple_task(self):
        """Test parsing a simple task."""
        parser = TaskParser()
        
        text = "- Fix the API bug"
        summary = parser.parse(text)
        
        assert len(summary.tasks) == 1
        task = summary.tasks[0]
        assert "Fix" in task.title or "API" in task.title
    
    def test_parse_task_with_owner(self):
        """Test parsing task with owner."""
        parser = TaskParser()
        
        text = "- Update documentation @john"
        summary = parser.parse(text)
        
        assert len(summary.tasks) == 1
        task = summary.tasks[0]
        assert task.owner == "John"
        assert not task.owner_assumed
    
    def test_parse_task_without_owner(self):
        """Test parsing task without owner."""
        parser = TaskParser()
        
        text = "- Deploy new version"
        summary = parser.parse(text)
        
        assert len(summary.tasks) == 1
        task = summary.tasks[0]
        assert task.owner_assumed
    
    def test_detect_software_category(self):
        """Test detection of software category."""
        parser = TaskParser()
        
        text = "- Fix the database bug in the API"
        summary = parser.parse(text)
        
        assert len(summary.tasks) == 1
        assert summary.tasks[0].category == TaskCategory.SOFTWARE
    
    def test_detect_hardware_category(self):
        """Test detection of hardware category."""
        parser = TaskParser()
        
        text = "- Replace the broken sensor on the motor"
        summary = parser.parse(text)
        
        assert len(summary.tasks) == 1
        assert summary.tasks[0].category == TaskCategory.MECHANICAL_HARDWARE
    
    def test_detect_high_urgency(self):
        """Test detection of high urgency."""
        parser = TaskParser()
        
        text = "- URGENT: Fix production server issue"
        summary = parser.parse(text)
        
        assert len(summary.tasks) == 1
        assert summary.tasks[0].urgency == TaskUrgency.HIGH
    
    def test_detect_blocked_status(self):
        """Test detection of blocked status."""
        parser = TaskParser()
        
        text = "- Cannot proceed with deployment, blocked"
        summary = parser.parse(text)
        
        assert len(summary.tasks) == 1
        assert summary.tasks[0].status == TaskStatus.BLOCKED
    
    def test_detect_waiting_on_status(self):
        """Test detection of waiting on status."""
        parser = TaskParser()
        
        text = "- Update API documentation waiting for John"
        summary = parser.parse(text)
        
        assert len(summary.tasks) == 1
        task = summary.tasks[0]
        assert task.status == TaskStatus.WAITING_ON
        assert "John" in task.status_detail
    
    def test_parse_multiple_tasks(self):
        """Test parsing multiple tasks."""
        parser = TaskParser()
        
        text = """
- Fix bug in login
- Update documentation
- Order new sensors
"""
        summary = parser.parse(text)
        
        assert len(summary.tasks) == 3
    
    def test_extract_risks(self):
        """Test extraction of risk signals."""
        parser = TaskParser()
        
        text = "- Deploy update but there's a safety risk with the new code"
        summary = parser.parse(text)
        
        assert len(summary.tasks) == 1
        task = summary.tasks[0]
        assert len(task.risks) > 0
    
    def test_parse_with_deadline(self):
        """Test parsing task with deadline."""
        parser = TaskParser()
        
        text = "- Complete report by tomorrow"
        summary = parser.parse(text)
        
        assert len(summary.tasks) == 1
        task = summary.tasks[0]
        assert task.deadline is not None
    
    def test_scrub_sensitive_data(self):
        """Test that sensitive data is scrubbed during parsing."""
        parser = TaskParser()
        
        text = "- Update config with password: secret123"
        summary = parser.parse(text)
        
        # Check that warnings were generated
        assert len(summary.warnings) > 0
        
        # Verify task doesn't contain the password
        task = summary.tasks[0]
        assert "secret123" not in task.title
    
    def test_empty_input(self):
        """Test parsing empty input."""
        parser = TaskParser()
        
        text = ""
        summary = parser.parse(text)
        
        assert len(summary.tasks) == 0
    
    def test_todo_format(self):
        """Test parsing TODO format."""
        parser = TaskParser()
        
        text = "TODO: Implement new feature"
        summary = parser.parse(text)
        
        assert len(summary.tasks) == 1
        assert "feature" in summary.tasks[0].title.lower()
