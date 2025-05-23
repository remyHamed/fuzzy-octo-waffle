
from asyncio import Protocol
from typing import runtime_checkable

from app.dto.requests.create_task_request import CreateTaskRequest
from app.dto.responses.task_response import TaskResponse


class TaskSaver(Protocol):

    @runtime_checkable
    def save_task(self, task_data: dict | CreateTaskRequest) -> TaskResponse:
        ...