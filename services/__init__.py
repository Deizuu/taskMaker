import sqlite3

with sqlite3.connect("tasks.db") as conn:
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        completion BOOLEAN NOT NULL DEFAULT 0
        )""")
