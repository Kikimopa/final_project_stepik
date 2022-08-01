from selenium.webdriver.common.by import By

class BasketPageLocators():
    BASKET = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    BASKET_TEXT = (By.XPATH, '//*[@id="content_inner"]/p')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FROM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ITEM = (By.TAG_NAME, "h1")
    PRICE = (By.CLASS_NAME, "price_color")
    ITEM_IN_BASKET = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRICE_IN_BASKET = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'alert-success')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
