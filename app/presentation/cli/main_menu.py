
from app.controller.task_controller import TaskController
from app.dto.requests.create_task_request import CreateTaskRequest
from domain.models.task import Task

class MainMenu():
    
    
    def __init__(self, task_controller: TaskController):
        super().__init__()
        self._task_controller = task_controller
    

    def display_menu(self) -> None:
        print(" Fuzzy octo waffle\n ")
        print("--- Taper le chiffre qui correspond à l'opperation désirer ---")
        print(" 1- Ajouter une task \n ")
        print(" 2- Modifier une task \n ")
        print(" 3- Supprimer une task\n ")
        print(" 4- Fin du programme \n ")

    
    def display_tasks(self) -> None:
        if len(self._tasks_list) <= 0:
            return
        for i in self._tasks_list:
            print(i, end = '\n')
    

    def get_input(sefl, message :str) -> None:
        user_input = input(message)
        return user_input
    
    def get_task_controller(self) -> TaskController:
        return self._task_controller
    
    def set_task_controller(self, task_controller :TaskController) -> None:
        if not isinstance(task_controller, TaskController):
            raise TypeError("var must be set to an task_controller")
        self._task_controller = task_controller
    task_controller = property(get_task_controller, set_task_controller)
    

    def input_matcher(self, input: str) -> bool:
        match input:
            case "1":
                print("selection ajout de task\n")
                new_title = self.get_input("titre de la Task\n")
                new_resume = self.get_input("Description de la Task\n")
                create_task_request = CreateTaskRequest(new_title, new_resume)
                self._task_controller.create_new_task(create_task_request)
                return True
            case "2":
                print("modification de task\n")
                id_of_updat_task = self.get_input("selectionner l'id de l'app a modifier\n")
                t_to_update = Task()
                for task in self.get_task_list():
                    if task._get_id() == int(id_of_updat_task):
                        t_to_update = task
                    break
                self._db_h.Update_task(t_to_update, self.get_task_list())
                return True
            case "3":
                print("suppretion de task\n")
                return True
            case "4":
                print("fin du programm\n")
                self._db_h.close()
                return False
            case _:
                print("default")
                return True