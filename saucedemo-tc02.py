from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

user = driver.find_element(By.ID, "user-name")

user.send_keys("testing_user")

password= driver.find_element(By.ID, "password")

password.send_keys("secret_sauce")


btn_login = driver.find_element(By.ID, "login-button")

btn_login.click()

time.sleep(4)

message = driver.find_element(By.CSS_SELECTOR, ".error-message-container > h3:nth-child(1)")

assert message.text == "Epic sadface: Username and password do not match any user in this service", "eeroor"


time.sleep(4)
