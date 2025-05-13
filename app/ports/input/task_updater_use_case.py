from abc import ABC, abstractmethod
from asyncio import Task


class TaskUpdaterUseCase(ABC):
    @abstractmethod
    def update_task(self, Task : Task) -> Task:
        pass