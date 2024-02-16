import os
import re
import subprocess
from selenium import webdriver
import time as t
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from bs4 import BeautifulSoup

input_departures = "BEL" #str(input('Digite as siglas do aeroporto de partida: '))
date_departure = "16/06/2024" #data de ida
input_arrivals = "GRU" #str(input('Digite as siglas do aeroporto de chegada: '))
date_arrivals = "20/06/2024" #data de volta
value_travels = 500 #digite o valor que podes pagar em uma passagem

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get('https://www.google.com/travel/flights/')

t.sleep(5)

# Usando XPath para encontrar onde vou digitar as siglas dos aeroportos
departures = driver.find_element(By.XPATH, "(//div[contains(@class, 'e5F5td BGeFcf')]//input)[1]")
arrivals = driver.find_element(By.XPATH, "(//div[contains(@class, 'e5F5td vxNK6d')]//input)[1]")

t.sleep(2)

'''
    Inicio onde vai ser inserido a local de saida de voo e chegada
'''

#departures
departures.clear() #limpa o campo de saida
t.sleep(1)
departures.send_keys(f"{input_departures}") #envia os dados do local que quero sair ex: BEL - Belém
t.sleep(1)
driver.find_element(By.XPATH, "//ul[@class='DFGgtd']/li[1]").click()
t.sleep(1)

# #arrivals
arrivals.clear() #limpa o campo de saida
t.sleep(1)
arrivals.send_keys(f"{input_arrivals}") #envia os dados do local que quero sair ex: BEL - Belém
t.sleep(1)
driver.find_element(By.XPATH, "//ul[@class='DFGgtd']/li[1]").click()
t.sleep(1)

'''
    aqui será inserido a data de ida e volta e logo em seguida a pesquisa
'''

#date departures
driver.find_element(By.XPATH, "(//div[contains(@class, 'NA5Egc') and contains(@class, 'ESCxub') and contains(@class, 'fXx9Lc') and contains(@class, 'cd29Sd') and contains(@class, 'wg2eAc')])[1]").click()
t.sleep(1)
driver.find_element(By.XPATH, "(//input[contains(@class, 'TP4Lpb') and contains(@class, 'eoY5cb') and contains(@class, 'j0Ppje')])[3]").send_keys(f"{date_departure}")
t.sleep(1)
driver.find_element(By.XPATH, "(//input[contains(@class, 'TP4Lpb') and contains(@class, 'eoY5cb') and contains(@class, 'j0Ppje')])[3]").send_keys(Keys.ENTER)
t.sleep(1)
driver.find_element(By.XPATH, "(//input[contains(@class, 'TP4Lpb') and contains(@class, 'eoY5cb') and contains(@class, 'j0Ppje')])[4]").send_keys(f"{date_arrivals}")
t.sleep(1)
driver.find_element(By.XPATH, "(//input[contains(@class, 'TP4Lpb') and contains(@class, 'eoY5cb') and contains(@class, 'j0Ppje')])[4]").send_keys(Keys.ENTER)
t.sleep(1)
driver.find_element(By.XPATH, "//div[contains(@class, 'WXaAwc')]//button").send_keys(Keys.ENTER)
t.sleep(1)
driver.find_element(By.XPATH, "//div[contains(@class, 'xFFcie')]//button").send_keys(Keys.ENTER)
t.sleep(1)

'''
    Iremos capturar o primeiro valor da passagem encontrado para fazer o comparativo se está igual ou menor que o valor
    que informei logo no inicio
'''
data = driver.find_element(By.XPATH, "(//ul[contains(@class, 'Rk10dc')])[1]")
html = data.get_attribute("innerHTML")
soup = BeautifulSoup(html, "html.parser")
div = soup.find('div', class_='YMlIz FpEdX jLMuyc')
span = div.find('span')
span_content = span.text

span_no_dol = span_content.replace("R$", "")
value_travels_search = int(span_no_dol.replace(" ", ""))

print("O valor da passagem menor é: ", span_content)
print("-------------------------------------------")

if value_travels >= value_travels_search:
    print("Da de viajar")
else:
    print("Vamo viajar só ano que vem")

t.sleep(2)  # Aguarde um pouco para que os resultados sejam exibidos

driver.quit()
