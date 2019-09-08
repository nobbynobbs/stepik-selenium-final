from selenium.webdriver.common.by import By

from pages.base import BasePage


class MainPage(BasePage):
    
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        want_true = self._is_element_present(By.CSS_SELECTOR, "#login_link")
        error_msg = "Login link is not presented" 
        assert want_true, error_msg
