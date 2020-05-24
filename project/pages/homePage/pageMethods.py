import sys

sys.path.append("./")

from project.pages.homePage.locators import Locators
from project.pages.factory import PageFactory
from project.utils.wait_utils import WaitUtils

waits = WaitUtils()


class HomePage(PageFactory):
    def clicking_create_an_account_button(self):
        try:
            waits.wait_for(by_locator=Locators.create_account_button)
            self.click_on(by_locator=Locators.create_account_button)
        except Exception as error:
            self.shutdown()
            self.fail(f'Error trying to click on create an account button, {error}')
