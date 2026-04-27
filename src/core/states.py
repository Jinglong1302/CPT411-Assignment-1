from enum import Enum, auto


class State(Enum):
    """Legacy DFA state enum retained for compatibility and references."""

    START = auto()
    INT = auto()
    PERCENT = auto()
    ORD_S = auto()
    ORD_N = auto()
    ORD_R = auto()
    ORD_T = auto()
    ORD_DONE = auto()
    AFTER_INT_SPACE = auto()
    WORD = auto()
    AFTER_WORD = auto()
    DATE_YEAR = auto()
    TRAP = auto()


class Category(Enum):
    """Semantic categories assigned to accepted patterns."""

    EXACT_QUANTITY = "exact_quantity"
    PERCENTAGE = "percentage"
    ORDINAL = "ordinal"
    DATE = "date"
    QUANTITY_WITH_UNIT = "quantity_with_unit"

