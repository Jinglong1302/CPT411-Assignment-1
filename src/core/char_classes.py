def is_digit(ch: str) -> bool:
    """Return True when a character is an ASCII digit."""
    return "0" <= ch <= "9"


def is_letter(ch: str) -> bool:
    """Return True when a character is an ASCII alphabetic letter."""
    return ("a" <= ch <= "z") or ("A" <= ch <= "Z")


def is_space(ch: str) -> bool:
    """Return True when a character is one of the supported whitespace symbols."""
    return ch in {" ", "\t", "\n", "\r"}


def is_boundary(ch: str | None) -> bool:
    """Return True when a character marks the boundary of a token."""
    if ch is None:
        return True
    return not (is_digit(ch) or is_letter(ch) or ch == "%")
