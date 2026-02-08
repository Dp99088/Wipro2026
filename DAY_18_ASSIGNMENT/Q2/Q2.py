from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


driver=webdriver.Firefox()
driver.implicitly_wait(10)
wait=WebDriverWait(driver,10)

driver.get("https://letcode.in/frame")
iframe=driver.find_element(By.TAG_NAME,"iframe")
driver.switch_to.frame(iframe)
driver.find_element(By.NAME,"fname").send_keys("Durga")
driver.find_element(By.NAME,"lname").send_keys("Prasad")
time.sleep(2)
driver.switch_to.default_content()
insight=driver.find_element(By.XPATH,"//p[text()=' Insight ']").is_displayed()
driver.quit()
print("Insight is displayed:",insight)