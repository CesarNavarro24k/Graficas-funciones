import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = x**2
plt.plot(x, y)
plt.show()
plt.savefig(f"graficas/plot.pdf")