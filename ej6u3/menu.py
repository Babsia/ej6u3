
from objectencoder import ObjectEncoder
from aparatos import aparatos
from heladera import Heladeras
from televisor import televisor
from lavarropas import lavarropa
from typing import List
class menuu:
    __switcher=None
    __M=None

    def __init__(self):
        self.__switcher = { 
            'a':self.opcion1,
            'b':self.opcion2,
            'c':self.opcion3,
            'd':self.opcion4,
            'e':self.opcion5,
            'f':self.opcion6,
            'g':self.salir
            }
        unencoder=ObjectEncoder()
        d=unencoder.leerJSONArchivo('aparatoselectronicos.json')
        self.__M=unencoder.decodificarDiccionario(d)

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        unobjen=ObjectEncoder()
        diccionario=self.__M.toJSON()
        unobjen.guardarJSONArchivo(diccionario, "aparatoselectronicos.json")
        print('Salir')
    def ingresador(self):
        unAparato=None
        tipodeaparato=input('ingrese el tipo de aparato: \n [televisor] \n [lavarropas] \n [heladera]\n ').lower()
        marca = input("Ingrese la marca: ")
        modelo = input("Ingrese el modelo: ")
        color = input("Ingrese el color: ")
        paisFabricacion = input("Ingrese el pais de fabricacion: ")
        preciobase=int(input('ingrese el precio base: '))
        if tipodeaparato== 'Televisor'.lower():
            tipopantalla=input('ingrese el tipo de pantalla: [lcd] [led]: \n').lower()
            pulgadas=int(input('ingrese pulgadas: '))
            definicion=input('ingrese definicion: [HD] [FULLHD] [SD]').lower()
            conexion=input('ingrese si tiene conexion a internet: [si] [no]\n')
            conexion=conexion=='si'
            unAparato = televisor(marca,modelo,color,paisFabricacion,preciobase,tipopantalla,pulgadas,definicion,conexion)
        if tipodeaparato=='lavarropas':
            capacidad=int(input('ingrese la capacidad: '))
            velocidad=input('ingrese la velocidad de centrifugado: 600 rpm o 1200 rpm ')
            cantp=int(input('ingrese la cantidad de programas: '))
            tipodecarga=input('ingrese el tipo de carga: [frontal] [superior]: ')
            unAparato=lavarropa(capacidad,velocidad,cantp,tipodecarga,marca,modelo,color,paisFabricacion,preciobase)
        if tipodeaparato=='heladera':
            litros=int(input('ingrese la cantidad de litros: '))
            freezer=input('posee freezer? [si] [no]: ').lower()
            freezer=freezer=='si'
            ciclica=input('es ciclica? [si] [no]: ').lower()
            ciclica=ciclica=='si'
            unAparato=Heladeras(litros,freezer,ciclica,marca,modelo,color,paisFabricacion,preciobase)
        return unAparato







        #\

    def opcion1(self):
        print("insertar aparato en una pocicion a")
        insertado=False
        unaparato=self.ingresador()
        pos=int(input('ingrese la posicion: '))
        while not insertado:
            try:
                self.__M.insertarElemento(unaparato,pos)
            except IndexError:
                print('posicion erronea intente nuevamente')
                pos=int(input('ingrese la posicion: '))

            else:
                insertado=True
                print('aparato insertado')
        
    def opcion2(self):
        print("opcion b")
        unAparato = self.ingresador()
        self.__M.agregaraparato(unAparato)
    def opcion3(self):
        print("opcion 3")
        pos=int(input('ingrese una posicion para mostrar: '))
        print(self.__M.mostrarAparato(pos))
    def opcion4(self):
        print ('opcion 4') 
        conth=contl=conttv=0
        for elemento in self.__M:
            if isinstance(elemento,Heladeras)and elemento.getmarca()=='phillips':
                conth+=1
            if isinstance(elemento,televisor)and elemento.getmarca()=='phillips':
                conttv+=1
            if isinstance(elemento,lavarropa)and elemento.getmarca()=='phillips':
                contl+=1
        print('la cantidad de aparatos phillips son: {}'.format(contl+conth+conttv))
        print('heladeras: {}'.format(conth))
        print('televisores: {}'.format(conttv))
        print('lavarropas: {}'.format(contl))
    def opcion5(self):
        print('Mostrar la marca de todos los lavarropas que tienen carga superior .')
        marcas:List[str]=[]
        for elemento in self.__M:
            if isinstance(elemento,lavarropa)and elemento.getmarca().lower() not in [unaMarca.lower() for unaMarca in marcas]and elemento.gettipo() == "Superior":
                marcas.append(elemento.getmarca())
        marcas.sort()
        for unaMarca in marcas:
            print(unaMarca)
    def opcion6(self):
        for elemento in self.__M:
            print(elemento)







