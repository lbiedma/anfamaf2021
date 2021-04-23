import ej7
import matplotlib.pyplot as plt
import numpy as np

#x = np.linspace(0.0, 1.5, 100)
h = 1.5/99
x = [i*h for i in range(100)]
y_bisec = [ej7.lab2ej7bisec(xi) for xi in x]
y_newton = [ej7.lab2ej7newton(xi) for xi in x]
y_ipf = [ej7.lab2ej7ipf(xi) for xi in x]

fig,ax = plt.subplots(3,1)

ax[0].plot(x,y_bisec)
ax[1].plot(x,y_newton)
ax[2].plot(x,y_ipf)
plt.show()

plt.plot(x,y_ipf,'g')
plt.plot(x,y_bisec,'--r')
plt.plot(x,y_newton,'ob')
plt.show()
