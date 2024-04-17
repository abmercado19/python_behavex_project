"""
Base Page Class for Page Object Model (POM)

It encapsulates common functionality and utilities used across multiple pages in the application.
The other page object classes should inherit from this class.

"""

from features.steps.pages.web_utils import WebUtils


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.web_utils = WebUtils(driver)

    def get_current_url(self):
        return self.driver.current_url
