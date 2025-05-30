
from app.controller.task_controller import TaskController
from app.dto.requests.create_task_request import CreateTaskRequest
from app.presentation.cli.menu_displayer import MenuDisplayer

class MainMenu():
    
    
    def __init__(self, task_controller: TaskController, menu_displayer :MenuDisplayer):
        super().__init__()
        self._task_controller = task_controller
        self._menu_displayer = menu_displayer
    

    def display_menu(self) -> None:
        print(" Fuzzy octo waffle\n ")
        print("--- Taper le chiffre qui correspond à l'opperation désirer ---")
        print(" 1- Ajouter une task \n ")
        print(" 2- Modifier une task \n ")
        print(" 3- Supprimer une task\n ")
        print(" 4- Fin du programme \n ")

    
    def display_tasks(self) -> None:
        task_list = self._task_controller.get_all_tasks()
        self._menu_displayer.show_tasks(task_list)
    

    def get_input(sefl, message :str) -> None:
        user_input = input(message)
        return user_input
    

    def yes_or_not_input_catcher(self, question: str) -> bool:
        input_casted = 0

        while input_casted != 1 or input_casted != 2 :
            user_input = input(question)
            input_casted = int(user_input)
            
            if input_casted == 1:
                return True
            
            if input_casted == 2:
                return False
        
        
    def input_matcher(self, input: str) -> bool:
        match input:
            case "1":
                print("selection ajout de task\n")
                new_title = self.get_input("titre de la Task:\n")
                new_resume = self.get_input("Description de la Task:\n")
                create_task_request = CreateTaskRequest(new_title, new_resume)
                self._task_controller.create_new_task(create_task_request)
                return True
            case "2":
                print("modification de task\n")
                id_of_updated_task = self.get_input("selectionner l'id de l'app a modifier\n")
                task_to_update = self._task_controller.get_one_task(int(id_of_updated_task))
                update_title = None
                update_resume = None
                
                if task_to_update == None:
                    print("la task n'existe pas")
                    return True
                
                if self.yes_or_not_input_catcher("Changer le titre ?\n1 : oui \n2 : non \n"):
                    update_title = self.get_input("titre de la Task\n")
                
                if self.yes_or_not_input_catcher("Changer la description ?\n1 : oui \n2 : non \n"):
                    update_resume = self.get_input("Description de la Task:\n")

                if update_title != None:
                    task_to_update.title = update_title
                
                if update_resume != None:
                    task_to_update.resume = update_resume
                
                self._task_controller.update_task(task_to_update)
                
                return True
            case "3":
                print("suppretion de task\n")
                id_of_deleted_task = self.get_input("selectionner l'id de la tache à supprimer.\n")
                task_to_delete = self._task_controller.get_one_task(id_of_deleted_task)
                if task_to_delete == None:
                    print("la task n'existe pas")
                    return True
                self._task_controller.delete_task(task_to_delete)
                return True
            case "4":
                print("fin du programm\n")
                self._task_controller.close_db()
                return False
            case _:
                print("default")
                return True