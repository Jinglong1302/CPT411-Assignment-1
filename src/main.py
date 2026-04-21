from pathlib import Path

from src.app.matcher import StreamingMatcher
from src.app.reporter import highlight_matches, to_table_rows


def run_cli(input_path: str = "sample_input.txt") -> None:
    path = Path(input_path)
    text = path.read_text(encoding="utf-8") if path.exists() else ""

    matcher = StreamingMatcher()
    matches = matcher.find_matches(text)

    print("Pattern: all recognized L2 number patterns")
    print("Text:")
    print(text)
    print("Status:", "Accept" if matches else "Reject")
    print("Additional information:")
    print("- Number of pattern occurrences:", len(matches))

    for row in to_table_rows(matches):
        print(
            f"- Pattern '{row['pattern']}' at [{row['start']}, {row['end']}] "
            f"category={row['category']} status={row['status']}"
        )

    print("Visualization:")
    print(highlight_matches(text, matches))


if __name__ == "__main__":
    run_cli()
