
import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk
import time
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import datetime

# Global variables
tasks = []
clock_update_interval = 1000
priority_options = ["high", "medium", "low"]
UserName_options = ["Bafana", "Sesethu", "Spheleke", "Lorraine", "Isivile"]

# Function to load tasks from file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save tasks to file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)

# Function to add a task
def add_task():
  title = UserName_var.get()
  description = description_entry.get()
  try:
    due_date = due_date_combobox.get_date().strftime('%Y-%m-%d')
  except:
    # Handle exception if no date is selected
    messagebox.showerror("Error", "Please select a due date.")
    return

  priority = priority_var.get()
  comment = comment_entry.get()

  # Check for required fields and empty description
  if not all([title, description, priority]):
    messagebox.showerror("Error", "Please fill in all required fields.")
    return
  if not description.strip():
    messagebox.showerror("Error", "Task Description cannot be empty.")
    description_entry.delete(0, tk.END)
    return

  # Validate due date is in the future (or today)
  try:
    today = datetime.date.today()
    due_date_obj = datetime.datetime.strptime(due_date, '%Y-%m-%d').date()
    if due_date_obj < today:
      messagebox.showerror("Error", "Due date cannot be in the past.")
      return
  except ValueError:
    # Handle invalid date format
    messagebox.showerror("Error", "Invalid due date format. Please select a date from the combobox.")
    return

  # Add task if all validations pass
  tasks.append({
      "name": title,
      "description": description,
      "due_date": due_date,
      "priority": priority,
      "completed": False,
      "comment": comment
  })
  save_tasks()
  clear_entries()
  update_task_list()
  messagebox.showinfo("Success", "Task added successfully")


# Function to clear entry fields
def clear_entries():
    UserName_var.set("")
    description_entry.delete(0, tk.END)
    due_date_combobox.set_date(time.strftime("%Y-%m-%d"))
    priority_var.set("")
    comment_entry.delete(0, tk.END)

# Function to edit a task
def edit_task():
    global selected_task
    selected_item = task_tree.selection()
    if selected_item:
        task_index = int(task_tree.item(selected_item, 'values')[0]) - 1
        selected_task = tasks[task_index]
        
        # Open a new window for editing the task
        edit_window = tk.Toplevel()
        edit_window.title("Edit Task")

        # Entry fields for editing task details
        name_label = ttk.Label(edit_window, text="Name:")
        name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        UserName_var_edit = tk.StringVar(edit_window, value=selected_task["name"])
        UserName_combobox_edit = ttk.Combobox(edit_window, textvariable=UserName_var_edit, values=UserName_options,
                                              state="readonly")
        UserName_combobox_edit.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        description_label = ttk.Label(edit_window, text="Description:")
        description_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        description_entry_edit = ttk.Entry(edit_window)
        description_entry_edit.grid(row=1, column=1, padx=5, pady=5)
        description_entry_edit.insert(0, selected_task["description"])

        priority_label = ttk.Label(edit_window, text="Priority:")
        priority_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        priority_var_edit = tk.StringVar(edit_window, value=selected_task["priority"])
        priority_combobox_edit = ttk.Combobox(edit_window, textvariable=priority_var_edit, values=priority_options,
                                              state="readonly")
        priority_combobox_edit.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        due_date_label = ttk.Label(edit_window, text="Due Date:")
        due_date_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        due_date_combobox_edit = DateEntry(edit_window, date_pattern='yyyy-mm-dd')
        due_date_combobox_edit.grid(row=3, column=1, padx=5, pady=5)
        due_date_combobox_edit.set_date(selected_task["due_date"])

        comment_label = ttk.Label(edit_window, text="Comment:")
        comment_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        comment_entry_edit = ttk.Entry(edit_window)
        comment_entry_edit.grid(row=4, column=1, padx=5, pady=5)
        comment_entry_edit.insert(0, selected_task["comment"])
        
        def save_edit():
            selected_task["name"] = UserName_var_edit.get().strip()
            selected_task["description"] = description_entry_edit.get().strip()
            selected_task["priority"] = priority_var_edit.get().strip()
            selected_task["due_date"] = due_date_combobox_edit.get_date().strftime('%Y-%m-%d')
            selected_task["comment"] = comment_entry_edit.get().strip()
            save_tasks()
            update_task_list()
            edit_window.destroy()
            messagebox.showinfo("Success", "Task edited successfully!")

        save_button = ttk.Button(edit_window, text="Save", command=save_edit)
        save_button.grid(row=5, columnspan=2, padx=5, pady=10)

# Function to mark a task as completed
def mark_completed():
    selected_item = task_tree.selection()
    if selected_item:
        index = int(task_tree.item(selected_item, 'values')[0]) - 1
        tasks[index]['completed'] = True
        save_tasks()
        update_task_list()

# Function to delete a task
def delete_task():
    selected_item = task_tree.selection()
    if selected_item:
        index = int(task_tree.item(selected_item, 'values')[0]) - 1
        del tasks[index]
        save_tasks()
        update_task_list()
        messagebox.showinfo("Success", "Task deleted successfully")
    else:
        messagebox.showerror("Error", "Please select a task to delete")

# Function to update the task list
def update_task_list():
    task_tree.delete(*task_tree.get_children())
    for i, task in enumerate(tasks, start=1):
        task_tree.insert("", "end", values=(i, task['name'], task['description'], task['due_date'], task['priority'], task['completed'], task.get('comment', '')))

# Function to update the clock
def update_clock():
    current_time = time.strftime("%Y-%m-%d, %H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(clock_update_interval, update_clock)

# Main function
def main():
    global tasks, task_tree, UserName_var, description_entry, due_date_combobox, priority_var, comment_entry, clock_label

    tasks = load_tasks()

    root = ThemedTk(theme="arc")
    root.title("Sonics Task Viewer")

    # Style configuration
    style =ttk.Style()
    style.configure("TLabel", background="#282c34", foreground="white", font=("Arial", 12, "bold"))
    style.configure("TEntry", background="#33373b", foreground="black", font=("Arial", 12, "bold"))
    style.configure("TButton", background="#7c56b8", foreground="black", font=("Arial", 12, "bold"))
    style.configure("TCombobox", background="#33373b", foreground="black", font=("Arial", 12, "bold"))
    style.configure("Treeview", background="#282c34", foreground="white", font=("Arial", 12, "bold"))
    style.configure("Treeview.Heading", background="#4e54c8", foreground="Black", font=("Arial", 12, "bold"))
    style.configure('Custom.TDateEntry',background='lightgray', foreground='black', fieldbackground='white', arrowscolor='blue', headerbackground='blue', headerforeground='white',bordercolor='blue', selectbackground='blue', selectforeground='white')

    image = Image.open("C:\\Users\\Bafana.Madume\\Bafana Madume capaciti Python\\.ipynb_checkpoints\\CR.png") 
    image = image.resize((230, 180))#, Image.ANTIALIAS)  
    photo = ImageTk.PhotoImage(image)
 
    # Create a label to display the image
    image_label = tk.Label(root, image=photo)
    image_label.image = photo  
    image_label.place(x=0,y=0)
    

    # Header label
    header_label = ttk.Label(root, text="SONICS TASK VIEWER", font=("impact", 30, "bold"), background="#f0f0f0", foreground="#258699")
    header_label.place(x=510, y=60)

    # Clock label
    clock_label = ttk.Label(root, font=("Impact", 16, "bold"), background="#f0f0f0", foreground="#258699")
    clock_label.place(x=1150, y=446)
    update_clock()

    # User Name combobox
    name_label = ttk.Label(root, text="User Name:", font=("Arial", 12, "bold"))
    name_label.place(x=1120, y=8)
    UserName_var = tk.StringVar(root)
    UserName_combobox = ttk.Combobox(root, textvariable=UserName_var, values=UserName_options, state="readonly")
    UserName_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="e")

    # Task Description entry
    description_label = ttk.Label(root, text="Task Description:", font=("Arial", 12, "bold"))
    description_label.place(x=1120, y=40)
    description_entry = ttk.Entry(root)
    description_entry.grid(row=1, column=1, padx=5, pady=5, sticky="e")

    # Priority combobox
    priority_label = ttk.Label(root, text="Priority:", font=("Arial", 12, "bold"))
    priority_label.place(x=1120, y=75)
    priority_var = tk.StringVar(root)
    priority_combobox = ttk.Combobox(root, textvariable=priority_var, values=priority_options, state="readonly")
    priority_combobox.grid(row=2, column=1, padx=5, pady=5, sticky="e")

    # Due Date combobox
    due_date_label = ttk.Label(root, text="Due Date:", font=("Arial", 12, "bold"))
    due_date_label.place(x=1120, y=110)
    due_date_combobox = DateEntry(root, date_pattern='yyyy-mm-dd', width=20)
    due_date_combobox.grid(row=3, column=1, padx=5, pady=5, sticky="e")

    # Comment entry
    comment_label = ttk.Label(root, text="Comment:", font=("Arial", 12, "bold"))
    comment_label.place(x=1120, y=145)
    comment_entry = ttk.Entry(root)
    comment_entry.grid(row=4, column=1, padx=5, pady=5, sticky="e")

    # Add task button
    add_button = ttk.Button(root, text="Add Task", command=add_task)
    add_button.place(x=435, y=444)

    # Edit task button
    edit_button = ttk.Button(root, text="Edit Task", command=edit_task)
    edit_button.place(x=575, y=444)

    # Delete task button
    delete_button = ttk.Button(root, text="Delete Task", command=delete_task)
    delete_button.grid(row=6, column=1, columnspan=2, sticky="e", padx=430, pady=10)

    # Mark as completed button
    mark_completed_button = ttk.Button(root, text="Mark Completed", command=mark_completed)
    mark_completed_button.place(x=715, y=444)

    # Task list with Treeview
    task_tree = ttk.Treeview(root, columns=("ID", "Name", "Description", "Due Date", "Priority", "Completed", "Comment"), show="headings")
    task_tree.heading("ID", text="ID")
    task_tree.heading("Name", text="User Name")
    task_tree.heading("Description", text="Task Description")
    task_tree.heading("Due Date", text="Due Date")
    task_tree.heading("Priority", text="Priority")
    task_tree.heading("Completed", text="Completed")
    task_tree.heading("Comment", text="Comment")
    task_tree.grid(row=5, column=0, columnspan=2)

    # Initialize task list
    update_task_list()

    root.mainloop()

if __name__ == "__main__":
    main()
