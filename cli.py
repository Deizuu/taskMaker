from services.task_service import create_task
from services.task_service import update_task
from services.task_service import get_task_by_id
from models import Task
'''
Welcome to taskMaker.
What do you want to do?
1. Add task
2. List tasks
3. Rename task
4. Complete/Uncomplete a task
'''


def run_cli():
    # Loop variable, if running is True, the loop will continue
    running = True
    # What the user types in the terminal.
    user_prompt = ""
    print("""Welcome to taskMaker.\n
    What do you want to do?""")
    while running:
        print("""
            1. Create a task\n
            2. List all tasks\n
            3. Rename a task\n
            4. Complete/Uncomplete a task\n
            5. Exit the program""")
        user_prompt = input("Enter action number: ")

        match user_prompt[0]:
            case "1":
                title = input("Enter the title for the task: ")
                description = input(
                            "Enter task description (Leave empty if none): ")
                task = Task(title=title, description=description)
                create_task(task)
            case "2":
                pass

            case "3":
                pass

            case "4":
                pass

            case "5":
                pass

            case _:
                pass
    print("Goodbye!")
