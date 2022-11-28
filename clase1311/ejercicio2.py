####Funciones 

def nombreFuncion():
    print("Hello word")

nombreFuncion()


def nombreFuncionConParametro(variableNombre):
    print("Hello word",variableNombre)

nombre="gianmarco"
nombreFuncionConParametro(nombre)

""" la funcion debe tener el return para que se pueda asignar a una variable
variable1=nombreFuncionConParametro
print(variable1) """

def saludar():
    """ ACA PUEDES AGREGAR LOGICA QUE DESEES """
    return "Hello word desde funcion" # 

saludo=saludar()

print(saludo)

### realizar una funcion que reciba 2 parametros numericos mayores a 0 (puedes colocarlo en duro) y retorne la suma

n1=int(input("numero1:"))
n2=int(input("numero2:"))

def suma(sumando1,sumando2):
    c=-1
    if( sumando1 >= 0 and sumando2 >=0):
        c=sumando1+sumando2
    return c

suma(1,2)

print(suma(10,12))
""" print(suma(21,12))
print(suma(14,12))
print(suma(16,12))
print(suma(13,12))
print(suma(17,12))
print(suma(16,14)) """

##realizar una funcion que compare dos numero,que los numero sea parametros

def comparar(a,b):
    if a==b:
        return (f"El numero : ",a,"es igual a : ",b)
    elif a!=b:
        return ("Son numeros diferentes")
    elif a>b:
        return (f"El numero : ", a ,"es mayor que : ", b)
    elif b>=a:
        return (f"El numero : " ,b, "es mayor que : " ,a)
    else:
        return ("error")

print(f'Ingresar 2 numeros')
valor1=float(input("Ingrese un numero: "))
valor2=float(input("Ingrese un numero: "))
comparar(valor1,valor2)








