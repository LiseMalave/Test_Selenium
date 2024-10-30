from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# abrimos el navegador
driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

# seleccionamos los elementos

user = driver.find_element(By.ID,"user-name")

password = driver.find_element(By.ID,"password")

btn_login = driver.find_element(By.ID, "login-button" )

time.sleep(3)

user.send_keys("standard_user")

password.send_keys("secret_sauce")

btn_login.click()

time.sleep(3)

titulo = driver.find_element(By.CLASS_NAME, "app_logo")



assert titulo.text == "Swag Labs", "error"
assert driver.title == "Swag Labs", "otro eeror"


btn_hamburger = driver.find_element(By.ID, "react-burger-menu-btn")

btn_logout = driver.find_element(By.ID, "logout_sidebar_link")

time.sleep(5)

btn_hamburger.click()

time.sleep(5) 
btn_logout.click()

time.sleep(5)
