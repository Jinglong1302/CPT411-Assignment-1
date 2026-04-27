# CPT411 L2 Number Data Finder (DFA Recognizer)

This project implements a deterministic finite automaton (DFA) recognizer for number data patterns:
- exact quantities
- percentages
- ordinal numbers
- dates

## Architecture
- `src/core`: DFA states, character classification, and transition engine.
- `src/app`: streaming matcher and report helpers.
- `src/ui`: Streamlit simulation and output display.
- `tests`: unit tests.


## Setup (First Time)
```bash
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Run (CLI)
```bash
.\.venv\Scripts\activate
python -m src.main
```


## Run (UI)
```bash
.\.venv\Scripts\activate
streamlit run src/ui/app.py
```

## Notes on Constraints
- Recognition logic is manual and DFA-based.
- Text is processed left-to-right, one character at a time.
- Trap-state termination is used.
- No regex or automaton libraries are used for main recognition.