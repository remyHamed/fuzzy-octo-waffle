from asyncio import Protocol
from typing import runtime_checkable
from app.domain.models.task import Task

@runtime_checkable
class TaskUpdater(Protocol):
    def Update_task(self, t: Task) -> Task | None:
        ...