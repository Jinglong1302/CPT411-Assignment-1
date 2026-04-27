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

    # Text Date states
    M_J = "M_J"
    M_JA = "M_JA"
    M_JAN = "M_JAN"
    M_JANU = "M_JANU"
    M_JANUA = "M_JANUA"
    M_JANUAR = "M_JANUAR"
    M_JANUARY = "M_JANUARY"
    M_F = "M_F"
    M_FE = "M_FE"
    M_FEB = "M_FEB"
    M_FEBR = "M_FEBR"
    M_FEBRU = "M_FEBRU"
    M_FEBRUA = "M_FEBRUA"
    M_FEBRUAR = "M_FEBRUAR"
    M_FEBRUARY = "M_FEBRUARY"
    M_M = "M_M"
    M_MA = "M_MA"
    M_MAR = "M_MAR"
    M_MARC = "M_MARC"
    M_MARCH = "M_MARCH"
    M_A = "M_A"
    M_AP = "M_AP"
    M_APR = "M_APR"
    M_APRI = "M_APRI"
    M_APRIL = "M_APRIL"
    M_MAY = "M_MAY"
    M_JU = "M_JU"
    M_JUN = "M_JUN"
    M_JUNE = "M_JUNE"
    M_JUL = "M_JUL"
    M_JULY = "M_JULY"
    M_AU = "M_AU"
    M_AUG = "M_AUG"
    M_AUGU = "M_AUGU"
    M_AUGUS = "M_AUGUS"
    M_AUGUST = "M_AUGUST"
    M_S = "M_S"
    M_SE = "M_SE"
    M_SEP = "M_SEP"
    M_SEPT = "M_SEPT"
    M_SEPTE = "M_SEPTE"
    M_SEPTEM = "M_SEPTEM"
    M_SEPTEMB = "M_SEPTEMB"
    M_SEPTEMBE = "M_SEPTEMBE"
    M_SEPTEMBER = "M_SEPTEMBER"
    M_O = "M_O"
    M_OC = "M_OC"
    M_OCT = "M_OCT"
    M_OCTO = "M_OCTO"
    M_OCTOB = "M_OCTOB"
    M_OCTOBE = "M_OCTOBE"
    M_OCTOBER = "M_OCTOBER"
    M_N = "M_N"
    M_NO = "M_NO"
    M_NOV = "M_NOV"
    M_NOVE = "M_NOVE"
    M_NOVEM = "M_NOVEM"
    M_NOVEMB = "M_NOVEMB"
    M_NOVEMBE = "M_NOVEMBE"
    M_NOVEMBER = "M_NOVEMBER"
    M_D = "M_D"
    M_DE = "M_DE"
    M_DEC = "M_DEC"
    M_DECE = "M_DECE"
    M_DECEM = "M_DECEM"
    M_DECEMB = "M_DECEMB"
    M_DECEMBE = "M_DECEMBE"
    M_DECEMBER = "M_DECEMBER"
    MDY_SPACE1 = "MDY_SPACE1"
    MDY_D1 = "MDY_D1"
    MDY_D2 = "MDY_D2"
    MDY_COMMA = "MDY_COMMA"
    MDY_SPACE2 = "MDY_SPACE2"
    MDY_Y1 = "MDY_Y1"
    MDY_Y2 = "MDY_Y2"
    MDY_Y3 = "MDY_Y3"
    MDY_Y4 = "MDY_Y4"

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
            elif ch in ("j", "J"):
                self.state = self.M_J
            elif ch in ("f", "F"):
                self.state = self.M_F
            elif ch in ("m", "M"):
                self.state = self.M_M
            elif ch in ("a", "A"):
                self.state = self.M_A
            elif ch in ("s", "S"):
                self.state = self.M_S
            elif ch in ("o", "O"):
                self.state = self.M_O
            elif ch in ("n", "N"):
                self.state = self.M_N
            elif ch in ("d", "D"):
                self.state = self.M_D
            else:
                self.state = self.TRAP
            return self.state

        if s == self.INT_1:
            if ch.isdigit():
                self.state = self.INT_2
            elif ch == "%":
                self.state = self.PERCENT
            elif ch in ("s", "S"):
                self.state = self.ORD_S
            elif ch in ("n", "N"):
                self.state = self.ORD_N
            elif ch in ("r", "R"):
                self.state = self.ORD_R
            elif ch in ("t", "T"):
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
            elif ch in ("s", "S"):
                self.state = self.ORD_S
            elif ch in ("n", "N"):
                self.state = self.ORD_N
            elif ch in ("r", "R"):
                self.state = self.ORD_R
            elif ch in ("t", "T"):
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
            elif ch in ("s", "S"):
                self.state = self.ORD_S
            elif ch in ("n", "N"):
                self.state = self.ORD_N
            elif ch in ("r", "R"):
                self.state = self.ORD_R
            elif ch in ("t", "T"):
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
            self.state = self.ORD_DONE if ch in ("t", "T") else self.TRAP
            return self.state

        if s == self.ORD_N:
            self.state = self.ORD_DONE if ch in ("d", "D") else self.TRAP
            return self.state

        if s == self.ORD_R:
            self.state = self.ORD_DONE if ch in ("d", "D") else self.TRAP
            return self.state

        if s == self.ORD_T:
            self.state = self.ORD_DONE if ch in ("h", "H") else self.TRAP
            return self.state

        if s == self.ORD_DONE:
            self.state = self.TRAP
            return self.state

        if s == self.AFTER_INT_SPACE:
            if ch in ("g", "G"):
                self.state = self.UNIT_G
            elif ch in ("k", "K"):
                self.state = self.UNIT_K
            elif ch in ("m", "M"):
                self.state = self.UNIT_M
            elif ch in ("c", "C"):
                self.state = self.UNIT_C
            elif ch in ("l", "L"):
                self.state = self.UNIT_L
            else:
                self.state = self.TRAP
            return self.state

        if s == self.UNIT_K:
            self.state = self.UNIT_KG if ch in ("g", "G") else self.TRAP
            return self.state

        if s == self.UNIT_M:
            self.state = self.UNIT_ML if ch in ("l", "L") else self.TRAP
            return self.state

        if s == self.UNIT_C:
            self.state = self.UNIT_CM if ch in ("m", "M") else self.TRAP
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

        if s == self.M_J:
            if ch in ("a", "A"):
                self.state = self.M_JA
            elif ch in ("u", "U"):
                self.state = self.M_JU
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_JA:
            if ch in ("n", "N"):
                self.state = self.M_JAN
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_JAN:
            if ch in ("u", "U"):
                self.state = self.M_JANU
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_JANU:
            if ch in ("a", "A"):
                self.state = self.M_JANUA
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_JANUA:
            if ch in ("r", "R"):
                self.state = self.M_JANUAR
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_JANUAR:
            if ch in ("y", "Y"):
                self.state = self.M_JANUARY
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_JANUARY:
            if ch == " ":
                self.state = self.MDY_SPACE1
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_F:
            if ch in ("e", "E"):
                self.state = self.M_FE
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_FE:
            if ch in ("b", "B"):
                self.state = self.M_FEB
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_FEB:
            if ch in ("r", "R"):
                self.state = self.M_FEBR
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_FEBR:
            if ch in ("u", "U"):
                self.state = self.M_FEBRU
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_FEBRU:
            if ch in ("a", "A"):
                self.state = self.M_FEBRUA
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_FEBRUA:
            if ch in ("r", "R"):
                self.state = self.M_FEBRUAR
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_FEBRUAR:
            if ch in ("y", "Y"):
                self.state = self.M_FEBRUARY
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_FEBRUARY:
            if ch == " ":
                self.state = self.MDY_SPACE1
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_M:
            if ch in ("a", "A"):
                self.state = self.M_MA
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_MA:
            if ch in ("r", "R"):
                self.state = self.M_MAR
            elif ch in ("y", "Y"):
                self.state = self.M_MAY
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_MAR:
            if ch in ("c", "C"):
                self.state = self.M_MARC
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_MARC:
            if ch in ("h", "H"):
                self.state = self.M_MARCH
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_MARCH:
            if ch == " ":
                self.state = self.MDY_SPACE1
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_A:
            if ch in ("p", "P"):
                self.state = self.M_AP
            elif ch in ("u", "U"):
                self.state = self.M_AU
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_AP:
            if ch in ("r", "R"):
                self.state = self.M_APR
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_APR:
            if ch in ("i", "I"):
                self.state = self.M_APRI
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_APRI:
            if ch in ("l", "L"):
                self.state = self.M_APRIL
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_APRIL:
            if ch == " ":
                self.state = self.MDY_SPACE1
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_MAY:
            if ch == " ":
                self.state = self.MDY_SPACE1
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_JU:
            if ch in ("n", "N"):
                self.state = self.M_JUN
            elif ch in ("l", "L"):
                self.state = self.M_JUL
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_JUN:
            if ch in ("e", "E"):
                self.state = self.M_JUNE
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_JUNE:
            if ch == " ":
                self.state = self.MDY_SPACE1
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_JUL:
            if ch in ("y", "Y"):
                self.state = self.M_JULY
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_JULY:
            if ch == " ":
                self.state = self.MDY_SPACE1
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_AU:
            if ch in ("g", "G"):
                self.state = self.M_AUG
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_AUG:
            if ch in ("u", "U"):
                self.state = self.M_AUGU
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_AUGU:
            if ch in ("s", "S"):
                self.state = self.M_AUGUS
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_AUGUS:
            if ch in ("t", "T"):
                self.state = self.M_AUGUST
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_AUGUST:
            if ch == " ":
                self.state = self.MDY_SPACE1
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_S:
            if ch in ("e", "E"):
                self.state = self.M_SE
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_SE:
            if ch in ("p", "P"):
                self.state = self.M_SEP
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_SEP:
            if ch in ("t", "T"):
                self.state = self.M_SEPT
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_SEPT:
            if ch in ("e", "E"):
                self.state = self.M_SEPTE
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_SEPTE:
            if ch in ("m", "M"):
                self.state = self.M_SEPTEM
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_SEPTEM:
            if ch in ("b", "B"):
                self.state = self.M_SEPTEMB
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_SEPTEMB:
            if ch in ("e", "E"):
                self.state = self.M_SEPTEMBE
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_SEPTEMBE:
            if ch in ("r", "R"):
                self.state = self.M_SEPTEMBER
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_SEPTEMBER:
            if ch == " ":
                self.state = self.MDY_SPACE1
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_O:
            if ch in ("c", "C"):
                self.state = self.M_OC
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_OC:
            if ch in ("t", "T"):
                self.state = self.M_OCT
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_OCT:
            if ch in ("o", "O"):
                self.state = self.M_OCTO
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_OCTO:
            if ch in ("b", "B"):
                self.state = self.M_OCTOB
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_OCTOB:
            if ch in ("e", "E"):
                self.state = self.M_OCTOBE
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_OCTOBE:
            if ch in ("r", "R"):
                self.state = self.M_OCTOBER
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_OCTOBER:
            if ch == " ":
                self.state = self.MDY_SPACE1
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_N:
            if ch in ("o", "O"):
                self.state = self.M_NO
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_NO:
            if ch in ("v", "V"):
                self.state = self.M_NOV
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_NOV:
            if ch in ("e", "E"):
                self.state = self.M_NOVE
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_NOVE:
            if ch in ("m", "M"):
                self.state = self.M_NOVEM
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_NOVEM:
            if ch in ("b", "B"):
                self.state = self.M_NOVEMB
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_NOVEMB:
            if ch in ("e", "E"):
                self.state = self.M_NOVEMBE
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_NOVEMBE:
            if ch in ("r", "R"):
                self.state = self.M_NOVEMBER
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_NOVEMBER:
            if ch == " ":
                self.state = self.MDY_SPACE1
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_D:
            if ch in ("e", "E"):
                self.state = self.M_DE
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_DE:
            if ch in ("c", "C"):
                self.state = self.M_DEC
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_DEC:
            if ch in ("e", "E"):
                self.state = self.M_DECE
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_DECE:
            if ch in ("m", "M"):
                self.state = self.M_DECEM
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_DECEM:
            if ch in ("b", "B"):
                self.state = self.M_DECEMB
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_DECEMB:
            if ch in ("e", "E"):
                self.state = self.M_DECEMBE
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_DECEMBE:
            if ch in ("r", "R"):
                self.state = self.M_DECEMBER
            else:
                self.state = self.TRAP
            return self.state

        if s == self.M_DECEMBER:
            if ch == " ":
                self.state = self.MDY_SPACE1
            else:
                self.state = self.TRAP
            return self.state


        if s == self.MDY_SPACE1:
            self.state = self.MDY_D1 if ch.isdigit() else self.TRAP
            return self.state

        if s == self.MDY_D1:
            if ch.isdigit():
                self.state = self.MDY_D2
            elif ch == ",":
                self.state = self.MDY_COMMA
            else:
                self.state = self.TRAP
            return self.state

        if s == self.MDY_D2:
            self.state = self.MDY_COMMA if ch == "," else self.TRAP
            return self.state

        if s == self.MDY_COMMA:
            self.state = self.MDY_SPACE2 if ch == " " else self.TRAP
            return self.state

        if s == self.MDY_SPACE2:
            self.state = self.MDY_Y1 if ch.isdigit() else self.TRAP
            return self.state

        if s == self.MDY_Y1:
            self.state = self.MDY_Y2 if ch.isdigit() else self.TRAP
            return self.state

        if s == self.MDY_Y2:
            self.state = self.MDY_Y3 if ch.isdigit() else self.TRAP
            return self.state

        if s == self.MDY_Y3:
            self.state = self.MDY_Y4 if ch.isdigit() else self.TRAP
            return self.state

        if s == self.MDY_Y4:
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
        if s in {self.DATE_YEAR_4, self.MDY_Y4}:
            return Category.DATE
        return None

    def is_trap(self, state: str | None = None) -> bool:
        """Return True when a state is the TRAP (dead) state."""
        s = state or self.state
        return s == self.TRAP
