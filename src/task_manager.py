from .tasks import Tasks


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Tasks(title, description, status="Incomplete")
        self.tasks.append(task)
        print(f"The Task '{title}' has correctly been added")

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"The Task '{title}' has correctly been removed")
                return
        print(f"No task with title '{title}' found.")

    def view_tasks(self):
        if self.tasks:
            print("Tasks : \n")
            for i, task in enumerate(self.tasks, start=1):
                print(
                    f"{i}. Title : {task.title}, Description : {task.description}, Status : {task.status}"
                )
        else:
            print("No tasks found.")

    def mark_tasks(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_tasks_complete()
                print(f"Task '{title}' marked as complete.")
                return
        print(f"No task with title '{title}' found.")
