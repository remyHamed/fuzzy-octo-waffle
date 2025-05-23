# app/presentation/cli/menu_displayer.py
class MenuDisplayer:
    def show(self, options: dict) -> None:
        """Affiche le menu"""
        print("\n=== MENU ===")
        for key, label in options.items():
            print(f"{key}. {label}")
        print("============")
    
    def show_tasks(self, tasks: list) -> None:
        """Affiche la liste des tâches"""
        for task in tasks:
            print(f"→ {task['title']}: {task['description']}")
    
    def show_error(self, message: str) -> None:
        """Affiche les erreurs"""
        print(f"⚠️ {message}")