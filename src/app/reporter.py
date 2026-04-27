from src.app.models import MatchResult


def highlight_matches(text: str, matches: list[MatchResult]) -> str:
    """Return text with each matched span wrapped for visual emphasis."""

    if not matches:
        return text

    pieces: list[str] = []
    cursor = 0
    for match in matches:
        pieces.append(text[cursor : match.start])
        pieces.append(f"**[{text[match.start:match.end + 1]}]**")
        cursor = match.end + 1
    pieces.append(text[cursor:])
    return "".join(pieces)


def to_table_rows(matches: list[MatchResult]) -> list[dict[str, str | int]]:
    """Convert match objects into flat rows for table-style display."""

    rows: list[dict[str, str | int]] = []
    for index, match in enumerate(matches, start=1):
        rows.append(
            {
                "no": index,
                "pattern": match.pattern,
                "start": match.start,
                "end": match.end,
                "status": match.status,
                "category": match.category,
            }
        )
    return rows
