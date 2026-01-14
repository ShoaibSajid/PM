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
    # Order matters - more specific patterns should come first
    PATTERNS = [
        # GitHub tokens (must come before generic token pattern)
        (r'ghp_[a-zA-Z0-9]{30,40}', '(GitHub token omitted)'),
        (r'gho_[a-zA-Z0-9]{30,40}', '(GitHub OAuth token omitted)'),
        (r'ghs_[a-zA-Z0-9]{30,40}', '(GitHub server token omitted)'),
        (r'ghr_[a-zA-Z0-9]{30,40}', '(GitHub refresh token omitted)'),
        # AWS keys (must come before generic token pattern)
        (r'(?i)(?:AKIA|ASIA)[0-9A-Z]{16}', '(AWS key omitted)'),
        # Private keys
        (r'-----BEGIN (?:RSA |EC )?PRIVATE KEY-----[\s\S]*?-----END (?:RSA |EC )?PRIVATE KEY-----', 
         '(private key omitted)'),
        # Passwords (common patterns) - updated to handle "is", "was", etc.
        (r'(?i)password\s*(?:is|was)?\s*[:\s=]+\s*[^\s]+', 'password: (omitted)'),
        (r'(?i)passwd\s*(?:is|was)?\s*[:\s=]+\s*[^\s]+', 'passwd: (omitted)'),
        (r'(?i)pwd\s*(?:is|was)?\s*[:\s=]+\s*[^\s]+', 'pwd: (omitted)'),
        # Usernames with passwords
        (r'(?i)user(?:name)?\s*(?:is|was)?\s*[:\s=]+\s*[^\s]+\s+pass(?:word)?\s*(?:is|was)?\s*[:\s=]+\s*[^\s]+', '(credentials omitted)'),
        # IP addresses (be careful with version numbers)
        (r'\b(?:\d{1,3}\.){3}\d{1,3}\b', '(IP omitted)'),
        # API keys and generic long tokens (should be last to not interfere with specific patterns)
        (r'\b[A-Za-z0-9_-]{20,}\b', '(token omitted)'),
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
