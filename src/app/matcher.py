from src.app.models import MatchResult, TransitionStep
from src.core.char_classes import is_boundary, is_digit
from src.core.dfa_engine import DFAEngine


class StreamingMatcher:
    def __init__(self) -> None:
        self.engine = DFAEngine()

    def find_matches(self, text: str) -> list[MatchResult]:
        matches: list[MatchResult] = []
        i = 0

        while i < len(text):
            if i > 0 and not is_boundary(text[i - 1]):
                i += 1
                continue

            match = self._consume_from(text, i)
            if match is None:
                i += 1
                continue

            matches.append(match)
            i = match.end + 1

        return matches

    def _consume_from(self, text: str, start: int) -> MatchResult | None:
        self.engine.reset()
        trace: list[TransitionStep] = []
        last_accept_end = -1
        last_accept_category = ""
        last_accept_trace_len = 0

        pos = start
        while pos < len(text):
            ch = text[pos]
            prev_state = self.engine.state
            next_state = self.engine.step(ch)
            trace.append(
                TransitionStep(
                    index=pos,
                    char=ch,
                    from_state=self._state_name(prev_state),
                    to_state=self._state_name(next_state),
                )
            )

            if self.engine.is_trap(next_state):
                break

            next_char = text[pos + 1] if pos + 1 < len(text) else None
            if self.engine.is_accepting(next_state) and is_boundary(next_char):
                category = self.engine.accepted_category(next_state)
                if category is not None:
                    last_accept_end = pos
                    last_accept_category = category.value
                    last_accept_trace_len = len(trace)

            pos += 1

        if last_accept_end < start:
            return None

        return MatchResult(
            pattern=text[start : last_accept_end + 1],
            start=start,
            end=last_accept_end,
            status="Accept",
            category=last_accept_category,
            trace=trace[:last_accept_trace_len],
        )

    @staticmethod
    def _state_name(state: object) -> str:
        return getattr(state, "name", str(state))
