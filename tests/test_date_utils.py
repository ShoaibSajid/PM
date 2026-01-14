"""Tests for date/time utilities."""

import sys
from pathlib import Path
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.date_utils import parse_relative_date, get_current_kst, add_kst_marker, KST


def test_get_current_kst():
    """Test getting current KST time."""
    kst_time = get_current_kst()
    assert kst_time.tzinfo == KST


def test_parse_today():
    """Test parsing 'today'."""
    reference = datetime(2026, 1, 14, 12, 0, tzinfo=KST)
    date_str, is_assumed = parse_relative_date("today", reference)
    
    assert date_str == "2026-01-14"
    assert not is_assumed


def test_parse_tomorrow():
    """Test parsing 'tomorrow'."""
    reference = datetime(2026, 1, 14, 12, 0, tzinfo=KST)
    date_str, is_assumed = parse_relative_date("tomorrow", reference)
    
    assert date_str == "2026-01-15"
    assert not is_assumed


def test_parse_explicit_date():
    """Test parsing explicit date."""
    date_str, is_assumed = parse_relative_date("2026-01-20")
    
    assert date_str == "2026-01-20"
    assert not is_assumed


def test_parse_next_week():
    """Test parsing 'next week'."""
    reference = datetime(2026, 1, 14, 12, 0, tzinfo=KST)
    date_str, is_assumed = parse_relative_date("next week", reference)
    
    assert is_assumed  # "next week" is ambiguous
    assert "2026-01-" in date_str


def test_add_kst_marker():
    """Test adding KST marker to dates."""
    text = "Deadline is 2026-01-15"
    marked = add_kst_marker(text)
    
    assert "(KST)" in marked
    assert "2026-01-15 (KST)" in marked


if __name__ == "__main__":
    test_get_current_kst()
    test_parse_today()
    test_parse_tomorrow()
    test_parse_explicit_date()
    test_parse_next_week()
    test_add_kst_marker()
    
    print("All date/time tests passed!")
