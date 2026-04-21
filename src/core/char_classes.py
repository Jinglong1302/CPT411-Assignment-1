def is_digit(ch: str) -> bool:
    return "0" <= ch <= "9"


def is_letter(ch: str) -> bool:
    return ("a" <= ch <= "z") or ("A" <= ch <= "Z")


def is_space(ch: str) -> bool:
    return ch in {" ", "\t", "\n", "\r"}


def is_boundary(ch: str | None) -> bool:
    if ch is None:
        return True
    return not (is_digit(ch) or is_letter(ch) or ch == "%")
