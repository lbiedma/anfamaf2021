from ej1 import simpson

def simpson_simple(fun,a,b):
	return simpson(fun,a,b,2)

def simpson_adap_recursiva(fun,a,b,err):
	c = (a+b)/2
	q = simpson_simple(fun,a,b)
	q1 = simpson_simple(fun,a,c)
	q2 = simpson_simple(fun,c,b)
	if abs(q-q1-q2) < 15*err:
		I = q1 + q2
	else:
		q1 = simpson_adap(fun,a,c,err/2)
		q2 = simpson_adap(fun,c,b,err/2)
		I = q1 + q2
	return I

def simpson_adap(fun,a,b,err):
	q = simpson_simple(fun,a,b)
	stack = [[a,b,q,err]]
	I = 0.
	while stack:
		cur_int = stack.pop(-1)
		cur_a = cur_int[0]
		cur_b = cur_int[1]
		cur_q = cur_int[2]
		cur_err = cur_int[3]
		c = (cur_a + cur_b) / 2
		q1 = simpson_simple(fun,cur_a,c)
		q2 = simpson_simple(fun,c,cur_b)
		if abs(cur_q - q1 - q2) < 15*cur_err:
			I += q1 + q2
		else:
			# partir el intervalo
			# agregar ambas mitades a la pila
			stack.append([cur_a,c,q1,cur_err/2])
			stack.append([c,cur_b,q2,cur_err/2])
	return I

import numpy as np
import time

fun = lambda x : x*np.exp(-x**2)

err = 1e-15

I_exacta = 0.5*(1-np.exp(-1))

start = time.time()

I_recursiva = simpson_adap_recursiva(fun,0,1,err)

print(f"Simpson adaptativo recursivo demoró {time.time()-start} y calculó {I_recursiva}")

start = time.time()

I_no_recursiva = simpson_adap(fun,0,1,err)

print(f"Simpson adaptativo no recursivo demoró {time.time()-start} y calculó {I_no_recursiva}")

cota_d4f = 156

N_simpson = int(np.ceil((cota_d4f/(err*180))**(1/4)))

start = time.time()

I_compuesta = simpson(fun,0,1,N_simpson)

print(f"Simpson compuesta demoró {time.time()-start} y calculó {I_compuesta}")
