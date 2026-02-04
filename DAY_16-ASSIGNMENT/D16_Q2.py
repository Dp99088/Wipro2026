import time

from selenium import webdriver


driver=webdriver.Edge()
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()
print("title is", driver.title)

driver.get("https://tutorialsninja.com/demo/index.php?route=product/category&path=20_27")
print("title is", driver.title)
time.sleep(5)
driver.back()
print("title after back", driver.title)
driver.forward()
print("title after forward", driver.title)
driver.refresh()
print("title after refresh", driver.title)
driver.close()

