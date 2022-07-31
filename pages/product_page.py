from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):

    def adding_to_cart(self):
        login_link = self.browser.find_element(*ProductPageLocators.BUTTON)
        login_link.click()

    def should_be_link_to_cart(self):
        assert self.browser.find_element(*ProductPageLocators.BUTTON), "No basket here"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        # try:
        #     alert = self.browser.switch_to.alert
        #     alert_text = alert.text
        #     print(f"Your code: {alert_text}")
        #     alert.accept()
        # except NoAlertPresentException:
        #     print("No second alert presented")

    def product_price_and_name(self, name, price):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM).text

        item_price = self.browser.find_element(*ProductPageLocators.PRICE).text
        assert price == item_price, "The price is not expected"
        assert name == item_name, "Name of book is not expected"

    def product_price_and_name_after_adding_to_basket(self, name, price):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_IN_BASKET).text
        item_price = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text

        assert price == item_price, "The price is not expected"
        assert name == item_name, "Name of book is not expected"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"



