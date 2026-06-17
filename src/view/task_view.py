from .messages import Messages
from .view_utils import show_message
from prettytable import PrettyTable


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

        table = PrettyTable()
        table.field_names = ["Title", "Description", "Priority", "Status"]

        for task in tasks:
            table.add_row([task.title, task.description, task.priority, task.status])

        print(table)
