from tkinter import *


class Window:
    def __init__(self, width, height, title, resizable=(False, False)):
        self.root = Tk()
        self.window_title = title
        self.root.title(self.window_title)
        self.window_geometry = f"{width}x{height}"
        self.root.geometry(self.window_geometry)
        self.root.resizable(resizable[0], resizable[1])

        self.
    def draw_widgets(self):
        pass

    def run(self):
        self.root.mainloop()




#wind = Window(1200, 600, "birthdayapp")
#wind.run()