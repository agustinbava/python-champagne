import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By 
import time
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
import pathlib

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

    def findText(browser,inby,buscar):
        campos = browser.find_elements(inby,buscar)
        for campo in campos:
            texto = campo.get_attribute('innerHTML')
            break
        return texto

class General():
    def sendmail(asunto,botmail,passmail,destino,smtp,port,mensaje,directorio):
        msg = MIMEMultipart("plain")
        msg['From'] = botmail
        msg['To'] = destino
        msg['Subject'] = asunto
        msg.attach(MIMEText(mensaje,"plain"))
        if directorio != "":
            for archivo in os.listdir(directorio):
                adjunto = MIMEBase("application","octect-stream")
                ruta = directorio + "\\" + archivo
                adjunto.set_payload(open(ruta,"rb").read())
                encoders.encode_base64(adjunto)
                adjunto.add_header("content-Disposition","attachmet; filename= {0}".format(os.path.basename(archivo)))
                msg.attach(adjunto)

        # Send the message via our own SMTP server.
        server = smtplib.SMTP(smtp, port)
        server.starttls()
        server.login(botmail, passmail)
        server.sendmail(botmail,destino, msg.as_string())    
        server.quit()