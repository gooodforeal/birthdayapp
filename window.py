from tkinter import *
from createwindow import CreateWindow
from db import Database


class Window:
    def __init__(self, width, height, title, resizable=(False, False)):
        self.list_of_dates = []
        self.root = Tk()
        self.window_title = title
        self.root.title(self.window_title)
        self.window_geometry = f"{width}x{height}"
        self.root.geometry(self.window_geometry)
        self.root.resizable(resizable[0], resizable[1])
        self.lab_title = Label(self.root, text="Birthday App", font="Impact 30")
        self.create_button = Button(text="Создать напоминание", width=100, height=2, command=self.create_task)

    def draw_widgets(self):
        self.lab_title.pack(anchor="n")
        self.create_button.pack(side="bottom", pady=25)

    def create_task(self):
        create_window = CreateWindow(self.root, 300, 200, "Создание напоминания", (False, False))

    def draw_list(self):
        db_con = Database("database.db")
        all_lines_from_db = db_con.sql_get_all_items()
        if len(all_lines_from_db) > len(self.list_of_dates):
            max_l = all_lines_from_db
            min_l = self.list_of_dates
            self.list_of_dates = all_lines_from_db
        elif len(all_lines_from_db) < len(self.list_of_dates):
            min_l = all_lines_from_db
            max_l = self.list_of_dates
        else:
            max_l = all_lines_from_db
            min_l = self.list_of_dates
        diff = sorted(list(set(max_l) - set(min_l)))
        for el in diff:
            number = Label(self.root, text=f"{el[0]}. {el[1]} -> {el[2]}", font="Arial 16")
            number.pack(anchor="center")
        self.root.after(1000, self.draw_list)

    def run(self):
        self.draw_widgets()
        self.draw_list()
        self.root.mainloop()
        self.root.after(1000, self.draw_list)


wind = Window(1200, 600, "birthdayapp")
wind.run()