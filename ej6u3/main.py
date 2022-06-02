from menu import menuu
from objectencoder import ObjectEncoder
if __name__=='__main__':
    bandera = False
    m=menuu()

    while not bandera:
        print("")
        print("a insertar aparato en una posicion especifica de la coleccion")
        print("b cargar aparato")
        print("c mostrar aparato segun posicion")
        print('d mostrar cantidad de aparatos phillips')
        print('e Mostrar la marca de todos los lavarropas que tienen carga superior .')
        print('f Mostrar para todos los aparatos que la empresa tiene a la venta, marca, país de fabricación e importe de venta.')
        print('g salir')
        opcion= input("Ingrese una opción: ")
        m.opcion(opcion)
        bandera =(opcion)=='g'