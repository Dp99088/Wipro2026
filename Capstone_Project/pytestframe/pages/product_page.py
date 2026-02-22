from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class ProductPage(BasePage):
    # Use generic class selector to find all buttons, then filter in logic
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".button-cart")
    # Success message appears in a toast, not a standard alert div
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".toast-body")
    cart_btn_locator = "button-cart" # ID string for scroll

    def add_to_cart_with_handling(self):
        """Attempts to add to cart and handles stock/error scenarios."""
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BTN)
        
        # Scenario: Add to cart button not present (Out of Stock)
        if not buttons or not any(b.is_displayed() for b in buttons):
            print("sorry item is not available now try again after sometime")
            return "out_of_stock"
            
        # Scenario: Button present, try to click
        try:
            clicked = False
            for btn in buttons:
                if btn.is_displayed():
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
                    time.sleep(1)
                    btn.click() # Try standard click first
                    clicked = True
                    break
            
            if not clicked:
                 self.js_click(self.ADD_TO_CART_BTN)
            
            # Wait a moment for validation or toast to kick in
            time.sleep(3)
            
            # Check for validation errors (e.g. "Size required")
            errors = self.driver.find_elements(By.CSS_SELECTOR, ".text-danger")
            if errors and any(e.is_displayed() for e in errors):
                print("there is a problem while adding to cart")
                return "error"
            
            # Verify if success toast actually appeared
            if not self.get_success_message():
                print("there is a problem while adding to cart (no success message)")
                return "error"
                 
            return "success"
        except Exception as e:
            # Scenario: Unexpected problem while adding
            print("there is a problem while adding to cart")
            return "error"

    def get_success_message(self):
        try:
            # Use a shorter wait specifically for the check
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            wait = WebDriverWait(self.driver, 5)
            element = wait.until(EC.visibility_of_element_located(self.SUCCESS_ALERT))
            return element.text
        except:
            return ""
