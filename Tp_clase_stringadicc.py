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

o = string_A_dicc(schema)
print(o.schema)

d = o.convertidor(row)
print (d)