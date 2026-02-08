from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from DAY_18_ASSIGNMENT.Q1.Login_Page import Login_page
import time

def test_login():
    driver = webdriver.Edge()
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 10)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    loginobj = Login_page(driver)
    loginobj.enterusername("Admin")
    loginobj.enterpassword("admin123")
    loginobj.clicklogin()
    time.sleep(3)
    driver.quit()