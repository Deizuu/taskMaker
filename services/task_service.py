import sqlite3
from config import get_database_path
from models import Task


def create_task(task: Task):
    with sqlite3.connect(get_database_path()) as conn:
        c = conn.cursor()
        c.execute(
            "INSERT INTO tasks (title, description) VALUES (?, ?)",
            (task.title, task.description)
        )
        conn.commit()


def update_task(task: Task):
    with sqlite3.connect(get_database_path()) as conn:
        c = conn.cursor()
        c.execute(
            "UPDATE tasks SET title=?, description=?, completion=? WHERE id=?",
            (task.title, task.description, task.completion, task.id)
        )
        conn.commit()


def get_task_by_id(task_id: int):
    with sqlite3.connect(get_database_path()) as conn:
        c = conn.cursor()
        c.execute(
            "SELECT * FROM tasks WHERE id=?",
            (task_id,)
        )
        row = c.fetchone()
        if row:
            return Task(*row)
        return None
