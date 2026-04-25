from dataclasses import dataclass

from src.core.char_classes import is_digit, is_letter
from src.core.states import Category, MONTHS, State, UNITS_AND_SCALES


@dataclass
class DFAContext:
    word_buffer: str = ""
    word_kind: str = ""  # month | unit | unknown
    number_buffer: str = ""  # digits collected for the integer token (day candidate)
    year_count: int = 0
    year_value: int = 0


class DFAEngine:
    # configure acceptable year range
    YEAR_MIN = 1000
    YEAR_MAX = 2100

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.state = State.START
        self.ctx = DFAContext()

    def step(self, ch: str) -> State:
        s = self.state

        if s == State.START:
            if is_digit(ch):
                self.ctx.number_buffer = ch
                self.state = State.INT
            else:
                self.state = State.TRAP
            return self.state

        if s == State.INT:
            if is_digit(ch):
                # collect digits for day/current integer token
                self.ctx.number_buffer += ch
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
            # Only start year parsing if previous word classified as month,
            # and the number (day) we collected is 1-2 digits long (date day must be 1 or 2 digits).
            if self.ctx.word_kind == "month" and is_digit(ch) and 1 <= len(self.ctx.number_buffer) <= 2:
                # initialize year parsing with first digit
                self.ctx.year_count = 1
                self.ctx.year_value = int(ch)
                self.state = State.DATE_YEAR
            else:
                self.state = State.TRAP
            return self.state

        if s == State.DATE_YEAR:
            if is_digit(ch):
                # Allow exactly 4 digits for year; a 5th digit -> TRAP
                if self.ctx.year_count < 4:
                    self.ctx.year_count += 1
                    self.ctx.year_value = self.ctx.year_value * 10 + int(ch)
                    self.state = State.DATE_YEAR
                else:
                    self.state = State.TRAP
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
            # require exactly 4 year digits and perform day/year validation
            if self.ctx.year_count != 4:
                return None
            try:
                day = int(self.ctx.number_buffer)
            except Exception:
                return None
            year = self.ctx.year_value
            if not (self.YEAR_MIN <= year <= self.YEAR_MAX):
                return None
            # month name is in ctx.word_buffer (lowercased)
            max_day = self._days_in_month(self.ctx.word_buffer, year)
            if 1 <= day <= max_day:
                return Category.DATE
            return None
        if s == State.WORD and self.ctx.word_buffer in UNITS_AND_SCALES:
            return Category.QUANTITY_WITH_UNIT
        if s == State.INT:
            return Category.EXACT_QUANTITY
        return None

    def _days_in_month(self, month_name: str, year: int) -> int:
        m = (month_name or "").lower()
        if m in {"january", "march", "may", "july", "august", "october", "december"}:
            return 31
        if m in {"april", "june", "september", "november"}:
            return 30
        if m == "february":
            # leap year
            if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
                return 29
            return 28
        # fallback
        return 31
