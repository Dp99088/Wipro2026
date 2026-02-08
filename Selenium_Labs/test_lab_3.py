from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Launch Edge browser
driver = webdriver.Edge()
driver.maximize_window()

# 1. Open URL
driver.get("https://tutorialsninja.com/demo/")
time.sleep(5)

# 2. Click on Desktops menu
driver.find_element(By.LINK_TEXT, "Desktops").click()
time.sleep(3)

# 3. Click on Mac (1)
driver.find_element(By.LINK_TEXT, "Mac (1)").click()
time.sleep(3)

# 4. Select Sort By → Name (A - Z)
sort_dropdown = Select(driver.find_element(By.ID, "input-sort"))
sort_dropdown.select_by_visible_text("Name (A - Z)")
time.sleep(2)



# 5. Click Add to Cart
driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(5)

print("Mac product added to cart successfully")

driver.quit()