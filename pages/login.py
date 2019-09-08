from pages.base import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "url must contain 'login' substring"

    def should_be_login_form(self):
        error_message = "login form is not presented on page"
        assert self._is_element_present(*LoginPageLocators.LOGIN_FORM), error_message

    def should_be_register_form(self):
        error_message = "register form is not presented on page"
        assert self._is_element_present(*LoginPageLocators.REGISTER_FORM), error_message
