import tkinter as tk

class RoundedButton(tk.Canvas):
    def __init__(self, parent, text, command=None, radius=20, padding=10, width=150, height=40):
        super().__init__(parent, width=width, height=height, bg='white', highlightthickness=0)
        self.command = command
        self.radius = radius
        self.text = text
        self.button_color = "white"
        self.text_color = "black"
        self.border_color = "black"
        self.padding = padding

        # Dessine le bouton avec bords arrondis
        self.draw_button()

        # Lie les événements de clic
        self.tag_bind("button", "<Button-1>", self.on_click)
        self.tag_bind("text", "<Button-1>", self.on_click)
        

    def draw_button(self):
        r = self.radius
        w = int(self["width"])
        h = int(self["height"])
        self.create_round_rect(0, 0, w, h, r, fill=self.button_color, outline=self.border_color, tags="button")
        self.create_text(w // 2, h // 2, text=self.text, fill=self.text_color, font=("Helvetica", 12), tags="text")

    def create_round_rect(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = [
            x1+radius, y1,
            x2-radius, y1,
            x2, y1,
            x2, y1+radius,
            x2, y2-radius,
            x2, y2,
            x2-radius, y2,
            x1+radius, y2,
            x1, y2,
            x1, y2-radius,
            x1, y1+radius,
            x1, y1
        ]
        return self.create_polygon(points, smooth=True, **kwargs)

    def on_click(self, event):
        if self.command:
            self.command()
