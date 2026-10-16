
import re

def extract_patterns(text: str, pattern_type: str) -> list:
    """
    Returns a list of matched strings.
    """
    email_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    url_pattern = r'https?://[^\s,]+'
    hashtags_pattern = r'#[\w\u00c0-\u024f]+'
    date_pattern = r'\b(?:\d{4}-\d{1,2}-\d{1,2}|\d{1,2}/\d{1,2}/\d{2,4})\b'
    money_pattern = r'\$\d+(?:\.\d{2})?'

    patterns = {
        "emails": email_pattern,
        "urls": url_pattern,
        "hashtags": hashtags_pattern,
        "dates": date_pattern,
        "money": money_pattern,
    }

    if pattern_type not in patterns:
        return []

    result = re.findall(patterns[pattern_type], text)

    if pattern_type == "urls":
        result = [re.sub(r'[,.)!?;:]+$', '', url) for url in result]

    return result
