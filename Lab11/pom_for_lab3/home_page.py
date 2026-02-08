from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ShopPage:

    def __init__(self, driver):
        self.driver = driver

    # ---------- HOME PAGE LOCATORS ----------
    desktops_menu = (By.LINK_TEXT, "Desktops")
    mac_link = (By.LINK_TEXT, "Mac (1)")

    # ---------- MAC PAGE LOCATORS ----------
    sort_dropdown = (By.ID, "input-sort")
    add_to_cart_button = (
        By.XPATH,
        '//*[@id="content"]/div[2]/div/div/div[2]/div[2]/button[1]'
    )

    # ---------- HOME PAGE ACTIONS ----------
    def open_desktops_menu(self):
        self.driver.find_element(*self.desktops_menu).click()

    def open_mac_page(self):
        self.driver.find_element(*self.mac_link).click()

    # ---------- MAC PAGE ACTIONS ----------
    def sort_products_name_a_to_z(self):
        dropdown = Select(self.driver.find_element(*self.sort_dropdown))
        dropdown.select_by_visible_text("Name (A - Z)")

    def add_mac_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()
