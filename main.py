import numpy as np
import matplotlib.pyplot as plt
import os

# Crear la carpeta si no existe
os.makedirs('figuras', exist_ok=True)

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

# Pedir nombre al usuario
nombre = input("¿Qué nombre quieres darle al archivo de la gráfica? (sin extensión): ")

# Asegurar que el nombre tenga extensión .pdf
if not nombre.endswith('.pdf'):
    nombre += '.pdf'

# Guardar con el nombre especificado
ruta_completa = os.path.join('figuras', nombre)
plt.savefig(ruta_completa, format='pdf', bbox_inches='tight')

# Mostrar confirmación
print(f"Gráfica guardada como: {ruta_completa}")

# Mostrar la gráfica
plt.show()