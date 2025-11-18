import tkinter as tk

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

# Window setup
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

entry = tk.Entry(window, width=20, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        tk.Button(window, text=text, width=5, height=2, command=calculate).grid(row=row, column=col)
    else:
        tk.Button(window, text=text, width=5, height=2, command=lambda t=text: click_button(t)).grid(row=row, column=col)

# Clear button
tk.Button(window, text="C", width=22, height=2, command=clear).grid(row=5, column=0, columnspan=4)

window.mainloop()
