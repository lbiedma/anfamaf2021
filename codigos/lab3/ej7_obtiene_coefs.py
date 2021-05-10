from ej1 import ilagrange

def obtiene_coefs(x,y):
	# x = [x1, x2, x3]
	# y = [y1, y2, y3]
	z = [0,1,-1]
	c, ab1, ab2 = ilagrange(x,y,z)
	# ab1 = a+b+c
	ab1 = ab1 - c
	# ab2 = a-b+c
	ab2 = ab2 - c
	a = (ab1+ab2)/2
	b = (ab2-ab1)/2
	return a, b, c
