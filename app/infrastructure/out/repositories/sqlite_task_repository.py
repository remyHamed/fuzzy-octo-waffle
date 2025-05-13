from pathlib import Path
import sqlite3

from app.dto.requests.create_task_request import CreateTaskRequest
from app.dto.responses.task_response import TaskResponse


class SqliteTaskRepository():
    
    def __init__(self) :
        self.db_path = Path("pomodoro.db")
        self._con = sqlite3.connect(self.db_path)
        self._cur = self._con.cursor()
        self._init_db()

    def _init_db(self) -> None:
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

    def save_task(self, task: CreateTaskRequest) -> TaskResponse:
        self._cur.execute(
            "INSERT INTO tasks (title, creation_date, resume, is_done) VALUES (?, ?, ?, ?)",
            (task.title, task.creation_date, task.resume, task.is_done)
        )
        self._con.commit()
        return TaskResponse(
            id=str(self._cur.lastrowid),
            title=task.title,
            status="done" if task.is_done else "pending"
        )

    def get_all_tasks(self, tasks_list :list) -> list:
        tasks_list.clear()
        self._cur.execute("SELECT id, title, creation_date, resume, is_done FROM tasks")
        for row in self._cur.fetchall():
            task = Task(
                id=row[0],
                title=row[1],
                creation_date=datetime.datetime.fromisoformat(row[2]),
                resume=row[3],
                is_done=bool(row[4])
            )
            tasks_list.append(task)
            
        return tasks_list
    
    def get_task(self, t: Task) -> Task:
        self._cur.execute("SELECT id, title, creation_date, resume, is_done FROM tasks WHERE id=?;", 
            (str(t._get_id()),)
        )
        t = self._cur.fetchone()
        return t
        
    def Update_task(self, t: Task, task_list: list) -> list:
        self._cur.execute(
            "UPDATE tasks SET title = ?, creation_date = ?, resume = ?, is_done = ? where id = ?;",
            (t._get_title(), t._get_creation_date(), t._get_resume(), t._get_is_done(), t._get_id())
        )
        self._con.commit()
        t = self.get_task(t)
        for i, task in task_list:
            if int(task._get_id()) == int(t._get_id()):
                task_list[i] = t
                break
        
        return task_list
    
    def close(self) -> None:
        self._con.close()