import unittest
from window import Window
from db import Database
import os


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

