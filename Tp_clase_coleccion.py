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

   
   def importar_coleccion(self, ruta_archivo):
      with open(ruta_archivo, 'r') as file:
        schema =file.readline().replace("\n", "")
        parser = string_A_dicc(schema)
        line = file.readline()
        i = 0 #(i funciona como id inicial de los documentos y se incrementa en el siguiente while)
 
        while line != "":
          d = Documento(i,parser.convertidor(line.strip())) 
          self.agregar_documentos(d)
          i = i+1 #( i como id_incremental )
          line = file.readline()
         
   def lista_documento(self):

      listadedocumentos = []
      for i in self.documentos:
         listadedocumentos.append(self.documentos[i])
      return listadedocumentos
   

   def __str__(self):
      return f"Coleccion {self.nombre} con {len(self.documentos)} documentos"