"""Date/time utilities for KST timezone handling."""

from datetime import datetime, timedelta
try:
    from zoneinfo import ZoneInfo
except ImportError:
    # Fallback for Python < 3.9
    from pytz import timezone as ZoneInfo
from typing import Optional
import re


try:
    KST = ZoneInfo("Asia/Seoul")
except:
    # Fallback for pytz
    import pytz
    KST = pytz.timezone("Asia/Seoul")


def get_current_kst() -> datetime:
    """Get current datetime in KST timezone."""
    return datetime.now(KST)


def parse_relative_date(text: str, reference_date: Optional[datetime] = None) -> tuple[str, bool]:
    """
    Parse relative date references and convert to explicit KST dates.
    
    Args:
        text: Input text with potential relative dates
        reference_date: Reference date for relative calculations (defaults to now in KST)
    
    Returns:
        Tuple of (explicit_date_string, is_assumed)
    """
    if reference_date is None:
        reference_date = get_current_kst()
    
    text_lower = text.lower()
    
    # Today
    if "today" in text_lower:
        return reference_date.strftime("%Y-%m-%d"), False
    
    # Tomorrow
    if "tomorrow" in text_lower:
        tomorrow = reference_date + timedelta(days=1)
        return tomorrow.strftime("%Y-%m-%d"), False
    
    # Yesterday
    if "yesterday" in text_lower:
        yesterday = reference_date - timedelta(days=1)
        return yesterday.strftime("%Y-%m-%d"), False
    
    # Next week
    if "next week" in text_lower:
        next_week = reference_date + timedelta(weeks=1)
        return next_week.strftime("%Y-%m-%d"), True
    
    # This week
    if "this week" in text_lower:
        return reference_date.strftime("%Y-%m-%d"), True
    
    # Day of week (e.g., "Monday", "next Friday")
    days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    for i, day in enumerate(days_of_week):
        if day in text_lower:
            # Calculate days until that day
            current_weekday = reference_date.weekday()
            target_weekday = i
            days_ahead = (target_weekday - current_weekday) % 7
            if days_ahead == 0 and "next" in text_lower:
                days_ahead = 7
            elif days_ahead == 0:
                days_ahead = 7  # Assume next occurrence
            
            target_date = reference_date + timedelta(days=days_ahead)
            return target_date.strftime("%Y-%m-%d"), True
    
    # Explicit date pattern (YYYY-MM-DD or similar)
    date_pattern = r'\d{4}-\d{2}-\d{2}'
    match = re.search(date_pattern, text)
    if match:
        return match.group(0), False
    
    # No date found - propose reasonable follow-up
    default_followup = reference_date + timedelta(days=2)
    return default_followup.strftime("%Y-%m-%d"), True


def format_kst_datetime(dt: datetime) -> str:
    """Format datetime as KST string."""
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=KST)
    else:
        dt = dt.astimezone(KST)
    return dt.strftime("%Y-%m-%d %H:%M:%S KST")


def add_kst_marker(text: str) -> str:
    """Add KST marker to date mentions in text."""
    # Pattern for dates
    date_pattern = r'(\d{4}-\d{2}-\d{2})'
    return re.sub(date_pattern, r'\1 (KST)', text)
