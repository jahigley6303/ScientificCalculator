## Unified Advanced Calculator

A multi‑function desktop calculator built with Python and Tkinter.
Designed with a shared input field and multiple calculator modes organized into tabs, including Basic, Scientific, and Modern ttk‑styled interfaces. Also includes a global theme system and scientific Degree/Radian toggle.

## Features

### ✔ Shared Display
All calculator modes use a single unified input/display field at the top of the interface.
### ✔ Multiple Calculator Tabs
This application isorganized using a ttk.Notebook with three calculator modes.

### Basic Calculator
- Standard operations (+, –, ×, ÷)
- Decimal support
- Memory functions:
-- MC – Clear memory
-- MR – Recall memory
-- M+ – Add to memory
-- M- – Subtract from memory
- Uses Python’s eval() for evaluation

###  Scientific Calculator
Includes advanced mathematical operations:
- Trigonometric functions: sin, cos, tan
- Square root: sqrt
- Logarithms:
--  log (base 10)
--  ln (natural log)
- pi constant
- Factorial: !
- Parentheses for complex expressions

### Angle Mode Toggle:
- Degrees (DEG)  
- Radians (RAD).

### Modern Calculator 
A modern calculator interface using ttk widgets.

- Clean ttk-styled interface theme
- Uses ttk.Button components
- Provides the same core functionality as the Basic Calculator

## Theme System
Theme buttons allow users to change the application's color scheme dynamically.

Available themes include:
- Light
- Dark
- Blue
- Orange/ High Contrast

Themes changes update:
- Application background colors
- Display field
- Calculator buttons
- Calculator tabs and interface styling

## Keyboard Support
The calculator supports keyboard and keypad input for faster operation.

Users can:
- Enter numbers using the keyboard or numeric keypad
- Use arithmetic operators
- Press the Enter key to evaluate expressions

## Technologies Used
-Python
-Tkinter
-ttk
-math

No external libraries are required.

## Installation

### Requirements
Python 3.x 

The application uses only Python standard libraries:
- tkinter
- math

### Run the Program
python calculator.py

## Project Structure
Unified-Advanced-Calculator/
│
├── calculator.py
├── README.md
└── images/
    └── calculator-orange.png

## How It Works

## GUI Framework
The application uses Tkinter for the main window and interface components. A ttk.Notebook organizes the calculator into three separate modes.

## Shared Logic
- A single tk.Entry widget is used as the shared display.
- Calculator buttons append values and operations to the display.
- Expressions are evaluated when the user presses the equals button or Enter key.

## Scientific Mode
- Trigonometric functions automatically convert degrees to radians when Degree mode is active.
- Logarithmic, factorial, and square root operations use Python's math module.

## Error Handling
Basic error handling is included to prevent the application from crashing.

Invalid expressions display:
- Error

## Known Limitations
- The Basic and Modern calculator modes use eval() for expression evaluation. This is acceptable for a local calculator project but would not be recommended for evaluating untrusted user input.
- Some ttk components may require additional styling because ttk manages themes separately from standard Tkinter widgets.

## Planned Improvements 
Potential future enhancements include:

- Calculation history
- Graphing functionality
- Custom user-created themes
- Animation and hover effects
- Application settings
- Packaging as a standalone Windows executable

## License
This project is free to modify and extend.
