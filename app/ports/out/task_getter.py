from asyncio import Protocol
from typing import runtime_checkable

from app.domain.models.task import Task
from app.dto.responses.task_response import TaskResponse


@runtime_checkable
class TaskGetter(Protocol):
    def get_all_tasks(self) -> list[Task] | None:
        ...