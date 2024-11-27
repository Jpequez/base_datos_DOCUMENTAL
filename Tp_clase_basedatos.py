from Tp_clase_coleccion import  Coleccion
from Tp_clase_stringadicc import string_A_dicc
from Tp_clase_documentos import Documento
class BasededatosDocumental (object):
    def __init__(self):
        self.colecciones= {}
    def crear_coleccion(self,nombre_coleccion):
        if nombre_coleccion not in self.colecciones:
            self.colecciones[nombre_coleccion] = Coleccion(nombre_coleccion)

    def eliminar_coleccion(self, nombre_coleccion):
        if nombre_coleccion in self.colecciones:
            del self.colecciones[nombre_coleccion]

    def obtener_coleccion(self ,nombre_coleccion):
        return self.colecciones.get(nombre_coleccion,None)
    
    def importar_csv ():
        direccion = "D:\CURSADA\orientacion a objetos\projecto_1.1\datos_personales.csv"
        with open(direccion, 'rt') as file:  
            schema = file.readline().replace("\n", "") 
            parser = string_A_dicc(schema) 
            i= 0 
            line= file.readline() 
 
            while line != "": 
                d=Documento(i,parser.convertidor(line)) 
                self.agregar_documento(d) 
                i = i+1 
                line= file.readline()
    def __str__(self):
        return f"Coleccion{self.nombre} con {len(self.documentos)} documentos."
    


