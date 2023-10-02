import unittest
from window import Window


class Test_main_window(unittest.TestCase):
    def test_window_params(self):
        wind = Window(800, 600, "birthdayapp",)
        self.assertEquals(wind.root.title, "birthdayapp")
