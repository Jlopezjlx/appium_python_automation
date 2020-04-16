import unittest
import sys
import time

sys.path.append("./")

from core.configs.driver import Driver
from project.pages.homePage.pageMethods import HomePage
from project.utils.wait_utils import WaitUtils

driver = Driver()
waits = WaitUtils()
home_page = HomePage()


class TestFirst(unittest.TestCase):
    def test_home_page(self):
        driver.start_app()
        home_page.clicking_create_an_account_button()
        time.sleep(4)
        driver.shutdown()

