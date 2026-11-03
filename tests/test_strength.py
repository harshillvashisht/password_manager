"""Tests for local password strength scoring."""

from password_manager.strength import check_password_strength


def test_common_password_is_weak() -> None:
    result = check_password_strength("password")

    assert result.rating == "weak"
    assert result.is_common


def test_short_password_is_weak() -> None:
    result = check_password_strength("aB3!")

    assert result.rating == "weak"
    assert result.length == 4


def test_long_mixed_password_is_strong() -> None:
    result = check_password_strength("L0cal!Strength-2026")

    assert result.rating == "strong"
    assert result.character_variety == 4
    assert result.entropy_bits >= 70
