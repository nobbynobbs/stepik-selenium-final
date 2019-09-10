from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_into_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def should_be_success_message(self):
        message = "success message is not presented, but should be"
        assert self._is_element_present(*ProductPageLocators.SUCCESS_MESSAGE, timeout=1), message

    def should_not_be_success_message(self):
        message = "success message is presented, but should not be"
        assert self._is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE, timeout=1), message

    def success_message_should_disappear(self):
        message = "success message still present, but should disappear"
        assert self._is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), message

    def success_message_should_contain_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_IN_SUCCESS_MESSAGE).text
        message = "product name in the alert doesn't match product name in description"
        assert product_name == product_name_in_message, message

    def total_should_be_equal_to_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        info = self.browser.find_element(*ProductPageLocators.TOTAL_MESSAGE).text
        message = "total price in the alert doesn't match the product price"
        assert price in info, message
