from models import Task


def prettify_task_output(task: Task):
    return (f"{task.title} | ",
            f"{"Completed" if task.completion else "Not Completed"}",
            f"\n {task.description}"
            )
