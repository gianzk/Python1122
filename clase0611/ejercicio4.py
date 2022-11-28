## operador %
#residuo=12%7
#print(residuo)
#12=7*1 + 5
#d =D*q +r

#Ejercicio

salario = float(input('Ingrese su salario anual: '))
tasa=0.0
renta=0.0

if salario>=0 and salario< 10000:
    tasa=0.05
elif salario >= 10000 and salario <20000:
    tasa=0.15
elif salario >= 20000 and salario <30000:
    tasa=0.25
elif salario >= 30000 and salario <40000:
    tasa=0.35
else:
    tasa=0.45

renta=tasa*salario

print(renta)