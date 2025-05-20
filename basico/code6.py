"""
Determinar si un número es primo
"""
num = int(input("Ingresa un número: "))

if num > 1 and all(num % i != 0 for i in range(2, num)):
    print("Este número es primo")
else:
    print("Este número no es primo")
