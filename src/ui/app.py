import sys
import os
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import streamlit as st
from streamlit.components.v1 import html

from src.app.matcher import StreamingMatcher
from src.app.reporter import highlight_matches, to_table_rows
from src.ui.simulator import trace_rows
from src.ui.state_diagram import render_state_diagram_html


def _load_text(uploaded_file) -> str:
    """Load text from uploaded file or fallback sample file."""
    if uploaded_file is None:
        default_path = Path("sample_input.txt")
        if default_path.exists():
            return default_path.read_text(encoding="utf-8")
        return ""
    return uploaded_file.read().decode("utf-8")


def main() -> None:
    """Run the Streamlit UI for interactive DFA matching and simulation."""
    st.set_page_config(page_title="L2 Number Data Finder (DFA)", layout="wide")
    st.markdown(
        """
        <style>
        .stAppDeployButton {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.title("Number Data Finder - DFA Recognizer")

    uploaded_file = st.file_uploader("Upload text file", type=["txt"])
    text = _load_text(uploaded_file)

    st.subheader("Text")
    text = st.text_area("Input text", value=text, height=180)

    matcher = StreamingMatcher()
    matches = matcher.find_matches(text)

    st.subheader("Output")
    st.write(f"Pattern occurrences: {len(matches)}")
    st.write(f"Text length: {len(text)} characters")

    if matches:
        st.dataframe(to_table_rows(matches), use_container_width=True)

        selected = st.selectbox(
            "Select a recognized pattern for DFA simulation",
            options=list(range(len(matches))),
            format_func=lambda i: f"{matches[i].pattern} ({matches[i].start}-{matches[i].end})",
        )

        chosen = matches[selected]
        match_key = f"{selected}:{chosen.start}:{chosen.end}:{len(chosen.trace)}"
        if st.session_state.get("active_match_key") != match_key:
            st.session_state["active_match_key"] = match_key
            st.session_state["step_index"] = len(chosen.trace)

        st.write(f"Pattern: {chosen.pattern}")
        st.write(f"Status: {chosen.status}")
        st.write(f"Category: {chosen.category}")
        st.write(f"Position: {chosen.start} to {chosen.end}")

        st.subheader("Character-by-character DFA trace")
        st.dataframe(trace_rows(chosen), use_container_width=True)

        max_step = len(chosen.trace)
        step_index = min(st.session_state.get("step_index", max_step), max_step)

        if step_index == 0:
            current_state = "START"
            transition_text = "No transition yet"
            step_message = "Step 0: machine is at START state."
        else:
            active = chosen.trace[step_index - 1]
            current_state = active.to_state
            transition_text = f"read '{active.char}' at index {active.index}"
            step_message = (
                f"Step {step_index}: {active.from_state} -> {active.to_state} "
                f"while reading '{active.char}'"
            )

        st.markdown(
            (
                "<div style='display:grid;grid-template-columns: 2.2fr 3.1fr;"
                "width:100%;border:1px solid #263238;border-radius:8px;overflow:hidden;'>"
                "<div style='background:#050a17;padding:18px 16px;border-right:1px solid #37474f;"
                "display:flex;align-items:center;'>"
                "<div style='font-size:26px;font-weight:800;line-height:1.1;'>Interactive DFA State Diagram</div>"
                "</div>"
                "<div style='background:#050a17;padding:16px 18px;'>"
                "<div style='display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;'>"
                f"<div><div style='font-size:13px;font-weight:700;opacity:0.9;'>STEP</div><div style='font-size:34px;font-weight:800;line-height:1.1;margin-top:2px;'>{step_index}</div></div>"
                f"<div><div style='font-size:13px;font-weight:700;opacity:0.9;'>CURRENT STATE</div><div style='font-size:28px;font-weight:800;line-height:1.1;margin-top:4px;'>{current_state}</div></div>"
                f"<div><div style='font-size:13px;font-weight:700;opacity:0.9;'>TRANSITION</div><div style='font-size:24px;font-weight:700;line-height:1.2;margin-top:4px;'>{transition_text}</div></div>"
                "</div>"
                "</div>"
                "</div>"
            ),
            unsafe_allow_html=True,
        )

        st.markdown(
            (
                "<div style='padding:12px 14px;border-radius:10px;"
                "background:#fff4e5;border:1px solid #f0b55b;"
                "font-size:20px;font-weight:700;color:#5d4037;margin:8px 0 12px 0;'>"
                f"{step_message}"
                "</div>"
            ),
            unsafe_allow_html=True,
        )

        html(
            render_state_diagram_html(chosen.trace, step_index),
            height=420,
            scrolling=True,
        )

        st.markdown(
            """
            <div style="display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px;width:100%;margin-top:6px;align-items:center;">
                <div style="display:flex;align-items:center;gap:8px;">
                    <span style="width:14px;height:14px;border-radius:50%;background:#ffcc80;display:inline-block;border:1px solid #8d6e63"></span>
                    <span>Current state</span>
                </div>
                <div style="display:flex;align-items:center;gap:8px;">
                    <span style="width:14px;height:14px;border-radius:50%;background:#bbdefb;display:inline-block;border:1px solid #455a64"></span>
                    <span>Visited state</span>
                </div>
                <div style="display:flex;align-items:center;gap:8px;">
                    <span style="width:14px;height:14px;border-radius:50%;background:#e8f5e9;display:inline-block;border:1px solid #455a64"></span>
                    <span>Unvisited state</span>
                </div>
                <div style="display:flex;align-items:center;gap:8px;">
                    <span style="width:14px;height:14px;border-radius:50%;background:#ffcdd2;display:inline-block;border:1px solid #b71c1c"></span>
                    <span>Trap state</span>
                </div>
                <div style="display:flex;align-items:center;gap:8px;">
                    <span style="width:14px;height:14px;border-radius:50%;background:#e8f5e9;display:inline-block;border:2px solid #455a64;box-shadow:0 0 0 3px #ffffff, 0 0 0 4px #455a64"></span>
                    <span>Accepting state (double circle)</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        slider_cols = st.columns([8, 1], vertical_alignment="center")
        with slider_cols[0]:
            slider_step = st.slider(
                "Simulation step",
                min_value=0,
                max_value=max_step,
                value=step_index,
                help="Move step-by-step to see state and transition movement.",
            )
        with slider_cols[1]:
            numeric_step = int(
                st.number_input(
                    "Step",
                    min_value=0,
                    max_value=max_step,
                    value=slider_step,
                    step=1,
                    label_visibility="collapsed",
                )
            )

        next_step = numeric_step
        nav_cols = st.columns([1, 1])
        if nav_cols[0].button("Previous Step", use_container_width=True):
            next_step = max(0, numeric_step - 1)
        if nav_cols[1].button("Next Step", use_container_width=True):
            next_step = min(max_step, numeric_step + 1)

        if next_step != step_index:
            st.session_state["step_index"] = next_step
            st.rerun()

    else:
        st.warning("No accepted pattern found. Status: Reject")

    st.subheader("Visualization")
    st.markdown(highlight_matches(text, matches))


if __name__ == "__main__":
    main()
