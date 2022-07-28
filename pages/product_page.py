from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def adding_to_cart(self):
        login_link = self.browser.find_element(*ProductPageLocators.BUTTON)
        login_link.click()

    def should_be_link_to_cart(self):
        assert self.browser.find_element(*ProductPageLocators.BUTTON), "No cart here"
