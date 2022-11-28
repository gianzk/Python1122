### cuando tienees indetermiados numero de argumentos en una lista
def indeterminados_posicion(*args):
    for arg in args:
        print(arg)

indeterminados_posicion(5,"Hola",[1,2,3,4,5],{'dia':'sabado'})
#### cuando tienes indeterminados numero de argumentos llave valor 
def indeterminados_nombre(**kwargs):
    print(kwargs) #
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])

indeterminados_nombre(n=5, c="Hola", l=[1,2,3,4,5])   




