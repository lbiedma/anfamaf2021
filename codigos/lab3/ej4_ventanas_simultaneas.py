from ej2 import inewton
from math import cos, pi
import matplotlib.pyplot as plt

f = lambda x : 1 / (1 + 25*x**2)

a = -1
b = 1
h = (b-a)/199
x_plot = [-1 + h*i for i in range(200)]

f_plot = [f(x) for x in x_plot]

for n in range(1,16):
	# interpolación de p
	x_inter_p = [2*(i-1)/n -1 for i in range(1,n+2)]
	f_inter_p = [f(x) for x in x_inter_p]
	p_plot = inewton(x_inter_p,f_inter_p,x_plot)
	# interpolación de q
	x_inter_q = [cos(pi*(2*i+1)/(2*n+2)) for i in range(n+1)]
	f_inter_q = [f(x) for x in x_inter_q]
	q_plot = inewton(x_inter_q,f_inter_q,x_plot)
	plt.figure(n)
	plt.plot(x_plot, f_plot)
	plt.plot(x_plot, p_plot)
	plt.plot(x_plot, q_plot)
	plt.grid()

plt.show()

