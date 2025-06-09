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

    def insertarNodo(self, apellido):
        # funcion para insertar una persona si el nodo no existe
        if self.raiz is None:
            self.raiz = Nodo(apellido)
        else:
            self.insertarNodoRecursivo(self.raiz, apellido)
        
    def insertarNodoRecursivo(self, nodo, apellido):
        # funcion para insertar una persona cuando existe el nodo
        if nodo.apellido == apellido:
            # si el apellido ya existe no se agrega ningun nodo
            return
        elif apellido < nodo.apellido:
            # si el nodo esta vacío se agrega el apellido
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(apellido)
            else:
                # se avanza hacia la izquierda y se repite el proceso
                self.insertarNodoRecursivo(nodo.izquierda, apellido)
        else:
            # si el nodo esta vacío se agrega el apellido
            if nodo.derecha is None:
                nodo.derecha = Nodo(apellido)
            else:
                # se avanza hacia la derecha y se repite el proceso
                self.insertarNodoRecursivo(nodo.derecha, apellido)

    def buscarNodoRecursivo(self, nodo, apellido):
        if nodo is None:
            return None
        elif nodo.apellido == apellido:
            return nodo
        elif apellido < nodo.apellido:
            return self.buscarNodoRecursivo(nodo.izquierda, apellido)
        else:
            return self.buscarNodoRecursivo(nodo.derecha, apellido)

    def agregarPersona(self, persona):
        nodo = self.buscarNodoRecursivo(self.raiz, persona.apellido)

        if nodo is None:
            self.insertarNodo(persona.apellido)
            nodo = self.buscarNodoRecursivo(self.raiz, persona.apellido)
              
        if nodo is not None: nodo.personas.append(persona)

    def mostrarInordenRecursivo(self, nodo):
        # Se procesa el nodo izquierdo, se muestra el nodo actual y se procesa el nodo derecho
        # Queda una representación en orden asciendente
        if nodo is not None:
            return self.mostrarInordenRecursivo(nodo.izquierda) + "\n" + nodo.__str__() + "\n" + self.mostrarInordenRecursivo(nodo.derecha)
        else:
            return ""