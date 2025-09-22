import json
import os

class Storage:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return data if isinstance(data, list) else []
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_tasks(self, tasks):
        with open(self.file_path, 'w') as file:
            json.dump(tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append(task.to_dict())
        self.save_tasks(self.tasks)

    def update_task(self, index, task):
        self.tasks[index] = task.to_dict()
        self.save_tasks(self.tasks)

    def delete_task(self, index):
        self.tasks.pop(index)
        self.save_tasks(self.tasks)

    def get_tasks(self):
        return self.tasks
