from src.model.task_manager import TaskManager
from src.view.task_view import TaskView
from src.view.messages import Messages
from src.view.view_utils import *


def main():
    task_manager = TaskManager()
    task_view = TaskView()

    # Menu:
    print("Welcome to the Terminal Task Manager (TTM) !")

    while True:
        show_menu()

        user_choice = int(input("Enter your choice (1-5)"))

        match user_choice:
            case 1:
                line_break()
                title = input("Enter the task title : ")
                description = input("Enter the task description : ")
                task_manager.add_task(title, description)
                show_message(Messages.TASK_ADDED.format(title=title))

            case 2:
                line_break()
                title = input("Enter the task title : ")
                task_manager.mark_task_complete(title)
                show_message(Messages.TASK_COMPLETED.format(title=title))
            case 3:
                line_break()
                task_view.show_tasks(task_manager.tasks)

            case 4:
                line_break()
                title = input("Enter the task title : ")
                task_manager.delete_task(title)
                show_message(Messages.TASK_REMOVED.format(title=title))

            case 5:
                line_break()
                print("Goodbye ! ")
                return

            case _:
                line_break()
                print("Enter a valid number")


main()
