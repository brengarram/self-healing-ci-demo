import pytest

from src.contact_utils import (
    normalize_email,
    is_valid_email,
    deduplicate_emails
)

def test_normalize_email_strips_spaces():
    assert normalize_email("  user@example.com  ") == "user@example.com"

def test_valid_email_simple():
    assert is_valid_email("user@example.com") is True

def test_invalid_email_missing_at():
    assert is_valid_email("userexample.com") is False


def test_invalid_email_missing_domain():
    assert is_valid_email("user@") is False


def test_deduplicate_emails_removes_duplicates():
    emails = [
        "USER@example.com",
        "user@example.com",
        "admin@example.com"
    ]

    result = deduplicate_emails(emails)

    assert result == [
        "user@example.com",
        "admin@example.com"
    ]

    assert result == [
        "user@example.com",
        "admin@example.com"
    ]