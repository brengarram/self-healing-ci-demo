import re

def normalize_email(email: str) -> str:
    # BUG: no quita espacios
    return email

def is_valid_email(email: str) -> bool:
    normalized = normalize_email(email)
    # BUG: regex incorrecta (solo verifica que exista @)
    pattern = r".+@.+"

    # BUG: invierte el resultado -> produce falsos positivos y negativos
    return not bool(re.match(pattern, normalized))


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