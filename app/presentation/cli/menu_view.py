
class MenuView:
    def show_menu(self, options: dict) -> None:
        print("\n" + "="*20)
        for key, label in options.items():
            print(f"{key}. {label}")
        print("="*20)

    def show_tasks(self, tasks: list) -> None:
        for task in tasks:
            print(f"[{task['id']}] {task['title']} - {task['description']}")

    def show_message(self, message: str) -> None:
        print(message)