
from domain.classes.task import Task
import datetime

class MainMenu():
    
    def __init__(self):
        super().__init__()
        self._tasks_list = [Task("test", datetime.datetime.now(), "resume test", False) for i in range(100)]
    
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


    def get_task_list(self) -> None:
        return self.__tasks_list
    
    def input_matcher(self, input: str) -> bool:
        match input:
            case "1":
                print("selection ajout de task")
                return True
            case "2":
                print("modification de task")
                return True
            case "3":
                print("suppretion de task")
                return True
            case "4":
                print("fin du programm")
                return False
            case _:
                print("default")