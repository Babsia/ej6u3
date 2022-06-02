from menu import menuu
from objectencoder import ObjectEncoder
if __name__=='__main__':
    bandera = False
    m=menuu()

    while not bandera:
        print("")
        print("a insertar aparato en una posicion especifica de la coleccion")
        print("b cargar aparato")
        print("c para salir")
        opcion= input("Ingrese una opción: ")
        m.opcion(opcion)
        bandera =(opcion)=='c'