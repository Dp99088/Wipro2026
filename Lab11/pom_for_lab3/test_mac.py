from selenium import webdriver
import time

from Selenium_Labs.Lab11.pom_for_lab3.home_page import ShopPage

def test_mac():

    driver = webdriver.Edge()
    driver.maximize_window()

    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(3)

    shop = ShopPage(driver)

    shop.open_desktops_menu()
    time.sleep(2)

    shop.open_mac_page()
    time.sleep(2)

    shop.sort_products_name_a_to_z()
    time.sleep(2)

    shop.add_mac_to_cart()
    time.sleep(3)

    print("Mac product added to cart successfully")

    driver.quit()
