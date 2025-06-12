import os
import tkinter as tk
from app.controller.task_controller import TaskController
from PIL import Image, ImageTk

class MainWindow:
    def __init__(self, taskController: TaskController):
        self.root = tk.Tk()
        self.root.title("Fenêtre avec fond dégradé")
        self._taskController = taskController

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = screen_width // 2
        window_height = screen_height // 2
        self.root.geometry(f"{window_width}x{window_height}+100+100")

        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, "../../../"))
        image_path = os.path.join(project_root, "assets", "background.jpg")

        original_image = Image.open(image_path)
        resized_image = original_image.resize((window_width, window_height), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(resized_image)

        background_label = tk.Label(self.root, image=self.background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def run(self):
        self.root.mainloop()
