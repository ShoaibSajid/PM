"""Task Candidate data model for the PM system."""

from dataclasses import dataclass, field
from typing import Optional, List
from datetime import datetime


@dataclass
class TaskCandidate:
    """Represents a task candidate extracted from messy inputs."""
    
    title: str
    """Copy-paste ready task title with imperative verb, single objective."""
    
    owner: str
    """Task owner. Append ' (Assumed)' if inferred rather than explicit."""
    
    status: str
    """One of: Not started, In progress, Blocked, Waiting on X, Needs clarification"""
    
    urgency: str
    """One of: High, Medium, Low"""
    
    next_follow_up: str
    """What to ask or check next, with explicit KST date if applicable."""
    
    risks: str
    """Dependencies, safety concerns, schedule risks, or system instability warnings."""
    
    category: str
    """One of: Software, Mechanical/Hardware, Logistics, Documentation, Follow-ups"""
    
    description: Optional[str] = ""
    """Additional context or details about the task."""
    
    dependencies: List[str] = field(default_factory=list)
    """List of blocking dependencies."""
    
    deadline: Optional[str] = None
    """Explicit deadline in KST, mark as 'Assumed' if inferred."""
    
    source: Optional[str] = None
    """Reference to source material (chat, email, etc.)."""
    
    extracted_at: datetime = field(default_factory=datetime.now)
    """When this task was extracted."""
    
    confidence: str = "High"
    """Extraction confidence: High, Medium, Low"""
    
    sensitive_info_scrubbed: bool = False
    """Whether sensitive information was found and scrubbed."""
    
    def __post_init__(self):
        """Validate task fields."""
        valid_statuses = [
            "Not started", "In progress", "Blocked", 
            "Waiting on X", "Needs clarification"
        ]
        valid_urgencies = ["High", "Medium", "Low"]
        valid_categories = [
            "Software", "Mechanical/Hardware", "Logistics",
            "Documentation", "Follow-ups"
        ]
        
        if self.status not in valid_statuses and not self.status.startswith("Waiting on "):
            raise ValueError(f"Invalid status: {self.status}")
        
        if self.urgency not in valid_urgencies:
            raise ValueError(f"Invalid urgency: {self.urgency}")
        
        if self.category not in valid_categories:
            raise ValueError(f"Invalid category: {self.category}")
    
    def to_markdown(self) -> str:
        """Format task as Asana-ready markdown."""
        lines = [
            f"### Task: {self.title}",
            f"- **Owner**: {self.owner}",
            f"- **Status**: {self.status}",
            f"- **Urgency**: {self.urgency}",
            f"- **Next follow-up**: {self.next_follow_up}",
            f"- **Risks**: {self.risks}",
        ]
        
        if self.description:
            lines.append(f"- **Description**: {self.description}")
        
        if self.dependencies:
            deps = ", ".join(self.dependencies)
            lines.append(f"- **Dependencies**: {deps}")
        
        if self.deadline:
            lines.append(f"- **Deadline**: {self.deadline}")
        
        if self.sensitive_info_scrubbed:
            lines.append(f"- **Note**: Sensitive information was scrubbed from this task")
        
        return "\n".join(lines)
    
    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "title": self.title,
            "owner": self.owner,
            "status": self.status,
            "urgency": self.urgency,
            "next_follow_up": self.next_follow_up,
            "risks": self.risks,
            "category": self.category,
            "description": self.description,
            "dependencies": self.dependencies,
            "deadline": self.deadline,
            "source": self.source,
            "extracted_at": self.extracted_at.isoformat(),
            "confidence": self.confidence,
            "sensitive_info_scrubbed": self.sensitive_info_scrubbed,
        }
