
from app.domain.models.task import Task
from app.domain.services.task_service import TaskService
from app.dto.requests.create_task_request import CreateTaskRequest
from app.dto.requests.update_task_request import UpdateTaskRequest
from app.dto.responses.task_response import TaskResponse
from app.mappers.task_mapper import TaskMapper


class TaskController:

    def __init__(self, task_service: TaskService):
        self.task_service = task_service
        self.task_mapper = TaskMapper()


    def create_new_task(self, create_task_request : CreateTaskRequest) -> None:
        self.task_service.execute_task_creation(create_task_request)
        return
    
    def update_task(self, update_task_request : UpdateTaskRequest) -> None:
        self.task_service.execute_update_task(update_task_request)
        return
    
    def get_one_task(self, id :int)-> Task | None:
        return self.task_service.get_task(id)


    def get_all_tasks(self) -> list| None:
        return self.task_service.get_tasks()

    def delete_task(self,Task : Task) -> None:
        self.task_service.execute_delete_task(Task)
        return
    
    def close_db(self)-> None:
        self.task_service.close_data_base()