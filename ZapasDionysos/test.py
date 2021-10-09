from datetime import datetime
from test_class import Persona
import time

inputName = input("enter your name, please")
inputAge = input("enter your age, please")


peti = Persona(inputName, inputAge)

edadPeti = peti.consultarEdad()
nombrePeti = peti.consultarNombre()

print(edadPeti)
print(nombrePeti[0],type(nombrePeti))

while 1:

    time.sleep(3)
    print(datetime.now())