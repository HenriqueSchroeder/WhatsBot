import unittest
from Chrome import Chrome
import time


class TestChrome(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.chrome = Chrome()

    def test_abertura(self):
        self.chrome.get("https://www.google.com/")
        time.sleep(2)
        self.assertEqual(self.chrome.title, "Google")

    @classmethod
    def tearDownClass(self):
        self.chrome.quit()
