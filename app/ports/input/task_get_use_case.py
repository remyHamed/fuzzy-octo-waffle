from asyncio import Protocol
from typing import runtime_checkable
from app.domain.models.task import Task

class TaskGetUseCase(Protocol):
    @runtime_checkable
    def get_task(self, id: int) -> Task:
        ...