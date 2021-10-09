import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By 
import time

class Scrapper():
    def openChrome():
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--profile-directory=Default")
        chrome_options.add_argument("--disable-plugins-discovery")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("user_agent=DN")

        browser = uc.Chrome(options=chrome_options)
        browser.delete_all_cookies()

        browser.maximize_window()
        return browser

    def fillForm(browser,inby,idcampo,valorcampo,segundos):
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

        