"""
Hacer un programa que identifique los tipos de triangulos por sus:
1. lados
2. angulos
"""
lado1 = int(input("Ingresa el tamaño del primer lado como numero entero:"))
lado2 = int(input("Ingresa el tamaño del segundo lado como numero entero:"))
lado3 = int(input("Ingresa el tamaño del tercer lado como numero entero:"))

if lado1 == lado2 == lado3:
    print("El triangulo es equilatero porque tiene todos sus lados iguales")
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    print("El triangulo es isoceles porque solamente tiene dos lados iguales")
elif lado1 != lado2 != lado3:
    print("El triangulo es escaleno porque tiene tres lados diferentes")
angulo1 = int(input("Ingresa el valor para el primer ángulo:"))
angulo2 = int(input("Ingresa el valor para el segundo ángulo:"))
angulo3 = int(input("Ingresa el valor para el tercer ángulo:"))
if angulo1 == angulo2 == angulo3:
    print("El triangulo es acutángulo debido a que sus tres angulos son iguales")
elif angulo1 == 90 or angulo2 ==90 or angulo3 == 90:
    print("El triangulo es rectangulo, debido a que uno de los lados mide 90 grados")
elif (angulo1 >90 and angulo1 <180) or (angulo2 > 90 and angulo2 < 180) or (angulo3 >90 and angulo3 <180):
    print("El triangulo es obtusángulo debido a que uno de sus ángulos es obtuso")

