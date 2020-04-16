"""
Common Methods
"""
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from allure_commons.types import AttachmentType
import allure
import time
import unittest
import datetime

from core.configs.driver import Driver

Driver = Driver()
Base = None


class CommonMethods(unittest.TestCase):
    """Clase de metodos comunes
    """

    @classmethod
    def setup(cls):
        cls.driver = Driver.driver
        return cls.driver

    def swipe(self, start_x, start_y, end_x, end_y, duration=None):
        """[Swipe en la pantalla actual]

        Arguments:
            start_x {[coordenadas]} -- [ex. 266]
            start_y {[coordenadas]} -- [ex. 266]
            end_x {[coordenadas]} -- [ex. 260]
            end_y {[coordenadas]} -- [ec. 260]

        Keyword Arguments:
            duration {[int]} -- [parametro opcional en segundos] (default: {None})
        """
        driver = self.setup()
        try:
            driver.swipe(start_x, start_y, end_x, end_y, duration)
        except TimeoutException:
            allure.attach(
                body=Base.driver.get_screenshot_as_png(),
                name='Swipe Error',
                attachment_type=allure.attachment_type.PNG)

    def get_direction(self, to, x, y_start, y_end):
        """[Get direction where to scroll]

        Arguments:
            to {[str]} -- [Direction, down or up]
            x {[int]} -- [position in x]
            y_start {[int]} -- [position in y]
            y_end {[int]} -- [position in y]
        """
        try:
            if to == "down":
                self.swipe(x, y_start, x, y_end)
            elif to == "up":
                self.swipe(x, y_end, x, y_start)
        except:
            self.fail("Prueba fallida obteniendo la direccion para scroll")

    def find_element(self, by, element, direction, x, y_start, y_end):
        """[Method to be able to find a element on page using scroll, just support ID and XPATH]

        Arguments:
            by {[str]} -- [method to be used to find element]
            element {[locator]} -- [description]
            direction {[str]} -- [Direction, down or up]
            x {[int]} -- [position in x]
            y_start {[int]} -- [position in y]
            y_end {[int]} -- [position in y]
        """
        try:
            timeout = time.time() + 25
            if by == "id":
                elm = Base.element_is_displayed(Base.find_element(element))
                while not elm:
                    if time.time() > timeout:
                        break
                    self.get_direction(
                        to=direction,
                        x=x,
                        y_start=y_start,
                        y_end=y_end
                    )
                    elm = Base.element_is_displayed(Base.find_element(element))
            elif by == "xpath":
                elm = Base.element_is_displayed(Base.find_element_by_xpath(element))
                while not elm:
                    if time.time() > timeout:
                        break
                    self.get_direction(
                        to=direction,
                        x=x,
                        y_start=y_start,
                        y_end=y_end
                    )
                    elm = Base.element_is_displayed(Base.find_element_by_xpath(element))
        except:
            self.fail("Prueba fallida en scroll until element")

    def scroll(self, direction: str, until_element: bool = False, element=None, by: str = "id"):
        """[Scroll/swipe on current page, just support UP & DOWN]

        Arguments:
            direction {str} -- [Direction where to scroll]

        Keyword Arguments:
            until_element {bool} -- [just use if this method will be used to find an element] (default: {False})
            element {[type]} -- [just use if this method will be used to find an element, locator of the element, XPATH or ID] (default: {None})
            by {str} -- [just use if this method will be used to find an element, method to use to find the element] (default: {"id"})
        """
        try:
            driver = self.setup()
            # getting current windows size
            size = driver.get_window_size()
            # calculating coordinates to swipe on this page
            y_start = int(size.get('height') * 0.7)
            y_end = int(size.get('height') * 0.3)
            x = int(size.get('width') / 2)
            # y_end = 0
            # x = 0
            # y_start = 0

            # verifying if swipe is being used to find an element or jus swipe
            if until_element:
                self.find_element(
                    by=by,
                    element=element,
                    direction=direction,
                    x=x,
                    y_start=y_start,
                    y_end=y_end
                )
            else:
                self.get_direction(
                    to=direction,
                    x=x,
                    y_start=y_start,
                    y_end=y_end
                )
        except:
            Base.attach_screenshot()
            Driver.shutdown()
            self.fail("Error en Scroll")
