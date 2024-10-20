from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# abro el navegador

driver = webdriver.Chrome()

# defino q se maximiza

driver.maximize_window()

# abre la pagina q vamos a automatizar
driver.get("https://institutoweb.com.ar/test/login.html")


# carga de los elementos de la página en base a sus selectores

usuario = driver.find_element (By.ID, "tuusuario")

clave = driver.find_element (By.ID, "tuclave" ) 

email = driver.find_element (By.ID, "tumail")

btn_ingresar = driver.find_element (By.CSS_SELECTOR, "body > form > button:nth-child(8)" )


# acciones de la 1º pagina

usuario.send_keys("lucas")

clave.send_keys("1234")

email.send_keys("lucas@gmail.com")
time.sleep(4)
btn_ingresar.click()

# carga de los elementos de la segunda página en base a sus selectores


lnk_cerrarSesión = driver.find_element(By.ID, "volver")
h3_titulo =driver.find_element(By.CSS_SELECTOR,"body > h3:nth-child(1)")

# acciones de la 2º pagina

assert h3_titulo.text == "Acceso correcto!", "fallo, el h3 no es igual al texto esperado"

time.sleep(4)

lnk_cerrarSesión.click()