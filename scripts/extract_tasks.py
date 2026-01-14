#!/usr/bin/env python3
"""
CLI tool for extracting task candidates from messy inputs.

Usage:
    python extract_tasks.py --input file.txt
    python extract_tasks.py --input file.txt --output tasks.md
    python extract_tasks.py --input-dir ./inputs/ --output-dir ./outputs/
"""

import argparse
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.parser import TaskExtractor
from src.formatter import format_tasks_for_asana, generate_summary


def main():
    parser = argparse.ArgumentParser(
        description="Extract task candidates from messy inputs"
    )
    
    # Input options
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        "--input", "-i",
        type=str,
        help="Input file path"
    )
    input_group.add_argument(
        "--input-dir", "-d",
        type=str,
        help="Input directory for batch processing"
    )
    
    # Output options
    parser.add_argument(
        "--output", "-o",
        type=str,
        help="Output file path (default: stdout)"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        help="Output directory for batch processing"
    )
    
    # Format options
    parser.add_argument(
        "--format", "-f",
        choices=["markdown", "json", "csv", "plain"],
        default="markdown",
        help="Output format (default: markdown)"
    )
    
    # Category filter
    parser.add_argument(
        "--category", "-c",
        choices=["Software", "Mechanical/Hardware", "Logistics", "Documentation", "Follow-ups"],
        help="Filter by category"
    )
    
    # Summary option
    parser.add_argument(
        "--summary", "-s",
        action="store_true",
        help="Include summary statistics"
    )
    
    args = parser.parse_args()
    
    # Initialize extractor
    extractor = TaskExtractor()
    
    # Single file processing
    if args.input:
        process_single_file(
            args.input,
            args.output,
            args.format,
            args.category,
            args.summary,
            extractor
        )
    
    # Batch processing
    elif args.input_dir:
        if not args.output_dir:
            print("Error: --output-dir required for batch processing", file=sys.stderr)
            sys.exit(1)
        
        process_directory(
            args.input_dir,
            args.output_dir,
            args.format,
            args.category,
            args.summary,
            extractor
        )


def process_single_file(
    input_path: str,
    output_path: str,
    format_type: str,
    category_filter: str,
    include_summary: bool,
    extractor: TaskExtractor
):
    """Process a single input file."""
    # Read input
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        print(f"Error reading {input_path}: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Extract tasks
    tasks = extractor.parse(text, source=input_path)
    
    # Filter by category if specified
    if category_filter:
        tasks = [t for t in tasks if t.category == category_filter]
    
    # Format output
    output = format_tasks_for_asana(tasks, format_type)
    
    # Add summary if requested
    if include_summary:
        summary = generate_summary(tasks)
        output = f"{summary}\n\n{output}"
    
    # Write or print output
    if output_path:
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(output)
            print(f"Extracted {len(tasks)} task(s) to {output_path}")
        except Exception as e:
            print(f"Error writing {output_path}: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(output)


def process_directory(
    input_dir: str,
    output_dir: str,
    format_type: str,
    category_filter: str,
    include_summary: bool,
    extractor: TaskExtractor
):
    """Process all files in a directory."""
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    if not input_path.is_dir():
        print(f"Error: {input_dir} is not a directory", file=sys.stderr)
        sys.exit(1)
    
    # Create output directory
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Process each text file
    input_files = list(input_path.glob("*.txt")) + list(input_path.glob("*.md"))
    
    if not input_files:
        print(f"No .txt or .md files found in {input_dir}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Processing {len(input_files)} file(s)...")
    
    for input_file in input_files:
        # Determine output filename
        output_file = output_path / f"{input_file.stem}_tasks.{_get_extension(format_type)}"
        
        print(f"  {input_file.name} -> {output_file.name}")
        
        # Process file
        process_single_file(
            str(input_file),
            str(output_file),
            format_type,
            category_filter,
            include_summary,
            extractor
        )
    
    print(f"\nCompleted: {len(input_files)} file(s) processed")


def _get_extension(format_type: str) -> str:
    """Get file extension for format type."""
    extensions = {
        "markdown": "md",
        "json": "json",
        "csv": "csv",
        "plain": "txt"
    }
    return extensions.get(format_type, "txt")


if __name__ == "__main__":
    main()
