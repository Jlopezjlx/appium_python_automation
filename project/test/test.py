import unittest
import sys
import time

sys.path.append("./")

from project.pages.homePage.pageMethods import HomePage
from project.utils.wait_utils import WaitUtils

home_page = HomePage()


def test_home_page(driver):
    home_page.clicking_create_an_account_button()
    time.sleep(4)
    driver.shutdown()

