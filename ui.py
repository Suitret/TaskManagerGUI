import tkinter as tk
from tkinter import messagebox, ttk
from task import Task
from utils import validate_date, PRIORITIES, CATEGORIES

class TaskManagerGUI:
    def __init__(self, root, storage):
        self.root = root
        self.storage = storage
        self.root.title("Task Manager")
        self.root.geometry("800x600")

        # Input fields
        self.create_input_fields()
        # Buttons
        self.create_buttons()
        # Task list
        self.create_task_list()

        # Load and display tasks
        self.refresh_task_list()

    def create_input_fields(self):
        # Frame for inputs
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        # Title
        tk.Label(input_frame, text="Title:").grid(row=0, column=0, padx=5, pady=5)
        self.title_entry = tk.Entry(input_frame, width=50)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        # Description
        tk.Label(input_frame, text="Description:").grid(row=1, column=0, padx=5, pady=5)
        self.desc_entry = tk.Text(input_frame, height=4, width=50)
        self.desc_entry.grid(row=1, column=1, padx=5, pady=5)

        # Due Date
        tk.Label(input_frame, text="Due Date (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5)
        self.due_date_entry = tk.Entry(input_frame, width=50)
        self.due_date_entry.grid(row=2, column=1, padx=5, pady=5)

        # Priority
        tk.Label(input_frame, text="Priority:").grid(row=3, column=0, padx=5, pady=5)
        self.priority_var = tk.StringVar(value=PRIORITIES[0])
        self.priority_menu = ttk.Combobox(input_frame, textvariable=self.priority_var, values=PRIORITIES, state="readonly")
        self.priority_menu.grid(row=3, column=1, padx=5, pady=5)

        # Category
        tk.Label(input_frame, text="Category:").grid(row=4, column=0, padx=5, pady=5)
        self.category_var = tk.StringVar(value=CATEGORIES[0])
        self.category_menu = ttk.Combobox(input_frame, textvariable=self.category_var, values=CATEGORIES, state="readonly")
        self.category_menu.grid(row=4, column=1, padx=5, pady=5)

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Task", command=self.add_task).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Update Task", command=self.update_task).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Delete Task", command=self.delete_task).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Clear Fields", command=self.clear_fields).pack(side=tk.LEFT, padx=5)

    def create_task_list(self):
        # Frame for task list
        list_frame = tk.Frame(self.root)
        list_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Treeview for tasks
        self.task_list = ttk.Treeview(
            list_frame,
            columns=("Title", "Due Date", "Priority", "Category"),
            show="headings",
            yscrollcommand=scrollbar.set
        )
        self.task_list.heading("Title", text="Title")
        self.task_list.heading("Due Date", text="Due Date")
        self.task_list.heading("Priority", text="Priority")
        self.task_list.heading("Category", text="Category")
        self.task_list.column("Title", width=300)
        self.task_list.column("Due Date", width=100)
        self.task_list.column("Priority", width=100)
        self.task_list.column("Category", width=100)
        self.task_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.task_list.yview)

        # Bind selection event
        self.task_list.bind("<<TreeviewSelect>>", self.on_task_select)

    def add_task(self):
        title = self.title_entry.get().strip()
        description = self.desc_entry.get("1.0", tk.END).strip()
        due_date = self.due_date_entry.get().strip()
        priority = self.priority_var.get()
        category = self.category_var.get()

        # Validate inputs
        if not title:
            messagebox.showerror("Error", "Title is required.")
            return
        if not validate_date(due_date):
            messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
            return

        task = Task(title, description, due_date, priority, category)
        self.storage.add_task(task)
        self.refresh_task_list()
        self.clear_fields()
        messagebox.showinfo("Success", "Task added successfully.")

    def update_task(self):
        selected = self.task_list.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a task to update.")
            return

        index = int(self.task_list.index(selected[0]))
        title = self.title_entry.get().strip()
        description = self.desc_entry.get("1.0", tk.END).strip()
        due_date = self.due_date_entry.get().strip()
        priority = self.priority_var.get()
        category = self.category_var.get()

        # Validate inputs
        if not title:
            messagebox.showerror("Error", "Title is required.")
            return
        if not validate_date(due_date):
            messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
            return

        task = Task(title, description, due_date, priority, category)
        self.storage.update_task(index, task)
        self.refresh_task_list()
        self.clear_fields()
        messagebox.showinfo("Success", "Task updated successfully.")

    def delete_task(self):
        selected = self.task_list.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a task to delete.")
            return

        index = int(self.task_list.index(selected[0]))
        self.storage.delete_task(index)
        self.refresh_task_list()
        self.clear_fields()
        messagebox.showinfo("Success", "Task deleted successfully.")

    def clear_fields(self):
        self.title_entry.delete(0, tk.END)
        self.desc_entry.delete("1.0", tk.END)
        self.due_date_entry.delete(0, tk.END)
        self.priority_var.set(PRIORITIES[0])
        self.category_var.set(CATEGORIES[0])

    def refresh_task_list(self):
        # Clear current list
        for item in self.task_list.get_children():
            self.task_list.delete(item)

        # Populate with tasks
        for task in self.storage.get_tasks():
            self.task_list.insert("", tk.END, values=(
                task["title"],
                task["due_date"],
                task["priority"],
                task["category"]
            ))

    def on_task_select(self, event):
        selected = self.task_list.selection()
        if not selected:
            return

        index = int(self.task_list.index(selected[0]))
        task = self.storage.get_tasks()[index]

        # Populate fields with selected task
        self.clear_fields()
        self.title_entry.insert(0, task["title"])
        self.desc_entry.insert("1.0", task["description"])
        self.due_date_entry.insert(0, task["due_date"])
        self.priority_var.set(task["priority"])
        self.category_var.set(task["category"])
