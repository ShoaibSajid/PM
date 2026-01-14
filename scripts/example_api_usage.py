#!/usr/bin/env python3
"""
Example script demonstrating the PM Assistant Python API.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.parser import TaskParser
from src.formatter import AsanaFormatter
from schemas.task_model import TaskCategory

# Example input text
sample_input = """
Meeting Notes - Weekly Standup

Software Tasks:
- Fix authentication bug in API @john (URGENT)
- Deploy new version to production by tomorrow
- Code review PR #456

Hardware:
- Replace faulty sensor on line 2 (safety risk)
- Order 10 replacement motors from vendor

Documentation:
- Update API documentation with new endpoints

Blockers:
- Cannot test integration until database is migrated
- Waiting for approval from management on budget
"""

def main():
    print("=" * 70)
    print("PM Assistant - Python API Example")
    print("=" * 70)
    
    # Initialize parser and formatter
    parser = TaskParser(timezone="Asia/Seoul")
    formatter = AsanaFormatter()
    
    # Parse the input
    print("\n📥 Parsing input...")
    summary = parser.parse(sample_input, source="Weekly standup meeting")
    
    # Display stats
    print(f"\n✓ Extracted {len(summary.tasks)} task(s)")
    print(f"  - High urgency: {sum(1 for t in summary.tasks if t.urgency == 'High')}")
    print(f"  - Medium urgency: {sum(1 for t in summary.tasks if t.urgency == 'Medium')}")
    print(f"  - Low urgency: {sum(1 for t in summary.tasks if t.urgency == 'Low')}")
    
    if summary.warnings:
        print(f"\n⚠️  {len(summary.warnings)} warning(s):")
        for warning in summary.warnings:
            print(f"  - {warning}")
    
    # Show tasks by category
    print("\n📊 Tasks by Category:")
    for category in TaskCategory:
        tasks = summary.get_tasks_by_category(category)
        if tasks:
            print(f"  - {category.value}: {len(tasks)}")
    
    # Generate formatted output
    print("\n" + "=" * 70)
    print("Formatted Output (Asana-ready)")
    print("=" * 70 + "\n")
    
    markdown = formatter.format_summary(summary)
    print(markdown)
    
    # Show compact summary
    print("\n" + "=" * 70)
    print("Compact Summary")
    print("=" * 70 + "\n")
    
    compact = formatter.format_compact_summary(summary)
    print(compact)
    
    # Example: Filter and display high urgency tasks
    print("\n" + "=" * 70)
    print("High Urgency Tasks Only")
    print("=" * 70 + "\n")
    
    high_urgency = [t for t in summary.tasks if t.urgency == "High"]
    if high_urgency:
        for task in high_urgency:
            print(f"🔥 {task.title}")
            print(f"   Owner: {task.owner} {'(Assumed)' if task.owner_assumed else ''}")
            print(f"   Status: {task.status}")
            print(f"   Category: {task.category}")
            if task.risks:
                print(f"   ⚠️  Risks: {', '.join(task.risks)}")
            print()
    else:
        print("No high urgency tasks found.")
    
    print("=" * 70)
    print("✓ Example completed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
