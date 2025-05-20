"""
Suma de los primeros N números naturales: Pedir un número y calcular la suma desde 1 hasta N.
Se utiliza la formula para saber la suma de los primeros N naturales:
S = N x N (N + 1) / 2.
input-> 5
output-> 15, porque 1 + 2 + 3 + 4 + 5 = 15
"""
num = int(input("Ingresa un numero:"))
suma = num * (num + 1) // 2
print(suma)