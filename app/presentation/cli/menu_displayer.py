from app.domain.models.task import Task


class MenuDisplayer:
    def show(self, options: dict) -> None:
        print("\n=== MENU ===")
        for key, label in options.items():
            print(f"{key}. {label}")
        print("============")
    
    def show_tasks(self, tasks: list[Task]) -> None:
        for task in tasks:
            print(f"→ {task.id}: {task.title}: {task.resume}")
    
    def show_error(self, message: str) -> None:
        print(f"⚠️ {message}")