from utils.cli import (
    handle_task_completion,
    handle_task_creation,
    handle_task_listing,
    handle_task_modification
)


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
            3. Modify a task\n
            4. Complete/Uncomplete a task\n
            5. Exit the program""")
        user_prompt = input("Enter action number: ")

        if not user_prompt:
            print("Input cannot be empty. Please enter a valid value.")
            continue

        match user_prompt[0]:
            case "1":
                handle_task_creation()

            case "2":
                '''TODO make print() output
                readable'''
                handle_task_listing()

            case "3":
                '''TODO print all tasks in the table
                for the user'''
                handle_task_modification()

            case "4":
                handle_task_completion()

            case "5":
                running = False

            case _:
                pass
    print("Goodbye!")
