from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Edge()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
driver.maximize_window()


driver.implicitly_wait(10)
print("Implicit wait applied")

wait = WebDriverWait(driver, 15)

login_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@value='Login']"))
)
print("Explicit wait: Login button is clickable")

fluent_wait = WebDriverWait(
    driver,
    timeout=20,
    poll_frequency=2,
    ignored_exceptions=[NoSuchElementException]
)

email_field = fluent_wait.until(
    EC.visibility_of_element_located((By.ID, "input-email"))
)

print("Fluent wait: Email field is available for interaction")


email_field.send_keys("test@example.com")
driver.find_element(By.ID, "input-password").send_keys("test123")
login_button.click()

print("Login action performed")
time.sleep(5)

driver.quit()