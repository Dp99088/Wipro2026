from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://letcode.in/alert")

time.sleep(5)

driver.find_element(By.ID, "accept").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

time.sleep(5)

driver.find_element(By.ID, "confirm").click()
alert = driver.switch_to.alert
print(alert.text)
alert.dismiss()

time.sleep(5)

driver.find_element(By.ID, "prompt").click()
alert = driver.switch_to.alert
alert.send_keys("Durga Prasad")
print(alert.text)
alert.accept()

time.sleep(5)

result = driver.find_element(By.ID, "myName").text
print(result)

driver.quit()