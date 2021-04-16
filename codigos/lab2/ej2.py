# Importamos nuestra implementación de bisección
from ej1 import rbisec
# Importamos el módulo de gráficos de matplotlib
import matplotlib.pyplot as plt

def raiz_de_tres(x):
    """
    Función que nos devuelve la raíz cuadrada de x menos 3, para encontrar x**2 = 3.
    """
    return x**2 - 3

# Obtenemos nuestro historial de puntos y evaluaciones
hx, hf = rbisec(raiz_de_tres, [0, 2], 1e-5, 100)
# Imprimimos en pantalla el último valor de x
print(hx[-1])

# Graficamos el historial de puntos con marcador estrella
plt.plot(hx, hf, '*')

# Creamos una lista de 21 puntos equiespaciados entre 0 y 2 y sus valores:
# puntos = [0, 0.1, 0.2, ... , 1.9, 2]
# evals = [f(0), f(0.1), ..., f(1.9), f(2)]
puntos = [0]
evals = [raiz_de_tres(0)]
for idx in range(1, 21):
    puntos.append(idx * 0.1)
    evals.append(raiz_de_tres(idx * 0.1))

# Graficamos puntos en X y evals en Y
plt.plot(puntos, evals)
# Mostramos ambos gráficos al mismo tiempo
plt.show()

