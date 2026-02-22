from selenium.webdriver.common.by import By
from .base_page import BasePage

class AccountPage(BasePage):
    MY_ACCOUNT_DROPDOWN = (By.LINK_TEXT, "My account")
    LOGOUT_LINK = (By.LINK_TEXT, "Logout")
    LOGOUT_HEADER = (By.CSS_SELECTOR, "h1") # Should say "Account Logout"

    def logout(self):
        self.click(self.MY_ACCOUNT_DROPDOWN)
        self.click(self.LOGOUT_LINK)

    def is_logged_out(self):
        return "Account Logout" in self.get_title()

    def is_logged_in(self):
        # If 'Logout' link is present, user is likely logged in
        return self.is_visible(self.LOGOUT_LINK)
