import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Day_20.driverfactory import get_driver


@pytest.mark.parametrize("browser", ["chrome", "edge", "firefox"])
def test_google(browser):
    driver = get_driver(browser)
    driver.get("https://www.google.com")

    WebDriverWait(driver, 10).until(EC.title_contains("Google"))
    assert "Google" in driver.title

    driver.quit()


@pytest.mark.parametrize("browser", ["chrome", "edge", "firefox"])
def test_google_search(browser):
    driver = get_driver(browser)
    driver.get("https://www.google.com")

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    search_box.send_keys("selenium grid")
    search_box.submit()

    WebDriverWait(driver, 10).until(
        EC.title_contains("selenium")
    )

    assert "selenium" in driver.title.lower()
    driver.quit()
