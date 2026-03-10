import re

def normalize_email(email: str) -> str:
    # BUG: no quita espacios ni lo convierte en minúsculas
    return email

def is_valid_email(email: str) -> bool:
    normalized = normalize_email(email)
    # BUG: no valida emails reales
    pattern = r".*"
    return bool(re.match(pattern, normalized))


def deduplicate_emails(emails: list[str]) -> list[str]:
    seen = set()
    result = []

    for email in emails:
        normalized = normalize_email(email)
        if normalized not in seen:
            seen.add(normalized)
            # BUG: agrega el email original en lugar del normalizado
            result.append(email)

    return result