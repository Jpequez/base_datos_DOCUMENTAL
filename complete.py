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

d = Documento(1,{'nombre': 'jose'})
print(d)

#obtenemos un valor que no existe
nombre = d.obtenervalor('nombre') # intencionalmente buscamos un valor que no existe dejando una imprension "no existente"
if not d.obtenervalor('direccion'):
   print("no existe la direccion")
#obtenemos un valor existente#
print (d.obtenervalor('nombre'))  # cuando no se encuentra tira un none (no definido)
#actualizamos o agragamos un valor#
if not d.obtenervalor('direccion'):
   d.alctualizarvalor ('direccion', 'calle 12')
print (d.obtenervalor('direccion'))



''' // creamos una clase que maneje una coleccion de documentos , algunas funciones para modificar los contenidos '''


'''2.creamos la clase coleccion '''

class Coleccion(object):
   def __init__(self , nombre):
      self.nombre = nombre
      self.documentos = {}

   def agregar_documentos(self,documento):
      self.documentos[documento.id] = documento

   def eliminar_documento (self, id_documento):
      if id_documento in self.documentos:
         del self.documentos[id_documento]

   def buscar_documento(self, id_documento):
      return self.documentos.get(id_documento, None)

   def __str__(self):
      return f"Coleccion {self.nombre} con {len(self.documentos)} documentos"


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





'''// se creo la clase collecion que manejara los documentos
puede agregar,eliminar,buscar'''


'''3.creamos la clase base de datos  '''

class BasededatosDocumental (object):
    def __init__(self):
        self.colecciones= {}

    def crear_coleccion (self,nombre_coleccion):
        if nombre_coleccion not in self.colecciones:
            self.colecciones[nombre_coleccion] = Coleccion(nombre_coleccion)

    def eliminar_coleccion (self, nombre_coleccion):
        if nombre_coleccion in self.colecciones:
            del self.colecciones[nombre_coleccion]

    def obtener_coleccion (self ,nombre_coleccion):
        return self.colecciones.get(nombre_coleccion,None)
    
    def __str__(self):
        return f"Coleccion{self.nombre} con {len(self.documentos)} documentos."
    

''' manejara las colecciones ,, tendra capacidad de eliminar y mostrar las colecciones existentes de al base de datos '''



''' clase string a diccionario '''
schema = "Nombre,Apellido,Edad,Mail,altura"
row = "jose,pequez,22,pequezjoseluis@gmail.com,2.23"

class string_A_dicc(object):
    def __init__(self,schemastr,separator= ","):
        self.schema = schemastr.split(separator)
        self.seperator = separator


    def convertidor (self, row):
        tempo = row.split(self.seperator)
        if len(tempo)== len(self.schema):
         i = 0 
         dicc = {}
         while i < len(tempo):
            #dicc[self.schema[i]] = tempo[i]
            key = self.schema[i]
            val = tempo[i]
            dicc[key] = val
            i = i+1
        return dicc
    
''' permite la conversion de un archivo csv a diccionario '''