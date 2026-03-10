import re

def normalize_email(email: str) -> str:
    return email.strip().lower()

def is_valid_email(email: str) -> bool:
    normalized = normalize_email(email)
    pattern = r"^[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,}$"
    return bool(re.match(pattern, normalized))


def deduplicate_emails(emails: list[str]) -> list[str]:
    seen = set()
    result = []

    for email in emails:
        normalized = normalize_email(email)
        if normalized not in seen:
            seen.add(normalized)
            result.append(normalized)

    return result