from dataclasses import dataclass


@dataclass
class TransitionStep:
    """Represents one DFA transition taken while scanning a token."""

    index: int
    char: str
    from_state: str
    to_state: str


@dataclass
class MatchResult:
    """Stores one recognized pattern with metadata and transition trace."""

    pattern: str
    start: int
    end: int
    status: str
    category: str
    trace: list[TransitionStep]
