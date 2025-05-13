from abc import ABC, abstractmethod
from asyncio import Task


class TaskDeleterUseCase(ABC):
    @abstractmethod
    def delete_task(self, Task : Task) -> None:
        pass