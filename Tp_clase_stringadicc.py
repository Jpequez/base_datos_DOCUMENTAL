schema = "Nombre,Apellido,Edad,Mail,altura"
row = "jose,pequez,22,pequezjoseluis@gmail.com,2.23"

class string_A_dicc(object):
    def __init__(self, schemastr, separator=","):
        self.separator = separator
        self.schema = schemastr.split(separator)

    def convertidor(self, row):
        temp = row.split(self.separator)
        if len(temp) == len(self.schema):
            dicc = {}
            i = 0
            while i < len(temp):
                dicc[self.schema[i]] = temp[i]
                i = i + 1
            return dicc

