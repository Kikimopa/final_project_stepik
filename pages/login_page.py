from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "No current login url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), 'No login form here'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FROM), "No register form here"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)
        password_input1 = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT1)
        password_input1.send_keys(password)
        password_input2 = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT2)
        password_input2.send_keys(password)
        registry_button = self.browser.find_element(*LoginPageLocators.REGISTRY_BUTTON)
        registry_button.click()
