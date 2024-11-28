# main.py
from Tp_clase_basedatos   import  *
from Tp_clase_coleccion   import  *
from Tp_clase_documentos  import  *
from Tp_clase_stringadicc import  *

def mostrar_menu():
    print("\n--- Base de Datos Documental ---")
    print("1. Crear colección")
    print("2. Importar CSV a colección")
    print("3. Consultar documento en colección")
    print("4. Eliminar documento de colección")
    print("5. Listar todos los documentos en colección")
    print("6. Salir")
    return input("Seleccione una opción: ")

def main():
    db = BasededatosDocumental()

    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            db.crear_coleccion(nombre_coleccion)
            print(f"Colección '{nombre_coleccion}' creada.")
        
        elif opcion == "2":
          nombre_coleccion = input("Ingrese el nombre de la colección: ")
          coleccion = db.obtener_coleccion(nombre_coleccion)
          if coleccion:
             ruta_csv = input("Ingrese la ruta del archivo CSV: ")
             coleccion.importar_coleccion(ruta_csv)
             print ("IMPORTACION EXITOSA".title())
          else:
              print (f"IMPORTACION FALLIDA NO EXISTE LA COLECCION : {nombre_coleccion}")
            

        elif opcion == "3":
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            coleccion = db.obtener_coleccion(nombre_coleccion)
            if coleccion:
                doc_id = int(input("Ingrese el ID del documento: "))
                documento = coleccion.buscar_documento(doc_id)
                if documento:
                    print("Documento encontrado:".title())
                    print(documento)
                else:
                    print("Documento no encontrado.".title())
            else:
                print(f"Colección '{nombre_coleccion}' no encontrada.")

        elif opcion == "4":
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            coleccion = db.obtener_coleccion(nombre_coleccion)
            if coleccion:
                doc_id = int(input("Ingrese el ID del documento a eliminar: "))
                documento = coleccion.buscar_documento(doc_id)
                contador= True
                while contador:
                 if documento:
                    coleccion.eliminar_documento(doc_id)
                    print("Eliminacion Existosa".title())
                    contador = False
                 else:
                    print("Error , ID inexistente , intente nuevamente")  
                    doc_id = int(input("Ingrese el ID del documento a eliminar: ")) 
                    documento = coleccion.buscar_documento(doc_id)   
            else:
                print(f"no existe tal coleccion {nombre_coleccion} para poder eliminar un documento")
                
        elif opcion == "5":
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            coleccion = db.obtener_coleccion(nombre_coleccion)
            if coleccion:
                documentos = coleccion.lista_documento()
                if documentos:
                    print("\n--- Lista de Documentos ---")
                    for doc in documentos:
                        print(doc)
                        print("-"*50)
                else:
                    print("No hay documentos en la colección.".title())
            else:
                print(" NO EXISTE ESA COLECCION, INTENTE NUEVAMENTE o CREE UNA COLECCION")
        elif opcion == "6":
            print("Saliendo del programa.".title())
            break
        
        else:
            print("Opción no válida. Intente nuevamente.".title())

if __name__ == "__main__":
    main()


