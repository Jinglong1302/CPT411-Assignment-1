from src.core.states import Category


class DFAEngine:
    """Implements deterministic transitions for numeric-pattern recognition."""

    # Core control states.
    START = "START"
    INT_1 = "INT_1"
    INT_2 = "INT_2"
    INT_3PLUS = "INT_3PLUS"
    PERCENT = "PERCENT"
    ORD_S = "ORD_S"
    ORD_N = "ORD_N"
    ORD_R = "ORD_R"
    ORD_T = "ORD_T"
    ORD_DONE = "ORD_DONE"

    AFTER_INT_SPACE = "AFTER_INT_SPACE"
    UNIT_G = "UNIT_G"
    UNIT_K = "UNIT_K"
    UNIT_KG = "UNIT_KG"
    UNIT_M = "UNIT_M"
    UNIT_ML = "UNIT_ML"
    UNIT_C = "UNIT_C"
    UNIT_CM = "UNIT_CM"
    UNIT_L = "UNIT_L"

    DATE_SLASH_1 = "DATE_SLASH_1"
    DATE_MONTH_1 = "DATE_MONTH_1"
    DATE_MONTH_2 = "DATE_MONTH_2"
    DATE_SLASH_2 = "DATE_SLASH_2"
    DATE_YEAR_1 = "DATE_YEAR_1"
    DATE_YEAR_2 = "DATE_YEAR_2"
    DATE_YEAR_3 = "DATE_YEAR_3"
    DATE_YEAR_4 = "DATE_YEAR_4"

    TRAP = "TRAP"

    def __init__(self) -> None:
        """Create a DFA engine instance and initialize to START state."""
        self.reset()

    def reset(self) -> None:
        """Reset the machine back to the START state."""
        self.state = self.START

    def step(self, ch: str) -> str:
        """Consume one character and move to the next deterministic state."""
        if not ch:
            self.state = self.TRAP
            return self.state

        s = self.state

        if s == self.START:
            if ch.isdigit():
                self.state = self.INT_1
            else:
                self.state = self.TRAP
            return self.state

        if s == self.INT_1:
            if ch.isdigit():
                self.state = self.INT_2
            elif ch == "%":
                self.state = self.PERCENT
            elif ch == "s":
                self.state = self.ORD_S
            elif ch == "n":
                self.state = self.ORD_N
            elif ch == "r":
                self.state = self.ORD_R
            elif ch == "t":
                self.state = self.ORD_T
            elif ch == " ":
                self.state = self.AFTER_INT_SPACE
            elif ch == "/":
                self.state = self.DATE_SLASH_1
            else:
                self.state = self.TRAP
            return self.state

        if s == self.INT_2:
            if ch.isdigit():
                self.state = self.INT_3PLUS
            elif ch == "%":
                self.state = self.PERCENT
            elif ch == "s":
                self.state = self.ORD_S
            elif ch == "n":
                self.state = self.ORD_N
            elif ch == "r":
                self.state = self.ORD_R
            elif ch == "t":
                self.state = self.ORD_T
            elif ch == " ":
                self.state = self.AFTER_INT_SPACE
            elif ch == "/":
                self.state = self.DATE_SLASH_1
            else:
                self.state = self.TRAP
            return self.state

        if s == self.INT_3PLUS:
            if ch.isdigit():
                self.state = self.INT_3PLUS
            elif ch == "%":
                self.state = self.PERCENT
            elif ch == "s":
                self.state = self.ORD_S
            elif ch == "n":
                self.state = self.ORD_N
            elif ch == "r":
                self.state = self.ORD_R
            elif ch == "t":
                self.state = self.ORD_T
            elif ch == " ":
                self.state = self.AFTER_INT_SPACE
            else:
                self.state = self.TRAP
            return self.state

        if s == self.PERCENT:
            self.state = self.TRAP
            return self.state

        if s == self.ORD_S:
            self.state = self.ORD_DONE if ch == "t" else self.TRAP
            return self.state

        if s == self.ORD_N:
            self.state = self.ORD_DONE if ch == "d" else self.TRAP
            return self.state

        if s == self.ORD_R:
            self.state = self.ORD_DONE if ch == "d" else self.TRAP
            return self.state

        if s == self.ORD_T:
            self.state = self.ORD_DONE if ch == "h" else self.TRAP
            return self.state

        if s == self.ORD_DONE:
            self.state = self.TRAP
            return self.state

        if s == self.AFTER_INT_SPACE:
            if ch == "g":
                self.state = self.UNIT_G
            elif ch == "k":
                self.state = self.UNIT_K
            elif ch == "m":
                self.state = self.UNIT_M
            elif ch == "c":
                self.state = self.UNIT_C
            elif ch == "L":
                self.state = self.UNIT_L
            else:
                self.state = self.TRAP
            return self.state

        if s == self.UNIT_K:
            self.state = self.UNIT_KG if ch == "g" else self.TRAP
            return self.state

        if s == self.UNIT_M:
            self.state = self.UNIT_ML if ch == "l" else self.TRAP
            return self.state

        if s == self.UNIT_C:
            self.state = self.UNIT_CM if ch == "m" else self.TRAP
            return self.state

        if s in {self.UNIT_G, self.UNIT_KG, self.UNIT_ML, self.UNIT_L, self.UNIT_CM}:
            self.state = self.TRAP
            return self.state

        if s == self.DATE_SLASH_1:
            self.state = self.DATE_MONTH_1 if ch.isdigit() else self.TRAP
            return self.state

        if s == self.DATE_MONTH_1:
            if ch.isdigit():
                self.state = self.DATE_MONTH_2
            elif ch == "/":
                self.state = self.DATE_SLASH_2
            else:
                self.state = self.TRAP
            return self.state

        if s == self.DATE_MONTH_2:
            self.state = self.DATE_SLASH_2 if ch == "/" else self.TRAP
            return self.state

        if s == self.DATE_SLASH_2:
            self.state = self.DATE_YEAR_1 if ch.isdigit() else self.TRAP
            return self.state

        if s == self.DATE_YEAR_1:
            self.state = self.DATE_YEAR_2 if ch.isdigit() else self.TRAP
            return self.state

        if s == self.DATE_YEAR_2:
            self.state = self.DATE_YEAR_3 if ch.isdigit() else self.TRAP
            return self.state

        if s == self.DATE_YEAR_3:
            self.state = self.DATE_YEAR_4 if ch.isdigit() else self.TRAP
            return self.state

        if s == self.DATE_YEAR_4:
            self.state = self.TRAP
            return self.state

        self.state = self.TRAP
        return self.state

    def is_accepting(self, state: str | None = None) -> bool:
        """Return True when a state corresponds to an accepted category."""
        return self.accepted_category(state) is not None

    def accepted_category(self, state: str | None = None) -> Category | None:
        """Map an accepting state to its semantic category."""
        s = state or self.state
        if s in {self.INT_1, self.INT_2, self.INT_3PLUS}:
            return Category.EXACT_QUANTITY
        if s == self.PERCENT:
            return Category.PERCENTAGE
        if s == self.ORD_DONE:
            return Category.ORDINAL
        if s in {self.UNIT_G, self.UNIT_KG, self.UNIT_ML, self.UNIT_L, self.UNIT_CM}:
            return Category.QUANTITY_WITH_UNIT
        if s == self.DATE_YEAR_4:
            return Category.DATE
        return None

    def is_trap(self, state: str | None = None) -> bool:
        """Return True when a state is the TRAP (dead) state."""
        s = state or self.state
        return s == self.TRAP
