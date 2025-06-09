# Modulos
from lib.Persona import Persona

# Paquetes
import random

def dniAleatorio():
        return str(random.randint(20000000, 48000000))

def popularArbol(arbol):        
    arbol.agregarPersona(Persona("Ovelar", "Javier", dniAleatorio()))
    arbol.agregarPersona(Persona("Rodriguez", "Karina", dniAleatorio()))
    arbol.agregarPersona(Persona("Martinez", "Sandra", dniAleatorio()))
    arbol.agregarPersona(Persona("Gimenez", "Camilo", dniAleatorio()))
    arbol.agregarPersona(Persona("Perez", "Eduardo", dniAleatorio()))
    arbol.agregarPersona(Persona("Rodriguez", "Sebastian", dniAleatorio()))