import math

from selenium.common.exceptions import (
    NoSuchElementException, NoAlertPresentException, TimeoutException
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote import webdriver


class BasePage():
    def __init__(self, browser: webdriver.WebDriver, url: str):
        self.browser = browser
        self.url = url

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
