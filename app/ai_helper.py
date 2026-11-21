from typing import Optional


def infer_priority_and_tag(title: str, content: Optional[str] = None) -> tuple[str, str]:
    text = f"{title} {content or ''}".lower()

    high_keywords = ["urgent", "asap", "deadline", "exam", "today", "important", "payment", "due"]
    low_keywords = ["someday", "idea", "later", "optional", "maybe"]

    if any(word in text for word in high_keywords):
        priority = "High"
    elif any(word in text for word in low_keywords):
        priority = "Low"
    else:
        priority = "Medium"

    if any(word in text for word in ["remind", "meeting", "call", "alarm", "schedule", "time"]):
        tag = "Reminder"
    elif any(word in text for word in ["code", "api", "bug", "sql", "python", "fastapi", "project"]):
        tag = "Dev"
    elif any(word in text for word in ["gym", "workout", "bike", "ride", "health"]):
        tag = "Personal"
    else:
        tag = "General"

    return priority, tag
