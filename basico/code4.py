"""
Calculadanda de IMC.
"""
peso = float(input("Ingresa tu peso en kg:"))
altura = float(input("Ingresa tu altura en cm:"))
IMC = peso / altura ** 2
print(IMC)
if IMC < 18.5:
    print("Tienes el IMC bajo")
elif IMC >= 18.5 and IMC <= 24.9:
    print("Tienes el IMC nandmal")
elif IMC >= 25.0 and IMC <= 29.9:
    print("Tienes sobrepeso")
elif IMC >= 30.0 and IMC <= 34.9:
    print("Tienes obesidad tip I")
elif IMC >= 35.0 and IMC <= 39.9:
    print("Tienes obesidad tipo II")
elif IMC >= 39.9:
    print("Tienes obsidad tipo III")