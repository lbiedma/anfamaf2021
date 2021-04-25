import math
from ej5 import ripf

def fun_lab2ej6(x):
	return math.pow(2,x-1)

for x0 in []:
	hx = ripf(fun_lab2ej6, x0, 1e-5, 100)
	print(hx[-1])
