"""
Hacer un código para saber si el año es bisiesto
"""
año = int(input("Ingresa el año para el que deseas saber si es bisiesto: "))
if año % 4 == 0 and año % 100 != 0:
    print("El año es bisiesto")
elif año % 400 == 0:
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")
