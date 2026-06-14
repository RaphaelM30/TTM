from dataclasses import dataclass


@dataclass
class Task:
    title: str
    description: str
    status: str = "Incomplete"

    def mark_tasks_complete(self):
        self.status = "Complete"
