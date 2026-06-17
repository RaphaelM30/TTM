from .task import Task
from .data.data_manager import DataManager


class TaskManager:
    """Manages a collection of tasks, allowing for adding, deleting, and marking tasks as complete."""

    def __init__(self):
        self.tasks = DataManager("src/model/data/database.json").load_data()
        self.data_manager = DataManager("src/model/data/database.json")

    def add_task(self, title, description, priority) -> str:
        """Function to add a new task to the task manager.

        Args:
            title (str): title of the task
            description (str): description of the task
            priority (int): priority of the task

        Returns:
            str: The title of the added task
        """
        if title and description:
            task = Task(title, description, priority, status="Incomplete")
            self.tasks.append(task)
            self.data_manager.save_data(self.tasks)
            return title

    def delete_task(self, title) -> bool:
        """Function to delete a task from the task manager.

        Args:
            title (str): title of the task to delete

        Returns:
            bool: True if the task was deleted, False otherwise
        """

        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                self.data_manager.remove_task(title)
                return True
        return False

    def mark_task_complete(self, title) -> bool:
        """Function to mark a task as complete.

        Args:
            title (str): title of the task to mark as complete

        Returns:
            bool: True if the task was marked as complete, False otherwise
        """

        for task in self.tasks:
            if task.title == title:
                task.mark_tasks_complete()
                self.data_manager.save_data(self.tasks)
                return True
        return False

    def change_task_priority(self, title, new_priority) -> bool:
        """Function to change the priority of a task.

        Args:
            title (str): title of the task to change priority
            new_priority (int): new priority value

        Returns:
            bool: True if the task's priority was changed, False otherwise
        """

        for task in self.tasks:
            if task.title == title:
                task.priority = new_priority
                self.data_manager.save_data(self.tasks)
                return True
        return False
