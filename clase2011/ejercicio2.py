try:
    edad=int(input("ingrese su edad: "))
    print("su edad es",edad)
except:
    print("ingrese una valor numerico")
else:
    print("este solo se ejecuta si el 'try' es correcto ")
finally:
    print("siempre se ejecuta")