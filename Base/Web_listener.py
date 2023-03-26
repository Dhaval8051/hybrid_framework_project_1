
#  -------------------    "https://www.linkedin.com/home  -------------------------- #

import pytest
from selenium import webdriver
class WebDriverWrapper:
    driver = None
    @pytest.fixture(scope="function", autouse=True)
    def browser_config(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.linkedin.com/home")
        yield
        self.driver.quit()
