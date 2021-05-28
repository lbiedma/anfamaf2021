import numpy as np

def intenumcomp(fun,a,b,N,regla):
	if regla == 'trapecio':
		return trapecio(fun,a,b,N)
	elif regla == 'pm':
		return pm(fun,a,b,N)
	elif regla == 'simpson':
		return simpson(fun,a,b,N)
	else:
		print("regla inválida")

def simpson(fun,a,b,N):
	if N%2 != 0:
		print("N debe ser par")
		return None
	h = (b-a)/N
	x = np.linspace(a,b,N+1)
	f = np.array([fun(xi) for xi in x])
	fn = f[-1]
	f = np.reshape(f[:-1],(-1,2))
	f0 = f[0,0]
	f_pares = f[1:,0]
	f_impares = f[:,1]
	I = (h/3)*(f0 + 2*np.sum(f_pares) + 4*np.sum(f_impares) + fn )
	return I
