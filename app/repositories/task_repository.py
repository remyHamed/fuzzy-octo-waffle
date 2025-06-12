import datetime
from pathlib import Path
import shutil
import sqlite3
import os
import sys
from typing import Optional

from app.domain.models.task import Task




class TaskRepository():
    
    def __init__(self) :
        self._con: Optional[sqlite3.Connection] = None
        self._cur: Optional[sqlite3.Cursor] = None
        self._initialize_database()
        self._init_db()

    def _get_app_data_dir(self) -> Path:

        if os.name == 'nt':
            base_path = Path(os.getenv('LOCALAPPDATA'))
        else:
            base_path = Path.home() / '.local' / 'share'
        
        app_path = base_path / 'MonApplication'
        app_path.mkdir(exist_ok=True, parents=True)
        return app_path
    
    def _get_db_path(self) -> Path:
        return self._get_app_data_dir() / 'app_data.db'
    
    def _initialize_database(self) -> None:
        db_path = self._get_app_data_dir() / 'app_data.db'
        
        db_exists = db_path.exists()
        
        self._con = sqlite3.connect(db_path)
        self._cur = self._con.cursor()
        
        if not db_exists:
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

    def save_task(self, task: Task) -> Task | None:
        try:
            self._cur.execute(
                "INSERT INTO tasks (title, creation_date, resume, is_done) VALUES (?, ?, ?, ?)",
                (task.title, task.creation_date, task.resume, task.is_done)
            )
            self._con.commit()
            task.id = self._cur.lastrowid
            return task
        except Exception as e:
            print(f"Erreur lors de l'enregistrement de la tâche : {e}")
            self._con.rollback()
            return None


    def get_all_tasks(self) -> list[Task] | None:
        try:
            tasks_list = list()
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
        except Exception as e:
            print(f"Erreur lors de récupération des taches : {e}")
            return None
    
    def get_task(self, id : int) -> Task | None:
        try:
            self._cur.execute(
                "SELECT id, title, creation_date, resume, is_done FROM tasks WHERE id=?;",
                (id,)
            )
            row = self._cur.fetchone()
            if row is None:
                return None
            
            task = Task(
                id=row[0],
                title=row[1],
                creation_date=row[2],
                resume=row[3],
                is_done=bool(row[4])
            )
            return task
        except Exception as e:
            print(f"Erreur lors de la récupération de la tâche : {e}")
            return None
        
    def update_task(self, t: Task) -> Task | None:
        try:

            self._cur.execute(
                "UPDATE tasks SET title = ?, creation_date = ?, resume = ?, is_done = ? where id = ?;",
                (t.title, t.creation_date, t.resume, t.is_done, t.id)
            )
            self._con.commit()
            return t
        except Exception as e:
             print(f"Erreur update de la tâche : {e}")
             return None
    
    def execute_delete_task(self, t: Task) -> None:
        try:
            self._cur.execute(" DELETE FROM tasks WHERE id = ?;", (t.id,))
            return
        except Exception as e:
            print(f"Erreur de suppression de la tâche : {e}")
            return None
       
    
    def close(self) -> None:
        self._con.close()