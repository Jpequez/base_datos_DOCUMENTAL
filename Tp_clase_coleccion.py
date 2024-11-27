from Tp_clase_documentos import *
from Tp_clase_stringadicc import *

'''2.creamos la clase coleccion '''

class Coleccion(object):
   def __init__(self , nombre):
      self.nombre = nombre
      self.documentos = {}

   def agregar_documentos(self,documento):
      self.documentos[documento.id] = documento

   def eliminar_documento(self, id_documento):
        if id_documento in self.documentos:
            del self.documentos[id_documento]

   def buscar_documento(self, id_documento):
      return self.documentos.get(id_documento, None)

   def __str__(self):
      return f"Coleccion {self.nombre} con {len(self.documentos)} documentos"
   
   def importar_coleccion(self, ruta_archivo):
      with open(ruta_archivo , 'r') as file:
         schema =file.readline().replace("\n", "")
         parser = string_A_dicc(schema)
         i = 0 
         line = file.readline()

         while line != "":
            d = Documento(i,parser.convertidor(line.strip())) 
            self.agregar_documentos(d)
            i = i+1
            line = file.readline()
         
         print ("importacion exitosa ")
         
   def lista_documentos (self, valor):
      i = 0 
      while valor.buscar_documento(i) != None:
         print (valor.buscar_documento(i))
         i = i + 1
         print ("-"*90)


# c = Coleccion('Libros')

# libro1 = Documento(1,{'Titulo':'Python para todos', 'Autor': 'Teto Medina'})
# libro2 = Documento(2,{'Titulo': 'Fundamentos del lenguaje ', 'Autor': 'Eduso'})
# #agregamos un libro a nuestra collecion "libros"
# c.agregar_documentos(libro1)
# c.agregar_documentos(libro2)
# #buscamos un documento
# libro = c.buscar_documento(1)
# print (libro.obtenervalor('Titulo'), libro.obtenervalor('Autor'))

# #borramos un documento
# c.eliminar_documento(libro.id)

# #buscador para libros
# libro = c.buscar_documento(1)
# if libro is not None:
#    print(libro.obtenervalor('Titulo'), libro.obtenervalor('Autor'))
# else:
#    print("El libro no existe mas")

# funcion importar archivo 

# direccion = "C:\\Users\\CHELO\\Documents\\GitHub\\base_datos_DOCUMENTAL\\datos_personales.csv"
# prueba = Coleccion ("prueba01")
# prueba.importar_coleccion(direccion)
# print(prueba)
# print(prueba.buscar_documento(2))
# '''// se creo la clase collecion que manejara los documentos
# puede agregar,eliminar,buscar'''


# c = Coleccion ("prueba1 ")
# direccion = "C:\\Users\\CHELO\\Documents\\GitHub\\base_datos_DOCUMENTAL\\datos_personales.csv"
# c.importar_coleccion(direccion)
# c.lista_coleccion(c)