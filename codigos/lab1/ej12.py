def SonOrtogonales(x,y):
	# x = [x1, x2]
	# y = [y1, y2]
	tol = 1e-10
	prod_punto = x[0]*y[0] + x[1]*y[1]
	# if prod_punto == 0:
	if abs(prod_punto) < tol :
		return True
