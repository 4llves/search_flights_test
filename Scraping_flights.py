import os
import re
import subprocess
from selenium import webdriver
import time as t
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  # Importe a classe By

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get('https://www.google.com/travel/flights/')

t.sleep(5)

# Encontre um elemento usando XPath
departures = driver.find_element(By.XPATH, "//input[@value='Tucuruí']")
departures.click()
departures.send_keys("BEL")

t.sleep(2)  # Aguarde um pouco para que os resultados sejam exibidos

driver.quit()