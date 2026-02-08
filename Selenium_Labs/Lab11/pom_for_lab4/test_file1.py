from selenium import webdriver
import time

from Selenium_Labs.Lab11.pom_for_lab4.homee_page import Shoppage

def test_lab4():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(3)

    shop = Shoppage(driver)

    # Navigate to Mac page
    shop.click_desktops()
    time.sleep(2)
    shop.click_mac()
    time.sleep(2)

    # Sort and add to cart
    shop.sort_by_name_a_to_z()
    time.sleep(2)
    shop.add_mac_to_cart()
    time.sleep(3)

    print("Mac product added to cart successfully")

    # Search Mobile
    shop.search_product("Mobile")
    time.sleep(2)
    shop.clear_search_input()
    shop.enable_description_search()
    shop.click_search_button()
    time.sleep(2)

    # Search Monitors
    shop.search_product("Monitors")
    time.sleep(2)
    shop.click_search_button()
    time.sleep(2)

    driver.close()
