import ej1
import ej3
import ej5
import math

def lab2ej7bisec(x):
	# calcula u(x) = y
	fun_auxiliar = lambda y : y - math.exp(-(1-x*y)**2)
	hy, hu = ej1.rbisec(fun_auxiliar, [0.0,2.0], 1e-6, 100)
	y = hy[-1]
	return y

def lab2ej7newton(x):
	# calcula u(x) = y
	fun_auxiliar = lambda y : (y - math.exp(-(1-x*y)**2), \
		1 - math.exp(-(1-x*y)**2)*(-2*(1-x*y)*(-x)))
	hy, hu = ej3.rnewton(fun_auxiliar, 1.0, 1e-6, 100)
	y = hy[-1]
	return y

def lab2ej7ipf(x):
	fun_auxiliar = lambda y : math.exp(-(1-x*y)**2)
	hy = ej5.ripf(fun_auxiliar, 1.0, 1e-6, 100)
	y = hy[-1]
	return y
