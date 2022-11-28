

loremipsum='hola mundo desde aca'

with open('./bd.txt','w') as archivo:
        archivo.write(loremipsum)
        archivo.write('\n hola')