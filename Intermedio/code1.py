"""
Factorial de un número: Implementar una función que calcule el factorial de un número.
"""
num = int(input("Ingresa el numero para el que le quieres conocer el factorial:"))
resultado = 1
if num >= 0:
    for i in range(1, num + 1):  
        resultado *= i
    print("El factorial de", num, "es:", resultado)
else:
    print("No esta definido el factorial para los numeros negativos")  
