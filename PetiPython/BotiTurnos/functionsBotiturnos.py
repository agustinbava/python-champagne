import keyboard
import time
from datetime import datetime
from random import randint
from os import remove
import os
import pyautogui
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

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

def enviarmail(asuntomail,botmail,destinomail,smtpmail,portmail,passmail,mensaje):
    msg = EmailMessage()
    msg.set_content(mensaje)

    msg['Subject'] = asuntomail
    msg['From'] = botmail
    msg['To'] = destinomail

    # Send the message via our own SMTP server.
    server = smtplib.SMTP(smtpmail, portmail)
    server.starttls()
    server.login(botmail, passmail)
    server.send_message(msg)
    server.quit()

def enviarmailadjunto(asuntomail,botmail,destinomail,smtpmail,portmail,passmail,directorio,carpetaimagenes,mensaje):
    msg = MIMEMultipart("plain")
    msg['From'] = botmail
    msg['To'] = destinomail
    msg['Subject'] = asuntomail
    msg.attach(MIMEText(mensaje,"plain"))
    for archivo in os.listdir(directorio):
        adjunto = MIMEBase("application","octect-stream")
        ruta = carpetaimagenes + archivo
        print(ruta)
        adjunto.set_payload(open(ruta,"rb").read())
        encoders.encode_base64(adjunto)
        adjunto.add_header("content-Disposition","attachmet; filename= {0}".format(os.path.basename(archivo)))
        msg.attach(adjunto)    

    # Send the message via our own SMTP server.
    server = smtplib.SMTP(smtpmail, portmail)
    server.starttls()
    server.login(botmail, passmail)
    server.sendmail(botmail,destinomail, msg.as_string())    
    server.quit()
#CREO FUNCIONES - FIN 