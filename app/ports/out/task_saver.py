
from asyncio import Protocol


class TaskSaver(Protocol):
    def save(self, task_data: dict | TaskDTO) -> str: