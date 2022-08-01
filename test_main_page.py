from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
import pytest
import time



link = "http://selenium1py.pythonanywhere.com"

# def test_guest_can_go_to_login_page(browser):
#
#     page = MainPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()


# def test_should_be_see_login_link(browser):
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    basket = BasketPage(browser, browser.current_url)
    basket.click_to_basket_from_main_page()
    basket.check_empty_basket()
    time.sleep(5)
    basket.check_basket_text()




