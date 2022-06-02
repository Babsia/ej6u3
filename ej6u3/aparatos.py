import abc
from abc import ABC

class aparatos(ABC):
    #marca, modelo, color, país de fabricación y precio base
    __marca=''
    __modelo=''
    __color=''
    __paisF=''
    __precio=''
    def __init__(self,marca,modelo,color,pais,precio):
        self.__marca=marca
        self.__modelo=modelo
        self.__color=color
        self.__paisF=pais
        self.__precio=precio
    def getmarca(self):
        return self.__marca
    def getmodelo(self):
        return self.__modelo
    def getcolor(self):
        return self.__color
    def getprecio(self):
        return self.__precio
    def getpais(self):
        return self.__paisF
    #\
    def __str__(self):
        cadena=''
        cadena=('marca:{} modelo:{} \n color:{} pais:{} \n precio:{}'.format(self.__marca,self.__modelo,self.__color,self.__paisF,self.__precio))
        return cadena
    @abc.abstractclassmethod
    def importetotal(self):
        pass
    
