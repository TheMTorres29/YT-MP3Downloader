# Todo List using customtkinter tutorial
# first ctk project

# Packages
import customtkinter as ctk

# Functions
# Add Todo
def add_todo():
    todo = entry.get()
    label = ctk.CTkLabel(scrollable_frame, text=todo)
    label.pack()
    entry.delete(0, ctk.END)

# tkinter GUI
root = ctk.CTk()
root.geometry("750x450")
root.title("Todo App")

# Title
title_label = ctk.CTkLabel(root, text="Daily Tasks", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(30, 20))

# Scrollable Window Frame
scrollable_frame = ctk.CTkScrollableFrame(root, width=500, height=200)
scrollable_frame.pack(pady=10)

# Todo Entry
entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Add todo")
entry.pack(fill="x")

# Add Button
add_button = ctk.CTkButton(root, text="Add", width=500, command=add_todo)
add_button.pack(pady=20)

root.mainloop()