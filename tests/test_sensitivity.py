"""
Tests for the sensitivity scrubber.
"""
import pytest
from src.sensitivity import SensitivityScrubber


class TestSensitivityScrubber:
    """Test cases for SensitivityScrubber."""
    
    def test_scrub_password(self):
        """Test scrubbing of password patterns."""
        scrubber = SensitivityScrubber()
        
        text = "The password is: secretpass123"
        scrubbed, warnings = scrubber.scrub(text)
        
        assert "secretpass123" not in scrubbed
        assert "(omitted)" in scrubbed
        assert len(warnings) > 0
    
    def test_scrub_ip_address(self):
        """Test scrubbing of IP addresses."""
        scrubber = SensitivityScrubber()
        
        text = "Connect to server at 192.168.1.100"
        scrubbed, warnings = scrubber.scrub(text)
        
        assert "192.168.1.100" not in scrubbed
        assert "(IP omitted)" in scrubbed
        assert len(warnings) > 0
    
    def test_scrub_github_token(self):
        """Test scrubbing of GitHub tokens."""
        scrubber = SensitivityScrubber()
        
        text = "Use token ghp_1234567890abcdefghijklmnopqrstuv"
        scrubbed, warnings = scrubber.scrub(text)
        
        assert "ghp_" not in scrubbed
        assert "(GitHub token omitted)" in scrubbed
        assert len(warnings) > 0
    
    def test_no_sensitive_data(self):
        """Test that clean text passes through unchanged."""
        scrubber = SensitivityScrubber()
        
        text = "This is a clean message about tasks"
        scrubbed, warnings = scrubber.scrub(text)
        
        assert scrubbed == text
        assert len(warnings) == 0
    
    def test_has_sensitive_data_detection(self):
        """Test detection without scrubbing."""
        scrubber = SensitivityScrubber()
        
        assert scrubber.has_sensitive_data("password: secret123")
        assert scrubber.has_sensitive_data("192.168.1.1")
        assert not scrubber.has_sensitive_data("This is clean text")
    
    def test_multiple_sensitive_items(self):
        """Test scrubbing multiple sensitive items."""
        scrubber = SensitivityScrubber()
        
        text = "password: secret123 at IP 10.0.0.1"
        scrubbed, warnings = scrubber.scrub(text)
        
        assert "secret123" not in scrubbed
        assert "10.0.0.1" not in scrubbed
        assert len(warnings) >= 2
