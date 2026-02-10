from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import time

grid_url = "http://192.168.1.11:4444"

browsers = {
    "Chrome": ChromeOptions(),
    "Firefox": FirefoxOptions(),
    "Edge": EdgeOptions()
}

for browser_name, options in browsers.items():
    print(f"\nRunning test on {browser_name}")

    driver = webdriver.Remote(
        command_executor=grid_url,
        options=options
    )

    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(2)

    print("Page Title:", driver.title)
    print("Browser:", driver.capabilities["browserName"])
    print("Platform:", driver.capabilities.get("platformName"))

    driver.quit()