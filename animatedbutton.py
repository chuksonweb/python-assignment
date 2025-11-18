import tkinter as tk

# ---------- Button Animation Styles ----------
def on_enter(e):
    e.widget["background"] = "#d1d1d1"   # hover color

def on_leave(e):
    e.widget["background"] = "#f0f0f0"   # default color

def on_click(e):
    e.widget["background"] = "#bdbdbd"   # click color
    e.widget.after(100, lambda: e.widget.config(background="#d1d1d1"))

# ---------- Calculator Functions ----------
def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# ---------- Window Setup ----------
window = tk.Tk()
window.title("Animated Calculator")
window.geometry("320x420")

entry = tk.Entry(window, width=20, font=("Arial", 22), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# ---------- Button Config ----------
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

def create_button(text, row, col):
    if text == "=":
        btn = tk.Button(window, text=text, width=5, height=2, font=("Arial", 16),
                        command=calculate, background="#f0f0f0")
    else:
        btn = tk.Button(window, text=text, width=5, height=2, font=("Arial", 16),
                        command=lambda t=text: click_button(t), background="#f0f0f0")

    # Add animations
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    btn.bind("<Button-1>", on_click)

    btn.grid(row=row, column=col, padx=3, pady=3)

# Create all buttons
for text, row, col in buttons:
    create_button(text, row, col)

# ---------- Clear Button ----------
clear_btn = tk.Button(window, text="C", width=22, height=2, font=("Arial", 16),
                      command=clear, background="#f0f0f0")
clear_btn.bind("<Enter>", on_enter)
clear_btn.bind("<Leave>", on_leave)
clear_btn.bind("<Button-1>", on_click)

clear_btn.grid(row=5, column=0, columnspan=4, padx=3, pady=3)

window.mainloop()
