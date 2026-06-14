from src.task_manager import TaskManager


def main():
    task_manager = TaskManager()

    # Menu:
    print("Welcome to the Terminal Task Manager (TTM) !")

    while True:
        print("\nMenu :")
        print("1. Add tasks.")
        print("2. Mark task as complete.")
        print("3. View all tasks.")
        print("4. Delete task.")
        print("5. Exit.")

        user_choice = int(input("Enter your choice (1-5)"))

        match user_choice:
            case 1:
                print("\n")
                title = input("Enter the task title : ")
                description = input("Enter the task description : ")
                task_manager.add_task(title, description)

            case 2:
                print("\n")
                title = input("Enter the task title : ")
                task_manager.mark_tasks(title)

            case 3:
                print("\n")
                task_manager.view_tasks()

            case 4:
                print("\n")
                title = input("Enter the task title : ")
                task_manager.delete_task(title)

            case 5:
                print("Goodbye ! ")
                return

            case _:
                print("Enter a valid number")


main()
