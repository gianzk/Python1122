import re
texto = "En esta cadena se encuentra una palabra mágica"
busqueda=re.search("dictionario",texto)

print(busqueda)
if busqueda:
    print("encontro")
else:
    print("no encontro")


