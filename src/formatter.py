"""
Formatter for converting task summaries to Asana-friendly markdown.
"""
from typing import List
from datetime import datetime
from schemas.task_model import TaskSummary, TaskCandidate, TaskCategory


class AsanaFormatter:
    """
    Formats task summaries into copy-paste ready markdown for Asana.
    """
    
    def format_summary(self, summary: TaskSummary) -> str:
        """
        Format a task summary into markdown.
        
        Args:
            summary: TaskSummary to format
            
        Returns:
            Formatted markdown string
        """
        output = []
        
        # Header
        output.append("# Actionable Tasks Summary")
        output.append(f"\n**Extracted:** {summary.extraction_date.strftime('%Y-%m-%d %H:%M %Z')}")
        output.append(f"**Timezone:** {summary.timezone}\n")
        
        # Warnings
        if summary.warnings:
            output.append("## ⚠️ Warnings\n")
            for warning in summary.warnings:
                output.append(f"- {warning}")
            output.append("")
        
        # High urgency tasks callout
        if summary.has_high_urgency_tasks():
            output.append("## 🔥 High Urgency Tasks\n")
            high_urgency_tasks = [t for t in summary.tasks if t.urgency == "High"]
            for task in high_urgency_tasks:
                output.append(f"- **{task.title}** ({task.category}) - Owner: {task.owner}")
            output.append("")
        
        # Tasks by category
        output.append("## Tasks by Category\n")
        
        categories = [
            TaskCategory.SOFTWARE,
            TaskCategory.MECHANICAL_HARDWARE,
            TaskCategory.LOGISTICS,
            TaskCategory.DOCUMENTATION,
            TaskCategory.FOLLOWUPS,
        ]
        
        for category in categories:
            tasks = summary.get_tasks_by_category(category)
            if tasks:
                output.append(f"### {category.value}\n")
                for task in tasks:
                    output.append(self._format_task(task))
                output.append("")
        
        return "\n".join(output)
    
    def _format_task(self, task: TaskCandidate) -> str:
        """
        Format a single task into markdown.
        
        Args:
            task: TaskCandidate to format
            
        Returns:
            Formatted markdown string for the task
        """
        lines = []
        
        # Title with status indicator
        status_emoji = self._get_status_emoji(task.status)
        urgency_emoji = self._get_urgency_emoji(task.urgency)
        lines.append(f"**{status_emoji} {task.title}** {urgency_emoji}")
        
        # Owner
        owner_text = f"{task.owner} (Assumed)" if task.owner_assumed else task.owner
        lines.append(f"  - **Owner:** {owner_text}")
        
        # Status
        if task.status_detail:
            lines.append(f"  - **Status:** {task.status} - {task.status_detail}")
        else:
            lines.append(f"  - **Status:** {task.status}")
        
        # Urgency
        lines.append(f"  - **Urgency:** {task.urgency}")
        
        # Deadline
        if task.deadline:
            deadline_str = task.deadline.strftime('%Y-%m-%d %H:%M')
            if task.deadline_assumed:
                deadline_str += " (Assumed)"
            lines.append(f"  - **Deadline:** {deadline_str}")
        
        # Next follow-up
        lines.append(f"  - **Next Follow-up:** {task.next_followup}")
        
        # Risks
        if task.risks:
            lines.append(f"  - **⚠️ Risks:**")
            for risk in task.risks:
                lines.append(f"    - {risk}")
        
        # Dependencies
        if task.dependencies:
            lines.append(f"  - **Dependencies:** {', '.join(task.dependencies)}")
        
        # Source
        if task.source:
            lines.append(f"  - **Source:** {task.source}")
        
        lines.append("")  # Empty line between tasks
        
        return "\n".join(lines)
    
    def _get_status_emoji(self, status: str) -> str:
        """Get emoji for task status."""
        emoji_map = {
            "Not started": "⭕",
            "In progress": "🔄",
            "Blocked": "🚫",
            "Waiting on": "⏸️",
            "Needs clarification": "❓",
        }
        return emoji_map.get(status, "⭕")
    
    def _get_urgency_emoji(self, urgency: str) -> str:
        """Get emoji for task urgency."""
        emoji_map = {
            "High": "🔴",
            "Medium": "🟡",
            "Low": "🟢",
        }
        return emoji_map.get(urgency, "⚪")
    
    def format_compact_summary(self, summary: TaskSummary) -> str:
        """
        Format a compact version of the summary.
        Useful for quick reviews or Slack messages.
        
        Args:
            summary: TaskSummary to format
            
        Returns:
            Compact formatted string
        """
        output = []
        output.append(f"📋 **{len(summary.tasks)} tasks extracted** ({summary.extraction_date.strftime('%Y-%m-%d %H:%M')})\n")
        
        if summary.has_high_urgency_tasks():
            high_count = sum(1 for t in summary.tasks if t.urgency == "High")
            output.append(f"🔥 {high_count} high urgency task(s)\n")
        
        # Count by category
        for category in [TaskCategory.SOFTWARE, TaskCategory.MECHANICAL_HARDWARE, 
                        TaskCategory.LOGISTICS, TaskCategory.DOCUMENTATION, TaskCategory.FOLLOWUPS]:
            count = len(summary.get_tasks_by_category(category))
            if count > 0:
                output.append(f"- {category.value}: {count}")
        
        if summary.warnings:
            output.append(f"\n⚠️ {len(summary.warnings)} warning(s)")
        
        return "\n".join(output)
