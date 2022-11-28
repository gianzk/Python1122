try: 
    # lo que quiero intentar hacer
    n = float(input("Introduce un número: "))
    m = float(input("Introduce un número: "))
    print("{}/{} = {}".format(n,m,n/m))

except:
    # en caso de error, como lo resuelvo
    print("Ha ocurrido un error, introduce bien el número")
    n = 8
    m = 4
    print("{}/{} = {}".format(n,m,n/m))
