from Nodo import Nodo
from zope.interface import implementer
from zope.interface import interface
from interfaz import interfaz
from aparatos import aparatos
@implementer(interfaz)
class Lista:
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0
    def __init__(self):
        self.__comienzo=None
        self.__actual=None


    
    def agregaraparato(self, aparato):
        nodo = Nodo(aparato)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
    def getope(self):
        return self.__tope
    def insertarElemento(self, elemento:aparatos, pos: int): 
        insertado = False
        unNodo = Nodo(elemento)
        if pos == 0:
            unNodo.setSiguiente(self.__comienzo)
            self.__comienzo = unNodo
            self.__actual = self.__comienzo
            insertado = True
        else:
            if self.__comienzo != None:
                i = 1
                aux = self.__comienzo
                while aux.getSiguiente() != None and i < pos:
                    aux = aux.getSiguiente()
                    i += 1
                if i == pos:
                    unNodo.setSiguiente(aux.getSiguiente())
                    aux.setSiguiente(unNodo)
                    insertado = True
                else:
                    raise IndexError("Indice fuera de rango")
        self.__tope += 1
        return insertado
    def mostrarAparato(self,posicionBuscada):
        i = 0
        self.__actual = self.__comienzo
        if (posicionBuscada == 1):
            aparatoBuscado = self.__actual.getDato()
    
        while i < posicionBuscada-1 and self.__actual.getSiguiente() != None:
            i += 1
            self.__actual =self.__actual.getSiguiente()
        
        if i< posicionBuscada-1 or i > posicionBuscada-1:
            raise(IndexError("Fuera de indice"))
        
        aparatoBuscado = self.__actual.getDato()
        return aparatoBuscado
        
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            aparatos=[unAparato.toJSON() for unAparato in self]
        )
        return d


