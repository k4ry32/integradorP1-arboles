
import lib.Persona

class Nodo:
    def __init__(self, apellido):
        self.apellido = apellido
        self.personas = []  # Lista que guarda las personas con el mismo apellido
        self.izquierda = None
        self.derecha = None

    def __str__(self):
        # Muestra el apellido del nodo y la cantidad de personas asociadas
        return f"Nodo Apellido: '{self.apellido}' ({len(self.personas)} personas)"
    
class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def __str__(self):
        # Muestra el arbol completo
        if self.raiz is None:
            return "Arbol vacio"
        else:
            return self.mostrarInordenRecursivo(self.raiz)

    def insertar(self, apellido):
        # funcion para insertar una persona si el nodo no existe
        if self.raiz is None:
            self.raiz = Nodo(apellido)
        else:
            self.insertarRecursivo(apellido)

    def insertarRecursivo(self, apellido):
        # funcion para insertar una persona cuando existe el nodo
        print("Funcion insertarRecursivo")

    def mostrarInordenRecursivo(self, nodo):
        print("Funcion mostrarEnOrdenRecursivo")