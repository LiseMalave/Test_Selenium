from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# abrimos el navegador

driver = webdriver.Chrome()



driver.get("https://demoqa.com/text-box")

# seleccionamos los elementos
time.sleep(3)
user = driver.find_element(By.ID, "userName")

userEmail = driver.find_element(By.ID, "userEmail")

address = driver.find_element(By.ID, "currentAddress")

permanentAddress = driver.find_element(By.ID, "permanentAddress")

btn_submit = driver.find_element(By.ID, "submit")



# ingresamos datos

user.send_keys("Luca")
userEmail.send_keys("luca@gmail.com")
address.send_keys("Rivadavia - argentina")
permanentAddress.send_keys("Av dorrego 1234")


btn_submit.click()


time.sleep(5)

message = driver.find_element(By.ID, "email") 

# verificamos

if ("luca@gmail.com" in message.text):
   print("el texto se encuentra")

time.sleep(3)
driver.close()