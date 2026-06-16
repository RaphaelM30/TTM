from src.model.task import Task
import json


class DataManager:
    """Class to manage data operations."""

    def __init__(self, database_path):
        """Class initialisation

        Args:
            database_path (str): Path to the database file
        """
        self.database_path = database_path

    def save_data(self, data):
        """Save data to the database.

        Args:
            data (list): Data to be saved
        """
        tasks_list = []

        for task in data:
            dict_task = {
                "title": task.title,
                "description": task.description,
                "status": task.status,
            }
            tasks_list.append(dict_task)

        with open(self.database_path, "w") as file:
            json.dump({"Tasks": tasks_list}, file, indent=4)

    def load_data(self) -> list[Task]:
        """Load data from the database.

        Returns:
            list[Task]: A list of Task instances loaded from the database
        """

        try:
            with open(self.database_path, "r") as file:
                data = json.load(file)
                tasks_data = data.get("Tasks", [])
                tasks = []

                for task_data in tasks_data:
                    task = Task(
                        title=task_data["title"],
                        description=task_data["description"],
                        status=task_data["status"],
                    )
                    tasks.append(task)

                return tasks

        except FileNotFoundError:
            return []

    def remove_task(self, title):
        """Remove a task from the database.

        Args:
            title (str): Title of the task to be removed
        """

        tasks = self.load_data()

        new_tasks = []

        for task in tasks:
            if task.title != title:
                new_tasks.append(task)

        self.save_data(new_tasks)
