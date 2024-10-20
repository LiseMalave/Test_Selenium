from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# abrimos el navegador

driver = webdriver.Chrome()

# seleccionamos los elementos

user = driver.find_element(By.ID, "userName")

userEmail = driver.find_element(By.ID, "userEmail")

address = driver.find_element(By.ID, "currentAddress")

permanentAddress = driver.find_element(By.ID, "permanentAddress")

btn_submit = driver.find_element(By.ID, "submit")

message = driver.find_element(By.CSS_SELECTOR, "div.col-12:nth-child(2) > div:nth-child(4)")

# ingresamos datos

user.send_keys("Luca")
userEmail.send_keys("luca@gmail.com")
address.send_keys("Rivadavia - argentina")
permanentAddress.send_keys("Av dorrego 1234")

time.sleep(3)
btn_submit.click()


# hacemos la aserción para verificar

assert message == Name