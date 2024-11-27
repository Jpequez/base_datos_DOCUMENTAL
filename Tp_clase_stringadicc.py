schema = "Nombre,Apellido,Edad,Mail,altura"
row = "jose,pequez,22,pequezjoseluis@gmail.com,2.23"

class string_A_dicc(object):
   def __init__(self, schemaStr, separator=","):
        self.schema = schemaStr.split(separator)
        self.separator = separator

   def convertidor(self, row):
        temp = row.split(self.separator)
        if len(temp) == len(self.schema):
            i = 1
            d = {}
            while i < len(temp):
                d[self.schema[i]] = temp[i]
                i = i + 1
            return d

