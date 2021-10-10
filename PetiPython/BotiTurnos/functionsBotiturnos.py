import keyboard
import time
from datetime import datetime
from random import randint
from os import remove
import os
import pyautogui

#CREO FUNCIONES - INICIO
def ingresartextoteclado(texto):
    keyboard.write(texto)
    keyboard.send("enter")
    time.sleep(3)

def iterohasta(hasta):
    #ITERO HASTA QUE SEAN LAS 00 - INICIO
    print(hasta)
    while datetime.now() < hasta:
        print(datetime.now())
        time.sleep(0.2)
        pass
    #ITERO HASTA QUE SEAN LAS 00 - FIN      

def guardararchivohtml(urldir):
    number = randint(0,9999)
    urlarchivo = urldir + str(datetime.now().year).strip() + str(datetime.now().month).strip() + str(datetime.now().day).strip()  + "-" + str(number).strip() + ".html"
    #ELIMINAR HTML LOCAL - INICIO
    if os.path.isfile(urlarchivo):
        remove(urlarchivo)
    #ELIMINAR HTML LOCAL - FIN

    #GUARDAR HTML DE MANERA LOCAL - INICIO
    time.sleep(1.5)
    keyboard.press_and_release('ctrl + s')
    time.sleep(1.5)
    keyboard.write(urlarchivo)
    time.sleep(1.5)   
    keyboard.send("enter")
    time.sleep(8)   
    #GUARDAR HTML DE MANERA LOCAL - FIN 

def capturarpantalla(capturas,directorio):  
    time.sleep(2)
    cantcapturas = capturas + 1
    urlimagen = directorio + r"\imagen" + str(cantcapturas).strip() + ".png"
    screenshot = pyautogui.screenshot()
    screenshot.save(urlimagen)
    return cantcapturas
#CREO FUNCIONES - FIN 