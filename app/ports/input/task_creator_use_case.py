from abc import ABC, abstractmethod
from asyncio import Task


class TaskCreatorUseCase(ABC):
    @abstractmethod
    def create_task(self, Task : Task) -> Task:
        pass