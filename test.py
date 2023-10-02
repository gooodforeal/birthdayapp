import unittest
from window import Window


class TestMainWindow(unittest.TestCase):
    def test_window_params(self):
        wind = Window(800, 600, "birthdayapp",)
        self.assertEqual(wind.window_title, "birthdayapp")
        self.assertEqual(wind.window_geometry, "800x600")


