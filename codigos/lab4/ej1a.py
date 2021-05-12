import numpy as np
import matplotlib.pyplot as plt

# Leemos nuestro set de datos con Numpy
# Lo que tenemos entre comillas va a depender de dónde tenemos descargados nuestros archivos
# Recordar que, para Windows, las "\" deben reemplazarse por "\\"
datos = np.loadtxt("datos/lab4/datos1a.dat")

# Los datos vienen en dos columnas, podemos guardar la 1ra en "x" y la 2da en "y"
x = datos[:, 0]
y = datos[:, 1]

# Debemos calcular los 5 distintos coeficientes que se usan en el teórico
m = len(x)
sum_xi = sum(x)
sum_yi = sum(y)
sum_xi2 = sum(x ** 2)
sum_xiyi = sum(x * y)

# Hay que resolver el siguiente sistema lineal
# [m      sum_xi ] [a0] = [ sum_yi ]
# [sum_xi sum_xi2] [a1]   [sum_xiyi]

# En el teórico tenemos las fórmulas para cada uno de los coeficientes de la recta.
a0 = (sum_xi2 * sum_yi - sum_xiyi * sum_xi) / (m * sum_xi2 - sum_xi ** 2)
a1 = (m * sum_xiyi - sum_xi * sum_yi) / (m * sum_xi2 - sum_xi ** 2)

# Creamos una función que haga la evaluación de nuestra recta
def eval_pol(x):
    return a1 * x + a0

# Imprimimos en pantalla nuestros coeficientes
print(a0, a1)

# Armamos 100 puntos entre 0 y 5 y les aplicamos la función
z = np.linspace(0, 5, 100)
w = eval_pol(z)

# Ploteamos los puntos iniciales y la recta.
plt.plot(x, y, '*')
plt.plot(z, w)
plt.show()
