import json
from Lista import Lista
from aparatos import aparatos
from heladera import Heladeras
from lavarropas import lavarropa
from televisor import televisor



class ObjectEncoder:


    def decodificarDiccionario(self, d):
        retorno = None
        if "__class__" not in d:
            retorno = d
        else:
            class_name = d["__class__"]
            class_ = eval(class_name)
            if class_name == "Lista":
                aparatos = d["aparatos"]
                unaColeccionAparatos:Lista = class_()
                for i in range(len(aparatos)):
                    dAparato = aparatos[i]
                    class_name = dAparato.pop("__class__")
                    class_ = eval(class_name)
                    atributos = dAparato["__atributos__"]
                    unAparato = class_(**atributos)
                    unaColeccionAparatos.insertarElemento(unAparato, 0)
            retorno = unaColeccionAparatos
        return retorno
    

    def guardarJSONArchivo(self, diccionario: dict, nombreArchivo):
        archivo = open(nombreArchivo, "w", encoding="UTF-8")
        json.dump(diccionario, archivo, indent=4)
        archivo.close()
    

    def leerJSONArchivo(self, nombreArchivo):
        archivo = open(nombreArchivo)
        diccionario = json.load(archivo)
        archivo.close()
        return diccionario