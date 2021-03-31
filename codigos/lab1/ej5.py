# Inciso a
# print(6 * 5 * 4 * 3 * 2 * 1)

resultado = 1
for num in range(1, 7):
    resultado = resultado * num

print(f"El factorial de 6 con un for es {resultado}")


# Inciso b
# import math
from math import factorial
print(f"El factorial de 6 con la librería math es {factorial(6)}")

# Inciso c
def factorial_mio(numero):
    resultado = 1
    for num in range(1, numero + 1):
        resultado = resultado * num

    return resultado

print(f"El factorial de 6 con nuestra funcion es {factorial_mio(6)}")
