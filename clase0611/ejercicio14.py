print("Bienvenido al curso de python")

while True:
    print("""Escribe una opcion 
            1)saludar
            2)sumar 
            3)salir""")
    opcion=input()

    if opcion == '1':
        print("hola mundo")
    elif opcion == '2':
        print("ingresa 2 numero")
        n1=float(input("numero 1"))
        n2=float(input("numero 2"))
        print(f"el resultado es {n1+n2}")
    elif opcion == '3':
        break;
    else:
        print("ingrese un opcion valida")