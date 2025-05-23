from asyncio import Protocol
from typing import runtime_checkable
from app.domain.models.task import Task
from app.dto.requests.update_task_request import UpdateTaskRequest


class TaskUpdaterUseCase(Protocol):
    @runtime_checkable
    def execute_update_task(self, update_task_request : UpdateTaskRequest) -> Task:
        ...