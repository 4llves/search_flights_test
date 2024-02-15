import os
import re
import subprocess
from selenium import webdriver
import time as t
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui as py

text_in_departures = "Tucuruí" #str(input('Insira o nome da cidade que inicia seu site: '))
input_departures = "BEL" #str(input('Digite as siglas do aeroporto de partida: '))
text_in_arrivals = "Para onde?"
input_arrivals = "GRU"


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get('https://www.google.com/travel/flights/')

t.sleep(5)

# Encontre um elemento usando XPath
departures = driver.find_element(By.XPATH, "(//div[contains(@class, 'e5F5td BGeFcf')]//input)[1]")
arrivals = driver.find_element(By.XPATH, "(//div[contains(@class, 'e5F5td vxNK6d')]//input)[1]")

#departures
t.sleep(2)
departures.clear() #limpa o campo de saida
t.sleep(2)
departures.send_keys(f"{input_departures}") #envia os dados do local que quero sair ex: BEL - Belém
t.sleep(2)
driver.find_element(By.XPATH, "//ul[@class='DFGgtd']/li[1]").click()
t.sleep(2)

#arrivals
arrivals.clear() #limpa o campo de saida
t.sleep(2)
arrivals.send_keys(f"{input_arrivals}") #envia os dados do local que quero sair ex: BEL - Belém
t.sleep(2)
driver.find_element(By.XPATH, "//ul[@class='DFGgtd']/li[1]").click()
t.sleep(2)

t.sleep(2)  # Aguarde um pouco para que os resultados sejam exibidos

driver.quit()
