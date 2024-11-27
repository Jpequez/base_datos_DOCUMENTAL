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

# d = Documento(1,{'nombre': 'jose'})
# print(d)

# #obtenemos un valor que no existe
# nombre = d.obtenervalor('nombre') # intencionalmente buscamos un valor que no existe dejando una imprension "no existente"
# if not d.obtenervalor('direccion'):
#    print("no existe la direccion")
# #obtenemos un valor existente#
# print (d.obtenervalor('nombre'))  # cuando no se encuentra tira un none (no definido)
# #actualizamos o agragamos un valor#
# if not d.obtenervalor('direccion'):
#    d.alctualizarvalor ('direccion', 'calle 12')
# print (d.obtenervalor('direccion'))



''' // creamos una clase que maneje una coleccion de documentos , algunas funciones para modificar los contenidos '''