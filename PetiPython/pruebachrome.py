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

#INICIALIZO PARAMETROS - INICIO
parametros = open(r"C:\Users\JoacoLacal\Desktop\Python\GitHub\config.txt")
link = parametros.readline().strip() #"https://www.buenosaires.gob.ar/vicejefatura/deportes/actividades/tenis-en-el-polideportivo-costa-rica"
diasreserva = int(parametros.readline().strip()) #6#7
btnreserva = "Reservá tu turno"
btngoogle = parametros.readline().strip()
btncomenzar = parametros.readline().strip()
btnposfecha = int(parametros.readline().strip())
btnsiguiente = parametros.readline().strip()
classdia = parametros.readline().strip()
classcancha = parametros.readline().strip()
classhora = parametros.readline().strip()
usrmail = parametros.readline().strip()
usrpass = parametros.readline().strip()
horareserva = parametros.readline().strip()#"19:00"#"13:00"
horariosreserva = dict(ast.literal_eval(parametros.readline().strip()))
formcantidad = int(parametros.readline().strip())
texto = ""
urldir = r"C:\Users\JoacoLacal\Desktop\Python\GitHub\PruebaHTML.html"
dialimite = datetime(datetime.now().year,datetime.now().month,datetime.now().day,0,0,0)
dialimite += timedelta(1)
isprueba = True
guardarhtml = False
iterar = False
#INICIALIZO PARAMETROS - FIN

#CREO FUNCIONES - INICIO
def llenarcampoform(idcampo,valorcampo,segundos):
    encontro = False
    campos = browser.find_elements(By.ID,idcampo)
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

def guardararchivohtml(urlarchivo):
    #ELIMINAR HTML LOCAL - INICIO
    if os.path.isfile(urlarchivo):
        remove(urlarchivo)
    #ELIMINAR HTML LOCAL - FIN

    #GUARDAR HTML DE MANERA LOCAL - INICIO
    keyboard.press_and_release('ctrl + s')
    time.sleep(1.5)
    keyboard.write(urlarchivo)
    time.sleep(1.5)   
    keyboard.send("enter")
    time.sleep(5)   
    #GUARDAR HTML DE MANERA LOCAL - FIN    
#CREO FUNCIONES - FIN    

#BUSCO FECHA DE RESERVA - INICIO
fechareserva = datetime.now().date() + timedelta(diasreserva)
diareserva = fechareserva.day
diasemanareserva = fechareserva.isoweekday()
listahorariosstr = horariosreserva.get(diasemanareserva,"")
if listahorariosstr == "":
    listahorariosstr = horareserva
    listahorarios = listahorariosstr.strip().split(",")
elif listahorariosstr.strip() == "NO":
    listahorarios = []    
else:    
    listahorarios = listahorariosstr.strip().split(",")
print(listahorarios)    
#BUSCO FECHA DE RESERVA - FIN 

for reservarhora in listahorarios:
    if isprueba == False:
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

        isok = clickearboton(By.LINK_TEXT,btnreserva,1)
        isok = clickearboton(By.LINK_TEXT,btngoogle,5)

        if iterar:
            iterohasta(dialimite)  

        #LOGUEO EL USUARIO DE GOOGLE - INICIO
        ingresartextoteclado(usrmail)
        ingresartextoteclado(usrpass)
        #LOGUEO EL USUARIO DE GOOGLE - FIN

        #CLICKEO EN EL COMENZAR DE POR FECHA - INICIO
        buttons = browser.find_elements(By.LINK_TEXT,btncomenzar)
        button = buttons[btnposfecha]
        button.click()
        time.sleep(3)
        #CLICKEO EN EL COMENZAR DE POR FECHA - FIN

        #BUSCO Y CLICKEO EL DIA DE LA RESERVA - INICIO
        dias = browser.find_elements(By.CLASS_NAME, classdia)
        for dia in dias:
            nro = dia.get_attribute('innerHTML')
            if  int(nro)==diareserva:
                dia.click()
                time.sleep(3)
                break
        #BUSCO Y CLICKEO EL DIA DE LA RESERVA - FIN

        #BUSCO Y CLICKEO CANCHA DISPONIBLE
        isok = clickearboton(By.CLASS_NAME,classcancha,3)

        #BUSCO Y CLICKEO HORARIO DISPONIBLE - INICIO
        horas = browser.find_elements(By.CLASS_NAME,classhora)
        for hora in horas:
            texto = hora.get_attribute('innerHTML')
            if texto.find(reservarhora)>-1: 
                hora.click()
                time.sleep(3)
                break
        #BUSCO Y CLICKEO HORARIO DISPONIBLE - FIN

        #CLICK EN SIGUIENTE
        isok = clickearboton(By.CLASS_NAME,btnsiguiente,3)

        #PARA PODER REVISAR EL HTML - INICIO
        if guardarhtml==True:
            guardararchivohtml(urldir)
        #PARA PODER REVISAR EL HTML - FIN

    #PRUEBA LOCAL - INICIO
    elif isprueba == True:
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

        browser.get(r"C:/Users/JoacoLacal/Desktop/Python/GitHub/colegiales/PruebaHTML.html")
        time.sleep(5)
        #ABRO CHROME - FIN
    #PRUEBA LOCAL - FIN

    #LLENO FORMULARIO - INICIO
    datosform = open(r"C:\Users\JoacoLacal\Desktop\Python\GitHub\datosformulario.txt")
    for j in range(1,formcantidad+1):
        lst = list(datosform.readline().strip().split(","))
        isok = llenarcampoform(lst[0],lst[1],1.5)
    #LLENO FORMULARIO -FIN

    #CLICK EN SIGUIENTE
    btnsig1 = browser.find_element(By.CLASS_NAME,btnsiguiente)
    btnsig1.click()
    time.sleep(3)
    #CLICK EN SIGUIENTE - FIN

    #CLICK EN SIGUIENTE - INICIO
    buttons = browser.find_elements(By.CLASS_NAME,btnsiguiente)
    for button in buttons:
        if btnsig1 != button:
            button.click()
            time.sleep(3)
            break
    #CLICK EN SIGUIENTE - FIN

    #PARA PODER REVISAR EL HTML - INICIO
    if guardarhtml==True:
        guardararchivohtml(urldir)
    #PARA PODER REVISAR EL HTML - FIN

    time.sleep(10)


#CODIGO BASURA - INICIO
    #wait = WebDriverWait(browser, 10)
    #campo = wait.until(EC.element_to_be_clickable((By.ID, 'input_0')))
    #campo.send_keys("XXX")

    #button = browser.find_elements_by_link_text(fechareserva.day.__str__())
    #button.click()
    #login_button_init = self.browser.find_element_by_xpath("//a[@aria-label='Sign in']") 
    #login_button_init.click()

    # locate the login button
    #login_button = self.browser.find_element_by_xpath("//paper-button[@aria-label='Sign in']")
    #login_button.click()

    # get email and set to email input box
    #email = self.browser.find_element_by_id("identifierId")
    #myemail = os.environ.get('YOUTUBE_EMAIL')
    #email.send_keys(myemail)

    # click next button
    #email_next_button = self.browser.find_element_by_id("identifierNext")
    #email_next_button.click()

    # get password and set to password input box
    #password = self.browser.find_element_by_name("password")
    #mypassword = os.environ.get('YOUTUBE_PASSWORD')
    #password.send_keys(mypassword)
    #sleep(2)

    # click next button to log in
    #pass_next_button = self.browser.find_element_by_id("passwordNext")
    #pass_next_button.click()
#CODIGO BASURA - FIN    