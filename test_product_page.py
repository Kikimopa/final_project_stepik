from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
import time


@pytest.mark.need_review
@pytest.mark.parametrize('offer', ["?promo=offer0",
                                   # "?promo=offer1",
                                   # "?promo=offer2",
                                   # "?promo=offer3",
                                   # "?promo=offer4",
                                   # "?promo=offer5",
                                   # "?promo=offer6",
                                   # pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                   # "?promo=offer8",
                                   # "?promo=offer9"
                                   ])
def test_guest_can_add_product_to_basket(browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{offer}"
    page = MainPage(browser, link)
    page.open()
    cart = ProductPage(browser, browser.current_url)
    cart.product_price_and_name("Coders at Work", "19,99 £")
    cart.adding_to_cart()
    cart.solve_quiz_and_get_code()
    time.sleep(5)
    cart.product_price_and_name_after_adding_to_basket("Coders at Work", "19,99 £")


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    cart = ProductPage(browser, browser.current_url)
    cart.adding_to_cart()
    cart.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    cart = ProductPage(browser, browser.current_url)
    cart.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    cart = ProductPage(browser, browser.current_url)
    cart.adding_to_cart()
    cart.should_dissapear_of_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = ProductPage(browser, link)
    page.open()
    basket = BasketPage(browser, browser.current_url)
    basket.click_to_basket_from_main_page()
    basket.check_empty_basket()
    basket.check_basket_text()


@pytest.mark.negative
@pytest.mark.xfail
def test_guest_cant_see_product_in_basket_opened_from_product_page_negative(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = ProductPage(browser, link)
    page.open()
    basket = BasketPage(browser, browser.current_url)
    basket.click_to_basket_from_main_page()
    basket.negative_check_basket_text()
    basket.negative_check_basket_text()


class TestUserAddToBasketFromProductPage:
    # Я так и не понял, что надо было сделать в уроке 4.3.13
    # Наверно так и должно выглядеть

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.register_new_user(email=str(time.time()) + "@fakemail.org",
                                    password=str(time.time()) + "@fakemail.org")
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = MainPage(browser, link)
        page.open()
        cart = ProductPage(browser, browser.current_url)
        cart.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = MainPage(browser, link)
        page.open()
        cart = ProductPage(browser, browser.current_url)
        cart.product_price_and_name("Coders at Work", "19,99 £")
        cart.adding_to_cart()
        cart.solve_quiz_and_get_code()
        cart.product_price_and_name_after_adding_to_basket("Coders at Work", "19,99 £")
