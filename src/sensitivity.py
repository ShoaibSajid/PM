"""
Sensitivity scrubber to protect credentials and sensitive information.
"""
import re
from typing import Tuple, List


class SensitivityScrubber:
    """
    Scrubs sensitive information from text inputs.
    Replaces credentials, secrets, tokens, IPs, etc. with safe placeholders.
    """
    
    # Patterns for sensitive data
    PATTERNS = [
        # API keys and tokens
        (r'\b[A-Za-z0-9_-]{20,}\b', '(token omitted)'),
        # Passwords (common patterns)
        (r'(?i)password[:\s=]+[^\s]+', 'password: (omitted)'),
        (r'(?i)passwd[:\s=]+[^\s]+', 'passwd: (omitted)'),
        (r'(?i)pwd[:\s=]+[^\s]+', 'pwd: (omitted)'),
        # Usernames with passwords
        (r'(?i)user(?:name)?[:\s=]+[^\s]+\s+pass(?:word)?[:\s=]+[^\s]+', '(credentials omitted)'),
        # IP addresses (be careful with version numbers)
        (r'\b(?:\d{1,3}\.){3}\d{1,3}\b', '(IP omitted)'),
        # AWS keys
        (r'(?i)(?:AKIA|ASIA)[0-9A-Z]{16}', '(AWS key omitted)'),
        # GitHub tokens
        (r'ghp_[a-zA-Z0-9]{36}', '(GitHub token omitted)'),
        (r'gho_[a-zA-Z0-9]{36}', '(GitHub OAuth token omitted)'),
        # Private keys
        (r'-----BEGIN (?:RSA |EC )?PRIVATE KEY-----[\s\S]*?-----END (?:RSA |EC )?PRIVATE KEY-----', 
         '(private key omitted)'),
        # Email addresses (optional - may want to keep these)
        # (r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '(email omitted)'),
    ]
    
    def __init__(self):
        """Initialize the scrubber with compiled patterns."""
        self.compiled_patterns = [
            (re.compile(pattern), replacement) 
            for pattern, replacement in self.PATTERNS
        ]
    
    def scrub(self, text: str) -> Tuple[str, List[str]]:
        """
        Scrub sensitive information from text.
        
        Args:
            text: Input text that may contain sensitive info
            
        Returns:
            Tuple of (scrubbed_text, list_of_warnings)
        """
        scrubbed = text
        warnings = []
        
        for pattern, replacement in self.compiled_patterns:
            matches = pattern.findall(scrubbed)
            if matches:
                scrubbed = pattern.sub(replacement, scrubbed)
                warnings.append(f"Sensitive data detected and removed: {replacement}")
        
        return scrubbed, warnings
    
    def has_sensitive_data(self, text: str) -> bool:
        """
        Check if text contains sensitive data without scrubbing.
        
        Args:
            text: Input text to check
            
        Returns:
            True if sensitive data is detected
        """
        for pattern, _ in self.compiled_patterns:
            if pattern.search(text):
                return True
        return False
