import os
import tkinter as tk
from app.controller.task_controller import TaskController
from PIL import Image, ImageTk

class MainWindow:
    def __init__(self, taskController):
        self.root = tk.Tk()
        self._taskController = taskController

        self.root.title("Fenêtre avec fond dégradé")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.window_width = screen_width // 2
        self.window_height = screen_height // 2
        self.root.geometry(f"{self.window_width}x{self.window_height}+100+100")

        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, "../../../"))
        image_path = os.path.join(project_root, "assets", "background.jpg")
        self.original_image = Image.open(image_path)

        self.canvas = tk.Canvas(self.root, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.update_background(self.window_width, self.window_height)

        self.root.bind("<Configure>", self.on_resize)

    def update_background(self, width, height):
        resized_image = self.original_image.resize((width, height), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(resized_image)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

    def on_resize(self, event):
        if event.width != self.window_width or event.height != self.window_height:
            self.window_width = event.width
            self.window_height = event.height
            self.update_background(self.window_width, self.window_height)

    def run(self):
        self.root.mainloop()
