from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test_lab5():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")

    act_title=driver.title
    exp_title="Your Store"
    print("title of the page is",act_title)

    driver.find_element(By.XPATH,"//*[@id='top-links']/ul/li[2]/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//*[@id='top-links']/ul/li[2]/ul/li[1]/a").click()
    driver.find_element(By.XPATH,'//*[@id="content"]/form/div/div/input[2]').click()
    time.sleep(5)
    driver.find_element(By.ID,"input-firstname").send_keys("Durga")
    driver.find_element(By.ID,"input-lastname").send_keys("Prasad")
    driver.find_element(By.ID,"input-email").send_keys("dp43_@gmail.com")
    driver.find_element(By.ID,"input-telephone").send_keys("9976544216")
    driver.find_element(By.ID,"input-password").send_keys("Password123")
    driver.find_element(By.ID,"input-confirm").send_keys("Password123")
    driver.find_element(By.XPATH,'//*[@id="content"]/form/fieldset[3]/div/div/label[1]/input').click()
    driver.find_element(By.XPATH,'//*[@id="content"]/form/div/div/input[1]').click()
    driver.find_element(By.XPATH,'//*[@id="content"]/form/div/div/input[2]').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="content"]/div/div/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="content"]/ul[1]/li[3]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="content"]/div/div[2]/a').click()
    time.sleep(1)
    driver.find_element(By.NAME,"firstname").send_keys("Durga")
    driver.find_element(By.NAME,"lastname").send_keys("Prasad")
    driver.find_element(By.ID,"input-address-1").send_keys("123-street")
    driver.find_element(By.ID,"input-city").send_keys("Hyderabad")
    driver.find_element(By.ID,"input-postcode").send_keys("500019")
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="input-country"]').click()
    driver.find_element(By.XPATH,'//*[@id="input-country"]/option[107]').click()
    driver.find_element(By.XPATH,'//*[@id="input-zone"]').click()
    driver.find_element(By.XPATH,'//*[@id="input-zone"]/option[3]').click()
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/form/div/div[2]/input').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[1]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="content"]/ul[2]/li[1]/a').click()
    time.sleep(5)
    driver.close()