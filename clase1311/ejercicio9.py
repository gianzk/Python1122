
my_string = "This string will be split"
print(my_string.split(sep=" "))

print(my_string.split(sep=" ", maxsplit=2)) #maxsplit -> delimita la cantidad de palabras a ser separadas de la cadena

# Find -> Realiza una búsqueda en texto

my_string = "Where's Waldo?"
print(my_string.find("Waldo"))


print(my_string.find("Wenda")) # No se encotro palabra buscada

### funcion genericas 
## ES UN AYUDA DEL TYPEOF is(diversos tipos de datos) dentro de un string
""" variable=""
variable.isnumeric """