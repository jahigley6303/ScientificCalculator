import tkinter as tk
from tkinter import ttk
import math



# MAIN APP CLASS
class UnifiedCalculatorApp:
    def __init__(self, root_window):
        self.root = root_window
        self.root.title("Scientific Calculator")

        # Shared state

        self.angle_mode = "DEG"  # DEG or RAD
        self.theme_color = "lightgray"

        # ===== Shared Display =====

        self.display = tk.Entry(self.root, font=("Arial", 22), borderwidth=5, width=25)
        self.display.pack(pady=10)

        root_window.bind("<Return>", self.enter_equal)
        root_window.bind("<KP_Enter>", self.enter_equal)

        # ===== Global Theme Buttons =====

        theme_frame = tk.Frame(self.root)
        theme_frame.pack()

        tk.Button(theme_frame, text="Light", command=lambda: self.set_theme("light")).pack(side="left", padx=5)
        tk.Button(theme_frame, text="Dark", command=lambda: self.set_theme("dark")).pack(side="left", padx=5)
        tk.Button(theme_frame, text="Blue", command=lambda: self.set_theme("blue")).pack(side="left", padx=5)
        tk.Button(theme_frame, text="Orange", command=lambda: self.set_theme("orange")).pack(side="left", padx=5)


        # ===== Tabs =====

        notebook = ttk.Notebook(self.root)
        notebook.pack(expand=True, fill="both")

        # Create tabs

        self.basic_tab = BasicCalculatorTab(notebook, self.display)
        self.scientific_tab = ScientificCalculatorTab(notebook, self.display, self)
        self.modern_tab = ModernCalculatorTab(notebook, self.display)

        notebook.add(self.basic_tab.frame, text="Basic")
        notebook.add(self.scientific_tab.frame, text="Scientific")
        notebook.add(self.modern_tab.frame, text="Modern")

        self.apply_theme()

    # === Theme Logic ===

    def set_theme(self, theme):
        self.theme_color = theme
        self.apply_theme()

    def apply_theme(self):
        theme_map = {
            "light": "white",
            "dark": "black",
            "blue": "#4682B4",
            "orange": "#F26724"
        }

        color = theme_map.get(self.theme_color, "white")
        self.root.configure(bg=color)
        self.display.configure(bg="white" if color != "black" else "#222",
                               fg="black" if color != "black" else "white")

        # Determine foreground text color
        fg_color = "white" if color == "black" else "black"

        # Apply to all tabs
        self.basic_tab.apply_theme(color, fg_color)
        self.scientific_tab.apply_theme(color, fg_color)
        self.modern_tab.apply_theme(color, fg_color)

    def enter_equal(self, event=None):
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")



# BASIC CALCULATOR TAB
class BasicCalculatorTab:
    def __init__(self, notebook, display):
        self.display = display
        self.memory = 0

        self.frame = tk.Frame(notebook)

        # Buttons
        buttons = [
            ("1/x", 1, 0), ("x²", 1, 1), ("C", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            (" ", 5, 0), ("0", 5, 1), (".", 5, 2), ("=", 5, 3),
        ]

        for (text, r, c) in buttons:
            tk.Button(self.frame, text=text, width=6, height=2,
                      command=lambda button_text=text: self.press(button_text)
                      ).grid(row=r, column=c, padx=3, pady=3)

        # Memory Buttons

        mem_buttons = [("MC", 0, 0), ("MR", 0, 1), ("M+", 0, 2), ("M-", 0, 3)]

        for (text, r, c) in mem_buttons:
            tk.Button(self.frame, text=text, width=6, height=2,
                      command=lambda mem_cmd=text: self.memory_action(mem_cmd)
                      ).grid(row=r, column=c, padx=3, pady=3)

    def press(self, value):
        if value == "C":
            self.display.delete(0, tk.END)
            return

        if value == "=":
            try:
                result = eval(self.display.get())
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                return

            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
        else:
            self.display.insert(tk.END, value)

    def press(self, value):
        if value == "C":
            self.display.delete(0, tk.END)
            return

        if value == "1/x":
            try:
                num = float(self.display.get())
                result = 1 / num
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                return

            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
            return

        if value == "x²":
            try:
                num = float(self.display.get())
                result = num * num
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                return

            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
            return

        if value == "=":
            try:
                result = eval(self.display.get())
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                return

            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
        else:
            self.display.insert(tk.END, value)

    def memory_action(self, act):
        try:
            val = float(self.display.get())
        except Exception:
            val = 0

        if act == "MC":
            self.memory = 0
        elif act == "MR":
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(self.memory))
        elif act == "M+":
            self.memory += val
        elif act == "M-":
            self.memory -= val

    def apply_theme(self, color, fg):
        self.frame.configure(bg=color)
        for widget in self.frame.winfo_children():
            try:
                widget.configure(bg=color, fg = fg)
            except Exception:
                pass

# SCIENTIFIC CALCULATOR TAB
class ScientificCalculatorTab:
    def __init__(self, notebook, display_entry, parent_app):
        self.display = display_entry
        self.app = parent_app

        self.frame = tk.Frame(notebook)

        sci_buttons = [
            ("sin", 1, 0), ("cos", 1, 1), ("tan", 1, 2), ("sqrt", 1, 3),
            ("log", 2, 0), ("ln", 2, 1), ("pi", 2, 2), ("!", 2, 3),
            ("(", 3, 0), (")", 3, 1)
        ]

        for (text, r, c) in sci_buttons:
            tk.Button(self.frame, text=text, width=6, height=2,
                      command=lambda fn=text: self.f_press(fn)
                      ).grid(row=r, column=c, padx=3, pady=3)

        # DEG/RAD toggle

        self.mode_button = tk.Button(self.frame, text="Mode: DEG", width=10,
                                     command=self.toggle_mode)
        self.mode_button.grid(row=0, column=0, columnspan=4)

    def toggle_mode(self):
        self.app.angle_mode = "RAD" if self.app.angle_mode == "DEG" else "DEG"
        self.mode_button.config(text=f"Mode: {self.app.angle_mode}")

    def f_press(self, func):
        if func == "pi":
            self.display.insert(tk.END, str(math.pi))
            return

        if func == "!":
            try:
                n = int(self.display.get())
                result = math.factorial(n)
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                return

            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
            return

        try:
            x = float(self.display.get())
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
            return

        if func in ["sin", "cos", "tan"]:
            if self.app.angle_mode == "DEG":
                x = math.radians(x)

            try:
                result = getattr(math, func)(x)
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                return

            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
            return

        try:
            if func == "sqrt":
                result = math.sqrt(x)
            elif func == "log":
                result = math.log10(x)
            elif func == "ln":
                result = math.log(x)
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
            return

        self.display.delete(0, tk.END)
        self.display.insert(tk.END, result)

    def apply_theme(self, color, fg):
        self.frame.configure(bg=color)
        for widget in self.frame.winfo_children():
            try:
                widget.configure(bg=color, fg = fg)
            except Exception:
                pass



# MODERN TTK-STYLED CALCULATOR TAB
class ModernCalculatorTab:
    def __init__(self, notebook, display):
        self.display = display

        self.frame = tk.Frame(notebook)

        style = ttk.Style()
        style.theme_use("clam")

        modern_buttons = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
            ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3)
        ]

        for (text, r, c) in modern_buttons:
            ttk.Button(self.frame, text=text, width=6,
                       command=lambda button_text=text: self.p_press(button_text)
                       ).grid(row=r, column=c, padx=5, pady=5)

    def p_press(self, value):
        if value == "=":
            try:
                result = eval(self.display.get())
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                return

            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
        else:
            self.display.insert(tk.END, value)

    def apply_theme(self, color, fg):
        self.frame.configure(bg=color)

        # TTK buttons need a style
        style = ttk.Style()

        if color == "black":  # dark mode
            style.configure("TButton",
                            foreground="white",
                            background="black",
                            padding=5)
        else:
            style.configure("TButton",
                            foreground="black",
                            background=color,
                            padding=5)


# RUN THE APP
if __name__ == "__main__":
    root_window = tk.Tk()
    app = UnifiedCalculatorApp(root_window)
    root_window.mainloop()