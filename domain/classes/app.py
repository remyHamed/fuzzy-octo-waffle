from domain.classes.db_handler import DbHandler
from domain.classes.main_menu import MainMenu

class App():

    def __init__(self):
        super().__init__()

    def run(self) -> None:

        boolean_runner = True
        menu_main = MainMenu()
        
        while boolean_runner:
            menu_main.display_tasks()
            menu_main.display_menu()
            boolean_runner = menu_main.input_matcher(menu_main.get_input("taper votre commande\n"))
        
        print("fin")
       

    
