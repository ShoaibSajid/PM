"""Task extraction parser for converting messy inputs to structured tasks."""

import re
from typing import List, Dict, Optional
from datetime import datetime

from schemas.task_candidate import TaskCandidate
from src.date_utils import parse_relative_date, get_current_kst, add_kst_marker
from src.sensitivity import scrub_sensitive_info


class TaskExtractor:
    """Extracts task candidates from unstructured text."""
    
    def __init__(self):
        """Initialize the task extractor."""
        self.current_kst = get_current_kst()
        self.tasks: List[TaskCandidate] = []
    
    def parse(self, text: str, source: Optional[str] = None) -> List[TaskCandidate]:
        """
        Parse unstructured text and extract task candidates.
        
        Args:
            text: Input text (chat transcript, email, notes, etc.)
            source: Optional source reference
        
        Returns:
            List of TaskCandidate objects
        """
        # Scrub sensitive information first
        scrubbed_text, was_scrubbed = scrub_sensitive_info(text)
        
        # Split into sections/messages
        sections = self._split_into_sections(scrubbed_text)
        
        tasks = []
        for section in sections:
            extracted_tasks = self._extract_tasks_from_section(section, source, was_scrubbed)
            tasks.extend(extracted_tasks)
        
        self.tasks = tasks
        return tasks
    
    def _split_into_sections(self, text: str) -> List[str]:
        """Split text into logical sections (messages, paragraphs, etc.)."""
        # Try to identify section boundaries
        # Common patterns: timestamps, usernames, blank lines
        
        # Split by double newlines (paragraphs)
        sections = re.split(r'\n\s*\n', text)
        
        # Further split by timestamps or user mentions if present
        refined_sections = []
        timestamp_pattern = r'\[\d{2}:\d{2}(?::\d{2})?\]|\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}'
        
        for section in sections:
            if re.search(timestamp_pattern, section):
                # Split by timestamps
                parts = re.split(f'({timestamp_pattern})', section)
                refined_sections.extend([p.strip() for p in parts if p.strip()])
            else:
                refined_sections.append(section.strip())
        
        return [s for s in refined_sections if s]
    
    def _extract_tasks_from_section(
        self, 
        text: str, 
        source: Optional[str],
        has_sensitive_info: bool
    ) -> List[TaskCandidate]:
        """Extract tasks from a single section of text."""
        tasks = []
        
        # Look for action keywords
        action_keywords = [
            'need to', 'needs to', 'must', 'should', 'have to',
            'todo', 'to-do', 'action item', 'task:',
            'please', 'can you', 'will you', 'could you',
            'implement', 'fix', 'update', 'create', 'test',
            'review', 'check', 'verify', 'deploy', 'configure'
        ]
        
        text_lower = text.lower()
        contains_action = any(keyword in text_lower for keyword in action_keywords)
        
        if not contains_action:
            return tasks
        
        # Extract task details
        task = self._parse_task_details(text, source, has_sensitive_info)
        if task:
            tasks.append(task)
        
        return tasks
    
    def _parse_task_details(
        self, 
        text: str, 
        source: Optional[str],
        has_sensitive_info: bool
    ) -> Optional[TaskCandidate]:
        """Parse task details from text."""
        
        # Extract title (first sentence or action phrase)
        title = self._extract_title(text)
        if not title:
            return None
        
        # Extract owner
        owner = self._extract_owner(text)
        
        # Determine status
        status = self._determine_status(text)
        
        # Determine urgency
        urgency = self._determine_urgency(text)
        
        # Extract or infer next follow-up
        next_follow_up = self._extract_next_followup(text)
        
        # Identify risks
        risks = self._identify_risks(text)
        
        # Categorize task
        category = self._categorize_task(text)
        
        # Extract description
        description = self._extract_description(text, title)
        
        # Extract dependencies
        dependencies = self._extract_dependencies(text)
        
        # Extract deadline
        deadline = self._extract_deadline(text)
        
        try:
            task = TaskCandidate(
                title=title,
                owner=owner,
                status=status,
                urgency=urgency,
                next_follow_up=next_follow_up,
                risks=risks,
                category=category,
                description=description,
                dependencies=dependencies,
                deadline=deadline,
                source=source,
                extracted_at=self.current_kst,
                sensitive_info_scrubbed=has_sensitive_info
            )
            return task
        except ValueError as e:
            # Invalid task fields, skip
            return None
    
    def _extract_title(self, text: str) -> Optional[str]:
        """Extract task title from text."""
        # Look for imperative verbs and create actionable title
        imperative_verbs = [
            'test', 'implement', 'fix', 'update', 'create', 'deploy',
            'configure', 'review', 'check', 'verify', 'install',
            'calibrate', 'order', 'ship', 'document', 'write'
        ]
        
        # Extract first sentence
        sentences = re.split(r'[.!?]\s+', text)
        if not sentences:
            return None
        
        first_sentence = sentences[0].strip()
        
        # Check if it starts with imperative verb
        words = first_sentence.lower().split()
        if words and words[0] in imperative_verbs:
            # Capitalize first letter
            title = first_sentence[0].upper() + first_sentence[1:]
            # Limit length
            if len(title) > 80:
                title = title[:77] + "..."
            return title
        
        # Try to find action phrase
        for verb in imperative_verbs:
            pattern = rf'\b{verb}\s+[^.!?]*'
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                title = match.group(0).strip()
                title = title[0].upper() + title[1:]
                if len(title) > 80:
                    title = title[:77] + "..."
                return title
        
        # Default: use first phrase
        if len(first_sentence) > 80:
            return first_sentence[:77] + "..."
        return first_sentence
    
    def _extract_owner(self, text: str) -> str:
        """Extract task owner from text."""
        # Look for name patterns
        # Common patterns: "@name", "assign to name", "name will", "name needs to"
        
        owner_patterns = [
            r'@(\w+)',
            r'assign(?:ed)?\s+to\s+(\w+(?:\s+\w+)?)',
            r'(\w+(?:\s+\w+)?)\s+will\s+',
            r'(\w+(?:\s+\w+)?)\s+needs?\s+to',
            r'(\w+(?:\s+\w+)?)\s+should',
            r'ask\s+(\w+(?:\s+\w+)?)',
        ]
        
        for pattern in owner_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                owner_name = match.group(1).strip()
                # Capitalize
                owner_name = ' '.join(word.capitalize() for word in owner_name.split())
                return owner_name
        
        # No explicit owner found
        return "Team Member (Assumed)"
    
    def _determine_status(self, text: str) -> str:
        """Determine task status from text."""
        text_lower = text.lower()
        
        # Check for explicit status indicators
        if any(word in text_lower for word in ['blocked', 'stuck', 'can\'t proceed']):
            return "Blocked"
        
        if any(word in text_lower for word in ['waiting', 'pending', 'need', 'needs']):
            # Check what they're waiting on
            if 'waiting for' in text_lower or 'waiting on' in text_lower:
                match = re.search(r'waiting (?:for|on)\s+(\w+(?:\s+\w+){0,3})', text_lower)
                if match:
                    return f"Waiting on {match.group(1)}"
            return "Waiting on X"
        
        if any(word in text_lower for word in ['unclear', 'not sure', 'clarify', 'clarification']):
            return "Needs clarification"
        
        if any(word in text_lower for word in ['working on', 'in progress', 'currently']):
            return "In progress"
        
        # Default
        return "Not started"
    
    def _determine_urgency(self, text: str) -> str:
        """Determine task urgency from text."""
        text_lower = text.lower()
        
        # High urgency indicators
        high_indicators = [
            'urgent', 'asap', 'critical', 'immediately', 'emergency',
            'high priority', 'blocker', 'must', 'deadline'
        ]
        if any(indicator in text_lower for indicator in high_indicators):
            return "High"
        
        # Low urgency indicators
        low_indicators = [
            'low priority', 'when possible', 'eventually', 'nice to have',
            'optional', 'if time permits'
        ]
        if any(indicator in text_lower for indicator in low_indicators):
            return "Low"
        
        # Default to medium
        return "Medium"
    
    def _extract_next_followup(self, text: str) -> str:
        """Extract or infer next follow-up action."""
        # Look for follow-up mentions
        followup_patterns = [
            r'follow[- ]up\s+(?:with|on)\s+([^.!?]+)',
            r'check\s+(?:with|on)\s+([^.!?]+)',
            r'confirm\s+([^.!?]+)',
            r'verify\s+([^.!?]+)',
        ]
        
        for pattern in followup_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                action = match.group(1).strip()
                # Add date
                date_str, is_assumed = parse_relative_date(text, self.current_kst)
                suffix = " (Assumed)" if is_assumed else ""
                return f"{action} by {date_str} (KST){suffix}"
        
        # Default follow-up
        date_str, _ = parse_relative_date("2 days", self.current_kst)
        return f"Check status by {date_str} (KST) (Assumed)"
    
    def _identify_risks(self, text: str) -> str:
        """Identify risks, dependencies, and concerns."""
        text_lower = text.lower()
        
        risks = []
        
        # Safety concerns
        if any(word in text_lower for word in ['safety', 'dangerous', 'hazard', 'risk']):
            risks.append("Safety concern")
        
        # Schedule risks
        if any(word in text_lower for word in ['delay', 'late', 'behind', 'schedule']):
            risks.append("Schedule risk")
        
        # Dependency risks
        if any(word in text_lower for word in ['depends on', 'blocked by', 'waiting', 'requires']):
            risks.append("Dependency exists")
        
        # System stability
        if any(word in text_lower for word in ['unstable', 'crash', 'bug', 'error', 'fail']):
            risks.append("System instability")
        
        # Integration risks
        if any(word in text_lower for word in ['integrate', 'compatibility', 'conflict']):
            risks.append("Integration complexity")
        
        if not risks:
            return "None identified"
        
        return "; ".join(risks)
    
    def _categorize_task(self, text: str) -> str:
        """Categorize task into one of the standard categories."""
        text_lower = text.lower()
        
        # Software keywords
        software_keywords = [
            'code', 'software', 'api', 'database', 'deploy', 'test',
            'bug', 'firmware', 'script', 'config', 'system', 'server'
        ]
        if any(keyword in text_lower for keyword in software_keywords):
            return "Software"
        
        # Mechanical/Hardware keywords
        hardware_keywords = [
            'hardware', 'mechanical', 'sensor', 'motor', 'calibrate',
            'assemble', 'wiring', 'circuit', 'component', 'unit', 'device'
        ]
        if any(keyword in text_lower for keyword in hardware_keywords):
            return "Mechanical/Hardware"
        
        # Logistics keywords
        logistics_keywords = [
            'order', 'ship', 'delivery', 'procurement', 'vendor',
            'schedule', 'coordinate', 'logistics', 'purchase', 'supplier'
        ]
        if any(keyword in text_lower for keyword in logistics_keywords):
            return "Logistics"
        
        # Documentation keywords
        doc_keywords = [
            'document', 'manual', 'report', 'specification', 'drawing',
            'write', 'documentation', 'notes', 'guide', 'procedure'
        ]
        if any(keyword in text_lower for keyword in doc_keywords):
            return "Documentation"
        
        # Follow-up keywords
        followup_keywords = [
            'follow up', 'check', 'confirm', 'verify', 'status',
            'update', 'clarify', 'ask', 'contact'
        ]
        if any(keyword in text_lower for keyword in followup_keywords):
            return "Follow-ups"
        
        # Default to Follow-ups for unclear tasks
        return "Follow-ups"
    
    def _extract_description(self, text: str, title: str) -> str:
        """Extract additional description beyond the title."""
        # Remove the title from text to get remainder
        description = text.replace(title, "", 1).strip()
        
        # Limit length
        if len(description) > 200:
            description = description[:197] + "..."
        
        return description
    
    def _extract_dependencies(self, text: str) -> List[str]:
        """Extract task dependencies."""
        dependencies = []
        
        patterns = [
            r'depends on\s+([^.!?]+)',
            r'blocked by\s+([^.!?]+)',
            r'requires\s+([^.!?]+)',
            r'needs\s+([^.!?]+)\s+(?:first|before)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                dep = match.group(1).strip()
                if len(dep) < 100:  # Reasonable length
                    dependencies.append(dep)
        
        return dependencies
    
    def _extract_deadline(self, text: str) -> Optional[str]:
        """Extract explicit deadline if mentioned."""
        # Look for deadline mentions
        deadline_patterns = [
            r'(?:by|before|due)\s+(\w+day|\d{4}-\d{2}-\d{2}|\w+\s+\d{1,2})',
            r'deadline[:\s]+([^.!?]+)',
        ]
        
        for pattern in deadline_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                date_text = match.group(1).strip()
                date_str, is_assumed = parse_relative_date(date_text, self.current_kst)
                suffix = " (Assumed)" if is_assumed else ""
                return f"{date_str} (KST){suffix}"
        
        return None
