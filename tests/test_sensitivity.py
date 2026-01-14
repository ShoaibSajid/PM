"""Tests for sensitivity scrubbing."""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.sensitivity import scrub_sensitive_info, SensitivityScrubber


def test_password_scrubbing():
    """Test password scrubbing."""
    text = "The password: secret123 should not be visible."
    scrubbed, was_scrubbed = scrub_sensitive_info(text)
    
    assert was_scrubbed
    assert "secret123" not in scrubbed
    assert "sensitive details omitted" in scrubbed


def test_ip_address_scrubbing():
    """Test IP address scrubbing."""
    text = "Connect to 192.168.1.100 for testing."
    scrubbed, was_scrubbed = scrub_sensitive_info(text)
    
    assert was_scrubbed
    assert "192.168.1.100" not in scrubbed
    assert "sensitive details omitted" in scrubbed


def test_token_scrubbing():
    """Test token scrubbing."""
    text = "API token: abcd1234efgh5678ijkl"
    scrubbed, was_scrubbed = scrub_sensitive_info(text)
    
    assert was_scrubbed
    assert "abcd1234efgh5678ijkl" not in scrubbed


def test_safe_text():
    """Test that safe text is not modified."""
    text = "We need to test the firmware tomorrow."
    scrubbed, was_scrubbed = scrub_sensitive_info(text)
    
    assert not was_scrubbed
    assert scrubbed == text


def test_multiple_sensitive_items():
    """Test scrubbing multiple sensitive items."""
    text = "Password: pass123 and token: tok456 at IP 10.0.0.1"
    scrubbed, was_scrubbed = scrub_sensitive_info(text)
    
    assert was_scrubbed
    assert "pass123" not in scrubbed
    assert "tok456" not in scrubbed
    assert "10.0.0.1" not in scrubbed


def test_scrubber_tracking():
    """Test that scrubber tracks what was scrubbed."""
    scrubber = SensitivityScrubber()
    text = "Password: secret123"
    scrubbed, was_scrubbed = scrubber.scrub(text)
    
    assert was_scrubbed
    scrubbed_items = scrubber.get_scrubbed_items()
    assert len(scrubbed_items) > 0


if __name__ == "__main__":
    test_password_scrubbing()
    test_ip_address_scrubbing()
    test_token_scrubbing()
    test_safe_text()
    test_multiple_sensitive_items()
    test_scrubber_tracking()
    
    print("All sensitivity tests passed!")
