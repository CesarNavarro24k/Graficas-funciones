import random
num = random.randint(1,10)
adi_num = int(input("Cual numero crees que va a salir?(entre 1 y 10):"))
cont = 0
intentos = 3
while intentos > 0:
    if num == adi_num:
        print("Has adivinado el numero")
        cont += 1
        break
    else:
        intentos -= 1
    if intentos > 0:
        print(f"No has adivinado el numero")
        print(f"Te quedan {intentos} intentos")
        adi_num = int(input("Cual numero crees que va a salir?(entre 1 y 10):"))
    else:
        print(f"No has adivinado el numero, el numero es {num}")
    print(f"Tu puntaje es: {cont} puntos")

"""
Crea un programa en Python que permita jugar a una adivinanza de números. 
El programa debe generar un número aleatorio entre 1 y 10,
y el jugador tendrá 3 intentos para adivinarlo. Después de cada intento fallido, 
el programa debe indicar cuántos intentos le quedan al jugador.
Si el jugador adivina el número, se le felicita y se suma un punto a su puntaje. Al finalizar, 
se debe mostrar el número correcto (si no fue adivinado) y el puntaje obtenido.
Ejemplo:
Cual numero crees que va a salir?(entre 1 y 10):6
No has adivinado el numero
Te quedan 2 intentos
Cual numero crees que va a salir?(entre 1 y 10):7
Tu puntaje es: 0 puntos
No has adivinado el numero
Te quedan 1 intentos
Cual numero crees que va a salir?(entre 1 y 10):9
Tu puntaje es: 0 puntos
No has adivinado el numero, el numero es 2
Tu puntaje es: 0 puntos
"""