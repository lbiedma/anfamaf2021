def inewton(x,y,z):
	n = len(y) # cantidad de puntos a interpolar

	matriz_coefs = [[0.0]*m for m in range(n,0,-1)]

	for i in range(n):
		matriz_coefs[i][0] = y[i]

	for j in range(1,n):
		for i in range(0,n-j):
			matriz_coefs[i][j] = (matriz_coefs[i+1][j-1]-matriz_coefs[i][j-1]) / (x[i+j] - x[i])

	coefs = matriz_coefs[0]

	#w = [polinomio(zj) for zj in z]
	w = [horn_newton(zj,x,coefs) for zj in z]
	return w

def horn_newton(zj,x,coefs):
	n = len(coefs)
	valor = coefs[n-1]
	for i in range(n-2,-1,-1):
		valor = coefs[i] + (zj - x[i])*valor
	return valor

# c_0 + c 1 (x − x 0 ) + c 2 (x − x 0 )(x − x 1 ) + · · · + c n (x − x 0 ) . . . (x − x n−1)
# c_0 + (x − x_0 )*c_1 + c 2 (x − x 0 )(x − x 1 ) + · · · + c n (x − x 0 ) . . . (x − x n−1)
# c_0 + (x − x_0)* [c_1 + c 2 (x − x 1 ) + · · · + c n (x − x 1 ) . . . (x − x n−1)]
# c_0 + (x − x_0)* [c_1 + (x − x_1)*c_2 + · · · + c n (x − x 1 ) . . . (x − x n−1)]

# c_0 + (x − x_0)*[c_1 + (x − x_1)*c_2]
