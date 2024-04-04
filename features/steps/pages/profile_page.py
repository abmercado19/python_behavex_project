from selenium.webdriver.common.by import By

from features.steps.pages.base_page import BasePage


class ProfilePage(BasePage):

    user_name_label = (By.ID, "userName-value")

    def __init__(self, driver):
        super().__init__(driver)

    def get_user_name_displayed(self):
        user_name_displayed = self.web_utils.find_element(*self.user_name_label).text
        return user_name_displayed
