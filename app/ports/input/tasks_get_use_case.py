from asyncio import Protocol
from typing import runtime_checkable
from app.domain.models.task import Task

class TasksGetUseCase(Protocol):
    @runtime_checkable
    def get_tasks(self) -> list[Task]:
        ...