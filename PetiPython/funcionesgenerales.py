import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
import time

class WebScrapping():
    def fillform(browser,inby,idcampo,valorcampo,segundos):
        encontro = False
        campos = browser.find_elements(inby,idcampo)
        for campo in campos:
            campo.send_keys(valorcampo)
            time.sleep(segundos)
            encontro = True
            break
        return encontro

    def clickButton(browser,inby,buscar,segundos):
        encontro = False
        botones = browser.find_elements(inby,buscar)
        for boton in botones:
            boton.click()
            time.sleep(segundos)
            encontro = True
            break 
        return encontro    