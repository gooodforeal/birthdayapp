from tkinter import *


class Window:
    def __init__(self, width, height, title, resizable=(False, False)):
        self.root = Tk()
        self.window_title = title
        self.root.title(self.window_title)
        self.window_geometry = f"{width}x{height}"
        self.root.geometry(self.window_geometry)
        self.root.resizable(resizable[0], resizable[1])
        self.lab_title = Label(self.root, text="Birthday App", font="Impact 30")

    def draw_widgets(self):
        self.lab_title.pack(anchor="n")

    def run(self):
        self.draw_widgets()
        self.root.mainloop()




#wind = Window(1200, 600, "birthdayapp")
#wind.run()