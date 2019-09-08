from pages.base import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_into_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()
    
    def success_message_should_contain_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGES).text
        assert product_name in message
        
    def total_should_be_equal_to_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        info = self.browser.find_element(*ProductPageLocators.TOTAL_MESSAGE).text
        assert price in info
