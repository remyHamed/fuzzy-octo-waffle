from asyncio import Protocol
from typing import runtime_checkable
from app.domain.models.task import Task
from app.dto.requests.create_task_request import CreateTaskRequest


class TaskCreatorUseCase(Protocol):
    @runtime_checkable
    def execute_task_creation(self, create_task_request : CreateTaskRequest) -> Task:
        ...