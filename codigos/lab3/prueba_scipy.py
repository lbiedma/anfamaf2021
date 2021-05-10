import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

# Vamos a tratar de interpolar la parábola con spline cúbico con 5 puntos.
x = [-2.0, -1.0, 0.0, 1.0, 2.0]
y = [4.0, 1.0, 0.0, 1.0, 4.0]

# interp1d nos crea una función que evalúa el polinomio interpolante
polinomio = interp1d(x, y, kind="cubic")

# Armamos una lista de 100 puntos entre -2 y 2 y evaluamos ahí para plotear
z = np.linspace(-2, 2, 100)
w = polinomio(z)

plt.plot(x, y, "*", z, w)
plt.show()
