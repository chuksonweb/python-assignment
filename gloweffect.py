import tkinter as tk

# ---------- Glow Animation Functions ----------
def glow_in(widget, step=0):
    if step > 10:
        return
    color = f"#{hex(240 - step*8)[2:]:0>2}{hex(240 - step*8)[2:]:0>2}ff"
    widget.config(highlightbackground=color, highlightcolor=color, highlightthickness=3)
    widget.after(20, lambda: glow_in(widget, step + 1))

def glow_out(widget, step=0):
    if step > 10:
        widget.config(highlightthickness=0)
        return
    color = f"#c8c8ff"
    widget.config(highlightbackground=color, highlightcolor=color, highlightthickness=3)
    widget.after(20, lambda: glow_out(widget, step + 1))


# ---------- Calculator Logic ----------
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


# ---------- Window ----------
window = tk.Tk()
window.title("Glow Effect Calculator")
window.geometry("330x440")
window.configure(bg="#222")


# ---------- Display ----------
entry = tk.Entry(window, width=20, font=("Arial", 22), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# ---------- Button Setup ----------
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

def create_button(text, row, col):
    if text == "=":
        btn = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18),
                        command=calculate, bg="#f0f0f0", relief="flat")
    else:
        btn = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18),
                        command=lambda t=text: click_button(t), bg="#f0f0f0", relief="flat")
    
    # Glow events
    btn.bind("<Enter>", lambda e, b=btn: glow_in(b))
    btn.bind("<Leave>", lambda e, b=btn: glow_out(b))

    btn.grid(row=row, column=col, padx=5, pady=5)


# Create all buttons
for text, row, col in buttons:
    create_button(text, row, col)


# ---------- Clear Button ----------
clear_btn = tk.Button(window, text="C", width=22, height=2, font=("Arial", 18),
                      command=clear, bg="#f0f0f0", relief="flat")

clear_btn.bind("<Enter>", lambda e: glow_in(clear_btn))
clear_btn.bind("<Leave>", lambda e: glow_out(clear_btn))

clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

window.mainloop()
