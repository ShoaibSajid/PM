#!/usr/bin/env python3
"""
Command-line interface for PM Assistant.
Parse messy inputs into Asana-ready task lists.
"""
import sys
import argparse
from pathlib import Path

from src.parser import TaskParser
from src.formatter import AsanaFormatter


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="PM Assistant - Extract actionable tasks from messy inputs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Parse a text file
  pm-parse input.txt
  
  # Parse from stdin
  cat meeting_notes.txt | pm-parse -
  
  # Specify source and output file
  pm-parse transcript.txt --source "Team meeting" --output tasks.md
  
  # Compact output
  pm-parse notes.txt --compact
        """
    )
    
    parser.add_argument(
        'input',
        type=str,
        help='Input file path or "-" for stdin'
    )
    
    parser.add_argument(
        '--source',
        type=str,
        help='Source description (e.g., "email from John", "Slack #engineering")',
        default=None
    )
    
    parser.add_argument(
        '--output',
        '-o',
        type=str,
        help='Output file path (default: stdout)',
        default=None
    )
    
    parser.add_argument(
        '--compact',
        action='store_true',
        help='Use compact output format'
    )
    
    parser.add_argument(
        '--timezone',
        '-tz',
        type=str,
        help='Timezone for date interpretation (default: Asia/Seoul)',
        default='Asia/Seoul'
    )
    
    args = parser.parse_args()
    
    # Read input
    try:
        if args.input == '-':
            input_text = sys.stdin.read()
        else:
            input_path = Path(args.input)
            if not input_path.exists():
                print(f"Error: Input file '{args.input}' not found", file=sys.stderr)
                sys.exit(1)
            input_text = input_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading input: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Parse tasks
    try:
        task_parser = TaskParser(timezone=args.timezone)
        summary = task_parser.parse(input_text, source=args.source)
    except Exception as e:
        print(f"Error parsing tasks: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Format output
    try:
        formatter = AsanaFormatter()
        if args.compact:
            output_text = formatter.format_compact_summary(summary)
        else:
            output_text = formatter.format_summary(summary)
    except Exception as e:
        print(f"Error formatting output: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Write output
    try:
        if args.output:
            output_path = Path(args.output)
            output_path.write_text(output_text, encoding='utf-8')
            print(f"Tasks written to {args.output}", file=sys.stderr)
        else:
            print(output_text)
    except Exception as e:
        print(f"Error writing output: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Print summary to stderr
    task_count = len(summary.tasks)
    high_urgency_count = sum(1 for t in summary.tasks if t.urgency == "High")
    print(f"\n✓ Extracted {task_count} task(s)", file=sys.stderr)
    if high_urgency_count > 0:
        print(f"⚠ {high_urgency_count} high urgency task(s) found", file=sys.stderr)
    if summary.warnings:
        print(f"⚠ {len(summary.warnings)} warning(s)", file=sys.stderr)


if __name__ == '__main__':
    main()
