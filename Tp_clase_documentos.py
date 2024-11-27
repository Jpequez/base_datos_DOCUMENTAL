'''1. creacion de la clase documento '''

class Documento(object):
   def __init__(self , id , contenido = None ):
      self.id = id
      self.contenido  = contenido if contenido is not None else {}

   def obtenervalor(self, clave):
      return self.contenido.get(clave, None)

   def alctualizarvalor (self,clave, valor):
      self.contenido[clave] = valor

   def __str__(self):
      return f"Documento (id ={self.id }, contenido= {self.contenido})"

''' // creamos una clase que maneje una coleccion de documentos , algunas funciones para modificar los contenidos '''