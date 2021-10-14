import keyboard
import time
from datetime import datetime
from random import randint
from os import remove
import os
import pyautogui
import pymysql
import base64

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

def insertarReservaDB(polideportivo,fecha,hora,cancha,usuario,logueo,estado,nroturno):
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="Carp2204",
        db="botiturnos"
    )

    cursor = connection.cursor()

    fechastr = str(fecha.year) + "-" + str(fecha.month) + "-" + str(fecha.day)
    sql = "INSERT INTO Reserva(ReservaPolideportivo, ReservaFecha, ReservaHora, ReservaCancha, ReservaUsuario, ReservaLogueo, ReservaEstado, ReservaTurno)"
    sql += "VALUES ('" + polideportivo + "', '" + fechastr
    sql += "', '" + hora + "', '" + cancha + "', '" + usuario + "', '" + logueo + "', '" + estado + "', '" + nroturno + "')"

    cursor.execute(sql)

    connection.commit()    

def generarURLTurno(nroturno):
    encriptado = base64.b64encode(bytes(nroturno, 'utf-8'))
    url = r"https://formulario-sigeci.buenosaires.gob.ar/cancelar/"
    url += encriptado.decode("utf-8") 
    url += r"/NjMxYzZhZTE0YmFlNGE0NjoyMDIxLTEwLTExVDAwOjQ1OjE5LjY5Nw=="
    return url
#CREO FUNCIONES - FIN 