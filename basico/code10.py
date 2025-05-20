frase = input("ingresa una frase:")
vocales = "aeiou"
encontradas = []
for i in frase:
    if i in vocales:
        encontradas.append(i)
print(f"Las vocales encontradas son: {encontradas}")
print(f"La cantidad de vocales encontradas es: {len(encontradas)}")

"""
Escribe un programa en Python que solicite al usuario una frase y cuente cuántas vocales contiene.
El programa debe identificar las vocales en la frase, mostrarlas en una lista y al final indicar
la cantidad total de vocales encontradas.
No es necesario diferenciar entre vocales mayúsculas y minúsculas.
Ejemplo:
ingresa una frase:Hola mundo
Las vocales encontradas son: ['o', 'a', 'u', 'o']
La cantidad de vocales encontradas es: 4
"""
