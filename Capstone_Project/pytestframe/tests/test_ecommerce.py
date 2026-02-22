import pytest
import random
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.account_page import AccountPage
from utilities.utils import get_csv_data
import os

# Load data
data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'test_data.csv')
test_data = get_csv_data(data_path)

@pytest.mark.parametrize("data", test_data)
class TestEcommerce:
    # State management for granular steps
    emails = {}        
    stock_status = {}  
    is_registered = {} 

    @pytest.fixture(autouse=True)
    def setup_pages(self, driver):
        self.login_page = LoginPage(driver)
        self.search_page = SearchPage(driver)
        self.product_page = ProductPage(driver)
        self.cart_page = CartPage(driver)
        self.account_page = AccountPage(driver)

    def get_data_index(self, data):
        return test_data.index(data)

    def test_01_invalid_login(self, data, step):
        idx = self.get_data_index(data)
        step(f"Scenario {idx} for User: {data['first_name']} {data['last_name']}")
        
        step("Navigate to Login page")
        self.login_page.navigate_to_login()
        
        step("Attempt login with unique invalid credentials")
        unique_invalid = f"invalid_{random.randint(1000, 9999)}@email.com"
        self.login_page.login(unique_invalid, "wrongpass")
        
        step("Check for login warning message")
        warning = self.login_page.get_warning_message()
        print(f"Warning Message: {warning}")
        assert "Warning" in warning or "No match" in warning, f"Expected warning message but got: {warning}"

    def test_02_registration(self, data, step):
        idx = self.get_data_index(data)
        step(f"Register New User for Row {idx}")
        
        email = data['email'].replace("{random}", str(random.randint(1000, 9999)))
        TestEcommerce.emails[idx] = email
        step(f"Generated randomized email: {email}")
        
        step(f"Submit registration for {data['first_name']} {data['last_name']}")
        self.login_page.data_register(
            data['first_name'], 
            data['last_name'], 
            email, 
            data['phone'], 
            data['password']
        )
        
        step("Verify account creation success message")
        success_msg = self.login_page.get_registration_success_message()
        print(f"Registration Status: {success_msg}")
        
        success = "Created" in success_msg
        TestEcommerce.is_registered[idx] = success
        assert success, f"Registration failed. Message: {success_msg}"

    def test_03_logout_login(self, data, step):
        idx = self.get_data_index(data)
        if not TestEcommerce.is_registered.get(idx):
             pytest.skip("Registration failed, skipping follow-up login")

        email = TestEcommerce.emails[idx]
        step(f"Logout after registration and re-login as {email}")
        
        try:
            self.account_page.logout()
            step("Initial logout successful")
        except:
            step("Logout not required or handled via redirect")
            
        step("Navigate back to Login page")
        self.login_page.navigate_to_login()
        
        step(f"Logging in with credentials: {email} / {data['password']}")
        self.login_page.login(email, data['password'])
        
        step("Verify user is now logged in")
        assert self.account_page.is_logged_in(), "Login verification failed: Logout link not visible"

    def test_04_search_and_add_to_cart(self, data, step):
        idx = self.get_data_index(data)
        product = data['product_name']

        step(f"Search for product: {product}")
        self.search_page.search_product(product)

        if not self.search_page.is_product_found():
            step("Product not found in search results")
            pytest.fail(
                "Product is not found, Please search different product available in the page."
            )

        self.search_page.select_product()
        step(f"Product '{product}' found and selected")

        step("Check availability and attempt 'Add to Cart'")
        status = self.product_page.add_to_cart_with_handling()
        TestEcommerce.stock_status[idx] = status

        if status == "success":
            step("Item successfully added to cart")
            success = self.product_page.get_success_message()
            print(f"Cart Message: {success}")
        elif status == "out_of_stock":
            step("Item is out of stock (Verified: 'sorry' message or missing button)")
        elif status == "error":
            step("There was a problem adding to cart (likely required options/validation)")
        elif status == "not_found":
            pytest.fail("Product disappeared during selection attempt.")

    def test_05_cart_management(self, data, step):
        idx = self.get_data_index(data)
        status = TestEcommerce.stock_status.get(idx)
        if status != "success":
            step(f"Skipping cart management as product add status was: {status}")
            pytest.skip(f"No items in cart (Status: {status})")

        step(f"Navigate to Shopping Cart and update quantity to {data['quantity']}")
        self.cart_page.navigate_to_cart()
        self.cart_page.edit_quantity(data['quantity']) 
        step(f"Quantity updated to {data['quantity']}")
        
        step("Remove item from cart")
        self.cart_page.remove_item()
        
        step("Verify 'Empty Cart' message is displayed")
        empty_msg = self.cart_page.get_empty_cart_message()
        print(f"Empty Cart Message: {empty_msg}")
        assert "empty" in empty_msg.lower(), f"Expected empty cart message, but got: {empty_msg}"
        
        step("Navigate back to store via 'Continue' button")
        self.cart_page.continue_shopping()

    def test_06_logout(self, data, step):
        step("Final logout and session cleanup")
        try:
            self.account_page.logout()
            step("Logout executed")
        except:
            step("Logout attempt failed or session already expired")
            
        step("Verify final logout status (Title check)")
        assert self.account_page.is_logged_out(), "Final logout verification failed"
        step("Session terminated successfully")
