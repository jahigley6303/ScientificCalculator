### Unified Advanced Calculator

A multi‑function desktop calculator built with Python and Tkinter.
Designed with a shared input field and multiple calculator modes organized into tabs, including Basic, Scientific, and Modern ttk‑styled interfaces. Also includes a global theme system and scientific Degree/Radian toggle.

## Features

# ✔ Shared Display
All calculator modes use a single unified input/display field at the top of the interface.
# ✔ Multiple Calculator Tabs
Organized using a ttk.Notebook:

# 1. Basic Calculator
- Standard operations (+, –, ×, ÷)
- Decimal support
- Memory functions:
-- MC – Clear memory
-- MR – Recall memory
-- M+ – Add to memory
-- M- – Subtract from memory
- Uses Python’s eval() for evaluation

# 2. Scientific Calculator
Includes advanced mathematical operations:
- Trigonometric functions: sin, cos, tan
- Square root: sqrt
- Logarithms: log (base 10) and ln (natural log)
- pi constant
- Factorial: !
- Parentheses for complex expressions

# Angle Mode Toggle:
Switch between Degrees (DEG) and Radians (RAD).

# 3. Modern Calculator (ttk Styled)
- Clean “clam” theme
- Uses ttk.Button components
- Same functionality as basic calculator with a modern look

## Global Theme System
Theme buttons located above the tabs allow changing the overall calculator color scheme:
- Light
- Dark
- Blue
- High Contrast

# Themes update:
- Background colors
- Display field
- All calculator tabs

## Installation
# Requirements
Make sure Python 3.x is installed.
No external modules required — only standard Python libraries:
- tkinter
- math
# Run the Program
Shell
python calculator_colorful.py
Show more lines

## Project Structure

calculator.py   # Main application file

README.md                # Project information

## How It Works
# GUI Framework
The app uses Tkinter for the main window and widgets, and ttk.Notebook to organize three tabs.
# Shared Logic
- A single tk.Entry widget is shared across all calculator types.
- Button presses append or evaluate expressions in this display.

# Scientific Mode
- Trigonometric functions automatically convert degrees to radians if DEG mode is active.
- Logs, factorials, and square root use Python’s math module.

# Error Handling
All operations include minimal error handling to prevent crashes:
- Invalid entries display "Error".

## Known Limitations
- Uses eval() for basic and modern tabs (acceptable for local calculators but not recommended for user-supplied untrusted input).
- Theme coloring may not apply fully to all ttk components (ttk has separate styling).

## Planned Improvements (Optional)
- Calculation history window
- Graphing tab
- Custom user themes
- Animation and hover effects
- Packaging as an executable (.exe)

## License
This project is free to modify and extend.