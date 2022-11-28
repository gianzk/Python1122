#valores por defecto
def rango(start,stop,step=1):
    return start+stop+step


a=rango(1,10)
b=rango(1,10,2)

print(a,b)


def calcularPrecio(precio,porcentajeDescuento=1):
    return precio*porcentajeDescuento

p1=calcularPrecio(100)
p2=calcularPrecio(100,0.8)
