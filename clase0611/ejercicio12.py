#conjunto
conj=set()
print(type(conj))
conj={1,2,3,4,5,6}
conj2={4,5,6,7,8,9}

#operacion de conjunto son :interseccion ,union , diferencia ,diferencia simetrica ,etc

inter=conj.intersection(conj2)
print(inter)
union=conj.union(conj2)
print(union)
### el conjunto es una lista ??
## si y no

lista=[1,2,3,5,7]

conj3=set(lista)
print(conj3)

lista2=list(conj3)
print(lista2)