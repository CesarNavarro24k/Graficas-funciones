"""
Ordenamiento de lista (Burbuja).
Utilizar este metodo para ordendar una lista de numeros.
El ordenamiento es hace en pares, es decir el metodo siempre compara un par de numero y el que es mayor es colocado
a la derecha, así el ultimo numero sera el numero mayor de la lista.
"""
numeros = [
    5,3,4,8,7,5,1,2,3
]
for i in range(len(numeros)):
    for j in range(len(numeros)- i - 1):
        if numeros[j] > numeros[j + 1]:
            temp = numeros[j]
            numeros[j] = numeros[j + 1]
            numeros[j + 1] = temp
print(numeros)