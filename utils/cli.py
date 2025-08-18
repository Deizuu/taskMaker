from models import Task
from services.task_service import (
    create_task,
    get_all_tasks,
    get_task_by_id,
    update_task
)


def prettify_task_output(task: Task):
    return (f"{task.title} | ",
            f"{"Completed" if task.completion else "Not Completed"}",
            f"\n {task.description}"
            )


def handle_task_creation():
    title = input("Enter the title for the task: ")
    desc = input(
        "Enter task description (Leave empty if none): ")
    task = Task(title=title, description=desc)
    create_task(task)


def handle_task_listing():
    print(get_all_tasks())


def handle_task_modification():
    # TODO fill in input prompts
    update_task(
        id=int(input()),
        title=input(),
        desc=input()
    )


def handle_task_completion():
    # TODO fill in input prompt
    id = int(input(
        "Enter the ID of the task you want to complete:"))
    task = get_task_by_id(id)
    if task is not None:
        update_task(
            id=id,
            completion=True if (
                task.completion is False
            ) else False
        )
