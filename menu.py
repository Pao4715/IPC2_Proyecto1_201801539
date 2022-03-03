from manejoArchivos import extraerDatos, mostrarBuscarPatron, imprimirOrdenar
from listaDoble import ListaDoble

class Menu:

    listaD = ListaDoble()
    
    def menuPrincipal():
        print("=================================")
        print("           MENÚ PRINCIPAL          ")
        print("=================================")
        print("1. Cargar Archivo                  ")
        print("2. Elegir Piso y Patrón Inicial    ")
        print("3. Graficar Patron                 ")
        print("4. Elegir Nuevo Patrón             ")
        print("5. Mostrar todos los Patrones      ")
        print("6. Salir                           ")
        print("=================================")


    while True:
        menuPrincipal()
        opcion = input("Escoja una opción >> ") 

        if opcion == "1":
            extraerDatos()
        elif opcion == "2":
            mostrarBuscarPatron()
        elif opcion == "3":
            print(" ")
        elif opcion == "4":
            print(" ")
        elif opcion == "5":
            imprimirOrdenar()
        elif opcion == "6":
            break
        else: 
            input("Selección no válida")