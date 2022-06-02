from aparatos import aparatos
class lavarropa(aparatos):
    # capacidad de lavado (5 Kg, 6kg, etc), velocidad de centrifugado (600 rpm, 1200 rpm), cantidad de programas, tipo de carga( Frontal, Superior).
    __capacidad=0
    __velocidad=''
    __Cprog=''
    __tipodecarga=''
    def __init__(self,capacidad:int,velocidad:str,Cprog:int,tipodecarga:str,marca,modelo,color,pais,precio):
        super().__init__(marca,modelo,color,pais,precio)
        self.__capacidad=capacidad
        self.__velocidad=velocidad
        self.__Cprog=Cprog
        self.__tipodecarga=tipodecarga
    #def __str__(self):
    def getcapacidad(self):
        return self.__capacidad
    def getvelocidad(self):
        return self.__velocidad
    def getcprog(self):
        return self.__Cprog
    def gettipo(self):
        return self.__tipodecarga
    def importetotal(self):
        importe=self.__precio
        if self.__capacidad<=5:
            importe+=importe*0.01
        elif self.__capacidad>5:
            importe+=importe*0.03
        return importe
    

    