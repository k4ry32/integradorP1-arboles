# Modulos
from lib.Persona import Persona
from lib.ArbolBinario import ArbolBinario
from utils.popularArbol import popularArbol

def menu():
    while True:
        print("1- Agregar una persona")
        print("2- Mostrar Arbol de Apellidos y Lista de Personas")
        print("3- Borrar una persona")
        print("4- Buscar una persona")
        print("5- Salir")
        
        try:
            opcion = int(input("\nIngrese una opcion: "))
        except ValueError:
            print("Opcion invalida")
            continue
        else:
            break
    return opcion

def main():
    arbol = ArbolBinario()
    opcion = 0

    print("\n--------------------------------------------------------")
    print("Bienvenido al arbol de apellidos!")
    populate = input("Desea popular el arbol con personas de prueba? (si/no): ")
    if populate.lower() == "si": popularArbol(arbol)

    while opcion != 5:
        print("\n--------------------------------------------------------")
        opcion = menu()
        print("--------------------------------------------------------\n")
        
        match(opcion):
            case 1:
                apellido = input("Ingrese el apellido: ")
                nombre = input("Ingrese el nombre: ")
                dni = input("Ingrese el DNI: ")

                nuevaPersona = Persona(apellido, nombre, dni)
                arbol.agregarPersona(nuevaPersona)
                
            case 2:
                print(arbol)

            case 3:
                apellido = input("Ingrese el apellido de la persona que desea borrar: ")
                # Agregar funcion para borrar persona
                
            case 4:
                apellido = input("Ingrese el apellido de la persona que desea buscar: ")
                #  Agregar funcion para buscar persona

            case 5:
                print("Saliendo del programa...")
                break

            case _:
                print("Opcion invalida")
                pass

main()