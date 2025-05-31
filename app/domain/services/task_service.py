import datetime
from app.domain.models.task import Task
from app.dto.requests.create_task_request import CreateTaskRequest
from app.dto.requests.update_task_request import UpdateTaskRequest
from app.repositories.task_repository import TaskRepository


class TaskService():

    def __init__(self, task_repository: TaskRepository ):
        self._task_repository = task_repository
    
    def execute_task_creation(self, create_taskR_request: CreateTaskRequest) -> Task:
        self._task_repository.save_task(
            Task(
                None,
                create_taskR_request.title,
                datetime.datetime.now(),
                create_taskR_request.resume
            )
        )
        return
    
    def execute_update_task(self, update_task_request : UpdateTaskRequest) -> Task:
        self._task_repository.update_task(
            Task(
                update_task_request.id,
                update_task_request.title,
                update_task_request.creation_date,
                update_task_request.resume,
                update_task_request.is_done
            )
        )
        return
        
    def execute_delete_task(self, t : Task) -> None:
        self._task_repository.execute_delete_task(t)
        return
    
    def get_task(self, id: int) -> Task | None:
        return self._task_repository.get_task(id)
    
    def get_tasks(self) -> list[Task] | None:
        return self._task_repository.get_all_tasks()
    
    def close_data_base(self) -> None:
        self._task_repository.close()