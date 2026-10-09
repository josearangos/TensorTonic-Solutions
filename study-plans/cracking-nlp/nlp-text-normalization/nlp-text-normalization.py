import re

def text_normalize(text: str, operations: list) -> str:
    """
    Returns the normalized string.
    """
    for op in operations:
        match op:
            case "lowercase":
                text = text.lower()
            case "strip":
                text = text.strip()
            case "remove_punctuation":
                text = re.sub(r'[^\w\s]|_', '', text)
            case "remove_digits":
                text = re.sub(r'\d+', '', text)
            case"collapse_whitespace":
                text = re.sub(r'\s+', ' ', text)
    return text