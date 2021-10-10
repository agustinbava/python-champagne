import time
from datetime import datetime
from datetime import timedelta
import os
import ast
import wget
from random import randint
from selenium.webdriver.common.by import By 
import functionsBotiturnos as fBotiturnos
import sys
sys.path.insert(1, r'C:\Users\JoacoLacal\Desktop\Python\MiCodigo')
from functions import Scrapper
from functions import General

#RECUPERO ARCHIVO CONFIGURACION - INICIO
if True:
    rutasbotiturnos = r"C:\Users\JoacoLacal\Desktop\Python\MiCodigo\BotiTurnos\rutasbotiturnos.txt"
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

#INICIALIZO PARAMETROS - INICIO
if True:
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
    texto = ""
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

#BUSCO FECHA DE RESERVA - INICIO
if True:
    fechareserva = datetime.now().date() + timedelta(diasreserva)
    diareserva = fechareserva.day
    print(fechareserva)
    mensajemail = "Fecha de Reserva: " + str(fechareserva)
#BUSCO FECHA DE RESERVA - FIN

#BUSCO HORARIOS A RESERVAR - INICIO
if True:
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
browser = Scrapper.openChrome()
browser.get(link)
#ABRO CHROME - FIN

#LOGUEO EL USUARIO DE GOOGLE O FACEBOOK - INICIO
if True:
    contcapturas = fBotiturnos.capturarpantalla(contcapturas,directorio)
    if Scrapper.clickButton(browser,By.LINK_TEXT,btnreserva,1):
        contcapturas = fBotiturnos.capturarpantalla(contcapturas,directorio)
        if Scrapper.clickButton(browser,By.LINK_TEXT,btngoogle,1):
            contcapturas = fBotiturnos.capturarpantalla(contcapturas,directorio)
            if loggoogle == True:        
                isok = Scrapper.fillForm(browser,By.ID,formidusr,usrmail,1)
                isok = Scrapper.clickButton(browser,By.ID,btnsiggoogleusr,3)
            else:
                isok = Scrapper.fillForm(browser,By.ID,formidusrfb,usrmail,1)
                isok = Scrapper.fillForm(browser,By.ID,formidpassfb,usrpass,1)
                isok = Scrapper.clickButton(browser,By.ID,btnloginfb,3)

            if isok == True:
                if loggoogle == True:    
                    contcapturas = fBotiturnos.capturarpantalla(contcapturas,directorio)
                    isok = Scrapper.fillForm(browser,By.NAME,formnamepass,usrpass,1)
                    if Scrapper.clickButton(browser,By.ID,btnsiggooglepass,3):
                        pass
                    else:
                        continuar = False
                        print("NO ENCONTRO EL BOTON DE SIGUIENTE - GOOGLE PASS")    
                        mensajemail +=  f"\r\r\n NO ENCONTRO EL BOTON DE SIGUIENTE - GOOGLE PASS"    
            else:
                continuar = False
                print("NO ENCONTRO EL BOTON DE SIGUIENTE - GOOGLE USUARIO O FACEBOOK")       
                mensajemail +=  f"\r\r\n NO ENCONTRO EL BOTON DE SIGUIENTE - GOOGLE USUARIO O FACEBOOK" 
        else:
            continuar = False
            print("NO ENCONTRO EL BOTON DE GOOGLE O FACEBOOK")    
            mensajemail +=  f"\r\r\n NO ENCONTRO EL BOTON DE GOOGLE O FACEBOOK"
    else:
        continuar = False
        print("NO ENCONTRO BOTON DE RESERVAR TURNO") 
        mensajemail +=  f"\r\r\n NO ENCONTRO BOTON DE RESERVAR TURNO"        
#LOGUEO EL USUARIO DE GOOGLE O FACEBOOK - FIN   

if continuar == True:
#RESERVO - ELIJO DIA, HORA Y CANCHA - INICIO
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
                fBotiturnos.iterohasta(dialimite)
                actualizopest = True
            canchasclickeadas = []    
            while salir == False:
                continuar = True    
                if actualizopest == True:    
                    browser.get(linkreserva)
                actualizopest = True    
                #CLICKEO EN EL COMENZAR DE POR FECHA - INICIO
                contcapturas = fBotiturnos.capturarpantalla(contcapturas,directorio)
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
                    contcapturas = fBotiturnos.capturarpantalla(contcapturas,directorio)
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
                        contcapturas = fBotiturnos.capturarpantalla(contcapturas,directorio)
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
                            contcapturas = fBotiturnos.capturarpantalla(contcapturas,directorio)
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
                                contcapturas = fBotiturnos.capturarpantalla(contcapturas,directorio)
                                isok = Scrapper.clickButton(browser,By.CLASS_NAME,btnsiguiente,3)
                                if isok == False:
                                    continuar = False
                                    print("NO ENCONTRO EL BOTON SIGUIENTE - ANTERIOR A LLENAR FORMULARIO")   
                                    mensajemail +=  f"\r\r\n NO ENCONTRO EL BOTON SIGUIENTE - ANTERIOR A LLENAR FORMULARIO"
                                #PARA PODER REVISAR EL HTML - INICIO
                                if guardarhtml==True:
                                    fBotiturnos.guardararchivohtml(urldir)
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
            #PASO FINAL - LLENO FORMULARIO Y FINALIZO - INICIO
            if continuar == True:
                #LLENO FORMULARIO - INICIO
                contcapturas = fBotiturnos.capturarpantalla(contcapturas,directorio)
                datosform = open(urlguardardatosform)
                for j in range(1,formcantidad+1):
                    lst = list(datosform.readline().strip().split(","))
                    isok = Scrapper.fillForm(browser,By.ID,lst[0],lst[1],1.5)
                #LLENO FORMULARIO -FIN

                #CLICK EN SIGUIENTE
                contcapturas = fBotiturnos.capturarpantalla(contcapturas,directorio)
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
                    contcapturas = fBotiturnos.capturarpantalla(contcapturas,directorio)
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
                            fBotiturnos.guardararchivohtml(urldir)
                        #PARA PODER REVISAR EL HTML - FIN

                        contcapturas = fBotiturnos.capturarpantalla(contcapturas,directorio)
                        if Scrapper.clickButton(browser,By.CLASS_NAME,btnfinalizar,3):
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
            #PASO FINAL - LLENO FORMULARIO Y FINALIZO - FIN        
        #FOR HORARIOS - SUBLISTA - FIN
    #FOR HORARIOS - FIN    
#RESERVO - ELIJO DIA, HORA Y CANCHA - INICIO

General.sendmail(asuntomail,botmail,passmail,destinomail,smtpmail,portmail,mensajemail,directorio) 
