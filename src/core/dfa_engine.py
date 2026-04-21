from dataclasses import dataclass

from src.core.char_classes import is_digit, is_letter
from src.core.states import Category, MONTHS, State, UNITS_AND_SCALES


@dataclass
class DFAContext:
    word_buffer: str = ""
    word_kind: str = ""  # month | unit | unknown


class DFAEngine:
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.state = State.START
        self.ctx = DFAContext()

    def step(self, ch: str) -> State:
        s = self.state

        if s == State.START:
            if is_digit(ch):
                self.state = State.INT
            else:
                self.state = State.TRAP
            return self.state

        if s == State.INT:
            if is_digit(ch):
                self.state = State.INT
            elif ch == "%":
                self.state = State.PERCENT
            elif ch == "s":
                self.state = State.ORD_S
            elif ch == "n":
                self.state = State.ORD_N
            elif ch == "r":
                self.state = State.ORD_R
            elif ch == "t":
                self.state = State.ORD_T
            elif ch == " ":
                self.state = State.AFTER_INT_SPACE
            else:
                self.state = State.TRAP
            return self.state

        if s == State.PERCENT:
            self.state = State.TRAP
            return self.state

        if s == State.ORD_S:
            self.state = State.ORD_DONE if ch == "t" else State.TRAP
            return self.state

        if s == State.ORD_N:
            self.state = State.ORD_DONE if ch == "d" else State.TRAP
            return self.state

        if s == State.ORD_R:
            self.state = State.ORD_DONE if ch == "d" else State.TRAP
            return self.state

        if s == State.ORD_T:
            self.state = State.ORD_DONE if ch == "h" else State.TRAP
            return self.state

        if s == State.ORD_DONE:
            self.state = State.TRAP
            return self.state

        if s == State.AFTER_INT_SPACE:
            if is_letter(ch):
                self.ctx.word_buffer = ch.lower()
                self.state = State.WORD
            else:
                self.state = State.TRAP
            return self.state

        if s == State.WORD:
            if is_letter(ch):
                self.ctx.word_buffer += ch.lower()
            elif ch == " ":
                self._finalize_word_kind()
                self.state = State.AFTER_WORD
            else:
                self.state = State.TRAP
            return self.state

        if s == State.AFTER_WORD:
            if self.ctx.word_kind == "month" and is_digit(ch):
                self.state = State.DATE_YEAR
            else:
                self.state = State.TRAP
            return self.state

        if s == State.DATE_YEAR:
            if is_digit(ch):
                self.state = State.DATE_YEAR
            else:
                self.state = State.TRAP
            return self.state

        self.state = State.TRAP
        return self.state

    def _finalize_word_kind(self) -> None:
        word = self.ctx.word_buffer
        if word in MONTHS:
            self.ctx.word_kind = "month"
        elif word in UNITS_AND_SCALES:
            self.ctx.word_kind = "unit"
        else:
            self.ctx.word_kind = "unknown"

    def is_accepting(self, state: State | None = None) -> bool:
        s = state or self.state
        return s in {State.INT, State.PERCENT, State.ORD_DONE, State.WORD, State.DATE_YEAR}

    def accepted_category(self, state: State | None = None) -> Category | None:
        s = state or self.state
        if s == State.PERCENT:
            return Category.PERCENTAGE
        if s == State.ORD_DONE:
            return Category.ORDINAL
        if s == State.DATE_YEAR:
            return Category.DATE
        if s == State.WORD and self.ctx.word_buffer in UNITS_AND_SCALES:
            return Category.QUANTITY_WITH_UNIT
        if s == State.INT:
            return Category.EXACT_QUANTITY
        return None
