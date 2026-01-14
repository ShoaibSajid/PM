"""
PM Assistant - Industrial Project Coordination Assistant
Core module for task extraction and formatting.
"""
from src.parser import TaskParser
from src.formatter import AsanaFormatter
from src.sensitivity import SensitivityScrubber

__all__ = [
    "TaskParser",
    "AsanaFormatter",
    "SensitivityScrubber",
]

__version__ = "0.1.0"
