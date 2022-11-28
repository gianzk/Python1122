## tuplas

tupla=(1,2,3,1,5,[1,2,3],"texto",(1,2,3))
print(type(tupla))
print("pos1",tupla[0])
print("posicion final",tupla[-1])

### metodos de la tupla
posicion=tupla.index(1)
print("la posicion del valor que estoy ingresando",posicion)
numeroDeVeces=tupla.count(1)
print(numeroDeVeces) # las numero de  veces que se repite un valor