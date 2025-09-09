from utils.cli import (
    handle_help,
    handle_task_completion,
    handle_task_creation,
    handle_task_deletion,
    handle_task_listing,
    handle_task_modification
)


def run_cli():
    # Loop variable, if running is True, the loop will continue
    running = True
    # What the user types in the terminal.
    user_prompt = ""
    print("Welcome to taskMaker.")
    while running:
        user_prompt = input('What do you want to do? (enter "h" for help): ')

        if not user_prompt:
            continue

        match user_prompt[0].lower():
            case "1":
                handle_task_creation()

            case "2":
                '''TODO print all tasks in the table
                for the user'''
                handle_task_modification()

            case "3":
                '''TODO print all tasks in the table
                for the user'''
                handle_task_completion()

            case "4":
                '''TODO make print() output
                readable'''
                handle_task_listing()

            case "5":
                '''TODO print all tasks in the table
                for the user'''
                handle_task_deletion()

            case "6":
                running = False

            case "h":
                # TODO print help
                handle_help()

            case _:
                pass
    print("Goodbye!")
