lista=["nombre",10,42,12,45,6]

if "nombre" in lista:
    print("el elemento existe en la lista")
else:
    print("el elemento no existe en la lista")

### lista anidada
### palabra=['p','a','l']
a=[1,2,3]
b=[3,4,5]
c=[6,7,"palabra"]

d=[a,b,c]
print(d[-1][-1])

if type(d[-1][-1])==str:
    print(d[-1][-1][-1])
