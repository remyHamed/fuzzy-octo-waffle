from app.ports.input.task_creator_use_case import TaskCreatorUseCase
from app.ports.input.task_deleter_use_case import TaskDeleterUseCase
from app.ports.input.task_get_use_case import TaskGetUseCase
from app.ports.input.task_updater_use_case import TaskUpdaterUseCase


class TaskService(
    TaskCreatorUseCase,
    TaskDeleterUseCase,
    TaskGetUseCase,
    TaskUpdaterUseCase
    ):

    def __init__(self, task_repository):
        self._task_repository = task_repository
    
    def create_task(self, Task):
        return self._task_repository.save(task)