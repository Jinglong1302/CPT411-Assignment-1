from __future__ import annotations

from typing import Iterable

from src.app.models import TransitionStep
from src.core.states import State


ACCEPTING_STATES = {
    State.INT.name,
    State.PERCENT.name,
    State.ORD_DONE.name,
    State.WORD.name,
    State.DATE_YEAR.name,
}

STATE_POSITIONS: dict[str, tuple[int, int]] = {
    State.START.name: (-780, 20),
    State.INT.name: (-520, 20),
    State.PERCENT.name: (-250, -220),
    State.ORD_S.name: (-250, -60),
    State.ORD_N.name: (-250, 70),
    State.ORD_R.name: (-250, 200),
    State.ORD_T.name: (-250, 330),
    State.ORD_DONE.name: (40, 120),
    State.AFTER_INT_SPACE.name: (-250, 470),
    State.WORD.name: (70, 470),
    State.AFTER_WORD.name: (390, 470),
    State.DATE_YEAR.name: (700, 470),
    State.TRAP.name: (320, -220),
}


def _node_color(state_name: str, current_state_name: str | None, visited: set[str]) -> str:
    if state_name == current_state_name:
        return "#ffcc80"
    if state_name in visited:
        return "#bbdefb"
    if state_name == State.TRAP.name:
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
        (State.START.name, State.INT.name, "digit"),
        (State.INT.name, State.INT.name, "digit"),
        (State.INT.name, State.PERCENT.name, "%"),
        (State.INT.name, State.ORD_S.name, "s"),
        (State.INT.name, State.ORD_N.name, "n"),
        (State.INT.name, State.ORD_R.name, "r"),
        (State.INT.name, State.ORD_T.name, "t"),
        (State.INT.name, State.AFTER_INT_SPACE.name, "space"),
        (State.ORD_S.name, State.ORD_DONE.name, "t"),
        (State.ORD_N.name, State.ORD_DONE.name, "d"),
        (State.ORD_R.name, State.ORD_DONE.name, "d"),
        (State.ORD_T.name, State.ORD_DONE.name, "h"),
        (State.AFTER_INT_SPACE.name, State.WORD.name, "letter"),
        (State.WORD.name, State.WORD.name, "letter"),
        (State.WORD.name, State.AFTER_WORD.name, "space"),
        (State.AFTER_WORD.name, State.DATE_YEAR.name, "digit (month path)"),
        (State.DATE_YEAR.name, State.DATE_YEAR.name, "digit"),
    ]


def _trap_hint_sources() -> list[str]:
    # These are representative invalid-input paths that can move to TRAP.
    return [
        State.START.name,
        State.INT.name,
        State.PERCENT.name,
        State.ORD_S.name,
        State.ORD_N.name,
        State.ORD_R.name,
        State.ORD_T.name,
        State.ORD_DONE.name,
        State.AFTER_INT_SPACE.name,
        State.WORD.name,
        State.AFTER_WORD.name,
        State.DATE_YEAR.name,
    ]


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

    visited_states: set[str] = {State.START.name}
    traversed_pairs: set[tuple[str, str]] = set()
    current_state = State.START.name

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
                "smooth": {
                    "enabled": true,
                    "type": "curvedCW",
                    "roundness": 0.18
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

    for state in State:
        pos_x, pos_y = STATE_POSITIONS[state.name]
        network.add_node(
            state.name,
            label=state.name,
            color=_node_color(state.name, current_state, visited_states),
            shape=_node_shape(state.name),
            borderWidth=_node_border_width(state.name, current_state),
            title=f"State: {state.name}",
            x=pos_x,
            y=pos_y,
            physics=False,
            fixed={"x": True, "y": True},
            size=24 if state.name in ACCEPTING_STATES else 20,
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
            State.TRAP.name,
            label="invalid",
            color="#b0bec5",
            width=1,
            arrows="to",
            dashes=True,
            smooth={"enabled": True, "type": "curvedCCW", "roundness": 0.12},
        )

    # Show trap transitions encountered in current trace even though they are input-specific.
    for step in step_prefix:
        pair = (step.from_state, step.to_state)
        if pair[1] == State.TRAP.name:
            network.add_edge(
                pair[0],
                pair[1],
                label=f"'{step.char}'",
                color="#d32f2f",
                width=4,
                arrows="to",
            )

    return network.generate_html(notebook=False)
