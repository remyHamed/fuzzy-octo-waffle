import datetime
import sqlite3
from pathlib import Path

from domain.classes.task import Task

class DbHandler():
    
    def __init__(self):
        self.db_path = Path("pomodoro.db")
        self._con = sqlite3.connect(self.db_path)
        self._cur = self._con.cursor()
        self._init_db()

    def _init_db(self):
        self._cur.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                creation_date DATETIME NOT NULL,
                resume TEXT,
                is_done BOOLEAN NOT NULL DEFAULT 0
            )
        """)
        self._con.commit()

    def save_task(self, task: Task) -> Task:
        self._cur.execute(
            "INSERT INTO tasks (title, creation_date, resume, is_done) VALUES (?, ?, ?, ?)",
            (task.title, task.creation_date, task.resume, task.is_done)
        )
        self._con.commit()

    def get_all_tasks(self, tasks_list :list):
        tasks_list.clear()
        self._cur.execute("SELECT id, title, creation_date, resume, is_done FROM tasks")
        for row in self._cur.fetchall():
            task = Task(
                title=row[1],
                creation_date=datetime.datetime.fromisoformat(row[2]),
                resume=row[3],
                is_done=bool(row[4])
            )
            tasks_list.append(task)
            
        return tasks_list
    
    def close(self):
        self._con.close()