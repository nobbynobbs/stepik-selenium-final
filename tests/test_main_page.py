from pages.main import MainPage
from pages.login import LoginPage
from pages.cart_page import CartPage
from pages.cart_page import EMPTY_CART_MESSAGES


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_be_login_link()      # проверяем что есть ссылка для перехода на страницу логина
    page.go_to_login_page()          # переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, user_language):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.click_cart_button()
    cart_page = CartPage(browser, browser.current_url)
    expected_message = EMPTY_CART_MESSAGES[user_language]
    cart_page.cart_should_be_empty(expected_message)
