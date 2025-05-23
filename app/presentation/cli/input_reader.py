
class InputReader:

    def read_choice(self) -> str:
        return input("Votre choix: ").strip()
    
    def read_new_task(self) -> tuple[str, str]:
        title = input("Titre: ").strip()
        description = input("Description: ").strip()
        return title, description