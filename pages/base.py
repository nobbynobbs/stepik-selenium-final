from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote import webdriver


class BasePage():
    def __init__(self, browser: webdriver.WebDriver, url: str, timeout: int = 10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self.url = url

    def open(self): 
        self.browser.get(self.url)

    def _is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
