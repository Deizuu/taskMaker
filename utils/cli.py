from models import Task
from services.task_service import (
    create_task,
    delete_task,
    get_all_tasks,
    get_task_by_id,
    update_task
)

# Function possibly not needed
#def prettify_task_output(task: Task):
#    return (f"{task.title} | ",
#            f"{"Completed" if task.completion else "Not Completed"}",
#            f"\n {task.description}"
#            )


def handle_task_creation():
    title = input("Enter the title for the task: ")
    desc = input(
        "Enter task description (Leave empty if none): ")
    task = Task(title=title, description=desc)
    create_task(task)


def handle_task_listing():
    print(get_all_tasks())


def handle_task_modification():
    # TODO check if title/description is empty
    # If empty, leave the name as-is
    id = int(input("Enter task ID: "))
    task = get_task_by_id(id)
    if task is not None:
        update_task(
            id=id,
            title=input("Enter new title: "),
            desc=input("Enter new description: ")
        )


def handle_task_completion():
    id = int(input("Enter task ID: "))
    task = get_task_by_id(id)
    if task is not None:
        update_task(
            id=id,
            completion=True if not task.completion else False
        )


def handle_task_deletion():
    id = int(input(
        'Enter the ID of the task you want to delete (type "0" if none): '
    ))
    if id == 0:
        return
    delete_task(id)


def handle_help():
    print("""
        1. Create a task\n
        2. Modify a task\n
        3. Complete/Uncomplete a task\n
        4. List all tasks\n
        5. Delete a task\n
        6. Exit the program""")
