from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import Select
import time


def test_lab4():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Desktops").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Mac (1)").click()
    time.sleep(3)
    sort_dropdown = Select(driver.find_element(By.ID, "input-sort"))
    sort_dropdown.select_by_visible_text("Name (A - Z)")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div/div[2]/div[2]/button[1]').click()
    time.sleep(5)
    print("Mac product added to cart successfully")
    driver.find_element(By.NAME, "search").send_keys("Mobile")
    driver.find_element(By.XPATH, "//*[@id='search']/span/button").click()
    time.sleep(2)
    driver.find_element(By.ID,"input-search").clear()
    driver.find_element(By.ID,"description").click()
    driver.find_element(By.ID,"button-search").click()
    time.sleep(2)
    driver.find_element(By.NAME, "search").send_keys("Monitors")
    driver.find_element(By.XPATH, "//*[@id='search']/span/button").click()
    driver.find_element(By.ID,"button-search").click()
    time.sleep(2)
    driver.close()

