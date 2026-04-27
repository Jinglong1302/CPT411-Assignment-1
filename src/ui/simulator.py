from src.app.models import MatchResult


def trace_rows(match: MatchResult) -> list[dict[str, str | int]]:
    """Convert transition trace data into table rows for UI display."""
    rows: list[dict[str, str | int]] = []
    for step_no, step in enumerate(match.trace, start=1):
        rows.append(
            {
                "step": step_no,
                "index": step.index,
                "char": step.char,
                "from_state": step.from_state,
                "to_state": step.to_state,
            }
        )
    return rows
