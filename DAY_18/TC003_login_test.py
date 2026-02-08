from selenium.webdriver.support.wait import WebDriverWait

from DAY_18.Loginpage import loginpage
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
# time.sleep(5)
loginobj = loginpage(driver)

loginobj.enterusername("Admin")
loginobj.enterpassword("admin123")

loginobj.clicklogin()




