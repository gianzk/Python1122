## 
suma=0
cantidad=0
for i in range(1,101):
    suma +=i
    cantidad=i

##print(suma/cantidad)

####
listaNumeros=[]
for i in range(1,10):
    for j in range(1,10):
        if j>5:
            break
        else:
           listaNumeros.append([i,j])

""" 
print(listaNumeros) """

""" 
h = int(input('Ingrese la altura del triangulo: '))
for f in range(h):
    print('#'* (f+1))

     """
numero=int(input("ingrese un numero:"))
isPrimo=False

for n in range(2,numero): ###0.0000001  5645864564848481 
    if numero % n==0:
        isPrimo=True
        break

if isPrimo:
    print("no es primo")
else:
    print(" es primo")