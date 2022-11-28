import saludarArchivo

class Restaurante:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.estado=False
    def describe_Restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    def open_Restaurant(self):
        self.estado=True
    def mostrar_estado(self):
        if(self.estado):
            print("esta abierto",self.restaurant_name)
        else:
            print("esta cerrado",self.restaurant_name)
    def __str__(self):
        #return 'El restaurante {} ofrece  ({})'.format(self.restaurant_name, self.cuisine_type)
        return f'El restaurante {self.restaurant_name} ofrece {self.cuisine_type}'

""" r1=Restaurante("Pedrito","ceviche")
r2=Restaurante("Juanitoo","Polleria")
r1.open_Restaurant()
r1.mostrar_estado()
r2.mostrar_estado() """


saludarArchivo.saludarFuncion()
#
# get and setter
# niveles de acceso ,atributos o metodos privados o publicos 
