from __future__ import annotations

from typing import Iterable

from src.app.models import TransitionStep
from src.core.dfa_engine import DFAEngine


STATE_NAMES: list[str] = [
    DFAEngine.START,
    DFAEngine.INT_1,
    DFAEngine.INT_2,
    DFAEngine.INT_3PLUS,
    DFAEngine.PERCENT,
    DFAEngine.ORD_S,
    DFAEngine.ORD_N,
    DFAEngine.ORD_R,
    DFAEngine.ORD_T,
    DFAEngine.ORD_DONE,
    DFAEngine.AFTER_INT_SPACE,
    DFAEngine.UNIT_G,
    DFAEngine.UNIT_K,
    DFAEngine.UNIT_KG,
    DFAEngine.UNIT_M,
    DFAEngine.UNIT_ML,
    DFAEngine.UNIT_C,
    DFAEngine.UNIT_CM,
    DFAEngine.UNIT_L,
    DFAEngine.DATE_SLASH_1,
    DFAEngine.DATE_MONTH_1,
    DFAEngine.DATE_MONTH_2,
    DFAEngine.DATE_SLASH_2,
    DFAEngine.DATE_YEAR_1,
    DFAEngine.DATE_YEAR_2,
    DFAEngine.DATE_YEAR_3,
    DFAEngine.DATE_YEAR_4,
    DFAEngine.TRAP,
    DFAEngine.M_J,
    DFAEngine.M_JA,
    DFAEngine.M_JAN,
    DFAEngine.M_JANU,
    DFAEngine.M_JANUA,
    DFAEngine.M_JANUAR,
    DFAEngine.M_JANUARY,
    DFAEngine.M_F,
    DFAEngine.M_FE,
    DFAEngine.M_FEB,
    DFAEngine.M_FEBR,
    DFAEngine.M_FEBRU,
    DFAEngine.M_FEBRUA,
    DFAEngine.M_FEBRUAR,
    DFAEngine.M_FEBRUARY,
    DFAEngine.M_M,
    DFAEngine.M_MA,
    DFAEngine.M_MAR,
    DFAEngine.M_MARC,
    DFAEngine.M_MARCH,
    DFAEngine.M_A,
    DFAEngine.M_AP,
    DFAEngine.M_APR,
    DFAEngine.M_APRI,
    DFAEngine.M_APRIL,
    DFAEngine.M_MAY,
    DFAEngine.M_JU,
    DFAEngine.M_JUN,
    DFAEngine.M_JUNE,
    DFAEngine.M_JUL,
    DFAEngine.M_JULY,
    DFAEngine.M_AU,
    DFAEngine.M_AUG,
    DFAEngine.M_AUGU,
    DFAEngine.M_AUGUS,
    DFAEngine.M_AUGUST,
    DFAEngine.M_S,
    DFAEngine.M_SE,
    DFAEngine.M_SEP,
    DFAEngine.M_SEPT,
    DFAEngine.M_SEPTE,
    DFAEngine.M_SEPTEM,
    DFAEngine.M_SEPTEMB,
    DFAEngine.M_SEPTEMBE,
    DFAEngine.M_SEPTEMBER,
    DFAEngine.M_O,
    DFAEngine.M_OC,
    DFAEngine.M_OCT,
    DFAEngine.M_OCTO,
    DFAEngine.M_OCTOB,
    DFAEngine.M_OCTOBE,
    DFAEngine.M_OCTOBER,
    DFAEngine.M_N,
    DFAEngine.M_NO,
    DFAEngine.M_NOV,
    DFAEngine.M_NOVE,
    DFAEngine.M_NOVEM,
    DFAEngine.M_NOVEMB,
    DFAEngine.M_NOVEMBE,
    DFAEngine.M_NOVEMBER,
    DFAEngine.M_D,
    DFAEngine.M_DE,
    DFAEngine.M_DEC,
    DFAEngine.M_DECE,
    DFAEngine.M_DECEM,
    DFAEngine.M_DECEMB,
    DFAEngine.M_DECEMBE,
    DFAEngine.M_DECEMBER,
    DFAEngine.MDY_SPACE1,
    DFAEngine.MDY_D1,
    DFAEngine.MDY_D2,
    DFAEngine.MDY_COMMA,
    DFAEngine.MDY_SPACE2,
    DFAEngine.MDY_Y1,
    DFAEngine.MDY_Y2,
    DFAEngine.MDY_Y3,
    DFAEngine.MDY_Y4,
]

ACCEPTING_STATES = {
    DFAEngine.INT_1,
    DFAEngine.INT_2,
    DFAEngine.INT_3PLUS,
    DFAEngine.PERCENT,
    DFAEngine.ORD_DONE,
    DFAEngine.UNIT_G,
    DFAEngine.UNIT_KG,
    DFAEngine.UNIT_ML,
    DFAEngine.UNIT_L,
    DFAEngine.UNIT_CM,
    DFAEngine.DATE_YEAR_4,
    DFAEngine.MDY_Y4,
}

STATE_POSITIONS: dict[str, tuple[int, int]] = {
    DFAEngine.START: (-980, 40),
    DFAEngine.INT_1: (-780, 40),
    DFAEngine.INT_2: (-590, 40),
    DFAEngine.INT_3PLUS: (-400, 40),
    DFAEngine.PERCENT: (-770, -220),
    DFAEngine.ORD_S: (-770, -70),
    DFAEngine.ORD_N: (-770, 80),
    DFAEngine.ORD_R: (-770, 230),
    DFAEngine.ORD_T: (-770, 380),
    DFAEngine.ORD_DONE: (-520, 180),
    DFAEngine.AFTER_INT_SPACE: (-400, 220),
    DFAEngine.UNIT_G: (-150, 260),
    DFAEngine.UNIT_K: (-320, 360),
    DFAEngine.UNIT_KG: (-80, 360),
    DFAEngine.UNIT_M: (120, 260),
    DFAEngine.UNIT_ML: (320, 260),
    DFAEngine.UNIT_C: (120, 410),
    DFAEngine.UNIT_CM: (320, 410),
    DFAEngine.UNIT_L: (520, 260),
    DFAEngine.DATE_SLASH_1: (-150, -150),
    DFAEngine.DATE_MONTH_1: (80, -150),
    DFAEngine.DATE_MONTH_2: (300, -150),
    DFAEngine.DATE_SLASH_2: (520, -150),
    DFAEngine.DATE_YEAR_1: (750, -150),
    DFAEngine.DATE_YEAR_2: (930, -150),
    DFAEngine.DATE_YEAR_3: (1110, -150),
    DFAEngine.DATE_YEAR_4: (1290, -150),
    DFAEngine.TRAP: (180, 100),
    DFAEngine.M_J: (-800, 600),
    DFAEngine.M_JA: (-650, 600),
    DFAEngine.M_JAN: (-500, 600),
    DFAEngine.M_JANU: (-350, 600),
    DFAEngine.M_JANUA: (-200, 600),
    DFAEngine.M_JANUAR: (-50, 600),
    DFAEngine.M_JANUARY: (100, 600),
    DFAEngine.M_F: (-800, 700),
    DFAEngine.M_FE: (-650, 700),
    DFAEngine.M_FEB: (-500, 700),
    DFAEngine.M_FEBR: (-350, 700),
    DFAEngine.M_FEBRU: (-200, 700),
    DFAEngine.M_FEBRUA: (-50, 700),
    DFAEngine.M_FEBRUAR: (100, 700),
    DFAEngine.M_FEBRUARY: (250, 700),
    DFAEngine.M_M: (-800, 800),
    DFAEngine.M_MA: (-650, 800),
    DFAEngine.M_MAR: (-500, 800),
    DFAEngine.M_MARC: (-350, 800),
    DFAEngine.M_MARCH: (-200, 800),
    DFAEngine.M_A: (-800, 900),
    DFAEngine.M_AP: (-650, 900),
    DFAEngine.M_APR: (-500, 900),
    DFAEngine.M_APRI: (-350, 900),
    DFAEngine.M_APRIL: (-200, 900),
    DFAEngine.M_M: (-800, 1000),
    DFAEngine.M_MA: (-650, 1000),
    DFAEngine.M_MAY: (-500, 1000),
    DFAEngine.M_J: (-800, 1100),
    DFAEngine.M_JU: (-650, 1100),
    DFAEngine.M_JUN: (-500, 1100),
    DFAEngine.M_JUNE: (-350, 1100),
    DFAEngine.M_J: (-800, 1200),
    DFAEngine.M_JU: (-650, 1200),
    DFAEngine.M_JUL: (-500, 1200),
    DFAEngine.M_JULY: (-350, 1200),
    DFAEngine.M_A: (-800, 1300),
    DFAEngine.M_AU: (-650, 1300),
    DFAEngine.M_AUG: (-500, 1300),
    DFAEngine.M_AUGU: (-350, 1300),
    DFAEngine.M_AUGUS: (-200, 1300),
    DFAEngine.M_AUGUST: (-50, 1300),
    DFAEngine.M_S: (-800, 1400),
    DFAEngine.M_SE: (-650, 1400),
    DFAEngine.M_SEP: (-500, 1400),
    DFAEngine.M_SEPT: (-350, 1400),
    DFAEngine.M_SEPTE: (-200, 1400),
    DFAEngine.M_SEPTEM: (-50, 1400),
    DFAEngine.M_SEPTEMB: (100, 1400),
    DFAEngine.M_SEPTEMBE: (250, 1400),
    DFAEngine.M_SEPTEMBER: (400, 1400),
    DFAEngine.M_O: (-800, 1500),
    DFAEngine.M_OC: (-650, 1500),
    DFAEngine.M_OCT: (-500, 1500),
    DFAEngine.M_OCTO: (-350, 1500),
    DFAEngine.M_OCTOB: (-200, 1500),
    DFAEngine.M_OCTOBE: (-50, 1500),
    DFAEngine.M_OCTOBER: (100, 1500),
    DFAEngine.M_N: (-800, 1600),
    DFAEngine.M_NO: (-650, 1600),
    DFAEngine.M_NOV: (-500, 1600),
    DFAEngine.M_NOVE: (-350, 1600),
    DFAEngine.M_NOVEM: (-200, 1600),
    DFAEngine.M_NOVEMB: (-50, 1600),
    DFAEngine.M_NOVEMBE: (100, 1600),
    DFAEngine.M_NOVEMBER: (250, 1600),
    DFAEngine.M_D: (-800, 1700),
    DFAEngine.M_DE: (-650, 1700),
    DFAEngine.M_DEC: (-500, 1700),
    DFAEngine.M_DECE: (-350, 1700),
    DFAEngine.M_DECEM: (-200, 1700),
    DFAEngine.M_DECEMB: (-50, 1700),
    DFAEngine.M_DECEMBE: (100, 1700),
    DFAEngine.M_DECEMBER: (250, 1700),
    DFAEngine.MDY_SPACE1: (1000, 1150),
    DFAEngine.MDY_D1: (1150, 1150),
    DFAEngine.MDY_D2: (1300, 1150),
    DFAEngine.MDY_COMMA: (1450, 1150),
    DFAEngine.MDY_SPACE2: (1600, 1150),
    DFAEngine.MDY_Y1: (1750, 1150),
    DFAEngine.MDY_Y2: (1900, 1150),
    DFAEngine.MDY_Y3: (2050, 1150),
    DFAEngine.MDY_Y4: (2200, 1150),
}


def _node_color(state_name: str, current_state_name: str | None, visited: set[str]) -> str:
    if state_name == current_state_name:
        return "#ffcc80"
    if state_name in visited:
        return "#bbdefb"
    if state_name == DFAEngine.TRAP:
        return "#ffcdd2"
    return "#e8f5e9"


def _node_shape(state_name: str) -> str:
    return "dot" if state_name in ACCEPTING_STATES else "ellipse"


def _node_border_width(state_name: str, current_state_name: str | None) -> int:
    if state_name == current_state_name:
        return 4
    if state_name in ACCEPTING_STATES:
        return 2
    return 1


def _edge_color(pair: tuple[str, str], traversed: set[tuple[str, str]]) -> str:
    return "#e53935" if pair in traversed else "#9e9e9e"


def _base_edges() -> list[tuple[str, str, str]]:
    return [
        (DFAEngine.START, DFAEngine.INT_1, "digit"),
        (DFAEngine.INT_1, DFAEngine.INT_2, "digit"),
        (DFAEngine.INT_2, DFAEngine.INT_3PLUS, "digit"),
        (DFAEngine.INT_1, DFAEngine.PERCENT, "%"),
        (DFAEngine.INT_2, DFAEngine.PERCENT, "%"),
        (DFAEngine.INT_3PLUS, DFAEngine.PERCENT, "%"),
        (DFAEngine.INT_1, DFAEngine.ORD_S, "s,S"),
        (DFAEngine.INT_1, DFAEngine.ORD_N, "n,N"),
        (DFAEngine.INT_1, DFAEngine.ORD_R, "r,R"),
        (DFAEngine.INT_1, DFAEngine.ORD_T, "t,T"),
        (DFAEngine.INT_2, DFAEngine.ORD_S, "s,S"),
        (DFAEngine.INT_2, DFAEngine.ORD_N, "n,N"),
        (DFAEngine.INT_2, DFAEngine.ORD_R, "r,R"),
        (DFAEngine.INT_2, DFAEngine.ORD_T, "t,T"),
        (DFAEngine.INT_3PLUS, DFAEngine.ORD_S, "s,S"),
        (DFAEngine.INT_3PLUS, DFAEngine.ORD_N, "n,N"),
        (DFAEngine.INT_3PLUS, DFAEngine.ORD_R, "r,R"),
        (DFAEngine.INT_3PLUS, DFAEngine.ORD_T, "t,T"),
        (DFAEngine.INT_1, DFAEngine.AFTER_INT_SPACE, "space"),
        (DFAEngine.INT_2, DFAEngine.AFTER_INT_SPACE, "space"),
        (DFAEngine.INT_3PLUS, DFAEngine.AFTER_INT_SPACE, "space"),
        (DFAEngine.ORD_S, DFAEngine.ORD_DONE, "t,T"),
        (DFAEngine.ORD_N, DFAEngine.ORD_DONE, "d,D"),
        (DFAEngine.ORD_R, DFAEngine.ORD_DONE, "d,D"),
        (DFAEngine.ORD_T, DFAEngine.ORD_DONE, "h,H"),
        (DFAEngine.AFTER_INT_SPACE, DFAEngine.UNIT_G, "g,G"),
        (DFAEngine.AFTER_INT_SPACE, DFAEngine.UNIT_K, "k,K"),
        (DFAEngine.UNIT_K, DFAEngine.UNIT_KG, "g,G"),
        (DFAEngine.AFTER_INT_SPACE, DFAEngine.UNIT_M, "m,M"),
        (DFAEngine.UNIT_M, DFAEngine.UNIT_ML, "l,L"),
        (DFAEngine.AFTER_INT_SPACE, DFAEngine.UNIT_C, "c,C"),
        (DFAEngine.UNIT_C, DFAEngine.UNIT_CM, "m,M"),
        (DFAEngine.AFTER_INT_SPACE, DFAEngine.UNIT_L, "L,l"),
        (DFAEngine.INT_1, DFAEngine.DATE_SLASH_1, "/"),
        (DFAEngine.DATE_SLASH_1, DFAEngine.DATE_MONTH_1, "digit"),
        (DFAEngine.DATE_MONTH_1, DFAEngine.DATE_MONTH_2, "digit"),
        (DFAEngine.DATE_MONTH_1, DFAEngine.DATE_SLASH_2, "/"),
        (DFAEngine.DATE_MONTH_2, DFAEngine.DATE_SLASH_2, "/"),
        (DFAEngine.DATE_SLASH_2, DFAEngine.DATE_YEAR_1, "digit"),
        (DFAEngine.DATE_YEAR_1, DFAEngine.DATE_YEAR_2, "digit"),
        (DFAEngine.DATE_YEAR_2, DFAEngine.DATE_YEAR_3, "digit"),
        (DFAEngine.DATE_YEAR_3, DFAEngine.DATE_YEAR_4, "digit"),
        (DFAEngine.START, DFAEngine.M_J, "j,J"),
        (DFAEngine.START, DFAEngine.M_F, "f,F"),
        (DFAEngine.START, DFAEngine.M_M, "m,M"),
        (DFAEngine.START, DFAEngine.M_A, "a,A"),
        (DFAEngine.START, DFAEngine.M_S, "s,S"),
        (DFAEngine.START, DFAEngine.M_O, "o,O"),
        (DFAEngine.START, DFAEngine.M_N, "n,N"),
        (DFAEngine.START, DFAEngine.M_D, "d,D"),
        (DFAEngine.M_J, DFAEngine.M_JA, "a,A"),
        (DFAEngine.M_J, DFAEngine.M_JU, "u,U"),
        (DFAEngine.M_JA, DFAEngine.M_JAN, "n,N"),
        (DFAEngine.M_JAN, DFAEngine.M_JANU, "u,U"),
        (DFAEngine.M_JANU, DFAEngine.M_JANUA, "a,A"),
        (DFAEngine.M_JANUA, DFAEngine.M_JANUAR, "r,R"),
        (DFAEngine.M_JANUAR, DFAEngine.M_JANUARY, "y,Y"),
        (DFAEngine.M_JANUARY, DFAEngine.MDY_SPACE1, "space"),
        (DFAEngine.M_F, DFAEngine.M_FE, "e,E"),
        (DFAEngine.M_FE, DFAEngine.M_FEB, "b,B"),
        (DFAEngine.M_FEB, DFAEngine.M_FEBR, "r,R"),
        (DFAEngine.M_FEBR, DFAEngine.M_FEBRU, "u,U"),
        (DFAEngine.M_FEBRU, DFAEngine.M_FEBRUA, "a,A"),
        (DFAEngine.M_FEBRUA, DFAEngine.M_FEBRUAR, "r,R"),
        (DFAEngine.M_FEBRUAR, DFAEngine.M_FEBRUARY, "y,Y"),
        (DFAEngine.M_FEBRUARY, DFAEngine.MDY_SPACE1, "space"),
        (DFAEngine.M_M, DFAEngine.M_MA, "a,A"),
        (DFAEngine.M_MA, DFAEngine.M_MAR, "r,R"),
        (DFAEngine.M_MA, DFAEngine.M_MAY, "y,Y"),
        (DFAEngine.M_MAR, DFAEngine.M_MARC, "c,C"),
        (DFAEngine.M_MARC, DFAEngine.M_MARCH, "h,H"),
        (DFAEngine.M_MARCH, DFAEngine.MDY_SPACE1, "space"),
        (DFAEngine.M_A, DFAEngine.M_AP, "p,P"),
        (DFAEngine.M_A, DFAEngine.M_AU, "u,U"),
        (DFAEngine.M_AP, DFAEngine.M_APR, "r,R"),
        (DFAEngine.M_APR, DFAEngine.M_APRI, "i,I"),
        (DFAEngine.M_APRI, DFAEngine.M_APRIL, "l,L"),
        (DFAEngine.M_APRIL, DFAEngine.MDY_SPACE1, "space"),
        (DFAEngine.M_MAY, DFAEngine.MDY_SPACE1, "space"),
        (DFAEngine.M_JU, DFAEngine.M_JUN, "n,N"),
        (DFAEngine.M_JU, DFAEngine.M_JUL, "l,L"),
        (DFAEngine.M_JUN, DFAEngine.M_JUNE, "e,E"),
        (DFAEngine.M_JUNE, DFAEngine.MDY_SPACE1, "space"),
        (DFAEngine.M_JUL, DFAEngine.M_JULY, "y,Y"),
        (DFAEngine.M_JULY, DFAEngine.MDY_SPACE1, "space"),
        (DFAEngine.M_AU, DFAEngine.M_AUG, "g,G"),
        (DFAEngine.M_AUG, DFAEngine.M_AUGU, "u,U"),
        (DFAEngine.M_AUGU, DFAEngine.M_AUGUS, "s,S"),
        (DFAEngine.M_AUGUS, DFAEngine.M_AUGUST, "t,T"),
        (DFAEngine.M_AUGUST, DFAEngine.MDY_SPACE1, "space"),
        (DFAEngine.M_S, DFAEngine.M_SE, "e,E"),
        (DFAEngine.M_SE, DFAEngine.M_SEP, "p,P"),
        (DFAEngine.M_SEP, DFAEngine.M_SEPT, "t,T"),
        (DFAEngine.M_SEPT, DFAEngine.M_SEPTE, "e,E"),
        (DFAEngine.M_SEPTE, DFAEngine.M_SEPTEM, "m,M"),
        (DFAEngine.M_SEPTEM, DFAEngine.M_SEPTEMB, "b,B"),
        (DFAEngine.M_SEPTEMB, DFAEngine.M_SEPTEMBE, "e,E"),
        (DFAEngine.M_SEPTEMBE, DFAEngine.M_SEPTEMBER, "r,R"),
        (DFAEngine.M_SEPTEMBER, DFAEngine.MDY_SPACE1, "space"),
        (DFAEngine.M_O, DFAEngine.M_OC, "c,C"),
        (DFAEngine.M_OC, DFAEngine.M_OCT, "t,T"),
        (DFAEngine.M_OCT, DFAEngine.M_OCTO, "o,O"),
        (DFAEngine.M_OCTO, DFAEngine.M_OCTOB, "b,B"),
        (DFAEngine.M_OCTOB, DFAEngine.M_OCTOBE, "e,E"),
        (DFAEngine.M_OCTOBE, DFAEngine.M_OCTOBER, "r,R"),
        (DFAEngine.M_OCTOBER, DFAEngine.MDY_SPACE1, "space"),
        (DFAEngine.M_N, DFAEngine.M_NO, "o,O"),
        (DFAEngine.M_NO, DFAEngine.M_NOV, "v,V"),
        (DFAEngine.M_NOV, DFAEngine.M_NOVE, "e,E"),
        (DFAEngine.M_NOVE, DFAEngine.M_NOVEM, "m,M"),
        (DFAEngine.M_NOVEM, DFAEngine.M_NOVEMB, "b,B"),
        (DFAEngine.M_NOVEMB, DFAEngine.M_NOVEMBE, "e,E"),
        (DFAEngine.M_NOVEMBE, DFAEngine.M_NOVEMBER, "r,R"),
        (DFAEngine.M_NOVEMBER, DFAEngine.MDY_SPACE1, "space"),
        (DFAEngine.M_D, DFAEngine.M_DE, "e,E"),
        (DFAEngine.M_DE, DFAEngine.M_DEC, "c,C"),
        (DFAEngine.M_DEC, DFAEngine.M_DECE, "e,E"),
        (DFAEngine.M_DECE, DFAEngine.M_DECEM, "m,M"),
        (DFAEngine.M_DECEM, DFAEngine.M_DECEMB, "b,B"),
        (DFAEngine.M_DECEMB, DFAEngine.M_DECEMBE, "e,E"),
        (DFAEngine.M_DECEMBE, DFAEngine.M_DECEMBER, "r,R"),
        (DFAEngine.M_DECEMBER, DFAEngine.MDY_SPACE1, "space"),
        (DFAEngine.MDY_SPACE1, DFAEngine.MDY_D1, "digit"),
        (DFAEngine.MDY_D1, DFAEngine.MDY_D2, "digit"),
        (DFAEngine.MDY_D1, DFAEngine.MDY_COMMA, ","),
        (DFAEngine.MDY_D2, DFAEngine.MDY_COMMA, ","),
        (DFAEngine.MDY_COMMA, DFAEngine.MDY_SPACE2, "space"),
        (DFAEngine.MDY_SPACE2, DFAEngine.MDY_Y1, "digit"),
        (DFAEngine.MDY_Y1, DFAEngine.MDY_Y2, "digit"),
        (DFAEngine.MDY_Y2, DFAEngine.MDY_Y3, "digit"),
        (DFAEngine.MDY_Y3, DFAEngine.MDY_Y4, "digit"),
    ]


def _trap_hint_sources() -> list[str]:
    return [state for state in STATE_NAMES if state != DFAEngine.TRAP]


def render_state_diagram_html(
    trace: Iterable[TransitionStep],
    current_step: int,
    width: str = "100%",
    height: str = "540px",
) -> str:
    try:
        from pyvis.network import Network
    except ImportError:
        import sys

        python_exe = sys.executable.replace("\\\\", "\\\\\\\\")
        return (
            "<div style='font-size:14px;'>"
            "<p><b>Interactive graph unavailable:</b> pyvis is not installed in the Python interpreter used by Streamlit.</p>"
            f"<p>Current interpreter: <code>{python_exe}</code></p>"
            f"<p>Install with: <code>\"{python_exe}\" -m pip install pyvis</code></p>"
            "</div>"
        )

    trace_list = list(trace)
    step_prefix = trace_list[:current_step]

    visited_states: set[str] = {DFAEngine.START}
    traversed_pairs: set[tuple[str, str]] = set()
    current_state = DFAEngine.START

    for step in step_prefix:
        visited_states.add(step.to_state)
        traversed_pairs.add((step.from_state, step.to_state))
        current_state = step.to_state

    network = Network(height=height, width=width, directed=True, bgcolor="#ffffff", font_color="#222222")
    network.set_options(
        """
        var options = {
            "physics": {"enabled": false},
            "interaction": {
                "dragNodes": false,
                "zoomView": true,
                "dragView": true
            },
            "layout": {"improvedLayout": false},
            "edges": {
                "font": {
                    "align": "top",
                    "size": 10
                },
                "smooth": {
                    "enabled": true,
                    "type": "curvedCW",
                    "roundness": 0.14
                }
            }
        }
        """
    )

    for state_name in ACCEPTING_STATES:
        if state_name not in STATE_POSITIONS: continue
        pos_x, pos_y = STATE_POSITIONS[state_name]
        network.add_node(
            f"ring_{state_name}",
            label=" ",
            color={"background": "rgba(0,0,0,0)", "border": "#455a64"},
            shape="dot",
            size=34,
            x=pos_x,
            y=pos_y,
            physics=False,
            fixed={"x": True, "y": True},
            selectable=False,
            title="",
            font={"size": 1, "color": "rgba(0,0,0,0)"},
        )

    for state_name in STATE_NAMES:
        if state_name not in STATE_POSITIONS: continue
        pos_x, pos_y = STATE_POSITIONS[state_name]
        title_text = f"State: {state_name}"
        if state_name == DFAEngine.DATE_YEAR_4 or state_name == DFAEngine.MDY_Y4:
            title_text += "\\nAccepts only if the year has exactly 4 digits."
        
        is_acc = state_name in ACCEPTING_STATES
        network.add_node(
            state_name,
            label=state_name,
            color=_node_color(state_name, current_state, visited_states),
            shape="dot" if is_acc else "ellipse",
            borderWidth=_node_border_width(state_name, current_state) if not is_acc else 2,
            title=title_text,
            x=pos_x,
            y=pos_y,
            physics=False,
            fixed={"x": True, "y": True},
            size=24 if is_acc else 20,
        )

    base_edges = _base_edges()
    
    for source, target, label in base_edges:
        pair = (source, target)
        network.add_edge(
            source,
            target,
            label=label,
            color=_edge_color(pair, traversed_pairs),
            width=4 if pair in traversed_pairs else 1,
            arrows="to",
        )

    for step in step_prefix:
        pair = (step.from_state, step.to_state)
        if pair[1] == DFAEngine.TRAP:
            network.add_edge(
                pair[0],
                pair[1],
                label=f"'{step.char}'",
                color="#d32f2f",
                width=4,
                arrows="to",
            )

    return network.generate_html(notebook=False)
