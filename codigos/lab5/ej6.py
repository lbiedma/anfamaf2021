import numpy as np
from ej1 import simpson

def periodo(alpha_rad, theta):
    denominador = np.sqrt(1 - np.sin(alpha_rad / 2)**2 * np.sin(theta)**2)
    return 1 / denominador


def pendulo(longitud, alpha):
    alpha_rad = alpha * np.pi / 180
    fun_periodo = lambda theta: periodo(alpha_rad, theta)

    integral = simpson(fun_periodo, 0, np.pi / 2, 2**10)

    periodo_final = 4 * np.sqrt(longitud / 9.8) * integral

    print(f"Tenemos un periodo de {periodo_final:.2f}")
    return periodo_final

