class Tasks:
    def __init__(self, title, description, status="Incomplete"):
        self.title = title
        self.description = description
        self.status = status

    def mark_tasks_complete(self):
        self.status = "Complete"
