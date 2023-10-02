import unittest
from window import Window
from db import Database
import datetime
import os
from reg import date_check


class TestMainWindow(unittest.TestCase):
    def test_window_params(self):
        wind = Window(800, 600, "birthdayapp")
        self.assertEqual(wind.window_title, "birthdayapp")
        self.assertEqual(wind.window_geometry, "800x600")

    def test_label_text(self):
        wind = Window(800, 600, "birthdayapp")
        self.assertEqual(wind.lab_title.cget("text"), "Birthday App")
        self.assertEqual(wind.lab_title.cget("font"), "Impact 30")

    def test_create_button(self):
        wind = Window(800, 600, "birthdayapp")
        self.assertIn("create_task", wind.create_button.cget("command"), "Error, Wrong function activaited!")


class TestDatabase(unittest.TestCase):
    def test_db_connection(self):
        test_db = Database("test")
        self.assertIsNotNone(test_db.con)

    def test_db_inout(self):
        d = Database("test")
        d.sql_insert_into_table(("DR", datetime.datetime.now().date()))
        self.assertEqual(d.sql_get_by_date("2023-10-02"), (1, 'DR', '2023-10-02'))

    def test_to_get_all_items_from_db(self):
        d = Database("test")
        d.sql_insert_into_table(("DR", "2023-10-01"))
        self.assertEqual(d.sql_get_all_items(), [(1, "DR", "2023-10-01")])


class ReDateCheck(unittest.TestCase):
    def test_date_check_if_letters(self):
        date = "aa-bb-cccc"
        self.assertFalse(date_check(date))

    def test_date_check_if_numbers(self):
        date = "2133413"
        self.assertFalse(date_check(date))

    def test_date_check_if_empty(self):
        date = ""
        self.assertFalse(date_check(date))