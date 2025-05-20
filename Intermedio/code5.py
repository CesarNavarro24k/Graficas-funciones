"""
Suma de números pares en una lista.
"""
numeros = [ 
    5,6,7,8,14,60,45,78
]
suma_pares = 0
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        print("Estos son los numeros pares de tu lista:", numeros[i])
        suma_pares += numeros[i]
print("La suma de los numeros pares de la lista es:", suma_pares)
