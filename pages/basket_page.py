from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def check_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"

    def check_basket_text(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_TEXT).text[:18] == "Ваша корзина пуста", "Your basket is not empty"

