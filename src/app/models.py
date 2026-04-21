from dataclasses import dataclass


@dataclass
class TransitionStep:
    index: int
    char: str
    from_state: str
    to_state: str


@dataclass
class MatchResult:
    pattern: str
    start: int
    end: int
    status: str
    category: str
    trace: list[TransitionStep]
