import numpy as np
import matplotlib.pyplot as plt

# Generar datos
x = np.linspace(-10, 10, 400)
y = x**2

# Crear la gráfica
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'b-', linewidth=2)
plt.title('Gráfica de f(x) = x²')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Guardar como PDF
plt.savefig('grafica_x_cuadrado.pdf', format='pdf', bbox_inches='tight')

# Mostrar la gráfica
plt.show()