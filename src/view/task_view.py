from .messages import Messages
from .view_utils import show_message


class TaskView:
    """Handles the display of tasks and messages to the user."""

    def show_tasks(self, tasks):
        """Function to show the tasks

        Args:
            tasks (list): A list of Task instances to display
        """
        if not tasks:
            show_message(Messages.NO_TASKS)
            return

        show_message(Messages.TASK_LIST)

        for i, task in enumerate(tasks, start=1):
            print(
                f"{i}. Title: '{task.title}', Description: '{task.description}', Status: '{task.status}'"
            )
