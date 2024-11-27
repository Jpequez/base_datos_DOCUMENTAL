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
    

    def __str__(self):
        return f"Coleccion{self.nombre} con {len(self.documentos)} documentos."
    

D = Coleccion ("libros")

a = BasededatosDocumental()

a.crear_coleccion("pelis")

