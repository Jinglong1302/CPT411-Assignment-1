from enum import Enum, auto


class State(Enum):
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
    EXACT_QUANTITY = "exact_quantity"
    PERCENTAGE = "percentage"
    ORDINAL = "ordinal"
    DATE = "date"
    QUANTITY_WITH_UNIT = "quantity_with_unit"


MONTHS = {
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
}


UNITS_AND_SCALES = {
    "litre",
    "litres",
    "liter",
    "liters",
    "cup",
    "cups",
    "million",
    "billion",
    "thousand",
    "kg",
    "g",
    "ml",
}
