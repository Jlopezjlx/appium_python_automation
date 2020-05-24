import unittest
import sys
import time

sys.path.append("./")

from project.test.baseTest import BaseTest


class TestHome(BaseTest):
    def test_home_page(self):
        self.home.clicking_create_an_account_button()
        time.sleep(4)
        self.driver.shutdown()
