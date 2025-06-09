from lib.ArbolBinario import ArbolBinario
from lib.Persona import Persona

def menu():
    while True:
        print("1- Agregar una persona")
        print("2- Mostrar Arbol de Apellidos y Lista de Personas")
        print("3- Borrar una persona")
        print("4- Salir")
        
        try:
            opcion=int(input("Ingrese un numero: "))
        except ValueError:
            print("Opcion invalida")
            continue
        else:
            break
    return opcion

def main():
    opcion=0

    arbol=ArbolBinario()

    while opcion!=4:
        opcion=menu()
        
        match(opcion):
            case 1:
                apellido=input("Ingrese un apellido: ")
                nombre=input("Ingrese un nombre: ")
                dni=input("Ingrese un DNI: ")

                nuevaPersona=Persona(apellido,nombre,dni)
                arbol.agregarPersona(nuevaPersona)
                
            case 2:
                arbol.mostrar()

            case 3:
                arbol.borrarPersona(arbol.raiz)

            case 4:
                break
            case _:
                print("Opcion invaida")
                pass

main()