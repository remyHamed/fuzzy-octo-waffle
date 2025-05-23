from app.controller.task_controller import TaskController
from app.domain.services.task_service import TaskService
from app.presentation.cli.main_menu import MainMenu
from app.presentation.cli.menu_view import MenuView
from app.repositories.task_repository import TaskRepository
class App():

    def __init__(self):
        super().__init__()
        self._task_repository = TaskRepository()
        self._task_service = TaskService(self._task_repository)
        self._task_controller = TaskController(self._task_service)
        self.menu_main = MainMenu(self._task_controller)


    def run(self) -> None:
        boolean_runner = True
        
        while boolean_runner:
            self.menu_main.display_tasks()
            self.menu_main.display_menu()
            boolean_runner = self.menu_main.input_matcher(self.menu_main.get_input("taper votre commande\n"))
        
        print("fin")


    
