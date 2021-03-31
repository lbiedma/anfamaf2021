# Importamos la función de raiz cuadrada de la librería math
from math import sqrt

def mala(a, b, c):
    """
    Esta función calcula las raíces usando Bhaskhara para ambas.
    Recibe a, b y c (pensando en el polinomio a*x**2 + b*x + c)
    y devuelve una lista con las dos raíces.
    """
    disc = b**2 - 4 * a * c

    if disc < 0:
        print("El discriminante es negativo, no vamos a encontrar raíces reales.")
        return None

    x_1 = (-b + sqrt(disc)) / (2.0 * a)
    x_2 = (-b - sqrt(disc)) / (2.0 * a)

    return [x_1, x_2]

def buena(a, b, c):
    """
    Casi lo mismo que mala, sólo que usamos Bhaskhara para calcular la raíz
    más lejana al cero y luego usamos que x_1 * x_2 = c / a para conseguir la
    segunda raíz. Esto permite eliminar errores numéricos.
    """
    disc = b**2 - 4 * a * c

    if disc < 0:
        print("El discriminante es menor que 0, intente de nuevo")
        return None

    # encontrar la raiz más lejana al cero en valor absoluto.
    if b > 0:
        x_1 = (-b - sqrt(disc)) / (2.0 * a)
    else:
        x_1 = (-b + sqrt(disc)) / (2.0 * a)

    x_2 = (c / a) / x_1

    return [x_1, x_2]

