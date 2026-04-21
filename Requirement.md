# CPT411 Assignment Requirement  
## L2: Number Data Finder (DFA Recognizer)

## 1. Objective
Develop a **well-structured** and **well-documented** recognizer using a **Deterministic Finite Automaton (DFA)** for the assigned language.

## 2. Core Implementation Rules
- The program must be based on a **complete DFA** for the language.
- The program may terminate early if a **trap state** is reached.
- Input must be processed **one character at a time**, from **left to right**, simulating a finite state machine.
- **No alternative strategy** is allowed.

## 3. Development and Testing
- A text file will be provided as sample input for implementation and testing.

## 4. Required Demonstration Output
For each program run, display:
1. **Pattern** (input string)
2. **Text** used for demonstration
3. **Status**: `Accept` or `Reject`
4. **Additional information**, such as:
    - Position of the matched pattern
    - Number of pattern occurrences
    - Visualization (e.g., boldface highlighting of matched patterns in the text)

## 5. Problem to Solve
### Language: **L2 – Number Data Finder**
Design a DFA that captures numerical data, including:
- Exact quantities
- Percentages
- Dates
- Ordinal numbers

### Example valid forms
- `3rd`
- `100%`
- `3 million`
- `2017`
- `16 September 2016`
- `5 litres`
- `2 cups`

## 6. Additional Constraint
- The core solution must be implemented manually without using automaton libraries for the main pattern recognition logic.