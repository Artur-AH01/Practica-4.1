from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import time

# Parametros para el webdriver
driver = webdriver.Chrome("./chromedriver_win32/chromedriver.exe")
driver.maximize_window()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")


action = ActionChains(driver)

# Diccionacion con los respectivos IDs de cada lista
Box = {
    '//*[@id="box1"]': '//*[@id="box101"]',
    '//*[@id="box2"]': '//*[@id="box102"]',
    '//*[@id="box3"]': '//*[@id="box103"]',
    '//*[@id="box4"]': '//*[@id="box104"]',
    '//*[@id="box5"]': '//*[@id="box105"]',
    '//*[@id="box6"]': '//*[@id="box106"]',
    '//*[@id="box7"]': '//*[@id="box107"]',
}

# Ciclo donde se encuentra el elemento en i y se encuentra el destino en j
# Se deja caer en el destino
for i, j in Box.items():
    element = driver.find_element(By.XPATH, i)
    element2 = driver.find_element(By.XPATH, j)
    action.drag_and_drop(element, element2).perform()
    time.sleep(3)
# Se cierra el navegador 
driver.quit()