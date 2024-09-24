"""
Task 2: Task Management System
"""


class Task:
    def __init__(self, title, description, status="open", due_date=None):
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due_date

    def __str__(self):
        return f"{self.title} [{self.status}]"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task_status(self, title, new_status):
        for task in self.tasks:
            if task.title == title:
                task.status = new_status
                break

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def list_tasks(self):
        return [str(task) for task in self.tasks]

    def filter_tasks_by_status(self, status):
        return [task for task in self.tasks if task.status == status]
