import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("https://www.google.com.ar")

caja_de_busqueda = driver.find_element(By.ID, "APjFqb")
caja_de_busqueda.send_keys("fotos de gatitos" + Keys.ENTER)


time.sleep(5)
driver.quit()


print("hola mundis")