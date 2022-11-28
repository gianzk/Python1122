#pasar datos a una funcion por valor y referencia
#por valor
# los tipos entero,flotante ,boolean ,str 
variable=1 # no cambia su valor
def function1(variable):
    variable=variable+1
    return variable

resultado=function1(variable)
print(resultado)
print(variable)

# por referencia  las listas ,los diccionarios 
# conjuntos son mutables osea se pasan por referencia 
# quiere decir que su valor al intentar hacer un copia en 
# una funcion se altera
lista=[1,2,3,4] 

def aumentarLista(li):
    print(li)
    for i,j in enumerate(li):
        li[i]*=2
         #li[i-1]*=2 que al valor de lista[0]=lista[0]*2

aumentarLista(lista)
print(lista)










