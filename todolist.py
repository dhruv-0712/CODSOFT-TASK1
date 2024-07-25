import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_task():
    try:
        index = listbox.curselection()[0]
        task = entry.get()
        if task:
            listbox.delete(index)
            listbox.insert(index, task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(
    frame,
    width=50,
    height=10,
    font=("Courier New", 12),
    bd=0,
    fg="#464646",
    selectbackground="#a6a6a6"
)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(
    root,
    font=("Courier New", 12)
)
entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(
    button_frame,
    text="Add Task",
    command=add_task,
    font=("Courier New", 12)
)
add_button.pack(side=tk.LEFT)

delete_button = tk.Button(
    button_frame,
    text="Delete Task",
    command=delete_task,
    font=("Courier New", 12)
)
delete_button.pack(side=tk.LEFT)

update_button = tk.Button(
    button_frame,
    text="Update Task",
    command=update_task,
    font=("Courier New", 12)
)
update_button.pack(side=tk.LEFT)

root.mainloop()