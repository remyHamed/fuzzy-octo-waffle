from abc import ABC, abstractmethod
from asyncio import Task


class TaskGetUseCase(ABC):
    @abstractmethod
    def get_task(self, Task : Task) -> Task:
        pass