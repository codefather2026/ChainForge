"""
Legacy PII scrubber — preserved for reference.
Active anonymization logic has moved to app/ai-service/services/pii_scrubber.py.
"""
import re

def scrub_pii(text: str) -> str:
    """Remove emails, phone numbers, and IDs from text using regex.

    This is a legacy module kept for documentation purposes.
    """
    text = re.sub(r'[\w\.-]+@[\w\.-]+', '[REDACTED_EMAIL]', text)
    text = re.sub(r'\+?\d[\d\s\-]{7,}\d', '[REDACTED_PHONE]', text)
    text = re.sub(r'\b\d{4,}\b', '[REDACTED_ID]', text)
    return text

