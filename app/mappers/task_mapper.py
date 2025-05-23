import datetime
from app.domain.models.task import Task
from app.dto.requests.create_task_request import CreateTaskRequest


class TaskMapper:

    def toTaskFromRequest(self,create_task_request : CreateTaskRequest)-> Task:
        return Task(
            None,
            create_task_request.title,
            datetime.datetime.now(), 
            create_task_request.resume
        )