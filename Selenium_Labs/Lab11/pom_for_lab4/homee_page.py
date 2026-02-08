from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Shoppage:

    def __init__(self, driver):
        self.driver = driver

    # ---------- HOME PAGE LOCATORS ----------
    desktops_link = (By.LINK_TEXT, "Desktops")
    mac_link = (By.LINK_TEXT, "Mac (1)")
    search_box = (By.NAME, "search")
    search_button = (By.XPATH, "//*[@id='search']/span/button")

    # ---------- MAC PAGE LOCATORS ----------
    sort_dropdown = (By.ID, "input-sort")
    add_to_cart_button = (
        By.XPATH,
        '//*[@id="content"]/div[2]/div/div/div[2]/div[2]/button[1]'
    )

    # ---------- SEARCH PAGE LOCATORS ----------
    search_input = (By.ID, "input-search")
    description_checkbox = (By.ID, "description")
    button_search = (By.ID, "button-search")

    # ---------- HOME PAGE ACTIONS ----------
    def click_desktops(self):
        self.driver.find_element(*self.desktops_link).click()

    def click_mac(self):
        self.driver.find_element(*self.mac_link).click()

    def search_product(self, product_name):
        self.driver.find_element(*self.search_box).clear()
        self.driver.find_element(*self.search_box).send_keys(product_name)
        self.driver.find_element(*self.search_button).click()

    # ---------- MAC PAGE ACTIONS ----------
    def sort_by_name_a_to_z(self):
        dropdown = Select(self.driver.find_element(*self.sort_dropdown))
        dropdown.select_by_visible_text("Name (A - Z)")

    def add_mac_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    # ---------- SEARCH PAGE ACTIONS ----------
    def clear_search_input(self):
        self.driver.find_element(*self.search_input).clear()

    def enable_description_search(self):
        self.driver.find_element(*self.description_checkbox).click()

    def click_search_button(self):
        self.driver.find_element(*self.button_search).click()
