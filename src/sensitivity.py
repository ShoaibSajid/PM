"""Sensitivity scrubber for removing credentials and secrets from task text."""

import re
from typing import List, Tuple


# Patterns for sensitive information
SENSITIVE_PATTERNS = [
    # IP addresses (IPv4 and IPv6)
    (r'\b(?:\d{1,3}\.){3}\d{1,3}\b', 'IP address'),
    (r'\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b', 'IPv6 address'),
    
    # Passwords and tokens (common patterns)
    (r'\b[Pp]assword\s*[:\=]\s*\S+', 'password'),
    (r'\b[Tt]oken\s*[:\=]\s*\S+', 'token'),
    (r'\b[Aa]pi[_\-\s]?[Kk]ey\s*[:\=]\s*\S+', 'API key'),
    (r'\b[Ss]ecret\s*[:\=]\s*\S+', 'secret'),
    (r'\b[Aa]ccess[_\-\s]?[Kk]ey\s*[:\=]\s*\S+', 'access key'),
    
    # Common credential formats
    # Note: This may match commit hashes or UUIDs - review output carefully
    # (r'[a-zA-Z0-9]{32,}', 'potential token'),  # Disabled to reduce false positives
    
    # Database connection strings
    (r'(?:mysql|postgresql|mongodb)://[^\s]+', 'database connection'),
    
    # Email addresses (contextual - may or may not be sensitive)
    # (r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 'email'),
    
    # URLs with credentials
    (r'https?://[^:]+:[^@]+@', 'URL with credentials'),
    
    # Private keys
    (r'-----BEGIN (?:RSA )?PRIVATE KEY-----', 'private key'),
    
    # AWS keys
    (r'AKIA[0-9A-Z]{16}', 'AWS access key'),
    
    # Generic base64 that might be sensitive (be conservative)
    # Note: May produce false positives for legitimate base64 content
    # (r'\b[A-Za-z0-9+/]{40,}={0,2}\b', 'potential encoded secret'),  # Disabled to reduce false positives
]


class SensitivityScrubber:
    """Scrubs sensitive information from text."""
    
    def __init__(self, strict_mode: bool = True):
        """
        Initialize scrubber.
        
        Args:
            strict_mode: If True, aggressively scrub potential secrets.
                        If False, only scrub obvious secrets.
        """
        self.strict_mode = strict_mode
        self.scrubbed_items: List[str] = []
    
    def scrub(self, text: str) -> Tuple[str, bool]:
        """
        Scrub sensitive information from text.
        
        Args:
            text: Input text to scrub
        
        Returns:
            Tuple of (scrubbed_text, was_scrubbed)
        """
        original_text = text
        self.scrubbed_items = []
        
        for pattern, label in SENSITIVE_PATTERNS:
            matches = list(re.finditer(pattern, text))
            if matches:
                self.scrubbed_items.append(label)
                # Replace sensitive content
                text = re.sub(pattern, f'(sensitive details omitted: {label})', text)
        
        # Check for common sensitive keywords
        sensitive_keywords = [
            'password', 'passwd', 'pwd', 'secret', 'token', 'key', 
            'credential', 'auth', 'login', 'username'
        ]
        
        text_lower = text.lower()
        for keyword in sensitive_keywords:
            # Look for keyword followed by colon or equals and a value
            pattern = rf'\b{keyword}\s*[:\=]\s*[^\s,;]+'
            if re.search(pattern, text_lower):
                text = re.sub(pattern, f'(sensitive details omitted: {keyword})', text, flags=re.IGNORECASE)
                if keyword not in self.scrubbed_items:
                    self.scrubbed_items.append(keyword)
        
        was_scrubbed = text != original_text
        return text, was_scrubbed
    
    def get_scrubbed_items(self) -> List[str]:
        """Get list of scrubbed item types from last scrub operation."""
        return self.scrubbed_items
    
    def validate_safe(self, text: str) -> bool:
        """
        Check if text appears safe (no obvious sensitive data).
        
        Returns:
            True if text appears safe, False if potential sensitive data found
        """
        _, was_scrubbed = self.scrub(text)
        return not was_scrubbed


def scrub_sensitive_info(text: str, strict: bool = True) -> Tuple[str, bool]:
    """
    Convenience function to scrub sensitive information from text.
    
    Args:
        text: Input text
        strict: Use strict mode
    
    Returns:
        Tuple of (scrubbed_text, was_scrubbed)
    """
    scrubber = SensitivityScrubber(strict_mode=strict)
    return scrubber.scrub(text)
