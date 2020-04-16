from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from core.configs.driver import Driver
from core.configs.exceptions import ElementNotFound


class WaitUtils(Driver):
    def wait_for(self, by_locator, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(by_locator))
        except TimeoutException:
            raise ElementNotFound(by_locator)

    def wait_for_element(self, by_locator, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(by_locator))
        except TimeoutException:
            raise ElementNotFound(by_locator)


if __name__ == '__main__':
    print("Driver")
