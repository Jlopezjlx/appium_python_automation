import pytest

import sys

sys.path.append("./")

from core.configs.driver import Driver


@pytest.fixture
def driver():
    driver = Driver()
    driver.start_app()
    return driver
