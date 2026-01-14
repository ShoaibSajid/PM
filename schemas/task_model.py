"""
Task candidate data models for the PM Assistant.
"""
from enum import Enum
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field


class TaskCategory(str, Enum):
    """Task category classification."""
    SOFTWARE = "Software"
    MECHANICAL_HARDWARE = "Mechanical/Hardware"
    LOGISTICS = "Logistics"
    DOCUMENTATION = "Documentation"
    FOLLOWUPS = "Follow-ups"


class TaskStatus(str, Enum):
    """Task status."""
    NOT_STARTED = "Not started"
    IN_PROGRESS = "In progress"
    BLOCKED = "Blocked"
    WAITING_ON = "Waiting on"
    NEEDS_CLARIFICATION = "Needs clarification"


class TaskUrgency(str, Enum):
    """Task urgency level."""
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class TaskCandidate(BaseModel):
    """
    A task candidate extracted from messy inputs.
    Ready to be copied into Asana by the project owner.
    """
    title: str = Field(..., description="Copy-paste ready title with imperative verb")
    category: TaskCategory = Field(..., description="Task category")
    owner: str = Field(..., description="Task owner (explicit or assumed)")
    owner_assumed: bool = Field(default=False, description="Whether owner was inferred")
    status: TaskStatus = Field(..., description="Current task status")
    status_detail: Optional[str] = Field(None, description="Additional status context (e.g., 'Waiting on John')")
    urgency: TaskUrgency = Field(..., description="Task urgency")
    next_followup: str = Field(..., description="What to ask/check next")
    risks: List[str] = Field(default_factory=list, description="Risks and escalation signals")
    deadline: Optional[datetime] = Field(None, description="Task deadline if mentioned")
    deadline_assumed: bool = Field(default=False, description="Whether deadline was inferred")
    dependencies: List[str] = Field(default_factory=list, description="Task dependencies")
    notes: Optional[str] = Field(None, description="Additional context or notes")
    source: Optional[str] = Field(None, description="Source of the task (e.g., email, chat)")

    class Config:
        use_enum_values = True


class TaskSummary(BaseModel):
    """
    Summary of extracted tasks grouped by category.
    """
    extraction_date: datetime = Field(default_factory=datetime.utcnow)
    timezone: str = Field(default="Asia/Seoul")
    tasks: List[TaskCandidate] = Field(default_factory=list)
    warnings: List[str] = Field(default_factory=list, description="Warnings about missing or sensitive info")
    
    def get_tasks_by_category(self, category: TaskCategory) -> List[TaskCandidate]:
        """Get all tasks for a specific category."""
        return [t for t in self.tasks if t.category == category]
    
    def has_high_urgency_tasks(self) -> bool:
        """Check if there are any high urgency tasks."""
        return any(t.urgency == TaskUrgency.HIGH for t in self.tasks)
