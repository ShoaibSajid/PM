"""
Task parser for extracting task candidates from messy inputs.
"""
import re
from typing import List, Optional
from datetime import datetime, timedelta
import pytz
from dateutil import parser as date_parser

from schemas.task_model import (
    TaskCandidate,
    TaskCategory,
    TaskStatus,
    TaskUrgency,
    TaskSummary,
)
from src.sensitivity import SensitivityScrubber


class TaskParser:
    """
    Parses messy inputs (chat transcripts, emails, notes) into structured task candidates.
    """
    
    # Keywords for detecting task categories
    CATEGORY_KEYWORDS = {
        TaskCategory.SOFTWARE: ['code', 'software', 'bug', 'deploy', 'api', 'database', 'server', 'app', 'system', 'script'],
        TaskCategory.MECHANICAL_HARDWARE: ['hardware', 'mechanical', 'circuit', 'board', 'sensor', 'motor', 'physical', 'assembly'],
        TaskCategory.LOGISTICS: ['order', 'ship', 'deliver', 'procurement', 'vendor', 'purchase', 'supply'],
        TaskCategory.DOCUMENTATION: ['document', 'manual', 'guide', 'spec', 'readme', 'wiki', 'write up'],
        TaskCategory.FOLLOWUPS: ['follow up', 'check in', 'verify', 'confirm', 'review', 'meet'],
    }
    
    # Keywords for detecting status
    STATUS_KEYWORDS = {
        TaskStatus.BLOCKED: ['blocked', 'stuck', 'cannot proceed', 'waiting for'],
        TaskStatus.IN_PROGRESS: ['working on', 'in progress', 'currently', 'ongoing'],
        TaskStatus.NEEDS_CLARIFICATION: ['unclear', 'need clarification', 'not sure', 'question'],
    }
    
    # Keywords for detecting urgency
    URGENCY_KEYWORDS = {
        TaskUrgency.HIGH: ['urgent', 'asap', 'critical', 'immediately', 'emergency', 'high priority'],
        TaskUrgency.LOW: ['low priority', 'whenever', 'eventually', 'nice to have'],
    }
    
    # Risk keywords
    RISK_KEYWORDS = ['risk', 'danger', 'unsafe', 'safety', 'delay', 'late', 'overrun', 'unstable', 'breaking']
    
    def __init__(self, timezone: str = "Asia/Seoul"):
        """
        Initialize the parser.
        
        Args:
            timezone: Timezone for date interpretation (default: Asia/Seoul)
        """
        self.timezone = pytz.timezone(timezone)
        self.scrubber = SensitivityScrubber()
    
    def parse(self, text: str, source: Optional[str] = None) -> TaskSummary:
        """
        Parse text input into a task summary.
        
        Args:
            text: Input text (chat transcript, email, notes)
            source: Source description (e.g., "email from John", "Slack transcript")
            
        Returns:
            TaskSummary with extracted tasks
        """
        # Scrub sensitive data first
        scrubbed_text, warnings = self.scrubber.scrub(text)
        
        # Extract tasks from text
        tasks = self._extract_tasks(scrubbed_text, source)
        
        # Create summary
        summary = TaskSummary(
            extraction_date=datetime.now(self.timezone),
            timezone=str(self.timezone),
            tasks=tasks,
            warnings=warnings,
        )
        
        return summary
    
    def _extract_tasks(self, text: str, source: Optional[str]) -> List[TaskCandidate]:
        """
        Extract task candidates from text.
        
        This is a basic implementation that looks for action items.
        Can be enhanced with NLP or more sophisticated parsing.
        """
        tasks = []
        
        # Split text into lines and look for task-like patterns
        lines = text.strip().split('\n')
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Look for common task patterns
            # - [ ] Task
            # - Task
            # TODO: Task
            # Action: Task
            task_match = re.match(r'^[-*•]\s*(?:\[[ x]\]\s*)?(.+)$', line, re.IGNORECASE)
            if not task_match:
                task_match = re.match(r'^(?:TODO|Action|Task)[:\s]+(.+)$', line, re.IGNORECASE)
            
            if task_match:
                task_text = task_match.group(1).strip()
                task = self._parse_task_line(task_text, source)
                if task:
                    tasks.append(task)
        
        # If no explicit tasks found, check if the whole text looks like a single task
        if not tasks and len(lines) <= 3:
            # Might be a single task description
            task = self._parse_task_line(text.strip(), source)
            if task:
                tasks.append(task)
        
        return tasks
    
    def _parse_task_line(self, text: str, source: Optional[str]) -> Optional[TaskCandidate]:
        """
        Parse a single line into a task candidate.
        """
        if len(text) < 5:  # Too short to be meaningful
            return None
        
        # Filter out lines that are just metadata or credentials (after scrubbing)
        # These lines typically don't contain verbs or action words
        if re.match(r'^(?:Server|IP|API Key|Token|Password|Username|Port|Host|Production|Staging|Database|Credentials?)[:\s]', text, re.IGNORECASE):
            return None
        
        # Filter out lines that are just placeholder text from scrubbing
        if text.strip() in ['(IP omitted)', '(token omitted)', '(GitHub token omitted)', 
                            '(password omitted)', '(credentials omitted)']:
            return None
        
        # Filter out section headers (lines ending with colon and short)
        if re.match(r'^[A-Za-z\s]+:$', text) and len(text) < 30:
            return None
        
        # Filter out lines that are primarily about configuration/credentials
        # Look for patterns like "X: value" or "X is: value" where X is a config term
        if re.match(r'^(?:Config|Setting|Parameter|Variable|Value|Key|Secret)[:\s]', text, re.IGNORECASE):
            return None
        
        # Extract owner if mentioned
        owner, owner_assumed = self._extract_owner(text)
        
        # Detect category
        category = self._detect_category(text)
        
        # Detect status
        status, status_detail = self._detect_status(text)
        
        # Detect urgency
        urgency = self._detect_urgency(text)
        
        # Extract risks
        risks = self._extract_risks(text)
        
        # Extract deadline
        deadline, deadline_assumed = self._extract_deadline(text)
        
        # Generate title (clean up the text)
        title = self._generate_title(text)
        
        # Generate next follow-up
        next_followup = self._generate_followup(text, owner, status)
        
        task = TaskCandidate(
            title=title,
            category=category,
            owner=owner,
            owner_assumed=owner_assumed,
            status=status,
            status_detail=status_detail,
            urgency=urgency,
            next_followup=next_followup,
            risks=risks,
            deadline=deadline,
            deadline_assumed=deadline_assumed,
            source=source,
            notes=text if len(text) > len(title) + 20 else None,
        )
        
        return task
    
    def _extract_owner(self, text: str) -> tuple[str, bool]:
        """Extract task owner from text."""
        # Look for patterns like "Owner: John", "@john", "assigned to john"
        owner_match = re.search(r'(?:owner|assigned to|@)[\s:]*([A-Za-z]+)', text, re.IGNORECASE)
        if owner_match:
            return owner_match.group(1).capitalize(), False
        
        # Default assumption
        return "Unassigned", True
    
    def _detect_category(self, text: str) -> TaskCategory:
        """Detect task category from keywords."""
        text_lower = text.lower()
        
        scores = {}
        for category, keywords in self.CATEGORY_KEYWORDS.items():
            score = sum(1 for kw in keywords if kw in text_lower)
            if score > 0:
                scores[category] = score
        
        if scores:
            return max(scores, key=scores.get)
        
        # Default to Follow-ups if unclear
        return TaskCategory.FOLLOWUPS
    
    def _detect_status(self, text: str) -> tuple[TaskStatus, Optional[str]]:
        """Detect task status from keywords."""
        text_lower = text.lower()
        
        for status, keywords in self.STATUS_KEYWORDS.items():
            for keyword in keywords:
                if keyword in text_lower:
                    # Extract additional context for "waiting on"
                    if status == TaskStatus.BLOCKED:
                        match = re.search(r'waiting (?:for|on)\s+([A-Za-z\s]+)', text_lower)
                        if match:
                            return TaskStatus.WAITING_ON, f"Waiting on {match.group(1).strip().title()}"
                    return status, None
        
        # Default status
        return TaskStatus.NOT_STARTED, None
    
    def _detect_urgency(self, text: str) -> TaskUrgency:
        """Detect task urgency from keywords."""
        text_lower = text.lower()
        
        for urgency, keywords in self.URGENCY_KEYWORDS.items():
            if any(kw in text_lower for kw in keywords):
                return urgency
        
        # Default to medium
        return TaskUrgency.MEDIUM
    
    def _extract_risks(self, text: str) -> List[str]:
        """Extract risk signals from text."""
        risks = []
        text_lower = text.lower()
        
        for keyword in self.RISK_KEYWORDS:
            if keyword in text_lower:
                # Extract sentence containing the risk keyword
                sentences = re.split(r'[.!?]', text)
                for sentence in sentences:
                    if keyword in sentence.lower():
                        risks.append(sentence.strip())
                        break
        
        return risks
    
    def _extract_deadline(self, text: str) -> tuple[Optional[datetime], bool]:
        """Extract deadline from text."""
        # Look for date patterns
        deadline_match = re.search(
            r'(?:by|due|deadline|before)\s+([A-Za-z]+\s+\d{1,2}|\d{1,2}[/-]\d{1,2}(?:[/-]\d{2,4})?|today|tomorrow|next week)',
            text,
            re.IGNORECASE
        )
        
        if deadline_match:
            date_str = deadline_match.group(1).strip()
            try:
                # Handle relative dates
                now = datetime.now(self.timezone)
                if date_str.lower() == 'today':
                    return now.replace(hour=17, minute=0, second=0, microsecond=0), False
                elif date_str.lower() == 'tomorrow':
                    return (now + timedelta(days=1)).replace(hour=17, minute=0, second=0, microsecond=0), False
                elif date_str.lower() == 'next week':
                    return (now + timedelta(days=7)).replace(hour=17, minute=0, second=0, microsecond=0), False
                else:
                    # Try to parse as date
                    parsed_date = date_parser.parse(date_str, fuzzy=True)
                    # Localize to timezone
                    if parsed_date.tzinfo is None:
                        parsed_date = self.timezone.localize(parsed_date)
                    return parsed_date, False
            except:
                pass
        
        return None, False
    
    def _generate_title(self, text: str) -> str:
        """Generate a clean, copy-paste ready title."""
        # Remove owner mentions, status keywords, etc.
        title = re.sub(r'(?:owner|assigned to|@)[\s:]*[A-Za-z]+', '', text, flags=re.IGNORECASE)
        title = re.sub(r'(?:by|due|deadline)\s+[A-Za-z0-9\s/-]+', '', title, flags=re.IGNORECASE)
        title = re.sub(r'\s+', ' ', title).strip()
        
        # Ensure it starts with an imperative verb if possible
        # If it doesn't, prepend a reasonable verb
        common_starts = ['check', 'review', 'update', 'fix', 'create', 'implement', 'test', 'verify']
        if not any(title.lower().startswith(verb) for verb in common_starts):
            # Keep as is, might already be good
            pass
        
        # Capitalize first letter
        if title:
            title = title[0].upper() + title[1:]
        
        # Limit length
        if len(title) > 100:
            title = title[:97] + "..."
        
        return title
    
    def _generate_followup(self, text: str, owner: str, status: TaskStatus) -> str:
        """Generate a suggested follow-up action."""
        if status == TaskStatus.BLOCKED or status == TaskStatus.WAITING_ON:
            return f"Check with dependencies or {owner} on blockers"
        elif status == TaskStatus.NEEDS_CLARIFICATION:
            return "Clarify requirements and scope with stakeholders"
        elif owner == "Unassigned":
            return "Assign owner and confirm scope"
        else:
            return f"Check progress with {owner}"
