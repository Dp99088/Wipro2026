from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class SearchPage(BasePage):
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BTN = (By.CSS_SELECTOR, "#search button")
    PRODUCT_THUMB = (By.CSS_SELECTOR, "div.product-thumb")
    PRODUCT_LINK = (By.CSS_SELECTOR, "div.caption h4 a")

    def search_product(self, product_name):
        self.send_keys(self.SEARCH_INPUT, product_name)
        # Use submit() as button click is unreliable
        self.find_element(self.SEARCH_INPUT).submit()
        # Wait for page to reload
        self.wait.until(EC.title_contains("Search"))

    def is_product_found(self):
        products = self.driver.find_elements(*self.PRODUCT_THUMB)
        return len(products) > 0

    def select_product(self):
        self.click(self.PRODUCT_LINK)
