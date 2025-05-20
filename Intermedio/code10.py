import turtle
import time

# Configuración inicial de la ventana
wn = turtle.Screen()
wn.title("Torres de Hanoi")
wn.bgcolor("white")
wn.setup(width=800, height=400)

# Variables globales
num_disks = 4  # Cambia esto para más discos
peg_positions = [-250, 0, 250]  # Posiciones X de las torres

# Crear una lista para almacenar los discos como tortugas
discos = []

# Crear los postes
def dibujar_postes():
    poste = turtle.Turtle()
    poste.hideturtle()
    poste.speed(0)
    poste.pensize(5)
    for x in peg_positions:
        poste.penup()
        poste.goto(x, -150)
        poste.pendown()
        poste.goto(x, 100)

# Crear discos como tortugas
def crear_discos(n):
    for i in range(n):
        disco = turtle.Turtle()
        disco.shape("square")
        disco.shapesize(stretch_wid=1, stretch_len=(n - i) * 1.5)
        disco.color("skyblue")
        disco.penup()
        disco.goto(peg_positions[0], -140 + i * 20)
        discos.append(disco)

# Pegar torres como listas (pila)
torres = [list(reversed(range(num_disks))), [], []]

# Mover disco gráficamente
def mover_disco(origen, destino):
    disco_id = torres[origen].pop()
    torres[destino].append(disco_id)
    disco = discos[disco_id]

    # Mover hacia arriba
    disco.goto(disco.xcor(), 120)
    time.sleep(0.2)

    # Mover horizontalmente
    disco.goto(peg_positions[destino], 120)
    time.sleep(0.2)

    # Calcular nueva altura
    nueva_y = -140 + torres[destino].index(disco_id) * 20
    disco.goto(peg_positions[destino], nueva_y)
    time.sleep(0.2)

# Algoritmo recursivo
def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        mover_disco(origen, destino)
    else:
        hanoi(n - 1, origen, auxiliar, destino)
        mover_disco(origen, destino)
        hanoi(n - 1, auxiliar, destino, origen)

# Ejecutar
dibujar_postes()
crear_discos(num_disks)
time.sleep(1)
hanoi(num_disks, 0, 2, 1)
wn.mainloop()
