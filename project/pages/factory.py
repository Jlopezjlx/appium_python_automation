"""
BasePage
"""
import sys

sys.path.append("../")

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from allure_commons.types import AttachmentType
import allure
import datetime

from core.configs.driver import Driver
from core.configs.exceptions import NotAbleToCLickOrType, ElementNotFound, ElementNotDisplayed


class PageFactory(Driver):
    def find_element(self, by_locator):
        try:
            elem = self.driver.find_element(*by_locator)
            return elem
        except NoSuchElementException:
            raise ElementNotFound(by_locator)

    def element_is_displayed(self, by_locator):
        try:
            elem = self.driver.find_element(*by_locator)
            return elem.is_displayed()
        except Exception as error:
            raise ElementNotDisplayed(by_locator, error)

    def click_on(self, by_locator):
        try:
            self.driver.find_element(*by_locator).click()
        except TimeoutException:
            self.attach_screenshot()
            raise NotAbleToCLickOrType(by_locator)

    def type_in(self, by_locator, text):
        try:
            self.driver.find_element(*by_locator).send_keys(text)
        except TimeoutException:
            self.attach_screenshot()
            raise NotAbleToCLickOrType(by_locator)

    def get_text(self, by_locator):
        try:
            elem = self.driver.find_element(*by_locator)
            return elem.text
        except Exception as error:
            print(error)
            self.attach_screenshot()

    def attach_screenshot(self):
        """[Agrega screenshot a reporte en allure]
        """
        try:
            attachment_name = "screenshot {0}".format(datetime.datetime.now().isoformat())
            allure.attach(self.driver.get_screenshot_as_png(), name=attachment_name, attachment_type=AttachmentType.PNG)
        except Exception as e:
            print(e)
