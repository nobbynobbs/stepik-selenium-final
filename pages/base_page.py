import math

from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote import webdriver

from pages.locators import BasePageLocators


class BasePage():
    def __init__(self, browser: webdriver.WebDriver, url: str):
        self.browser = browser
        self.url = url

    def click_cart_button(self):
        cart_link = self.browser.find_element(*BasePageLocators.CART_LINK)
        cart_link.click()

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_authorized_user(self):
        err = "User icon is not presented, probably unauthorised user"
        assert self._is_element_present(*BasePageLocators.USER_ICON), err

    def should_be_login_link(self):
        want_true = self._is_element_present(*BasePageLocators.LOGIN_LINK)
        error_msg = "Login link is not presented"
        assert want_true, error_msg

    def open(self):
        self.browser.get(self.url)

    def _is_element_present(self, how, what, timeout=4):
        return not self._is_not_element_present(how, what, timeout)

    def _is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True
        return False

    def _is_disappeared(self, how, what, timeout=4):
        try:
            waiter = WebDriverWait(self.browser, timeout, 1, TimeoutException)
            waiter.until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
