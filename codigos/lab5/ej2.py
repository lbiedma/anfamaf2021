import numpy as np
from ej1 import *

intervalos = [4,10,20]

fun = lambda x : np.exp(-x)

# valor exacto de la integral:
I_exacta = - np.exp(-1) + np.exp(0)

print(f"El valor exacto de la integral es I={I_exacta}")

for N in intervalos:
	I = intenumcomp(fun,0,1,N,'simpson')
	err_exacto = np.abs(I-I_exacta)
	cota_error = (1/180) * (1/N)**4
	print(f"El valor aproximado es I={I}")
	print(f"El error exacto de integrar con N={N} intervalos es e={err_exacto} y la cota es c={cota_error}")
