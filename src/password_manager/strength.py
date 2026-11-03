"""Local password strength scoring."""

from dataclasses import dataclass
import math
import string


_COMMON_PASSWORDS: frozenset[str] = frozenset(
    {
        "123456",
        "123456789",
        "12345678",
        "12345",
        "1234567",
        "1234567890",
        "password",
        "password1",
        "password123",
        "qwerty",
        "qwerty123",
        "abc123",
        "admin",
        "admin123",
        "letmein",
        "welcome",
        "welcome1",
        "monkey",
        "dragon",
        "football",
        "iloveyou",
        "sunshine",
        "princess",
        "master",
        "login",
        "passw0rd",
        "654321",
        "superman",
        "qwertyuiop",
        "asdfgh",
        "asdfghjkl",
        "1q2w3e4r",
        "123123",
        "111111",
        "000000",
        "whatever",
        "trustno1",
        "baseball",
        "shadow",
        "michael",
        "jennifer",
        "charlie",
        "jordan",
        "hunter",
        "freedom",
        "secret",
        "access",
        "mustang",
        "starwars",
        "nothing",
    }
)


@dataclass(frozen=True, slots=True)
class PasswordStrength:
    """The local measurements and rating for a password."""

    rating: str
    length: int
    character_variety: int
    entropy_bits: float
    is_common: bool


def check_password_strength(password: str) -> PasswordStrength:
    """Return a local strength rating without displaying the password."""
    has_lower = any(character in string.ascii_lowercase for character in password)
    has_upper = any(character in string.ascii_uppercase for character in password)
    has_digit = any(character in string.digits for character in password)
    has_symbol = any(not character.isalnum() for character in password)
    variety = sum((has_lower, has_upper, has_digit, has_symbol))

    alphabet_size = sum(
        (
            26 if has_lower else 0,
            26 if has_upper else 0,
            10 if has_digit else 0,
            33 if has_symbol else 0,
        )
    )
    entropy_bits = (
        len(password) * math.log2(alphabet_size)
        if alphabet_size
        else 0.0
    )
    is_common = password.casefold() in _COMMON_PASSWORDS

    if is_common or len(password) < 8 or entropy_bits < 40:
        rating = "weak"
    elif len(password) >= 12 and variety >= 3 and entropy_bits >= 70:
        rating = "strong"
    else:
        rating = "fair"

    return PasswordStrength(
        rating = rating,
        length = len(password),
        character_variety = variety,
        entropy_bits = entropy_bits,
        is_common = is_common,
    )
