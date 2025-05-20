"""
Hacer un programa que cuente las palabras en un texto o frase
"""
frase = input("Ingresa la frase para contar las palabras: ").strip()

# Inicializamos contadores
cont = 0
en_palabra = False  # Para detectar el inicio de una nueva palabra

for caracter in frase:
    if caracter.isalnum():  # Si es una letra o número
        if not en_palabra:  # Si no estábamos en una palabra, iniciamos una nueva
            cont += 1
            en_palabra = True
    else:
        en_palabra = False  # Si encontramos un espacio u otro signo, ya no estamos en una palabra

print(f"El número de palabras en tu texto es: {cont}")
