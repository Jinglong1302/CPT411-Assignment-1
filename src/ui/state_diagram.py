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
}


def _node_color(state_name: str, current_state_name: str | None, visited: set[str]) -> str:
    """Choose node color based on current, visited, and trap-state status."""
    if state_name == current_state_name:
        return "#ffcc80"
    if state_name in visited:
        return "#bbdefb"
    if state_name == DFAEngine.TRAP:
        return "#ffcdd2"
    return "#e8f5e9"


def _node_shape(state_name: str) -> str:
    """Return graph node shape, using a dot for accepting states."""
    return "dot" if state_name in ACCEPTING_STATES else "ellipse"


def _node_border_width(state_name: str, current_state_name: str | None) -> int:
    """Set border thickness to emphasize current and accepting states."""
    if state_name == current_state_name:
        return 4
    if state_name in ACCEPTING_STATES:
        return 2
    return 1


def _edge_color(pair: tuple[str, str], traversed: set[tuple[str, str]]) -> str:
    """Color traversed edges differently from non-traversed edges."""
    return "#e53935" if pair in traversed else "#9e9e9e"


def _base_edges() -> list[tuple[str, str, str]]:
    """Return canonical DFA transitions and labels for static diagram rendering."""
    return [
        (DFAEngine.START, DFAEngine.INT_1, "digit"),
        (DFAEngine.INT_1, DFAEngine.INT_2, "digit"),
        (DFAEngine.INT_2, DFAEngine.INT_3PLUS, "digit"),
        (DFAEngine.INT_1, DFAEngine.PERCENT, "%"),
        (DFAEngine.INT_2, DFAEngine.PERCENT, "%"),
        (DFAEngine.INT_3PLUS, DFAEngine.PERCENT, "%"),
        (DFAEngine.INT_1, DFAEngine.ORD_S, "s"),
        (DFAEngine.INT_1, DFAEngine.ORD_N, "n"),
        (DFAEngine.INT_1, DFAEngine.ORD_R, "r"),
        (DFAEngine.INT_1, DFAEngine.ORD_T, "t"),
        (DFAEngine.INT_2, DFAEngine.ORD_S, "s"),
        (DFAEngine.INT_2, DFAEngine.ORD_N, "n"),
        (DFAEngine.INT_2, DFAEngine.ORD_R, "r"),
        (DFAEngine.INT_2, DFAEngine.ORD_T, "t"),
        (DFAEngine.INT_3PLUS, DFAEngine.ORD_S, "s"),
        (DFAEngine.INT_3PLUS, DFAEngine.ORD_N, "n"),
        (DFAEngine.INT_3PLUS, DFAEngine.ORD_R, "r"),
        (DFAEngine.INT_3PLUS, DFAEngine.ORD_T, "t"),
        (DFAEngine.INT_1, DFAEngine.AFTER_INT_SPACE, "space"),
        (DFAEngine.INT_2, DFAEngine.AFTER_INT_SPACE, "space"),
        (DFAEngine.INT_3PLUS, DFAEngine.AFTER_INT_SPACE, "space"),
        (DFAEngine.ORD_S, DFAEngine.ORD_DONE, "t"),
        (DFAEngine.ORD_N, DFAEngine.ORD_DONE, "d"),
        (DFAEngine.ORD_R, DFAEngine.ORD_DONE, "d"),
        (DFAEngine.ORD_T, DFAEngine.ORD_DONE, "h"),
        (DFAEngine.AFTER_INT_SPACE, DFAEngine.UNIT_G, "g"),
        (DFAEngine.AFTER_INT_SPACE, DFAEngine.UNIT_K, "k"),
        (DFAEngine.UNIT_K, DFAEngine.UNIT_KG, "g"),
        (DFAEngine.AFTER_INT_SPACE, DFAEngine.UNIT_M, "m"),
        (DFAEngine.UNIT_M, DFAEngine.UNIT_ML, "l"),
        (DFAEngine.AFTER_INT_SPACE, DFAEngine.UNIT_C, "c"),
        (DFAEngine.UNIT_C, DFAEngine.UNIT_CM, "m"),
        (DFAEngine.AFTER_INT_SPACE, DFAEngine.UNIT_L, "L"),
        (DFAEngine.INT_1, DFAEngine.DATE_SLASH_1, "/"),
        (DFAEngine.DATE_SLASH_1, DFAEngine.DATE_MONTH_1, "digit"),
        (DFAEngine.DATE_MONTH_1, DFAEngine.DATE_MONTH_2, "digit"),
        (DFAEngine.DATE_MONTH_1, DFAEngine.DATE_SLASH_2, "/"),
        (DFAEngine.DATE_MONTH_2, DFAEngine.DATE_SLASH_2, "/"),
        (DFAEngine.DATE_SLASH_2, DFAEngine.DATE_YEAR_1, "digit"),
        (DFAEngine.DATE_YEAR_1, DFAEngine.DATE_YEAR_2, "digit"),
        (DFAEngine.DATE_YEAR_2, DFAEngine.DATE_YEAR_3, "digit"),
        (DFAEngine.DATE_YEAR_3, DFAEngine.DATE_YEAR_4, "digit"),
    ]


def _trap_hint_sources() -> list[str]:
    """Return states that can show generic invalid-input paths to TRAP."""
    # These are representative invalid-input paths that can move to TRAP.
    return [state for state in STATE_NAMES if state != DFAEngine.TRAP]


def render_state_diagram_html(
    trace: Iterable[TransitionStep],
    current_step: int,
    width: str = "100%",
    height: str = "540px",
) -> str:
    """Render an interactive HTML graph of DFA states and transitions."""
    try:
        from pyvis.network import Network
    except ImportError:
        import sys

        python_exe = sys.executable.replace("\\", "\\\\")
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
        pos_x, pos_y = STATE_POSITIONS[state_name]
        title_text = f"State: {state_name}"
        if state_name == DFAEngine.DATE_YEAR_4:
            title_text += "\nAccepts only if the year has exactly 4 digits."
        elif state_name in {
            DFAEngine.DATE_SLASH_1,
            DFAEngine.DATE_MONTH_1,
            DFAEngine.DATE_MONTH_2,
            DFAEngine.DATE_SLASH_2,
            DFAEngine.DATE_YEAR_1,
            DFAEngine.DATE_YEAR_2,
            DFAEngine.DATE_YEAR_3,
        }:
            title_text += "\nPart of the DD/MM/YYYY path."
        network.add_node(
            state_name,
            label=state_name,
            color=_node_color(state_name, current_state, visited_states),
            shape=_node_shape(state_name),
            borderWidth=_node_border_width(state_name, current_state),
            title=title_text,
            x=pos_x,
            y=pos_y,
            physics=False,
            fixed={"x": True, "y": True},
            size=24 if state_name in ACCEPTING_STATES else 20,
        )

    for source, target, label in _base_edges():
        pair = (source, target)
        network.add_edge(
            source,
            target,
            label=label,
            color=_edge_color(pair, traversed_pairs),
            width=4 if pair in traversed_pairs else 1,
            arrows="to",
        )

    # Show generic invalid-input paths to TRAP so trap reachability is always visible.
    for source in _trap_hint_sources():
        network.add_edge(
            source,
            DFAEngine.TRAP,
            label="",
            title="invalid",
            color="#b0bec5",
            width=1,
            arrows="to",
            dashes=True,
            smooth={"enabled": True, "type": "curvedCCW", "roundness": 0.09},
        )

    # Show trap transitions encountered in current trace even though they are input-specific.
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
