import requests
from datetime import datetime

class Persona():
    def __init__(self, nombre, edad):
        self.horario = 0
        self.nombre = nombre
        self.edad = edad
        
        print("Inicia el llamador")

    def consultarHora(self):
        return datetime.now()

    def consultarEdad(self):
        return self.edad
    
    def consultarNombre(self):
        return self.nombre, self.edad