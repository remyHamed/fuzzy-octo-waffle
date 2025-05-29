from asyncio import Protocol
from typing import runtime_checkable

from app.domain.models.task import Task


@runtime_checkable
class TaskDeleter(Protocol):
    def execute_delete_task(self, task: Task) -> None:
        ...
