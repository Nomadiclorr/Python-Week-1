import json
import datetime
import tkinter as tk
from tkinter import ttk, Tk, Label, PhotoImage
from tkinter import messagebox

# Declare global variables for entry fields
name_entry = None
description_entry = None
priority_entry = None
due_date_entry = None

# Function to load tasks from file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save tasks to file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Function to add a task
def add_task():
    global name_entry, description_entry, priority_entry, due_date_entry
    name = name_entry.get().strip()
    description = description_entry.get().strip()
    priority = priority_entry.get()
    due_date = due_date_entry.get()
    if not ([name, description, priority, due_date]):
         messagebox.showinfo("Error", "enter details!") 
         return

    tasks.append({
            "name": name,
            "description": description,
            "priority": priority,
            "due_date": due_date,
            "completed": False
    })
    save_tasks(tasks)
    update_task_list()
    clear_entries()
    messagebox.showinfo("Success", "Task added successfully!")  # Display success message

# Function to clear entry fields
def clear_entries():
    global name_entry, description_entry, priority_entry, due_date_entry
    name_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    priority_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)

# Function to update the task list
def update_task_list():
    global task_tree
    task_tree.delete(*task_tree.get_children())
    for i, task in enumerate(tasks, start=1):
        task_tree.insert("", "end", values=(i, task['name'], task['description'], task['priority'], task['due_date'], task['completed']))

# Function to mark a task as completed
def mark_completed():
    global task_tree
    selected_item = task_tree.selection()
    if selected_item:
        index = int(task_tree.item(selected_item, 'values')[0]) - 1
        tasks[index]['completed'] = True
        save_tasks(tasks)
        update_task_list()

# Function to delete task       
def delete_task():
        selected_item = task_tree.selection()
        if selected_item:
            task_index = int(task_tree.item(selected_item, 'values')[0]) - 1
            del tasks[task_index]
            update_task_list()
            



# Main function
def main():
    global tasks, task_tree, name_entry, description_entry, priority_entry, due_date_entry
    tasks = load_tasks()

    root = tk.Tk()
    root.title("CYBER SONICS TASK TRACKER")
    
    # window background color
    root.configure(bg="#BE93D4")

    # Create entry fields
    name_label = tk.Label(root, text="User Name:", bg = "#311432", fg = "white")
    name_label.grid(row=0, column=0, sticky="e")
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1)

    description_label = tk.Label(root, text="Task Description:", bg = "#311432", fg = "white")
    description_label.grid(row=2, column=0, sticky="e")
    description_entry = tk.Entry(root)
    description_entry.grid(row=2, column=1)

    priority_label = tk.Label(root, text="Priority(Low/Medium/High):", bg = "#311432", fg = "white")
    priority_label.grid(row=3, column=0, sticky="e", pady=5)
    priority_entry = tk.Entry(root)
    priority_entry.grid(row=3, column=1, pady=5)

    due_date_label = tk.Label(root, text="Due Date(YYYY-MM-DD):", bg = "#311432", fg = "white")
    due_date_label.grid(row=4, column=0, sticky="e")
    due_date_entry = tk.Entry(root)
    due_date_entry.grid(row=4, column=1, pady=5)
    
    def edit_task():
        selected_item = task_tree.selection()
        if selected_item:
            # Get the selected task
            selected_task_index = int(selected_item[0][1:]) - 1  # Get the index of the selected task from its ID
            selected_task = tasks[selected_task_index]

            # Create a separate window for editing the task
            edit_window = tk.Toplevel(root)
            edit_window.title("Edit Task")

            # Entry labels for editing task fields
            name_label = tk.Label(edit_window, text="Name:")
            name_label.grid(row=0, column=0, padx=5, pady=5)
            name_entry = tk.Entry(edit_window)
            name_entry.grid(row=0, column=1, padx=5, pady=5)
            name_entry.insert(0, selected_task["name"])
            
            priority_label = tk.Label(edit_window, text="Description:")
            priority_label.grid(row=1, column=0, padx=5, pady=5)
            priority_entry = tk.Entry(edit_window)
            priority_entry.grid(row=1, column=1, padx=5, pady=5)
            priority_entry.insert(0, selected_task["description"])

            priority_label = tk.Label(edit_window, text="Priority:")
            priority_label.grid(row=2, column=0, padx=5, pady=5)
            priority_entry = tk.Entry(edit_window)
            priority_entry.grid(row=2, column=1, padx=5, pady=5)
            priority_entry.insert(0, selected_task["priority"])

            due_date_label = tk.Label(edit_window, text="Due Date:")
            due_date_label.grid(row=3, column=0, padx=5, pady=5)
            due_date_entry = tk.Entry(edit_window)
            due_date_entry.grid(row=3, column=1, padx=5, pady=5)
            due_date_entry.insert(0, selected_task["due_date"])

            completed_label = tk.Label(edit_window, text="Completed:")
            completed_label.grid(row=4, column=0, padx=5, pady=5)
            completed_entry = tk.Entry(edit_window)
            completed_entry.grid(row=4, column=1, padx=5, pady=5)
            completed_entry.insert(0, selected_task["completed"])
            
    # Edit button
    edit_button = tk.Button(root, text="Edit Task", command=edit_task, bg= "orange")
    edit_button.grid(row=0, column=2, columnspan=1,  sticky="w")

    # Add task button
    add_button = tk.Button(root, text="Add Task", command=add_task, bg= "light green")
    add_button.grid(row=2, column=2, columnspan=1,  sticky="w")
    
    # Save button
    #save_button = tk.Button(root, text="Save new Task", command=edit_task, bg= "light green")
    #save_button.grid(row=0, column=2, columnspan=1,  sticky="w")

    # Task list
  
    task_tree = ttk.Treeview(root, columns=("ID", "User Name", "Task Description", "Priority", "Due Date", "Completed"), show="headings")
    task_tree.heading("ID", text="ID")
    task_tree.heading("User Name", text="User Name")
    task_tree.heading("Task Description", text="Task Description")
    task_tree.heading("Priority", text="Priority")
    task_tree.heading("Due Date", text="Due Date")
    task_tree.heading("Completed", text="Completed")
    task_tree.grid(row=5, column=0, columnspan=2, padx = 10)
    
    

    # Mark as completed button
    mark_completed_button = tk.Button(root, text="Mark Completed", command=mark_completed, bg= "light green")
    mark_completed_button.grid(row=3, column=2, columnspan=2)
    
    # Delete task button
    delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="red")
    delete_button.grid(row=4, column=2, columnspan=2, sticky="w")

    # Initialize task list
    update_task_list()

    root.mainloop()

if __name__ == "__main__":
    main()
