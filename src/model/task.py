from dataclasses import dataclass


@dataclass
class Task:
    """Represents a task with a title, description, and status."""

    title: str
    description: str
    priority: int = 1
    status: str = "Incomplete"

    def mark_tasks_complete(self):
        """Marks the task as complete.

        Args:
            self: The instance of the Task class.
        """
        self.status = "Complete"
