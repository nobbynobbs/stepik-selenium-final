from selenium.webdriver.common.by import By

from pages.base import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        want_true = self._is_element_present(*MainPageLocators.LOGIN_LINK)
        error_msg = "Login link is not presented" 
        assert want_true, error_msg
