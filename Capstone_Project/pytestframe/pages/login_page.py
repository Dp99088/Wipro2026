from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
class LoginPage(BasePage):
    # Locators
    LOGIN_LINK = (By.LINK_TEXT, "Login")
    REGISTER_LINK = (By.LINK_TEXT, "Register")
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BTN = (By.CSS_SELECTOR, "input[value='Login']")
    WARNING_MSG = (By.CSS_SELECTOR, "div.alert-danger")
    
    # Registration Locators
    FIRST_NAME = (By.ID, "input-firstname")
    LAST_NAME = (By.ID, "input-lastname")
    REG_EMAIL = (By.ID, "input-email")
    TELEPHONE = (By.ID, "input-telephone")
    REG_PASSWORD = (By.ID, "input-password")
    CONFIRM_PASSWORD = (By.ID, "input-confirm")
    PRIVACY_POLICY = (By.NAME, "agree")
    CONTINUE_BTN = (By.CSS_SELECTOR, "input[value='Continue']")
    SUCCESS_MSG = (By.CSS_SELECTOR, "div#content h1")

    def navigate_to_login(self):
        self.click((By.LINK_TEXT, "My account"))
        self.click(self.LOGIN_LINK)

    def login(self, email, password):
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BTN)

    def get_warning_message(self):
        return self.get_text(self.WARNING_MSG)

    def data_register(self, first, last, email, phone, password):
        self.click((By.LINK_TEXT, "Continue")) # From login page to register
        self.send_keys(self.FIRST_NAME, first)
        self.send_keys(self.LAST_NAME, last)
        self.send_keys(self.REG_EMAIL, email)
        self.send_keys(self.TELEPHONE, phone)
        self.send_keys(self.REG_PASSWORD, password)
        self.send_keys(self.CONFIRM_PASSWORD, password)
        self.js_click(self.PRIVACY_POLICY)
        self.click(self.CONTINUE_BTN)

    def get_registration_success_message(self):
        self.wait.until(EC.title_contains("Account"))
        element = self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MSG)
        )
        return element.text
