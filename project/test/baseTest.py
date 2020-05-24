import sys
import unittest

sys.path.append("./")

from project.pages.homePage.pageMethods import HomePage
from core.configs.driver import Driver


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()
        self.driver.start_app()
        self.home = HomePage()
