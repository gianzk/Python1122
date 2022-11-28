lista=["nombre",10,42,12,45,6,7,8,9]
lista[-1]=8
print(lista)
print("elementos",lista[:2])
print("elementos 2",lista[2::3])
print("elementos 3",lista[0:4:2])
lista.append('add')
print(lista)
valor=lista.index(42)
print(valor)
lista.pop(1) # tienes que darle la posicion // removio el 10 ya que tiene la posicion 1
print(lista)
if 6 in lista:
    lista.remove(6) #tienes que darle el valor
print(lista)
lista.reverse()
print(lista)
lista.clear()
print(lista)



