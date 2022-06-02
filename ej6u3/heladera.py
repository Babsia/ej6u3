from aparatos import aparatos
class Heladeras(aparatos):
    #capacidad en litros, freezer (Verdadero/Falso), cíclica (Verdadero/Falso).
    __litros=0
    __freezer=False
    __ciclica=False
    def __init__(self,litros:int,freezer:bool,ciclica:bool,marca,modelo,color,pais,precio):
        super().__init__(marca,modelo,color,pais,precio)
        self.__litros=litros
        self.__freezer=freezer
        self.__ciclica=ciclica
    def getcapacidad(self):
        return self.__litros
    def getfreezer(self):
        return self.__freezer
    def getcilica(self):
        return self.__ciclica
    def __str__(self):
        cadena=super().__str__()+("capacidad:{} frezzer:{} \n ciclica:{}".format(self.__litros,self.__freezer,self.__ciclica))
        return cadena
    def importetotal(self):
        importe=self.__precio
        if not self.__freezer:
            importe+=importe*0.01
        else:
            importe+=importe*0.05
        if self.__ciclica:
            importe+=importe*0.1
        return importe

