from tkinter import *
from reg import date_check
from db import Database


class CreateWindow:
    def __init__(self, parent, width, height, title, resizable=(False, False)):
        self.parent = parent
        self.root = Toplevel(parent)
        self.window_title = title
        self.root.title(self.window_title)
        self.window_geometry = f"{width}x{height}"
        self.root.geometry(self.window_geometry)
        self.root.resizable(resizable[0], resizable[1])
        self.lab_title = Label(self.root, text="Создать напоминание", font="Impact 15", pady=5)
        self.create_button = Button(self.root, text="Создать напоминание", width=20, height=2, command=self.finish_task)
        self.lab_event = Label(self.root, text="Событие:", font="Arial 10", pady=0)
        self.lab_date = Label(self.root, text="Дата:", font="Arial 10", pady=3)
        self.text_field = Entry(self.root, width=20)
        self.text_field_date = Entry(self.root, width=20)
        self.draw_widgets()
        self.grab_focus()

    def grab_focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()

    def draw_widgets(self):
        self.lab_title.pack(anchor="n")
        self.lab_event.pack(anchor="center")
        self.text_field.pack(anchor="center")
        self.lab_date.pack(anchor="center")
        self.text_field_date.pack(anchor="center")
        self.create_button.pack(side="bottom", pady=5)

    def finish_task(self):
        text = self.text_field.get()
        date = self.text_field_date.get()
        if date_check(date):
            db_con = Database("database.db")
            db_con.sql_insert_into_table((text, date))
            self.root.destroy()






