##Escribir un programa que pida al usuario un número entero 
# y muestre por pantalla si es par o impar.

numero=int(input("ingrese el numero"))

residuode2=numero%2

if residuode2 == 0:
    print("es par")
else:
    print("es impar")
