from app.controller.task_controller import TaskController
from app.domain.services.task_service import TaskService
from app.presentation.graphique.main_window import MainWindow
from app.repositories.task_repository import TaskRepository
class App():

    def __init__(self):
        super().__init__()
        self._task_repository = TaskRepository()
        self._task_service = TaskService(self._task_repository)
        self._task_controller = TaskController(self._task_service)
        self.main_window = MainWindow(self._task_controller)

    def run(self) -> None:
        self.main_window.run()

    
