### PLANTEO DEL PROBLEMA
### x = cuanto tengo que comprar de T1 y T2,
### (x1 := cantidad de T1, x2 := cantidad de T2)
### c = valores de cada kilo de fertilizante (10, 8)
### 3 restricciones, minimo de P, N y K
### x1 * 3 + x2 * 2 >= 3 (P)
### x1 * 1 + x2 * 3 >= 1.5 (N)
### x1 * 8 + x2 * 2 >= 4 (K)

### Se transforma (para entrar en scipy)
### x1 * -3 + x2 * -2 <= -3 (P)
### x1 * -1 + x2 * -3 <= -1.5 (N)
### x1 * -8 + x2 * -2 <= -4 (K)
###         [-3, -2]
### A_ub =  [-1, -3]
###         [-8, -2]
### b_ub = [-3, -1.5, -4]
### No tenemos restricciones de igualdad
### Tenemos cotas (0, inf) para nuestras variables, esto es la cota por defecto en Scipy

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

# Definimos nuestro vector de costos
c = np.array([10., 8])

# Definimos nuestra matriz de restricciones de desigualdad
A_ub = np.array([
    [-3., -2],
    [-1, -3],
    [-8, -2]
])
# y su vector
b_ub = np.array([-3, -1.5, -4])

# Vamos a guardar nuestra solución en una variable y corremos al mismo tiempo
solucion = optimize.linprog(c, A_ub, b_ub)
# Verificamos si la búsqueda de óptimo fue exitosa (success == True)
print(solucion.success)
# Imprimimos valores importantes
print(f"El mínimo se consigue en {solucion.x}")
print(f"El costo mínimo para generar el fertilizante adecuado es {solucion.fun}")

### GRAFICAMOS REGION FACTIBLE
### Para graficar debemos obtener nuestras rectas de las restricciones
### x2 = (-3/2) * x1 + 3/2 (P)
### x2 = (-1/3) * x1 + 1/2 (N)
### x2 = (-4) * x1 + 2 (K)

# Podemos graficar muchos puntos entre 0 y 1.
x_res = np.linspace(0, 1, 100)

# Hagamos las rectas
p_res = -1.5 * x_res + 1.5
n_res = -1 / 3 * x_res + 0.5
k_res = -4 * x_res + 2

# Grafiquemos las rectas
plt.plot(x_res, p_res, label="fosforo")
plt.plot(x_res, n_res, label="nitrogeno")
plt.plot(x_res, k_res, label="potasio")

# Ahora debemos tener en cuenta que nuestras restricciones son del tipo mayor igual
# Por lo tanto nuestro polígono de restricciones va a estar "relleno hacia el infinito"
# Podemos usar la función fill_between de matplotlib para graficarlo, pero primero
# debemos generar los extremos inferiores del poligono, que corresponden al maximo de todas las restricciones

# Podemos usar la función maximum de numpy para obtener los máximos elemento a elemento de cada lista
max_res = np.maximum(p_res, n_res)
max_res = np.maximum(max_res, k_res)

# Usamos fill_between, y ponemos una cota superior a los valores, por ejemplo 5, para rellenar por encima del poligono
plt.fill_between(x_res, max_res, 5, alpha=0.4, color="red")

# Podemos además graficar nuestra solución
plt.plot(solucion.x[0], solucion.x[1], "*k", label="solucion")
plt.legend()
plt.xlim([0, 1])
plt.ylim([0, 5])

# Mostramos en pantalla
plt.show()

