### recursividad 
def jugar(intento : int =1 ):
    respuesta = input("¿De qué color es una naranja? ")
    print(f"tienes {intento-1} intento")
    if respuesta.lower() != "naranja":
        if intento > 1:
            intento -= 1 
            print(f"\nFallaste! Inténtalo de nuevo te quedan {intento} intentos")             
            jugar(intento)  # Llamada recursiva         
        else:
            print("\nPerdiste!")     
    else:
        print("\nGanaste!")

def suma(numero:int):
    if numero ==1:
        return 1
    else:
        return numero+suma(numero-1)

sumaTotal=suma(10)
print(sumaTotal)


def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

factorial=factorial(5)
print(factorial)
