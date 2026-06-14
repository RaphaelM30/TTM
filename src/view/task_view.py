from .messages import Messages


class TaskView:

    def show_tasks(self, tasks):

        if not tasks:
            self.show_message(Messages.NO_TASKS)
            return

        self.show_message(Messages.TASK_LIST)

        for i, task in enumerate(tasks, start=1):
            print(
                f"{i}. "
                f"Title : {task.title}, "
                f"Description : {task.description}, "
                f"Status : {task.status}"
            )

    def show_message(self, message):
        print(message)
