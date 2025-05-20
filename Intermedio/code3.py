"""
Palíndromo
"""
palabra = input("Ingresa la palabra para saber si es un palindromo:")
if palabra == palabra[::-1]:
    print("Es un palindromo")
else:
    print("No es un palindromo")
    