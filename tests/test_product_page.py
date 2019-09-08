from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_into_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_into_cart()
    page.solve_quiz_and_get_code()
    page.success_message_should_contain_product_name()
    page.total_should_be_equal_to_price()
