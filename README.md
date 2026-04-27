# CPT411 L2 Number Data Finder (DFA Recognizer)

This project implements a strict, mathematically pure Deterministic Finite Automaton (DFA) recognizer for extracting numerical and date-based data patterns from raw text. 

The system operates strictly character-by-character from left-to-right, transitioning through purely defined states.

### Recognized Categories
- **Exact Quantities:** (e.g., `100`, `45`)
- **Percentages:** (e.g., `50%`)
- **Ordinal Numbers:** Case-insensitive ordinals (e.g., `1st`, `2ND`, `3rd`, `4TH`)
- **Quantity with Units:** Case-insensitive standard units (e.g., `10 kg`, `5 L`, `100 ml`, `5 cm`, `10 g`)
- **Dates:** 
  - Standard format: `DD/MM/YYYY`
  - Textual format: Spelled out English dates for all 12 months (e.g., `April 23, 2021`, `june 30, 2021`)

---

## Architecture
- `src/core`: Pure DFA states and the transition engine. The engine uses strict branching edges (e.g., `ch in ('a', 'A')`) to achieve case insensitivity without violating Automata string pre-processing rules.
- `src/app`: The `StreamingMatcher` that feeds characters to the DFA engine and handles word boundaries to ensure maximum-length non-overlapping token extraction.
- `src/ui`: Interactive Streamlit dashboard that provides a real-time visualization of the DFA graph and steps through the state transitions visually.

---

## Setup
If running for the first time, initialize your virtual environment:
```bash
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Run (UI Dashboard)
The best way to interact with the DFA engine is through the Streamlit visualization tool:
```bash
.\.venv\Scripts\activate
streamlit run src/ui/app.py
```
> **Note:** The UI includes an interactive `pyvis` network graph that displays all 60+ generated states for the textual month paths. You can trace the DFA's exact character-by-character path live.

## Run (CLI)
```bash
.\.venv\Scripts\activate
python -m src.main
```

---

## Notes on Automata Constraints
This project strictly adheres to theoretical Automata properties:
1. **No External Libraries:** No regex (`re`) or external parsing libraries are used for recognition.
2. **Left-to-Right Processing:** Text is evaluated exactly one character at a time.
3. **Pure-State Transitions:** Case insensitivity and long string matching (like 12 English months) are achieved entirely by defining discrete, hardcoded state transitions mapping to explicit characters. No string buffering, mathematical counters, or `.lower()` normalization preprocessing is used.
4. **Trap-State Termination:** Invalid character sequences instantly dump the engine into a terminal `TRAP` state.