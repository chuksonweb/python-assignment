import tkinter as tk
from tkinter import messagebox

# ---------- CALCULATION FUNCTIONS ----------
def calculate_si():
    try:
        p = float(principal_entry.get())
        r = float(rate_entry.get())
        t = float(time_entry.get())

        si = (p * r * t) / 100
        result_label.config(text=f"Simple Interest: {si:.2f}")
    except:
        messagebox.showerror("Error", "Please enter valid numbers")

def calculate_ci():
    try:
        p = float(principal_entry.get())
        r = float(rate_entry.get())
        t = float(time_entry.get())

        ci = p * ((1 + r/100)**t) - p
        result_label.config(text=f"Compound Interest: {ci:.2f}")
    except:
        messagebox.showerror("Error", "Please enter valid numbers")

def clear_fields():
    principal_entry.delete(0, tk.END)
    rate_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    result_label.config(text="")

# ---------- WINDOW ----------
window = tk.Tk()
window.title("Interest Calculator")
window.geometry("350x350")
window.configure(bg="#e9f5ff")


# ---------- TITLE ----------
title = tk.Label(window, text="Simple & Compound Interest Calculator",
                 font=("Arial", 14, "bold"), bg="#e9f5ff")
title.pack(pady=10)


# ---------- INPUT FRAME ----------
frame = tk.Frame(window, bg="#e9f5ff")
frame.pack(pady=10)

tk.Label(frame, text="Principal (P):", font=("Arial", 12), bg="#e9f5ff").grid(row=0, column=0, sticky="w")
principal_entry = tk.Entry(frame, font=("Arial", 12), width=15)
principal_entry.grid(row=0, column=1)

tk.Label(frame, text="Rate (%) (R):", font=("Arial", 12), bg="#e9f5ff").grid(row=1, column=0, sticky="w")
rate_entry = tk.Entry(frame, font=("Arial", 12), width=15)
rate_entry.grid(row=1, column=1)

tk.Label(frame, text="Time (T):", font=("Arial", 12), bg="#e9f5ff").grid(row=2, column=0, sticky="w")
time_entry = tk.Entry(frame, font=("Arial", 12), width=15)
time_entry.grid(row=2, column=1)


# ---------- BUTTONS ----------
btn_frame = tk.Frame(window, bg="#e9f5ff")
btn_frame.pack(pady=15)

si_button = tk.Button(btn_frame, text="Calculate SI", font=("Arial", 12),
                      command=calculate_si, width=12)
si_button.grid(row=0, column=0, padx=5)

ci_button = tk.Button(btn_frame, text="Calculate CI", font=("Arial", 12),
                      command=calculate_ci, width=12)
ci_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(window, text="Clear", font=("Arial", 12),
                         command=clear_fields, width=26)
clear_button.pack(pady=5)


# ---------- RESULT ----------
result_label = tk.Label(window, text="", font=("Arial", 14, "bold"), bg="#e9f5ff", fg="blue")
result_label.pack(pady=10)


window.mainloop()
