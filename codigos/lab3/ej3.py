from ej2 import inewton
import matplotlib.pyplot as plt

f = lambda x : 1/x

lista_i = list(range(1,6))
lista_f = [f(i) for i in lista_i]

lista_x = [24/25 + j/25 for j in range(1,102)]
f_plot = [f(x) for x in lista_x]

p_plot = inewton(lista_i, lista_f, lista_x)

plt.plot(lista_x, f_plot, label="funcion f")
plt.plot(lista_x, p_plot, label="polinomio interpolante")
plt.grid()
plt.legend()

plt.show()
