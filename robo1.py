from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd

print("Iiniciando nosso Robo...\n")

arq = open("resultado.txt", "w")

dominios = []
workbook = xlrd.open_workbook('dominios.xlsx')

sheet = workbook.sheet_by_index(0) 

for linha in range(0, 11):
    for coluna in range (0,2):
        dominios.append(sheet.cell_value(linha,coluna))    



driver = webdriver.Chrome('/home/erik/Robos/chromedriver')
driver.get('https://registro.br/')

pesquisa = driver.find_element_by_id('is-avail-field')
pesquisa.clear()


for dominio in dominios:
    pesquisa = driver.find_element_by_id('is-avail-field')
    pesquisa.clear()
    pesquisa.send_keys(dominio)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(2)
    resultados = driver.find_elements_by_tag_name("strong")
    print("Dominio %s %s"  % (dominio, resultados[4].text))
    texto = "Dominio %s %s\n"  % (dominio, resultados[4].text)
    arq.write(texto)



time.sleep(3)
arq.close()
driver.close()