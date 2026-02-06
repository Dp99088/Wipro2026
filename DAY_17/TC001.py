from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://www.google.com")
print(driver.title)
driver.quit()
