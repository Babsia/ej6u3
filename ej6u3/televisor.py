from tkinter import TRUE
from aparatos import aparatos
class televisor(aparatos):
    #tipo de pantalla, pulgadas, tipo de definición (SD, HD, FULL HD), conexión a internet(Verdadero/Falso).
    __tipo_de_pantalla=''
    __pulgadas=''
    __definicion=''
    __conexion=False
    def __init__(self,marca,modelo,color,pais,precio,tipop:str,pulgadas:str,definicion:str,conexion:bool):
        #marca, modelo, color, país de fabricación y precio base
        super().__init__(marca,modelo,color,pais,precio)
        self.__tipo_de_pantalla=tipop
        self.__pulgadas=pulgadas
        self.__definicion=definicion
        self.conexion=conexion
    def gettipoP(self):
        return self.__tipo_de_pantalla
    def getpulgadas(self):
        return self.__pulgadas
    def getdef(self):
        return self.__definicion
    def getconexion(self):
        return self.__conexion
    def __str__(self):
        cadena=super().__str__()+("tipo de pantalla:{} pulgadas:{} \n definicion:{} conexion:{} \n".format(self.__tipo_de_pantalla,self.__pulgadas,self.__definicion,self.__conexion))
        return cadena
    def importetotal(self):
        importe=self.__precio
        if self.__definicion.upper()=='SD':
            importe+=importe*0.01
        elif self.__definicion.upper()=='HD':
            importe+=importe*0.02
        elif self.__definicion.upper()=='FULLHD':
            importe+=importe*0.03
        if self.__conexion==True:
            importe+=self.__precio*0.1
        return importe





