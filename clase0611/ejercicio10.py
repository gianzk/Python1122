#diccionarios

diccionario={} #inizializa un diccionario
print("el tipo de dato (collection",type(diccionario))
### llave -> valor 
diccionario={
    "key1":200,
    "1.1":100,
    "1.2":200
}
print("el diccionario ",diccionario)

print(diccionario['key1']) #obtener el valor de la llave
llaves=diccionario.keys()
print(type(llaves))
items=diccionario.items()
print(items)

diccionario["key1"]=diccionario["key1"]/2

print(items)