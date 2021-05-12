import matplotlib.pyplot as plt
import numpy as np

# Generamos 20 puntos en el intervalo [0, 10]
# y los correspondientes puntos en la recta original
x = np.linspace(0, 10, 20)
y = 0.75 * x - 0.5

# Aplicamos una desviación a cada punto en y por una distribución normal
y_desviado = y + np.random.randn(20)

# Hacemos un ajuste lineal sobre esta nueva nube de puntos
polinomio = np.polyfit(x, y_desviado, 1)
# Evaluamos en x este ajuste para graficar
eval_y_desviado = np.polyval(polinomio, x)

# Graficamos las 3 cosas juntas.
plt.plot(x, y, label="recta original")
plt.plot(x, y_desviado, "*", label="puntos desviados")
plt.plot(x, eval_y_desviado, label="nueva aproximacion")
plt.legend()
# Una grilla para tener como referencia
plt.grid()
plt.show()
