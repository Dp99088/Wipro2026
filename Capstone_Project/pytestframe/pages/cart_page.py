from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
import time

class CartPage(BasePage):
    # Updated locators based on user request and debug results
    CART_ICON = (By.CSS_SELECTOR, ".widget-cart a")
    VIEW_CART_LINK = (By.LINK_TEXT, "View Cart")
    EDIT_CART_LINK = (By.PARTIAL_LINK_TEXT, "Edit cart")
    QUANTITY_INPUT = (By.CSS_SELECTOR, "input[name^='quantity']")
    UPDATE_BTN = (By.CSS_SELECTOR, "button[title='Update'], button[data-original-title='Update']")
    REMOVE_BTN = (By.CSS_SELECTOR, "button[title='Remove'], button[data-original-title='Remove']")
    EMPTY_MSG = (By.CSS_SELECTOR, "div#content p")
    CONTINUE_BTN = (By.LINK_TEXT, "Continue")

    def navigate_to_cart(self):
        # User request: wait 15s until popup disappears
        print("Waiting 15s for popup to disappear...")
        time.sleep(15)
        
        # User request: scroll up
        print("Scrolling to top...")
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        
        # User request: click on shopping cart icon
        print("Clicking shopping cart icon...")
        try:
            # Try standard click first to trigger drawer event
            self.click(self.CART_ICON)
        except:
            self.js_click(self.CART_ICON)
        
        # Wait for drawer animation
        time.sleep(3)
        
        # User request: click on edit cart
        print("Clicking Edit cart...")
        # Broad search to find the link regardless of case or whitespace
        all_links = self.driver.find_elements(By.TAG_NAME, "a")
        clicked = False
        for link in all_links:
            text = link.get_attribute("textContent").lower()
            if "edit" in text and "cart" in text:
                print(f"Found link with text: '{link.text}'")
                self.driver.execute_script("arguments[0].click();", link)
                clicked = True
                break
        
        if not clicked:
             # Fallback to the toast link if header icon navigation failed
             print("Edit cart link not found in header, próbujemy 'View Cart' link...")
             try:
                 view_cart = self.driver.find_element(By.LINK_TEXT, "View Cart")
                 self.driver.execute_script("arguments[0].click();", view_cart)
                 clicked = True
             except:
                 raise Exception("Could not find 'Edit cart' or 'View Cart' link")
        
        # Synchronization: Wait for page to load
        if clicked:
            self.wait.until(EC.title_contains("Shopping Cart"))
            print("Navigated to Shopping Cart page")

    def edit_quantity(self, qty):
        self.send_keys(self.QUANTITY_INPUT, qty)
        self.click(self.UPDATE_BTN)
        # Wait for update (spinner or page reload)
        time.sleep(2) # Simple wait for demo, better to wait for specific element change

    def remove_item(self):
        self.click(self.REMOVE_BTN)
        time.sleep(2) # Wait for removal

    def get_empty_cart_message(self):
        return self.get_text(self.EMPTY_MSG)

    def continue_shopping(self):
        self.click(self.CONTINUE_BTN)
