import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()
print("title is", driver.title)

driver.get("https://www.google.com/")
print("title is", driver.title)
time.sleep(5)
driver.back()
print("title after back", driver.title)
driver.forward()
print("title after forward", driver.title)