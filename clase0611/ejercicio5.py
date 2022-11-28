#que vacuna toca segun la edad
edad =int(input("ingrese su edad:"))
vacuna=""


if edad>=0 and edad<18:
    vacuna="MODERNA"
elif edad>=18 and edad <30:
    vacuna="SINOPHARM"
elif edad>=30 and edad<45:
    vacuna="vacuna X"
else :
    vacuna="PFIZER"
print("la vacuna es ",vacuna)
print('la vacuna que te toca es {} con la edad {}'.format(vacuna,edad))
print(f'la vacuna que tomar es {vacuna} por su edad {edad}')

