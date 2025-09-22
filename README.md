# Task Management Application

This is a Python-based Task Management Application with a graphical user interface (GUI) built using `tkinter`. It allows users to create, edit, delete, and view tasks with attributes like title, description, due date, priority, and category. Tasks are stored persistently in a JSON file.

## Features

- Add new tasks with title, description, due date, priority, and category.
- Edit existing tasks.
- Delete tasks.
- View all tasks in a scrollable list.
- Persistent storage using JSON.
- Input validation for dates and required fields.
- User-friendly GUI with `tkinter`.

## File Structure

```
task_manager/
├── main.py              # Entry point to run the application
├── task.py             # Task class definition
├── storage.py          # Handles JSON file operations
├── ui.py               # GUI implementation with tkinter
├── utils.py            # Helper functions for validation and formatting
├── config.py           # Configuration settings
└── README.md           # Project documentation
```

## Setup Instructions

### Prerequisites

- Python 3.6 or higher.
- `tkinter` (included with standard Python installations).

### Installation

1. Clone or download the project files to a local directory.
2. No external dependencies are required beyond Python's standard library.

### Running the Application

1. Navigate to the `task_manager` directory.
2. Run the following command:
   ```
   python main.py
   ```
3. The GUI will open, allowing you to manage tasks.

### Data Storage

- Tasks are saved in `tasks.json` in the project directory.
- The file is created automatically when you add your first task.

## Usage

- **Add Task**: Fill in the task details (title, description, due date, priority, category) in the input fields and click "Add Task".
- **Edit Task**: Select a task from the list, modify the details in the input fields, and click "Update Task".
- **Delete Task**: Select a task from the list and click "Delete Task".
- **View Tasks**: All tasks are displayed in a scrollable list, showing title, due date, priority, and category.

## Development Notes

- The application uses `tkinter` for the GUI, making it cross-platform.
- Tasks are stored in a JSON file for simplicity and persistence.
- Input validation ensures valid dates and required fields.
- The code is modular, with separate concerns for task logic, storage, UI, and utilities.

## Example Task Data

Tasks are stored in `tasks.json` in the following format:

```json
[
  {
    "title": "Complete Project",
    "description": "Finish the task manager app",
    "due_date": "2025-10-01",
    "priority": "High",
    "category": "Work"
  }
]
```

## Future Improvements

- Add task filtering by category or priority.
- Implement task completion status.
- Add sorting options for the task list.
- Enhance the GUI with themes or additional styling.

## License

This project is licensed under the MIT License.