"""
Mayor de tres números.
"""
num1 = int(input("Ingresa un primer numero:"))
num2 = int(input("Ingresa un segundo numero:"))
num3 = int(input("Ingresa un tercer numero:"))

if num1 > num2:
    print(f"El numero {num1} es mayor que {num2} y {num3}")

elif num2 > num3:
    print(f"El numero {num2} es mayor que {num3} y {num1}")
elif num3 > num1:
    print(f"El numero {num3} es mayor que {num1} y {num2}")