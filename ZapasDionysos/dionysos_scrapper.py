from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
import time
import pandas as pd
import undetected_chromedriver.v2 as uc
from functions import Scrapper
import csv

browser = Scrapper.openChrome()
reader = csv.DictReader(open("Datos.csv"), delimiter=";")

for row in reader:
    browser.get('https://dionysos.com.ar/')

    time.sleep(1)

    if Scrapper.clickButton(browser,By.ID,"caba",1):
        # browser.get(r'C:/Users/User/Documents/Python/GitHub/python-champagne/ZapasDionysos/ZapasDionysos/DIONYSOS%20-%20AIR%20JORDAN%201%20RETRO%20HIGH%20OG%20_ELECTRO%20ORANGE_%20CABA.html')

        if Scrapper.clickButton(browser,By.ID,"participate",1):
            # browser.get(r'C:/Users/User/Documents/Python/GitHub/python-champagne/ZapasDionysos/ZapasDionysos/DIONYSOS%20-%20AIR%20JORDAN%201%20RETRO%20HIGH%20OG%20_ELECTRO%20ORANGE_%20CABA-2.html')
            
            for key in row:
                Scrapper.fillForm(browser, By.NAME, key, row[key],0)   

            if Scrapper.clickButton(browser,By.NAME, 'terms',1):
                if Scrapper.clickButton(browser,By.ID, 'sendFrm',1):
                    pass


time.sleep(5)
