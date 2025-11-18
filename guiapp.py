import tkinter as tk
from tkinter import messagebox

# ---------- SAVE & LOAD ----------
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for task in file:
                task_list.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = task_list.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

# ---------- BUTTON FUNCTIONS ----------
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Enter a task first!")

def delete_task():
    try:
        index = task_list.curselection()[0]
        task_list.delete(index)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

def clear_tasks():
    task_list.delete(0, tk.END)
    save_tasks()

# ---------- GUI SETUP ----------
window = tk.Tk()
window.title("To-Do List App")
window.geometry("300x400")

# Entry box
task_entry = tk.Entry(window, width=25, font=("Arial", 12))
task_entry.pack(pady=10)

# Buttons
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

clear_button = tk.Button(window, text="Clear All", command=clear_tasks)
clear_button.pack(pady=5)

# Listbox for tasks
task_list = tk.Listbox(window, width=40, height=15)
task_list.pack(pady=10)

# Load tasks from file
load_tasks()

window.mainloop()
