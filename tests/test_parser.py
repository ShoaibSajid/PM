"""Tests for task extraction parser."""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.parser import TaskExtractor
from schemas.task_candidate import TaskCandidate


def test_basic_extraction():
    """Test basic task extraction from simple text."""
    extractor = TaskExtractor()
    
    text = "John needs to test the firmware by tomorrow. This is urgent."
    
    tasks = extractor.parse(text)
    
    assert len(tasks) > 0
    task = tasks[0]
    assert isinstance(task, TaskCandidate)
    assert "test" in task.title.lower() or "firmware" in task.title.lower()
    assert task.urgency == "High"  # "urgent" should trigger high urgency


def test_owner_extraction():
    """Test owner identification."""
    extractor = TaskExtractor()
    
    text = "Sarah will update the documentation."
    tasks = extractor.parse(text)
    
    assert len(tasks) > 0
    task = tasks[0]
    assert "Sarah" in task.owner


def test_status_detection():
    """Test status detection from text."""
    extractor = TaskExtractor()
    
    # Blocked status
    text1 = "We need to fix the bug but we're blocked by the dependency."
    tasks1 = extractor.parse(text1)
    assert len(tasks1) > 0
    assert tasks1[0].status == "Blocked"
    
    # Waiting status
    text2 = "John is waiting for approval to proceed."
    tasks2 = extractor.parse(text2)
    assert len(tasks2) > 0
    assert "Waiting" in tasks2[0].status


def test_categorization():
    """Test task categorization."""
    extractor = TaskExtractor()
    
    # Software task
    text1 = "Deploy the new API endpoint to production."
    tasks1 = extractor.parse(text1)
    assert len(tasks1) > 0
    assert tasks1[0].category == "Software"
    
    # Hardware task
    text2 = "Calibrate the pressure sensor on unit 5."
    tasks2 = extractor.parse(text2)
    assert len(tasks2) > 0
    assert tasks2[0].category == "Mechanical/Hardware"
    
    # Logistics task
    text3 = "Order replacement parts from the vendor."
    tasks3 = extractor.parse(text3)
    assert len(tasks3) > 0
    assert tasks3[0].category == "Logistics"


def test_urgency_detection():
    """Test urgency level detection."""
    extractor = TaskExtractor()
    
    # High urgency
    text1 = "This is urgent - fix the critical bug immediately."
    tasks1 = extractor.parse(text1)
    assert len(tasks1) > 0
    assert tasks1[0].urgency == "High"
    
    # Low urgency
    text2 = "Update the documentation when you have time."
    tasks2 = extractor.parse(text2)
    # May extract task or not depending on action keywords
    # If extracted, should not be high priority


def test_multiple_tasks():
    """Test extraction of multiple tasks from one text."""
    extractor = TaskExtractor()
    
    text = """
    We need to:
    1. Test the firmware
    2. Update the documentation
    3. Order new components
    """
    
    tasks = extractor.parse(text)
    
    # Should extract at least 2 tasks
    assert len(tasks) >= 2


def test_empty_input():
    """Test handling of empty input."""
    extractor = TaskExtractor()
    
    tasks = extractor.parse("")
    assert len(tasks) == 0
    
    tasks = extractor.parse("   ")
    assert len(tasks) == 0


def test_no_actionable_content():
    """Test text with no actionable items."""
    extractor = TaskExtractor()
    
    text = "The weather is nice today. We had a good meeting."
    tasks = extractor.parse(text)
    
    # Should not extract tasks from non-actionable text
    assert len(tasks) == 0


if __name__ == "__main__":
    # Run tests
    test_basic_extraction()
    test_owner_extraction()
    test_status_detection()
    test_categorization()
    test_urgency_detection()
    test_multiple_tasks()
    test_empty_input()
    test_no_actionable_content()
    
    print("All tests passed!")
