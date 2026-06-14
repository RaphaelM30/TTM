from .task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description, status="Incomplete")
        self.tasks.append(task)
        return title

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return True
        return False

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_tasks_complete()
                return True
        return False
