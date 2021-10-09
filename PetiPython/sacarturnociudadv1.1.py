import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import keyboard
from datetime import datetime
from datetime import timedelta
from os import remove
import os
import ast
import wget
from random import randint
import pyautogui
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from funcionesgenerales import WebScrapping

#INICIALIZO PARAMETROS - INICIO
texto = ""
#RECUPERO ARCHIVO CONFIGURACION - INICIO
rutasbotiturnos = r"C:\Users\JoacoLacal\Desktop\Python\MiCodigo\rutasbotiturnos.txt"
rutas = open(rutasbotiturnos)
urlconfig = rutas.readline().strip()
urldatosformulario = rutas.readline().strip()
dirruta = rutas.readline().strip()
number = randint(0,9999)
directorio = dirruta + str(datetime.now().year).strip() + str(datetime.now().month).strip() + str(datetime.now().day).strip()  + "-" + str(number).strip()
os.mkdir(directorio) 
carpetaimagenes = directorio +  r"\a"
carpetaimagenes = carpetaimagenes[:len(carpetaimagenes)-1]
urlguardarconfig = directorio + r"\config.txt"
urlguardardatosform = directorio + r"\datosformulario.txt"
wget.download(urlconfig,urlguardarconfig)
wget.download(urldatosformulario,urlguardardatosform)
#RECUPERO ARCHIVO CONFIGURACION - FIN
parametros = open(urlguardarconfig)
colegialeslink = parametros.readline().strip()
colegialeslinkreserva = parametros.readline().strip()
costaricalink = parametros.readline().strip()
costaricalinkreserva = parametros.readline().strip()
onegalink = parametros.readline().strip()
onegalinkreserva = parametros.readline().strip()
polideportivo = parametros.readline().strip()
if polideportivo.upper().strip() == "COSTA RICA":
    link = costaricalink
    linkreserva = costaricalinkreserva
elif polideportivo.upper().strip() == "ONEGA":
    link = onegalink
    linkreserva = onegalinkreserva
else:
    link = colegialeslink
    linkreserva = colegialeslinkreserva
urldir = parametros.readline().strip()
diasreserva = int(parametros.readline().strip())
btnreserva = "Reservá tu turno"
btngoogle = parametros.readline().strip()
btncomenzar = parametros.readline().strip()
btnposfecha = int(parametros.readline().strip())
btnsiguiente = parametros.readline().strip()
btnfinalizar = parametros.readline().strip()
formidusr = parametros.readline().strip()
btnsiggoogleusr = parametros.readline().strip()
formnamepass = parametros.readline().strip()
btnsiggooglepass = parametros.readline().strip()
formidusrfb = parametros.readline().strip()
formidpassfb = parametros.readline().strip()
btnloginfb = parametros.readline().strip()
classdia = parametros.readline().strip()
classcancha = parametros.readline().strip()
classhora = parametros.readline().strip()
buscarcancha = parametros.readline().strip()
usrmail = parametros.readline().strip()
usrpass = parametros.readline().strip()
horareserva = parametros.readline().strip()
horariosreserva = dict(ast.literal_eval(parametros.readline().strip()))
formcantidad = int(parametros.readline().strip())
asuntomail = parametros.readline().strip()
botmail = parametros.readline().strip()
destinomail = parametros.readline().strip()
passmail = parametros.readline().strip()
smtpmail = parametros.readline().strip()
portmail = int(parametros.readline().strip())
dialimite = datetime(datetime.now().year,datetime.now().month,datetime.now().day,0,0,0)
dialimite += timedelta(1)
isprueba = False
guardarhtml = False
continuar = True
contcapturas = 0
mensajemail = ""
actualizopest = False
reservado = False
listaadjuntos = []
if datetime.now().hour == 23:
    iterar = True
else:
    iterar = False    
    diasreserva -= 1
if btngoogle.upper().find("GOOGLE") > -1:
    loggoogle = True
else:
    loggoogle = False
#INICIALIZO PARAMETROS - FIN

#CREO FUNCIONES - INICIO
def llenarcampoform(idcampo,valorcampo,segundos,inby):
    encontro = False
    campos = browser.find_elements(inby,idcampo)
    for campo in campos:
        campo.send_keys(valorcampo)
        time.sleep(segundos)
        encontro = True
        break
    return encontro

def clickearboton(inby,buscar,segundos):
    encontro = False
    botones = browser.find_elements(inby,buscar)
    for boton in botones:
        boton.click()
        time.sleep(segundos)
        encontro = True
        break 
    return encontro

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

def guardararchivohtml():
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

def capturarpantalla(capturas):  
    time.sleep(2)
    cantcapturas = capturas + 1
    urlimagen = directorio + r"\imagen" + str(cantcapturas).strip() + ".png"
    screenshot = pyautogui.screenshot()
    screenshot.save(urlimagen)
    return cantcapturas

def enviarmail(mensaje):
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

def enviarmailadjunto(mensaje):
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

#BUSCO FECHA DE RESERVA - INICIO
fechareserva = datetime.now().date() + timedelta(diasreserva)
diareserva = fechareserva.day
print(fechareserva)
mensajemail = "Fecha de Reserva: " + str(fechareserva)
#BUSCO FECHA DE RESERVA - FIN

#BUSCO HORARIOS A RESERVAR - INICIO
diasemanareserva = fechareserva.isoweekday()
listahorariosstr = horariosreserva.get(diasemanareserva,"")
if listahorariosstr == "":
    listahorariosstr = horareserva
    listahorarios = listahorariosstr.strip().split(";")
elif listahorariosstr.strip() == "NO":
    listahorarios = []    
else:    
    listahorarios = listahorariosstr.strip().split(";")
print(listahorarios)
mensajemail +=  f"\r\r\n HORARIOS DE RESERVA: " + str(listahorarios)    
#BUSCO HORARIOS A RESERVAR - FIN 

#ABRO CHROME - INICIO
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

browser.get(link)
#ABRO CHROME - FIN

contcapturas = capturarpantalla(contcapturas)
isok = WebScrapping.clickearboton(browser,By.LINK_TEXT,btnreserva,1)
#isok = clickearboton(By.LINK_TEXT,btnreserva,1)
if isok == True:
    contcapturas = capturarpantalla(contcapturas)
    isok = clickearboton(By.LINK_TEXT,btngoogle,1)
    if isok == True:
        #LOGUEO EL USUARIO DE GOOGLE O FACEBOOK - INICIO
        contcapturas = capturarpantalla(contcapturas)
        if loggoogle == True:        
            isok = llenarcampoform(formidusr,usrmail,1,By.ID)
            isok = clickearboton(By.ID,btnsiggoogleusr,3)
        else:
            isok = WebScrapping.llenarcampoform(browser,formidusrfb,usrmail,1,By.ID)
            isok = WebScrapping.llenarcampoform(browser,formidpassfb,usrmail,1,By.ID)
            #isok = llenarcampoform(formidusrfb,usrmail,1,By.ID)
            #isok = llenarcampoform(formidpassfb,usrpass,1,By.ID)
            isok = clickearboton(By.ID,btnloginfb,3)

        if isok == True:
            if loggoogle == True:    
                contcapturas = capturarpantalla(contcapturas)
                isok = llenarcampoform(formnamepass,usrpass,1,By.NAME)
                isok = clickearboton(By.ID,btnsiggooglepass,3)
                #ingresartextoteclado(usrmail)
                #ingresartextoteclado(usrpass)

            if isok == True:
        #LOGUEO EL USUARIO DE GOOGLE O FACEBOOK - FIN
                #FOR HORARIOS - INICIO
                for sublistahorariosstr in listahorarios:
                    if reservado == True:
                        break
                    sublistahorarios = sublistahorariosstr.strip().split(",")
                    #FOR HORARIOS - SUBLISTA - INICIO
                    for reservarhora in sublistahorarios:
                        continuar = True
                        salir = False
                        if iterar:
                            iterohasta(dialimite)
                            actualizopest = True
                        canchasclickeadas = []    
                        while salir == False:
                            continuar = True    
                            if actualizopest == True:    
                                browser.get(linkreserva)
                            actualizopest = True    
                            #CLICKEO EN EL COMENZAR DE POR FECHA - INICIO
                            contcapturas = capturarpantalla(contcapturas)
                            encontrofecha = False
                            buttons = browser.find_elements(By.LINK_TEXT,btncomenzar)
                            contador = 0
                            for button in buttons:
                                if contador==btnposfecha:
                                    encontrofecha = True
                                    button.click()
                                    time.sleep(3)
                                    break
                                contador += 1    
                            #CLICKEO EN EL COMENZAR DE POR FECHA - FIN

                            if encontrofecha == True:
                                #BUSCO Y CLICKEO EL DIA DE LA RESERVA - INICIO
                                contcapturas = capturarpantalla(contcapturas)
                                encontrodia = False
                                dias = browser.find_elements(By.CLASS_NAME, classdia)
                                for dia in dias:
                                    nro = dia.get_attribute('innerHTML')
                                    if  int(nro)==diareserva:
                                        encontrodia = True
                                        dia.click()
                                        time.sleep(3)
                                        break
                                #BUSCO Y CLICKEO EL DIA DE LA RESERVA - FIN

                                if encontrodia == True:
                                    #BUSCO Y CLICKEO CANCHA DISPONIBLE
                                    contcapturas = capturarpantalla(contcapturas)
                                    encontrocancha = False
                                    canchas = browser.find_elements(By.CLASS_NAME, classcancha)
                                    canchasdisponibles = len(canchas)
                                    if len(canchasclickeadas) == 0:
                                        for cancha in canchas:
                                            texto = cancha.get_attribute('innerHTML')
                                            if texto.find(buscarcancha)>-1: 
                                                encontrocancha = True
                                                canchasclickeadas.append(cancha)
                                                cancha.click()
                                                time.sleep(3)
                                                break
                                    if encontrocancha == False:   
                                        for cancha in canchas:
                                            if not cancha in canchasclickeadas:
                                                encontrocancha = True
                                                canchasclickeadas.append(cancha)
                                                cancha.click()
                                                time.sleep(3)
                                                break
                                    
                                    if len(canchasclickeadas) == canchasdisponibles:
                                        salir = True 

                                    if encontrocancha == True:
                                        #BUSCO Y CLICKEO HORARIO DISPONIBLE - INICIO
                                        contcapturas = capturarpantalla(contcapturas)
                                        encontrohora = False
                                        horas = browser.find_elements(By.CLASS_NAME,classhora)
                                        for hora in horas:
                                            texto = hora.get_attribute('innerHTML')
                                            if texto.find(reservarhora)>-1: 
                                                encontrohora = True
                                                hora.click()
                                                time.sleep(3)
                                                break
                                        #BUSCO Y CLICKEO HORARIO DISPONIBLE - FIN

                                        if encontrohora == True:
                                            salir = True
                                            #CLICK EN SIGUIENTE
                                            contcapturas = capturarpantalla(contcapturas)
                                            isok = clickearboton(By.CLASS_NAME,btnsiguiente,3)
                                            if isok == False:
                                                continuar = False
                                                print("NO ENCONTRO EL BOTON SIGUIENTE - ANTERIOR A LLENAR FORMULARIO")   
                                                mensajemail +=  f"\r\r\n NO ENCONTRO EL BOTON SIGUIENTE - ANTERIOR A LLENAR FORMULARIO"
                                            #PARA PODER REVISAR EL HTML - INICIO
                                            if guardarhtml==True:
                                                guardararchivohtml()
                                            #PARA PODER REVISAR EL HTML - FIN
                                        else:
                                            continuar = False
                                            print("NO ENCONTRO EL HORARIO DE RESERVA " + reservarhora)
                                            mensajemail +=  f"\r\r\n NO ENCONTRO EL HORARIO DE RESERVA " + reservarhora
                                    else:
                                        salir = True
                                        continuar = False
                                        print("NO ENCONTRO CANCHA")  
                                        mensajemail +=  f"\r\r\n NO ENCONTRO CANCHA"
                                else:
                                    salir = True
                                    continuar = False
                                    print("NO ENCONTRO EL DÍA DE RESERVA")
                                    mensajemail +=  f"\r\r\n NO ENCONTRO EL DIA DE RESERVA"
                            else:
                                salir = True
                                continuar = False
                                print("NO ENCONTRO EL COMENZAR - FECHA")  
                                mensajemail +=  f"\r\r\n NO ENCONTRO EL COMENZAR - FECHA"   
                        if continuar == True:
                            #LLENO FORMULARIO - INICIO
                            contcapturas = capturarpantalla(contcapturas)
                            datosform = open(urlguardardatosform)
                            for j in range(1,formcantidad+1):
                                lst = list(datosform.readline().strip().split(","))
                                isok = llenarcampoform(lst[0],lst[1],1.5,By.ID)
                            #LLENO FORMULARIO -FIN

                            #CLICK EN SIGUIENTE
                            contcapturas = capturarpantalla(contcapturas)
                            encontro = False
                            buttons = browser.find_elements(By.CLASS_NAME,btnsiguiente)
                            for button in buttons:
                                btnsig1 = button
                                btnsig1.click()
                                time.sleep(3)
                                encontro = True
                                break 
                            #CLICK EN SIGUIENTE - FIN

                            if encontro == True:
                                #CLICK EN SIGUIENTE - INICIO
                                contcapturas = capturarpantalla(contcapturas)
                                encontro = False
                                buttons = browser.find_elements(By.CLASS_NAME,btnsiguiente)
                                for button in buttons:
                                    if btnsig1 != button:
                                        encontro = True
                                        button.click()
                                        time.sleep(3)
                                        break  
                                #CLICK EN SIGUIENTE - FIN

                                if encontro == True:
                                    #PARA PODER REVISAR EL HTML - INICIO
                                    if guardarhtml==True:
                                        guardararchivohtml()
                                    #PARA PODER REVISAR EL HTML - FIN

                                    contcapturas = capturarpantalla(contcapturas)
                                    isok = clickearboton(By.CLASS_NAME,btnfinalizar,3)
                                    if isok == True:
                                        #pw.sendwhatmsg("+5491136004283", "FINALIZO LA RESERVA CORRECTAMENTE", 15,00)
                                        print("FINALIZO LA RESERVA CORRECTAMENTE")
                                        mensajemail +=  f"\r\r\n FINALIZO LA RESERVA CORRECTAMENTE"
                                        reservado = True
                                    else:
                                        mensajemail +=  f"\r\r\n FALLO LA RESERVA"    

                                    time.sleep(10)
                                else:
                                    print("NO ENCONTRO EL BOTON DE SIGUIENTE - FORMULARIO CONFIRMACION")    
                                    mensajemail +=  f"\r\r\n NO ENCONTRO EL BOTON DE SIGUIENTE - FORMULARIO CONFIRMACION"
                            else:
                                print("NO ENCONTRO EL BOTON DE SIGUIENTE - FORMULARIO")    
                                mensajemail +=  f"\r\r\n NO ENCONTRO EL BOTON DE SIGUIENTE - FORMULARIO"
                    #FOR HORARIOS - SUBLISTA - FIN
                #FOR HORARIOS - FIN    
            else:
                continuar = False
                print("NO ENCONTRO EL BOTON DE SIGUIENTE - GOOGLE PASS")    
                mensajemail +=  f"\r\r\n NO ENCONTRO EL BOTON DE SIGUIENTE - GOOGLE PASS"    
        else:
            continuar = False
            print("NO ENCONTRO EL BOTON DE SIGUIENTE - GOOGLE USUARIO")       
            mensajemail +=  f"\r\r\n NO ENCONTRO EL BOTON DE SIGUIENTE - GOOGLE USUARIO" 
    else:
        continuar = False
        print("NO ENCONTRO EL BOTON DE GOOGLE")    
        mensajemail +=  f"\r\r\n NO ENCONTRO EL BOTON DE GOOGLE"
else:
    continuar = False
    print("NO ENCONTRO BOTON DE RESERVAR TURNO") 
    mensajemail +=  f"\r\r\n NO ENCONTRO BOTON DE RESERVAR TURNO"

enviarmailadjunto(mensajemail) 