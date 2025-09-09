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


def delete_task(id: int):
    with sqlite3.connect(get_database_path()) as conn:
        c = conn.cursor()
        c.execute(
            "DELETE FROM tasks where id=?",
            (id,)
        )


def get_all_tasks():
    with sqlite3.connect(get_database_path()) as conn:
        c = conn.cursor()
        c.execute(
            "SELECT * FROM tasks"
        )
        rows = c.fetchall()
        if rows:
            return rows
        return None


def get_task_by_id(task_id: int):
    with sqlite3.connect(get_database_path()) as conn:
        c = conn.cursor()
        c.execute(
            "SELECT title, description, completion FROM tasks WHERE id=?",
            (task_id,)
        )
        row = c.fetchone()
        if row:
            return Task(*row)
            return
        return None


def update_task(id: int, title=None, desc=None, completion=None):
    # TODO only take Task value as input (task: Task)
    fields = []
    values = []
    if title is not None:
        fields.append("title=?")
        values.append(title)
    if desc is not None:
        fields.append("description=?")
        values.append(desc)
    if completion is not None:
        fields.append("completion=?")
        values.append(completion)
    if not fields:
        raise ValueError("No fields to update.")
    values.append(id)
    sql = f"UPDATE tasks SET {', '.join(fields)} WHERE id=?"
    with sqlite3.connect(get_database_path()) as conn:
        c = conn.cursor()
        c.execute(sql, values)
        conn.commit()
