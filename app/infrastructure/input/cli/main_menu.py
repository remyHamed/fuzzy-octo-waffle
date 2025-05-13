
from app.infrastructure.out.repositories.db_handler import DbHandler
from domain.models.task import Task

class MainMenu():
    
    
    def __init__(self):
        super().__init__()
        self._db_h = DbHandler()
        self._tasks_list = list()
    

    def display_menu(self) -> None:
        print(" Fuzzy octo waffle\n ")
        print("--- Taper le chiffre qui correspond à l'opperation désirer ---")
        print(" 1- Ajouter une task \n ")
        print(" 2- Modifier une task \n ")
        print(" 3- Supprimer une task\n ")
        print(" 4- Fin du programme \n ")

    
    def display_tasks(self) -> None:
        self._db_h.get_all_tasks(self._tasks_list)
        if len(self._tasks_list) <= 0:
            return
        for i in self._tasks_list:
            print(i, end = '\n')
    

    def get_input(sefl, message :str) -> None:
        user_input = input(message)
        return user_input


    def get_task_list(self) -> None:
        return self._tasks_list
    

    def input_matcher(self, input: str) -> bool:
        match input:
            case "1":
                print("selection ajout de task\n")
                nw_t = Task()
                nw_t._set_title(self.get_input("titre de la Task\n"))
                nw_t._set_resume(self.get_input("Description de la Task\n"))
                self._db_h.save_task(nw_t)
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