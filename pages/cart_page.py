from pages.base_page import BasePage
from pages.locators import CartPageLocators

EMPTY_CART_MESSAGES = {
    "en": "Your basket is empty. Continue shopping",
    "ru": "Ваша корзина пуста Продолжить покупки",
    "fr": "Votre panier est vide. Continuer ses achats",
    "es": "Tu carrito esta vacío. Continuar sus compras",
}


class CartPage(BasePage):

    def cart_should_be_empty(self, empty_message):
        cart_content = self.browser.find_element(*CartPageLocators.CART_CONTENT)
        content_text = cart_content.text.strip()
        err = f"want {empty_message}, got {content_text}"
        assert cart_content.text == empty_message, err
