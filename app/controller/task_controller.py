
from app.domain.services.task_service import TaskService
from app.dto.requests.create_task_request import CreateTaskRequest
from app.dto.responses.task_response import TaskResponse
from app.mappers.task_mapper import TaskMapper


class TaskController:

    def __init__(self, task_service: TaskService):
        self.task_service = task_service
        self.task_mapper = TaskMapper()


    def create_new_task(self, create_task_request : CreateTaskRequest) -> None:
        self.task_service.execute_task_creation(create_task_request)
        return
    
