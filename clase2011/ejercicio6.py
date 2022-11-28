##herencia
class Persona:
    def __init__(self,fullname,tipo,documento):
        self.fullname=fullname
        self.tipo=tipo
        self.documento=documento
    def tasaImpuesto(self,tasa):
        self.impuesto=tasa

class PersonaNatural(Persona):
    pass


p1=PersonaNatural()