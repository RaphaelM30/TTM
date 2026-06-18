from src.model.data.data_manager import DataManager
from src.model.task import Task
from src.model.task_manager import TaskManager
from src.view.task_view import TaskView
from src.view.messages import Messages
from src.view.view_utils import *


def main():
    task_manager = TaskManager()
    task_view = TaskView()

    print("Welcome to the Terminal Task Manager (TTM) !")

    while True:
        show_menu()

        user_choice = int(input("Enter your choice (1-5)"))

        match user_choice:
            case 1:
                line_break()
                title = input("Enter the task title : ")
                description = input("Enter the task description : ")
                priority = int(input("Enter the task priority (1-5) : "))
                if task_manager.add_task(title, description, priority):
                    show_message(Messages.TASK_ADDED.format(title=title))
                else:
                    show_message(Messages.TASK_NOT_ADDED.format(title=title))

            case 2:
                line_break()
                title = input("Enter the task title : ")
                status = int(input("Enter the new status (1-Complete, 2-In Progress, 3-To do) : "))
                if task_manager.change_task_status(title, status):
                    show_message(Messages.TASK_STATUS_CHANGED.format(title=title))
                else:
                    show_message(Messages.TASK_NOT_STATUS_CHANGED.format(title=title))
            case 3:
                line_break()
                task_view.show_tasks(task_manager.tasks)

            case 4:
                line_break()
                title = input("Enter the task title : ")
                if task_manager.delete_task(title):
                    show_message(Messages.TASK_REMOVED.format(title=title))
                else:
                    show_message(Messages.TASK_NOT_FOUND.format(title=title))

            case 5:
                title = input("Enter the task title : ")
                new_priority = int(input("Enter the new priority (1-5) : "))
                if task_manager.change_task_priority(title, new_priority):
                    show_message(
                        Messages.TASK_PRIORITY_CHANGED.format(
                            title=title, priority=new_priority
                        )
                    )
                else:
                    show_message(Messages.TASK_NOT_PRIORITY_CHANGED.format(title=title))

            case 6:
                print("Goodbye ! ")

                return

            case _:
                line_break()
                print("Enter a valid number")


main()
