from asyncio import Protocol
from typing import runtime_checkable
from app.domain.models.task import Task


class TaskDeleterUseCase(Protocol):
    @runtime_checkable
    def delete_task(self, Task : Task) -> None:
        ...