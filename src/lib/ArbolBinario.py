class Nodo:
    def __init__(self, apellido):
        self.apellido = apellido
        self.personas = []  # Lista que guarda las personas con el mismo apellido
        self.izquierda = None
        self.derecha = None

    def __str__(self):
        # Muestra el apellido del nodo y la cantidad de personas asociadas
        print("\n")
        print(f"Apellido: '{self.apellido}' ({len(self.personas)} personas)")
        for persona in self.personas:
            print(f"- {persona}")
        return ""
    
class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def __str__(self):
        # Muestra el arbol completo
        if self.raiz is None:
            return "Arbol vacio"
        else:
            print("Arbol completo:")
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
        #Busca un nodo de forma recusiva en base al apellido, y devuelve una referencia al nodo
        #Si al terminar de recorrer todos los nodos, el nodo que se busca sigue siendo None (indicio de que no se encontro)
        #Se devuelve None
        if nodo == None:
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
        # Se procesa el nodo izquierdo, se muestra el nodo actual (con sus personas) y se procesa el nodo derecho
        # Queda una representación en orden ascendente
        if nodo is not None:
            return self.mostrarInordenRecursivo(nodo.izquierda) + str(nodo) + self.mostrarInordenRecursivo(nodo.derecha)
        else:
            return ""
        

    def borrarPersona(self,nodo):
        #Borrar personas por apellido y nombre
        apellidoABuscar=input("Ingrese el apellido de la persona a eliminar: ")
        posicion=self.buscarNodoRecursivo(nodo,apellidoABuscar)
        if posicion==None:
            print("No se encuentra el apellido")
        else:
            encontrado = None
            nombre=input("Ingrese el nombre a borrar: ")
            for persona in posicion.personas:
                if persona.nombre == nombre:
                    encontrado = persona
                    break

            if encontrado!= None:
                posicion.personas.remove(encontrado)
                print("¡Eliminado!")
            else:
                print("No se encontró el nombre indicado")
    
    def buscarPersona(self,nodo):
        apellido=input("Ingrese el apellido a buscar: ")
        posicion=self.buscarNodoRecursivo(nodo,apellido)
        if posicion!=None:
            nombre=input("Ingrese el nombre: ")
            encontrado=None
            for persona in posicion.personas:
                if persona.nombre==nombre:
                    encontrado=persona 
            if encontrado!=None:
                print(encontrado)
            else:
                print("No se encontro el nombre")
        else:
            print("No se encontro el apellido")