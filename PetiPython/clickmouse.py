import mouse 
import time
from datetime import datetime
from datetime import timedelta
import keyboard
import pyautogui
import calendar
import pyperclip as clipboard
import requests
from bs4 import BeautifulSoup
from os import remove
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#RECUPERAR POSICION DEL MOUSE
#pyautogui.displayMousePosition()

#INICIALIZO PARAMETROS - INICIO
link = "https://www.buenosaires.gob.ar/vicejefatura/deportes/actividades/tenis-en-el-polideportivo-colegiales"
link = "https://www.buenosaires.gob.ar/vicejefatura/deportes/actividades/tenis-en-el-polideportivo-costa-rica"
resturnox = 473
resturnoy = 737
diasreserva = 5 #7
selcanchax = 706
selcanchay = 797
selfechax = 927
selfechay = 675
googlex = 949
googley = 472
edgex = 612
edgey = 1058
centrox = 500
centroy = 500
posurlx = 776
posurly = 49
hlimite = "01:56:00" #"00:00:00"
urldir = r"C:\Users\JoacoLacal\Desktop\Python\GitHub\PruebaHTML.html"

#ASIGNO POSICION (X,Y) PARA CADA POSICION DEL CALENDARIO - INICIO
dictcalendar = {}
posinicialx = 892
posinicialy = 612 #SIN TURNOS DISPONIBLES
posinicialy = 542 #CON TURNOS DISPONIBLES
incrementalx = 35
incrementaly = 35
indicecalendar = 0
for j in range(1,7):
   for i in range(1,8):
      indicecalendar += 1
      dictcalendar[indicecalendar] = (posinicialx+(incrementalx*(i-1)),posinicialy+(incrementaly*(j-1)))
#ASIGNO POSICION (X,Y) PARA CADA POSICION DEL CALENDARIO - FIN
#INICIALIZO PARAMETROS - FIN

#PREPARO DATOS - INICIO
#BUSCO FECHA DE RESERVA
fechareserva = datetime.now().date() + timedelta(diasreserva)

#CONFIGURAR HORA LIMITE
horalimite = datetime.strptime(hlimite, "%X").time()

#BUSCO POSICION PRIMER DIA DEL MES
posinicial = calendar.weekday(datetime.now().date().year, datetime.now().date().month, 1) #MARTES=1 
posinicial += 2
if posinicial>7:
   posinicial=posinicial-7
#dateMonthStart="%s-%s-01" % (datetime.now().date().year, datetime.now().date().month)   
#dateMonthEnd="%s-%s-%s" % (today.year, today.month, calendar.monthrange(today.year-1, today.month-1)[1])

#BUSCO POSICION FECHA DE RESERVA
posreserva = posinicial + fechareserva.day - 1
xreserva, yreserva = dictcalendar[posreserva]
#PREPARO DATOS - FIN

#MINIMIZAR VENTANA
#keyboard.press_and_release('windows + d')

#time.sleep(3)
if 1==0:
   #ABRIR EDGE
   pyautogui.moveTo(edgex, edgey, duration=0.5)
   pyautogui.click()
   time.sleep(1.5)

   #ABRIR NUEVA VENTANA DEL EDGE
   pyautogui.moveTo(centrox, centroy, duration=0.5)
   pyautogui.click()
   time.sleep(1.5)
   
   keyboard.press_and_release('ctrl + n')
   time.sleep(1.5)

   #IR A LA PAGINA DE RESERVA
   keyboard.write(link)
   time.sleep(1.5)
   keyboard.send("enter")
   time.sleep(2.5)

   #CLICK EN RESERVAR TURNO
   pyautogui.moveTo(resturnox, resturnoy, duration=0.5)
   pyautogui.click()
   time.sleep(2.5)

   #ESPERO QUE SE HABILITE LA RESERVA **HACER CON FECHAS Y NO SOLO CON TIEMPO
   #while datetime.now().time() < horalimite:
      #pass
   #print(datetime.now().time())   

   #CLICK EN CONTINUAR CON GOOGLE
   pyautogui.moveTo(googlex, googley, duration=0.5)
   pyautogui.click()
   time.sleep(2.5)

   #CLICK EN SELECCIONAR POR FECHA
   pyautogui.moveTo(selfechax, selfechay, duration=0.5)
   pyautogui.click()
   time.sleep(2.5)

   #VOY A POSICION DEL DIA DE RESERVA
   # Do Lu Ma Mi Ju Vi Sa
   pyautogui.moveTo(xreserva, yreserva, duration=0.5)
   pyautogui.click()
   time.sleep(2.5)

   #SELECCIONO LA CANCHA
   pyautogui.moveTo(selcanchax, selcanchay, duration=0.5)
   pyautogui.click()
   time.sleep(2.5)

   #ELIMINAR HTML LOCAL - INICIO
   if os.path.isfile(urldir):
      remove(urldir)
   #ELIMINAR HTML LOCAL - FIN

   #GUARDAR HTML DE MANERA LOCAL - INICIO
   keyboard.press_and_release('ctrl + s')
   time.sleep(1.5)
   keyboard.write(urldir)
   time.sleep(1.5)   
   keyboard.send("enter")
   time.sleep(5)   
   #GUARDAR HTML DE MANERA LOCAL - FIN

if 1==1:
   # Create the webdriver object. Here the 
   # chromedriver is present in the driver 
   # folder of the root directory.
   #driver = webdriver.Edge(EdgeDriverManager().install())
   #driver = webdriver.Chrome(r"C:\Users\JoacoLacal\Desktop\Python\chromedriver.exe")
   driver = webdriver.Chrome(ChromeDriverManager().install())
   #driver = webdriver.Chrome(r"./driver/chromedriver")
   
   driver.maximize_window()

   time.sleep(10)

   # get https://www.geeksforgeeks.org/
   driver.get("https://www.buenosaires.gob.ar/vicejefatura/deportes/actividades/tenis-en-el-polideportivo-colegiales")
   
   # Maximize the window and let code stall 
   # for 10s to properly maximise the window.
   #driver.maximize_window()
   #time.sleep(10)
   
   # Obtain button by link text and click.
   button = driver.find_element_by_link_text("Reservá tu turno")
   button.click()

   time.sleep(5)

   button = driver.find_element_by_link_text("Continuar con Google")
   button.click()

if 1==0:
   #ABRIR HTML - INICIO
   f = open(urldir, encoding="utf8")     
   soup = BeautifulSoup(f, "html.parser")
   f.close()
   #ABRIR HTML - FIN

   #for button in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//button[contains(., 'button_text')]"))):
      #button.click()

   #OBTENGO LA TABLA DE HORARIOS DISPONIBLES
   entradas = soup.find_all('table',{'id': 'tabla-hora'})
   print(entradas)
   
   #RECORRO TABLA DE HORARIOS DISPONIBLES
   for i, entrada in enumerate(entradas):
      horarios = entrada.find_all('div', {'class': 'ng-binding'})
      #RECORRO HORARIOS
      for j, horario in enumerate(horarios):
         print(horario)
      # Con el método "getText()" no nos devuelve el HTML
      #titulo = entrada.find('span', {'class': 'tituloPost'}).getText()
      # Sino llamamos al método "getText()" nos devuelve también el HTML
      #autor = entrada.find('span', {'class': 'autor'})
      #fecha = entrada.find('span', {'class': 'fecha'}).getText()

      # Imprimo el Título, Autor y Fecha de las entradas
      #print("%d - %s  |  %s  |  %s" % (i + 1, titulo, autor, fecha))
   #req = requests.get(page)
   #status_code = req.status_code
   #print(req.url)

   #status_code = 0
   #if status_code == 200 and 1==0:
      # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
      #html = BeautifulSoup(req.text, "html.parser")
      #print(html)  


   if 1==0:
      #ACCEDER A URL EN LA QUE ESTOY PARADO
      pyautogui.moveTo(posurlx, posurly, duration=0.5)
      pyautogui.click()
      time.sleep(2.5)
      keyboard.press_and_release('ctrl + c')
      time.sleep(1.5)
      url = clipboard.paste()
      
      pyautogui.moveTo(centrox, centroy, duration=0.5)
      pyautogui.click()
      time.sleep(1.5)

      req = requests.get(url)
      status_code = req.status_code
      print(url)
      print(req.url)
      if status_code == 200 and 1==0:
         # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
         html = BeautifulSoup(req.text, "html.parser")
         print(html)

         # Obtenemos todos los divs donde están las entradas
         entradas = html.find_all('div', {'class': 'col-md-4 col-xs-12'})
         entradas = html.find_all('table',{'id': 'tabla-hora'})
         print(entradas)

         # Recorremos todas las entradas para extraer el título, autor y fecha
         for i, entrada in enumerate(entradas):
            # Con el método "getText()" no nos devuelve el HTML
            titulo = entrada.find('span', {'class': 'tituloPost'}).getText()
            # Sino llamamos al método "getText()" nos devuelve también el HTML
            autor = entrada.find('span', {'class': 'autor'})
            fecha = entrada.find('span', {'class': 'fecha'}).getText()

            # Imprimo el Título, Autor y Fecha de las entradas
            print("%d - %s  |  %s  |  %s" % (i + 1, titulo, autor, fecha))

      else:
         print("Status Code %d" % status_code)

# (565, 1058) IR AL CHROME
#mouse.move(565, 1058, absolute=True, duration=0.5)
#mouse.click()
#time.sleep(1)
# (1898, 60) ABRIR NUEVA VENTANA
# (1800, 106)https://www.buenosaires.gob.ar/vicejefatura/deportes/actividades/tenis-en-el-polideportivo-colegiales
#mouse.move(1898, 60, absolute=True, duration=0.5)
#mouse.move(1800, 106, absolute=True, duration=0.5)
#mouse.click()

# ABRIR NUEVA VENTANA
#keyboard.press_and_release('ctrl + N')

#import win32api, win32con
#def click(x,y):
 #   win32api.SetCursorPos((x,y))
  #  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
   # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
#click(10,10)
 # import win32api
 # import pyautogui
 # pyautogui.moveTo(100, 150)
 # pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
 # pyautogui.dragTo(100, 150)
 # pyautogui.dragRel(0, 10)  # drag mouse 10 pixels down


# move 100 right and 100 down with a duration of 0.5 seconds

#time.sleep(3)
#keyboard.write("controlo el teclado")
#keyboard.wait('enter')

# left click
#mouse.click('left')
# right click
#mouse.click('right')

## Se simula que se presiona la tecla enter
#keyboard.send("enter")
 
## Se presionan las teclas shift y 7 de manera simultanea
#keyboard.press_and_release('shift + 7')

## Revisar si la tecla space esta presionada
#print(keyboard.is_pressed('space'))
## Detiene el programa hasta que se presione enter
#keyboard.wait('enter')

#while True:
   #time.sleep(3)
   #if mouse.is_pressed():
   #print(mouse.get_position())
   #keyboard.press_and_release('ctrl + N')


